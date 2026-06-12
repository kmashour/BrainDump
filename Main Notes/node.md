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
  - "[[Reference Notes/0-3_node_mechanics_and_resource_limits.md]]"
tags:
  - kubernetes/infrastructure
  - status/completed
against: []

---

# node

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Workloads & Infrastructure > **node**

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

---

This note covers the low-level mechanics of node registration, conditions, resource allocation math, lease configurations, and cgroup drivers.

---

## 🚪 1. Node Registration Pathway
A Node joins the cluster through one of two methods:
1. **Self-Registration (Default):** The Kubelet on the host node is launched with `--register-node=true`. It contacts the API Server, submits its capacity and details, and creates its own Node object.
2. **Manual Creation:** An administrator manually creates a Node YAML object:
   ```yaml
   apiVersion: v1
   kind: Node
   metadata:
     name: manual-node-1
   ```
   The Kubelet on that host must match `name` and wait for the object before it can register and run workloads.

---

## 🩺 2. Node Conditions & Lifecycle
The Control Plane tracks node health via specific Boolean flags under `status.conditions`:
* **`Ready`:** `True` if the node is healthy and prepared to accept Pods. `False` or `Unknown` if unhealthy.
* **`DiskPressure`:** `True` if the host's root disk space or container image cache filesystem is almost full.
* **`MemoryPressure`:** `True` if the host's physical RAM is running dangerously low.
* **`PIDPressure`:** `True` if there are too many active processes on the host.
* **`NetworkUnavailable`:** `True` if the node's network routing is misconfigured or the CNI is down.

---

## 🧮 3. Node Allocatable Math
A node's physical capacity is not fully available to run user Pods. Kubernetes calculates **Allocatable** resources using this formula:

$$\text{Allocatable} = \text{Capacity} - \text{Kube-Reserved} - \text{System-Reserved} - \text{Hard-Eviction-Thresholds}$$

* **`Capacity`:** Total hardware resources (CPU, Memory, Disk) detected on the machine.
* **`Kube-Reserved`:** Resources reserved for Kubernetes system components (`kubelet`, `kube-proxy`, container runtime).
* **`System-Reserved`:** Resources reserved for OS background daemons (e.g., `sshd`, `udev`, `systemd`).
* **`Hard-Eviction-Thresholds`:** Memory and Disk reserves held back by the kubelet (e.g., 100Mi memory) to trigger evictions before node crashes occur.

---

## 📑 4. Node Leases (Heartbeat Mechanism)
Rather than writing the bulky Node status object to `etcd` every 10 seconds, the Kubelet updates a lightweight `Lease` object:
* **Namespace:** `kube-node-lease`
* **Duration:** 10 seconds.
* **Benefit:** Reduces database writing pressure on the Control Plane by over 90%, particularly in large clusters, as full status objects are only updated when conditions change or every 5 minutes.

---

## 🧬 5. Cgroups (v1 vs. v2)
Control Groups (`cgroups`) are the Linux kernel feature used to limit container resource usage:
* **cgroups v1:** Divided resources (CPU, Memory, I/O) into separate, independent controller trees. Allowed processes to belong to different resource groups.
* **cgroups v2:** Unified resources under a single hierarchical tree, resolving synchronization issues (e.g., page cache writebacks and memory limits).
* **Driver Alignment:** Always ensure that the Container Runtime and the Kubelet use the same driver (`systemd` is recommended on modern OSs). A mismatch causes duplicate hierarchies and node crashes under load.

*Read more in [0-3_node_mechanics_and_resource_limits.md](../Reference%20Notes/0-3_node_mechanics_and_resource_limits.md#2-node-status-and-conditions).*

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **node**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
