---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
  - "database"
related_concepts:
  - "[[Amazon RDS]]"
  - "[[Amazon Aurora]]"
  - "[[AWS Lambda]]"
  - "[[Amazon S3]]"
against:
  - "[[Amazon RDS]]"
  - "[[Amazon Aurora]]"
reference_guides:
  - "[[Reference Notes/3-18_serverless.md]]"
tags:
  - aws/dynamodb
  - database/nosql
  - status/completed
---

# Amazon DynamoDB

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **Amazon DynamoDB**

---

## 🎯 Purpose (Why it is used)
Amazon DynamoDB is a fully managed, serverless, multi-AZ replicated NoSQL key-value and document database designed to deliver single-digit millisecond performance at any scale. It handles massive read/write workloads with automated scaling and partition management.

---

## ⚙️ Functionality (What it is doing)
*   **Key Schema & Schema Flexibility:** Composed of tables storing items (rows) up to a **maximum size of 400 KB** each. Items are identified by a Primary Key (composed of a Partition Key, and an optional Sort Key) and can hold varying attributes, allowing schemas to evolve dynamically.
*   **Read/Write Capacity Modes:**
    *   *Provisioned Capacity:* Allocates explicit Read Capacity Units (RCUs) and Write Capacity Units (WCUs) in advance, scaling automatically using Auto Scaling. Recommended for predictable workloads.
    *   *On-Demand Capacity:* Automatically adjusts read and write limits dynamically in response to traffic. Operates on a pay-per-request model, making it ideal for highly unpredictable or low-utilization apps.
*   **DynamoDB Accelerator (DAX):** A fully managed, API-compatible in-memory write-through cache placed in front of tables. Reduces read latencies to microseconds for raw reads and queries. 
    *   *Contrast with ElastiCache:* Use **DAX** as a drop-in cache for database query results; use **ElastiCache** for storing processed/aggregated calculation outputs.
*   **DynamoDB Streams:** Emits a rolling 24-hour log capturing all item modifications (inserts, updates, deletes) in real-time. Natively triggers Lambda handlers to enable event-driven architectures.
*   **Global Tables:** Configures Active-Active, multi-region database replication. Leverages DynamoDB Streams under the hood to synchronize data across global regions with low regional latency.
*   **Time-to-Live (TTL):** Automatically purges items from tables when an epoch timestamp value is exceeded. Deletions happen in the background without consuming write capacity units, making it ideal for session tokens or compliance.

---

## 🏛️ Architectural Context (How it fits in the architecture)
DynamoDB serves as the database layer for serverless microservices. It is queried by Lambda functions and is cached at the read level by DynamoDB Accelerator (DAX). It handles events by pushing streams to Lambda and integrates with S3 for data exports/imports.

---

## 🧩 Problem Solver (What problem it solves)
Traditional relational databases require managing connection limits, provisioning server CPU, scaling shards, setting up read replica synchronizations, and managing schemas. DynamoDB provides an out-of-the-box, serverless database that scales infinitely without connection limits.

---

## 🟢 Operational Impact (What will happen with it operating)
Applications store session states, user profiles, or transactional records with microsecond cached or single-digit millisecond direct access. Storage capacity scales dynamically, and security policies restrict access at the row level via IAM.

---

## 🔴 Failure Impact (What will happen without it)
If the DynamoDB database service fails or experiences throttling:
*   Workloads cannot read or write data, causing application timeouts and API failures.
*   Lambda functions execution times lengthen as they wait for queries, increasing compute costs.
*   Downstream event triggers (welcome emails, analytics pipelines) halt as streams stop emitting.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Amazon DynamoDB**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
