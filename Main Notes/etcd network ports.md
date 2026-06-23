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
    - --initial-cluster=controlplane=https://10.10.0.5:2380
    - --listen-metrics-urls=http://127.0.0.1:2381
```

### Flag Category Breakdowns

#### A. Listen Flags (Where the process binds)
These flags tell the `etcd` process which physical or virtual network interfaces to attach to on the Linux host:
*   **`--listen-client-urls`**: Binds port `2379` locally. Typically listens on `127.0.0.1` (so local tools like `etcdctl` can access the db) and the host network interface IP (so the `kube-apiserver` on other nodes can communicate with it).
*   **`--listen-peer-urls`**: Binds port `2380` locally for cluster sync. It listens only on the network IP as peer replication traffic only originates from other nodes over the network.
*   **`--listen-metrics-urls`**: Opens an unencrypted HTTP port (typically port `2381` on localhost) to expose prometheus-compatible health and performance metrics.

#### B. Advertise Flags (What it broadcasts to others)
These flags act as a megaphone. They tell other cluster components where they should try to reach this node:
*   **`--advertise-client-urls`**: Tells the `kube-apiserver` where to send client database queries (read/write/watch requests).
*   **`--initial-advertise-peer-urls`**: Tells other member `etcd` nodes where to connect for leader elections or data replication.

#### C. Bootstrapping Flags
*   **`--initial-cluster`**: Defines the initial static peer map. During startup, etcd nodes use this configuration to identify the address mappings of all voting nodes in the cluster to form a quorum (e.g., `node1=IP1:2380,node2=IP2:2380`).

> [!TIP]
> **CKA Exam Tip:** If running `etcdctl` commands returns connection refused errors, check `/etc/kubernetes/manifests/etcd.yaml`. The `--endpoints` parameter in your command must use one of the exactly matched endpoints specified in the `--listen-client-urls` (most commonly `https://127.0.0.1:2379`).

---

## 🔬 3. Verification Commands
Verify port listening status directly on the master node host:
```bash
sudo netstat -tulnp | grep -E '2379|2380|2381'
# or using ss
ss -lntp | grep -E '2379|2380|2381'
```

*Read more in [[Reference Notes/0-10_maintenance_upgrades_and_etcd.md#4-etcd-database-administration-and-restoration]]*