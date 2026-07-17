---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: language
domains:
  - "web-fundamentals"
related_concepts:
  - "[[programming/javascript]]"
against:
  - "[[infra/backend]]"
reference_guides:
  - "[[Reference Notes/6-Index - Web Fundamentals.md]]"
tags:
  - web/component
  - status/completed
---

# web-fundamentals

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Programming > **web-fundamentals**

---

## 🎯 Purpose (Why it is used)
Web Fundamentals cover the building blocks of the web platform: HTML for document structure and content semantics, and CSS for page styling, layouts, and typography.

---

## ⚙️ Functionality (What it is doing)
*   **HTML Structure:** Structures content semantics using standard HTML5 tags.
*   **CSS Presentation:** Enforces layouts using the Box Model, Flexbox, and Grid.
*   **Accessibility:** Implements accessible document hierarchies.

---

## 🏛️ Architectural Context
Web Fundamentals provide the foundation for client-side rendering engines (browsers) to parse and render application user interfaces.

---

## 🔍 Deeper Dive Notes
```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
