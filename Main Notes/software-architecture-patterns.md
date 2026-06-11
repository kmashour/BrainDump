---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "infra"
  - "database"
related_concepts:
  - "[[distributed-communication]]"
  - "[[api-protocols]]"
against:
  - "[[distributed-communication]]"
  - "[[api-protocols]]"
reference_guides:
  - "[[Reference Notes/1-7_software_architecture_patterns.md]]"
tags:
  - system-design/architecture
  - status/completed
---

# Software Architecture Patterns

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **Software Architecture Patterns**

---

## 🎯 Purpose (Why it is used)
Software Architecture Patterns provide structured templates and blueprint topologies for organizing codebase components, data ownership, deployment boundaries, and communication paths in software systems. They help guide teams on code distribution, operational scaling, fault isolation, and deployment workflows.

---

## ⚙️ Functionality (What it is doing)
- **Structuring Codebases:** Defines the packaging and logical separation of code (e.g., layers in Clean Architecture, modules in Modular Monolith).
- **Defining Data Ownership:** Dictates how databases and tables are structured and accessed (e.g., shared database in Monolith, service-private database in Microservices, separate write/read DBs in CQRS).
- **Determining Deployment Boundaries:** Establishes compile-time and runtime release packaging (e.g., single process binary in Monoliths, ephemeral trigger containers in Serverless, isolated microservices).
- **Structuring Communication:** Sets up inter-component connection styles (e.g., blocking in-process calls, network RPCs, async message broker routing).

---

## 🏛️ Architectural Context (How it fits in the architecture)
Architecture patterns form the macro-structural skeleton of the entire application suite. They determine how teams are organized (e.g., DDD bounded contexts mapped to teams), how services coordinate (e.g., Event-Driven Architecture), and how legacy code is refactored and modernized (e.g., Strangler Fig Pattern).

---

## 🧩 Problem Solver (What problem it solves)
- **Codebase Degradation:** Prevents modular boundary breakdown (spaghetti code) through architectural constraints.
- **Scaling Bottlenecks:** Solves resource scaling limitations by decomposing systems into independently scalable units (Microservices, Serverless).
- **Organizational Coupling:** Resolves deployment blocking and team coordination bottlenecks by providing service boundaries and independent release cycles.
- **Framework and Vendor Lock-in:** Isolates core business logic from database and network libraries (Clean Architecture).

---

## 🟢 Operational Impact (What will happen with it operating)
Systems benefit from isolated deployments, reduced blast radiuses for bugs, clearer boundaries for teams, and the ability to scale specific application bottlenecks independently, enhancing performance and availability.

---

## 🔴 Failure Impact (What will happen without it)
Without proper architecture planning, codebases devolve into a "Big Ball of Mud" with high coupling, making changes risky, releases slow, and debugging difficult. Operational bottlenecks in one module will exhaust system resources and trigger cascading outages across unrelated business domains.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Software Architecture Patterns**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[software-architecture-patterns]]
SORT file.name ASC
```
