---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[aws]]"
sub_type: core-concept
source_type: documentation
source_url: "https://docs.aws.amazon.com/rds/"
author: "AWS Documentation"
course_title: "AWS Database Services Overview"
against: []
tags:
  - aws/database
  - aws/rds
  - aws/dynamodb
  - aws/deep-dive
---

# aws - RDS, Aurora, and DynamoDB

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[aws]] > **RDS, Aurora, and DynamoDB**

---

## 📑 Relational (OLTP): RDS & Aurora

*   **Amazon RDS:** Managed relational database service. Supports MySQL, PostgreSQL, MariaDB, Oracle, and SQL Server.
    *   **RDS Multi-AZ (High Availability):** Syncs data synchronously to a Standby DB in a separate AZ. If the primary node fails, AWS automatically updates DNS endpoints to failover to the standby node (providing disaster recovery and high availability with zero developer code changes).
    *   **Read Replicas:** Async replication to read-only instances. Used to scale read heavy workloads (not for disaster recovery failover).
*   **Amazon Aurora:** AWS's cloud-native relational database engine (MySQL/PostgreSQL compatible). Uses a shared virtualized storage layer replicated 6 ways across 3 AZs. Supports auto-healing storage, Aurora Serverless, and Multi-Master writes.

---

## 📑 NoSQL (Key-Value): DynamoDB & DAX

*   **Amazon DynamoDB:** Managed, serverless, single-digit millisecond latency NoSQL key-value database. Scales horizontally automatically. Uses RCUs (Read Capacity Units) and WCUs (Write Capacity Units) to provision throughput.
*   **DynamoDB Accelerator (DAX):** In-memory cache layer for DynamoDB. Reduces read latency from milliseconds to microseconds (<1ms) for read-heavy or hot-key workloads.

---

## 📑 Caching (ElastiCache) & Warehousing (Redshift)

*   **Amazon ElastiCache:** Managed in-memory caching service supporting Redis (high availability, complex data types) and Memcached (simple key-value strings, multithreaded scaling).
*   **Amazon Redshift:** Fully managed columnar data warehouse (OLAP - Online Analytical Processing) designed for historical business intelligence queries. Scales to petabytes.

*Read more in [3-7_aws_rds_aurora_databases.md](../Reference%20Notes/3-7_aws_rds_aurora_databases.md) and [3-8_aws_dynamodb_nosql.md](../Reference%20Notes/3-8_aws_dynamodb_nosql.md)*
