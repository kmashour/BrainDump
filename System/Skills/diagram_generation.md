# SKILL: Mermaid.js Diagram Generation & Standards

This skill details how to design and insert strict-compliant Mermaid diagrams into markdown notes.

---

## 📋 Standard Guidelines
1. **Direction:** Use `graph TD` (top-down) or `graph LR` (left-to-right).
2. **Quoting Labels:** Always quote node labels containing spaces, parentheses, slashes, or special characters.
   - *Correct:* `A["My Node (details)"]`
   - *Incorrect:* `A[My Node (details)]`
3. **Ampersand Restriction:** NEVER use raw `&` inside label strings. Strictly replace with the word "and".
4. **List Collisions:** Do not start node labels with list numbers (e.g. `1. Node`). Use text indicators (e.g., `Step 1: Node`) to prevent Markdown parsers from breaking formatting.
5. **Strategic Subgraphs:** Use subgraphs to define clear boundaries (e.g. namespaces, node bounds, or network zones).
