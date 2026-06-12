---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: language
domains:
  - "python"
related_concepts:
  - "[[programming/go]]"
against:
  - "[[programming/bash]]"
reference_guides:
  - "[[Reference Notes/7-Index - Python.md]]"
tags:
  - python/component
  - status/completed
---

# python

**Breadcrumbs:** [[0-Index|🏠 Index]] > Programming > **python**

---

## 🎯 Purpose (Why it is used)
Python is an interpreted, high-level, general-purpose programming language widely used for systems scripting, backend API development, data science, and automation.

---

## ⚙️ Functionality (What it is doing)
*   **Scripting & Automation:** Automates repetitive tasks.
*   **Backend APIs:** Powers web servers (Flask, Django, FastAPI).
*   **Package Distribution:** Manages dependencies via pip.

---

## 🏛️ Architectural Context
Python serves as the main language for scripting administrative utilities (e.g. CLI runners), automating cloud environments, and executing machine learning tasks.

---

## 🔍 Deeper Dive Notes
```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
