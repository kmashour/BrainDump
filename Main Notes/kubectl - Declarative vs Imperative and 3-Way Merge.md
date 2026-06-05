---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kubectl]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/"
author: "Kubernetes Authors"
course_title: "CKA Exam Prep"
tags:
  - kubernetes/cli
  - apiserver/merge
---

# kubectl - Declarative vs Imperative and 3-Way Merge

**Breadcrumbs:** [[Index|🏠 Index]] > [[kubectl]] > **Declarative vs Imperative and 3-Way Merge**

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

*Read more in [13_kubernetes_api_management_and_pod_immutability.md](../Reference%20Notes/13_kubernetes_api_management_and_pod_immutability.md#2-the-3-way-merge-engine)*
