---
obsidianUIMode: preview
class: project-note
tier: project
domains:
  - "linux"
concepts_referenced:
  - "[[git_fundamentals_and_workflows]]"
difficulty: intermediate
status: completed
---

# Chapter 1: DevOps Leadership, Mentorship, and Stakeholder Alignment

**Breadcrumbs:** [[Projects/PwC Interview Preparation/Plan - DevOps Interview Roadmap|DevOps Interview Roadmap]] > Theory > **Chapter 1: Leadership & Mentorship**

---

## 🏛️ 1. Technical Mentorship and Team Governance

A Senior DevOps Associate is responsible for instilling engineering discipline, security awareness, and operational standards within the development team.

### A. Local Validation: Enforcing Pre-Commit Hooks
Instead of allowing poor formatting, plain-text secrets, or syntax errors to reach the CI pipeline (which wastes runner credits and feedback loops), establish **local pre-commit controls**.
*   **The Tool:** The `pre-commit` framework allows developers to execute security checks locally before git wraps the commit.
*   **The Configuration (`.pre-commit-config.yaml`):**
    ```yaml
    repos:
      - repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v4.6.0
        hooks:
          - id: check-yaml
          - id: end-of-file-fixer
          - id: trailing-whitespace
      - repo: https://github.com/compilerla/conventional-pre-commit
        rev: v3.2.0
        hooks:
          - id: conventional-pre-commit # Enforces clean commit message standards
    ```
*   **Verification:** Run `pre-commit install` to bind these scripts to `.git/hooks/pre-commit`.

### B. Git Branch Governance & Code Owners
*   **Branch Protection Rules:** Enforce strict controls on the `main` or `production` branches:
    *   Require a Pull Request (PR) before merging.
    *   Require at least 1 or 2 approving reviews.
    *   Require status checks to pass before merging (e.g., linting, unit tests, Trivy scans).
    *   Enforce signed commits (X.509/GPG) to verify committer identity.
*   **CODEOWNERS File:** Enforce code area approvals. Create `.github/CODEOWNERS`:
    ```text
    # Global owners for all files
    *       @kmashour
    # Infrastructure-specific files require approval from the DevOps team
    /terraform/   @kmashour @devops-team-lead
    # Security workflows require approval from DevSecOps
    /.github/workflows/   @security-team-approver
    ```

---

## 🗣️ 2. Stakeholder Management & Technical Communication

DevOps acts as the translator between business requirements, software development timelines, and infrastructure realities.

### A. Technical Debt Resolution Framework
When developers request new tools, but business stakeholders demand features, advocate for technical debt remediation:
1.  **Quantify Cost:** Frame technical debt in terms of business metrics (e.g., *"Our current lack of pipeline caching increases build wait times by 15 minutes per commit. Across 10 developers making 5 daily commits, we waste 12.5 engineer-hours weekly."*)
2.  **Define SLOs (Service Level Objectives):** Establish measurable reliability targets (e.g., App availability must be $\ge$ 99.9% over a 30-day window).
3.  **Establish Error Budgets:** The remaining room for failure ($0.1\%$). If the error budget is exhausted, block all new feature deployments and focus resources exclusively on stability and performance optimization.

### B. Architecture Decision Records (ADRs)
Standardize architectural changes using ADRs to preserve design context. An ADR contains:
*   **Title:** The decision name (e.g., `ADR-004: Standardize S3 Backend for Terraform State`).
*   **Context:** The technical problem and assumptions (e.g., local state file collisions).
*   **Decision:** The exact solution approved (e.g., DynamoDB locking + S3).
*   **Consequences:** The operational impact (e.g., devs must run `terraform init`, but state is locked).
*   *See similar structural formats in [[Reference Notes/git_fundamentals_and_workflows]] and [[Projects/Linux/Project - Migrating Legacy Init Scripts to systemd.md]].*
