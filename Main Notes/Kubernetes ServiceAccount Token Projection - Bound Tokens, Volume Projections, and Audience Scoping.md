---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Kubernetes ServiceAccounts and Workload Identity]]"
sub_type: mechanics
source_type: gemini-chat
author: "Antigravity Assistant"
course_title: "CKS Real Exam Blueprint & Identity Hardening"
tags:
  - kubernetes/security
  - kubernetes/service-account
  - kubernetes/projected-volumes
  - kubernetes/workload-identity
  - kubernetes/cks
  - kubernetes/deep-dive
---

# Kubernetes ServiceAccount Token Projection - Bound Tokens, Volume Projections, and Audience Scoping

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Kubernetes ServiceAccounts and Workload Identity]] > **ServiceAccount Token Projection - Bound Tokens, Volume Projections, and Audience Scoping**

---

## 🎯 1. The Architectural Shift: Legacy Tokens vs. Bound Projected Tokens

### The Legacy Vulnerability (Pre-v1.22)
Historically, Kubernetes automatically generated a static Secret of type `kubernetes.io/service-account-token` for every ServiceAccount.
* **No Expiration Date:** These tokens remained valid indefinitely until the ServiceAccount was deleted.
* **No Audience Restriction:** A single token could authenticate against the Kubernetes API Server, internal metrics endpoints, or any third-party service validating Kubernetes JWTs.
* **Default Auto-Mount:** Every Pod automatically had this infinite token injected into `/var/run/secrets/kubernetes.io/serviceaccount/token`.

```
[ Attacker Compromises Web Pod (RCE) ]
                 │
                 ▼ (cat /var/run/secrets/kubernetes.io/serviceaccount/token)
      [ Steals Plaintext JWT Token ]
                 │
                 ▼ (No expiration! Valid forever! No audience check!)
      [ Attacker queries kube-apiserver from external laptop indefinitely ]
```

### The Modern Defense: Bound ServiceAccount Token Volume (KEP-1205)
Modern Kubernetes decouples ServiceAccounts from static Secrets. Instead, tokens are:
1. **Time-Bound:** Enforced via `expirationSeconds` (e.g., 10 minutes to 1 hour).
2. **Audience-Bound:** Scoped via `audience` (e.g., restricted to HashiCorp Vault or Cloud IAM).
3. **Pod-Bound:** Cryptographically tied to the lifetime and UID of the specific Pod requesting it.
4. **Delivered via Projected Volumes:** Mounted on demand without persisting as a Kubernetes Secret.

---

## 🧭 2. Core Architectural Question: What is the Purpose of a ServiceAccount with NO Mounted Token?

Why assign a ServiceAccount to a Pod if `automountServiceAccountToken: false` is configured and no credentials exist inside the container?

A ServiceAccount represents the **Control Plane Identity** of the workload, independent of whether the container filesystem contains a token:

### 1. Control Plane Governance & Admission Control (PSA, OPA Gatekeeper, Kyverno)
Admission webhooks and policy controllers evaluate `spec.serviceAccountName` at Pod creation time before the container runtime is ever invoked:
* *Example Policy:* "Only workloads running under `serviceAccountName: secure-db-operator` are permitted to mount hostPath volumes or claim specific PVC storage tiers."
* The container code never needs to authenticate with the API Server; the identity is checked strictly by the API Server's admission phase.

### 2. Cloud Workload Identity Federation (AWS IRSA, GCP Workload Identity, Azure AD)
In production cloud environments, containerized applications rarely query the Kubernetes API; they interact with cloud infrastructure (e.g., AWS S3, GCP BigQuery, Azure Key Vault).
* The ServiceAccount is annotated with a Cloud IAM Role:
  ```yaml
  metadata:
    annotations:
      eks.amazonaws.com/role-arn: arn:aws:iam::123456789:role/AppS3Access
  ```
* The cloud provider's OIDC engine verifies the Pod's identity token via the cluster's public OIDC discovery endpoint (`/.well-known/openid-configuration`).
* The application gains cloud access without needing a cluster-admin Kubernetes token mounted on disk.

### 3. Absolute Least Privilege for Standard Workloads (90%+ of Pods)
Standard applications (e.g., Nginx web servers, Redis caches, Python APIs) never need to run `kubectl` commands. 
* If a zero-day Remote Code Execution (RCE) occurs, an attacker inspecting `/var/run/secrets/` finds nothing.
* The workload maintains an administrative identity in Kubernetes audits without exposing an attack surface.

### 4. Controlled, Scoped Token Injection (Least-Privilege Mounting)
Disabling default auto-mounting gives the cluster administrator total control over:
* **Which container** inside a multi-container Pod gets the token.
* **Where** the token is mounted on disk.
* **How long** the token remains valid.

---

## 📦 3. What is a Projected Volume?

In standard Kubernetes, a volume typically represents a **single source of data**:
* A `secret` volume mounts keys from one Secret.
* A `configMap` volume mounts keys from one ConfigMap.
* A `downwardAPI` volume mounts Pod runtime metadata.

