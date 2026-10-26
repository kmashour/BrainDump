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
  - kubernetes/security
  - kubernetes/admission-control
  - kubernetes/policy-engines
  - status/completed
---

# Kubernetes Pod Security and Policy Engines - Evolution from PSP to PSA, Gatekeeper, and Kyverno

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Kubernetes Pod Security and Policy Engines]] > **Evolution from PSP to PSA, Gatekeeper, and Kyverno**

---

## 🏛️ The 10-Year Policy Engine Evolution

To understand Kubernetes workload governance without getting lost in disjointed YAML flags, we must view it as an evolutionary timeline of how Kubernetes learned to control what users can deploy:

```
+-----------------------------------------------------------------------------------+
|                        THE 10-YEAR POLICY ENGINE EVOLUTION                        |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  1. THE EARLY DAYS (No Policies)                                                  |
|     - Any developer could create a privileged pod and root the entire cluster.    |
|                                                                                   |
|  2. THE DARK AGES (PodSecurityPolicy / PSP: v1.3 – v1.25) [REMOVED]               |
|     - Complex, confusing, checked the wrong identity, mutated specs silently,    |
|       and enabling it by accident killed the entire cluster instantly.            |
|                                                                                   |
|  3. THE MODERN STANDARD (Pod Security Admission / PSA: v1.25+) [BUILT-IN]         |
|     - Built directly into kube-apiserver.                                         |
|     - No complex objects: Just 3 levels (Privileged, Baseline, Restricted).       |
|     - Enforced simply by adding labels to Namespaces!                             |
|                                                                                   |
|  4. ADVANCED ENTERPRISE (OPA Gatekeeper & Kyverno) [EXTERNAL ADD-ONS]             |
|     - PSA only knows 3 fixed levels. What if you want to ban images from DockerHub|
|       or require every pod to have an `owner: billing` label?                     |
|     - OPA Gatekeeper and Kyverno are full-featured external policy engines.       |
+-----------------------------------------------------------------------------------+
```

---

## 1. The Nightmare of PodSecurityPolicy (PSP) (v1.3 – v1.25)

In Kubernetes versions 1.3 through 1.25, Kubernetes had a built-in feature called **`PodSecurityPolicy` (PSP)**. On paper, it sounded simple: *"Create a policy object that forbids root or privileged containers."*

In practice, it was one of the most hated and dangerous features in Kubernetes history due to three structural flaws:

### 1.1 The Catastrophic "Cluster Murder" Trap
To turn PSP on, administrators added an admission plugin flag to the API Server:
`--enable-admission-plugins=PodSecurityPolicy`.
* If you enabled this flag **before** creating a policy and binding it, **EVERY SINGLE POD CREATION IN THE CLUSTER IMMEDIATELY FAILED**.
* The cluster could not start CoreDNS, it could not start CNI networking, and it could not restart crashing pods. The entire cluster experienced total paralysis instantly.

### 1.2 The Identity Confusion: Who Actually Creates a Pod?
When a developer executes `kubectl apply -f deployment.yaml`:
* **The user** creates the `Deployment`.
* The `Deployment` controller creates a `ReplicaSet`.
* The `ReplicaSet` controller creates the `Pod`!
* **The Problem:** The Pod is NOT created by user `karim`! It is created by a background service account: the **`ServiceAccount`** of that namespace (e.g. `default`).
* In PSP, if you granted the PSP permission to *yourself*, your Deployment still failed because the underlying ServiceAccount didn't have the permission! Administrators had to write Byzantine RBAC `ClusterRoleBindings` linking ServiceAccounts across namespaces using a non-standard pseudo-verb: `verbs: ["use"]` on `podsecuritypolicies`.

### 1.3 The "Alphabetical Order" Mutation Trap
If a user or service account had access to multiple PSPs (e.g., `privileged-psp` and `restricted-psp`):
* How did Kubernetes decide which policy to apply?
* **It sorted the policy names ALPHABETICALLY!**
* If someone created a policy named `01-permissive`, Kubernetes picked it first and silently mutated the pod to be permissive. If someone created `00-super-restricted`, it picked that instead. Renaming a YAML file broke cluster admission behavior!

Because of these design flaws, the Kubernetes community **deprecated PSP in v1.21 and completely removed it in v1.25**.

---

## 2. The Modern Standard: Pod Security Standards (PSS) & Admission (PSA)

When Kubernetes removed PSP, they replaced it with **Pod Security Admission (PSA)**. 

Instead of requiring teams to write custom YAML policy objects and wire them with RBAC, Kubernetes hardcoded three opinionated standards directly into the API Server:

```
+-----------------------------------------------------------------------------------+
|                        PSA: JUST THREE NAMESPACE LABELS                           |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  1. pod-security.kubernetes.io/enforce: restricted                                |
|     --> REJECT any pod that is not fully hardened.                                |
|                                                                                   |
|  2. pod-security.kubernetes.io/warn: restricted                                   |
|     --> ALLOW the pod, but print a yellow WARNING in the developer's terminal.    |
|                                                                                   |
|  3. pod-security.kubernetes.io/audit: restricted                                  |
|     --> ALLOW the pod, but write a security warning to the cluster AUDIT LOG.     |
+-----------------------------------------------------------------------------------+
```

