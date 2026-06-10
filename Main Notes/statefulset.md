---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: workload
domains:
  - "kubernetes"
related_concepts:
  - "[[deployment]]"
  - "[[pod]]"
against:
  - "[[deployment]]"
reference_guides:
  - "[[Reference Notes/0-6_kubernetes_workloads_and_controllers.md]]"
tags:
  - kubernetes/controller
  - status/completed
---

# statefulset

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Workloads & Infrastructure > **statefulset**

---

## 🎯 Purpose (Why it is used)
The `StatefulSet` manages the deployment and scaling of stateful applications, guaranteeing stable, unique network identities, ordered startup/teardown, and persistent storage mapping for each individual pod ordinal.

---

## ⚙️ Functionality (What it is doing)
* **Ordinal Indexing:** Assigns a persistent zero-indexed integer to each pod (e.g. `web-0`, `web-1`).
* **Stable Network Identity:** Pairs with a Headless Service to create stable DNS records (e.g. `web-0.nginx.default.svc.cluster.local`).
* **Volume Claim Templates:** Dynamically provisions a dedicated Persistent Volume (PV) for each pod ordinal, ensuring storage remains attached to the exact same pod ordinal even after rescheduling.
* **Ordered Execution:** Defaults to starting and stopping pods in sequence (`0` to `N-1` for startup, `N-1` to `0` for teardown), preventing write conflicts in distributed databases.

---

## 🏛️ Architectural Context (How it fits in the architecture)
* **Stateful Orchestrator:** Sits alongside `Deployment`. Used primarily for databases (MySQL, Postgres, Cassandra), queues (RabbitMQ, Kafka), and cluster storage engines.
* **Headless Service dependency:** Requires a companion Headless Service (with `clusterIP: None`) to publish DNS names.

---

## 🧩 Problem Solver (What problem it solves)
* **Storage Re-attachment:** Solves database data loss on pod rescheduling. If `web-1` dies and restarts on a different node, it connects back to the exact same Persistent Volume (`www-web-1`) containing its data.
* **Clustered App Split-Brain:** Solves startup race conditions and split-brain states in consensus systems (like Raft or Paxos) by assigning stable DNS addresses and ordering startup.

---

## 🟢 Operational Impact (What will happen with it operating)
* Database clusters (like postgres-0, postgres-1) maintain stable master-replica sync mappings.
* Re-scheduled stateful pods find their dedicated disks automatically.
* Ordered upgrades execute safely without collapsing the consensus quorum.

---

## 🔴 Failure Impact (What will happen without it)
* Databases cannot run reliably inside the cluster; pods receive randomized IPs and dynamic volume attachments, causing data loss and synchronization failures.
* Split-brain errors occur frequently when nodes fail.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **statefulset**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[statefulset]]
SORT file.name ASC
```
