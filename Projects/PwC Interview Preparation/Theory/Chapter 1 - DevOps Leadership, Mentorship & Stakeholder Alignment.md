---
obsidianUIMode: preview
class: project-note
tier: project
domains:
  - "linux"
concepts_referenced:
  - "[[git_fundamentals_and_workflows]]"
difficulty: advanced
status: completed
---

# Chapter 1: DevOps Culture, Git Workflows, and Local Security Gates

**Breadcrumbs:** [[Projects/PwC Interview Preparation/Plan - DevOps Interview Roadmap|DevOps Interview Roadmap]] > Theory > **Chapter 1: Leadership & Git Governance**

---

## 🏛️ 1. Git Workflow Governance & Release Topologies

In an enterprise environment, branch management must balance developer velocity with strict release controls.

### A. GitFlow vs. Trunk-Based Development
*   **GitFlow:** Utilizes long-lived branches (`main`, `develop`, `release/*`, `feature/*`, `hotfix/*`).
    *   *Pros:* Highly structured, fits traditional scheduled releases, separate stabilization branch (`release`).
    *   *Cons:* High merge overhead, branch synchronization drift, delay in integration, merge conflicts.
*   **Trunk-Based Development (TBD):** Developers merge small, frequent commits into a single core branch (`main` or `trunk`). Featurization is managed using **Feature Flags (Toggles)**.
    *   *Pros:* Eliminates long-lived branch drift, forces small commits, enables continuous integration.
    *   *Cons:* Requires high test automation coverage and mature feature flag management.

### B. Commit Security & Identity Verification
*   **Signed Commits (GPG/X.509/SSH):** Enforce signature verification in Git settings. Standard commits can have their author metadata spoofed (e.g. configuring `user.email` to mimic another user). Signed commits cryptographically bind the commit to the developer's private key, proving identity.
*   **Branch Protection Controls:** Enforce rules on release branches:
    *   Require Linear History (blocks merge commits, enforces rebase).
    *   Require Signed Commits.
    *   Require Status Checks (forces unit tests and linter runs to succeed in CI before merge).
    *   **CODEOWNERS File:** Map specific file paths to required team reviews:
        ```text
        # Enforce DevOps team approval on infrastructure changes
        /terraform/      @devops-lead @kmashour
        # Enforce Security team approval on workflow updates
        /.github/workflows/   @security-lead
        ```

---

## 🛡️ 2. Shifting Security Left: Pre-Commit & Pre-Push Hook Gates

Instead of validating code only in the CI runner (which delays feedback and wastes compute credits), implement local git hook gates.

### A. Git Hook Primitives
Git hooks are scripts executed automatically at specific points in the git lifecycle, stored locally under `.git/hooks/`. Because `.git/` is not committed to remote repositories, use the **`pre-commit` framework** to distribute and manage hooks across the team.

### B. Custom Local Gate Design (`.pre-commit-config.yaml`)
Integrate local syntax, formatting, and security scans:
```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: check-yaml
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: check-merge-conflict # Blocks commits containing merge conflict markers
      - id: check-added-large-files
        args: ['--maxkb=500'] # Blocks accidental large binary commits

  - repo: https://github.com/compilerla/conventional-pre-commit
    rev: v3.2.0
    hooks:
      - id: conventional-pre-commit # Enforces semantic naming (e.g., 'feat:', 'fix:')

  - repo: https://github.com/hadolint/hadolint
    rev: v2.12.0
    hooks:
      - id: hadolint # Validates Dockerfiles locally before commit
```
*   **Deployment:** Run `pre-commit install` to register these hooks. If a developer writes a Dockerfile containing insecure instructions (e.g., using `latest` tag or running as root), `hadolint` intercepts the commit and aborts it locally.

---

## 🗣️ 3. Managing Technical Debt and Stakeholder Alignment

A Senior Associate must translate technical infrastructure needs into business value.

### A. The SLO/SLA/SLI Framework
*   **SLA (Service Level Agreement):** The legal commitment to users regarding system reliability (e.g., "99.9% uptime"). If broken, financial penalties are incurred.
*   **SLO (Service Level Objective):** The target reliability set by the engineering team (e.g., "99.95% uptime"). Must be stricter than the SLA to provide a safety buffer.
*   **SLI (Service Level Indicator):** The quantitative metric measured (e.g., `Successful HTTP Requests / Total HTTP Requests * 100`).

### B. Error Budget Management
The Error Budget is the allowable downtime over a period ($100\% - \text{SLO}$).
*   *Example:* A $99.9\%$ monthly SLO allows 43 minutes and 49 seconds of total downtime.
*   **The Policy:** If the error budget is healthy, developers can deploy new features. If the error budget is exhausted, new feature deployments are automatically blocked. The sprint goal pivots exclusively to stability, bug fixes, and infrastructure technical debt.

*See details on Git branches and workflows in [[Reference Notes/git_fundamentals_and_workflows]].*
