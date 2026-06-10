---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: workload
domains:
  - "kubernetes"
related_concepts:
  - "[[deployment]]"
  - "[[node]]"
against:
  - "[[deployment]]"
reference_guides:
  - "[[Reference Notes/0-6_kubernetes_workloads_and_controllers.md]]"
tags:
  - kubernetes/controller
  - status/completed
---

# daemonset

**Breadcrumbs:** [[0-Index|🏠 Index]] > Workloads & Infrastructure > **daemonset**

---

## 🎯 Purpose (Why it is used)
A `DaemonSet` ensures that all (or some) Nodes run a single copy of a Pod. It is designed for deploying background system daemons, cluster storage providers, log collectors, and node monitoring agents.

---

## ⚙️ Functionality (What it is doing)
* **Host Co-location:** Automatically schedules a copy of the declared Pod to every newly joined Node in the cluster.
* **Tolerations Overrides:** Bypasses normal scheduling rules, automatically adding tolerations (e.g. `node.kubernetes.io/unschedulable`) to schedule on control plane or cordoned nodes.
* **Automatic Eviction:** Terminates the target Pod copy when its parent Node is removed from the cluster.

---

## 🏛️ Architectural Context (How it fits in the architecture)
* **System Controller:** Operates under the `kube-controller-manager`'s DaemonSet controller thread.
* **Infra Workloads:** Typically manages system utilities (e.g. `kube-proxy`, CNI plugins like Calico/Flannel, log forwarders like Fluentd, or monitoring agents like Prometheus node-exporter).

---

## 🧩 Problem Solver (What problem it solves)
* **Uniform Log & Metric Collection:** Solves the challenge of manual daemon installation on hosts. Instead of configuring systemd services via Ansible on every node, the DaemonSet deploys them automatically.
* **Network Routing (CNI):** Solves cluster routing setup. Network plugins must run on every node to configure local virtual interfaces and route tables.

---

## 🟢 Operational Impact (What will happen with it operating)
* Log aggregators gather statistics from new worker nodes automatically.
* Virtual networking paths setup automatically upon node boot.

---

## 🔴 Failure Impact (What will happen without it)
* Node-level logging, monitoring, and networking must be configured manually on host operating systems.
* If a new node joins the cluster, it remains unmonitored and disconnected from the pod network until manual provisioning runs.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **daemonset**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[daemonset]]
SORT file.name ASC
```
