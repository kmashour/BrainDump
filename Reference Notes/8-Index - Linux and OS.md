---
obsidianUIMode: preview
class: index-note
tier: reference-note
tags:
  - linux/reference-index
  - obsidian/moc
---

# 🐧 Linux and Operating Systems Reference MOC

**Breadcrumbs:** [[--Index--|🏠 Index]] > **Linux and OS Reference MOC**

---

## 🏛️ Reference Modules & Frameworks

This index contains our Linux systems administration and Operating Systems study modules, spanning from low-level kernel architectures to enterprise clustering and disaster recovery.

- 🐧 **[Module 8-1: Linux Kernel Architecture & Process Mechanics](8-1_linux_architecture_and_kernel.md)**
  * Kernel vs. User space, Syscall interfaces, Loadable Kernel Modules, Process lifecycle (fork/exec, PID 1, signaling), CFS Scheduler, and cgroups/namespaces isolation.
- 💾 **[Module 8-2: File Systems & Advanced Storage](8-2_filesystems_and_storage.md)**
  * Virtual File System (VFS) layer, inode metadata tables, page cache vs. block cache, LVM volume pooling, software RAID topologies, and LUKS encryption.
- 🔌 **[Module 8-3: Network Interface & Services](8-3_networking_and_services.md)**
  * TCP/IP stack implementation, dynamic routing protocols (BGP/OSPF), Netfilter/iptables/nftables firewalls, SDN principles (OpenFlow, OVS), and Network Function Virtualization.
- 🔒 **[Module 8-4: User Management, Security & Hardening](8-4_user_management_and_hardening.md)**
  * POSIX permissions (SUID/SGID/Sticky bit), Access Control Lists (ACLs), Linux capabilities, SELinux/AppArmor MAC enforcement, PAM authentication, and auditd system auditing.
- ⚙️ **[Module 8-5: System Services, Initialization & Daemonization](8-5_system_services_and_initialization.md)**
  * Init system evolution: SysV init runlevels vs. Upstart events vs. modern systemd unit/target dependency graphs. Process daemonization and zombie reaping.
- 📊 **[Module 8-6: Monitoring, Logs & System Diagnostics](8-6_monitoring_logs_and_diagnostics.md)**
  * System logging (rsyslog, logrotate, journald binary logs), monitoring metrics (Prometheus Node Exporter), and diagnostic toolsets (strace, lsof, iostat, sar).
- 🗃️ **[Module 8-7: High Availability, Virtualization & Clustering](8-7_high_availability_and_clustering.md)**
  * Keepalived/Pacemaker clustering, KVM/QEMU hypervisor virtualization, and kernel process sandboxing.
- 🚀 **[Module 8-8: Enterprise Automation, Backup & Cloud Integration](8-8_automation_backup_and_cloud.md)**
  * Scripting (Bash/Python), agentless configuration (Ansible), cloud-init provisioning, and system backup/recovery procedures (rsync, dd).

---

## 🛠️ Verification Projects
Hands-on playbooks and milestone projects:
- 🚀 **[Project: High-Availability Keepalived Load Balancing](../Projects/Linux/Project%20-%20HA%20Keepalived%20Load%20Balancing.md)**
- 🚀 **[Project: Migrating legacy init scripts to systemd](../Projects/Linux/Project%20-%20Migrating%20Legacy%20Init%20Scripts%20to%20systemd.md)**
