---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[finalizer]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/"
author: "Kubernetes Documentation"
course_title: "Kubernetes Concepts Overview"
tags:
  - kubernetes/finalizer
  - kubernetes/deep-dive
---

# finalizer - Owners and BlockOwnerDeletion

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[finalizer]] > **Owners and BlockOwnerDeletion**

---

## 📑 Owner References and Dependent Relationships

In Kubernetes, some resources own others (e.g. a ReplicaSet owns Pods).
* **`ownerReferences`:** Dependent objects contain a list of owners in `metadata.ownerReferences` containing the owner's `apiVersion`, `kind`, `name`, and `uid`.
* **Cross-Namespace Rule:** Cross-namespace owner references are strictly disallowed by design. A namespaced dependent must reside in the same namespace as its owner. If an invalid cross-namespace reference is configured, Kubernetes ignores it and triggers a warning event:
  * **Event Reason:** `OwnerRefInvalidNamespace`
  * **Troubleshooting Command:**
    ```bash
    kubectl get events -A --field-selector=reason=OwnerRefInvalidNamespace
    ```

---

## ⚠️ Cascading Deletion & finalizers

When an owner resource is deleted, you can specify how its dependents are handled:

### 1. Foreground Cascading Deletion
Kubernetes adds the `foregroundDeletion` finalizer to the owner object.
* **Flow:** The owner remains in a `Terminating` state, and the controller deletes all dependents that have `ownerReferences.blockOwnerDeletion=true`. Once all blocked dependents are deleted, the owner finalizer is removed and the owner itself is deleted.

### 2. Orphan Cascading Deletion
Kubernetes adds the `orphan` finalizer to the owner object.
* **Flow:** The owner is deleted immediately, leaving all dependent objects running in the cluster. The garbage collector removes the owner reference from each dependent, rendering them orphans.

*Read more in [02_cluster_architecture_and_components.md](../Reference%20Notes/02_cluster_architecture_and_components.md#6-core-kubernetes-object-model-and-metadata)*
