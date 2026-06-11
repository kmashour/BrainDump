---
domains:
  - "jenkins"
---

# Module 5-3: Jenkins Administration & Troubleshooting

This module covers upgrading plugins, debugging compiler failures, and CD deployment stages.

---

## 1. Jenkins Upgrade & Dependency Management

Jenkins server health requires keeping plugins updated.
*   **Upgrades:** Always update the Jenkins core WAR file first, followed by plugin dependency chains.
*   **Backups:** Retain copies of `$JENKINS_HOME/*.xml` and `jobs/` configurations.

---

## 2. Debugging Pipeline Failures

#### Deep-Intuition (AARF) Breakdown:
1. **The Answer (Core Pattern):** Configure workspace cleanup post-steps and capture build artifacts to identify compiler failures:
    ```groovy
    post {
        always {
            cleanWs()
        }
    }
    ```
2. **The Assumptions (Context):** The agent disk space must be monitored, and file retention policies must be set to prevent disk filling.
3. **The Rationale (Why):** Workspace cleanups ensure subsequent builds run on a clean workspace, preventing residual files from corrupting compilation state.
4. **The Failure Loop (What if not):** Without workspace cleanups, transient build artifacts from past failed runs contaminate subsequent builds, producing false positives or hidden library version dependencies that crash in production.
5. **Alternative Case (When to use 'if not'):** Retaining target folders is acceptable when cache retention is needed to speed up compilation.
