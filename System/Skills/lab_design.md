# SKILL: Hands-on Lab Design & AARF Failure Validation

This skill defines the technical checklists, criteria, and execution steps used by the `LabArchitectAgent` to review reference notes and compile hands-on verification labs.

---

## 📋 Execution Steps

### 1. Audit Reference Notes
- Scan all markdown documents inside `Reference Notes/`.
- Identify the core domain of each module from its YAML metadata (`domains:`).
- Filter modules:
  - **Applicable Domains:** Kubernetes (`kubernetes`), Docker (`docker`), AWS (`aws`), Systems Design (`system-design`), Networking (`networking`), and Database (`database`).
  - **Excluded Domains:** Theoretical Computer Architecture, Operating System History, or general programming language syntax (unless specific framework integration like Flask packaging is active).

### 2. Identify Lab Requirements & Gaps
- For each applicable module, check for the presence of a dedicated hands-on section (e.g. `## Hands-on Labs` or links to `Projects/`).
- Determine if the existing labs cover the **AARF failure modes** highlighted in the module's Deep-Intuition (AARF) Breakdowns.
- If a concept has an AARF breakdown describing a specific Failure Loop (e.g. a stateless NACL blocking return ephemeral ports, or an Out-Of-Memory limit triggering a kernel panic), there **must** be a corresponding step in the labs showing the student how to:
  1. Deploy the system in the failure state.
  2. Capture the exact error signature or event log matching the Failure Loop.
  3. Modify the configuration to apply the Answer.
  4. Verify the healthy, operational state.

### 3. Lab Document Compilation
- Write lab instructions using the standard markdown playbook structure:
  - **Objective:** What is being verified.
  - **Topology / Prerequisites:** Virtual sandboxes, Kind clusters, local Docker networking parameters, or AWS CLI profiles.
  - **Step-by-Step CLI Execution:** Direct commands, configuration file write-outs, and verification queries.
  - **Failure Simulation & Capture:** Steps to generate the negative test case.
- Store multi-tier projects in the `Projects/` directory or document them under a dedicated `## Hands-on Project Labs` header in the respective module.
- Add back-links between the lab scripts and the conceptual landing/deeper notes.
