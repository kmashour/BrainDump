---
obsidianUIMode: preview
class: landing-note
tier: main-note
domains:
  - "kubernetes"
role: worker-node
related_concepts:
  - "[[kubelet]]"
  - "[[pod]]"
reference_guides:
  - "[[Reference Notes/0-5_containers_runtimes_and_lifecycle.md]]"
tags:
  - kubernetes/component
  - status/completed
against: []
deeper_dive: "[[container-runtime-deeper]]"
---

# container-runtime

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Worker Node Mechanics > **container-runtime**

---

## 🎯 Purpose (Why it is used)
The `container-runtime` is the execution engine on each node. It is responsible for pulling container images from remote registries, managing local cached images, and running the actual containerized applications inside isolated OS sandboxes, enforcing resource constraints.

---

## ⚙️ Functionality (What it is doing)
1. **gRPC Interface Hosting:** Exposes a Unix socket implementing the Container Runtime Interface (CRI) for communication with the `kubelet`.
2. **Image Management:** Pulls, caches, lists, and purges container images (`ImageService`).
3. **Sandbox Provisioning:** Establishes the Pod Sandbox (including the `pause` container) to lock down sharing namespaces (Network, IPC) for containers in the same Pod.
4. **Lifecycle Execution:** Launches, monitors, and stops containers (`RuntimeService`) by invoking low-level OCI executors.
5. **Cgroup Enforcement:** Maps and enforces CPU, memory, and PID limits onto OS control groups (`cgroups`).

---

## 🏛️ Architectural Context (How it fits in the architecture)
The `container-runtime` resides on the host OS of every cluster node:
* **The Kubelet's Engine:** The `kubelet` communicates with it using gRPC over a local Unix domain socket.
* **Kernel Link:** It acts as the direct supervisor of host container processes, configuring namespaces and cgroups in the Linux kernel to run container runtimes.

---

## 🧩 Problem Solver (What problem it solves)
* **Runtime Pluggability:** Separates the core Kubernetes codebase from container engine details. The Container Runtime Interface (CRI) allows any runtime (e.g., `containerd`, `CRI-O`) to be plugged in seamlessly.
* **Docker-to-Containerd Decoupling:** Bypasses unnecessary developer platform subsystems (such as the Docker API, build tools, and local volume managers) by transitioning directly to standalone CRI runtimes. This was finalized with the removal of Dockershim in Kubernetes v1.24, reducing the host footprint and overhead.
* **Process Isolation:** Solves the security and stability problem of running multiple applications on the same physical host by applying kernel namespaces (walls) and cgroups (limits) to prevent interference.

---

## 🟢 Operational Impact (What will happen with it operating)
* **Workload Execution:** Pods are successfully launched on worker nodes.
* **Image Delivery:** Images are pulled from container registries and saved locally.
* **QoS Enforcement:** Resource limits configured in Pod specs are applied, protecting the host system from resource exhaustion.

---

## 🔴 Failure Impact (What will happen without it)
* **CRI Errors:** The `kubelet` logs connection errors and cannot execute commands. The node may transition to `NotReady` or report runtime status errors.
* **Orphaned workloads:** Existing containers might continue running on the host OS, but they cannot be deleted, scaled, or upgraded by Kubernetes.
* **Scheduling Freeze:** Any pods assigned to the node fail to create, hanging in `ContainerCreating` or displaying `CRIInitializationError` status.
---

## 🔍 Deeper Dive
For detailed configurations, sub-concepts, and step-by-step CKA playbooks, see:
* **[[container-runtime-deeper]]**

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```


