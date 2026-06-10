---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: worker-node
domains:
  - "kubernetes"
  - "linux"
related_concepts:
  - "[[kubelet]]"
  - "[[node]]"
reference_guides:
  - "[[Reference Notes/0-14_cluster_administration_and_observability.md]]"
tags:
  - kubernetes/component
  - status/completed
against: []
---

# Swap Management

**Breadcrumbs:** [[0-Index|🏠 Index]] > Worker Node Mechanics > **Swap Management**

---

## 🎯 Purpose (Why it is used)
Swap memory management enables worker nodes to write inactive memory pages to disk. This helps absorb sudden memory spikes, shields nodes from Out-Of-Memory (OOM) kernel panics, and allows more cost-effective allocations for memory-heavy but sparsely-accessed workloads.

---

## ⚙️ Functionality (What it is doing)
1. **Swap Toleration:** Configures Kubelet (`failSwapOn: false`) to startup on hosts where OS swap space is provisioned.
2. **Cgroups v2 Resource Limiting:** Uses Linux control groups (cgroups v2) to set the `memory.swap.max` constraint for specific container directories.
3. **Behavior Customization:** 
   - **`NoSwap`:** Restricts Kubernetes pods from using swap while letting host-level daemons swap out cold pages.
   - **`LimitedSwap`:** Allows workloads to utilize a portion of swap relative to their physical memory requests and limits.
4. **Metric Reporting:** Exposes swap consumption details to `/metrics/resource` and `/stats/summary`.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Swap management is configured at the node layer inside the `KubeletConfiguration` and enforced at the kernel layer by cgroups v2. Container runtime engines (like containerd) interpret the swap allocation request and write limits directly into the filesystem-based cgroup paths.

---

## 🧩 Problem Solver (What problem it solves)
Historically, any sudden RAM spike on a node triggered immediate pod eviction or a host crash. Tolerating swap gives pods a buffer zone, converting hard memory out-of-bounds errors into slight performance downgrades while workloads swap cold pages to disk.

---

## 🟢 Operational Impact (What will happen with it operating)
* **Node Stability:** Workers survive short-lived memory saturation events.
* **Cost Efficiency:** Higher density of workloads can be scheduled by overcommitting physical RAM.

---

## 🔴 Failure Impact (What will happen without it)
* **Aggressive Evictions:** Pods exceeding memory requests are killed immediately via `OOMKilled` signals under resource pressure.
* **No Host Buffer:** Kernel panics can occur if host daemons cannot swap memory during kernel-level memory exhaustion.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Swap Management**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[Swap Management]]
SORT file.name ASC
```
