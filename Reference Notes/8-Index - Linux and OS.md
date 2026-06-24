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
- ⚙️ **[Module 8-9: Red Hat Enterprise Linux (RHEL) Administration](8-9_redhat_enterprise_linux_administration.md)**
  * Red Hat systems management: boot recovery (rd.break), network interfaces profiles (nmcli/teamd), RAID/LVM volumes, network file sharing (NFS/FTP), Apache HTTPD servers, BIND DNS servers, and FreeIPA LDAP authentication.

---

## 🛠️ Verification Projects
Hands-on playbooks and milestone projects:
- 🚀 **[Project: High-Availability Keepalived Load Balancing](../Projects/Linux/Project%20-%20HA%20Keepalived%20Load%20Balancing.md)**
- 🚀 **[Project: Migrating legacy init scripts to systemd](../Projects/Linux/Project%20-%20Migrating%20Legacy%20Init%20Scripts%20to%20systemd.md)**
- 🚀 **[Project: User Administration & POSIX/ACL Hardening](../Projects/Linux/Project%20-%20User%20Administration%20%26%20POSIX-ACL%20Hardening.md)**
- 🚀 **[Project: GRUB Boot Security & Root Password Recovery](../Projects/Linux/Project%20-%20GRUB%20Boot%20Security%20%26%20Root%20Password%20Recovery.md)**
- 🚀 **[Project: Disk Partitioning, Software RAID & LVM Volume Expansion](../Projects/Linux/Project%20-%20Disk%20Partitioning%2C%20Software%20RAID%20%26%20LVM%20Volume%20Expansion.md)**
- 🚀 **[Project: Network Interface Profiles, Teaming & Bridging](../Projects/Linux/Project%20-%20Network%20Interface%20Profiles%2C%20Teaming%20%26%20Bridging.md)**
- 🚀 **[Project: Log Rotation, Text Filtering & Automation Backup](../Projects/Linux/Project%20-%20Log%20Rotation%2C%20Text%20Filtering%20%26%20Automation%20Backup.md)**
- 🚀 **[Project: NFS and FTP Secure Network File Shares](../Projects/Linux/Project%20-%20NFS%20and%20FTP%20Secure%20Network%20File%20Shares.md)**
- 🚀 **[Project: Apache Web Server Deployment, Virtual Hosts, and Directory Security](../Projects/Linux/Project%20-%20Apache%20Web%20Server%20Deployment%2C%20Virtual%20Hosts%2C%20and%20Directory%20Security.md)**
- 🚀 **[Project: BIND DNS Server Installation and Caching Name Server](../Projects/Linux/Project%20-%20BIND%20DNS%20Server%20Installation%20and%20Caching%20Name%20Server.md)**
- 🚀 **[Project: Central LDAP/FreeIPA Domain Authentication](../Projects/Linux/Project%20-%20Central%20LDAP-FreeIPA%20Domain%20Authentication.md)**
- 🚀 **[Project: DHCP Server Installation and Dynamic IP Allocation](../Projects/Linux/Project%20-%20DHCP%20Server%20Installation%20and%20Dynamic%20IP%20Allocation.md)**
- 🚀 **[Project: iSCSI Target and Initiator Storage Configuration](../Projects/Linux/Project%20-%20iSCSI%20Target%20and%20Initiator%20Storage%20Configuration.md)**
- 🚀 **[Project: MariaDB Database Installation and User Security](../Projects/Linux/Project%20-%20MariaDB%20Database%20Installation%20and%20User%20Security.md)**
- 🚀 **[Project: ELK Stack Log Aggregation Clustering](../Projects/Linux/Project%20-%20ELK%20Stack%20Log%20Aggregation%20Clustering.md)**

