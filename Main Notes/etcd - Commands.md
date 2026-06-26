---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[etcd]]"
sub_type: use-case
source_type: udemy
source_url: "https://kodekloud.com"
author: "Mumshad Mannambeth"
course_title: "Certified Kubernetes Administrator (CKA)"
tags:
  - kubernetes/commands
  - kubernetes/deep-dive
---

# etcd - Commands

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[etcd]] > **Commands**

---

## 🛠️ CLI Tools: etcdctl & etcdutl
* **`etcdctl`:** Command-line client for interacting with a running `etcd` cluster. It is used to query or modify key-value pairs, check node health, manage members, and save runtime snapshots.
* **`etcdutl`:** Database utility client introduced in version 3.5. It is dedicated to offline operations (such as verifying, backing up, or restoring snapshot database files) without requiring a running etcd server.

---

## ⚙️ Selecting the API Version
By default, the `etcdctl` client might assume API v2. However, Kubernetes uses API v3. To ensure your commands execute using the v3 API, use one of the following methods:
1. **Per-Command Prefix:** Prepend the environment variable `ETCDCTL_API=3` to your CLI execution:
   ```bash
   ETCDCTL_API=3 etcdctl version
   ETCDCTL_API=3 etcdutl version
   ```
2. **Persistent Shell Export:** Export the variable in your current terminal session:
   ```bash
   export ETCDCTL_API=3
   etcdctl version
   ```

---

## 🆚 API v2 vs. API v3 CLI Command Comparison
The interface changed significantly between API v2 and v3. The following table highlights the difference in command syntax:

| Operation | API v2 Syntax (`ETCDCTL_API=2`) | API v3 Syntax (`ETCDCTL_API=3`) | Notes |
| :--- | :--- | :--- | :--- |
| **Check Version** | `etcdctl --version` | `etcdctl version` | v3 version is a subcommand. |
| **Write Key** | `etcdctl set key1 val` | `etcdctl put key1 val` | v3 uses `put` instead of `set`. |
| **Read Key** | `etcdctl get key1` | `etcdctl get key1` | v3 prints key name and value on separate lines. |
| **Query Key Prefix** | `etcdctl ls` | `etcdctl get / --prefix --keys-only` | v3 uses a flat keyspace without directories. |
| **Delete Key** | `etcdctl rm key1` | `etcdctl del key1` (or `delete`) | v2 uses `rm`; v3 uses `del` or `delete`. |
| **Watch Key** | `etcdctl watch key1` | `etcdctl watch key1` | v3 watch supports transaction streaming. |
| **Make Directory** | `etcdctl mkdir dir1` | *N/A* | Not supported in v3. |

---

## 🔬 Common CKA Diagnostic & Administrative Commands

### 1. View Cluster Member List
Requires TLS client authorization configurations on a default kubeadm static pod installation:
```bash
ETCDCTL_API=3 etcdctl \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  member list
```

### 2. Take a Snapshot Backup of a Live Cluster
```bash
ETCDCTL_API=3 etcdctl \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  snapshot save /opt/backup/etcd-snapshot.db
```

### 3. Check Snapshot Status & Integrity
```bash
ETCDCTL_API=3 etcdutl snapshot status /opt/backup/etcd-snapshot.db --write-out=table
# OR
ETCDCTL_API=3 etcdctl --write-out=table snapshot status /opt/backup/etcd-snapshot.db
```

### 4. Restore Snapshot Offline to a New Directory
```bash
ETCDCTL_API=3 etcdutl snapshot restore /opt/backup/etcd-snapshot.db \
  --data-dir=/var/lib/etcd-restored
```

### 5. Query All Kubernetes Registry Keys in etcd
```bash
ETCDCTL_API=3 etcdctl \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  get / --prefix --keys-only
```

*Read more in [[Reference Notes/0-10_maintenance_upgrades_and_etcd.md#4-etcd-backup-restore-stacked-external-topologies]]*
