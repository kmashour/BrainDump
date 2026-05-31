---
tags:
  - concept/container-runtime
  - component/worker-node
related:
  - [[kubelet]]
  - [[pod]]
---

# container-runtime

> [!NOTE] Landing Note
> **Related Concepts:** [[kubelet]], [[pod]]
> **Deeper Dive:** [[container-runtime-deeper]]
> **Detailed Reference:** [05_containers_runtimes_and_lifecycle.md](../Reference%20Notes/05_containers_runtimes_and_lifecycle.md#2-the-kubelet-to-cri-architecture)

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
