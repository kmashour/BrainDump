---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[replicaset]]"
sub_type: pitfall
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/"
author: "Kubernetes Authors"
course_title: "CKA Exam Prep"
tags:
  - kubernetes/replicaset
  - kubernetes/deep-dive
  - troubleshooting/thrashing
---

# replicaset - MatchExpressions and Thrashing

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[replicaset]] > **MatchExpressions and Thrashing**

---

## 📑 Set-Based Selectors & matchExpressions

While legacy Replication Controllers only supported equality-based selectors (e.g. `app: nginx`), ReplicaSets support set-based selectors using `matchExpressions`. This allows complex filtering using operators:
*   **`In`**: Label value must match one of the specified values.
*   **`NotIn`**: Label value must not match any of the specified values.
*   **`Exists`**: Label key must exist (no `values` array).
*   **`DoesNotExist`**: Label key must not exist (no `values` array).

*Example config:*
```yaml
selector:
  matchExpressions:
    - {key: tier, operator: In, values: [frontend, api]}
    - {key: partition, operator: Exists}
```

---

## ⚙️ Ownership, Adoption, and Orphaning

ReplicaSets do not maintain static lists of Pods. They query the API server dynamically for Pods matching their selectors.

1.  **`ownerReferences`:** When the controller manager creates a Pod for a ReplicaSet, it injects an `ownerReference` field into the Pod's metadata containing the ReplicaSet's UUID.
2.  **Adoption:** If a ReplicaSet finds matching Pods that are orphaned (they have no controller `ownerReference`), it **adopts** them by updating their `ownerReferences` to point to itself, counting them toward its active replica count.
3.  **Orphaning:** If you delete a ReplicaSet with the `--cascade=orphan` flag:
    ```bash
    kubectl delete rs my-replicaset --cascade=orphan
    ```
    The controller manager removes the `ownerReferences` from all managed Pods. These Pods keep running as orphaned workloads.

---

## ⚠️ Controller Collision and Thrashing Loops

Runaway Pod creation and deletion loops (thrashing) are typically triggered by two cluster-level anomalies:

### Scenario A: Overlapping Selectors (Controller Collision)
If two controllers (e.g. two ReplicaSets) have overlapping selectors but point to different templates (e.g. different images):
1.  ReplicaSet-B queries for `app: nginx` and finds Pods created by ReplicaSet-A.
2.  Because they belong to ReplicaSet-A, ReplicaSet-B cannot adopt them, calculating it has 0 replicas.
3.  ReplicaSet-B spins up 3 new Pods. The namespace now has 6 matching Pods.
4.  ReplicaSet-A wakes up, finds 6 Pods matching its selector, and scales down by deleting 3 excess Pods (without checking `ownerReferences` during scale down). It might delete ReplicaSet-B's Pods.
5.  ReplicaSet-B wakes up, finds its Pods are gone, and creates 3 new ones.
6.  This triggers an infinite creation/deletion loop (**thrashing**), causing heavy API Server CPU load.

**Resolution:** Update selectors in the manifests to ensure they are unique (e.g., adding a unique `tier` or `environment` label).

### Scenario B: Mutating Admission Webhook Interference
1.  A mutating admission webhook intercepts Pod creation requests.
2.  When the ReplicaSet submits a Pod matching its selector (e.g. `app: frontend`), the webhook modifies or strips the label.
3.  The Pod is created but lacks the label.
4.  The ReplicaSet queries the API server, sees a deficit because the new Pod does not match its selector, and submits another Pod creation request.
5.  This creates hundreds of orphaned Pods in a loop.

**Resolution:** Inspect mutating admission webhook configurations and check Pod label metadata.

*Read more in [07_kubernetes_workloads_and_controllers.md](../Reference%20Notes/07_kubernetes_workloads_and_controllers.md#83-set-based-selectors--matchexpressions-syntax)*
