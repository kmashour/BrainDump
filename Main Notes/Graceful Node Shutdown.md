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

# Graceful Node Shutdown

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Worker Node Mechanics > **Graceful Node Shutdown**

---

## 🎯 Purpose (Why it is used)
Graceful Node Shutdown allows a worker node to detect a host shutdown command and cleanly terminate running workloads. Instead of leaving container processes to crash or lock up resources, the Kubelet coordinates a structured eviction sequence to preserve application state.

---

## ⚙️ Functionality (What it is doing)
1. **Shutdown Detection:** Listens to D-Bus signals from systemd `logind` to detect an impending OS shutdown or reboot.
2. **Inhibitor Lock Request:** Utilizes systemd inhibitor locks to delay the OS power-off event.
3. **Pod Eviction:** Rejects new incoming pods and begins terminating currently running pods.
4. **Termination Phases:** Sequentially terminates standard workloads first, followed by a dedicated grace window for critical control plane/daemon pods.
5. **Status Update:** Updates the state of evicted pods to `Failed` in the API server.

---

## 🏛️ Architectural Context (How it fits in the architecture)
This feature bridges the host-level operating system daemon (`systemd-logind`) and the container management layer (`kubelet`). It ensures coordination between host hardware power state transitions and Kubernetes pod lifecycles.

---

## 🧩 Problem Solver (What problem it solves)
Without Graceful Node Shutdown, an OS reboot kills container engines immediately, leaving stateful data in an inconsistent state and leaving cloud volumes attached to dead VMs. By delaying shutdown, Kubelet cleanly terminates database connections, commits state, and allows network traffic to drain from endpoint lists.

---

## 🟢 Operational Impact (What will happen with it operating)
* **Zero Workload Corruption:** Workloads are given up to the configured `shutdownGracePeriod` duration to save state and exit cleanly.
* **Accurate Pod Statuses:** Pod states are marked as `Failed` (due to node shutdown) rather than lingering as `Running` on a dead node.

---

## 🔴 Failure Impact (What will happen without it)
* **State and Data Loss:** Container storage and databases suffer sudden power-off events, leading to file system corruption or data loss.
* **Stuck Volume Mounts:** Cloud storage disks (e.g. EBS) remain locked to the shut-down VM, causing long scheduler delays when rescheduled pods try to mount them elsewhere.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Graceful Node Shutdown**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
