---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[etcd-deeper]]"
sub_type: architecture
source_type: documentation
source_url: "https://etcd.io/docs/v3.5/faq/"
author: "etcd Maintainers"
against: []
tags:
  - kubernetes/etcd
  - etcd/architecture
---

# etcd - Raft Quorum Rules

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[etcd]] > [[etcd-deeper]] > **Raft Quorum Rules**

---

## 📑 1. What is Quorum?
In distributed databases, **Quorum** is the minimum number of active nodes required to make clustering decisions (such as electing leaders or committing writes). 

The formula for quorum in ETCD is:

$$\text{Quorum} = \lfloor N/2 \rfloor + 1$$

Where $N$ is the total number of members in the cluster.

---

## ⚙️ 2. Member/Failure Matrix
Because of quorum rules, ETCD clusters must always contain an **odd number** of members.

| Cluster Size | Quorum Size | Max Failures Tolerated |
| :---: | :---: | :---: |
| 1 | 1 | 0 |
| 3 | 2 | 1 |
| 5 | 3 | 2 |
| 7 | 4 | 3 |

* **Even counts (e.g. 4 nodes):** Quorum is 3. It tolerates only 1 failure (same as a 3-node cluster) but introduces higher networking costs, which is why it is discouraged.

---

## 🔬 3. Split-Brain Mitigation
If a network partition occurs and splits a 5-node cluster into a 3-node group and a 2-node group:
* **3-node group:** Has quorum ($3 \ge 3$) and continues functioning.
* **2-node group:** Lacks quorum ($2 < 3$) and rejects all write operations, preventing conflicting data writes.

*Read more in [[Reference Notes/0-10_maintenance_upgrades_and_etcd.md#4-etcd-database-administration-and-restoration]]*\n