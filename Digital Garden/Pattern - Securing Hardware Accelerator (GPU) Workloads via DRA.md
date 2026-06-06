---
obsidianUIMode: preview
class: pattern-note
tier: main-note
domains:
  - "kubernetes"
  - "linux"
components:
  - "[[dynamic-resource-allocation]]"
  - "[[device-plugin]]"
  - "[[pod]]"
  - "[[node]]"
sources:
  - "Kubernetes Hardening Guide"
tags:
  - architecture/pattern
---

# Pattern: Securing Hardware Accelerator (GPU) Workloads via DRA

**Breadcrumbs:** [[Index|🏠 Index]] > Patterns > **Securing Hardware Accelerator (GPU) Workloads via DRA**

---

## 🏛️ Architectural Context

Provisioning high-performance hardware accelerators (like NVIDIA GPUs or custom ASICs) to containerized workloads requires coordinating Kubernetes orchestration with the host Linux kernel and hardware topology:

```
+---------------------------------------------------------------------------------+
|                                 WORKER HOST                                     |
|                                                                                 |
|  [ Pod Container ]                                                              |
|        |                                                                        |
|  (Pins CPU & NUMA node)                                                        |
|        v                                                                        |
|  [ Linux cgroups v2 ] <======(Alignment)======> [ NUMA Node / GPU Hardware ]     |
|        ^                                                ^                       |
|        |                                                |                       |
|   (Configures)                                     (Allocates)                  |
|        |                                                |                       |
|  [ Kubelet / Topology Manager ] --------------> [ DRA Driver ]                  |
|                                                                                 |
+---------------------------------------------------------------------------------+
```

1. **Topology Alignment:** Kubelet's **Topology Manager** queries local CPU, memory, and PCIe device structures.
2. **Resource Claim:** The scheduler associates a Pod's `ResourceClaim` with available GPU classes on a node.
3. **Driver Allocation:** The host **DRA Driver** receives the gRPC allocate call from Kubelet. It configures the hardware (e.g. GPU partitions) and mounts directories directly into the container namespace.
4. **Cgroup Enforcement:** Kubelet writes boundaries to host `/sys/fs/cgroup/kubepods.slice/` to pin memory and CPU cores on the same physical NUMA node as the GPU, minimizing latency.

---

## ⚖️ Trade-offs & Alternatives

*   **DRA (Dynamic Resource Allocation) vs. Legacy Device Plugins:**
    *   *Legacy Device Plugins:* Simple to configure, but limited to static integer counts (e.g. `nvidia.com/gpu: 1`). Offers no native way to share devices dynamically or pass custom parameters.
    *   *DRA:* Highly flexible (supports fractional slicing, runtime parameter passing, and PV-like claims). However, it adds control plane complexity and requires modern v1.36+ clusters.
*   **Topology Policies:**
    *   *`single-numa-node`:* Guarantees maximum throughput by rejecting Pods if CPU, memory, and GPUs cannot reside on the same NUMA node. High risk of pending Pods if resources are fragmented.
    *   *`best-effort`:* Maximizes Pod scheduling success, but can result in cross-NUMA memory transfers, creating networking bottleneck latency.

---

## 🛠️ Verification & Practical Implementation

### 1. Verification of Topology alignment
Verify NUMA node alignment on the host using `numactl`:
```bash
# Check NUMA hardware layout and distances
numactl --hardware

# Inspect CPU-to-GPU NUMA binding
nvidia-smi topo -m
```

### 2. Restricting DRA Driver Permissions
Secure the host daemonset by enforcing the node-restricted `associated-node:update` verb in the ClusterRole:
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: gpu-driver-role
rules:
- apiGroups: ["resource.k8s.io"]
  resources: ["resourceclaims/driver"]
  verbs: ["associated-node:update", "associated-node:patch"]
```

*Read more in [16_kubernetes_api_extension_and_operators.md](../Reference%20Notes/16_kubernetes_api_extension_and_operators.md#4-device-plugins)*
