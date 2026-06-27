# Workspace Rules: Second Brain Assistant

## 🌐 Documentation & Sub-Link Scraping Rule
Whenever you ingest files (using `@ingest` or otherwise processing raw files in `inflow/`) that contain external documentation links (such as Kubernetes documentation, AWS whitepapers, database docs, etc.):
1. **Never Skip Scraping:** You MUST automatically identify, fetch, and scrape the body content of these URLs using standard scraping methods (e.g. executing the automatic scraper script `python3 "Reference Notes/scripts/scrape_docs.py" inflow/<file>.md` before beginning Phase 1).
2. **Scrape Sub-Links:** You MUST parse the fetched document to extract relevant sub-links (sub-sections, adjacent concepts, nested setting references) and recursively scrape those sub-links as well.
3. **Merge Before Refinement:** Combine the main URL text and all sub-link details with the inflow file's raw notes *before* starting Phase 1 (Refinement) of the multi-agent pipeline.
4. **Enforce Gating:** The verification script `review_vault.py` will automatically reject commits if documentation URLs inside inflow files are not cited and covered in the compiled vault.

## 🇸🇦 Multilingual Ingestion Rule (Arabic Transcripts)
Whenever raw material (such as transcripts or notes) inside `inflow/` is provided in Arabic:
1. **Translate to English:** You MUST translate the core technical concepts, configurations, and summaries to English during Phase 1 (Refinement) to align with the rest of the English vault.
2. **Preserve Terminology:** Keep standard technical keywords in English, and translate explanations, definitions, and contextual descriptions into high-quality technical English.
3. **Citations:** Note in the YAML frontmatter and in the reference notes that the source material was originally in Arabic, preserving a reference/link to the original source.

## 🌉 Evolutionary Conceptual Bridging Rule
Whenever you ingest, refine, or write notes regarding classical computing systems (e.g., UNIX kernel internals from classic books like Maurice Bach's *Design of the UNIX Operating System*) or evolving cloud infrastructures (e.g., AWS):
*   **Historical Trigger Constraint:** Only mention historical context if the inflow source is explicitly legacy/old content, or if a previously created modern note needs to be updated because a newly ingested inflow note introduces related historical context. Do NOT proactively inject legacy history into modern topics if the inflow source is entirely modern.
1. **Explain the Core Classic Concept:** Explain the fundamental concept, its original design parameters, and the technical intuition/insights behind it (e.g., UNIX inode tables, buffer cache, traditional fork-exec, or original eventual consistency models).
2. **Bridge the Gap to Modern Systems:** Explicitly bridge the gap to modern implementations, highlighting how it works today (e.g., Linux page cache, CFS/EEVDF process schedulers, copy-on-write `clone()` namespaces, or modern S3 strong consistency).
3. **Capture Evolutionary Constraints:** Document historical constraints and compare them with modern versions, capabilities, or replacements. This preserves the "why" behind the evolution of modern software architecture.

## 🎙️ Talks, Lectures & Video Ingestion Rule
Whenever an inflow note represents a talk, lecture, KubeCon/tech presentation, or video tutorial (identified by a YouTube/Vimeo source URL, timestamp structures in the body, or frontmatter containing fields like `type: talk`, `type: presentation`, or tag `clippings` from video sources):
1. **Isolate as Standalone:** You MUST compile the raw transcript content, Q&As, and presentation flow into a dedicated standalone reference note under `Reference Notes/` using the prefix of its respective domain (e.g., prefixing with `3-X` for AWS, `10-X` for Terraform, `12-X` for CNCF, etc.) and index it inside that domain's main Map of Content (MOC).
2. **Integrate Where it Belongs:** You MUST extract all configurations, architectural diagrams, commands, and conceptual definitions from the talk and integrate them into the relevant atomic conceptual notes in `Main Notes/`, project playbooks in `Projects/`, and structured reference modules in `Reference Notes/0-X...`.
3. **Dual Backlog Registration:** Document both the standalone file creation and the target note integrations in the transaction log (`backlog.md`).
