---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Kubernetes Pod Security and Policy Engines]]"
sub_type: architecture
source_type: gemini-chat
author: "Antigravity"
course_title: "CKS Masterclass"
tags:
  - kubernetes/admission-control
  - kubernetes/api-server
  - kubernetes/security
  - status/completed
---

# Kubernetes Admission Control - Request Lifecycle, Mutating and Validating Architecture

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Kubernetes Pod Security and Policy Engines]] > **Admission Request Lifecycle & Architecture**

---

## 🏛️ The Admission Request Lifecycle: The Complete Pipeline

When a client executes `kubectl apply -f manifest.yaml`, the resource must navigate through a strict, multi-stage pipeline inside the `kube-apiserver` before any data can be committed to the `etcd` datastore.

> [!IMPORTANT]
> **Read Operations Bypass Admission Control:**
> The entire admission control pipeline is only evaluated for **write/mutation verbs** (`CREATE`, `UPDATE`, `DELETE`, `CONNECT`). Read operations (`GET`, `LIST`, `WATCH`) bypass admission control completely and return directly after authentication and authorization.

```
[ Incoming kubectl / Client Request ]
                  │
                  ▼
[ 1. Authentication (AuthN) ] ──────► "Who are you?" (X.509 client cert, bearer token, OIDC)
                  │
                  ▼
[ 2. Authorization (AuthZ/RBAC) ] ──► "Do you have permission to perform this verb on this resource?"
                  │
                  ▼
═════════════════════════════════════════════════════════════════════════════════════════
                         THE ADMISSION CONTROL PIPELINE
═════════════════════════════════════════════════════════════════════════════════════════
                  │
                  ▼
[ PHASE 1: MUTATING ADMISSION ] ────► "The Editor / Auto-Injector"
  - Can MODIFY, INJECT, or DEFAULT the incoming object YAML.
  - Executed sequentially.
  - Built-in plugins (e.g. DefaultStorageClass, AlwaysPullImages).
  - External webhooks (MutatingAdmissionWebhook -> Istio sidecars, Kyverno mutate).
                  │
                  ▼
[ OPENAPI SCHEMA VALIDATION ] ──────► "Is the resulting YAML syntactically and structurally valid?"
                  │
                  ▼
[ PHASE 2: VALIDATING ADMISSION ] ──► "The Final Judge (Allow or Deny)"
  - Strictly READ-ONLY inspection; CANNOT alter object fields.
  - Inspects the FINAL mutated object.
  - Executed in parallel.
  - Returns a binary decision: YES (Admit) or NO (HTTP 403 Forbidden with error reason).
  - Built-in plugins (PodSecurity/PSA, NodeRestriction).
  - External webhooks (ValidatingAdmissionWebhook -> OPA Gatekeeper, Kyverno validate).
═════════════════════════════════════════════════════════════════════════════════════════
                  │
                  ▼
          [ etcd Database ] ────────► Persisted to cluster state!
```

---

## 1. Why Two Phases? (Why Mutate First, Then Validate?)

Kubernetes strictly enforces **Mutating Phase -> Schema Validation -> Validating Phase**. 

### The Security Flaw of the Inverse Order
If Kubernetes ran validation *before* mutation:
1. A developer submits a secure, unprivileged pod manifest.
2. The validating engine inspects it and says: *"Approved! Complies with all policies."*
3. A mutating plugin or webhook executes *afterward* and injects a root volume, privileged flag, or sidecar with elevated capabilities.
4. The newly dangerous pod would get saved directly to `etcd` without ever being inspected again!

**By placing Validation strictly after Mutation**, the Validating controllers inspect the **finished, final product** in its exact final form right before it touches the disk.

---

## 2. In-Tree (Built-In) vs. Out-of-Tree (Dynamic Webhooks)

Admission controllers exist in two distinct deployment patterns:

```
+-----------------------------------------------------------------------------------+
|                        BUILT-IN (IN-TREE) vs. WEBHOOK (OUT-OF-TREE)               |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  1. IN-TREE (Built-In Plugins)                                                    |
|     - Code compiled directly into the `kube-apiserver` Go binary.                 |
|     - Enabled via: `kube-apiserver --enable-admission-plugins=PluginA,PluginB`   |
|     - Fast, memory-local execution inside the API server process.                 |
|     - Examples: `NodeRestriction`, `PodSecurity`, `DefaultStorageClass`.          |
|                                                                                   |
|  2. OUT-OF-TREE (Dynamic Admission Webhooks)                                      |
|     - The API server cannot know every enterprise's custom business rules.        |
|     - Kubernetes provides two built-in "Doorman" gateway plugins:                 |
|         a) `MutatingAdmissionWebhook`                                             |
|         b) `ValidatingAdmissionWebhook`                                           |
|     - When active, these doormen serialize the YAML into an `AdmissionReview`     |
|       JSON payload, make an HTTPS POST call to an external web server, and wait   |
|       for an approval, rejection, or JSON Patch!                                  |
|     - Examples of External Webhooks: OPA Gatekeeper, Kyverno, Istio injector.     |
+-----------------------------------------------------------------------------------+
```

