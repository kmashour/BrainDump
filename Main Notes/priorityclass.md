---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: workload
domains:
  - "kubernetes"
related_concepts:
  - "[[pod]]"
  - "[[kube-scheduler]]"
against: []
reference_guides:
  - "[[Reference Notes/0-13_scheduling_logging_and_lifecycle.md]]"
tags:
  - kubernetes/priorityclass
  - status/completed
---

# priorityclass

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Control Plane > **priorityclass**

---

## 🎯 Purpose (Why it is used)
A `PriorityClass` defines a cluster-scoped mapping between a logical name and a 32-bit integer value. It allows cluster administrators to categorize and prioritize workloads so that critical system components or high-priority applications are guaranteed scheduling and resources over low-priority background jobs.

---

## ⚙️ Functionality (What it is doing)
* **Scheduling Queue Prioritization:** The scheduler sorts pending pods in the scheduling queue based on their numeric priority value, running higher-priority pods first.
* **Preemption Mechanics:** If a high-priority pod is blocked from scheduling due to resource constraints, the scheduler can preempt (evict) running pods of lower priority to free up capacity on a target node.
* **Global Defaulting:** A single `PriorityClass` can be marked as the default for the entire cluster (`globalDefault: true`). Pods that do not specify a `priorityClassName` will receive this default value (otherwise they receive a default priority of `0`).
* **Preemption Control:** The `preemptionPolicy` field determines whether the pod can preempt other pods:
  * `PreemptLowerPriority` (Default): Evicts lower-priority pods.
  * `Never`: Non-preempting; the pod waits in the queue but is prioritized for scheduling when resources naturally free up.

---

## 🏛️ Architectural Context (How it fits in the architecture)
* **Cluster-Scoped Resource:** PriorityClasses are non-namespaced and can be referenced by pods in any namespace.
* **Admission Controller Mutation:** The API server's `Priority` admission controller intercepts pod creation, resolves the referenced `priorityClassName`, and stamps the numeric value into `spec.priority` and `spec.preemptionPolicy` before persistence in `etcd`.
* **System Scopes:** Values above `2,000,000,000` are reserved for system-critical workloads (e.g. `system-cluster-critical` and `system-node-critical` are built-in). User workloads must fall between `-2,000,000,000` and `1,000,000,000`.

---

## 🧩 Problem Solver (What problem it solves)
* **Resource Starvation Prevention:** Solves the risk of batch jobs consuming all cluster CPU/memory, which would block critical API endpoints or user-facing microservices.
* **Deterministic Scheduling under Load:** Provides predictable ordering of placements when multiple applications are scale-out scaling concurrently under heavy cluster traffic.

---

## 🟢 Operational Impact (What will happen with it operating)
* Higher priority workloads are scheduled immediately even if the cluster is at 100% capacity (by evicting lower-priority pods).
* Evicted pods receive a standard `SIGTERM` signal, transition to `Terminating` state, and are rescheduled elsewhere if matching nodes are available.

---

## 🔴 Failure Impact (What will happen without it)
* All user workloads share a default priority of `0`, meaning pod placement ordering is purely FIFO or random, and no preemption occurs under load.
* A cluster running out of resources will keep new critical pods in `Pending` indefinitely even if minor background jobs are running on target nodes.

---

## 🛠️ Configuration Example
```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: high-priority-app
value: 1000000
globalDefault: false
preemptionPolicy: PreemptLowerPriority
description: "Mission-critical applications."
```

To use it in a Pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web-server
spec:
  priorityClassName: high-priority-app
  containers:
  - name: nginx
    image: nginx:alpine
```

---

## 🔍 Deeper Dive Notes
This table displays deeper concept files, scenarios, or configurations related to **priorityclass**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