### The Optical Projector Metaphor
A **Projected Volume** functions like an optical projector: it combines multiple independent data sources (Secrets, ConfigMaps, DownwardAPI metadata, and dynamically minted ServiceAccountTokens) and projects them all into **one single directory** inside the container.

```
+-----------------------------------------------------------+
|                   PROJECTED VOLUME SOURCES                |
|                                                           |
|  [ Source 1: secret ]          (e.g., db-password)        |
|  [ Source 2: configMap ]       (e.g., app-settings.json)  |
|  [ Source 3: downwardAPI ]     (e.g., pod-ip, pod-name)   |
|  [ Source 4: serviceAccountToken ] (e.g., 1-hour JWT)     |
+-----------------------------------------------------------+
                             │
                             ▼ (Projected into ONE mount directory)
+-----------------------------------------------------------+
| Container Mount Path: /var/run/secrets/tokens             |
|                                                           |
|  ├── db-password                                          |
|  ├── app-settings.json                                    |
|  ├── pod-ip                                               |
|  └── token  <── Dynamically refreshed by Kubelet!         |
+-----------------------------------------------------------+
```

### The Kubernetes Schema Rule for Tokens
In the Kubernetes storage schema, **there is no standalone `serviceAccountToken` volume type**. You cannot write `volumes[].serviceAccountToken`. To mount a dynamically minted, short-lived token, it **must** be declared as a source inside a `projected` volume.

### Kubelet's Background Token Rotation
When a `serviceAccountToken` is projected:
1. Kubelet requests the token from `kube-apiserver` via the `TokenRequest` API with the specified `expirationSeconds`.
2. Kubelet writes the token to the projected mount path.
3. Kubelet monitors the expiration window. When the token reaches approximately **80% of its lifetime**, Kubelet automatically requests a refreshed token and overwrites the file on disk.
4. **No pod restart is required**; the container process simply reads the updated token from disk.

---

## 🔬 4. Concrete Real-World Examples

### Example 1: The Unified Configuration Directory
Merges a Secret, a ConfigMap, and the Downward API into a single `/etc/app/config/` path:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: unified-app
spec:
  containers:
  - name: web
    image: busybox:1.36
    command: ["sleep", "3600"]
    volumeMounts:
    - name: unified-config-volume
      mountPath: /etc/app/config
      readOnly: true
  volumes:
  - name: unified-config-volume
    projected:
      sources:
      - secret:
          name: db-creds
          items:
          - key: password
            path: db-password.txt
      - configMap:
          name: app-config
          items:
          - key: log_level
            path: settings.json
      - downwardAPI:
          items:
          - path: my-pod-ip.txt
            fieldRef:
              fieldPath: status.podIP
```

**Result on container filesystem (`ls -la /etc/app/config`):**
```text
/etc/app/config/
├── db-password.txt      <-- Sourced from Secret db-creds
├── settings.json        <-- Sourced from ConfigMap app-config
└── my-pod-ip.txt        <-- Sourced from Downward API (e.g. 10.244.1.42)
```

---

### Example 2: Audience-Bound Token for External Services (HashiCorp Vault)
Ensures a token minted for HashiCorp Vault cannot be replayed against the Kubernetes API Server:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: vault-client-pod
spec:
  serviceAccountName: vault-auth-sa
  automountServiceAccountToken: false
  containers:
  - name: app
    image: alpine:latest
    command: ["sleep", "3600"]
    volumeMounts:
    - name: vault-token-vol
      mountPath: /var/run/secrets/vault
      readOnly: true
  volumes:
  - name: vault-token-vol
    projected:
      sources:
      - serviceAccountToken:
          audience: "https://vault.internal.company.com"   # Restricted strictly to Vault
          expirationSeconds: 1200                          # 20-minute lifetime
          path: vault-jwt
```

**Security Failure Loop:** If an attacker steals this token and queries `https://kube-apiserver:6443/api/v1/secrets`, the API Server immediately returns `401 Unauthorized`:
`"token audience does not match any of the allowed audiences for the Kubernetes API Server"`.

---

### Example 3: Zero-Trust Multi-Container Pod (Sidecar Isolation)
A public web app runs alongside an internal metrics sidecar. Only the trusted sidecar receives API credentials:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secured-sidecar-pod
spec:
  serviceAccountName: metrics-sa
  automountServiceAccountToken: false    # Block auto-mount for all containers

  containers:
  # Container 1: Vulnerable public app -> ZERO ACCESS TO TOKENS
  - name: legacy-php-app
    image: php:8.1-apache
    # NO volumeMounts!

  # Container 2: Internal trusted agent -> EXPLICIT PROJECTED MOUNT
  - name: sidecar-agent
    image: curlimages/curl:latest
    command: ["sleep", "3600"]
    volumeMounts:
    - name: api-token-volume
      mountPath: /var/run/secrets/tokens
      readOnly: true

  volumes:
  - name: api-token-volume
    projected:
      sources:
      - serviceAccountToken:
          expirationSeconds: 3600
          path: token
