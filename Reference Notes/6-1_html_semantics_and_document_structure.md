---
domains:
  - "web-fundamentals"
---

# Module 6-1: HTML Semantics & Document Structure

This module covers the core semantics and structural requirements of HTML5 documents.

---

## 1. HTML5 Semantic Layout Elements

Semantic elements define the meaning of the content structure to both the browser and search engines.
*   **Semantic Tags:** `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<footer>`.
*   **Accessibility:** Screen readers parse semantic tags to navigate pages efficiently.

---

## 2. Element Nesting Constraints

#### Deep-Intuition (AARF) Breakdown:
1. **The Answer (Core Pattern):** Adhere strictly to the HTML5 nesting schema. Never nest block-level elements inside inline elements:
    ```html
    <!-- Correct -->
    <a href="/link"><span class="highlight">Click here</span></a>
    
    <!-- Incorrect -->
    <span class="btn"><div class="content">Block text</div></span>
    ```
2. **The Assumptions (Context):** Browsers attempt to fix nested schema errors automatically, but they interpret layout blocks differently.
3. **The Rationale (Why):** Block-level elements (`<div>`, `<p>`) take up the full available width, while inline elements (`<span>`, `<a>`) take up only the width of their content. Nesting blocks inside inlines breaks CSS rendering models.
4. **The Failure Loop (What if not):** Browsers encountering block-level tags nested inside inline tags break the DOM tree. The browser terminates the inline tag prematurely, causing CSS selectors and parent-child selectors to fail.
5. **Alternative Case (When to use 'if not'):** In HTML5, the anchor tag (`<a>`) is a rare exception that can wrap block-level containers (like a whole card `<div>`), provided it does not contain other interactive elements (like other buttons).
