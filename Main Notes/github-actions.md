---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "github-actions"
related_concepts:
  - "[[Main Notes/docker.md]]"
  - "[[Main Notes/linux.md]]"
against:
  - "[[Main Notes/jenkins.md]]"
reference_guides:
  - "[[Reference Notes/9-Index - GitHub Actions.md]]"
tags:
  - github-actions/tool
  - status/completed
---

# GitHub Actions

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > CI/CD > **GitHub Actions**

---

## 🎯 Purpose (Why it is used)
GitHub Actions is an event-driven CI/CD platform designed to automate software build, test, package, and deployment workflows directly within a GitHub repository infrastructure, eliminating manual deployment handovers.

---

## ⚙️ Functionality (What it is doing)
*   **Workflow Orchestration:** Listens to repository event hooks (e.g. pushes, pull requests, API dispatches) to trigger automated job execution.
*   **Runner Lifecycle Management:** Schedules and provisions isolated execution runner virtual machines or containers to process pipeline steps.
*   **Artifact & Log Aggregation:** Streams console logs and stores generated compilation artifacts (binaries, packages, test reports) in secure central storage.

---

## 🏛️ Architectural Context (How it fits in the architecture)
GitHub Actions integrates natively with git repositories. It triggers workflows based on code changes, fetches dependencies, runs build commands, packages applications into Docker images, publishes them to registries (like GHCR), and prompts target environments (like Kubernetes or AWS EKS) to deploy the updated services.

---

## 🧩 Problem Solver (What problem it solves)
*   **Saves Manual Operations:** Eliminates repetitive build and packaging tasks.
*   **Prevents Code Drift:** Ensures code is compiled and tested under clean, reproducible sandbox environments before merging.
*   **Eliminates Password Anti-patterns:** Resolves security issues of long-lived credentials (like AWS Access Keys) by utilizing temporary passwordless OpenID Connect (OIDC) cloud roles.

---

## 🟢 Operational Impact (What will happen with it operating)
Every commit and PR is tested automatically. Build errors are flagged immediately. Successful builds publish immutable container images tagged with the Git commit SHA, creating a transparent delivery pipeline.

---

## 🔴 Failure Impact (What will happen without it)
Developers must build and test code locally, leading to environment mismatches. Manual credentials must be shared, increasing security risks. Release cycles slow down drastically, and deployment rollbacks become complex and error-prone.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes and use cases associated with GitHub Actions.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
