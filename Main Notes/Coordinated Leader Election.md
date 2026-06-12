---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: control-plane
domains:
  - "kubernetes"
related_concepts:
  - "[[kube-scheduler]]"
  - "[[kube-controller-manager]]"
reference_guides:
  - "[[Reference Notes/0-14_cluster_administration_and_observability.md]]"
tags:
  - kubernetes/component
  - status/completed
against: []
---

# Coordinated Leader Election

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Control Plane > **Coordinated Leader Election**

---

## 🎯 Purpose (Why it is used)
Coordinated Leader Election prevents active-active race conditions between redundant control plane instances (like `kube-scheduler` or `kube-controller-manager`) in High Availability (HA) clusters. It determines which instance actively makes cluster decisions.

---

## ⚙️ Functionality (What it is doing)
1. **Candidate Registration:** Replicas register their intent to lead by creating a **`LeaseCandidate`** object detailing their binary and emulation version.
2. **Lease Locking:** Candidates attempt to acquire a shared **`Lease`** object from the API server, acting as a lightweight distributed lock.
3. **Deterministic Selection:** During cluster upgrades, the API server selects a leader based on version skew rules (`OldestEmulationVersion` strategy) rather than allowing a network race.
4. **Heartbeat Renewal:** The active leader periodically updates the Lease's `renewTime` to maintain its leadership lock.
5. **Failover Execution:** If the leader fails to renew, other candidates detect the lease expiration and run a new election to pick a successor.

---

## 🏛️ Architectural Context (How it fits in the architecture)
This feature extends the standard Lease locking mechanism. It utilizes the `coordination.k8s.io/v1` API group for Leases and the `coordination.k8s.io/v1beta1` group for LeaseCandidates to manage HA component transitions during upgrades.

---

## 🧩 Problem Solver (What problem it solves)
During minor version upgrades, if a newer control plane instance runs as the active leader while older nodes are still active, it might write data structures that older replicas cannot parse. Coordinated Leader Election ensures the **oldest emulation version** retains leadership until the upgrade is complete, ensuring backward compatibility.

---

## 🟢 Operational Impact (What will happen with it operating)
* **Consistent Scheduling/Control Loops:** Only one replica actively mutates cluster states.
* **Safe Cluster Upgrades:** No data degradation or upgrade-related race conditions between old and new replicas.

---

## 🔴 Failure Impact (What will happen without it)
* **Active-Active Conflicts:** Multiple schedulers might bind different pods to the same node slot simultaneously, causing resource collisions.
* **Upgrade Version Anomalies:** Newer replicas could hijack leadership prematurely during upgrades, breaking compatibility with older worker nodes.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Coordinated Leader Election**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
WHERE class = "deeper-dive" AND contains(parent_concept, this.file.link)
SORT file.name ASC
```
