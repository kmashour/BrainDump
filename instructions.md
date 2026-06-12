# SKILL: Ingest & Restructure Kubernetes Study Vault

## Objective
This skill provides a systematic protocol for parsing new study transcripts/notes, incorporating them into the consolidated CKA knowledge base, and formatting them for Obsidian graphs without compromising architectural separation.

## Trigger
Execute this skill when:
1. New study material, transcripts, or documentation dumps are added to the `inflow/` directory.
2. Conceptual definitions require updates, link adjustments, or structural changes.
3. The user requests a review of the vault integrity using the `@review` keyword in their message.
4. The user requests ingestion of a file or URL index list using the `@ingest` keyword in their message.



---

## 1. Directory Structure & File Organization

The knowledge base is stored in `/home/karim/Desktop/BrainDumo/`.
- `README.md`: The central index and high-level visual Mermaid.js "Brain Map" connecting the main components.
- `instructions.md`: This file (the Ingestion Skill).
- `backlog.md`: The transaction log containing every update, change, and addition to the knowledge base.
- `inflow/`: A landing zone for raw lecture transcripts, documentation dumps, and external notes before consolidation.
- `Reference Notes/`: Detailed, high-verbosity study modules and hands-on PoCs. Contains `Reference Notes/0-Index.md` (dynamic index of all modules).
- `Main Notes/`: Atomic, conceptual summaries (Landing Notes and Deeper Notes). Contains `Main Notes/0-Index.md` (dynamic index of all landing and deeper notes).
- `Digital Garden/`: Connective architectural patterns and cross-domain connections. Contains `Digital Garden/0-Index.md` (dynamic index of patterns).
- `Projects/`: Workspaces for active projects. Contains `Projects/CKA/` specifically for CKA Exam preparation, speed hacks, and checklists.

---

## 1.1 Team of Specialized Agents

The specialized subagents and their profiles are defined in the `System/Agents/` directory:
- **OrchestrationAgent:** [orchestrator.md](System/Agents/orchestrator.md) (Pipeline Manager & Coordinator)
- **ResearchAgent:** [researcher.md](System/Agents/researcher.md) (Inflow Refinement & Reference Compiler)
- **AuditAgent:** [auditor.md](System/Agents/auditor.md) (Context Auditor & Tangent Expander)
- **DiagramAgent:** [diagrammer.md](System/Agents/diagrammer.md) (Mermaid.js Concept Designer)
- **MultiDomainPoCAgent:** [poc_developer.md](System/Agents/poc_developer.md) (Verification & Hands-on Implementation Developer)
- **LabArchitectAgent:** [lab_architect.md](System/Agents/lab_architect.md) (Specialized Lab Architect & Hands-on Lab Compiler)
- **GardenAgent:** [garden_architect.md](System/Agents/garden_architect.md) (Cross-Domain Connection & Pattern Architect)
- **CKAExamAgent:** [exam_expert.md](System/Agents/exam_expert.md) (Exam checklist & speed-optimization expert)

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
- Extensive architectural breakdowns and configurations.
- Practical step-by-step CLI validation guides using `kind`.
- Highlighting CKA exam tips in alert boxes (`> [!TIP]`, etc.).

### E. Deep-Intuition Documentation Style (AARF Extension)
To give vault knowledge maximum volume and diagnostic depth, the research and audit engines must extend Q&As, scenario solutions, and study files with the AARF framework:
1. **The Answer (Core Config):** Explicit command lines, dry-run formulas, or YAML manifests.
2. **The Assumptions (Context):** Prerequisites, cluster version skew constraints, namespace scope, or runtime config dependencies.
3. **The Rationale (Why):** System-level architecture explanation (why Kubernetes works this way under the hood).
4. **The Failure Loop (What if not):** The exact error message, kernel log event, pod CrashLoop state, or security warning if omitted/misconfigured.
5. **Alternative Case (When to use 'if not'):** Real-world production cases when the opposing configuration is the desired design target.

---

## 4. Obsidian-Friendly Linking Guidelines

To maintain a healthy knowledge graph:
- **Relative Paths:** Use relative paths between the folders:
  - From a Main Note to a Reference Note: `[Link text](../Reference%20Notes/filename.md#heading-slug)`
  - Between Main Notes: `[[other-concept]]` or `[[other-concept-deeper]]`
- **Related Block:** Every landing note must have a `related` YAML metadata block AND a matching `Related Concepts` alert block at the top of the body to guarantee both metadata parsing and inline visualization.


---

## 5. Mermaid.js Diagram Guidelines

When updating the visual brain map in `README.md`:
- Wrap labels containing special characters (like parentheses, slashes, or dashes) in double quotes (e.g., `node1["Core API (v1)"]`).
- Group related components into subgraphs to keep the diagram readable.
- Use distinct styling or arrows to represent control flow vs. data paths.

---

## 6. Iterative Standard Refinement

The standards and templates defined here will be evaluated and updated iteratively. As we identify better study workflows, Obsidian features, or CKA prep strategies, we will immediately revise this file and record the transition in `backlog.md`.
