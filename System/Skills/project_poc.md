# SKILL: PoC Agent Factory & Decoupled Project Compilation

This skill guides the `MultiDomainPoCAgent` (Factory) in dynamically detecting domains, creating specialized subagents, and compiling decoupled hands-on project playbooks.

---

## 📋 Execution Steps

### 1. Analyze Ingestion Context
- Read the newly refined Reference Note under `Reference Notes/`.
- Extract the list of domains from the note's YAML metadata (e.g. `domains: ["aws", "terraform"]`).

### 2. Specialized Agent Resolution
For each detected domain:
1. Check if the profile file `System/Agents/poc_[domain]_developer.md` exists.
2. **If missing (Factory Generation):**
   - Read the template `System/Templates/agent_profile.md`.
   - Replace placeholders (`[domain]`, `[Domain]`) with the target domain name.
   - Inject ecosystem-specific best coding practices into the prompt guidelines:
     - *Terraform:* State file locking, inputs validation, explicit resource tag mappings.
     - *AWS:* Least-privilege IAM policy blocks, isolated security group rules, multi-AZ reliability.
     - *Kubernetes:* Declarative YAML dry-runs, container resources request/limits, safe securityContexts.
     - *Networking:* Gateway ingress routing, TLS certification offloading, network segregation.
     - *Databases:* Prepared SQL statements (no concatenation), indexing tables, clustered replicas connection pools.
   - Write the generated profile file to `System/Agents/poc_[domain]_developer.md`.

### 3. Agent Definition & Invocation
1. Define the specialized agent dynamically via the `define_subagent` interface:
   - **Name:** `poc_[domain]_developer`
   - **Description:** Specialized subagent for generating [Domain] playbooks.
   - **System Prompt:** Load the text of the generated agent profile file.
   - **Capabilities:** Enable writing files and executing CLI tools.
2. Invoke the agent via `invoke_subagent` with the target note path and instructions to compile the Project note.

### 4. Decoupled Project Compilation (Executed by the Specialized Subagent)
1. Read the Reference Note and extract all CLI recipes and config blocks.
2. Create a standalone project file inside `Projects/[Domain]/Project - [Topic Name].md` using the standard `project_note.md` template.
3. Write production-grade, fully commented configurations and CLI checking recipes.
4. Add YAML links pointing back to the core landing notes in the Second Brain.

### 5. Concept Linkage Replacement (Executed by the Factory)
1. Replace the raw command and config blocks inside the Reference Note with a clean conceptual header and wiki-links referencing the generated project note:
   - *See complete implementation in [[Projects/[Domain]/Project - [Topic Name].md#section]]*
