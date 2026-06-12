---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[container-runtime-deeper]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/setup/production-environment/container-runtimes/#cgroup-drivers"
author: "Kubernetes Documentation"
tags:
  - kubernetes/container-runtime
  - kubernetes/kubelet
---

# container-runtime - Cgroup Drivers systemd vs cgroupfs

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[container-runtime]] > [[container-runtime-deeper]] > **Cgroup Drivers**

---

## 📑 1. What is a Cgroup Manager?
Operating systems use a cgroup manager to organize resource limits (CPU, memory) in a tree hierarchy. On modern Linux distributions (e.g. RHEL, Ubuntu), `systemd` acts as the primary cgroup manager.

---

## ⚙️ 2. Driver Types

### A. cgroupfs
The container runtime writes limits directly to the `/sys/fs/cgroup` directory file hierarchy.
* **Warning:** If systemd is running on the host, you will have two competing cgroup managers trying to allocate resources, leading to unstable nodes and resource starvation under heavy load.

### B. systemd
The container runtime and Kubelet request systemd to manage cgroup resource allocations.
* **Standard:** Recommended for production. Both Kubelet and Container Runtime must use this driver.

---

## 🔬 3. CKA Verification Commands
Inspect both components to verify driver alignment:

### 1. Check Kubelet Driver
```bash
grep -i cgroupDriver /var/lib/kubelet/config.yaml
# Expected: cgroupDriver: systemd
```

### 2. Check Containerd Driver
Verify `SystemdCgroup = true` in `/etc/containerd/config.toml`:
```toml
[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
  SystemdCgroup = true
```

*Read more in [[Reference Notes/0-3_node_mechanics_and_resource_limits.md#7-host-isolation-mechanics-namespaces-and-cgroups]]*\n