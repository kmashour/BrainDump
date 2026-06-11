---
domains:
  - "jenkins"
---

# Module 5-2: Jenkins Build Triggers & Variables

This module covers triggering automation workflows and manipulating pipeline data.

---

## 1. Pipeline Variables & Parameters

Declarative pipelines consume variables to customize compilation targets.
*   **Default Variables:** Environment properties exposed by Jenkins (e.g., `BUILD_NUMBER`, `BRANCH_NAME`).
*   **Custom Parameters:** Interactive prompts configured inside the pipeline (e.g., `parameters { choice(name: 'ENV', choices: ['dev', 'prod']) }`).

---

## 2. Jenkins Triggering Configurations

CI/CD automation requires triggering builds from developer code commits.

#### Deep-Intuition (AARF) Breakdown:
1. **The Answer (Core Pattern):** Standardize on Webhook-based API triggers (via Git integrations) instead of polling configurations:
    ```groovy
    pipeline {
        triggers {
            githubPush()
        }
    }
    ```
2. **The Assumptions (Context):** The GitHub repository must configure a Webhook pointing to `https://jenkins-server/github-webhook/` with port/HTTPS routing allowed.
3. **The Rationale (Why):** Decouples the build server from polling. The VCS pushes an event notification instantly upon code commits, triggering execution immediately.
4. **The Failure Loop (What if not):** Setting Jenkins to poll GitHub repositories periodically (e.g., every 5 minutes: `pollSCM('*/5 * * * *')`) causes a 5-minute lag for feedback. Additionally, frequent polling on large codebases exhausts VCS API rate limits and generates useless server disk I/O.
5. **Alternative Case (When to use 'if not'):** For nightly regression test runs or security scans, use cron schedules (`cron('H 0 * * *')`) instead of webhook triggers.
