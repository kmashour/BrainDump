---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[aws]]"
  - "[[Amazon RDS]]"
  - "[[RDS Proxy]]"
against:
  - "[[Amazon RDS]]"
reference_guides:
  - "[[Reference Notes/3-7_aws_rds_aurora_databases.md]]"
tags:
  - aws/aurora
  - status/completed
---

# Amazon Aurora

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **Amazon Aurora**

---

## 🎯 Purpose (Why it is used)
Amazon Aurora is a cloud-native, high-performance relational database engine compatible with MySQL and PostgreSQL. It is designed to provide commercial-grade performance, durability, and availability at a fraction of the cost of traditional databases, serving as the relational database backend for high-throughput, mission-critical enterprise applications.

---

## ⚙️ Functionality (What it is doing)
- **Shared Storage Mesh:** Striping data across a virtualized storage volume that auto-expands up to 128 TB, independent of database compute instances.
- **6-Way Replication:** Replicates every database write 6 ways across 3 Availability Zones (2 copies per AZ).
- **Quorum Writes/Reads:** Writes require a quorum of 4 out of 6 copies; reads require 3 out of 6 copies. Continuous background self-healing via peer-to-peer volume verification.
- **Fast Failovers:** Minimizes failover recovery times to under 30 seconds by promoting an active Read Replica (up to 15 supported) to Master.
- **Serverless & Global Scaling:** Automatically scales compute resources via Aurora Serverless v2, and provides global cross-region asynchronous replication with latency < 1 second.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Aurora cluster instances reside in a VPC. It separates compute (writer and reader instances) from the underlying shared storage layer. Applications connect to the database using cluster endpoints: the Writer Endpoint (redirecting to the Master instance) and the Reader Endpoint (load balancing connection traffic to replicas).

---

## 🧩 Problem Solver (What problem it solves)
Aurora solves the replication lag, storage volume provisioning limits, and slow failover times typical of traditional database replication models. By separating compute from storage, it eliminates disk IO bottlenecks, avoids backup impact on primary instance compute, and automates horizontal read scaling.

---

## 🟢 Operational Impact (What will happen with it operating)
Applications experience sub-10ms replica lag, high write throughput, and instantaneous background self-healing. Administrative teams can easily scale readers or clone database environments for testing with zero production impact using the copy-on-write protocol.

---

## 🔴 Failure Impact (What will happen without it)
A complete Aurora cluster failure halts all read and write queries, paralyzing application workflows. However, due to its 6-way storage replication, the loss of an entire Availability Zone does not cause data loss or service disruption, as writes continue with the remaining 4 quorum copies.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Amazon Aurora**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
