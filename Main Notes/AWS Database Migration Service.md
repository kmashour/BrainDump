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
against: []
reference_guides:
  - "[[Reference Notes/3-15_aws_disaster_recovery.md]]"
tags:
  - aws/dms
  - status/completed
---

# AWS Database Migration Service

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[Amazon RDS]] > **AWS Database Migration Service**

---

## 🎯 Purpose (Why it is used)
AWS Database Migration Service (DMS) helps migrate databases to AWS quickly and securely. The source database remains fully operational during the migration, minimizing downtime for applications that rely on it.

---

## ⚙️ Functionality (What it is doing)
- **Data Transport and Replication:** Pulls data from a source endpoint and writes it to a target endpoint using a replication instance.
- **Homogeneous Migrations:** Directly replicates between identical engines (e.g., PostgreSQL to PostgreSQL).
- **Heterogeneous Migrations:** Migrates between different engines (e.g., Oracle to Aurora MySQL). Integrates with the **AWS Schema Conversion Tool (SCT)** to convert schemas, stored procedures, and tables beforehand.
- **Change Data Capture (CDC):** Continuously captures source transactions in real-time to keep target databases updated prior to cutover.
- **Flexible Management:** Supports provisioned instances (with Multi-AZ replication) or Serverless mode to automatically scale replication compute.

---

## 🏛️ Architectural Context (How it fits in the architecture)
DMS runs on a replication instance located in a VPC subnet. It establishes connections to both the source endpoint (on-premises database or cloud database) and target endpoint (RDS, S3, Redshift, DynamoDB).

---

## 🧩 Problem Solver (What problem it solves)
DMS solves the problem of high downtime and complex coding tasks associated with database migrations. Instead of taking the database offline, performing a logical dump, copying it, and restoring it, DMS replicates the data live while applications continue writing.

---

## 🟢 Operational Impact (What will happen with it operating)
Database migrations are executed with zero downtime. Databases can be migrated, consolidated, or replicated continuously to enable reporting/analytics targets without affecting production transaction performance.

---

## 🔴 Failure Impact (What will happen without it)
Without DMS, database migrations require significant downtime (maintenance windows), custom replication script development, and manual schema translation errors.

---

## 📂 Reference Guides
*   [[3-15_aws_disaster_recovery]] ([3-15_aws_disaster_recovery.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/3-15_aws_disaster_recovery.md))

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **AWS Database Migration Service**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
