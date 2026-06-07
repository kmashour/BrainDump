# SKILL: Ingestion Pipeline Orchestration

This skill details how to manage the end-to-end execution of the multi-agent ingestion pipeline.

---

## 📋 Execution Steps
1. **Analyze Input File:**
   - Scan the target file in `inflow/`.
   - Identify the primary domains (e.g. `kubernetes`, `aws`, `networking`, `database`).
   - Identify if it belongs to an active study/exam track (e.g. CKA).
2. **Execute Phase 1 (Refinement) & Phase 2 (Audit):**
   - Delegate to ResearchAgent to compile the Reference Note.
   - Delegate to AuditAgent to enrich secondary/tangent domains.
3. **Execute Phase 2.5 (Diagram Design):**
   - Delegate to DiagramAgent to design and insert standard-compliant Mermaid diagrams.
4. **Execute Phase 3 (PoC Playbooks):**
   - For general system design / cloud architecture: package configurations and CLI recipes as a standalone project under `Projects/` and replace inline configs with wiki-links.
   - For Kubernetes: maintain validation configurations and CLI playbooks linked to cluster setups.
5. **Execute Phase 4 (Conceptual Main Notes) & Phase 5 (Garden Intersections):**
   - Create/update Landing Notes and Deeper Notes in `Main Notes/`.
   - Map E2E cross-domain patterns in `Digital Garden/`.
6. **Execute Phase 6 (Exam Focus / Certification Checklists):**
   - **Mandatory for Kubernetes/CKA:** Invoke CKAExamAgent to compile/append exam-focused checklists, aliases, VIM tricks, and diagnostic scripts to the appropriate checklist under `Projects/CKA/`.
7. **Verify & Sync:**
   - Run the vault review script.
   - Write a detailed transaction log in `backlog.md`.
   - Push to `origin main`.
