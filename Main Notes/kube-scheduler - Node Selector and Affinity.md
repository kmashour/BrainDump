---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kube-scheduler-deeper]]"
sub_type: core-concept
source_type: udemy
author: "Mumshad Mannambeth"
course_title: "Certified Kubernetes Administrator (CKA)"
against: []
tags:
  - kubernetes/kube-scheduler
  - kubernetes/deep-dive
---

# kube-scheduler - Node Selector and Affinity

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[kube-scheduler]] > [[kube-scheduler-deeper]] > **Node Selector and Affinity**

---

## 📑 Node Placement Mechanisms

Kubernetes provides multiple ways to attract Pods to specific worker nodes using node labels.

---

## ⚙️ 1. Node Selector (`nodeSelector`)

`nodeSelector` is the simplest form of node selection constraint. It uses equality-based key-value matching.
*   **Node Labeling:**
    ```bash
    kubectl label nodes worker-1 size=Large
    ```
*   **Pod Manifest:**
    ```yaml
    spec:
      containers:
      - name: nginx
        image: nginx
      nodeSelector:
        size: Large
    ```
*   **Constraint:** If no nodes match the exact label key-value pair, the Pod remains `Pending`.

---

## ⚙️ 2. Node Affinity (`nodeAffinity`)

Node Affinity expands on `nodeSelector` by offering set-based matching operators and defining soft/hard constraints.

### A. Core Types
1.  **`requiredDuringSchedulingIgnoredDuringExecution` (Hard Constraint):**
    *   The scheduler **must** find a node matching the rules to schedule the Pod.
    *   If no matching node is found, the Pod stays `Pending`.
2.  **`preferredDuringSchedulingIgnoredDuringExecution` (Soft Constraint):**
    *   The scheduler will try to schedule the Pod on a node matching the rules, but will schedule it elsewhere if no matches are found.
    *   Includes a `weight` parameter (1-100) to prioritize nodes.

### B. Operator Logic
Node affinity supports multiple set-based operators in `matchExpressions`:
*   `In`: Label value must be in the specified list.
*   `NotIn`: Label value must not be in the specified list (can be used to repel pods).
*   `Exists`: Label key must exist on the node, regardless of its value.
*   `DoesNotExist`: Label key must not exist on the node.
*   `Gt` / `Lt`: Label value is compared numerically.

---

## 🧩 Pod Manifest Example

```yaml
spec:
  containers:
  - name: web
    image: nginx
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: topology.kubernetes.io/zone
            operator: In
            values:
            - us-east-1a
            - us-east-1b
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 80
        preference:
          matchExpressions:
          - key: disktype
            operator: In
            values:
            - ssd
```

---

## ⚠️ IgnoredDuringExecution Context

For both Node Selector and Node Affinity, the suffix **`IgnoredDuringExecution`** means that if node labels change while a Pod is already running on that node (such that the affinity rules no longer match), the running Pod **will not be evicted**; it continues to run. Only new scheduling decisions evaluate the rules.

*   **Future/Planned Execution Phase (`RequiredDuringExecution`):**
    Kubernetes architecture designs include plans to support the suffix **`RequiredDuringExecution`** in the future. Under this policy, if a node's labels are changed during runtime such that a running Pod's hard affinity requirements are no longer satisfied, the system will immediately evict that Pod from the node.

*Read more in [0-13_scheduling_logging_and_lifecycle.md](../Reference%20Notes/0-13_scheduling_logging_and_lifecycle.md#d-node-selectors-and-node-affinity-attracting-workloads)*
