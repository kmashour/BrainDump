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
*   **Key-Value & Document Storage:** Persists unstructured or semi-structured data blocks, allowing items to have varying schemas and attributes.
*   **Capacity Tuning Modes:** Provisions Read/Write Capacity Units (RCU/WCU) for predictable traffic or scales dynamically (On-Demand) to handle spikes.
*   **Real-time Stream Integration:** Publishes modifications to tables to DynamoDB Streams or Kinesis streams to trigger downstream processes.
*   **Active-Active Replication:** Replicates tables globally (Global Tables) across regions, permitting low-latency regional reads and writes.

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
