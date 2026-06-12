---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[node]]"
sub_concepts:
  - "[[Node Registration Pathway]]"
  - "[[Node Conditions & Lifecycle]]"
  - "[[Node Allocatable Math]]"
  - "[[Node Leases (Heartbeat Mechanism)]]"
  - "[[cgroups v1 vs v2]]"
use_cases:
  - "[[Configuring kube-reserved and system-reserved limits]]"
external_links:
  - "[Mumshad CKA Course](https://kodekloud.com)"
  - "[Kubernetes Official Docs](https://kubernetes.io/docs/concepts/architecture/nodes/)"
sub_type: core-concept
source_type: udemy
tags:
  - kubernetes/deep-dive
---
# node deeper

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[node]] > **deeper dive**

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

## 🔍 Sub-Concepts & Use Cases
This table automatically displays all deeper notes, use cases, and configurations associated with **node-deeper**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
WHERE class = "deeper-dive" AND contains(parent_concept, this.file.link)
SORT file.name ASC
```
