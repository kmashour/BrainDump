---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
  - "database"
related_concepts:
  - "[[Amazon DynamoDB]]"
against:
  - "[[Amazon DynamoDB]]"
reference_guides:
  - "[[Reference Notes/3-19_databases_analytics_ml.md]]"
tags:
  - aws/keyspaces
  - database/nosql
  - status/completed
---

# Amazon Keyspaces

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **Amazon Keyspaces**

---

## 🎯 Purpose (Why it is used)
Amazon Keyspaces (for Apache Cassandra) is a scalable, highly available, and managed wide-column NoSQL database service. It is designed to run open-source Apache Cassandra workloads in the cloud without modifying application code or managing complex server clusters.

---

## ⚙️ Functionality (What it is doing)
*   **CQL API Compatibility:** Supports the Cassandra Query Language (CQL) API and standard Cassandra drivers without modifying application code.
*   **PITR Backups:** Provides continuous backups with Point-in-Time Recovery (PITR) up to 35 days for disaster restoration.
*   **Multi-Region Replication:** Automatically replicates table datasets across multiple Availability Zones natively, and supports multi-region active-active clusters.
*   **Flexible Capacity Modes:** Offers on-demand capacity scaling (automatic instant adjustments) or provisioned capacity modes (with target-tracking auto-scaling).
*   **IAM Authentication:** Integrates with AWS IAM for user database authentication and table-level access authorization.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Keyspaces acts as the managed NoSQL database backend for Cassandra-native applications. Developers point their application drivers to the Keyspaces endpoints, eliminating the need to manage EC2 Cassandra clusters.

---

## 🧩 Problem Solver (What problem it solves)
Managing Cassandra clusters involves complex node tuning, ring topology maintenance, node repair tasks, and disk space management. Keyspaces solves this by abstracting Cassandra into a serverless, pay-as-you-go API that handles replication and scaling automatically.

---

## 🟢 Operational Impact (What will happen with it operating)
Cassandra applications run on AWS with single-digit millisecond latency. Disk scaling, backup management (PITR), and cross-AZ replication are automated, freeing operations teams from database maintenance.

---

## 🔴 Failure Impact (What will happen without it)
Without Keyspaces, running Cassandra workloads requires provisioning, monitoring, and manually maintaining a cluster of EC2 instances, which leads to high operational complexity and potential failover risks.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Amazon Keyspaces**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
