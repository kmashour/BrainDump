---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[storageclass]]"
sub_type: pitfall
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/storage/storage-classes/#volume-binding-mode"
author: "Kubernetes Documentation"
course_title: "Kubernetes Storage Concepts"
tags:
  - kubernetes/storageclass
  - kubernetes/deep-dive
  - kubernetes/scheduling
---

# storageclass - Volume Binding Modes and Scheduling Traps

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[storageclass]] > **Volume Binding Modes and Scheduling Traps**

---

## 📑 Volume Binding Modes and Scheduling Traps

The `volumeBindingMode` field in a `StorageClass` controls when volume provisioning and binding occur. Configuring this field incorrectly for node-locked storage (like local disks) triggers scheduling deadlocks.

### 1. The Immediate Binding Trap
By default, the volume binding mode is `Immediate`.
* **Behavior:** As soon as a `PersistentVolumeClaim` is created, Kubernetes immediately binds it to a matching `PersistentVolume` (or triggers dynamic provisioning of a backing disk).
* **The Pitfall:** This binding happens **before** the Pod requesting the PVC is evaluated by the Scheduler. The volume may end up bound to a PV located on `Node A`. If the Scheduler subsequently processes the Pod and determines it can only run on `Node B` (due to cpu/memory exhaustion, taints, or node selectors on Node A), the Pod is stuck in a `Pending` state forever.

### 2. The Solution: `WaitForFirstConsumer`
Setting `volumeBindingMode: WaitForFirstConsumer` delays the binding and provisioning of a PersistentVolume until a Pod using the PersistentVolumeClaim is scheduled.
* **Topology-Aware Scheduling:** This allows the Scheduler to first select an eligible node for the Pod by evaluating all resource limits, affinities, and tolerations.
* **Coordinated Binding:** Once the target node is chosen, the volume controller binds the PVC to a PV physically matching that node (or triggers dynamic provisioning within the node's availability zone).

*Read more in [0-8-a_local_storage_models_and_scheduling_traps.md](../Reference%20Notes/0-8-a_local_storage_models_and_scheduling_traps.md#3-deep-intuition-aarf-breakdowns)*
