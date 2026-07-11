---
obsidianUIMode: preview
class: reference-note
tier: reference-note
tags:
  - github-actions
  - cicd/automation
  - status/completed
---

# Module 9-4: GitHub Actions & CI/CD Platform Automation (Elfakharny Lecture)

**Breadcrumbs:** [[9-Index - GitHub Actions|🏠 GitHub Actions References Index]] > **GitHub Actions & CI/CD Platform Automation (Elfakharny Lecture)**

---

> [!NOTE]
> **Source Citation & Translation**
> This reference module compiles, translates, and analyzes the Arabic lecture transcript **inflow/GithubAction-Elfakharny.md** by instructor **Elfakharny**. It outlines the core principles of CI/CD, explains why GitHub Actions is a platform-wide automation engine rather than a simple build tool, details YAML workflow syntax, and covers runner resource costs and GitHub Enterprise architectures.

---

## 🎯 Foundations of CI/CD (Continuous Integration & Continuous Deployment)

Before diving into tool configurations, it is critical to define the core pipeline methodologies:

### 1. Continuous Integration (CI)
* **Goal:** Automatically build and test code changes whenever a developer pushes to the central repository.
* **Problem Solved:** Prevents "integration hell" in microservices or collaborative team environments. It verifies that new features or bug fixes do not break existing components before merging.

### 2. Continuous Delivery vs. Continuous Deployment (CD)
* **Continuous Delivery:** The pipeline builds, tests, and deploys the code automatically to a staging or pre-production environment. However, deploying the final package to the **Production** environment requires a manual gate (a human approval click).
* **Continuous Deployment:** A fully automated pipeline where any code change passing all test stages is automatically pushed to the **Production** environment immediately without human intervention.

---

## 🏛️ Why GitHub Actions is a Platform-Wide Automation Engine

Traditional CI/CD tools (like Jenkins, GitLab CI, CircleCI, or Travis CI) are focused strictly on building and deploying code. GitHub Actions is designed differently:

* **Event-Driven Platform:** GitHub Actions is an automation platform for the entire GitHub repository lifecycle. It can be triggered by standard Git events (`push`, `pull_request`) or GitHub platform events (e.g., when a user opens an `issue`, comments on a PR, stars/watches a repository, or schedules a cron job).
* **Deep Integration:** Actions connect directly with other GitHub products like Codespaces (online IDE editor), GitHub Copilot (AI-assisted coding), and Dependabot (automated security vulnerability scanning).

---

## 🧱 Workflow Components & YAML Anatomy

GitHub Actions workflows are defined in YAML files placed inside the `.github/workflows/` directory.

```
+--------------------------------------------------------------+
| Workflow (.github/workflows/main.yml)                        |
|                                                              |
|   [Trigger / Event] -> on: push / pull_request / watch       |
|                                                              |
|   +------------------------------------------------------+   |
|   | Job 1: Build & Test (runs on ubuntu-latest)          |   |
|   |                                                      |   |
|   |   Step 1 (Checkout):  uses: actions/checkout@v4      |   |
|   |   Step 2 (Lint):      run: npm run lint              |   |
|   |   Step 3 (Test):      run: npm test                  |   |
|   +------------------------------------------------------+   |
|                                                              |
|   +------------------------------------------------------+   |
|   | Job 2: Deploy (needs: Job 1, runs on self-hosted)    |   |
|   |                                                      |   |
|   |   Step 1 (Deploy):    run: ./deploy.sh               |   |
|   +------------------------------------------------------+   |
+--------------------------------------------------------------+
```

### 1. Key YAML Directives
* **`name`:** A user-friendly name for the workflow displayed in the GitHub Actions UI.
* **`on`:** The trigger block defining what event runs the workflow.
* **`jobs`:** A list of independent execution blocks. Jobs run in **parallel** by default to speed up pipelines, but can be forced to run sequentially using the `needs` parameter.
* **`runs-on`:** Specifies the operating system runner (e.g., `ubuntu-latest`, `windows-latest`, `macos-latest`, or `self-hosted`).
* **`steps`:** A sequential list of tasks inside a job. Steps run one after another.
* **`run`:** Executes command-line scripts or shell commands.
* **`uses`:** References a pre-built Action from the GitHub Marketplace (e.g., `actions/checkout@v4`).

### 2. The Checkout Gotcha
Unlike other CI/CD platforms (like GitLab CI), **GitHub Actions does not clone your repository code onto the runner workspace by default**. You must explicitly call the checkout action as your first step:
```yaml
steps:
- name: Checkout Repository Code
  uses: actions/checkout@v4
```

---

## 💰 Billing, Tiers, & Resource Limits

GitHub Actions usage is billed based on repository visibility, running time (minutes), and the host OS.

### 1. Repository Visibility Rules
* **Public Repositories:** Absolutely free. There is **no limit** on running minutes, as GitHub hosts public open-source project workflows for free.
* **Private Repositories:** Free tier accounts receive **2,000 free minutes** per month. Paid tiers receive larger quotas:
  * *Pro/Team Tiers:* **3,000 minutes** per month.
  * *Enterprise Cloud:* **50,000 minutes** per month.

### 2. Multiplier Cost Tiers (By Host OS)
Additional minutes beyond the free tier are billed at different rates depending on the runner VM's operating system:
* **Linux (Ubuntu):** Base rate ($0.008 per minute).
* **Windows:** 2x rate multiplier ($0.016 per minute).
* **macOS:** 10x rate multiplier ($0.084 per minute) due to high infrastructure overhead.

### 3. Self-Hosted Runner Cost Savings
Running workflows on your own local infrastructure or virtual machines (`self-hosted`) is **completely free**. GitHub does not charge for minutes executed on self-hosted runners.

---

## 🏢 GitHub Enterprise Architectures

For large corporations requiring high security, isolation, and compliance auditing, GitHub provides Enterprise solutions:

| Feature | GitHub Enterprise Cloud | GitHub Enterprise Server |
| :--- | :--- | :--- |
| **Hosting Model** | Cloud-hosted by GitHub (SaaS). | On-Premise VM (self-hosted in own Data Center / Cloud). |
| **Authentication** | SAML Single Sign-On (SSO). | SAML / LDAP / Active Directory. |
| **Compliance Standards**| HIPAA, SOC2, GDPR, ISO. | Controlled internally on company servers. |
| **Hybrid Connectivity** | Standard cloud endpoints. | Connects to cloud via **GitHub Connect** tunnels. |
