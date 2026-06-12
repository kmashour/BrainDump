---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[node]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/architecture/nodes/#condition"
author: "Kubernetes Documentation"
tags:
  - kubernetes/node
  - kubernetes/architecture
---

# node - Node Conditions & Lifecycle

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[node]] > **Node Conditions**

---

## 📑 1. Core Node Conditions
The health of a Node is reported via specific conditions in its status. You can check these by running `kubectl describe node <node-name>`.

| Condition | Description | Healthy State |
| :--- | :--- | :--- |
| **`Ready`** | Node is healthy and ready to accept Pods. | `True` |
| **`DiskPressure`** | Free disk space on the node is running low. | `False` |
| **`MemoryPressure`** | Host memory is running low (triggering eviction threshold). | `False` |
| **`PIDPressure`** | Too many active processes on the host. | `False` |
| **`NetworkUnavailable`** | Routing or CNI config is misconfigured. | `False` |

---

## ⚙️ 2. Transition and Eviction Triggering
When a condition changes to an unhealthy state (e.g. `MemoryPressure: True`):
1. **Eviction Assessment:** Kubelet stops scheduling new Pods on the node.
2. **QoS Evictions:** Kubelet starts evicting existing Pods (starting with `BestEffort` and then `Burstable` that exceed requests) to free up memory before kernel OOM-killer triggers.

---

## 🔬 3. CKA Troubleshooting Commands
If a node status shows `NotReady`, execute these checks directly on the worker node:
```bash
# 1. Check Kubelet Service
systemctl status kubelet

# 2. Check logs for warnings/pressures
journalctl -u kubelet -n 100 -f

# 3. Check container runtime logs
journalctl -u containerd -n 100
```

*Read more in [[Reference Notes/0-3_node_mechanics_and_resource_limits.md#2-node-status-and-conditions]]*\n