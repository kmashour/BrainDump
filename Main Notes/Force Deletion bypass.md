---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kubectl-deeper]]"
sub_type: use-case
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-garbage-collection"
author: "Kubernetes Documentation"
against: []
tags:
  - kubernetes/kubectl
  - kubernetes/troubleshooting
---

# kubectl - Force Deletion bypass

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[kubectl]] > [[kubectl-deeper]] > **Force Deletion Bypass**

---

## 📑 1. Why Deletions Get Stuck
When you request a deletion, objects enter a `Terminating` state. The controller waits for helper resources (like finalizers or Kubelet confirmations) before removing it. If a node is down or finalizers fail, the object gets stuck.

---

## ⚙️ 2. Deletion Bypass Methods

### Method A: Immediate Eviction (Pods only)
Force delete a pod by setting the grace period to `0` and passing `--force`. This deletes the object from the API server without waiting for Kubelet validation:
```bash
kubectl delete pod stuck-pod --grace-period=0 --force
```

### Method B: Removing Finalizers (Any stuck resource)
If a PV, PVC, or Namespace is stuck in `Terminating` indefinitely, it is usually blocked by a finalizer. Remove finalizers using a merge patch:
```bash
# Remove finalizers from Namespace
kubectl patch ns stuck-namespace -p '{"metadata":{"finalizers":null}}' --type=merge

# Remove finalizers from PersistentVolume
kubectl patch pv stuck-pv -p '{"metadata":{"finalizers":null}}' --type=merge
```

---

## ⚠️ 3. Data Risks of Force Deletion
* **Split Brain:** Force deleting a StatefulSet pod while the worker node is still partially running may lead to two pods writing to the same network storage simultaneously, causing data corruption.

*Read more in [[Reference Notes/0-12_kubernetes_api_management_and_pod_immutability.md#4-force-deletion-mechanics-and-recreations]]*\n