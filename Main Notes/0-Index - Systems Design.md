---
obsidianUIMode: preview
class: index-note
tier: main-note
tags:
  - system-design/index
  - obsidian/moc
---

# 📐 Systems Design MOC

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > **Systems Design MOC**

---

## 🖥️ Distributed Systems Design & Infrastructure
*Foundational scaling paradigms, database selection schemas, distributed CDNs, caching topologies, and external API gateways.*

```dataview
TABLE related_concepts AS "Related Concepts", reference_guides AS "Reference Guides"
FROM "Main Notes"
WHERE class = "landing-note" AND role = "infra" AND (contains(domains, "database") OR contains(domains, "networking") OR contains(domains, "infra") OR contains(domains, "security") OR contains(domains, "system-design"))
SORT file.name ASC
```
