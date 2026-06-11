---
domains:
  - "web-fundamentals"
---

# Module 6-2: CSS Box Model & Inheritance

This module details CSS spacing, relative units, and inheritance primitives.

---

## 1. The CSS Box Model

Every HTML element is rendered as a rectangular box.

```
+---------------------------------------+
|  Margin (Outside spacing)             |
|   +-------------------------------+   |
|   |  Border                       |   |
|   |   +-----------------------+   |   |
|   |   |  Padding (Inside)     |   |   |
|   |   |   +---------------+   |   |   |
|   |   |   |  Content      |   |   |   |
|   |   |   +---------------+   |   |   |
|   |   +-----------------------+   |   |
|   +-------------------------------+   |
+---------------------------------------+
```

*   **Content:** The actual text or images.
*   **Padding:** Spacing around the content, inside the border.
*   **Border:** The edge wrapper.
*   **Margin:** Spacing outside the border, pushing other elements away.

---

## 2. CSS Units and Inheritance

#### Deep-Intuition (AARF) Breakdown:
1. **The Answer (Core Pattern):** Utilize relative units (`rem`, `em`) for typography and margins, and declare global resets for box-sizing:
    ```css
    * {
      box-sizing: border-box;
    }
    html {
      font-size: 16px;
    }
    body {
      font-size: 1rem;
    }
    ```
2. **The Assumptions (Context):** `rem` is relative to the root `<html>` font-size, while `em` is relative to the font-size of the element itself.
3. **The Rationale (Why):** Relative typography enables accessibility scaling. If a user increases the default browser font-size, `rem`-based pages scale proportionally. `border-box` includes padding and borders inside the element's defined width, simplifying layout calculations.
4. **The Failure Loop (What if not):** Using default `content-box` calculations means an element defined with `width: 100%` and `padding: 10px` expands to `100% + 20px`, overflowing container boundaries and breaking grid layouts.
5. **Alternative Case (When to use 'if not'):** Use absolute pixel units (`px`) for thin borders or UI elements that must not scale under any user accessibility overrides.
