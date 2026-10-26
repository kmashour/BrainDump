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
  - kubernetes/pod-security-standards
  - kubernetes/psa
  - kubernetes/security
  - status/completed
---

# Kubernetes Pod Security Admission - Tri-Mode Enforcement, Tiers, and Namespace Labels

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Kubernetes Pod Security and Policy Engines]] > **PSA Tri-Mode Enforcement & Namespace Labels**

---

## 🛡️ The Architecture of Pod Security Admission (PSA)

Built natively into `kube-apiserver` (v1.25+), **Pod Security Admission (PSA)** replaces the legacy `PodSecurityPolicy` (PSP) engine. Instead of managing complex CRDs or RBAC bindings, PSA evaluates Pod specifications against three standardized policy levels using **declarative namespace labels**.

```
+-----------------------------------------------------------------------------------+
|                           THE 3 TIERS (What to Check)                             |
+-----------------------------------------------------------------------------------+
| 1. PRIVILEGED  ──► Total access. Allows root, hostPath, privileged: true.         |
| 2. BASELINE    ──► Blocks host breakouts. Forbids privileged: true & hostPath.   |
| 3. RESTRICTED  ──► Zero-trust. Non-root only, drop ALL capabilities, ro-rootfs.   |
+-----------------------------------------------------------------------------------+

                                    COMBINED WITH

+-----------------------------------------------------------------------------------+
|                           THE 3 MODES (What Action to Take)                       |
+-----------------------------------------------------------------------------------+
| A. ENFORCE     ──► The Police. REJECTS and BLOCKS the request (HTTP 403).        |
| B. WARN        ──► The Advisor. ALLOWS the pod, but prints a WARNING in terminal. |
| C. AUDIT       ──► The Camera. ALLOWS the pod, but writes an alert in AUDIT LOG.  |
+-----------------------------------------------------------------------------------+
```

---

## 1. The Namespace Label Syntax

PSA configuration is controlled entirely through namespace labels following this schema:

```
pod-security.kubernetes.io/<MODE>: <TIER>
pod-security.kubernetes.io/<MODE>-version: <VERSION>
```

* **Valid Modes:** `enforce`, `warn`, `audit`
* **Valid Tiers:** `privileged`, `baseline`, `restricted`
* **Valid Versions:** `latest`, `v1.30`, `v1.32`

---

## 2. Real-World Practical Scenarios & Terminal Behavior

### Scenario A: Zero-Downtime Migration (`enforce: baseline`, `warn: restricted`, `audit: restricted`)
This is the gold standard for migrating live enterprise environments. It blocks critical host-takeover vectors immediately (`baseline`), while giving application developers clear feedback on how to achieve full hardening (`restricted`) without causing outages.

#### Apply the Labels:
```bash
kubectl label ns production \
  pod-security.kubernetes.io/enforce=baseline \
  pod-security.kubernetes.io/warn=restricted \
  pod-security.kubernetes.io/audit=restricted
```

#### What Happens When Submitting a Standard NGINX Pod (Meets Baseline, Fails Restricted):
```bash
kubectl apply -f nginx-legacy.yaml -n production
```

#### Exact Terminal Output:
```console
Warning: would violate PodSecurity "restricted:latest": 
- allowPrivilegeEscalation != false (container "nginx" must set securityContext.allowPrivilegeEscalation=false)
- unrestricted capabilities (container "nginx" must set securityContext.capabilities.drop=["ALL"])
- runAsNonRoot != true (pod or container "nginx" must set securityContext.runAsNonRoot=true)
- seccompProfile (pod or container "nginx" must set securityContext.seccompProfile.type to "RuntimeDefault" or "Localhost")

pod/nginx-legacy created  <-- ✅ THE POD IS CREATED! (Because enforce is only baseline!)
```

* **Outcome:** The pod runs cleanly in production.
* **Developer Feedback:** The developer sees a detailed checklist of exact YAML fields to harden.
* **Security Telemetry:** An audit event is recorded in `/var/log/kubernetes/audit/audit.log` for SIEM tracking.