### 2.1 The Three Security Tiers (PSS)
1. **Privileged (Unrestricted):** Completely open. Reserved for CNI, CSI drivers, and node monitors (`privileged: true`, host namespaces, hostPath allowed).
2. **Baseline (Minimally Restrictive):** Prevents known privilege escalation attacks for standard apps. Blocks `privileged: true`, host namespaces, and hostPath, but allows running as root (`UID 0`) and default capabilities.
3. **Restricted (Heavily Hardened / Zero Trust):** Mandates non-root execution (`runAsNonRoot: true`), `allowPrivilegeEscalation: false`, dropping `ALL` capabilities, and `RuntimeDefault` seccomp.

### 2.2 Why Engineers Love PSA
* **Zero policy files to manage:** The standards are built directly into Kubernetes code.
* **Safe, zero-downtime rollouts:** Administrators apply `warn: restricted` on a namespace for two weeks, observe audit logs, remediate pod templates, and only then flip the label to `enforce: restricted`.
* **No cluster outages:** Unlabeled namespaces simply default to `privileged` without breaking control plane components.

---

## 3. Why Do OPA Gatekeeper & Kyverno Exist?

If PSA is so clean, why do enterprise organizations install external policy engines like **OPA Gatekeeper** or **Kyverno**?

Because **PSA only knows about Pod Security**!
PSA is blind to custom business rules, cloud costs, and non-Pod resources.

### What PSA Cannot Do:
1. *"Require every namespace to have an `owner-email` and `billing-id` label."* (PSA only looks at Pods).
2. *"Block anyone from creating a Service of type `LoadBalancer` because cloud IPs cost money."* (PSA does not inspect Services).
3. *"Enforce that all container images MUST come from `mycompany.azurecr.io/*` and ban public Docker Hub."* (PSA does not inspect image registries).
4. *"Automatically inject an environment variable `ENV=production` or an Istio sidecar into every pod."* (PSA does not mutate).

For custom enterprise governance, organizations deploy a **General-Purpose Dynamic Admission Policy Engine**:

```
+-----------------------------------------------------------------------------------+
|                        DYNAMIC ADMISSION POLICY ENGINES                           |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  Kube-APIServer ──► Sends admission webhook JSON ──► [ Policy Engine ]           |
|                                                            │                      |
|                                                            ▼                      |
|                                                    Evaluates Rules:               |
|                                                    - Is image from trusted repo?  |
|                                                    - Does it have cost labels?    |
|                                                    - Is port 80 blocked?          |
|                                                            │                      |
|                                                            ▼                      |
|                     Returns: ALLOW / DENY / MUTATE (Inject configs)               |
+-----------------------------------------------------------------------------------+
```

---

## 4. OPA Gatekeeper vs. Kyverno: The Policy Engine War

Both engines sit as Admission Webhooks validating and mutating resources, but they follow opposing design philosophies:

| Feature | **OPA Gatekeeper** (The Industry Standard) | **Kyverno** (The Kubernetes-Native Alternative) |
| :--- | :--- | :--- |
| **Language** | Uses **Rego** (a specialized declarative query language created for Open Policy Agent). | Uses pure **Kubernetes YAML**! No new programming language required. |
| **Architecture** | 1. Define a `ConstraintTemplate` (the Rego logic).<br>2. Define a `Constraint` (parameters & targets). | You write a single `ClusterPolicy` manifest directly in standard YAML. |
| **Learning Curve** | **High** (learning Rego syntax, set theory, and syntax quirks takes significant ramp-up). | **Very Low** (if you know Kubernetes YAML, you can write Kyverno policies immediately). |
| **Cross-Platform** | Can enforce policies on Kubernetes, Terraform, Linux PAM, Envoy proxies, and microservices. | Kubernetes-only. |
| **Mutation & Generation** | Supports mutation, but primarily famous for validation. | Extremely powerful at auto-generating resources (e.g. *"When a namespace is created, auto-generate a NetworkPolicy"*). |

### Concrete Code Comparison: "Block Images Outside Trusted Registry"

#### In OPA Gatekeeper (Requires Rego code inside ConstraintTemplate):
```rego
package k8strustedimages
violation[{"msg": msg}] {
  image := input.review.object.spec.containers[_].image
  not startswith(image, "mycompany.azurecr.io/")
  msg := sprintf("Image '%v' is not from trusted registry!", [image])
}
```

#### In Kyverno (Pure Kubernetes YAML):
```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: restrict-image-registry
spec:
  validationFailureAction: Enforce
  rules:
  - name: validate-registries
    match:
      resources:
        kinds:
        - Pod
    validate:
      message: "Images must come from mycompany.azurecr.io!"
      pattern:
        spec:
          containers:
          - image: "mycompany.azurecr.io/*"
```

---

## 💡 The Grand Summary Mental Model

```
+-----------------------------------------------------------------------------------+
| 1. PSP (PodSecurityPolicy): The dead, removed ancestor (v1.3–v1.25). Complex      |
|    RBAC bindings, alphabetical mutation traps. GONE.                              |
|                                                                                   |
| 2. PSA (Pod Security Admission): The modern, built-in replacement (v1.25+).      |
|    Zero policy files; enforces Privileged, Baseline, or Restricted via labels.    |
|                                                                                   |
| 3. OPA Gatekeeper & Kyverno: The external superheroes. You install them when you  |
|    need custom enterprise rules (image registries, cost labels, network policies) |
|    that go beyond standard pod security.                                          |
+-----------------------------------------------------------------------------------+
```

---

*Read more in [[Reference Notes/0-7-2_pod_security_standards_and_admission.md#2-historical-architecture-pod-security-policy-psp-v13--v125|Module 0-7-2: Pod Security Standards, PSP & PSA Masterclass]]*
