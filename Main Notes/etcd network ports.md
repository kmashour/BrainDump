---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[etcd-deeper]]"
sub_type: core-concept
source_type: documentation
source_url: "https://etcd.io/docs/v3.5/op-guide/configuration/"
author: "etcd Maintainers"
against: []
tags:
  - kubernetes/etcd
  - etcd/networking
---

# etcd - etcd network ports

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[etcd]] > [[etcd-deeper]] > **etcd Network Ports**

---

## 📑 1. Core etcd Network Ports
ETCD uses two standard TCP ports for communication:

* **Port `2379` (Client Communication):** Used by clients (e.g., `kube-apiserver` and `etcdctl`) to read, write, and watch key-value pairs.
* **Port `2380` (Peer-to-Peer Communication):** Used by etcd members to replicate database entries and negotiate Raft leader elections.

```text
[ kube-apiserver ] --Port 2379--> [ etcd Node A ] <--Port 2380--> [ etcd Node B ]
[ etcdctl tool   ] --Port 2379--/
```

---

## ⚙️ 2. Configuration Flags in Manifest
Check the listener bindings in `/etc/kubernetes/manifests/etcd.yaml`:
```yaml
spec:
  containers:
  - command:
    - etcd
    - --listen-client-urls=https://127.0.0.1:2379,https://10.10.0.5:2379
    - --listen-peer-urls=https://10.10.0.5:2380
    - --advertise-client-urls=https://10.10.0.5:2379
    - --initial-advertise-peer-urls=https://10.10.0.5:2380
```

---

## 🔬 3. Verification Commands
Verify port listening status directly on the master node host:
```bash
sudo netstat -tulnp | grep -E '2379|2380'
# or using ss
ss -lntp | grep -E '2379|2380'
```

*Read more in [[Reference Notes/0-10_maintenance_upgrades_and_etcd.md#4-etcd-database-administration-and-restoration]]*\n