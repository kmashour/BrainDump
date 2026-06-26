---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: workload
domains:
  - "kubernetes"
related_concepts:
  - "[[deployment]]"
  - "[[pod]]"
against:
  - "[[replicationcontroller]]"
reference_guides:
  - "[[Reference Notes/0-6_kubernetes_workloads_and_controllers.md]]"
tags:
  - kubernetes/controller
  - status/completed
---

# replicaset

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Workloads & Infrastructure > **replicaset**

---

## 🎯 Purpose (Why it is used)
The `ReplicaSet` ensures that a specified number of stateless pod replicas are running at any given time. It is used as a stability mechanism to scale and maintain application availability.

---

## ⚙️ Functionality (What it is doing)
* **Replica Count Enforcer:** Spawns new pods or deletes excess pods to match the declared replica count.
* **Dynamic Pod Selection:** Uses set-based selectors (e.g. `matchExpressions`) to identify and acquire ownership of running pods in the namespace, even if those pods were created outside the ReplicaSet.

---

## 🌉 Evolutionary Bridge: Replication Controller vs. ReplicaSet
* **Replication Controller (RC - Legacy):** The older technology (`v1` core API group). It only supports simple equality-based selectors (e.g. `app=nginx`) and relies on client-side CLI tools like `kubectl rolling-update` for updates, which are brittle and slow.
* **ReplicaSet (RS - Modern):** Built on the `apps/v1` API group, replacing the RC. It supports set-based selectors (`matchExpressions` with `In`, `NotIn`, `Exists`, `DoesNotExist`) and serves as the underlying engine for Deployments, which perform rolling updates server-side.

### Scaling & Template Update Behaviors
* **Scaling Commands:** ReplicaSets can be scaled declaratively (updating the manifest and running `kubectl apply -f`) or imperatively using `kubectl scale rs <name> --replicas=<count>` or `kubectl edit rs <name>`.
* **Update Limitations:** Modifying a ReplicaSet's pod template does **not** update existing pods (it is not a rolling-update controller). The new configuration is only applied to newly created pods. To roll out changes, existing pods must be manually deleted to trigger the ReplicaSet's recreation logic.

---

## 🏛️ Architectural Context (How it fits in the architecture)
* **Intermediary Controller:** Managed directly by the `Deployment` controller. Admins rarely configure `ReplicaSets` directly in production.
* **Selectors:** Relies on label matching. If a pod matches the selector, the ReplicaSet counts it towards its target.

---

## 🧩 Problem Solver (What problem it solves)
* **Application Availability:** Solves the problem of individual pod failures. If a node hosting a pod dies, the ReplicaSet detects the loss and schedules a new pod on an active node.
* **Capacity Management:** Allows simple scaling of stateless capacity by increasing the `spec.replicas` count.

---

## 🟢 Operational Impact (What will happen with it operating)
* A constant pool of pods matches user requests.
* Pods are automatically redistributed across available nodes.

---

## 🔴 Failure Impact (What will happen without it)
* Pods become single points of failure; if a node goes down, the workload goes offline permanently.
* Manual capacity planning is required to scale workloads.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **replicaset**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
