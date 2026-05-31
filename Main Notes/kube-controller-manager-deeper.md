---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kube-controller-manager]]"
sub_concepts:
  - "[[Reconciliation Loop Mechanics]]"
  - "[[Node Eviction Grace Periods]]"
  - "[[HA Leader Election Leases]]"
use_cases:
  - "[[Cascading Deletions]]"
  - "[[Garbage Collection Owner References]]"
external_links:
  - "[Mumshad CKA Course](https://kodekloud.com)"
  - "[Kubernetes Official Docs](https://kubernetes.io/docs/concepts/architecture/controller/)"
tags:
  - kubernetes/deep-dive
---

# kube-controller-manager deeper

**Breadcrumbs:** [[Index|🏠 Index]] > [[kube-controller-manager]] > **deeper dive**

---

This note covers the low-level mechanics of garbage collection, cascading deletions, node eviction parameters, and leader election for the **kube-controller-manager**.

---

## 🗑️ 1. Garbage Collection & Cascading Deletions
The Garbage Collector (GC) tracks relationships between parent and child objects using the `metadata.ownerReferences` field. When a parent object (like a ReplicaSet) is deleted, its children (Pods) must be handled.

### Deletion Policies (CKA Essential)
When deleting resources, you can specify how children are cleaned up:
* **Background Deletion (Default):** Kubernetes deletes the owner object immediately, and the GC automatically deletes the dependents in the background.
  `kubectl delete deployment my-dep --cascade=background`
* **Foreground Deletion:** The owner object transitions to a "deletion in progress" state. The API server deletes all dependents first, and only deletes the owner once all dependents are gone.
  `kubectl delete deployment my-dep --cascade=foreground`
* **Orphan Deletion:** Deletes the owner object but leaves the dependent child pods running. They are orphaned and no longer managed by any controller.
  `kubectl delete deployment my-dep --cascade=orphan`

---

## ⏱️ 2. Node Controller Eviction Timelines
The Node Controller monitors node health via Lease objects. It uses specific timeout flags configured in the controller manager:
* **`--node-monitor-grace-period` (Default: `40s`):** The amount of time the controller manager waits before marking a node as `Unreachable` or `NotReady` in the API server when it stops receiving heartbeats.
* **`--pod-eviction-timeout` (Default: `5m`):** Once a node is marked `NotReady`, this is the grace period the controller manager waits before evicting pods from that node and scheduling replicas elsewhere.

---

## 👑 3. HA Leader Election & Leases
To prevent split-brain conflicts, only one `kube-controller-manager` process can actively modify resources at a time.
* **Mechanism:** When multiple control plane instances are running, they compete to acquire a `Lease` object in the `kube-system` namespace.
* **Active vs. Standby:** The instance that holds the lease becomes the leader and executes the reconciliation loops. The other instances go to sleep and poll the lease. If the leader fails to renew the lease within its TTL, a standby instance acquires the lease and takes over.
* Inspecting leader leases:
  ```bash
  kubectl get lease -n kube-system
  ```

*Read more in [02_cluster_architecture_and_components.md](../Reference%20Notes/02_cluster_architecture_and_components.md#d-kube-controller-manager-the-enforcer) and [04_workload_lifecycle_and_healing.md](../Reference%20Notes/04_workload_lifecycle_and_healing.md#2-garbage-collection-gc).*
