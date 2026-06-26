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
  - "[[Reference Notes/0-6_kubernetes_workloads_and_controllers.md]]"
tags:
  - kubernetes/controller
  - status/completed
---

# deployment

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Workloads & Infrastructure > **deployment**

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

## 🏛️ Deployment Hierarchy & Rollout Management

A Deployment behaves as a high-level wrapper orchestrating underlying resources:
$$\text{Deployment} \longrightarrow \text{ReplicaSet} \longrightarrow \text{Pods}$$
* **Hierarchy:** Updating the Pod template in the Deployment triggers the creation of a new ReplicaSet. The Deployment manager scales up the new ReplicaSet while scaling down the old one.

### Rollout Strategies
* **`RollingUpdate` (Default):** Replaces pods incrementally.
  * `maxSurge`: Maximum number of pods that can be created above the desired count during rollout (e.g. `25%` or `1`).
  * `maxUnavailable`: Maximum number of pods that can be offline during the update.
  * > [!IMPORTANT]
  > Both `maxSurge` and `maxUnavailable` cannot be `0` at the same time.
* **`Recreate`:** Terminates all existing pods before starting any new ones, causing temporary downtime (useful for single-writer databases or incompatible schemas).

### Rollout Checking & Rollback Commands
* **Check Status:** `kubectl rollout status deployment/<deployment-name>`
* **Rollout History:** `kubectl rollout history deployment/<deployment-name>` (Add `--revision=<num>` to view revision details).
* **Rollback (Undo):** `kubectl rollout undo deployment/<deployment-name>` (Add `--to-revision=<num>` to roll back to a specific revision).

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
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
