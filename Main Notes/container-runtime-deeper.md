---
tags:
  - concept/container-runtime
  - type/deeper-dive
related:
  - [[container-runtime]]
---

# container-runtime deeper

This note covers the Container Runtime Interface (CRI) services, OCI specifications, shim mechanics, the pause container, Cgroup drivers, and runtime command-line tools.

---

## 🔌 1. The CRI Dual Services (gRPC)
The Container Runtime Interface (CRI) consists of two gRPC services running over a local Unix domain socket:
1. **`RuntimeService`:** Manages the lifecycle of Pod Sandboxes and active containers (create, start, stop, remove, exec).
2. **`ImageService`:** Manages images (pull, list, inspect, remove).

---

## 🏛️ 2. High-Level vs. Low-Level Runtimes (OCI & runc)
Kubernetes decouples container execution into two tiers:
* **High-Level Runtime (CRI-compliant):** e.g., `containerd` or `CRI-O`. Handles the gRPC API, pulls images, unpacks them, and manages container networking and storage.
* **Low-Level Runtime (OCI-compliant):** e.g., `runc`. A lightweight CLI tool that talks directly to the Linux kernel to configure cgroups, namespaces, and execute the container process, then exits immediately.

---

## 🪓 3. containerd-shim
Because the low-level runtime (`runc`) exits after creating the container, something must stay active to monitor the container process:
* **containerd-shim:** A tiny process spawned for each container.
* **Responsibilities:**
  * Keeps the container's standard I/O (stdin, stdout, stderr) file descriptors open even if containerd restarts.
  * Reports the container exit status code back to containerd.
  * Prevents "zombie processes" if the container's main process crashes.

---

## ⏸️ 4. The Pause Container
Every Pod in Kubernetes runs a hidden helper container called the **pause container** (or infra container):
* **Namespace Holder:** It is the first container started in the Pod sandbox. It does not run any application code; it simply runs a sleep loop.
* **Resource Sharing:** It holds open the Network and IPC namespaces. All other application containers inside the same Pod join these namespaces, allowing them to communicate over `localhost` and share storage volumes.

---

## 🧬 5. Cgroup Drivers: systemd vs. cgroupfs
Linux uses control groups (`cgroups`) to limit container resources. Kubernetes and the container runtime must use the same driver to manage these cgroups:
* **`cgroupfs` (Legacy):** The runtime writes resource files directly to `/sys/fs/cgroup`.
* **`systemd` (Modern & Recommended):** The OS uses systemd as its init process, which manages cgroup mappings.
* **Critical Rule:** If the container runtime uses `systemd` but the kubelet uses `cgroupfs` (or vice versa), the node will experience duplicate control hierarchies and eventually crash under heavy memory load. Both must be aligned.

---

## 🛠️ 6. Debug CLI Tools Comparison (CKA Essential)
When debugging a broken node, you cannot use `kubectl` or `docker`. You must use node-level tools:

| CLI Tool | Target Level | Namespace Aware? | Purpose |
| :--- | :--- | :--- | :--- |
| **`ctr`** | containerd daemon | Yes (`ctr -n k8s.io ...`) | Native containerd debugging. |
| **`nerdctl`** | containerd daemon | Yes (`nerdctl -n k8s.io ...`) | Docker-compatible syntax for containerd. |
| **`crictl`** | CRI endpoint socket | Yes (Automatically connects to CRI) | **Kubernetes-native CLI** for troubleshooting runtime issues. |

### crictl Commands Example
To list Pods, Containers, and Images on a node using the CRI socket:
```bash
# Configure socket environment variable
export CRI_CONFIG_FILE=/etc/crictl.yaml
crictl pods
crictl ps
crictl images
crictl logs <container-id>
```

*Read more in [05_containers_runtimes_and_lifecycle.md](../Reference%20Notes/05_containers_runtimes_and_lifecycle.md#2-the-kubelet-to-cri-architecture).*
