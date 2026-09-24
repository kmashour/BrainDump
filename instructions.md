# SKILL: Universal Multi-Technology Ingestion & Vault Restructuring

## Objective
This skill provides a systematic protocol for parsing new study transcripts, documentation dumps, and technical books across **all engineering domains** (Linux, Cloud, Kubernetes, Systems Design, Networking, IaC, CI/CD, Databases), incorporating them into the consolidated Second Brain knowledge base, and formatting them for Obsidian graphs with rigorous architectural separation.

## Trigger
Execute this skill when:
1. New study material, transcripts, or documentation dumps are added to the `inflow/` directory.
2. Conceptual definitions require updates, link adjustments, or structural changes.
3. The user requests a review of the vault integrity using the `@review` keyword in their message.
4. The user requests ingestion of a file or URL index list using the `@ingest` keyword in their message.

---

## 0.1 Inflow Scraping Protocol (Mandatory)
Whenever the `@ingest` trigger is run or files containing documentation URLs are added:
1. **Scrape Before Refinement:** You MUST execute the automatic document crawler and scraper:
   `python3 "Reference Notes/scripts/scrape_docs.py" inflow/<filename>.md`
   This script fetches the main URL and its relevant sub-links, converts HTML to structured markdown, and appends them under `## 🌐 Scraped Reference Content` at the end of the inflow file.
2. **Include Citations:** The ResearchAgent MUST process this scraped section to construct reference notes and main notes, ensuring all links are fully cited.
3. **Audit Compliance:** The `review_vault.py` verification script will raise a hard failure if any documentation URLs present in the inflow notes are missing from the vault notes' references.

---

## 1. Directory Structure & File Organization

The knowledge base is structured as follows:
- `README.md`: The central index and high-level visual Mermaid.js "Universal Brain Map" connecting all engineering domains.
- `instructions.md`: This file (the Universal Ingestion Skill).
- `backlog.md`: The transaction log containing every update, change, and addition to the knowledge base.
- `inflow/`: A landing zone for raw lecture transcripts, documentation dumps, and external notes before consolidation.
- `Reference Notes/`: Authoritative, modular reference guides (`0-X` through `13-X` and `MISC`) with embedded contextual PoCs. Contains `Reference Notes/--Index--.md` (central index of all domains).
- `Main Notes/`: Atomic, conceptual summaries (Landing Notes and Deeper Notes). Contains `Main Notes/0-Index.md` (dynamic index of all landing and deeper notes).
- `Digital Garden/`: Connective architectural patterns and cross-domain connections. Contains `Digital Garden/0-Index.md` (dynamic index of patterns).
- `Projects/`: Collaborative workspace for co-authored projects built *together with the user* on demand, alongside dedicated certification tracks (e.g. `Projects/CKA/`, `Projects/CKS/`). **Standalone project files are never automatically generated.**

---

## 1.1 Team of Specialized Agents

The specialized subagents and their profiles are defined in the `System/Agents/` directory:
- **OrchestrationAgent:** [orchestrator.md](System/Agents/orchestrator.md) (Universal Pipeline Manager & Coordinator)
- **ResearchAgent:** [researcher.md](System/Agents/researcher.md) (Inflow Refinement & Core Reference Compiler)
- **AuditAgent:** [auditor.md](System/Agents/auditor.md) (Context Auditor & Evolutionary Tangent Expander)
- **DiagramAgent:** [diagrammer.md](System/Agents/diagrammer.md) (Mermaid.js Concept Designer)
- **MultiDomainPoCAgent:** [poc_developer.md](System/Agents/poc_developer.md) (Contextual In-Note PoC Developer & Collaborative Builder)
- **LabArchitectAgent:** [lab_architect.md](System/Agents/lab_architect.md) (In-Note Hands-on Lab Compiler & AARF Failure Simulator)
- **GardenAgent:** [garden_architect.md](System/Agents/garden_architect.md) (Cross-Domain Connection & Pattern Architect)
- **ExamAgent:** [exam_expert.md](System/Agents/exam_expert.md) (Certification checklist & speed-optimization expert)

---

## 2. Ingestion & Consolidation Workflow

The ingestion pipeline is standardized across all domains and orchestrated sequentially. Refer to the central [workflow.md](workflow.md) file in the root directory for:
- Phase-by-phase breakdown of the pipeline (Phase 1 to Phase 6).
- Mapping of agents and skills for each phase.
- Git synchronization and logging procedures.

All templates used during the ingestion workflow are stored in the `System/Templates/` directory.

---

## 3. Structure Templates for Notes

### A. Main Notes: Landing Note Template
Every landing note inside `Main Notes/` must contain the following frontmatter and sections:
```markdown
---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: <control-plane | worker-node | workload | client-tool | infra | network | language>
domains:
  - "kubernetes" # e.g. kubernetes, linux, aws, database, networking
related_concepts:
  - "[[concept-a]]"
against:
  - "[[opposing-concept]]" # Simple list of links to alternative/opposing approaches
reference_guides:
  - "[[Reference Notes/Reference_File.md]]"
tags:
  - kubernetes/component
  - status/completed
---

# <concept-name>

**Breadcrumbs:** [[0-Index|🏠 Index]] > <Layer> > **<concept-name>**

---

## 🎯 Purpose (Why it is used)
[Explain why this component exists and what role it plays in the cluster/system.]

---

## ⚙️ Functionality (What it is doing)
[List specific tasks, operations, and services this component performs.]

---

## 🏛️ Architectural Context (How it fits in the architecture)
[Describe its placement, who it talks to, and who talks to it.]

---

## 🧩 Problem Solver (What problem it solves)
[Describe what issues arise if this component is absent vs what it solves.]

---

## 🟢 Operational Impact (What will happen with it operating)
[Describe how the cluster/system behaves normally with this component active.]

---

## 🔴 Failure Impact (What will happen without it)
[Detail the exact consequences of this component failing or crashing.]

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **<concept-name>**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[<concept-name>]]
SORT file.name ASC
```
```

### B. Main Notes: Deeper Note Template
Deeper notes are atomic, modular files covering specific use cases, core concepts, or pitfalls. Every deeper note inside `Main Notes/` should follow this format:
```markdown
---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[<landing-concept-name>]]"
sub_type: <core-concept | architecture | use-case | pitfall>
source_type: <gemini-chat | youtube | udemy | newsletter | book | documentation>
source_url: "https://..."
author: "<author or instructor name>"
course_title: "<course or book title>"
tags:
  - kubernetes/<landing-concept-name>
  - kubernetes/deep-dive
