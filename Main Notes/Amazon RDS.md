---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[aws]]"
  - "[[Amazon Aurora]]"
  - "[[RDS Proxy]]"
against:
  - "[[Amazon ElastiCache]]"
reference_guides:
  - "[[Reference Notes/3-7_aws_rds_aurora_databases.md]]"
tags:
  - aws/rds
  - status/completed
---

# Amazon RDS

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **Amazon RDS**

---

## 🎯 Purpose (Why it is used)
Amazon RDS (Relational Database Service) is a managed SQL database service that simplifies the provisioning, operating, and scaling of traditional relational database engines in the cloud. It eliminates operational overhead (such as hardware provisioning, software patching, and backups) so developers can focus on database schema design and application queries.

---

## ⚙️ Functionality (What it is doing)
- **Engine Management:** Supports multiple relational database engines including PostgreSQL, MySQL, MariaDB, Oracle, Microsoft SQL Server, and IBM DB2.
- **Disaster Recovery (Multi-AZ):** Replicates data synchronously to a Standby DB instance in another Availability Zone. Provides automatic failover via DNS CNAME updates.
- **Read Scaling:** Provisions up to 15 Read Replicas with asynchronous replication (eventual consistency) within the same region or cross-region.
- **Storage Auto Scaling:** Dynamically increases allocated storage capacity on-demand with zero downtime based on free-space thresholds.
- **Backup & Recovery:** Performs automated daily backups and continuous transaction logging every 5 minutes to support Point-in-Time Recovery (PITR).

---

## 🏛️ Architectural Context (How it fits in the architecture)
RDS runs within a customer's Virtual Private Cloud (VPC). Best practices dictate placing database instances inside private subnets and using Security Groups to restrict access only to the application/backend tier. RDS does not provide SSH host access (except for the **RDS Custom** tier which supports admin access for Oracle and SQL Server).

---

## 🧩 Problem Solver (What problem it solves)
RDS eliminates the administrative burden, configuration complexity, and scaling limits of hosting relational databases on self-managed EC2 instances or on-premises servers. It automatically handles failover, OS-level patching, replication lag monitoring, and storage volume growth.

---

## 🟢 Operational Impact (What will happen with it operating)
Applications gain a highly available, durable database platform with automated failover and scaling. Administrative operations (such as vertical compute scaling or converting from Single-AZ to Multi-AZ) are performed with zero or minimal downtime.

---

## 🔴 Failure Impact (What will happen without it)
If RDS is unavailable, applications cannot execute read or write queries, causing complete system outages for stateful workflows. Outages or storage exhaustion will result in application timeouts, transaction drops, and potential data corruption in uncommitted states.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Amazon RDS**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
