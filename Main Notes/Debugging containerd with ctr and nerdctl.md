---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[container-runtime]]"
sub_type: use-case
source_type: documentation
source_url: "https://github.com/containerd/containerd/blob/main/docs/getting-started.md"
author: "containerd Maintainers"
tags:
  - kubernetes/container-runtime
  - containerd/troubleshooting
---

# container-runtime - Debugging containerd with ctr and nerdctl

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[container-runtime]] > **ctr & nerdctl**

---

## 📑 1. Core CLI Debugging Tools
If Kubelet fails to manage containers and you suspect containerd issues, use these command-line utilities directly on the host node.

* **`ctr`:** Low-level, official CLI tool bundled with containerd. Used for raw container administration (does not support high-level CRI configurations directly unless matching namespaces).
* **`nerdctl`:** User-friendly, Docker-compatible CLI for containerd that supports Docker-like syntax (`run`, `build`, `compose`).

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