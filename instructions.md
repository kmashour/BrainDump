# Kubernetes Knowledge Base Ingestion & Consolidation Instructions

This document defines the rules, formats, and procedures for parsing new Kubernetes transcripts/notes, appending them to the consolidated CKA knowledge base, and formatting them for Obsidian.

---

## 1. Directory Structure & File Organization

The knowledge base is stored in `/home/karim/Desktop/CKA/`.
- `README.md`: The central index and high-level visual Mermaid.js "Brain Map".
- `instructions.md`: This file.
- `backlog.md`: The transaction log containing every update, change, and addition to the knowledge base.
- `inflow/`: A landing zone for raw lecture transcripts, documentation dumps, and external notes before consolidation.
  - *Example:* `inflow/Overview-Architecuture-Kubernetes.md`.
- `01_kube_api_and_kubectl.md`: API server internals, groups, OpenAPI, watch, and kubectl commands.
- `02_cluster_architecture_and_components.md`: Macro control plane vs. worker node architecture, core processes, HA, CCM, and proxies.
- `03_node_mechanics_and_resource_limits.md`: Node conditions, leases, heartbeats, evictions, QoS classes, and cgroups.
- `04_workload_lifecycle_and_healing.md`: Self-healing pillars, probes, and garbage collection.

---

## 2. Ingestion & Consolidation Workflow

When a new source file (e.g., a documentation page, Mumshad course transcript, or architectural chat log) is introduced:

### Step 1: Landing
1. Place the raw input file directly into the `inflow/` directory.

### Step 2: Classification & Analysis
1. Analyze the technical topics covered in the new `inflow/` file.
2. Determine if these topics fit into one of the existing modules or warrant creating a new module (e.g., `05_kubernetes_networking.md`).

### Step 3: Integration & Compilation
- **If integrating into an existing file:**
  - Locate the exact section where the concept should reside.
  - Compile the raw text into a polished, structured markdown entry.
  - Integrate the new information smoothly, ensuring all granular details, command syntax, and CKA tips are preserved.
  - Avoid duplicate definitions; refine and expand existing definitions instead.
  - Review the existing `kind` PoC for that section and update it to incorporate testing of the new concepts.
- **If creating a new category:**
  - Create a new file in sequence (e.g., `05_kubernetes_networking.md`).
  - Follow the structure rules (Section 3).
  - Add the new file to the directory listing in `README.md` and update the Mermaid.js brain map to link the new concepts.

### Step 4: Consistency & Cross-Linking Checks
- Ensure all relative markdown links between files remain valid and updated.
- Verify that the Mermaid.js syntax in `README.md` is correct.

### Step 5: Update the Backlog
- Every update, compilation, or structural modification must be documented in `backlog.md` with a date and detailed description of the changes.

### Step 6: Git Synchronization (Push Updates)
- After compiling changes, verifying links, and updating the backlog, you MUST commit all modified and new files and push the updates to the remote GitHub repository:
  - Repository: `git@github.com:kmashour/BrainDump.git`
  - Commands:
    ```bash
    git add .
    git commit -m "feat/chore/docs: <brief description of changes>"
    git push origin main
    ```

---

## 3. Formatting and Structure Rules for Note Files

Every note file must strictly follow these structural guidelines:

### A. Conceptual Explanations (Thoroughness Standards)
- **No Brief Summaries:** Explanations must be thorough, context-rich, and detailed. Do not use summary bullet points that omit underlying mechanics unless it is for the explicit benefit of structural overview (like a reference table).
- **In-Depth Context:** Explain the *why* and *how* behind each component, including protocols, ports, database interactions, kernel parameters, and edge cases.
- **Practical Examples:** Provide complete examples (YAML files, command outputs, configuration snippets) rather than generic placeholders.
- **CKA Tips:** Highlight specific CKA troubleshooting tips using GitHub-style alerts (e.g., `> [!TIP]`, `> [!WARNING]`, `> [!IMPORTANT]`).

### B. Command Syntax
- Use the most efficient short names for resources (`po`, `deploy`, `svc`, `ns`, `no`).
- Document the exact flags needed, especially for high-speed operation (e.g., `--force --grace-period=0` or `-o yaml --dry-run=client`).

### C. Practical Proof of Concept (PoC) using `kind`
Every section must have a dedicated, hands-on verification section with these requirements:
- **Guided, Step-by-Step CLI Steps:** Provide exact commands to run in the terminal.
- **Verification Commands:** Show how to inspect the results (`kubectl describe`, `kubectl logs`, etc.).
- **No Placeholders:** Use real, working docker images (`nginx`, `redis`, `busybox`, `httpd`).
- **Resource Clean-up:** Provide the commands to clean up the resources to leave the cluster in a pristine state.

---

## 4. Obsidian-Friendly Linking Guidelines

To build a rich knowledge graph inside Obsidian, follow these linking rules:

- **Relative Markdown Links:** Use standard relative markdown links to connect files: `[Link Text](filename.md)`.
  - *Example:* Use `[kube-apiserver](01_kube_api_and_kubectl.md)` to reference the API server mechanics.
- **Anchor Links:** When referencing a specific concept in another file, link directly to the heading anchor: `[Link Text](filename.md#heading-slug)`.
  - *Example:* `[Node Conditions](03_node_mechanics_and_resource_limits.md#b-conditions)`.
- **Bidirectional Connections:** When modifying a file to point to another, ensure the target file also links back to the source file where appropriate.
- **"Related Modules" Section:** Every module note must contain a "Related Modules" section at the very end. This section should list all connected notes to build a clean Obsidian graph visualization.

---

## 5. Mermaid.js Diagram Guidelines

When updating the visual brain map in `README.md`:
- Wrap labels containing special characters (like parentheses, slashes, or dashes) in double quotes (e.g., `node1["Core API (v1)"]`).
- Group related components into subgraphs to keep the diagram readable.
- Use distinct styling or arrows to represent control flow vs. data paths.

---

## 6. Iterative Standard Refinement

The standards and templates defined here will be evaluated and updated iteratively. As we identify better study workflows, Obsidian features, or CKA prep strategies, we will immediately revise this file and record the transition in `backlog.md`.
