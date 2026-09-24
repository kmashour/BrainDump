# SKILL: Universal Ingestion Pipeline Orchestration

This skill details how to manage the end-to-end execution of the multi-agent ingestion pipeline across all engineering domains.

---

## 📋 Execution Steps
1. **Analyze & Scrape Input File:**
   - Scan the target file in `inflow/` for any external documentation URLs.
   - Automatically execute the scraper: `python3 "Reference Notes/scripts/scrape_docs.py" inflow/<filename>.md` to fetch and scrape the target URLs and their sub-links.
   - Confirm that the scraped content is successfully appended under `## 🌐 Scraped Reference Content` inside the inflow note before proceeding.
   - Identify primary domains across the 14 vault domains (`0-X` Kubernetes through `13-X` Azure, and `MISC`).
   - Identify if it relates to a certification track (e.g. CKA, CKS, CKAD, AWS SAA/SAP, RHCSA, AZ-104).
2. **Execute Phase 1 (Refinement) & Phase 2 (Audit):**
   - Delegate to ResearchAgent to enrich existing Core Reference Notes or compile new modular Reference Notes using the domain prefixing convention (`0-X` through `13-X`).
   - Delegate to AuditAgent to enrich secondary/tangent domains and include Evolutionary Bridges when historical content is present.
3. **Execute Phase 2.5 (Diagram Design):**
   - Delegate to DiagramAgent to design and insert standard-compliant Mermaid diagrams.
4. **Execute Phase 3 (Contextual PoC Integration):**
   - Delegate to MultiDomainPoCAgent to integrate practical Proof of Concept configurations, declarative manifests, verification commands, and failure-loop test cases **directly within the Reference Note**.
   - **Strictly prohibit** generating standalone project files under `Projects/`. (The `Projects/` directory is reserved for collaborative, co-authored builds with the user).
5. **Execute Phase 4 (Garden Intersections):**
   - Map E2E cross-domain patterns in `Digital Garden/`.
6. **Execute Phase 5 (Atomic Concept Notes):**
   - Update or create atomic landing and deeper-dive notes in `Main Notes/`.
7. **Execute Phase 6 (Exam Focus / Certification Synthesis):**
   - If relevant to an exam track (e.g. CKA, CKS, CKAD, AWS SAA/SAP, RHCSA), invoke ExamAgent to update the dedicated exam MOC (`Reference Notes/0-Index - <CERT>.md`) and exam study guides, linking back to the enriched Core Notes.
8. **Verify & Sync:**
   - Run `python "Reference Notes/scripts/review_vault.py"`.
   - Write a detailed transaction log in `backlog.md`.
   - Commit and push to `origin main`.

