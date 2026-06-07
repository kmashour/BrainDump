---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: control-plane
domains:
  - "kubernetes"
related_concepts:
  - "[[pod]]"
  - "[[resourcequota]]"
against:
  - "[[resourcequota]]"
reference_guides:
  - "[[Reference Notes/03_node_mechanics_and_resource_limits.md]]"
tags:
  - kubernetes/policy
  - status/completed
---

# LimitRange

**Breadcrumbs:** [[0-Index|🏠 Index]] > infra > **LimitRange**

---

## 🎯 Purpose (Why it is used)
A **LimitRange** is a policy resource that enforces resource allocation constraints (such as minimum/maximum CPU and memory requests/limits) for containers or pods within a single namespace. It prevents individual containers from requesting excessively high or low allocations.

---

## ⚙️ Functionality (What it is doing)
*   **Default Injection:** Automatically injects default resource requests and limits into containers that do not specify them in their manifests.
*   **Enforcement Gates:** Blocks pods from starting if their container resource allocations fall outside the specified minimum and maximum bounds.
*   **Ratio Enforcement:** Can restrict the ratio of request to limit for specific resources.

---

## 🏛️ Architectural Context (How it fits in the architecture)
*   **Admission Control:** Validated by the `LimitRanger` admission plug-in inside the `kube-apiserver` during the pod admission phase.
*   **Namespace Bound:** Applies strictly within the namespace where it is defined.

---

## 🧩 Problem Solver (What problem it solves)
In a shared cluster, developers might accidentally deploy pods without setting resource parameters, causing those pods to exhaust node compute. Alternatively, a pod might request excessive resources it doesn't need. LimitRange solves this by automatically setting defaults and validating boundary limits.

---

## 🟢 Operational Impact (What will happen with it operating)
*   **Safe Defaults:** Workloads without specified limits receive appropriate default parameters.
*   **Predictable Scheduling:** Scheduler receives accurate sizing allocations, improving bin-packing efficiency.

---

## 🔴 Failure Impact (What will happen without it)
*   **Resource Hogging:** Containers can claim unlimited compute, starvings neighbors.
*   **Unscheduled Workloads:** Containers with tiny requests but huge memory utilization can cause nodes to hit OOM limits unexpectedly.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **LimitRange**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[limitrange]]
SORT file.name ASC
```
