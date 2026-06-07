---
obsidianUIMode: preview
class: index-note
tier: main-note
tags:
  - kubernetes/index
  - obsidian/moc
---

# 🏠 Second Brain Conceptual Index

Welcome to the central conceptual landing page. To ensure atomic segregation and prevent subdomain mixing, the conceptual Map of Content (MOC) is divided into topic-specific index notes.

Select a domain to view its active landing concepts, deeper dive notes, and architectural structures:

---

### ☸️ [Kubernetes Concepts MOC](0-Index%20-%20Kubernetes.md)
*Control plane orchestrators, worker node mechanics, container runtimes, scheduling workloads, configuration components, storage mounts, and network policies.*
- **Go to MOC:** [[0-Index - Kubernetes|Kubernetes MOC]]

---

### 📐 [Systems Design MOC](0-Index%20-%20Systems%20Design.md)
*Distributed scaling frameworks, database selector models, caching write topologies, geographical CDN edge nodes, and API communication protocols/security.*
- **Go to MOC:** [[0-Index - Systems Design|Systems Design MOC]]

---

### 🐙 [Local DevOps & GitOps MOC](0-Index%20-%20Local%20DevOps.md)
*Self-hosted source control setups, automated runner contexts, dev environments, and CLI introspection/diagnostic tools.*
- **Go to MOC:** [[0-Index - Local DevOps|Local DevOps & GitOps MOC]]

---

## 🔍 Deeper-Dive Architectural Focus Notes
*A consolidated index of all deep architectural dive notes, use cases, and technical pitfalls across the vault.*

```dataview
TABLE parent_concept AS "Component", sub_type AS "Type", tags AS "Tags"
FROM "Main Notes"
WHERE class = "deeper-dive"
SORT parent_concept ASC, file.name ASC
```

---

## 🏛️ Architectural Patterns (Digital Garden)
*Connective pattern notes mapping intersections between multiple domains (e.g. Linux kernel hooks, AWS, Kubernetes namespaces) in production.*

```dataview
TABLE domains AS "Domains", components AS "Components", sources AS "Sources"
FROM "Digital Garden"
WHERE class = "pattern-note"
SORT file.name ASC
```
