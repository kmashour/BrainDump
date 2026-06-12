---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[node-deeper]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/"
author: "Kubernetes Documentation"
tags:
  - kubernetes/node
  - kubernetes/architecture
---

# node - Node Allocatable Math

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[node]] > [[node-deeper]] > **Node Allocatable Math**

---

## 📑 1. The Allocatable Formula
To protect OS background tasks and critical Kubernetes agent daemons from resource starvation, Kubernetes reserves a slice of the host's physical capacity. The resource capacity actually available to schedule user Pods is called **Allocatable**:

$$\text{Allocatable} = \text{Capacity} - \text{Kube-Reserved} - \text{System-Reserved} - \text{Hard-Eviction-Thresholds}$$

---

## ⚙️ 2. Resource Allocation Breakdown

```text
+--------------------------------------------------------+
|                      Node Capacity                     |
+-------------------+-----------------+------------------+
|   Kube-Reserved   | System-Reserved | Eviction-Limit   |
| (kubelet, CRI...) | (sshd, udev...) | (hard threshold) |
+-------------------+-----------------+------------------+
|                                                        |
|                    Node Allocatable                    |
|                (Available for user Pods)               |
|                                                        |
+--------------------------------------------------------+
```

### A. Kube-Reserved
Reserves CPU, memory, and disk space for core Kubernetes components (`kubelet`, `kube-proxy`, and container runtime).

### B. System-Reserved
Reserves resources for host operating system processes (such as `systemd`, `journald`, `sshd`, and graphical drivers).

### C. Hard-Eviction-Thresholds
Reserves a safety margin (e.g., `memory.available<100Mi`) to allow the kubelet to evict pods before the node crashes.

---

## 🔬 3. Config Example in Kubelet
These values are set inside `/var/lib/kubelet/config.yaml`:
```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
enforceNodeAllocatable:
- pods
- system-reserved
- kube-reserved
kubeReserved:
  cpu: "500m"
  memory: "500Mi"
systemReserved:
  cpu: "200m"
  memory: "250Mi"
evictionHard:
  memory.available: "100Mi"
  nodefs.available: "10%"
```

*Read more in [[Reference Notes/0-3_node_mechanics_and_resource_limits.md#3-resource-allocation-math-and-limits]]*\n