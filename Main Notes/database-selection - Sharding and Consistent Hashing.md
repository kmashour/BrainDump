---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[database-selection]]"
sub_type: core-concept
source_type: documentation
source_url: "https://www.youtube.com/watch?v=C842vFY5kRo"
author: "Hayk Simonyan"
course_title: "System Design Course"
tags:
  - system-design/database
  - system-design/deep-dive
---

# Database Selection - Sharding and Consistent Hashing

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[database-selection]] > **Sharding and Consistent Hashing**

---

## 📑 Database Scaling Strategies

When vertical scaling reaches hardware limits, we partition the data tier horizontally:

### 1. Master-Replica Replication
- Writes are executed on a primary (master) node, which replicates updates asynchronously to read replicas.
- **Limits:** Scales read capacity, but introduces **eventual consistency** latency. Write capacity remains bound to the primary node.

### 2. Database Sharding (Horizontal Partitioning)
- Splits a single dataset horizontally by distributing rows across independent database servers (shards).
- **Sharding Key:** The attribute that determines which shard holds a specific row (e.g. hashing `user_id`).
  - *Hot Spot Vulnerability:* Selecting a poor sharding key (e.g. `signup_country`) can direct $95\%$ of traffic to a single shard, causing resource exhaustion while other shards run idle.

---

## 📑 Consistent Hashing Mechanics

Traditional database routing using modular arithmetic (`hash(key) % N`) breaks down when shard count `N` changes, as it invalidates the mapping for almost all keys, requiring massive data migration.

**Consistent Hashing** resolves this by mapping keys and shards to a virtual ring:
1. **Hash Ring:** A virtual circle ranging from $0$ to $2^{32}-1$.
2. **Node Mapping:** Physical database or cache nodes are hashed and placed at specific positions on the ring.
3. **Key Assignment:** A key is hashed, placed on the ring, and routed clockwise to the first physical node encountered.
4. **Virtual Nodes (vnodes):** To prevent uneven key distribution, physical servers are mapped to multiple virtual locations (vnodes) scattered across the ring. This ensures balanced distribution and scales load dynamically according to server capacities.

*Read more in [System Design Fundamentals](../Reference%20Notes/17_system_design_fundamentals.md#e-consistent-hashing-mechanics)*