```

---

## ⚙️ 5. The Two-Tier Disabling Hierarchy & Exam Rules

Auto-mount suppression must be evaluated at two distinct levels:

```
+-------------------------------------------------------------------------------+
| LEVEL 1: ServiceAccount Level                                                 |
| automountServiceAccountToken: false                                           |
| (Defines default behavior for pods referencing this SA)                       |
+-------------------------------------------------------------------------------+
                                      │
                                      ▼ Overridden by
+-------------------------------------------------------------------------------+
| LEVEL 2: Pod / Deployment Level                                               |
| spec.template.spec.automountServiceAccountToken: false                        |
| (Explicit per-pod override; ALWAYS takes precedence over the SA level)        |
+-------------------------------------------------------------------------------+
```

> [!IMPORTANT]
> **The Precedence Rule:** Pod-level `automountServiceAccountToken` overrides the ServiceAccount-level setting. If an SA sets `false` but a Pod sets `true`, the token will be mounted. In real CKS exam scenarios, **always configure `false` at both levels** to ensure full compliance.

---

## 🎯 6. Real Exam Question 09 Blueprint & Verification

### Problem Statement
In namespace `automation`, disable automatic token mounting on ServiceAccount `bot-sa` and Deployment `bot-worker`. Manually project an audience-bound token with `expirationSeconds: 3600` into the container at mount path `/var/run/secrets/tokens` (`readOnly: true`).

### The 10-Second Exam Docs Navigation
1. Open `https://kubernetes.io/docs/`.
2. Search: **`projected volume serviceaccounttoken`**.
3. Copy the canonical YAML block from the **Projected Volumes** documentation.

### Terminal Verification Commands
```bash
# 1. Identify running pod
POD=$(kubectl get pod -n automation -l app=bot-worker -o jsonpath='{.items[0].metadata.name}')

# 2. Negative Verification: Confirm default path is ABSENT (Returns "No such file or directory")
kubectl exec -n automation $POD -- ls -la /var/run/secrets/kubernetes.io/serviceaccount

# 3. Positive Verification: Confirm projected path exists and is populated
kubectl exec -n automation $POD -- ls -la /var/run/secrets/tokens

# 4. Inspect JWT Token Payload (Check expiration timestamp)
kubectl exec -n automation $POD -- cat /var/run/secrets/tokens/token
```

---

## 🧠 7. First-Principles Clarifications: Storage, RAM, and Modern Auto-Rotation

### A. The Token Storage Paradox: Where Does the Token Actually Live?
When a token is projected via `serviceAccountToken`:
1. **Control Plane (`etcd`): Zero Bytes Stored!**
   - Unlike legacy static secrets (`kubernetes.io/service-account-token`), Bound Tokens are **never written to etcd**.
   - Kubelet calls the API Server's `TokenRequest` API on the fly. The API server mints and signs a dynamic JWT using `/etc/kubernetes/pki/sa.key` and immediately hands it to Kubelet.
2. **Worker Node Host: RAM Only via `tmpfs`!**
   - Kubelet writes the token to an in-memory `tmpfs` volume located at:
     `/var/lib/kubelet/pods/<pod-uid>/volumes/kubernetes.io~projected/<volume-name>/`
   - It **never touches the physical disk or SSD** of the worker node. If the node reboots or the pod dies, the RAM is cleared instantly.
3. **Inside the Container: Path Concatenation**
   - The final file path is the exact concatenation of `mountPath` and `path`:
     `mountPath: /var/run/secrets/tokens` + `path: token` = **`/var/run/secrets/tokens/token`**.

### B. Modern Kubernetes Auto-Rotation vs. Why Manual Projection is Still Essential
* **Does Modern Kubernetes Already Rotate Automounted Tokens?**
  **YES!** Since Kubernetes 1.22 (GA), the `BoundServiceAccountTokenVolume` feature is enabled by default. Even default automounted tokens are bound tokens backed by `tmpfs` and automatically rotated by Kubelet at ~80% of their TTL.
* **Why Then Must We Still Manually Project Tokens & Disable Auto-Mount?**
  1. **Attack Surface Elimination (`automountServiceAccountToken: false`):** 90%+ of workloads (Nginx, Redis, Python APIs) never communicate with the API Server. Leaving any valid token inside the pod gives an RCE/SSRF attacker an active credential to query cluster RBAC.
  2. **Audience Scoping (`audience:` claim):** Default automounted tokens are valid against the Kubernetes API Server (`https://kubernetes.default.svc`). Projected tokens can be scoped strictly to external services (e.g. `audience: "https://vault.internal.corp"`). If stolen, the Kubernetes API Server rejects the token with `401 Unauthorized: token audience invalid`.
  3. **Custom Expiration Durations:** Allows shrinking token lifetime from the default 1 hour down to minutes for hyper-sensitive microservices.
