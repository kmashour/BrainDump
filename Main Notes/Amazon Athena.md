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
  - "[[Amazon Redshift]]"
  - "[[AWS Glue]]"
against:
  - "[[Amazon Redshift]]"
reference_guides:
  - "[[Reference Notes/3-19_databases_analytics_ml.md]]"
tags:
  - aws/athena
  - database/query-engine
  - status/completed
---

# Amazon Athena

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **Amazon Athena**

---

## 🎯 Purpose (Why it is used)
Amazon Athena is an interactive, serverless query service designed to analyze data stored in Amazon S3 using standard SQL. It allows organizations to perform ad-hoc data discovery, schema validation, and analytics directly on raw or semi-structured S3 objects without needing to spin up, manage, or pay for continuous database servers.

---

## ⚙️ Functionality (What it is doing)
*   **Presto SQL Engine:** Runs standard ANSI SQL queries built on the open-source Presto distributed engine, executing directly on files in S3.
*   **Schema-on-Read Cataloging:** Resolves S3 text structures at query time by reading database and table schemas defined in the AWS Glue Data Catalog.
*   **Performance Optimization:** Minimizes scanned data volume and query costs through the use of columnar data formats (Parquet/ORC) and S3 path partitioning (e.g. `/year=/month=/`).
*   **Federated Query with Lambda:** Connects to external relational, NoSQL, and custom data sources (RDS, DynamoDB, on-premises) using AWS Lambda connectors.
*   **Multi-Format Ingestion:** Reads structured and semi-structured file types including CSV, JSON, Parquet, ORC, Avro, and raw logs.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Athena sits directly between S3 (the storage tier) and visualization or consuming applications (like QuickSight). It queries the AWS Glue Data Catalog to resolve table definitions and object locations in S3. 

---

## 🧩 Problem Solver (What problem it solves)
Traditional database analytics require loading data from storage buckets into a structured database warehouse (like Redshift) or running complex Hadoop/Spark clusters (EMR) which incur heavy management overhead and idle-resource costs. Athena solves this by executing queries directly on S3 objects on-demand, charging only for the amount of data scanned.

---

## 🟢 Operational Impact (What will happen with it operating)
With Athena active, users can immediately query logs (such as S3 access logs, CloudTrail logs, VPC Flow Logs, or ALB logs) and business data using standard SQL directly in S3. Operational costs are low for ad-hoc requests, and scaling is entirely managed.

---

## 🔴 Failure Impact (What will happen without it)
Without Athena, querying logs or files stored in S3 requires downloading raw files and parsing them using scripts, loading the data into a database instance, or provisioning and maintaining query servers (e.g., Presto or Hadoop clusters).

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Amazon Athena**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
