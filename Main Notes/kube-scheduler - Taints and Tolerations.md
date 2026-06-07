---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kube-scheduler]]"
sub_type: core-concept
source_type: udemy
author: "Mumshad Mannambeth"
course_title: "Certified Kubernetes Administrator (CKA)"
tags:
  - kubernetes/kube-scheduler
  - kubernetes/deep-dive
---

# kube-scheduler - Taints and Tolerations

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[kube-scheduler]] > **Taints and Tolerations**

---

## 📑 Taints and Tolerations Mechanics

While node affinity attracts Pods to a set of nodes, **Taints and Tolerations** allow nodes to **repel** Pods. They guarantee that workloads are not scheduled on dedicated or sensitive nodes (like control plane nodes).

*   **Taints** are applied to **Nodes**.
*   **Tolerations** are applied to **Pods**.

---

## ⚙️ Core Operations

### 1. Tainting a Node
To apply a taint to a node:
```bash
kubectl taint nodes <node-name> dedicated=special-user:NoSchedule
```
To remove a taint from a node, append a hyphen `-` to the end of the taint-effect:
```bash
kubectl taint nodes <node-name> dedicated=special-user:NoSchedule-
```

### 2. Taint Effects
*   **`NoSchedule` (Hard repel):** The scheduler will not place the Pod on this node unless it tolerates the taint. Existing running Pods on the node are unaffected.
*   **`PreferNoSchedule` (Soft repel):** The scheduler will try to avoid placing the Pod on this node, but can do so as a last resort if no other nodes are available.
*   **`NoExecute` (Eviction repel):** If applied to a node, any running Pods that do not tolerate this taint are immediately evicted from the node.

---

## 🧩 Pod Toleration Syntax

Define tolerations inside the Pod's `spec.tolerations` block:

### Example: Operator Equal
Matches key, value, and effect exactly.
```yaml
spec:
  containers:
  - name: nginx
    image: nginx
  tolerations:
  - key: "dedicated"
    operator: "Equal"
    value: "special-user"
    effect: "NoSchedule"
```

### Example: Operator Exists
Matches the key regardless of the value.
```yaml
tolerations:
- key: "dedicated"
  operator: "Exists"
  effect: "NoSchedule"
```

### Example: `tolerationSeconds` (with `NoExecute`)
Determines how long a Pod can stay on a node after a `NoExecute` taint is applied (e.g., when a node becomes unreachable):
```yaml
tolerations:
- key: "node.kubernetes.io/unreachable"
  operator: "Exists"
  effect: "NoExecute"
  tolerationSeconds: 300
```

---

## ⚖️ Taints vs. Node Affinity Combinations

*   **Taints only:** repels untolerated Pods, but tolerated Pods can still schedule on other nodes.
*   **Affinity only:** attracts Pods to specific nodes, but other Pods can still schedule there.
*   **Dedicating Nodes (Taint + Affinity):** To fully dedicate a node to a specific team:
    1.  **Taint the node:** Prevents other teams' pods from scheduling on it.
    2.  **Add Affinity to target Pods:** Attracts the target pods to these nodes.
    3.  **Add Toleration to target Pods:** Allows them to run on the tainted node.

*Read more in [14_scheduling_logging_and_lifecycle.md](../Reference%20Notes/14_scheduling_logging_and_lifecycle.md#c-taints-and-tolerations-repelling-workloads)*
