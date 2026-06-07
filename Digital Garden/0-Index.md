---
obsidianUIMode: preview
class: index-note
tier: garden-note
tags:
  - architecture/garden-index
  - obsidian/moc
---

# 🌲 The Digital Garden: Architectural Patterns Index

This directory holds the connective patterns linking multiple study domains (Linux, AWS, Kubernetes, Databases, Networking).

---

## 🏛️ Architectural Patterns MOC
These pattern notes detail cross-domain integrations, performance trade-offs, and verification steps.

```dataview
TABLE domains AS "Domains", components AS "Connected Components", sources AS "Sources"
FROM "Digital Garden"
WHERE class = "pattern-note"
SORT file.name ASC
```
