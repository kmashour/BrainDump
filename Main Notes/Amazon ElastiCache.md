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
against:
  - "[[Amazon RDS]]"
reference_guides:
  - "[[Reference Notes/3-7_aws_rds_aurora_databases.md]]"
tags:
  - aws/elasticache
  - status/completed
---

# Amazon ElastiCache

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **Amazon ElastiCache**

---

## 🎯 Purpose (Why it is used)
Amazon ElastiCache is a fully managed, in-memory caching service designed to improve the performance and scalability of web applications by retrieving data from fast, managed in-memory caches (Redis OSS or Memcached) instead of relying solely on slower disk-based relational databases.

---

## ⚙️ Functionality (What it is doing)
- **In-Memory Caching:** Stores frequently queried data in RAM, offering sub-millisecond latencies for read-intensive workloads.
- **Redis High Availability:** Supports Multi-AZ deployments with auto-failover, backup and restore, and read replica scaling.
- **Memcached Sharding:** Implements multi-threaded architecture with partitioned sharded data across multiple nodes for horizontal scaling of simple key-value lookups.
- **Gaming Leaderboards (Redis):** Native support for advanced data structures (e.g., Sorted Sets) to compute real-time leaderboards on-the-fly.
- **Session Management:** Stores volatile user session tokens using Time-to-Live (TTL) settings to maintain stateless application tiers.

---

## 🏛️ Architectural Context (How it fits in the architecture)
ElastiCache runs inside a private VPC. Unlike transparent caches (such as CloudFront), implementing ElastiCache requires explicit application-side code modifications. The application must be programmed to query the cache (lazy loading) and write updates back to it (write-through).

---

## 🧩 Problem Solver (What problem it solves)
ElastiCache solves query latency bottlenecks and database resource saturation caused by high volumes of read queries. It alleviates database CPU/RAM strain, reduces query execution times from milliseconds to microseconds, and eliminates session replication overhead across multiple web servers.

---

## 🟢 Operational Impact (What will happen with it operating)
Relational databases experience significantly reduced query loads, allowing developers to run smaller DB instances and save costs. End-users experience instantaneous response times, and applications scale seamlessly to millions of concurrent reads.

---

## 🔴 Failure Impact (What will happen without it)
If ElastiCache fails, all read traffic falls back directly to the backend database. This sudden query spike (cache stampede) can easily overload and crash relational databases, degrading application performance and causing cascade timeouts across the entire system.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Amazon ElastiCache**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
