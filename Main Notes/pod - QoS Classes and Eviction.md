---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[pod-deeper]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/"
author: "Kubernetes Authors"
course_title: "CKA Exam Prep"
tags:
  - kubernetes/pod
  - scheduling/qos
---

# pod - QoS Classes and Eviction

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[pod]] > [[pod-deeper]] > **QoS Classes and Eviction**

---

## 📑 QoS Classes and Eviction

Kubernetes categorizes Pods into three Quality of Service (QoS) classes based on their CPU/Memory requests and limits, which dictates their scheduling and node-level eviction priorities.

### 1. QoS Class Classifications
* **Guaranteed:** Every container in the Pod must have both requests and limits configured, and they must be exactly equal (`CPU Request = CPU Limit` and `Memory Request = Memory Limit`).
* **Burstable:** At least one container has a CPU/Memory request configured, but requests do not equal limits (or limits are unset).
* **BestEffort:** No container has any requests or limits configured.

### 2. Node-Level Eviction Order
When a Kubernetes worker node experiences resource pressure (e.g. Memory Pressure), the Kubelet evicts Pods to protect the node OS. Evictions follow a strict priority sequence based on QoS class and usage:

$$\text{Eviction Order:} \quad \text{BestEffort} \longrightarrow \text{Burstable} \longrightarrow \text{Guaranteed}$$

* **BestEffort:** Evicted first.
* **Burstable:** Evicted next, ordered by those consuming the most memory above their declared requests.
* **Guaranteed:** Evicted last, only if system daemons (`kubelet`, `docker`) are at risk of crash.

*Read more in [0-6_kubernetes_workloads_and_controllers.md](../Reference%20Notes/0-6_kubernetes_workloads_and_controllers.md#2-resource-specifications-and-qos-classes)*
