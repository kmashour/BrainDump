---
obsidianUIMode: preview
class: index-note
tier: reference-note
tags:
  - github-actions/reference-index
  - obsidian/moc
---

# 🐙 GitHub Actions Reference MOC

**Breadcrumbs:** [[--Index--|🏠 Index]] > **GitHub Actions Reference MOC**

---

## 🏛️ Reference Modules & Frameworks

This index contains our GitHub Actions CI/CD automation study modules, starting from basic architecture to advanced matrix configurations and security hardening.

- 🐙 **[Module 9-1: GitHub Actions Architecture & Workflow Design](9-1_github_actions_architecture_and_workflows.md)**
  * Core components (workflows, jobs, steps, actions, runners, events, artifacts), runtime architecture, and basic YAML pipeline structure.
- ⚙️ **[Module 9-2: Advanced Pipeline Control & Execution](9-2_github_actions_advanced_execution.md)**
  * Multi-job orchestration (dependencies, needs, outputs), dynamic storage (artifacts, dependency caching), matrix testing, environments, and secrets management.
- 🔒 **[Module 9-3: Runner Administration & Pipeline Hardening](9-3_github_actions_administration_and_security.md)**
  * Self-hosted runner systemd deployments on Linux hosts, security controls (GITHUB_TOKEN permissions, OIDC cloud trust, action SHA pinning), diagnostic debugging, and comparisons to Jenkins.
- 🐙 **[Module 9-4: GitHub Actions & CI/CD Platform Automation (Elfakharny Lecture)](9-4_github_actions_lecture_elfakharny.md)**
  * Basic CI/CD principles, event-driven platform automation triggers, YAML anatomy (the checkout gotcha), VM multiplier billing tiers, and Enterprise Cloud vs Server topologies.
- 🚀 **[Module 9-5: GitHub Actions Introduction & Production Workflows](9-5_github_actions_introduction_and_production_workflows.md)**
  * Foundations of CI/CD, core GHA architecture components, clean hosted/self-hosted environments, and production containerization pipelines with Docker Hub authentication and secrets.
- ⚙️ **[Module 9-6: GitHub Actions Triggers, Runners & Workflow Logic](9-6_github_actions_triggers_runners_and_logic.md)**
  * Advanced trigger filters (branches, paths, tags), standard vs. larger hosted runner sizing, built-in contexts, variables, and expression conditional evaluation.
- 🐙 **[Module 9-7: GitHub Actions Functions, Inputs, Outputs & Reusable Workflows](9-7_github_actions_functions_inputs_outputs_and_reusable_workflows.md)**
  * Generic utility functions, status check execution gates, input validation patterns, step/job output mapping, and modular reusable workflows.
- 📦 **[Module 9-8: GitHub Actions Artifacts & Caching](9-8_github_actions_artifacts_and_caching.md)**
  * Structured separation of outputs, persistent artifacts, and dependency caching lifecycle strategies to optimize pipeline speed.
- 📊 **[Module 9-9: GitHub Actions Matrix Strategy](9-9_github_actions_matrix_strategy.md)**
  * Multi-OS and multi-version testing configurations at scale, fail-fast controls, concurrency limitations, and dynamic include/exclude mapping.
- 🔒 **[Module 9-10: GitHub Actions Environments, Secrets & Approvals](9-10_github_actions_environments_secrets_and_approvals.md)**
  * Deployment targets, environment protection rules (manual approvals, wait timers), branch restrictions, and scoped secret overriding resolution.

---

## 🛠️ Verification Projects
Hands-on playbooks and milestone projects:
- 🚀 **[Project: GitHub Actions CI-CD Pipelines](../Projects/github-actions/Project%20-%20GitHub%20Actions%20CI-CD%20Pipelines.md)**

