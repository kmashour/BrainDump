---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
  - "database"
related_concepts:
  - "[[aws]]"
against:
  - "[[Amazon RDS]]"
reference_guides:
  - "[[Reference Notes/3-19_databases_analytics_ml.md]]"
tags:
  - aws/neptune
  - database/graph
  - status/completed
---

# Amazon Neptune

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **Amazon Neptune**

---

## 🎯 Purpose (Why it is used)
Amazon Neptune is a fast, reliable, fully managed graph database service optimized for storing and querying highly connected datasets. It supports popular graph models (Property Graph and W3C's RDF) and their respective query languages (Gremlin and SPARQL), enabling applications to query complex relationships with millisecond latency.

---

## ⚙️ Functionality (What it is doing)
*   **Graph Query Processing:** Evaluates complex relational networks without requiring expensive SQL JOIN operations.
*   **Multi-AZ Deployment:** Replicates data across multiple Availability Zones, offering high availability and supporting up to 15 low-latency read replicas.
*   **Neptune Streams:** Captures real-time changes to the graph dataset to trigger Lambda functions or synchronize external systems.
*   **W3C and Property Graph Support:** Enables standard Gremlin, openCypher, and SPARQL queries.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Neptune serves as the database engine for applications built on relationship maps (e.g., social feeds, fraud ring tracking, identity resolution engines, or recommendation engines). Frontend APIs query Neptune to load node connections dynamically.

---

## 🧩 Problem Solver (What problem it solves)
Querying highly nested relationships (like "friends-of-friends" or tracking indirect financial transfers in fraud detection) in SQL databases requires multiple JOIN commands that degrade database performance. Neptune solves this by storing relationships as direct pointers (edges) between data points (nodes), allowing fast traversal of connections.

---

## 🟢 Operational Impact (What will happen with it operating)
Graph traversals execute with consistent, single-digit millisecond latency. The database scales storage up to 64 TB automatically, and replicas handle query loads without impacting write performance.

---

## 🔴 Failure Impact (What will happen without it)
Without Neptune, developers must map graph relationships onto relational tables (resulting in slow JOIN operations and complex queries) or self-manage open-source graph databases (like Neo4j) on EC2, which introduces high administrative overhead.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Amazon Neptune**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
