---
obsidianUIMode: preview
class: landing-note
tier: main-note
domains:
  - "kubernetes"
role: workload
related_concepts:
  - "[[kubelet]]"
  - "[[kube-proxy]]"
  - "[[pod]]"
reference_guides:
  - "[[Reference Notes/03_node_mechanics_and_resource_limits.md]]"
tags:
  - kubernetes/infrastructure
  - status/completed
against: []
---

# node

**Breadcrumbs:** [[Index|🏠 Index]] > Workloads & Infrastructure > **node**

---

## 🎯 Purpose (Why it is used)
A `Node` represents a physical or virtual machine in the Kubernetes cluster. It provides the raw compute power (CPU, memory, storage, and network interfaces) needed to run application containers, serving as the worker machine that executes workloads assigned by the Control Plane.

---

## ⚙️ Functionality (What it is doing)
1. **Host Orchestration:** Executes node-level agents (`kubelet`, `kube-proxy`, and container runtime) directly on the host OS.
2. **Resource Reporting:** Continually reports its compute capacity, allocatable resources, and system metadata to the API Server.
3. **Container Isolation:** Implements kernel-level resource limits (cgroups) and security walls (namespaces) to isolate container processes.
4. **Heartbeat Broadcast:** Updates the Control Plane on node health and availability using lightweight Lease heartbeats.
5. **Workload Hosting:** Runs the Pod sandboxes and containers assigned to it by the scheduler.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Nodes form the execution plane (Worker Nodes) of the cluster:
* **Separation of Concerns:** While Control Plane nodes run the cluster's "brains" (`apiserver`, `scheduler`), Worker Nodes represent the "muscle," executing user workloads.
* **Control Boundary:** The node receives instructions from the control plane exclusively via the `kubelet` daemon, which registers the host node in the cluster database.

---

## 🧩 Problem Solver (What problem it solves)
* **Infrastructure Abstraction:** Merges multiple independent physical or cloud servers into a single, cohesive pool of compute capacity. Users deploy workloads to the cluster, not to specific hostnames.
* **Resource Partitioning:** Reserves critical CPU and memory margins for OS operations and Kubernetes daemons, preventing user workloads from overloading the server and causing kernel panics.

---

## 🟢 Operational Impact (What will happen with it operating)
* **Pod Execution:** The cluster can schedule and execute applications.
* **Scheduling Decisiveness:** The scheduler knows which nodes have the capacity and match labels to accept workloads.
* **Self-Healing Mechanics:** If a node's health deteriorates, the control plane detects it and migrates workloads to healthy nodes automatically.

---

## 🔴 Failure Impact (What will happen without it)
* **Zero Compute Capacity:** If no nodes are operating, workloads cannot run.
* **Pending States:** Newly created Pods hang in `Pending` because no worker node is available to accept them.
* **Eviction Outages:** If a running node crashes, its workloads fail. The Control Plane will attempt to recreate them, but if no other healthy nodes exist, the workloads will remain offline.
* **Split Brain & Frozen State:** If a node suffers a network partition, the control plane marks it `NotReady` but cannot terminate its processes, potentially leading to volume conflicts if the node is still running workloads locally.
---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **node**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[node]]
SORT file.name ASC
```
