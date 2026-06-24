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
  - "[[Amazon Aurora]]"
against: []
reference_guides:
  - "[[Reference Notes/3-7_aws_rds_aurora_databases.md]]"
tags:
  - aws/rds-proxy
  - status/completed
---

# RDS Proxy

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **RDS Proxy**

---

## 🎯 Purpose (Why it is used)
Amazon RDS Proxy is a fully managed, highly available database proxy that pools database connections, improving the scalability, resiliency, and security of applications interacting with Amazon RDS and Amazon Aurora databases. It prevents database resource exhaustion and connection timeout errors under heavy client load.

---

## ⚙️ Functionality (What it is doing)
- **Connection Pooling:** Pools and shares established database connections. Reuses connections instead of spawning a new database connection for each request.
- **Failover Acceleration:** Speeds up failover recovery time by up to 66% by preserving the client-side connection and routing traffic to the promoted master DB instantly.
- **Credential Segregation:** Integrates with AWS Secrets Manager to store credentials securely and enforces IAM database authentication.
- **VPC Containment:** Operates strictly within the VPC subnets, ensuring no public internet exposure.

---

## 🏛️ Architectural Context (How it fits in the architecture)
RDS Proxy sits in front of Amazon RDS or Amazon Aurora instances within the private subnet architecture. It is especially critical in serverless architectures using AWS Lambda, where sudden spikes in functions would otherwise trigger connection storms and exhaust database CPU and RAM.

---

## 🧩 Problem Solver (What problem it solves)
RDS Proxy solves the connection exhaustion problem in relational databases, which have a fixed capacity for concurrent active connections (scaling CPU and RAM limits). It prevents database crashes caused by connection spikes, handles automatic failover routing transparently, and eliminates the need for complex connection-pooling code inside client applications.

---

## 🟢 Operational Impact (What will happen with it operating)
Applications require less database capacity to handle high concurrency, resulting in lower RDS instance sizes and costs. The database remains protected from connection storms, and serverless compute scaling (e.g., Lambda functions) is decoupled from database scaling limits.

---

## 🔴 Failure Impact (What will happen without it)
Without RDS Proxy, applications must connect directly to the database, leaving the database vulnerable to CPU spikes, timeouts, and resource exhaustion under high load. Failover events will take longer to resolve (requiring client-side re-connections), and serverless scaling will be severely restricted by database connection limits.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **RDS Proxy**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
