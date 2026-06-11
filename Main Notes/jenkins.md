---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: client-tool
domains:
  - "jenkins"
related_concepts:
  - "[[github-actions]]"
against:
  - "[[gitlab-ci]]"
reference_guides:
  - "[[Reference Notes/5-Index - Jenkins.md]]"
tags:
  - jenkins/component
  - status/completed
---

# jenkins

**Breadcrumbs:** [[0-Index|🏠 Index]] > CI/CD > **jenkins**

---

## 🎯 Purpose (Why it is used)
Jenkins is an open-source automation server designed to orchestrate CI/CD pipelines, automating software compilation, testing, and deployment stages.

---

## ⚙️ Functionality (What it is doing)
*   Orchestrates build executions across distributed Agents.
*   Triggers pipelines via webhook notifications.
*   Publishes artifacts and tracks test reports (JUnit).

---

## 🏛️ Architectural Context
Jenkins operates as the core execution hub inside development teams, connecting Version Control Systems (GitHub) to deployable targets (Kubernetes, AWS).

---

## 🔍 Deeper Dive Notes
```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[jenkins]]
SORT file.name ASC
```
