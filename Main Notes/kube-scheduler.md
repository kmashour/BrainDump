---
obsidianUIMode: preview
class: landing-note
tier: main-note
domains:
  - "kubernetes"
role: control-plane
related_concepts:
  - "[[kube-apiserver]]"
  - "[[node]]"
  - "[[pod]]"
reference_guides:
  - "[[Reference Notes/0-2_cluster_architecture_and_components.md]]"
tags:
  - kubernetes/component
  - status/completed
against: []
deeper_dive: "[[kube-scheduler-deeper]]"
---

# kube-scheduler

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Control Plane > **kube-scheduler**

---

## 🎯 Purpose (Why it is used)
The `kube-scheduler` is the Control Plane's "matchmaker." It evaluates newly created, unassigned Pods and selects the optimal worker node in the cluster for them to run on, taking resource requirements, hardware constraints, affinity policies, and taints into account.

> [!TIP] Conceptual Analogy (Mumshad's CKA)
> In a shipping port analogy, the `kube-scheduler` represents the **Loading Crane** on the docks. It identifies containers waiting to be loaded and selects the most appropriate cargo ship (worker node) based on capacity, size, cargo destination constraints, and other carrying rules (taints/tolerations, node affinity).

---

## ⚙️ Functionality (What it is doing)
1. **Pending Pod Watch:** Watches the API Server for any Pod that has a blank `spec.nodeName` field.
2. **Filtering (Predicates):** Evaluates all available worker nodes and filters out those that cannot host the Pod (e.g., insufficient CPU/Memory, missing node label selectors, or node taints).
3. **Ranking (Priorities):** Scores the remaining eligible nodes (on a scale of 0 to 10) using priority algorithms (e.g., balancing resource usage, preferring nodes that already have the required container image cached).
4. **Binding:** Selects the node with the highest score, and sends a "Binding" API request to the `kube-apiserver` to write the chosen node name into the Pod's `spec.nodeName` field.

---

## 🏛️ Architectural Context (How it fits in the architecture)
The `kube-scheduler` runs as an independent control loop:
* **Decoupled Placement:** It does not directly deploy container processes. It only updates the metadata in the `kube-apiserver`.
* **Kubelet Hand-off:** Once the scheduler binds a Pod to a node in `etcd`, the `kubelet` daemon on that node detects the update and coordinates with the Container Runtime (CRI) to spin up the container.

---

## ⚙️ Configuration & Key Flags
The scheduler runs as a control daemon configured using key parameters and config paths:
* **Configuration File:** Manual deployments configure the scheduler process pointing to a configurations policy file via the `--config=<path>` option.
* **Predicates vs. Priorities:** The scheduling algorithm selects nodes using a two-step pipeline:
  1. **Filtering (Predicates):** Filters out nodes that do not satisfy requirements (e.g., checks resource availability, node selectors, taints).
  2. **Ranking (Priorities):** Assigns a score (0 to 10) to the remaining nodes using priority functions (e.g., image locality, least resource utilization) to choose the best host.
* **Deployment & Paths:**
  * **Static Pod Paths:** In a kubeadm setup, the manifest is located at `/etc/kubernetes/manifests/kube-scheduler.yaml`.
  * **Manual Service Units:** In non-kubeadm clusters, options are configured in the systemd service file at `/etc/systemd/system/kube-scheduler.service`.

---

## 🧩 Problem Solver (What problem it solves)
* **Resource Contention:** Prevents scheduling workloads on nodes that lack the capacity, avoiding host CPU starvation or Out-Of-Memory (OOM) kills.
* **Complex Placement Rules:** Handles complex affinity, anti-affinity, and co-location rules to place workloads close to their databases or spread them apart for high availability.
* **Topology Awareness:** Places pods across separate failure domains (e.g., racks, regions, availability zones) to ensure application resilience if a zone fails.

---

## 🟢 Operational Impact (What will happen with it operating)
* **Dynamic Orchestration:** Pods transition automatically from `Pending` to `ContainerCreating` and then `Running`.
* **Constraint Compliance:** Workloads are placed strictly on nodes that match their affinity rules, tolerations, and requirements.
* **Resource Balance:** The cluster maintains a balanced load across all worker nodes.

---

## 🔴 Failure Impact (What will happen without it)
* **Scheduling Freeze:** Any newly created Pods will remain in a `Pending` state indefinitely because no component is assigning them to nodes.
* **Existing Pod Safety:** Currently running Pods are unaffected and continue executing.
* **Self-Healing Failure:** If a running Pod crashes or its host node dies, the Controller Manager will detect it and create a replacement Pod, but this replacement will stay `Pending` because there is no scheduler to place it.
* **Manual Bypass:** Administrators can bypass a failed scheduler by manually defining `spec.nodeName: <node-name>` directly inside a Pod's YAML manifest at creation time.

---

## 📊 Observability (Logging & Profiling)
* **Tailing Logs:** Administrators debug custom or default scheduler issues by retrieving standard output logs:
  ```bash
  kubectl logs -n kube-system -l component=kube-scheduler
  ```
* **Performance Profiling:** When diagnosing scheduler bottlenecks or CPU/memory leaks, query Go's profiling endpoint (exposed via the `--enable-profiling=true` flag by default):
  ```bash
  kubectl get --raw /debug/pprof/profile > scheduler_cpu.pprof
  kubectl get --raw /debug/pprof/heap > scheduler_heap.pprof
  ```

---

## 🔍 Deeper Dive
For detailed configurations, sub-concepts, and step-by-step CKA playbooks, see:
* **[[kube-scheduler-deeper]]**

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```


