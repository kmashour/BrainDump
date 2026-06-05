---
obsidianUIMode: preview
class: landing-note
tier: main-note
domains:
  - "kubernetes"
role: control-plane
related_concepts:
  - "[[kube-apiserver]]"
reference_guides:
  - "[[Reference Notes/02_cluster_architecture_and_components.md]]"
  - "[[Reference Notes/11_maintenance_upgrades_and_etcd.md]]"
tags:
  - kubernetes/component
  - status/completed
against: []
---

# etcd

**Breadcrumbs:** [[Index|🏠 Index]] > Control Plane > **etcd**

---

## 🎯 Purpose (Why it is used)
`etcd` is a distributed, consistent key-value store that serves as the single source of truth for the entire Kubernetes cluster. It persists all cluster state, configuration details, and run-time statuses, ensuring that the cluster can recover from control plane component failures without data loss.

---

## ⚙️ Functionality (What it is doing)
1. **Key-Value Persistence:** Stores all Kubernetes objects (Pods, Deployments, Secrets, CRDs) as hierarchical, structured values under key prefixes (e.g., `/registry/pods/`).
2. **Consensus Coordination:** Uses the **Raft consensus protocol** to replicate state updates reliably across multiple database nodes, preventing split-brain conditions.
3. **Concurrency Control:** Employs Optimistic Concurrency Control (via resource versions) to prevent overlapping writes or updates from different clients.
4. **Lease Mechanism:** Employs temporary leases to support TTL (Time to Live) keys, which are used to monitor node health and handle control plane leader elections.

---

## 🏛️ Architectural Context (How it fits in the architecture)
`etcd` sits at the bottom layer of the Control Plane:
* **The API Server Shield:** Only the `kube-apiserver` can connect to and query `etcd`. All other control plane components (`kube-scheduler`, `kube-controller-manager`, etc.) interact with the cluster state by querying the API server, which acts as a database proxy and validation layer.
* **Multi-Master HA:** In high-availability configurations, an odd number of `etcd` members (e.g., 3 or 5) form a cluster to maintain consensus.

---

## 🧩 Problem Solver (What problem it solves)
* **State Synchronization:** In a large distributed system, keeping state synchronized across many nodes is notoriously difficult. `etcd` provides strict serializability of transactions.
* **Brain Split Prevention:** If master nodes lose network connection to one another, Raft ensures that only the majority partition (quorum) can accept writes, keeping the cluster state unified.
* **Failure Recovery:** By persisting state externally from transient container processes, any control plane node can crash and reboot without the cluster losing its configuration or active workload definitions.

---

## 🟢 Operational Impact (What will happen with it operating)
* **Consistent Scheduling & Routing:** The cluster knows exactly what resources exist and where they are running.
* **State Recovery:** If a control plane node crashes, it simply starts up again, reconnects to `etcd`, reads the stored state, and resumes management without interrupting running applications.
* **Zero-Downtime Control Plane:** In an HA cluster, if one `etcd` node crashes, the database continues processing reads and writes without interruption as long as a quorum (e.g., 2 out of 3 nodes) is maintained.

---

## 🔴 Failure Impact (What will happen without it)
* **Immediate Control Plane Crash:** The `kube-apiserver` will immediately fail to respond to read/write requests, reporting errors or refusing connections.
* **Management Freeze:** No new workloads can be deployed, scaled, deleted, or upgraded. `kubectl` is completely disabled.
* **Loss of Telemetry:** The cluster cannot detect node crashes, apply self-healing policies, or reschedule pods.
* **Complete Data Loss Risk:** If all `etcd` instances fail and no backup exists, the cluster's entire state (all resources, configuration, and security settings) is lost, requiring a complete redeployment of the cluster.
---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **etcd**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[etcd]]
SORT file.name ASC
```
