---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[container-runtime]]"
sub_type: architecture
source_type: documentation
source_url: "https://github.com/containerd/containerd/blob/main/docs/design/shim.md"
author: "containerd Maintainers"
tags:
  - kubernetes/container-runtime
  - containerd/architecture
---

# container-runtime - containerd-shim mechanics

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[container-runtime]] > **containerd-shim**

---

## 📑 1. What is containerd-shim?
The **containerd-shim** is a lightweight daemon process launched for each container in the cluster. It sits between the Container Runtime daemon (`containerd`) and the low-level executor (`runc`).

```text
[ containerd ] ---> [ containerd-shim ] ---> [ runc ] ---> [ Container Process (PID) ]
```

---

## ⚙️ 2. Core Responsibilities
* **Daemonless Containers:** The shim acts as the container's parent process. This decouples the container from the main `containerd` daemon, meaning you can restart or upgrade `containerd` without stopping or restarting the running container processes.
* **Standard Streams Handling:** It handles terminal I/O (stdin, stdout, stderr) and log file writing for the container.
* **Exit Status Reporting:** It reports the container exit code back to containerd after execution completes.

---

## 🔬 3. Process Trees on Host
View the processes on a Kubernetes host to inspect shims:
```bash
ps aux | grep containerd-shim
```
Output:
```text
root      12345  0.1  0.2 ... containerd-shim -namespace k8s.io -id abcde... -address /run/containerd/containerd.sock
```

*Read more in [[Reference Notes/0-5_containers_runtimes_and_lifecycle.md#1-container-runtime-engines-and-cri-compliance]]*\n