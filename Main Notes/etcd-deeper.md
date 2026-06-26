---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[etcd]]"
sub_concepts:
  - "[[Raft Consensus]]"
  - "[[Raft Quorum Rules]]"
  - "[[etcd network ports]]"
  - "[[etcd TLS certificate configurations]]"
  - "[[etcd - Architecture]]"
  - "[[etcd - Commands]]"
use_cases:
  - "[[etcd Backup and Restore]]"
external_links:
  - "[Mumshad CKA Course](https://kodekloud.com)"
  - "[etcd official website](https://etcd.io)"
sub_type: core-concept
source_type: udemy
against: []
tags:
  - kubernetes/deep-dive
---
# etcd deeper

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[etcd]] > **deeper dive**

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

## 🔍 Sub-Concepts & Use Cases
This table automatically displays all deeper notes, use cases, and configurations associated with **etcd-deeper**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
