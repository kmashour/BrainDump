---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "linux"
related_concepts:
  - "[[Main Notes/process-supervision.md]]"
  - "[[Main Notes/container-runtime.md]]"
against:
  - "[[Main Notes/aws.md]]"
reference_guides:
  - "[[Reference Notes/8-Index - Linux and OS.md]]"
tags:
  - linux/os
  - status/completed
---

# Linux and Operating Systems

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > **Linux & OS**

---

## 🎯 Purpose (Why it is used)
The Linux operating system serves as the foundational environment for modern containerized architectures and cloud infrastructure services, managing physical execution hardware and exposing system resources via standard API interfaces.

---

## ⚙️ Functionality (What it is doing)
*   **Resource Allocation:** Governs physical and virtual memory allocation, CPU process scheduling, and block/network I/O routing.
*   **Isolation Boundaries:** Separates software boundaries via namespaces and control groups to run containers securely on shared hardware.
*   **Service Supervision:** Spawns and manages system daemons, initializes user spaces (PID 1), and reaps terminated processes.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Linux interfaces directly with host hardware or virtualization hypervisors, exposing system services to container runtimes (like `containerd` or `cri-o`) which in turn host cluster workloads managed by Kubernetes.

---

## 🧩 Problem Solver (What problem it solves)
Without a modern preemptive kernel, applications would compete directly for raw hardware resources, causing memory write conflicts, un-throttled CPU starvation, and service collisions.

---

## 🟢 Operational Impact (What will happen with it operating)
Processes are scheduled fairly, memory is virtualized and protected, network packets are routed via Netfilter hooks, and filesystems are abstracted under a common VFS.

---

## 🔴 Failure Impact (What will happen without it)
Kernel panics, CPU locks, or resource exhaustion results in host crashes, terminating all containerized workloads, breaking Kubernetes scheduling, and causing cluster service outages.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes associated with Linux and OS.

```dataview
TABLE sub_type AS "Type", tags AS "Tags"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[linux]]
SORT file.name ASC
```
