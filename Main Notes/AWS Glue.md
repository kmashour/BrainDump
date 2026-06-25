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
  - "[[Amazon Athena]]"
against:
  - "[[Amazon EMR]]"
reference_guides:
  - "[[Reference Notes/3-19_databases_analytics_ml.md]]"
tags:
  - aws/glue
  - database/etl
  - status/completed
---

# AWS Glue

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **AWS Glue**

---

## 🎯 Purpose (Why it is used)
AWS Glue is a serverless, managed Extract, Transform, and Load (ETL) service designed to discover, prepare, copy, and integrate data from multiple sources for analytics. It allows organizations to build automated data pipelines that clean, format, and load data into data lakes or data warehouses.

---

## ⚙️ Functionality (What it is doing)
*   **Glue Data Catalog (Shared Metadata):** Central repository that stores metadata table definitions, shared across Athena, Redshift Spectrum, and EMR.
*   **Glue Crawlers (Schema Inference):** Connects to storage systems (S3, RDS, DynamoDB, JDBC), infers schema fields automatically, and writes structural tables to the catalog.
*   **Serverless ETL Execution:** Generates Scala/Python code running on serverless Apache Spark execution environments to transform and load datasets (e.g. CSV to Parquet/ORC).
*   **Job Bookmarks:** Remembers processed state across execution runs to prevent reprocessing historical data in recurring batch runs.
*   **Glue Data Brew:** Visual data preparation tool allowing analysts to clean and normalize data using pre-built transformations.
*   **Streaming ETL:** Executes real-time ETL processing against data streaming continuously from Kinesis Data Streams or Apache Kafka.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Glue sits as the central ingestion and metadata sync layer. It crawls source storage systems (like S3) to populate the Glue Data Catalog. Query engines (like Athena and Redshift Spectrum) then query the Glue Data Catalog to resolve physical data structures in S3.

---

## 🧩 Problem Solver (What problem it solves)
Building and scaling Spark clusters for simple ETL jobs requires provisioning machines and updating custom scripts. Furthermore, keeping query engine schemas synchronized with raw storage fields is error-prone. Glue solves this by automating schema discovery and providing serverless Spark compute environments.

---

## 🟢 Operational Impact (What will happen with it operating)
Metadata catalogs are updated automatically, and data format conversions (like CSV to Parquet/ORC) reduce query costs on S3. ETL jobs scale serverless capacity on-demand.

---

## 🔴 Failure Impact (What will happen without it)
Without Glue, engineers must manually maintain schema mappings inside Athena/Redshift and run continuous EC2/EMR clusters to perform daily data transformations and format conversions.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **AWS Glue**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
