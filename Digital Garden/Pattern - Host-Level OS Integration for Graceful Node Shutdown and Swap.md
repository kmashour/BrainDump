---
obsidianUIMode: preview
class: pattern-note
tier: main-note
domains:
  - "kubernetes"
  - "linux"
components:
  - "[[kubelet]]"
  - "[[node]]"
sources:
  - "[[Reference Notes/0-14_cluster_administration_and_observability.md]]"
tags:
  - architecture/pattern
  - kubernetes/kubelet
  - linux/systemd
  - linux/kernel
---

# Pattern: Host-Level OS Integration for Graceful Node Shutdown and Swap

**Breadcrumbs:** [[0-Index|🏠 Index]] > Patterns > **Host-Level OS Integration for Graceful Node Shutdown and Swap**

---

## 🏛️ Architectural Context

For worker nodes to run reliably, the Kubernetes control plane agent (`kubelet`) must integrate with the host's operating system components. Two key areas illustrate this dependency: **Graceful Node Shutdown** (relying on systemd logind inhibitor locks) and **Swap Memory Management** (relying on Linux kernel cgroups v2 boundaries and kernel swappiness configuration).

If these systems are configured in isolation, it leads to system instability:
1. **Shutdown Failure:** Without adjusting host-level logind delay settings, systemd will kill the Kubelet and shut down the machine before pods can be drained.
2. **Swap Crash or Thrashing:** Without cgroups v2, the Kubelet cannot enforce container-level swap boundaries, and setting swap limits will fail. Similarly, default kernel swappiness values might lead to excessive disk I/O under memory pressure.

```
+-----------------------------------------------------------------------------------------+
| WORKER NODE HOST (RHEL / Ubuntu / Debian)                                               |
|                                                                                         |
|  [ Linux Kernel (cgroups v2) ] <------ Sets memory.swap.max ----- [ Container Runtime ] |
|               |                                                            ^            |
|         Reads swappiness                                                   |            |
|               v                                                            |            |
|       [ Swap Storage ]                                                     | Directs    |
|                                                                            |            |
|  [ systemd-logind ] <==== DBus Inhibitor Lock ====> [ Kubelet Service ] ---+            |
|  (InhibitDelayMaxSec)                               (failSwapOn: false)                 |
|                                                     (LimitedSwap)                       |
|                                                                                         |
+-----------------------------------------------------------------------------------------+
```

---

## ⚖️ Trade-offs & Alternatives

### Node Shutdown Coordination
* **Approach A: Coordinated Kubelet + systemd logind delay (Recommended)**
  * **Pros:** Standard workloads get a full window to save state and close connections; critical control plane components receive a final dedicated window to clean up.
  * **Cons:** Increases host reboot times since systemd must wait for the inhibitor lock duration to expire.
* **Approach B: Instant Power-off (Uncoordinated)**
  * **Pros:** Rapid reboots and host recovery.
  * **Cons:** Risk of state database corruption, orphan volumes, and delayed rescheduling of stateful workloads.

### Swap Management
* **Approach A: Swap Disabled (Traditional)**
  * **Pros:** Guaranteed predictable latency; workloads are evited or killed cleanly when RAM is saturated.
  * **Cons:** Zero tolerance for memory spikes; causes high pod churn rates on nodes with volatile workloads.
* **Approach B: LimitedSwap with cgroups v2 (Modern)**
  * **Pros:** Prevents immediate OOM crashes by swapping out cold pages to disk, providing a temporary buffer.
  * **Cons:** Workloads accessing swapped pages suffer disk read latency (performance degradation).

---

## 🛠️ Verification & Practical Implementation

To implement host-level integration:

### Step 1: Configure systemd logind for Graceful Shutdown
1. Define the maximum delay systemd will wait for inhibitor locks. Create an override file:
   ```ini
   # /etc/systemd/logind.conf.d/kubelet-delay.conf
   [Login]
   InhibitDelayMaxSec=45
   ```
2. Restart the logind service:
   ```bash
   sudo systemctl restart systemd-logind
   ```

### Step 2: Configure Linux Kernel Swap Parameters
1. Enable cgroups v2 on the host (verify via `mount | grep cgroup`).
2. Add sysctl overrides for swappiness to reduce aggressive swapping:
   ```ini
   # /etc/sysctl.d/99-kubernetes-swap.conf
   vm.swappiness=10
   ```
3. Apply kernel settings:
   ```bash
   sudo sysctl --system
   ```

### Step 3: Configure Kubelet Configuration
1. Align the Kubelet parameters to match host-level delay and swap availability:
   ```yaml
   # /var/lib/kubelet/config.yaml
   apiVersion: kubelet.config.k8s.io/v1beta1
   kind: KubeletConfiguration
   failSwapOn: false
   memorySwap:
     swapBehavior: LimitedSwap
   gracefulNodeShutdown: true
   shutdownGracePeriod: 30s
   shutdownGracePeriodCriticalPods: 10s
   ```
2. Restart Kubelet:
   ```bash
   sudo systemctl restart kubelet
   ```
