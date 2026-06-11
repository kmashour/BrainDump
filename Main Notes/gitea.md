---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - git
  - linux
related_concepts:
  - "[[GIT]]"
  - "[[podman]]"
against:
  - "[[gitlab]]"
reference_guides:
  - "[[Reference Notes/gitea_installation_and_workflows.md]]"
tags:
  - git/server
  - status/completed
---

# gitea

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **gitea**

---

## 🎯 Purpose (Why it is used)
Gitea is a lightweight, self-hosted Git service written in Go. In air-gapped enterprise environments, it provides a centralized Git server, code collaboration interface, code reviews, and CI/CD pipelines as a single, low-overhead binary.

---

## ⚙️ Functionality (What it is doing)
* **Code Hosting:** Governs remote Git repositories over HTTP/HTTPS and SSH.
* **Collaboration Web Interface:** Provides pull requests, issues, branch protection, and project boards.
* **CI/CD Orchestration:** Integrates with `act_runner` to execute Gitea Actions workflows.
* **Git Server Hooks:** Executes server-side Git scripts (such as `pre-receive` and `post-receive`) to enforce governance.
* **Access Control:** Integrates with local databases (SQLite/MySQL) to manage user privileges and organization memberships.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Gitea operates as a central control plane tool for local development:
* **Inbound Traffic:** Exposes port `3000` directly or behind an Apache/Nginx reverse proxy.
* **Security Layer:** Intersects with OpenSSH (`sshd`) for multiplexed key authentication.
* **Database Layer:** Communicates with SQLite or MySQL databases over local Unix sockets or loopback interfaces.
* **Storage Layer:** References large LVM partitions via Filesystem Hierarchy Standard (FHS) compliant symlinks.
* **Execution Layer:** Dispatches CI/CD pipeline runs to unprivileged `act_runner` background services.

---

## 🧩 Problem Solver (What problem it solves)
In air-gapped environments where enterprise platforms like GitHub or GitLab (which are heavy, internet-dependent, or complex to install offline) cannot be used, Gitea solves the challenge of offline software version control. It runs on minimal resources (1 core, 512MB RAM minimum) while delivering full web-based team workflow support.

---

## 🟢 Operational Impact (What will happen with it operating)
* Teams can collaborate, review code, and execute merge request approvals entirely offline.
* Code deployments, testing pipelines, and linter audits execute automatically on staging/production VM targets when branches are merged.
* Branch protection rules and naming conventions are strictly enforced server-side.

---

## 🔴 Failure Impact (What will happen without it)
* Centralized code sharing is blocked, forcing teams to manually copy repositories via USB or raw clone channels, which leads to merge chaos.
* Automated testing and continuous deployment (CD) pipelines are halted, requiring manual, error-prone file transfers to VM runtime trees.
* Branch naming policies and pre-merge validation checks cannot be enforced.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **gitea**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[gitea]]
SORT file.name ASC
```
