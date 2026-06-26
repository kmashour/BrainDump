---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[etcd]]"
sub_type: architecture
source_type: udemy
source_url: "https://kodekloud.com"
author: "Mumshad Mannambeth"
course_title: "Certified Kubernetes Administrator (CKA)"
tags:
  - kubernetes/architecture
  - kubernetes/deep-dive
---

# etcd - Architecture

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[etcd]] > **Architecture**

---

## 🏛️ etcd Role in Kubernetes
`etcd` is the primary database for Kubernetes, serving as the sole persistent backend for the control plane.
* **Registry of Truth:** Every resource created, updated, or deleted (including nodes, pods, replica sets, configurations, secrets, and RBAC roles) must write its state to `etcd`.
* **State Verification:** A change in the cluster is only considered successful once it has been saved in `etcd`.
* **API Server Protection:** To maintain database consistency and secure data access, worker nodes and other control plane services never access `etcd` directly. Only the `kube-apiserver` communicates with `etcd`.

---

## 💾 Storage Model Selection (SQL vs. Document vs. Key-Value)
To understand why `etcd` is suited for Kubernetes, it is helpful to compare relational (SQL), document, and key-value databases:

| Database Type | Schema Constraint | Schema Impact on Changes | Query Complexity | Best Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **Relational (SQL)** | Strict schema (tabular rows & columns) | Affects the entire table structure (results in empty/null cells for irrelevant rows) | Supports complex joins and multi-table queries | Structured data requiring strict relationships |
| **Document Store** | Flexible schema (independent JSON/YAML docs) | Independent changes to individual files do not affect other records | Limited query capabilities (hard to run complex joins) | Semi-structured data requiring independent attributes |
| **Key-Value Store** | No schema (associates a value with a unique key) | Highly flexible (any key can store any data type, string, or document) | Simple key-based lookups (no join support) | Simple, rapid data lookups and high-speed writes |

As a **distributed key-value store**, `etcd` allows Kubernetes to represent cluster state objects cleanly as hierarchical key paths mapped to serialized configurations (JSON/Protobuf documents) with sub-millisecond read/write latency.

---

## 👥 Raft Consensus & High Availability
To prevent data corruption and achieve high availability, multiple instances of `etcd` are run across control plane master nodes.
* **Distributed Quorum:** Raft consensus protocol ensures that a majority (quorum) of etcd nodes must agree on writes.
  $$\text{Quorum} = \left\lfloor \frac{N}{2} \right\rfloor + 1$$
* **Leader Election:** The nodes elect a leader node. If the leader node crashes or becomes unreachable, the peer nodes automatically hold a new election to nominate a new leader.
* **Consensus Performance:** In February 2015, etcd version 2.0 redesigned the Raft consensus algorithm, enabling stable cluster configurations and performance scaling beyond 1,000 writes per second.

---

## 🔌 Port Bindings
`etcd` uses two distinct TCP ports for its communications:
1. **Port `2379` (Client Communication):** Used by clients like the `kube-apiserver` and the `etcdctl` CLI client to query and write cluster states.
2. **Port `2380` (Peer Communication):** Used by `etcd` cluster nodes internally to synchronize state, run the Raft protocol, and conduct leader elections.

---

## 📁 Key Registry Path Layout
In a Kubernetes cluster, `etcd` organizes all stored data under a hierarchical tree starting with the `/registry` prefix:
* **`/registry/minions/`**: Stores information and statuses for all worker nodes (referred to as minions historically).
* **`/registry/pods/<namespace>/<pod-name>`**: Stores configuration specs and statuses for pods.
* **`/registry/replicasets/`**: Stores metadata for replica sets.
* **`/registry/deployments/`**: Stores metadata for deployments.
* **`/registry/secrets/`**: Stores cluster secrets (encrypted or base64 encoded).
* **`/registry/configs/`**: Stores config maps.

*Read more in [[Reference Notes/0-2_cluster_architecture_and_components.md#b-etcd-the-source-of-truth]]*
