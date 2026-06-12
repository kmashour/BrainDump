---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "database"
  - "infra"
related_concepts:
  - "[[persistentvolume]]"
against:
  - "[[flat-files]]"
reference_guides:
  - "[[Reference Notes/1-3_database_architectures_and_sharding.md]]"
tags:
  - system-design/database
  - status/completed
---

# Database Selection

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **Database Selection**

---

## 🎯 Purpose (Why it is used)
Database Selection is the architectural process of choosing and deploying the correct data storage engine (Relational/SQL vs. Non-Relational/NoSQL) depending on requirements for consistency, performance, horizontal scalability, and data model relationships.

---

## ⚙️ Functionality (What it is doing)
- **Data Persistence:** Writes and commits application state to physical storage media (HDDs/SSDs).
- **Transaction Management:** Guarantees transactional properties (such as ACID in relational databases).
- **Query Processing:** Exposes structured query interfaces (SQL or API selectors) to retrieve and manipulate stored data.
- **Indexing:** Builds structures (B-Trees, LSM-Trees, inverted indexes) to accelerate read path speeds.
- **Replication and Partitioning:** Copies data across cluster nodes (replicas) or partitions it (shards) to achieve high availability and scaling.

---

## 🏛️ Architectural Context (How it fits in the architecture)
The database serves as the persistent data tier of an application. Application servers query it to read or write persistent state. It is typically deployed behind a caching layer (like Redis) and in a clustered primary-replica configuration.

---

## 🧩 Problem Solver (What problem it solves)
- **State Persistence:** Solves the challenge of storing application data permanently so it survives server crashes.
- **Data Integrity:** Prevents corrupted or partial transactions through write-ahead logging and transaction locks.
- **Scalability bottlenecks:** By selecting columnar or key-value structures, systems can handle high-throughput telemetry or user profiles that would swamp traditional relational tables.

---

## 🟢 Operational Impact (What will happen with it operating)
Selecting the right database structure ensures optimal search latency, clean data normalization, and reliable backups. It defines how the system handles schema updates and network partition events.

---

## 🔴 Failure Impact (What will happen without it)
Without a designated database engine, applications are forced to use raw flat files, leading to file-locking conflicts, query performance degradation, data inconsistency, and high risk of corruption under concurrent writes.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Database Selection**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), "database-selection")
SORT file.name ASC
```
