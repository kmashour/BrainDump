---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: workload
domains:
  - "kubernetes"
related_concepts:
  - "[[cronjob]]"
  - "[[pod]]"
against:
  - "[[deployment]]"
reference_guides:
  - "[[Reference Notes/0-6_kubernetes_workloads_and_controllers.md]]"
tags:
  - kubernetes/controller
  - status/completed
---

# job

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Workloads & Infrastructure > **job**

---

## 🎯 Purpose (Why it is used)
The `Job` controller creates one or more Pods and ensures that a specified number of them successfully terminate (exit with `0`). It is designed for run-to-completion batch tasks (e.g. database migrations, backups, calculations).

---

## ⚙️ Functionality (What it is doing)
* **Run-to-Completion Guard:** Monitors pod exits. If a pod exits with a non-zero code, the Job restarts it (up to `spec.backoffLimit`).
* **Parallel Execution:** Manages concurrent pod runs via `spec.parallelism` and tracks target completions via `spec.completions`.
* **Execution Limit:** Evicts and terminates pods if they exceed the maximum runtime limit (`spec.activeDeadlineSeconds`).

---

## 🏛️ Architectural Context (How it fits in the architecture)
* **Batch Controller:** Managed under `kube-controller-manager`. Differs from Deployments because its pods are expected to stop running rather than remain active.
* **Restart Policy restriction:** Requires the Pod template restart policy to be `OnFailure` or `Never`.

---

## 🧩 Problem Solver (What problem it solves)
* **Automated Batch Verification:** Solves manual check tasks. If a batch script fails halfway due to network drop, the Job controller automatically restarts and retries the process.
* **Orchestrated Parallel Processing:** Solves slow batch executions by distributing tasks across multiple concurrent pods.

---

## 🟢 Operational Impact (What will happen with it operating)
* Database schema upgrades run and exit cleanly during deployments.
* Large data conversion operations complete quickly by scaling horizontally.

---

## 🔴 Failure Impact (What will happen without it)
* Batch scripts must run on worker nodes manually or via ssh/ansible, lacking automatic error retries, tracking, and scaling limits.
* Script crashes go unnoticed unless external logging platforms catch them.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **job**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[job]]
SORT file.name ASC
```
