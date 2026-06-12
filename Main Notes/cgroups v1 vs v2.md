---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[node]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/architecture/nodes/#cgroups-version"
author: "Kubernetes Documentation"
tags:
  - kubernetes/node
  - kubernetes/architecture
---

# node - cgroups v1 vs v2

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[node]] > **cgroups v1 vs v2**

---

## 📑 1. Linux cgroups Background
**Control Groups** (`cgroups`) are a Linux kernel feature that limits, accounts for, and isolates the resource usage (CPU, memory, disk I/O, network) of a collection of processes.

---

## ⚙️ 2. Core Differences

### cgroups v1
* **Architecture:** Uses a separate hierarchical directory tree for each resource controller (e.g. `/sys/fs/cgroup/cpu` and `/sys/fs/cgroup/memory` are separate).
* **Limitation:** Hard to manage dependencies between different resources (e.g., page cache writes are resource-heavy but memory cgroups cannot throttle I/O effectively because writeback controllers belong to the I/O tree).

### cgroups v2
* **Architecture:** Uses a unified hierarchy. All controllers are attached to a single tree structure.
* **Benefit:** Simplifies configuration, allows clean multi-resource allocation tracking, and enables features like rootless containers and systemd alignment.

---

## 🔬 3. Driver Configuration (systemd vs. cgroupfs)
In modern Linux distributions, `systemd` acts as the cgroup manager. To avoid duplicate cgroup structures, Kubernetes recommends setting the Kubelet's cgroup driver to `systemd`:
```yaml
# /var/lib/kubelet/config.yaml
cgroupDriver: systemd
```
Verify matching configuration in Containerd:
```toml
# /etc/containerd/config.toml
[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
  SystemdCgroup = true
```

*Read more in [[Reference Notes/0-3_node_mechanics_and_resource_limits.md#7-host-isolation-mechanics-namespaces-and-cgroups]]*\n