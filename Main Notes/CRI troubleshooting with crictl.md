---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[container-runtime-deeper]]"
sub_type: use-case
source_type: documentation
source_url: "https://kubernetes.io/docs/tasks/debug/debug-cluster/crictl/"
author: "Kubernetes Documentation"
against: []
tags:
  - kubernetes/container-runtime
  - crictl/troubleshooting
---

# container-runtime - CRI troubleshooting with crictl

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[container-runtime]] > [[container-runtime-deeper]] > **crictl Troubleshooting**

---

## 📑 1. What is crictl?
`crictl` is a CLI tool for CRI-compatible container runtimes. It is designed specifically to debug Kubernetes runtimes (containerd, CRI-O) without needing Docker.

---

## ⚙️ 2. Configuration & Default Fallbacks
`crictl` must know where the runtime socket resides. 

### Configuration File (`/etc/crictl.yaml`):
```yaml
runtime-endpoint: unix:///run/containerd/containerd.sock
image-endpoint: unix:///run/containerd/containerd.sock
timeout: 10
debug: false
```

### Default Socket Polling Order:
If config files and environment variables are absent, `crictl` defaults to polling sockets in the following order:
1. `unix:///var/run/dockershim.sock` (Dockershim)
2. `unix:///run/containerd/containerd.sock` (containerd)
3. `unix:///run/crio/crio.sock` (CRI-O)
4. `unix:///var/run/cri-dockerd.sock` (cri-dockerd)

If empty, you can pass the socket via CLI arguments: `crictl --runtime-endpoint=unix:///run/containerd/containerd.sock ps` or set `export CONTAINER_RUNTIME_ENDPOINT=unix:///run/containerd/containerd.sock`.

### ⚠️ Production Warning
Do not run `crictl` commands to create, run, or start containers in production. Since Kubelet is the orchestrator on the node, it is unaware of containers created directly via the CRI socket. It will detect them as untracked resources in the sandbox and will automatically delete or garbage collect them. Use `crictl` strictly for inspection and debugging.

### 🎛️ Port Awareness
To list port mappings mapped under the Pod sandbox namespaces, use:
```bash
crictl ports
```

---

## 🔬 3. Troubleshooting Commands Cheat Sheet
Execute these commands on the worker host:

### A. List Pod Sandboxes
```bash
# List all pods on the host
crictl pods

# Filter by state
crictl pods --state Ready
```

### B. List Containers
```bash
# List running containers
crictl ps

# View container logs
crictl logs <container-id>

# Run execution command
crictl exec -it <container-id> sh
```

### C. Clean up Resources
```bash
# Delete a container
crictl rm <container-id>

# Delete a pod sandbox
crictl rmp <pod-sandbox-id>
```

*Read more in [[Reference Notes/0-11_troubleshooting_and_diagnostics.md#2-control-plane-diagnostics-and-static-pod-recovery]]*\n