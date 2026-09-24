# SKILL: Contextual Proof of Concept Integration & Collaborative Project Building

This skill guides the `MultiDomainPoCAgent` in developing high-fidelity Proof of Concepts (PoCs) directly within the explanation context of Reference Notes, and collaborating with the user on co-authored engineering projects.

---

## 📋 Execution Steps

### 1. In-Note Contextual PoC Integration (Phase 3 Default)
When invoked during the standard ingestion pipeline:
1. **Analyze Reference Note:** Read the refined Reference Note under `Reference Notes/` and identify the core technical mechanisms, tools, and configurations.
2. **Embed Declarative Manifests:** Rather than creating a detached file in `Projects/`, embed complete, production-grade configurations (YAML, HCL, Dockerfile, shell scripts, Python snippets) directly within the note under:
   - `## 🛠️ Verification & Practical Implementation`, or
   - `## 🧪 Hands-on Proof of Concept / Lab Simulation`
3. **Negative Testing & Failure Loop Simulation:** In accordance with the AARF framework, provide step-by-step instructions showing:
   - How to deploy the system in a failing/misconfigured state.
   - The exact error signature, event code, or kernel log emitted.
   - How to apply the fix (the Answer) and verify successful operation.
4. **Prohibition of Automatic Dumps:** Under NO circumstances should standalone project files be generated automatically in `Projects/`.

---

### 2. Collaborative Project Building (On-Demand With User)
When the user explicitly requests to build a project together:
1. **Scope the Project:** Clarify goals, requirements, constraints, and architecture with the user.
2. **Co-Design Architecture:** Outline the topology, component interactions, and Mermaid diagram collaboratively.
3. **Draft Implementation Playbook:**
   - Use `System/Templates/project_note.md`.
   - Place the project note inside `Projects/[Domain]/Project - [Topic Name].md`.
   - Incorporate fully commented code, security hardening, and modular parameters.
4. **Interactive Verification:** Walk through the verification steps and failure testing alongside the user.

