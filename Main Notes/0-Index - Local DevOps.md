---
obsidianUIMode: preview
class: index-note
tier: main-note
tags:
  - devops/index
  - obsidian/moc
---

# 🐙 Local DevOps & GitOps MOC

**Breadcrumbs:** [[0-Index|🏠 Index]] > **Local DevOps & GitOps MOC**

---

## 🐙 GitOps & Local Infrastructure
*Self-hosted git servers, automated runner CI/CD environments, and local cluster administration.*

```dataview
TABLE related_concepts AS "Related Concepts", reference_guides AS "Reference Guides"
FROM "Main Notes"
WHERE class = "landing-note" AND (role = "gitops" OR contains(file.name, "gitea"))
SORT file.name ASC
```

---

## 🛠️ Developer Tooling & Introspection
*Introspection clients, configuration contexts, and system-interaction shell wrappers.*

```dataview
TABLE related_concepts AS "Related Concepts", reference_guides AS "Reference Guides"
FROM "Main Notes"
WHERE class = "landing-note" AND role = "client-tool"
SORT file.name ASC
```