---

# <landing-concept-name> - <deeper-aspect-name>

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[<landing-concept-name>]] > **<deeper-aspect-name>**

---

## 📑 [Sub-Topic Name]
[Detail the technical concepts, code configs, or command logs.]

*Read more in [Reference_File.md](../Reference%20Notes/Reference_File.md#heading)*
```

### C. Main Notes: Architectural Pattern Note Template
Pattern notes document the "connective tissue" of the Second Brain, describing how multiple concepts across different domains combine in production.
```markdown
---
obsidianUIMode: preview
class: pattern-note
tier: main-note
domains:
  - "aws"
  - "kubernetes"
  - "database"
components:
  - "[[pod]]"
  - "[[node]]"
  - "[[etcd]]"
sources:
  - "AWS EKS Whitepaper"
tags:
  - architecture/pattern
---

# Pattern: <pattern-name>

**Breadcrumbs:** [[0-Index|🏠 Index]] > Patterns > **<pattern-name>**

---

## 🏛️ Architectural Context
[Detail how the components come together, their interaction flows, and network paths.]

---

## ⚖️ Trade-offs & Alternatives
[Describe the pros and cons of this design compared to alternatives listed in the 'against' properties.]

---

## 🛠️ Verification & Practical Implementation
[Link to reference notes and list terminal command formulas or configs.]
```

### D. Reference Notes Template
Reference notes retain their modular formatting, prioritizing:
- Extensive architectural breakdowns, protocol deep dives, and production-grade configurations.
- Practical step-by-step contextual Proof of Concept (PoC) workflows embedded directly within the note under `## 🛠️ Verification & Practical Implementation` or `## 🧪 Hands-on Proof of Concept / Lab Simulation`.
- In-depth failure loop reproductions, capturing exact error messages and recovery actions.
- Exam and certification tips highlighted in alert boxes (`> [!TIP]`, `> [!IMPORTANT]`, etc.).
- Prohibiting automatic generation of standalone files in `Projects/`; all PoCs belong in the explanation context unless building a collaborative project with the user.

### E. Deep-Intuition Documentation Style (AARF Extension)
To give vault knowledge maximum volume and diagnostic depth, the research and audit engines must extend Q&As, scenario solutions, and study files with the AARF framework across all engineering domains:
1. **The Answer (Core Config):** Explicit command lines, dry-run formulas, or YAML/HCL/Python manifests.
2. **The Assumptions (Context):** Prerequisites, OS/kernel dependencies, cluster version skew constraints, namespace scope, or runtime config dependencies.
3. **The Rationale (Why):** System-level architecture explanation (why the OS, cloud provider, or orchestrator behaves this way under the hood).
4. **The Failure Loop (What if not):** The exact error message, kernel log event, pod CrashLoop state, HTTP 5xx code, or security warning if omitted/misconfigured.
5. **Alternative Case (When to use 'if not'):** Real-world production cases when the opposing configuration is the desired design target.
6. **Evolutionary Bridge (Historical vs Modern):** When the inflow source itself is explicitly legacy/old content (e.g., traditional UNIX buffer caches, fork-exec, or process scheduler mechanics, or legacy AWS features), or when a newly ingested inflow note introduces related historical context for a modern topic, explicitly bridge the gap to modern implementations (e.g., modern Linux page caches, namespaces/cgroups, or updated strong consistency APIs) to detail *why* systems evolved. Do NOT proactively inject legacy/historical history for modern topics if the inflow source is entirely modern.

---

## 4. Obsidian-Friendly Linking Guidelines

To maintain a healthy knowledge graph:
- **Relative Paths:** Use relative paths between the folders:
  - From a Main Note to a Reference Note: `[Link text](../Reference%20Notes/filename.md#heading-slug)`
  - Between Main Notes: `[[other-concept]]` or `[[other-concept-deeper]]`
- **Related Block:** Every landing note must have a `related` YAML metadata block AND a matching `Related Concepts` alert block at the top of the body to guarantee both metadata parsing and inline visualization.

---

## 5. Mermaid.js Diagram Guidelines

When updating visual architecture maps and concept flows:
- Wrap labels containing special characters (like parentheses, slashes, or dashes) in double quotes (e.g., `node1["Core API (v1)"]`).
- Group related components into subgraphs to keep the diagram readable.
- Use distinct styling or arrows to represent control flow vs. data paths.

---

## 6. Iterative Standard Refinement

The standards and templates defined here are evaluated and updated iteratively. As we identify better study workflows, Obsidian features, or multi-domain engineering practices, we will immediately revise this file and record the transition in `backlog.md`.

