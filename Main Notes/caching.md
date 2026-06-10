---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "database"
  - "infra"
related_concepts:
  - "[[database-selection]]"
  - "[[cdn]]"
against: []
reference_guides:
  - "[[Reference Notes/1-4_caching_and_content_delivery_networks.md]]"
tags:
  - system-design/caching
  - status/completed
---

# Caching

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **Caching**

---

## 🎯 Purpose (Why it is used)
Caching is used to temporarily store copies of hot, high-demand, or computationally expensive data in high-speed, volatile memory (RAM) to minimize slow and resource-intensive disk reads or complex database query operations.

---

## ⚙️ Functionality (What it is doing)
- **Fast Reads:** Exposes data from in-memory stores (e.g., Redis, Memcached) with sub-millisecond latency.
- **Eviction Execution:** Releases memory using algorithms (e.g., LRU, LFU) when memory thresholds are reached.
- **Write Policy Enforcement:** Coordinates data updates between application layers, cache, and database tiers.
- **TTL Expiry:** Automatically deletes data records after a configured Time-To-Live (TTL) to prevent stale states.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Caching sits directly between the application server and the database or physical file systems. The application server intercepts incoming read queries, checking the cache tier first before descending into SQL/NoSQL databases.

---

## 🧩 Problem Solver (What problem it solves)
- **Database Bottlenecks:** Prevents primary database systems from reaching resource saturation (CPU/IOPS) under heavy read loads.
- **High Latency:** Lowers user response times by eliminating disk access and network hops.
- **Excessive Compute:** Stores pre-calculated API responses, preventing redundant application processing loops.

---

## 🟢 Operational Impact (What will happen with it operating)
With caching operating correctly, database systems experience low steady-state load. The system scales efficiently to handle spikes (e.g., viral posts) without crashing backend databases.

---

## 🔴 Failure Impact (What will happen without it)
Without caching, every user request translates directly to a database disk query. During traffic surges, databases become overloaded, leading to CPU exhaustion, query queues, high latencies, and total system outages (Cache Stampede).

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Caching**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[caching]]
SORT file.name ASC
```
