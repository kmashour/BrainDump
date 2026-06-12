---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kube-controller-manager-deeper]]"
sub_type: use-case
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/architecture/garbage-collection/#cascading-deletion"
author: "Kubernetes Documentation"
against: []
tags:
  - kubernetes/controller-manager
  - kubernetes/garbage-collection
---

# kube-controller-manager - Cascading Deletions

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[kube-controller-manager]] > [[kube-controller-manager-deeper]] > **Cascading Deletions**

---

## 📑 1. Concept of Cascading Deletion
When you delete an owner object (like a ReplicaSet or Deployment), you must decide whether to delete its children (dependent Pods) as well. This process is called **Cascading Deletion**.

---

## ⚙️ 2. Cascading Deletion Modes

### A. Foreground Cascading Deletion
In Foreground deletion, the owner object first enters a "deletion in progress" state. The API server then deletes the dependent objects, and only after all dependents are gone does it delete the owner.
* **Trigger Command:**
  ```bash
  kubectl delete deployment nginx --cascade=foreground
  ```

### B. Background Cascading Deletion (Default)
In Background deletion, Kubernetes deletes the owner object immediately. The garbage collector then automatically deletes the orphaned dependents in the background.
* **Trigger Command:**
  ```bash
  kubectl delete deployment nginx --cascade=background
  ```

### C. Orphan Deletion (Bypass)
If you want to keep the dependent Pods running while deleting the owner (e.g. deleting a ReplicaSet but keeping the Pods), orphan them:
* **Trigger Command:**
  ```bash
  kubectl delete deployment nginx --cascade=orphan
  ```

---

## 🔬 3. CKA Debugging Scenario
If a deployment cannot be deleted and stays stuck, inspect finalizers on the object. If finalizers exist, the cascading deletion will block. Remove finalizers using:
```bash
kubectl patch deployment nginx -p '{"metadata":{"finalizers":null}}' --type=merge
```

*Read more in [[Reference Notes/0-2_cluster_architecture_and_components.md#6-the-kubernetes-object-model]]*\n