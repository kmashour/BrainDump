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
   - **Structured Domains:** For major engineering domains, prefix filenames with their domain index: `0-X_` for Kubernetes, `1-X_` for Systems Design, `2-X_` for Docker, `3-X_` for AWS, `4-X_` for BGP, `5-X_` for Jenkins, `6-X_` for Web, `7-X_` for Python, `8-X_` for Linux & OS, `9-X_` for GitHub Actions, `10-X_` for Terraform, `11-X_` for CloudOps, `12-X_` for CNCF, `13-X_` for Azure.
   - **MISC Chapters:** For multi-disciplinary projects or chapters combining multiple fields without a dedicated numeric domain (like Gitea), omit any sequence prefix and list them under the `MISC` section of index notes.
   - **Citations & URLs:** Carry forward and cite all scraped documentation URLs in the notes' references to satisfy the integrity audit script (`review_vault.py`).
4. **Header standard:** Ensure all code blocks specify syntax (e.g. `yaml`, `nginx`, `bash`, `python`).
