---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: control-plane
domains:
  - "kubernetes"
related_concepts:
  - "[[kube-apiserver]]"
reference_guides:
  - "[[Reference Notes/0-14_cluster_administration_and_observability.md]]"
tags:
  - kubernetes/component
  - status/completed
against: []
---

# APIPriorityAndFairness

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Control Plane > **APIPriorityAndFairness**

---

## 🎯 Purpose (Why it is used)
API Priority and Fairness (APF) protects the `kube-apiserver` from becoming overloaded and unresponsive. It replaces simple max-inflight request limits with a multi-priority queuing engine that ensures critical control plane requests are processed even during heavy user traffic or controller malfunction.

---

## ⚙️ Functionality (What it is doing)
1. **Request Classification:** Inspects incoming API requests (user identity, group membership, verb, namespace, resource) and maps them to a specific **`FlowSchema`**.
2. **Priority Assignment:** Associates each `FlowSchema` with a **`PriorityLevelConfiguration`**, defining concurrency limits and queuing behavior.
3. **Queueing with Shuffled Round-Robin:** Places overflowing requests into parallel queues and uses Shuffled Round-Robin (SRR) dispatching to prevent resource-heavy clients from starving others.
4. **Concurrency Seat Allocation:** Allocates concurrency "seats" based on nominal limits. Once seats are free, queued requests are executed.

---

## 🏛️ Architectural Context (How it fits in the architecture)
APF is built directly into the request processing pipeline of the `kube-apiserver`. It intercepts all requests immediately after authentication and authorization, but before admission control and database commit phases.

---

## 🧩 Problem Solver (What problem it solves)
APF prevents **noisy neighbor starvation** in the cluster. For example, if a custom controller malfunctions and floods the API server with lists of all pods in the cluster, standard limits (`--max-requests-inflight`) would block all users. APF isolates the misbehaving controller to its own priority queue, allowing system admins to run debugging commands (like `kubectl get nodes`) without interruption.

---

## 🟢 Operational Impact (What will happen with it operating)
* **Consistent Response Times:** Control plane services (like scheduler heartbeats or controller reconciliation loops) remain stable under high client load.
* **Deterministic Queueing:** Spikes of API traffic are queued rather than immediately rejected with a `429 Too Many Requests` status.

---

## 🔴 Failure Impact (What will happen without it)
* **Control Plane Crashes:** The API server can run out of memory or suffer extreme latency spikes during load, freezing scheduling and cluster reconciliation.
* **Cascading Failures:** When the scheduler or controller manager cannot communicate with the API server, it halts cluster recovery and rescheduling efforts.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **APIPriorityAndFairness**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), "APIPriorityAndFairness")
SORT file.name ASC
```
