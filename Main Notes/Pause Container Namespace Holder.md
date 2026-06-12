---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[container-runtime]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/workloads/pods/#pod-networking"
author: "Kubernetes Documentation"
tags:
  - kubernetes/container-runtime
  - kubernetes/pod
---

# container-runtime - Pause Container Namespace Holder

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[container-runtime]] > **Pause Container**

---

## 📑 1. What is the Pause Container?
In Kubernetes, a **Pod** is not a single container but a group of containers. To share resources, all containers in the Pod must share the same network, IPC, and UTS namespaces.

The **Pause container** (run using the pause image) is launched first inside the Pod sandbox to serve as the namespace holder.

```text
[ Pod Sandbox ]
  |-- [ Pause Container (PID 1) ]  <-- Holds Network / IPC Namespaces
  |-- Container A (App)            <-- Joins namespaces of Pause
  |-- Container B (Sidecar)        <-- Joins namespaces of Pause
```

---

## ⚙️ 2. How it Works
1. **Sandbox Setup:** The Kubelet calls CRI to launch the pause container.
2. **Namespace Creation:** The pause container launches, initializes its network namespace (inheriting the CNI IP address), and goes to sleep.
3. **App Container Joining:** When application containers are launched, they join the network, IPC, and host UTS namespaces created by the pause container.

---

## 🔬 3. Inspecting the Sandbox Host-Level
Find the pause container running on a worker node host using `crictl`:
```bash
crictl ps | grep pause
```
Verify namespace links under `/proc`:
```bash
ls -l /proc/<pause-pid>/ns/
```
You will see that the app container PIDs share matching network (`net`) and IPC (`ipc`) namespace IDs.

*Read more in [[Reference Notes/0-5_containers_runtimes_and_lifecycle.md#2-pod-sandbox-namespaces-and-the-pause-container]]*\n