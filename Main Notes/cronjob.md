---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: workload
domains:
  - "kubernetes"
related_concepts:
  - "[[job]]"
  - "[[pod]]"
against:
  - "[[job]]"
reference_guides:
  - "[[Reference Notes/07_kubernetes_workloads_and_controllers.md]]"
tags:
  - kubernetes/controller
  - status/completed
---

# cronjob

**Breadcrumbs:** [[Index|🏠 Index]] > Workloads & Infrastructure > **cronjob**

---

## 🎯 Purpose (Why it is used)
The `CronJob` controller manages time-based, periodic Jobs. It executes tasks according to a cron schedule (e.g. database backups, report generation, system cleanup scripts).

---

## ⚙️ Functionality (What it is doing)
* **Schedule Engine:** Uses standard cron syntax (e.g. `*/5 * * * *`) to trigger new executions.
* **Job Spawner:** Creates a matching `Job` resource at each scheduled tick.
* **Concurrency Governance:** Restricts execution using `concurrencyPolicy`:
  - `Allow`: Runs overlapping jobs.
  - `Forbid`: Skips the tick if the previous run is still active.
  - `Replace`: Kills the running job and starts a new one.
* **History Retention:** Automatically purges old job records to prevent resource exhaustion based on `successfulJobsHistoryLimit` and `failedJobsHistoryLimit`.
* **DNS Naming Constraint:** A CronJob's name must not exceed **52 characters** because the controller automatically appends an 11-character timestamp suffix to child Job names, which are capped at 63 characters.

---

## 🏛️ Architectural Context (How it fits in the architecture)
* **Periodic Controller:** Sits directly above the `Job` resource. The `cronjob-controller` in the controller manager polls the schedules and spawns `Jobs`.
* **Execution window:** Skips runs if the scheduler is down for longer than `spec.startingDeadlineSeconds`.

---

## 🧩 Problem Solver (What problem it solves)
* **Centralized Task Scheduling:** Solves the challenge of managing OS-level crontabs across multiple nodes. Instead of maintaining `/etc/crontab` on VMs, schedules are stored declaratively inside the cluster.
* **Overlapping Job Control:** Solves the problem of server overload. If a daily database backup is slow and runs into the next day, `Forbid` prevents starting a second concurrent backup.

---

## 🟢 Operational Impact (What will happen with it operating)
* Dynamic system cleanups, SSL renewals, and automated reporting tasks run periodically.
* Resource leaks are blocked through automatic history pruning.

---

## 🔴 Failure Impact (What will happen without it)
* Periodic tasks must be run using VM-level cron daemons, losing centralized logs, resource limits, and error restart logic.
* Overlapping runs cannot be easily blocked, risking disk space exhaustion.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **cronjob**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[cronjob]]
SORT file.name ASC
```
