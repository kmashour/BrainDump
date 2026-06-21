# Workspace Rules: Second Brain Assistant

## 🌐 Documentation & Sub-Link Scraping Rule
Whenever you ingest files (using `@ingest` or otherwise processing raw files in `inflow/`) that contain external documentation links (such as Kubernetes documentation, AWS whitepapers, database docs, etc.):
1. **Never Skip Scraping:** You MUST automatically identify, fetch, and scrape the body content of these URLs using standard scraping methods (e.g. executing the automatic scraper script `python3 "Reference Notes/scripts/scrape_docs.py" inflow/<file>.md` before beginning Phase 1).
2. **Scrape Sub-Links:** You MUST parse the fetched document to extract relevant sub-links (sub-sections, adjacent concepts, nested setting references) and recursively scrape those sub-links as well.
3. **Merge Before Refinement:** Combine the main URL text and all sub-link details with the inflow file's raw notes *before* starting Phase 1 (Refinement) of the multi-agent pipeline.
4. **Enforce Gating:** The verification script `review_vault.py` will automatically reject commits if documentation URLs inside inflow files are not cited and covered in the compiled vault.
