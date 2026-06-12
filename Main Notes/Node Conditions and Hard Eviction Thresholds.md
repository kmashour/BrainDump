---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kubelet-deeper]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/"
author: "Kubernetes Documentation"
tags:
  - kubernetes/kubelet
  - kubernetes/eviction
---

# kubelet - Node Conditions and Hard Eviction Thresholds

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[kubelet]] > [[kubelet-deeper]] > **Eviction Thresholds**

---

## 📑 1. Kubelet Node-Pressure Eviction
When a node runs out of physical resources (memory, disk, pid), the Kubelet starts evicting Pods to reclaim resources and prevent host-level system instability.

---

## ⚙️ 2. Hard Eviction Thresholds
If resources drop below these limits, the Kubelet evicts Pods immediately **without any grace period**:
* `memory.available < 100Mi`
* `nodefs.available < 10%` (node root filesystem)
* `imagefs.available < 15%` (container runtime image cache)
* `pid.available < 10%`

### Configuration Spec in Kubelet
These values reside in `/var/lib/kubelet/config.yaml`:
```yaml
evictionHard:
  memory.available: "100Mi"
  nodefs.available: "10%"
  nodefs.inodesFree: "5%"
```

---

## 🔬 3. Pod Reclaim and Eviction Order
If a hard eviction threshold is breached, the Kubelet attempts to reclaim resources in this order:
1. **Garbage Collection:** Deletes unused container images and dead containers.
2. **Evict BestEffort:** Evicts BestEffort pods first.
3. **Evict Burstable:** Evicts Burstable pods whose resource usage exceeds their CPU/Memory requests.
4. **Evict Guaranteed:** Evicts Guaranteed pods last, if no other options exist.

*Read more in [[Reference Notes/0-3_node_mechanics_and_resource_limits.md#3-resource-allocation-math-and-limits]]*\n