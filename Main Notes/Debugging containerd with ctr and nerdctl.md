---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[container-runtime-deeper]]"
sub_type: use-case
source_type: documentation
source_url: "https://github.com/containerd/containerd/blob/main/docs/getting-started.md"
author: "containerd Maintainers"
against: []
tags:
  - kubernetes/container-runtime
  - containerd/troubleshooting
---

# container-runtime - Debugging containerd with ctr and nerdctl

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[container-runtime]] > [[container-runtime-deeper]] > **ctr & nerdctl**

---

## 📑 1. Core CLI Debugging Tools
If Kubelet fails to manage containers and you suspect containerd issues, use these command-line utilities directly on the host node. 

Both `ctr` and `nerdctl` are developed by the **containerd community** specifically for containerd, as opposed to `crictl`, which is developed by the Kubernetes community to target any CRI-compliant runtime socket.

* **Standalone containerd:** Containerd is a graduated CNCF project that can run standalone without any Docker Engine dependencies. You can install it on its own to manage containers via API or CLI.
* **`ctr`:** Low-level, official CLI tool bundled with containerd. Solely made for debugging containerd. It is not user-friendly and has a limited feature set.
* **`nerdctl`:** User-friendly, Docker-compatible CLI for containerd. It supports Docker-like command line syntax (`run`, `build`, `compose`) and exposes newer, advanced features of containerd:
  * Encrypted container images.
  * Lazy pulling of images (e.g., via eStargz).
  * Peer-to-peer (P2P) image distribution.
  * Image signing and verification.
  * Namespace awareness (e.g., inspecting Kubernetes namespaces via `-n k8s.io`).

---

## ⚙️ 2. ctr CLI Command Formulas
You must specify the Kubernetes namespace (`k8s.io`) when querying with `ctr` to see cluster containers:

```bash
# 1. List images in k8s namespace
sudo ctr -n k8s.io images list

# 2. List running tasks/processes
sudo ctr -n k8s.io tasks list

# 3. View container configuration specs
sudo ctr -n k8s.io containers info <container-id>
```

---

## 🔬 3. nerdctl Command Formulas
`nerdctl` matches Docker syntax:
```bash
# List containers in k8s namespace
sudo nerdctl -n k8s.io ps

# Run interactive debugging shell
sudo nerdctl -n k8s.io exec -it <container-id> sh
```

*Read more in [[Reference Notes/0-5_containers_runtimes_and_lifecycle.md#1-container-runtime-engines-and-cri-compliance]]*\n