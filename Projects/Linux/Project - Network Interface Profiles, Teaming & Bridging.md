---
obsidianUIMode: preview
class: project-playbook
tier: project-playbook
tags:
  - project
  - linux/networking
  - linux/teaming
---

# Project: Network Interface Profiles, Teaming & Bridging

**Breadcrumbs:** [[8-Index - Linux and OS|🏠 Linux and OS Index]] > **Projects** > **Network Interface Profiles, Teaming & Bridging**

---

## 🎯 Project Objective
This project demonstrates advanced NetworkManager CLI configurations, setting up physical and virtual connections, active-backup NIC teaming profiles configuration for network fault tolerance, and virtual bridge creation for VM environments.

---

## 💻 Scenario
A virtualization host requires:
1.  **Fault Tolerance:** Link two physical interfaces `ens37` and `ens38` into a logical team interface `team0` with `activebackup` runner configuration to survive hardware port failures.
2.  **IP Assignment:** Configure static IPv4 parameters on the team link.
3.  **Bridge Interface:** Set up a host bridge interface `br0` linked to physical network adapter `ens33` so virtual machines run directly on host subnets.

---

## 🛠️ Step-by-Step Implementation

### Step 1: Set up Active-Backup NIC Teaming
Configure NetworkManager profiles to bond physical interfaces under teaming controls.
```bash
# 1. Create team master interface profile
nmcli connection add type team con-name team0 ifname team0 config '{"runner": {"name": "activebackup"}}'

# 2. Assign static IPv4 settings to the team0 master profile
nmcli connection modify team0 ipv4.addresses "192.168.12.50/24"
nmcli connection modify team0 ipv4.gateway "192.168.12.1"
nmcli connection modify team0 ipv4.dns "8.8.8.8 8.8.4.4"
nmcli connection modify team0 ipv4.method manual

# 3. Add first slave interface profile to the master
nmcli connection add type team-slave con-name team0-slave1 ifname ens37 master team0

# 4. Add second slave interface profile to the master
nmcli connection add type team-slave con-name team0-slave2 ifname ens38 master team0

# 5. Bring up slave profiles and master profile
nmcli connection up team0-slave1
nmcli connection up team0-slave2
nmcli connection up team0
```

### Step 2: Set up Virtual Bridging
Create host networks routing bindings.
```bash
# 1. Add virtual bridge profile
nmcli connection add type bridge con-name br0 ifname br0

# 2. Configure static IP address on the bridge profile
nmcli connection modify br0 ipv4.addresses "192.168.1.50/24"
nmcli connection modify br0 ipv4.gateway "192.168.1.1"
nmcli connection modify br0 ipv4.dns "1.1.1.1"
nmcli connection modify br0 ipv4.method manual

# 3. Bind host physical interface ens33 as bridge port slave
nmcli connection add type bridge-slave con-name br0-slave ifname ens33 master br0

# 4. Bring up the bridge profiles
nmcli connection up br0-slave
nmcli connection up br0
```

---

## 🔬 Verification & Diagnostics

### Verify Link Mappings and Statuses
```bash
# Show active connection profiles
nmcli connection show --active

# Inspect teaming configurations and runner status
teamdctl team0 state
```

*Expected teamdctl Output snippet:*
```
setup:
  runner: activebackup
ports:
  ens37
    link watches:
      link count: 1
      active: true
  ens38
    link watches:
      link count: 1
      active: true
runner:
  active port: ens37
```

### Fault-Tolerance Testing (Simulating Port Failure)
We test failover behaviors by disabling the active link port.
```bash
# 1. Disable the active physical port
ip link set ens37 down

# 2. Re-verify teaming state
teamdctl team0 state
# (Verify that active port automatically switches to ens38 with zero connection drops)

# 3. Bring the interface back up and check status
ip link set ens37 up
teamdctl team0 state
```
---
> [!IMPORTANT]
> Ensure NetworkManager service is active and running during configuration:
> `systemctl status NetworkManager`
