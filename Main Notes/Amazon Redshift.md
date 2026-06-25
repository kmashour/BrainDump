---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
  - "database"
related_concepts:
  - "[[Amazon S3]]"
  - "[[Amazon Athena]]"
  - "[[AWS Glue]]"
against:
  - "[[Amazon Athena]]"
  - "[[Amazon Aurora]]"
reference_guides:
  - "[[Reference Notes/3-19_databases_analytics_ml.md]]"
tags:
  - aws/redshift
  - database/data-warehouse
  - status/completed
---

# Amazon Redshift

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **Amazon Redshift**

---

## 🎯 Purpose (Why it is used)
Amazon Redshift is a fully managed, petabyte-scale data warehouse service designed for Online Analytical Processing (OLAP). It enables organizations to run complex analytic queries against structured and semi-structured datasets, aggregating vast amounts of historical data to uncover business intelligence insights.

---

## ⚙️ Functionality (What it is doing)
*   **Columnar Data Storage:** Organizes data by column instead of row on disk, drastically reducing I/O and accelerating query aggregation.
*   **Leader & Compute Node Topology:** Deploys a **Leader Node** to parse queries, compile execution plans, and aggregate results, coordinating multiple **Compute Nodes** that execute queries in parallel and store database slices.
*   **Redshift Spectrum:** Queries massive external datasets directly in Amazon S3 by scanning metadata from Glue/Athena without loading S3 files into Redshift storage.
*   **Enhanced VPC Routing:** Secures network flows by routing all COPY and UNLOAD operations through private VPC subnets rather than crossing the public internet.
*   **Cross-Region Automated Snapshots:** Automatically replicates snapshots to a secondary AWS region for cross-region disaster recovery and disaster restoration.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Redshift acts as the central destination for enterprise data pipelines (ETL). Data is extracted from source transactional databases (like RDS) or files (in S3) and loaded into Redshift compute nodes. Business intelligence tools (like QuickSight) then connect to Redshift endpoints to query dashboards.

---

## 🧩 Problem Solver (What problem it solves)
Running heavy aggregation queries (e.g., counting billions of sales transactions) on Online Transaction Processing (OLTP) databases like RDS or Aurora degrades database performance and causes system bottlenecks. Redshift solves this by isolating analytical processing from transactional resources using optimized columnar storage.

---

## 🟢 Operational Impact (What will happen with it operating)
Operational analytics queries run at high speeds, and databases are protected from heavy analytical traffic. Query processing scales compute nodes automatically, and users can leverage S3 data lake storage dynamically via Redshift Spectrum.

---

## 🔴 Failure Impact (What will happen without it)
Without Redshift, organizations must run analytical queries directly on their transactional systems (resulting in degraded user performance or database crashes) or build complex self-managed Hadoop/Spark clusters to compile data reports.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Amazon Redshift**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
