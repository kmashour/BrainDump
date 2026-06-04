# SKILL: Ingest & Restructure Kubernetes Study Vault

## Objective
This skill provides a systematic protocol for parsing new study transcripts/notes, incorporating them into the consolidated CKA knowledge base, and formatting them for Obsidian graphs without compromising architectural separation.

## Trigger
Execute this skill when:
1. New study material, transcripts, or documentation dumps are added to the `inflow/` directory.
2. Conceptual definitions require updates, link adjustments, or structural changes.


---

## 1. Directory Structure & File Organization

The knowledge base is stored in `/home/karim/Desktop/CKA/`.
- `README.md`: The central index and high-level visual Mermaid.js "Brain Map" connecting the main components.
- `instructions.md`: This file (the Ingestion Skill).
- `backlog.md`: The transaction log containing every update, change, and addition to the knowledge base.
- `inflow/`: A landing zone for raw lecture transcripts, documentation dumps, and external notes before consolidation.
- `Reference Notes/`: Detailed, high-verbosity study modules and hands-on PoCs. Contains `Reference Notes/Index.md` (dynamic index of all modules).
- `Main Notes/`: Atomic, conceptual summaries (Landing Notes and Deeper Notes). Contains `Main Notes/Index.md` (dynamic index of all landing and deeper notes).
- `Digital Garden/`: Connective architectural patterns and cross-domain connections. Contains `Digital Garden/Index.md` (dynamic index of patterns).
- `Projects/`: Workspaces for active projects. Contains `Projects/CKA/` specifically for CKA Exam preparation, speed hacks, and checklists.

---

## 1.1 Team of Specialized Agents

To maintain and expand the vault efficiently, the following specialized AI subagents are available:
- **ResearchAgent (`research_refinement`):** Parses raw materials (Gemini logs, transcripts, email newsletters) in `inflow/`, cleans up debugging noise, and compiles structured Reference Notes in `Reference Notes/`.
- **MultiDomainPoCAgent (`poc_developer`):** Focuses on creating and writing dense, accurate, context-rich validation scripts and PoC setups across all domains (Linux, AWS, Kubernetes, Databases, and Networking).
- **GardenAgent (`garden_architect`):** Analyzes connections across domains (AWS, Linux, Databases, Networking, Kubernetes) and compiles Architectural Pattern Notes in `Digital Garden/`.
- **CKAExamAgent (`cka_exam_expert`):** Focuses on optimizing study notes for exam success, compiling time-management strategies, terminal configurations, VIM hacks, and topic-specific exam checklists inside `Projects/CKA/`.
- **IntegrationAgent (Main Session):** Coordinates all agents and orchestrates vault indexing and final commits.

---

## 2. Ingestion & Consolidation Workflow

When a new source file is introduced:

### Step 1: Landing
1. Place the raw input file directly into the `inflow/` directory.

### Step 2: Classification & Analysis
1. Analyze the technical topics covered in the new `inflow/` file.
2. Identify which core component it relates to (e.g. `kube-apiserver`, `etcd`, etc.) or if a new concept needs to be established.

### Step 3: Reference Note & PoC Integration
1. **Reference Note Compilation:** Delegate to `ResearchAgent` to parse raw details and write verbose explanations to `Reference Notes/`.
2. **Verification PoC Generation:** Delegate to `MultiDomainPoCAgent` to write and verify domain-specific verification scripts/commands inside the reference notes.

### Step 4: Main Note Creation & Update (Conceptual Atomicity)
1. If the concept is new, create its **Landing Note** and **Deeper Note** inside `Main Notes/` using the templates in Section 3.
2. If the concept is already present, update its deeper-dive notes to add links/context to the new sub-topics, connecting them back to the reference modules.

### Step 5: Architectural Pattern Identification (Digital Garden)
1. Delegate to `GardenAgent` to analyze how the new concepts connect to other domains (AWS, Linux, Databases, Networking).
2. Create or update Architectural Pattern Notes inside `Digital Garden/` to detail E2E configurations and trade-offs.

### Step 6: CKA Exam Checklist Extraction (Projects/CKA)
1. **Mandatory Default Execution:** For all new CKA or general Kubernetes material, the `CKAExamAgent` must run by default right after the previous steps (Reference Notes, Main Notes, Deeper Notes, and Digital Garden setup) are completed.
2. Delegate to `CKAExamAgent` to extract strictly exam-focused checklists, shortcuts, terminal tricks, or VIM setups based on the newly ingested/structured notes.
3. Create or update notes in `Projects/CKA/` (e.g. `Projects/CKA/Exam Checklist - ...`).

### Step 7: Update the Backlog
- Document all updates, creations, and restructurings in `backlog.md` with a timestamp and description of changes.

### Step 8: Git Synchronization (Push Updates)
- After verification of all relative links and file modifications, commit and push changes:
  ```bash
  git add .
  git commit -m "feat/chore/docs: <description>"
  git push origin main
  ```

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

**Breadcrumbs:** [[Index|🏠 Index]] > <Layer> > **<concept-name>**

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

**Breadcrumbs:** [[Index|🏠 Index]] > [[<landing-concept-name>]] > **<deeper-aspect-name>**

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

**Breadcrumbs:** [[Index|🏠 Index]] > Patterns > **<pattern-name>**

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
