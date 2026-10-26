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

## 📚 Consolidated, Resource-Agnostic Knowledge Synthesis Protocol
1. **Source-Agnostic Unification:** All learning materials—whether structured video courses (e.g., KodeKloud), multi-part lecture playlists (e.g., Moe Intelligence), official vendor documentation, or whitepapers—are treated as uniform technical inputs. Do NOT create redundant standalone digest notes (e.g., `-V` summary files) for courses or multi-part lecture playlists.
2. **One Canonical Reference Note Per Topic:** Every technical concept belongs in its canonical topic reference note (e.g., `13-104-02_administer_identity.md`). When ingesting additional resources:
   - If a concept is already covered, corroborate and deepen the existing explanations in-place.
   - If new operational nuances, step-by-step portal workflows, CLI recipes, or troubleshooting gotchas are introduced, integrate or append them directly into the target note.
3. **Deep Comprehension & First-Principles Articulation:** Notes must NOT be shallow exam-cram checklists. They must thoroughly explain the intuitive "why", internal mechanics, architectural trade-offs, real-world deployment decisions, and diagnostic failure loops (AARF) to enable deep comprehension and professional solution articulation, not just passing exams.
4. **Standalone Notes Strictly for Independent Landmark Talks:** Only isolate video material into a standalone reference note if it is a single, self-contained landmark keynote, conference presentation, or whitepaper review (e.g., Netflix Cloud-Native Authorization) that does not map into an existing curriculum module.

## 🌍 Universal Multi-Technology Scope & Consolidated Kubernetes Rule
1. **Multi-Domain Equality:** The Agentic system serves **all knowledge and technologies** (Linux OS & Kernel, AWS, Azure, GCP, Networking/BGP, Terraform/IaC, CI/CD, Databases, Distributed Systems, Web Fundamentals, Python).
2. **Kubernetes as a Consolidated Topic:** Kubernetes is treated as a single consolidated engineering domain among its peer domains.
3. **Certification Tracks as Overlays:** Segregations like CKA, CKAD, CKS, and KubeAstronaut (or AWS SAA/SAP, Red Hat RHCSA) exist *strictly* as Layer 2 certification overlays for exam-specific checklists and speed shortcuts, built on top of the consolidated Core Foundation Notes.

## 🚫 No Automatic Project Generation Rule (Collaborative Projects & Contextual PoCs Only)
1. **Stop Automatic Project File Creation:** You MUST NOT automatically generate, compile, or dump standalone project playbook files into the `Projects/` directory during ingestion, research, or pipeline runs.
2. **Contextual Proof of Concepts (PoCs):** All Proof of Concepts, verification manifests (YAML, Terraform, Dockerfile), diagnostic CLI recipes, and failure-loop scenarios MUST be embedded directly within the explanation context of the target note under `Reference Notes/` or delivered interactively in chat.
3. **Collaborative Project Workspace:** The `Projects/` directory is reserved for manual user management and collaborative projects built *together with the user* on demand. Standalone project files in `Projects/` are only created when the user explicitly requests to build a project together.

## 🧠 Conversational Explanations to Main Notes Protocol
Whenever the user requests to save a conceptual explanation from chat as a Main Note:
1. **Fidelity Without Clutter:** Formulate the explanation adhering strictly to what was explained in the conversation, without adding unsolicited extra content or deviating from the discussion.
2. **Landing Note & Deeper Note Hierarchy:**
   - Link or create the parent concept's **Landing Note** (`class: landing-note`) in `Main Notes/` indexed in `Main Notes/0-Index.md`.
   - The detailed explanation becomes a **Deeper Dive Note** (`class: deeper-dive`) using `parent_concept: "[[Landing Note Name]]"`.
3. **Strict User Request Gate for Extra Practical Aspects:**
   - Deeper notes covering additional aspects, edge cases, or extra practical examples MUST ONLY be added **when the user explicitly asks and instructs to do so**. Never proactively generate extra auxiliary deeper dive notes unless requested.

## 🎓 Layer 2 Certification Overlay Protocol (Advanced & Specialty Tracks)
Whenever expanding the Second Brain to cover higher-level or specialized certifications (such as AZ-305 Solutions Architect, AZ-700 Network Engineer, AZ-500 Security Engineer, or SC-300 IAM Administrator):
1. **Reference-First Bedrock:** NEVER duplicate foundational explanations or re-explain core concepts already documented in foundational notes (e.g., the canonical AZ-104 reference notes). Always link back to and build upon the existing canonical notes using explicit WikiLinks.
2. **Specialized Architectural Deltas:** Only document new specialized topics, advanced protocol internals, high-level design decision matrices, and capacity planning formulas that go beyond the foundational tier.
3. **Targeted Deep Dives:** Conduct deep dives only on topics unique to the higher-tier certification (e.g., advanced hybrid routing, complex multi-region failover topologies, zero-trust cryptographic architectures).
4. **Exam-Specific Tactical Overlay:** Provide targeted speed checklists, exam-specific gotchas, scenario decision trees, and case study blueprints without cluttering the foundational core.

