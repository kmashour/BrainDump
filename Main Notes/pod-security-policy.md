---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: control-plane
domains:
  - "kubernetes"
related_concepts:
  - "[[pod]]"
  - "[[pod-security-admission]]"
  - "[[rbac]]"
  - "[[admission-controller]]"
against:
  - "[[pod-security-admission]]"
reference_guides:
  - "[[Reference Notes/0-7-2_pod_security_standards_and_admission.md]]"
tags:
  - kubernetes/security
  - kubernetes/psp
  - status/completed
---

# Pod Security Policy

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > control-plane > **Pod Security Policy**

---

## 🎯 Purpose (Why it is used)
**Pod Security Policy (PSP)** was the original native cluster-level resource (in `policy/v1beta1`) and admission controller designed to enforce security constraints on Pod specifications before they are admitted into the cluster. It prevented unprivileged users from deploying privileged containers, mounting host paths, or escalating root privileges.

---

## ⚙️ Functionality (What it is doing)
*   **Admission Validation:** Intercepts Pod creation and update API requests to verify compliance against configured security parameters (`spec.privileged`, `runAsUser`, `capabilities`, `volumes`, `hostNetwork`).
*   **Admission Mutation:** Injects default values into Pod specifications (such as adding default capabilities or enforcing non-root UIDs) during admission.
*   **RBAC Authorization Binding:** Requires callers (or the Pod's ServiceAccount) to have the `use` verb on the specific `PodSecurityPolicy` resource via RoleBindings.

---

## 🏛️ Architectural Context (How it fits in the architecture)
*   **Kube-Apiserver Plugin:** Operated as an in-tree admission controller plugin enabled via `--enable-admission-plugins=PodSecurityPolicy`.
*   **Controller Manager Delegation:** When workloads are managed by Deployments, the `kube-controller-manager` creates Pods using the workload's `ServiceAccount`, meaning the ServiceAccount identity (rather than the deploying human user) was evaluated against PSP RBAC bindings.
*   **Evolutionary Replacement:** Deprecated in Kubernetes v1.21 and removed in v1.25, superseded by **[[pod-security-admission|Pod Security Admission (PSA)]]** and the **Pod Security Standards (PSS)** under KEP-2579.

---

## 🧩 Problem Solver (What problem it solves)
Without PSP, any user authorized to create Pods in any namespace could deploy a container with `privileged: true` and `hostPath: /`, granting them full root access over the host node. PSP solved this by validating Pod configurations against an administrator-defined security baseline.

---

## 🟢 Operational Impact (What will happen with it operating)
*   **Enforced Least Privilege:** Disallows unsafe configurations like host network sharing, root execution, and arbitrary volume mounts.
*   **Deterministic Failure:** Rejects non-compliant pods with explicit admission error messages.

---

## 🔴 Failure Impact (What will happen without it / Flaws)
*   **Cluster Lockout Trap:** Enabling the PSP admission plugin without pre-defined policies and RBAC bindings instantly blocked all pod creations across the entire cluster.
*   **Indirect Delegation Failures:** Workloads deployed via Deployments silently failed if the Pod's ServiceAccount lacked the `use` verb on the PSP.
*   **Silent Mutation Drift:** Automatic mutation modified Pod specs behind the scenes, creating divergence from committed GitOps manifests.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Pod Security Policy**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
