# SKILL: Inflow Refinement & Reference Notes Compilation

This skill outlines the process for refining raw inputs into structured Reference Notes.

---

## 📋 Execution Steps
1. **Raw Source Parsing:** Scan files in `inflow/` for technical transcripts, scraping logs, and the automatically generated `## 🌐 Scraped Reference Content` section (containing the crawled pages and sub-links).
2. **De-noising:**
   - Remove conversational fluff (e.g. "Welcome back", "In this video", "I passed interviews").
   - Consolidate repetitive descriptions.
   - Clean terminal prompt output junk while preserving command flags and inputs.
3. **Reference compilation:** Write clean markdown summaries inside `Reference Notes/` using the reference note template. Enforce topic-based splitting. 
   - **Structured Domains:** For major study tracks, prefix filenames with their domain index: `0-X_` for Kubernetes, `1-X_` for Systems Design, `2-X_` for future domains (like Terraform).
   - **MISC Chapters:** For projects or chapters combining multiple fields with no future history (like Gitea), omit any sequence prefix and list them under the `MISC` section of index notes.
   - **Citations & URLs:** Carry forward and cite all scraped documentation URLs in the notes' references to satisfy the integrity audit script (`review_vault.py`).
4. **Header standard:** Ensure all code blocks specify syntax (e.g. `yaml`, `nginx`, `bash`, `python`).
