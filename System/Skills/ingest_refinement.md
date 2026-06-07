# SKILL: Inflow Refinement & Reference Notes Compilation

This skill outlines the process for refining raw inputs into structured Reference Notes.

---

## 📋 Execution Steps
1. **Raw Source Parsing:** Scan files in `inflow/` for technical transcripts or scraping logs.
2. **De-noising:**
   - Remove conversational fluff (e.g. "Welcome back", "In this video", "I passed interviews").
   - Consolidate repetitive descriptions.
   - Clean terminal prompt output junk while preserving command flags and inputs.
3. **Reference compilation:** Write clean markdown summaries inside `Reference Notes/` using the reference note template.
4. **Header standard:** Ensure all code blocks specify syntax (e.g. `yaml`, `nginx`, `bash`, `python`).
