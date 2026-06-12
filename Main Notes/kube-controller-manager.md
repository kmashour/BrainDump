---
obsidianUIMode: preview
class: landing-note
tier: main-note
domains:
  - "kubernetes"
role: control-plane
related_concepts:
  - "[[kube-apiserver]]"
  - "[[pod]]"
  - "[[node]]"
reference_guides:
  - "[[Reference Notes/0-2_cluster_architecture_and_components.md]]"
tags:
  - kubernetes/component
  - status/completed
against: []
deeper_dive: "[[kube-controller-manager-deeper]]"
---

# kube-controller-manager

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Control Plane > **kube-controller-manager**

---

## 🎯 Purpose (Why it is used)
The `kube-controller-manager` is the Control Plane's "enforcer." It compiles multiple controller processes into a single running binary, executing continuous reconciliation loops that monitor the cluster's state and issue updates to drive the actual state toward the desired state defined in `etcd`.

---

## ⚙️ Functionality (What it is doing)
1. **Reconciliation Loop Execution:** Run continuous loops checking specific resources:
   $$\text{Actual State} \longleftrightarrow \text{Desired State}$$
2. **State Alignment:** If the actual state deviates from the desired state (e.g., a node goes offline, or a pod crashes), the controller manager instructs the `kube-apiserver` to make changes (e.g., launch a new pod or evict a dead node).
3. **Core Controller Execution:** Bundles essential controllers including:
   - **Node Controller:** Manages node statuses, detects node failures, and schedules evictions.
   - **ReplicaSet Controller:** Ensures the exact number of defined Pod replicas run at all times.
   - **Endpoints Controller:** Updates the endpoints list of Services as Pods are created, deleted, or restarted.
   - **Namespace Controller:** Cleans up all resources inside a namespace when it is deleted.

---

## 🏛️ Architectural Context (How it fits in the architecture)
The `kube-controller-manager` is an active administrative agent in the Control Plane:
* **API Client:** It communicates exclusively with the `kube-apiserver`, using the Watch mechanism to monitor state changes.
* **Passive DB:** It never talks directly to `etcd` or worker node `kubelets`. It modifies state in `etcd` by submitting updates to the API Server.

---

## 🧩 Problem Solver (What problem it solves)
* **Automation of Maintenance:** Automates tasks that would otherwise require manual administrator intervention (e.g., rescheduling containers when hardware fails, updating load balancer routing tables, or garbage collecting orphaned resources).
* **Declarative Guarantee:** Resolves the discrepancy between declarative intent (YAML specifications) and dynamic physical realities (running server processes).

---

## 🟢 Operational Impact (What will happen with it operating)
* **Self-Healing Active:** Crashing pods in Deployments or ReplicaSets are automatically replaced on healthy nodes.
* **Network Updates:** Service traffic is immediately redirected away from dead pods and routed to newly spawned pods.
* **Namespace Purging:** Deleting a namespace cleanly removes all Pods, Services, and Secrets nested inside it.
* **Leader Election HA:** In a multi-master control plane, a lease lock mechanism ensures only one active manager process issues commands, preventing split-brain resource creation.

---

## 🔴 Failure Impact (What will happen without it)
* **No Self-Healing:** If a worker node dies, the pods on that node are never evicted or rescheduled. If individual pods in a Deployment crash, they are never replaced.
* **Broken Service Routing:** Services do not update their routing tables. If a pod changes its IP address, kube-proxy will continue routing traffic to the old, inactive IP.
* **Terminating Namespaces:** Namespaces will hang in the `Terminating` phase indefinitely because the namespace cleanup controller is inactive.
* **Resource Leaks:** Stale objects, completed pods, and unused resources are never garbage collected, consuming cluster memory.
* **No Volume Attachment Control:** Volumes will fail to attach or detach from nodes when pods move, freezing workload migrations.
---

## 🔍 Deeper Dive
For detailed configurations, sub-concepts, and step-by-step CKA playbooks, see:
* **[[kube-controller-manager-deeper]]**

