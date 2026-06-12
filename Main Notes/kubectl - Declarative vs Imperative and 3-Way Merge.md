---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kubectl-deeper]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/"
author: "Kubernetes Authors"
course_title: "CKA Exam Prep"
against: []
tags:
  - kubernetes/cli
  - apiserver/merge
---

# kubectl - Declarative vs Imperative and 3-Way Merge

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[kubectl]] > [[kubectl-deeper]] > **Declarative vs Imperative and 3-Way Merge**

---

## 📑 Declarative vs Imperative Management

Managing cluster resources follows two primary methodologies:
* **Imperative (Commands):** Instructs the cluster via direct CLI verbs (e.g. `kubectl run`, `kubectl scale`). Best for fast operations and dry-run template generation.
* **Declarative (Manifests):** Declares a target final state in a file (`kubectl apply -f`). Recommended for production environments (GitOps, audits, and peer reviews).

---

## ⚙️ The 3-Way Merge Engine

Kubernetes applies declarative changes by performing a **3-way merge** patch:

```text
Local YAML File  ──┐
                   │
Live config (etcd) ┼───> [ 3-Way Merge ] ───> Updated Object
                   │
Last Applied Config│
(metadata annotation)
```

1. **Local File:** The configuration you are applying.
2. **Live Object:** The configuration currently active in cluster memory (`etcd`).
3. **Last Applied Configuration:** A hidden JSON annotation (`kubectl.kubernetes.io/last-applied-configuration`) inside the live object storing a backup of the previous applied manifest.

### Why the Annotation is Required
* **Handling Deletions:** If a label or port is deleted from the local file, comparing it only with the live object does not distinguish between "unmentioned" and "intended to delete". Checking the `last-applied-configuration` shows the field existed previously, indicating it should be deleted.
* **Server-Side Apply (SSA):** In newer clusters, Server-Side Apply (SSA) is the default. It replaces client-side JSON annotations with native server-side field ownership tracking under `metadata.managedFields`, preventing etcd metadata size errors.

---

## ⚠️ The Mixed-Management Warning & 2-Way Merge Fallback

If you create a resource using an imperative command like `kubectl create` (which does not write the `last-applied-configuration` annotation unless run with the `--save-config` flag) and later attempt to update it using `kubectl apply`, you will encounter this warning:
```plaintext
Warning: resource replicasets/my-replicaset is missing the kubectl.kubernetes.io/last-applied-configuration annotation which is required by kubectl apply... The missing annotation will be patched automatically.
```

### The 2-Way Merge Fallback (Blind Spot Mechanics)
When `kubectl apply` does not find the annotation, it cannot perform a 3-way merge. Instead, it falls back to a **2-Way Merge**, comparing only the **Local Configuration** directly against the **Live Object** currently in `etcd`.

This creates a significant operational blind spot:
* **Additions:** If you add a new port, environment variable, or label in your local file, the 2-way merge will successfully add it to the live object.
* **Updates:** If you modify an existing field (e.g., updating an image tag), the 2-way merge will successfully update it.
* **Deletions (Fail):** If you delete a label, volume, or environment variable from your local file, the 2-way merge **will not remove it** from the live object. Because there is no historical `last-applied-configuration` annotation to prove that the field was previously managed by you, Kubernetes assumes you simply chose to omit that field from your local file this time (leaving the live value alone) rather than wanting it destroyed.

### Auto-Recovery & Patching
When this warning is issued, Kubernetes applies your additions and updates using a 2-way merge, but to prevent future blind spots, it automatically generates and injects the `kubectl.kubernetes.io/last-applied-configuration` annotation into the live object based on your current local configuration. Subsequent `kubectl apply` commands on this resource will successfully execute as 3-way merges.

*Read more in [0-12_kubernetes_api_management_and_pod_immutability.md](../Reference%20Notes/0-12_kubernetes_api_management_and_pod_immutability.md#2-the-3-way-merge-engine)*
