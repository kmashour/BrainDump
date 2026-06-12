---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[etcd-deeper]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm/"
author: "Kubernetes Documentation"
against: []
tags:
  - kubernetes/etcd
  - etcd/security
---

# etcd - etcd TLS certificate configurations

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[etcd]] > [[etcd-deeper]] > **etcd TLS Configurations**

---

## 📑 1. PKI Folder Structure
Kubernetes secures ETCD traffic using client-server certificates located under `/etc/kubernetes/pki/etcd/` on the control plane node.

```text
/etc/kubernetes/pki/etcd/
  |-- ca.crt          (ETCD Certificate Authority)
  |-- ca.key
  |-- server.crt      (Server TLS Cert - presented to clients)
  |-- server.key
  |-- peer.crt        (Peer TLS Cert - presented to other members)
  |-- peer.key
  |-- healthcheck-client.crt (Used by APIServer liveness checks)
  |-- healthcheck-client.key
```

---

## ⚙️ 2. Securing the CLI with TLS
To query `etcdctl` without authentication warnings, you must pass the TLS certificate flags:
```bash
ETCDCTL_API=3 etcdctl   --endpoints=https://127.0.0.1:2379   --cacert=/etc/kubernetes/pki/etcd/ca.crt   --cert=/etc/kubernetes/pki/etcd/server.crt   --key=/etc/kubernetes/pki/etcd/server.key   endpoint health
```

---

## 🔬 3. Cert Expiry Check
Check the validity duration of the etcd certificate using `openssl`:
```bash
openssl x509 -in /etc/kubernetes/pki/etcd/server.crt -text -noout | grep -A 2 Validity
```
Alternatively, use `kubeadm`:
```bash
kubeadm certs check-expiration | grep etcd
```

*Read more in [[Reference Notes/0-10_maintenance_upgrades_and_etcd.md#4-etcd-database-administration-and-restoration]]*\n