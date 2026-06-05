---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[deployment]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#strategy"
author: "Kubernetes Authors"
course_title: "CKA Exam Prep"
tags:
  - kubernetes/deployment
  - deployment/strategy
---

# deployment - Rolling Update and Rollback Strategy

**Breadcrumbs:** [[Index|🏠 Index]] > [[deployment]] > **Rolling Update and Rollback Strategy**

---

## 📑 Rolling Update and Rollback Strategy

The Deployment controller automates zero-downtime updates through precise rollout strategies.

### 1. Rollout Strategies
* **`RollingUpdate` (Default):** Replaces pods in an incremental fashion.
  * **`maxSurge`:** The maximum number of pods that can be scheduled above the desired replica count (e.g. `25%` or `1`).
  * **`maxUnavailable`:** The maximum number of pods that can be offline during the update.
* **`Recreate`:** Terminates all active pods before launching any new replicas. Used when multiple versions of an application cannot share the database schema.

### 2. Rollout and Rollback Commands
Manage rollouts via the command-line:
```bash
# Check rollout status
kubectl rollout status deployment/web-deployment

# View revision history
kubectl rollout history deployment/web-deployment

# Revert to the previous stable release
kubectl rollout undo deployment/web-deployment

# Revert to a specific historical revision
kubectl rollout undo deployment/web-deployment --to-revision=2
```

*Read more in [07_kubernetes_workloads_and_controllers.md](../Reference%20Notes/07_kubernetes_workloads_and_controllers.md#8-deployments)*
