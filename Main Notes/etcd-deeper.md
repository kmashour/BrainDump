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
use_cases:
  - "[[etcd Backup and Restore]]"
external_links:
  - "[Mumshad CKA Course](https://kodekloud.com)"
  - "[etcd official website](https://etcd.io)"
tags:
  - kubernetes/deep-dive
---

# etcd deeper

**Breadcrumbs:** [[Index|🏠 Index]] > [[etcd]] > **deeper dive**

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

*Read more in [02_cluster_architecture_and_components.md](../Reference%20Notes/02_cluster_architecture_and_components.md#b-etcd-the-source-of-truth).*
