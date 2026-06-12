---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kubelet-deeper]]"
sub_type: architecture
source_type: documentation
source_url: "https://kubernetes.io/docs/setup/production-environment/container-runtimes/"
author: "Kubernetes Documentation"
tags:
  - kubernetes/kubelet
  - kubernetes/cri
---

# kubelet - CRI Socket Communication

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[kubelet]] > [[kubelet-deeper]] > **CRI Socket Communication**

---

## 📑 1. Kubelet to Container Runtime Communication
The Kubelet does not interact with containers directly. It communicates with the host Container Runtime (e.g. Containerd, CRI-O) over a Unix domain socket using gRPC via the **Container Runtime Interface (CRI)**.

```text
[ Kubelet ] ---gRPC over Unix Socket---> [ Container Runtime (CRI) ] ---> [ runc ]
```

---

## ⚙️ 2. Standard CRI Socket Paths
During node installation, you must configure the socket path in Kubelet's startup flags (`--container-runtime-endpoint`) or configuration file:

* **Containerd:** `unix:///run/containerd/containerd.sock` (Standard on modern Kubernetes clusters)
* **CRI-O:** `unix:///var/run/crio/crio.sock`
* **Docker Engine (via cri-dockerd shim):** `unix:///var/run/cri-dockerd.sock`

---

## 🔬 3. Kubelet Configuration Example
Set the socket endpoint in `/var/lib/kubelet/kubeadm-flags.env`:
```bash
KUBELET_KUBEADM_ARGS="--container-runtime-endpoint=unix:///run/containerd/containerd.sock"
```
Or in kubelet configuration file `/var/lib/kubelet/config.yaml` (v1.28+):
```yaml
containerRuntimeEndpoint: "unix:///run/containerd/containerd.sock"
```

*Read more in [[Reference Notes/0-3_node_mechanics_and_resource_limits.md#1-node-bootstrapping-and-kubelet-self-registration]]*\n