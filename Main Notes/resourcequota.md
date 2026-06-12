---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: control-plane
domains:
  - "kubernetes"
related_concepts:
  - "[[pod]]"
  - "[[limitrange]]"
against:
  - "[[limitrange]]"
reference_guides:
  - "[[Reference Notes/0-3_node_mechanics_and_resource_limits.md]]"
tags:
  - kubernetes/policy
  - status/completed
---

# ResourceQuota

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > infra > **ResourceQuota**

---

## 🎯 Purpose (Why it is used)
A **ResourceQuota** limits the aggregate resource consumption (CPU, memory, storage, and object counts) across all objects within a single namespace. It prevents one team or environment from monopolizing cluster-wide resources.

---

## ⚙️ Functionality (What it is doing)
*   **Compute Caps:** Restricts the total sum of CPU and memory requests/limits in a namespace.
*   **Storage Caps:** Restricts the total sum of persistent volume storage requests.
*   **Object Caps:** Restricts the total count of specific resources (e.g. maximum of 20 Pods, 10 Services, 10 Secrets).

---

## 🏛️ Architectural Context (How it fits in the architecture)
*   **Admission Control:** Enforced by the `ResourceQuota` admission plug-in inside the `kube-apiserver`.
*   **State Tracking:** API server tracks active resource totals, rejecting creations that cross quota thresholds.

---

## 🧩 Problem Solver (What problem it solves)
Without quotas, a single rogue namespace could deploy hundreds of pods, consume all cluster memory, or exhaust all available IP addresses in a CNI subnet. Quotas solve this by isolating namespaces inside resource quotas.

---

## 🟢 Operational Impact (What will happen with it operating)
*   **Fair Resource Share:** Multiple teams co-exist on a single cluster without resource exhaustion issues.
*   **Cost Management:** Prevents run-away auto-scaling and cloud billing spikes.

---

## 🔴 Failure Impact (What will happen without it)
*   **Cluster Depletion:** A single user can exhaust the entire cluster CPU, memory, or storage pool, starving other system operations.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **ResourceQuota**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
