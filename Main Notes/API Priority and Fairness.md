---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: control-plane
domains:
  - "kubernetes"
related_concepts:
  - "[[kube-apiserver]]"
  - "[[rbac]]"
against:
  - "[[max-requests-inflight]]"
reference_guides:
  - "[[Reference Notes/0-7-1_rbac_service_accounts_and_certificates.md]]"
tags:
  - kubernetes/control-plane
  - kubernetes/cks
  - status/completed
---

# API Priority and Fairness

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Control Plane > **API Priority and Fairness**

---

## 🎯 Purpose (Why it is used)
API Priority and Fairness (APF) protects the `kube-apiserver` from performance degradation and starvation caused by request overload. It supersedes the coarse legacy inflight request limits by classifying, prioritizing, and fairly queuing requests according to caller identity and resource importance.

---

## ⚙️ Functionality (What it is doing)
* **Request Classification:** Leverages `FlowSchema` objects to inspect incoming HTTP requests (verbs, resource paths, users, service accounts) and map them to priority queues.
* **Concurrency Allocation:** Leverages `PriorityLevelConfiguration` objects to assign concurrency shares (seats) and configure queue depth limits.
* **Shuffle Sharding:** Isolates abusive or misbehaving client streams into separate queue buckets to prevent head-of-line blocking.
* **Emergency Dispatch:** Ensures critical system controllers and emergency administrator requests bypass queues and execute immediately.

---

## 🏛️ Architectural Context (How it fits in the architecture)
APF is an in-tree admission and flow-control filter inside `kube-apiserver`. It evaluates requests immediately following authentication and authorization, but before admission plugins and etcd serialization.

---

## 🧩 Problem Solver (What problem it solves)
Without APF, high-volume automated scripts, misconfigured third-party operators, or batch jobs can consume all available HTTP handler worker pools, causing `kubectl` commands and Kubelet node lease updates to time out, triggering false node NotReady cascades.

---

## 🟢 Operational Impact (What will happen with it operating)
The API server maintains deterministic responsiveness under heavy traffic. Critical health checks and leader election leases continue without interruption even during severe control plane load.

---

## 🔴 Failure Impact (What will happen without it)
A surge in API requests (e.g. thousands of concurrent pods listing Secrets) triggers HTTP 429 Too Many Requests errors indiscriminately across all cluster operators, deadlocking cluster control loops.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **API Priority and Fairness**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[API Priority and Fairness]]
SORT file.name ASC
```