---

## 3. Comprehensive Plugin Classification Matrix

Admission plugins fall into three distinct functional categories based on whether they mutate, validate, or perform both actions:

| Admission Plugin / Tool | Deployment Type | Phase Executed | Exact Functional Behavior |
| :--- | :--- | :---: | :--- |
| **`DefaultStorageClass`** | Built-in (In-Tree) | **Mutating Only** | If a PVC omits `spec.storageClassName`, this plugin injects the name of the cluster default StorageClass. |
| **`AlwaysPullImages`** | Built-in (In-Tree) | **Mutating Only** | Modifies every incoming container specification to force `imagePullPolicy: Always` (prevents node cache poisoning). |
| **`NodeRestriction`** | Built-in (In-Tree) | **Validating Only** | Restricts Kubelets so they can only modify their own `Node` and `Pod` APIs. Blocks worker nodes from modifying other nodes. |
| **`ImagePolicyWebhook`** | Built-in (In-Tree) | **Validating Only** | Calls an external scanner backend (e.g. Trivy) over HTTPS to verify container image vulnerability status before admission. |
| **`PodSecurity` (PSA)** | Built-in (In-Tree) | **Validating Only** | Evaluates Pods against `Privileged`, `Baseline`, or `Restricted` standards via namespace labels. Strictly approves or denies. |
| **`ServiceAccount`** | Built-in (In-Tree) | **BOTH** | **Mutates:** Injects default ServiceAccount token volume if omitted.<br>**Validates:** Rejects the pod if the referenced ServiceAccount does not exist. |
| **`LimitRanger`** | Built-in (In-Tree) | **BOTH** | **Mutates:** Injects default CPU/RAM requests/limits if omitted.<br>**Validates:** Rejects pods whose resources exceed namespace `LimitRange` constraints. |
| **`PodSecurityPolicy` (PSP)** *(Legacy)* | Built-in (In-Tree) | **BOTH** | **Mutated:** Injected capabilities and user IDs based on alphabetical policy names.<br>**Validated:** Rejected non-compliant pods. *(Removed in v1.25)*. |
| **`MutatingAdmissionWebhook`** | Built-in Gateway | **Mutating Only** | Forwards admission requests to external mutation servers (e.g. Istio sidecar injection, Kyverno mutating rules). |
| **`ValidatingAdmissionWebhook`** | Built-in Gateway | **Validating Only** | Forwards admission requests to external policy engines (e.g. **OPA Gatekeeper**, Kyverno validation rules). |

---

## 4. Real Manifest: `ValidatingWebhookConfiguration`

Below is a production-ready manifest used to wire an external policy engine (such as OPA Gatekeeper) into the API Server:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  name: "pod-policy-validator"
webhooks:
  - name: "validate.security.company.com"
    admissionReviewVersions: ["v1"]
    sideEffects: None
    timeoutSeconds: 5

    # 1. Connection Target & TLS Trust
    clientConfig:
      service:
        name: "gatekeeper-webhook-service"
        namespace: "gatekeeper-system"
        path: "/v1/admit"
        port: 8443
      # Base64-encoded CA certificate that signed the webhook server's TLS certificate
      caBundle: "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCg=="

    # 2. Interception Scope
    rules:
      - operations: ["CREATE", "UPDATE"]
        apiGroups: [""]
        apiVersions: ["v1"]
        resources: ["pods"]
        scope: "Namespaced"

    # 3. Fail-Closed Security Policy
    # - Fail: If the webhook server is down or unreachable, REJECT the pod creation (Zero-Trust).
    # - Ignore: If the webhook server is down, ALLOW the pod creation anyway (Permissive).
    failurePolicy: Fail

    # 4. Mandatory Exemption Filter (Prevents Webhook Deadlock)
    namespaceSelector:
      matchExpressions:
        - key: kubernetes.io/metadata.name
          operator: NotIn
          values: ["kube-system", "gatekeeper-system"]
```

---

## 5. Real Manifest: `MutatingWebhookConfiguration`

Below is a production-ready mutating webhook configuration used to auto-inject sidecars or apply default security contexts:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingWebhookConfiguration
metadata:
  name: "security-sidecar-injector"
webhooks:
  - name: "inject.security.company.com"
    admissionReviewVersions: ["v1"]
    sideEffects: None
    timeoutSeconds: 5
    clientConfig:
      service:
        name: "sidecar-injector-service"
        namespace: "security-tools"
        path: "/mutate-pods"
        port: 443
      caBundle: "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCg=="
    rules:
      - operations: ["CREATE"]
        apiGroups: [""]
        apiVersions: ["v1"]
        resources: ["pods"]
    failurePolicy: Fail
    # Opt-in strategy: only mutate namespaces tagged with injection label
    namespaceSelector:
      matchLabels:
        security-injection: enabled
```

*Related Reference Module:* [[Reference Notes/0-16_admission_controllers.md|Module 0-16: Kubernetes Admission Controllers & Webhooks]]
