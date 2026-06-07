---
obsidianUIMode: preview
class: index-note
tier: main-note
tags:
  - kubernetes/index
  - obsidian/moc
---

# 🏠 Kubernetes Conceptual Index (Map of Content)

Welcome to the central landing page for the **Main Notes** of your Kubernetes Knowledge Base. This index is dynamically populated using the **Dataview** plugin.

---

## 🏛️ Control Plane (The Brains)
Core components running on the master nodes that manage cluster state, scheduling, and configuration.

```dataview
TABLE related_concepts AS "Related Concepts", reference_guides AS "Reference Guides"
FROM "Main Notes"
WHERE class = "landing-note" AND role = "control-plane"
SORT file.name ASC
```

---

## 💪 Worker Node Mechanics (The Muscle)
Daemons and environments running on every node to execute containerized workloads and route network traffic.

```dataview
TABLE related_concepts AS "Related Concepts", reference_guides AS "Reference Guides"
FROM "Main Notes"
WHERE class = "landing-note" AND role = "worker-node"
SORT file.name ASC
```

---

## 🧩 Workloads & Infrastructure
The foundational building blocks of applications and compute resources in the cluster.

```dataview
TABLE related_concepts AS "Related Concepts", reference_guides AS "Reference Guides"
FROM "Main Notes"
WHERE class = "landing-note" AND role = "workload"
SORT file.name ASC
```

---

## 🖥️ Systems Design & Core Infrastructure
Foundational architecture, database engines, traffic routing, and core security controls.

```dataview
TABLE related_concepts AS "Related Concepts", reference_guides AS "Reference Guides"
FROM "Main Notes"
WHERE class = "landing-note" AND role = "infra"
SORT file.name ASC
```

---

## 🛠️ Tooling & Interfaces
Command-line tools and utilities used to inspect and interact with the Kubernetes API.

```dataview
TABLE related_concepts AS "Related Concepts", reference_guides AS "Reference Guides"
FROM "Main Notes"
WHERE class = "landing-note" AND role = "client-tool"
SORT file.name ASC
```

---

## 🔍 All Deeper Dive Notes
A consolidated index of all deep architectural, use case, and pitfall notes across the vault.

```dataview
TABLE parent_concept AS "Component", sub_type AS "Type", tags AS "Tags"
FROM "Main Notes"
WHERE class = "deeper-dive"
SORT parent_concept ASC, file.name ASC
```

---

## 🏛️ Architectural Patterns
Connective notes documenting how multiple concepts across domains (e.g. Linux, AWS, Kubernetes) come together in production.

```dataview
TABLE domains AS "Domains", components AS "Components", sources AS "Sources"
FROM "Digital Garden"
WHERE class = "pattern-note"
SORT file.name ASC
```

---

> [!TIP] Obsidian Navigation Tip
> This MOC updates automatically. When you create a new note, make sure it has the correct frontmatter attributes (`class`, `role`, `parent_concept`, etc.) so it displays in these tables.
