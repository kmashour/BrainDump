---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: control-plane
domains:
  - "kubernetes"
related_concepts:
  - "[[pod]]"
  - "[[kube-apiserver]]"
against:
  - "[[hpa]]" # Vertical scaling vs Horizontal scaling
reference_guides:
  - "[[Reference Notes/0-6_kubernetes_workloads_and_controllers.md]]"
tags:
  - kubernetes/component
  - status/completed
---

# Vertical Pod Autoscaler

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > workloads > **Vertical Pod Autoscaler**

---

## 🎯 Purpose (Why it is used)
The **Vertical Pod Autoscaler (VPA)** automatically adjusts the CPU and memory requests and limits for containers in a pod. By monitoring actual resource utilization, it rightsizes workloads to optimize cluster resource allocation, prevent Out-of-Memory (OOM) crashes, and eliminate the need for manual capacity provisioning.

---

## ⚙️ Functionality (What it is doing)
*   **Capacity Telemetry Analysis:** Recommender monitors live and historical node cgroups metrics via the metrics API (`metrics.k8s.io`).
*   **Dynamic Resource Recommendation:** Calculates optimal CPU/Memory configurations (`Target`, `LowerBound`, `UpperBound`) for container limits and requests.
*   **Suboptimal Pod Eviction:** Updater terminates active running Pods whose current resource configurations deviate significantly from the recommended target.
*   **Pod Spec Mutation:** Admission Controller intercepts Pod creation requests (e.g. from Deployment controller) and injects recommended CPU and memory resource values before the Pod is scheduled.
*   **In-Place Resizing Integration:** In future releases, VPA Auto mode will scale running container resource limits dynamically in-place without restarting pods.

---

## 🏛️ Architectural Context (How it fits in the architecture)
*   **Metrics Server:** Provides the cluster-level CPU/Memory utilization values that the VPA Recommender polls.
*   **VPA Recommender:** Standalone controller that analyzes metrics and updates the `verticalpodautoscaler` custom resource status.
*   **VPA Updater:** Standalone controller that handles evicting pods that need updates.
*   **VPA Admission Webhook:** Mutating admission webhook that injects recommended resource sizes.
*   **Deployment / ReplicaSet Controller:** Re-creates Pods evicted by the Updater, triggering the Mutating Webhook.

---

## 🧩 Problem Solver (What problem it solves)
Without VPA, administrators must manually monitor workloads and update Deployment specs to avoid resource wastage (over-provisioning) or application instability (under-provisioning resulting in OOM kills). VPA automates this sizing lifecycle, optimizing hardware costs and workload reliability.

---

## 🟢 Operational Impact (What will happen with it operating)
*   **Minimized Wastage:** Unused CPU and memory requests are reclaimed, increasing cluster density.
*   **Downtime Risk (Recreate/Auto):** Unless Pod Disruption Budgets (PDBs) and multiple replicas are configured, evicting pods to resize them causes brief application downtime.
*   **Automatic Stabilization:** Highly-utilized containers are automatically upgraded to larger resource boundaries.

---

## 🔴 Failure Impact (What will happen without it)
*   **OOM Crashes:** Heavy workloads (like databases or Java engines) will exceed memory limits and crash with `OOMKilled` status.
*   **Resource Exhaustion:** Over-provisioned static workloads will lock down CPU/Memory allocations, starving other cluster resources.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Vertical Pod Autoscaler**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
