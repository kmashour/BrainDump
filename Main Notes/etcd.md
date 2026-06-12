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
  - "[[Reference Notes/0-2_cluster_architecture_and_components.md]]"
  - "[[Reference Notes/0-10_maintenance_upgrades_and_etcd.md]]"
tags:
  - kubernetes/component
  - status/completed
against: []

---

# etcd

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Control Plane > **etcd**

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

---

This note covers the low-level consensus rules, CLI management operations, backup/restore procedures, and configuration settings for the **etcd** database.

---

## 👥 1. Raft Consensus & Quorum Calculations
`etcd` uses the Raft protocol to replicate data and elect a leader:
* **Quorum Rule:** A write is only committed once a majority of nodes acknowledge it.
  $$\text{Quorum} = \lfloor \frac{n}{2} \rfloor + 1$$
* **Node Count Strategy:** Always run an odd number of nodes (3, 5, etc.). 
  * Running 3 nodes allows 1 failure ($3 - 2 = 1$).
  * Running 4 nodes still only allows 1 failure ($4 - 3 = 1$), but increases network overhead. Thus, odd numbers maximize resilience relative to host cost.

---

## 🔌 2. Network Ports
* **Port `2379` (Client Communication):** Used by the `kube-apiserver` and `etcdctl` to send state requests and read configurations.
* **Port `2380` (Peer Communication):** Used by `etcd` nodes internally to run the Raft protocol, synchronize state, and elect leaders.

---

## 🛡️ 3. Client Verification & TLS Arguments
Because `etcd` holds sensitive passwords, secrets, and configuration, it uses strict TLS authentication:
To run commands against `etcd` in a default `kubeadm` cluster:
```bash
export ETCDCTL_API=3
etcdctl \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  member list
```

---

## 💾 4. Backup & Restore (CKA Practical Steps)
Creating backups and restoring from them are critical operations for CKA preparation.

### A. Taking a Snapshot (Backup)
```bash
export ETCDCTL_API=3
etcdctl --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  snapshot save /opt/etcd-backup.db
```
Verification command:
```bash
etcdctl --write-out=table snapshot status /opt/etcd-backup.db
```

### B. Restoring a Snapshot
To restore a snapshot, you must create a new data directory to prevent conflicting with the active db:
```bash
export ETCDCTL_API=3
etcdctl snapshot restore /opt/etcd-backup.db \
  --data-dir=/var/lib/etcd-from-backup
```
*Note:* After restoring, you must update the `etcd` configuration (or Static Pod manifest at `/etc/kubernetes/manifests/etcd.yaml`) to point the volume hostPath for `etcd-data` to the new directory (`/var/lib/etcd-from-backup`).

---

## 🔌 5. ETCD API v2 vs. v3 Client Management
The CLI tool `etcdctl` is used to interact with the database. The environment variable `ETCDCTL_API` determines which version of the API `etcdctl` uses. While older systems or default client installations may use API v2, modern Kubernetes clusters utilize API v3.

### Configuring the API Version:
You can switch the active API version for `etcdctl` using one of two methods:
1.  **Prepend the Environment Variable:** Specify the variable on a per-command basis:
    ```bash
    ETCDCTL_API=3 etcdctl version
    ```
2.  **Export for the Shell Session:** Set the variable persistently for your current terminal session:
    ```bash
    export ETCDCTL_API=3
    etcdctl version
    ```

### CLI Command Comparison:
| Operation | API v2 Command (`ETCDCTL_API=2`) | API v3 Command (`ETCDCTL_API=3`) | Notes |
| :--- | :--- | :--- | :--- |
+| **Check Client Version** | `etcdctl --version` (Option flag) | `etcdctl version` (Subcommand) | v3 prints client and API server versions if connected. |
+| **Write/Store Key** | `etcdctl set key1 value1` | `etcdctl put key1 value1` | v2 uses `set`; v3 uses `put` and returns `OK`. |
+| **Read/Retrieve Key** | `etcdctl get key1` | `etcdctl get key1` | v3 output prints both the key name and the value on separate lines. |
+| **Query Key Prefix** | `etcdctl ls` (Lists directory content) | `etcdctl get / --prefix --keys-only` | v3 lacks directories; it uses a flat key-value namespace with prefixes. |
+| **Delete Key** | `etcdctl rm key1` | `etcdctl del key1` | v2 uses `rm`; v3 uses `del`. |
+| **Create Directory** | `etcdctl mkdir dir1` | *N/A* | Not supported in v3 due to flat keyspace model. |
+| **Watch Key Changes** | `etcdctl watch key1` | `etcdctl watch key1` | In v3, watching keys provides detailed transaction events. |

*Read more in [0-10_maintenance_upgrades_and_etcd.md](../Reference%20Notes/0-10_maintenance_upgrades_and_etcd.md#41-etcd-api-v2-vs-v3-client-management)*

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **etcd**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
WHERE class = "deeper-dive" AND contains(parent_concept, this.file.link)
SORT file.name ASC
```
