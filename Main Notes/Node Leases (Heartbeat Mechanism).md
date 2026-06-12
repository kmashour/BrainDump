---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[node-deeper]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/architecture/nodes/#heartbeats"
author: "Kubernetes Documentation"
tags:
  - kubernetes/node
  - kubernetes/architecture
---

# node - Node Leases (Heartbeat Mechanism)

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[node]] > [[node-deeper]] > **Node Leases**

---

## 📑 1. Why Leases Exist (Scalability)
Historically, the Kubelet updated its Node object status directly to report health every 10 seconds. In large clusters with hundreds of nodes, this caused huge write pressures on `etcd` since the Node object contains extensive metadata (addresses, capacity, conditions, images).

Starting in v1.13, Kubernetes introduced **Leases** to solve this.

---

## ⚙️ 2. How the Lease Heartbeat Works
* **轻量级 Heartbeat:** Every 10 seconds, the Kubelet updates its corresponding `Lease` object in the `kube-node-lease` namespace.
* **Update Interval:** If the lease object is renewed on time, the node is considered healthy.
* **Node Status Updates:** The full, bulky `Node` object status is now only updated when a node condition actually changes, or every 5 minutes (default `node-status-update-frequency` sync fallback).

---

## 🔬 3. Inspecting Leases
List all node lease objects:
```bash
kubectl get leases -n kube-node-lease
```
Output:
```text
NAME         HOLDER       SPEC.LEASEDURATIONSECONDS   AGE
worker-1     worker-1     40                          15d
worker-2     worker-2     40                          15d
```
The lease duration specifies the timeout (default `40s`) before the lease expires, marking the node unhealthy.

*Read more in [[Reference Notes/0-3_node_mechanics_and_resource_limits.md#1-node-bootstrapping-and-kubelet-self-registration]]*\n