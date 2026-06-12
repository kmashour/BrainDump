---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kube-scheduler]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/"
author: "Kubernetes Authors"
course_title: "Kubernetes Scheduling Concepts"
tags:
  - kubernetes/scheduler
  - kubernetes/deep-dive
---

# kube-scheduler - Priority Preemption and Topology Spread

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[kube-scheduler]] > **Priority Preemption and Topology Spread**

---

## 📑 Advanced Scheduling and Placement Control

Kubernetes supports granular scheduling control through topology distribution constraints, scheduling readiness gates, pluggable framework extensions, pod priorities, and node eviction mechanisms.

### 1. Topology Spread Constraints
**Topology Spread Constraints** allow cluster administrators to spread Pods evenly across failure domains (zones, regions, hostnames) to enforce high availability:
*   `maxSkew`: The maximum allowed imbalance in Pod counts between domains.
*   `whenUnsatisfiable`: Set to `DoNotSchedule` (stay Pending if skew cannot be satisfied) or `ScheduleAnyway` (schedule but prefer minimum skew).

### 2. Pod Scheduling Readiness (Scheduling Gates)
A Pod can be created in a "parked" state by specifying `spec.schedulingGates`:
*   The scheduler ignores the Pod entirely, avoiding CPU cycles until the gates are removed.
*   An external controller or operator verifies prerequisites (e.g. storage pre-provisioning) and removes the gate, letting the Pod enter the scheduler's queue.

### 3. Pluggable Scheduling Framework
The `kube-scheduler` divides pod scheduling into two cycles:
*   **Scheduling Cycle (Synchronous):** Evaluates nodes via plugins registered at extension hooks:
    *   `QueueSort`: Orders the queue.
    *   `PreFilter` / `Filter`: Evaluates feasibility (replaces legacy Predicates).
    *   `PreScore` / `Score`: Ranks matching nodes (replaces legacy Priority functions).
*   **Binding Cycle (Asynchronous):** Applies the node binding decision (`Reserve`, `Permit`, `PreBind`, `Bind`, `PostBind`).

### 4. Pod Priority & Preemption
*   **`PriorityClass`:** Defines a cluster-scoped integer priority (higher = more important).
*   **Preemption:** If a high-priority Pod is blocked due to lack of resources, the scheduler will preempt (evict) lower-priority Pods on a target node to reclaim space and schedule the high-priority workload.

### 5. Node-Pressure Eviction Signals & Thresholds
*   **Node-pressure Eviction:** Proactively triggered by the `kubelet` when node thresholds (OOM, disk full) are reached. Bypasses PDBs and changes the Pod phase to `Failed`.
*   **Eviction Signals:** Monitors `memory.available`, `nodefs.available`, `nodefs.inodesFree`, `imagefs.available`, `imagefs.inodesFree`, `containerfs.available`, `containerfs.inodesFree`, and `pid.available`.
*   **Hard vs Soft Eviction:** Hard eviction has a `0s` grace period and immediately terminates pods, ignoring PDBs and container settings. Soft eviction uses grace periods defined by `--eviction-soft-grace-period` and respects `--eviction-max-pod-grace-period`.

### 6. NodeResourcesFit Bin-Packing Strategies
The `NodeResourcesFit` score plugin supports bin-packing:
*   **`MostAllocated`:** Packs pods by preferring nodes with higher resource utilization, optimizing node scale-down.
*   **`RequestedToCapacityRatio`:** Assigns custom scores to nodes based on resource utilization shapes (defined in KubeSchedulerConfiguration).

### 7. PodGroup Co-Scheduling & Topology-Aware Workload Scheduling (TAS)
*   **PodGroup Co-Scheduling (v1.35+ Alpha):** Atomic scheduling for batch workloads (e.g. ML training). Pods in a PodGroup are scheduled simultaneously. If the minimum required pods cannot fit, no pods are bound (avoiding partial-allocation resource deadlocks).
*   **Topology-Aware Workload Scheduling (v1.36+ Alpha):** Placements are evaluated collectively to schedule all Pods in a `PodGroup` within the same topology zone using `TopologyPlacement`, `NodeResourcesFit`, and `PodGroupPodsCount` placement plugins.

### 8. Node Declared Features (KEP-5328)
*   Reports enabled features via `Node.status.declaredFeatures`.
*   The `NodeDeclaredFeatures` scheduler plugin filters out nodes lacking features required by the Pod, preventing scheduling skew in mixed-version clusters.

*Read more in [0-13_scheduling_logging_and_lifecycle.md](../Reference%20Notes/0-13_scheduling_logging_and_lifecycle.md#5-advanced-scheduling--eviction-control)*
