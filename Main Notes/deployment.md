---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: workload
domains:
  - "kubernetes"
related_concepts:
  - "[[replicaset]]"
  - "[[pod]]"
against:
  - "[[statefulset]]"
reference_guides:
  - "[[Reference Notes/07_kubernetes_workloads_and_controllers.md]]"
tags:
  - kubernetes/controller
  - status/completed
---

# deployment

**Breadcrumbs:** [[0-Index|🏠 Index]] > Workloads & Infrastructure > **deployment**

---

## 🎯 Purpose (Why it is used)
The `Deployment` controller provides declarative updates for Pods and ReplicaSets. It manages stateless application replication, handles rolling updates and rollbacks, and monitors rollout status to ensure zero-downtime application upgrades.

---

## ⚙️ Functionality (What it is doing)
* **Declarative Schema:** Translates desired state declarations (replicas, strategies, template) into low-level ReplicaSet commands.
* **Rollout Governance:** Implements rolling updates (replacing old pods with new pods incrementally) or recreate updates (killing all old pods first).
* **Rollback Management:** Maintains a history of rollout revisions, allowing quick rollbacks to stable versions.
* **Self-Healing:** Monitors pod health, spawning replacements if pods crash or nodes fail.

---

## 🏛️ Architectural Context (How it fits in the architecture)
* **High-Level Controller:** Sits above `ReplicaSet` and `Pod`. It does not manage Pods directly; it creates and manages `ReplicaSets` which in turn manage the `Pods`.
* **Reconciliation Loop:** Run by the `kube-controller-manager`'s deployment controller thread, continuously comparing actual cluster status to the deployment spec.
* **Service Binding:** Typically paired with a `Service` or `Ingress` to route traffic to the stateless pod replicas.

---

## 🧩 Problem Solver (What problem it solves)
* **No-Downtime Releases:** Solves the risk of service disruption during app updates by gradually scaling down the old version while scaling up the new version (using `maxSurge` and `maxUnavailable` limits).
* **Rollback Recovery:** Solves bad version releases by keeping a history of ReplicaSets to allow quick reverts via `kubectl rollout undo`.

---

## 🟢 Operational Impact (What will happen with it operating)
* Stateless web servers or API endpoints scale out automatically.
* Rolling upgrades execute automatically when the Pod template is modified (e.g., updating container image).
* Unhealthy pods are evicted and replaced dynamically.

---

## 🔴 Failure Impact (What will happen without it)
* Upgrades must be managed manually by deleting and creating pods, risking downtime and manual scripting errors.
* Reverting a broken release requires manual YAML tracking and redeploying.
* If pods crash, they are not replaced automatically unless lower-level controllers are run.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **deployment**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[deployment]]
SORT file.name ASC
```
