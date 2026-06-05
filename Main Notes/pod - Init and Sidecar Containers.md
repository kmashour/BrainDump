---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[pod]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/workloads/pods/init-containers/"
author: "Kubernetes Authors"
course_title: "CKA Exam Prep"
tags:
  - kubernetes/pod
  - container/sidecar
---

# pod - Init and Sidecar Containers

**Breadcrumbs:** [[Index|🏠 Index]] > [[pod]] > **Init and Sidecar Containers**

---

## 📑 Init and Sidecar Containers

Kubernetes supports sequential initialization tasks and native helper processes through specialized container lifecycles.

### 1. Init Containers
Init containers run sequentially to completion before any application containers start. If an init container fails, the Kubelet restarts it until it succeeds (unless the Pod `restartPolicy` is `Never`).

### 2. Native Sidecar Containers (restartPolicy: Always)
Introduced as a native feature, sidecar containers run alongside main application containers but start *before* them and stop *after* them.
* **Definition:** Configured in `spec.initContainers` but defined with `restartPolicy: Always`.
* **Execution:** Starts and blocks subsequent init container execution until its startup/readiness probe succeeds.

### 3. Resource Scheduling Math
* **Standard Init:** The Pod request/limit is calculated as the `Max(sum of app containers, highest init container)`.
* **Native Sidecar:** Because sidecar containers run concurrently with app containers, the pod scheduling calculation is modified:
  $$\text{Pod Request} = \text{Sum(App Containers)} + \text{Sum(Active Sidecars)}$$
  This sum is compared against the standard sequential init container values to select the absolute maximum.

*Read more in [07_kubernetes_workloads_and_controllers.md](../Reference%20Notes/07_kubernetes_workloads_and_controllers.md#3-init-containers-and-native-sidecars)*