---

### Scenario B: Hardened Production / Financial Namespace (`enforce: restricted`)
In zero-trust or compliance-governed environments (e.g. PCI-DSS, banking), workloads must be fully hardened before admission.

#### Apply the Label:
```bash
kubectl label ns banking \
  pod-security.kubernetes.io/enforce=restricted \
  pod-security.kubernetes.io/enforce-version=latest
```

#### What Happens When Submitting the Same Legacy NGINX Pod:
```bash
kubectl apply -f nginx-legacy.yaml -n banking
```

#### Exact Terminal Output:
```console
Error from server (Forbidden): pods "nginx-legacy" is forbidden: 
violates PodSecurity "restricted:latest": 
- allowPrivilegeEscalation != false (container "nginx" must set securityContext.allowPrivilegeEscalation=false)
- unrestricted capabilities (container "nginx" must set securityContext.capabilities.drop=["ALL"])
- runAsNonRoot != true (pod or container "nginx" must set securityContext.runAsNonRoot=true)
- seccompProfile (pod or container "nginx" must set securityContext.seccompProfile.type to "RuntimeDefault" or "Localhost")
```

* **Outcome:** ❌ **BLOCKED!** The API server returns HTTP 403. The pod is never scheduled.

---

### Scenario C: System Infrastructure Namespace (`enforce: privileged`)
System daemons (CNI plugins like Flannel/Calico, CSI drivers, and node diagnostic tools) require raw host access.

#### Apply the Label:
```bash
kubectl label ns kube-system \
  pod-security.kubernetes.io/enforce=privileged \
  pod-security.kubernetes.io/enforce-version=latest
```

* **Outcome:** Pods requesting `privileged: true`, `hostNetwork: true`, and `hostPath` are admitted without restrictions.

---

## 3. The 3x3 Evaluation Matrix

| Label Combination | Policy Level Tested | What Happens to the Workload | Real-World Use Case |
| :--- | :--- | :--- | :--- |
| **`enforce: privileged`** | `privileged` | Allows all configurations (`privileged: true`, `hostPath`). | `kube-system`, CNI, CSI storage plugins. |
| **`enforce: baseline`** | `baseline` | Rejects `privileged: true` and `hostPath`. Allows running as root. | General dev/staging environments. |
| **`enforce: restricted`** | `restricted` | Rejects anything not fully hardened (must drop `ALL`, non-root, seccomp). | Production, banking, PCI-DSS compliance. *(CKS Question 12)*. |
| **`warn: baseline`** | `baseline` | Warns if pod tries to use `privileged: true` or `hostPath`. | Monitoring permissive legacy clusters. |
| **`warn: restricted`** | `restricted` | Warns if pod is not hardened, but lets it run anyway. | Developer feedback loop before hardening. |
| **`audit: baseline`** | `baseline` | Writes audit log if pod violates baseline standards. | Security team compliance tracking. |
| **`audit: restricted`** | `restricted` | Writes audit log if pod violates restricted standards. | Enterprise SIEM compliance audits. |

---

## 4. ⚡ CKS Exam Speed Hacks

In the CKS exam, never write YAML files to configure PSA. Use direct imperative CLI commands:

```bash
# 1. Enforce Restricted on a namespace (CKS Question 12):
kubectl label --overwrite ns production pod-security.kubernetes.io/enforce=restricted

# 2. View all PSA labels on a namespace:
kubectl get ns production -o yaml | grep pod-security

# 3. Debugging ReplicaSet Rejections in a Restricted Namespace:
# When a Deployment shows 0/1 ready pods, inspect the ReplicaSet events:
kubectl describe rs -n production <replicaset-name>
# The 'Events' block will display the exact PSS violation strings!
```

*Related Reference Module:* [[Reference Notes/0-7-2_pod_security_standards_and_admission.md|Module 0-7-2: Pod Security Standards, PSP & PSA Masterclass]]
