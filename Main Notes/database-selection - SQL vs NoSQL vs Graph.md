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

# Database Selection - SQL vs NoSQL vs Graph

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[database-selection]] > **SQL vs NoSQL vs Graph**

---

## 📑 Core Database Categories

Understanding database architectures is critical for matching requirements to performance limits:

### 1. Relational (SQL) Databases
- **Structure:** Tabular schema with predefined columns, rows, and relationships (foreign keys).
- **Core Guarantees:** Strict **ACID** properties (Atomicity, Consistency, Isolation, Durability) for transaction integrity.
- **Query Mechanism:** Structured Query Language (SQL) supporting complex table joins.
- **Common Choices:** PostgreSQL, MySQL, MariaDB, SQLite.
- **Scaling Limit:** Scaled vertically by design; scaling horizontally requires read replicas, active-active proxying, or sharding (which compromises easy joins and multi-row transaction guarantees).

### 2. Document Databases (NoSQL)
- **Structure:** Stores data in JSON, BSON, or XML documents. Schema is dynamic and flexible.
- **Core Guarantees:** BASE properties (Basically Available, Soft state, Eventual consistency).
- **Query Mechanism:** API-based query selectors.
- **Common Choices:** MongoDB, CouchDB.
- **Ideal Use Case:** Catalog systems, content management, or user profiles with high, unpredictable attribute expansion.

### 3. Key-Value Stores (NoSQL)
- **Structure:** Simple hash table storing data against a unique string key.
- **Core Guarantees:** Optimized for sub-millisecond retrieval of atomic values.
- **Storage Tier:** In-memory (RAM) with optional disk persistence.
- **Common Choices:** Redis, Memcached.
- **Ideal Use Case:** Caching, session stores, rate limit counters, or message queues.

### 4. Column-Oriented / Columnar Databases (NoSQL)
- **Structure:** Stores data in columns rather than rows, allowing queries to read only the specific attributes needed.
- **Query Mechanism:** Key-space CQL queries.
- **Common Choices:** Apache Cassandra, HBase, ScyllaDB.
- **Ideal Use Case:** Big data analytics, telemetry log processing, and massive-scale write-heavy applications.

### 5. Graph Databases
- **Structure:** Represents data nodes (objects), edges (relationships), and properties.
- **Query Mechanism:** Graph traversal query languages (e.g., Cypher).
- **Common Choices:** Neo4j, Amazon Neptune.
- **Ideal Use Case:** Social graphs, recommendation engines, fraud detection patterns, and identity-access trees.

---

## 📑 Comparison Matrix

| Database Class | Normalization | Join Support | Scalability | Transaction Strength |
| :--- | :--- | :--- | :--- | :--- |
| **SQL** | High (Third Normal Form) | Native, highly optimized | Vertical (Shard for horizontal) | Strict ACID |
| **Document** | Denormalized (Nested structures) | Poor / Application-level joins | Horizontal (Native replica-sets) | Eventual Consistency (Local ACID) |
| **Key-Value** | None | No support | Horizontal | Atomic operations |
| **Columnar** | Denormalized | No support | High Horizontal (Peer-to-peer ring) | Eventual Consistency |
| **Graph** | Relational / Connective | Dynamic traversal (Index-free adjacency) | Cluster replication | ACID for graph modifications |

*Read more in [[Reference Notes/17_system_design_fundamentals.md#3. Database Architectures & Selection Framework]]*
