---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[pod]]"
sub_type: use-case
source_type: documentation
source_url: "https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/#ephemeral-container"
author: "Kubernetes Documentation"
tags:
  - kubernetes/pod
  - kubernetes/troubleshooting
---

# pod - Debugging with Ephemeral Containers

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[pod]] > **Ephemeral Containers**

---

## 📑 1. Purpose of Ephemeral Containers
In production, containers are often optimized for security and size by removing shell utilities (like bash, curl, netstat) or using distroless base images. If these pods fail, administrators cannot run standard troubleshooting commands inside them.

**Ephemeral containers** are created dynamically in a running pod sandbox using `kubectl debug` to facilitate troubleshooting.

---

## ⚙️ 2. Step-by-Step Troubleshooting Scenario

### Step 1: Launch Debugging Container
Add a troubleshooting container with diagnostic utilities to a running pod:
```bash
kubectl debug -it target-pod --image=busybox --target=app-container
```
* `--target`: Shares the process namespace with the target container, allowing you to see its running processes.

### Step 2: Diagnostic Verification
Inside the shell, verify process lists and network listening sockets:
```bash
# View processes of target-container
ps aux

# Check files/ports
netstat -tulpn
```

---

## 🔬 3. Target Namespace Sharing
To ensure process sharing works, target namespace sharing must be supported by the container runtime. Verify process visibility using `/proc/<PID>/root` from the debugging container shell to inspect target container files.

*Read more in [[Reference Notes/0-5_containers_runtimes_and_lifecycle.md#6-ephemeral-containers-for-debugging]]*\n