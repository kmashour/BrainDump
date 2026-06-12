---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[pod-deeper]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/"
author: "Kubernetes Documentation"
tags:
  - kubernetes/pod
  - kubernetes/deep-dive
---

# pod - Quality of Service (QoS) Classes

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[pod]] > [[pod-deeper]] > **QoS Classes**

---

## 📑 1. The Three QoS Classes
Kubernetes classifies Pods into three QoS levels to determine scheduling priority and eviction order when resources are constrained.

```text
EVICTION PRIORITY (Under Host Resource Pressure):
  [ BestEffort ]   --> Evicted First
        |
  [ Burstable ]    --> Evicted Second
        |
  [ Guaranteed ]   --> Evicted Last
```

---

## ⚙️ 2. Class Definitions and YAML Specs

### A. Guaranteed
Every container in the Pod must have both requests and limits specified for CPU and memory, and the **request must equal the limit**.
```yaml
spec:
  containers:
  - name: web-app
    resources:
      requests:
        memory: "250Mi"
        cpu: "500m"
      limits:
        memory: "250Mi" # Must equal request
        cpu: "500m"    # Must equal request
```

### B. Burstable
The Pod does not meet the criteria for Guaranteed, but at least one container has a CPU or memory request.
```yaml
spec:
  containers:
  - name: db-app
    resources:
      requests:
        memory: "250Mi"
```

### C. BestEffort
No requests or limits are specified for any container.
```yaml
spec:
  containers:
  - name: worker
    # resources block is omitted completely
```

---

## 🔬 3. OOM Score Adjustments
Kubelet assigns an Out-Of-Memory score adjustment (`oom_score_adj`) to each container based on its QoS class:
* **Guaranteed:** `-997` (almost never selected for host OOM killing).
* **BestEffort:** `1000` (evicted/killed first if host RAM is exhausted).
* **Burstable:** Calculated dynamically based on the percentage of requested memory.

*Read more in [[Reference Notes/0-3_node_mechanics_and_resource_limits.md#4-quality-of-service-qos-classes]]*\n