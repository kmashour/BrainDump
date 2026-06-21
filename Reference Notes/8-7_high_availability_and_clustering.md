---
obsidianUIMode: preview
class: reference-note
tier: reference-note
tags:
  - linux/clustering
  - linux/ha
  - virtualization
  - container/mechanics
---

# Module 8-7: High Availability, Virtualization & Clustering

**Breadcrumbs:** [[8-Index - Linux and OS|🏠 Linux and OS Index]] > **HA & Clustering**

---

## 🏛️ High Availability (HA) Principles & Topologies

High Availability clustering ensures that system services remain active and reachable even in the event of hardware, virtualization, or network path failures.

### Active-Passive vs. Active-Active
*   **Active-Passive Topology:** A primary node handles all active client traffic. A passive (standby) node monitors the primary via a heartbeat network. If the primary fails, the passive node takes over the virtual services.
*   **Active-Active Topology:** All cluster nodes actively handle client traffic simultaneously. Requires a load balancer to distribute connections. If one node fails, the surviving nodes absorb the remaining traffic load.

### Split-Brain Mitigation
A **Split-Brain** condition occurs when the network link connecting cluster nodes breaks, but the nodes remain running. Each node believes the other has crashed. In an Active-Passive setup, both nodes will attempt to bind the Virtual IP and write to shared storage, causing datastore corruption.
*   **Mitigation Strategies:**
    1.  **Quorum Rules:** Ensures that cluster operations are only permitted on the partition containing the majority of nodes (e.g. `n/2 + 1` nodes).
    2.  **STONITH (Shoot The Other Node In The Head):** A hard hardware fencing mechanism. The surviving node uses an out-of-band management controller (IPMI, iLO) or network power switch to cut the power of the non-communicating node before taking over resources.
    3.  **SBD (Storage-Based Death):** Fences nodes using a shared disk watchdog timer. If heartbeats stop, the nodes write self-termination poison pills to the disk.

---

## ⚙️ Clustering Frameworks: Keepalived & Pacemaker

### Keepalived (VRRP Protocol)
Keepalived uses the **Virtual Router Redundancy Protocol (VRRP)** to share a single Virtual IP (VIP) address between multiple active/passive routers/load balancers.

```
       Client Traffic (VIP: 192.168.1.50)
                     |
         +-----------+-----------+
         | (VRRP Heartbeats)     |
         v                       v
+------------------+    +------------------+
|   Primary Node   |    |   Backup Node    |
|   (Master - VIP) |    |     (Standby)    |
|   192.168.1.10   |    |   192.168.1.11   |
+------------------+    +------------------+
```

*   **Mechanism:**
    1.  The Master node binds the VIP and periodically broadcasts VRRP advertisement packets to the Backup node.
    2.  If the Backup node misses advertisements for a configured timeout, it takes over the VIP and broadcasts gratuitous ARP packets to update physical switches.

**Keepalived Configuration (`/etc/keepalived/keepalived.conf`):**
```ini
vrrp_instance VI_1 {
    state MASTER                  # Initial state (BACKUP on secondary node)
    interface eth0                # Network interface binding
    virtual_router_id 51          # Unique identifier (must match across peers)
    priority 101                  # High priority wins Master election (e.g., secondary has 100)
    advert_int 1                  # Broadcast interval in seconds

    authentication {
        auth_type PASS
        auth_pass SecretToken
    }

    virtual_ipaddress {
        192.168.1.50/24           # The shared Virtual IP (VIP)
    }
}
```

### Pacemaker & Corosync
*   **Corosync:** The cluster engine responsible for managing node membership, consensus, and secure heartbeat messaging between nodes.
*   **Pacemaker:** The Cluster Resource Manager (CRM) that monitors resource states (services, file systems, VIPs) and orchestrates starts/stops/failovers across cluster members.

---

## 💻 Virtualization (KVM) vs. Container Mechanics

Operating system partitioning ranges from hardware-level virtualization to kernel-level process namespaces.

### KVM/QEMU Hypervisor Virtualization
*   **KVM (Kernel-based Virtual Machine):** A Linux kernel module that turns the kernel into a Type-1 Hypervisor. It exposes `/dev/kvm` to leverage CPU hardware virtualization extensions (Intel VT-x or AMD-V).
*   **QEMU:** Emulates hardware (motherboards, network controllers, PCI slots) in user space for the guest operating system.

### Container Sandboxing Deep-Dive
Containers do not execute a separate kernel or run a hypervisor. They are standard Linux processes executing directly on the host kernel, isolated via kernel parameters:
*   **Resource Throttling (cgroups):** Restricts the amount of CPU cycles, physical memory pages, and I/O writes a process can consume.
*   **Namespace Boundaries:** Isolates what the process can "see" (e.g. other PIDs, network routing tables, hostnames, file system mounts).
*   **`chroot` / `pivot_root`:** Restricts a process's view of the directory hierarchy, locking it into a target folder acting as `/` (root).
*   **`runc`:** The standardized CLI tool that configures namespaces, cgroups, and executes container boundaries before launching the target container application.
*   **Alternative Sandboxes (e.g. gVisor / Kata):**
    *   *gVisor:* Intercepts container system calls and runs them inside a user-space kernel (Sentry), protecting the host kernel.
    *   *Kata Containers:* Runs the container inside a lightweight microVM, using QEMU/KVM virtual hardware barriers for maximum security.
