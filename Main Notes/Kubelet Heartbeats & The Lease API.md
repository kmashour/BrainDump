---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kubelet-deeper]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/architecture/nodes/#heartbeats"
author: "Kubernetes Documentation"
against: []
tags:
  - kubernetes/kubelet
  - kubernetes/architecture
---

# kubelet - Kubelet Heartbeats & The Lease API

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[kubelet]] > [[kubelet-deeper]] > **Kubelet Heartbeats**

---

## 📑 1. Heartbeat Reporting Mechanisms
The Kubelet reports node health to the API Server using two methods:
1. **Lease API (Heartbeat):** A lightweight `Lease` object in the `kube-node-lease` namespace. Updated every 10 seconds (default).
2. **Node Status:** The complete `Node` object. Updated only when conditions change or every 5 minutes (fallback check).

---

## ⚙️ 2. Lifecycle Timing Parameters
The Control Plane uses these parameters to monitor health:
* **Lease Duration:** Default `40` seconds. If the lease is not renewed within 40 seconds, the node is marked unhealthy.
* **Lease Sync Interval:** Kubelet updates the lease every 10 seconds. If updates fail (network partition), the master node controller waits for the grace period to expire before marking it `NotReady`.

---

## 🔬 3. CKA Troubleshooting Check
To check active leases in a cluster:
```bash
kubectl get lease -n kube-node-lease
```
If a lease has a high renewal offset, the Kubelet on that node is likely failing or unreachable.

*Read more in [[Reference Notes/0-3_node_mechanics_and_resource_limits.md#1-node-bootstrapping-and-kubelet-self-registration]]*\n