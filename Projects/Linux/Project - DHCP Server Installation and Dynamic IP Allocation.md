---
obsidianUIMode: preview
class: project-playbook
tier: project-playbook
tags:
  - project
  - linux/services
  - linux/dhcp
---

# Project: DHCP Server Installation and Dynamic IP Allocation

**Breadcrumbs:** [[8-Index - Linux and OS|🏠 Linux and OS Index]] > **Projects** > **DHCP Server Installation and Dynamic IP Allocation**

---

## 🎯 Project Objective
This playbook covers installing, configuring, testing, and securing a Dynamic Host Configuration Protocol (DHCP) server on a Red Hat Enterprise Linux system to automate IPv4 parameters distribution.

---

## 💻 Scenario
1.  **DHCP Server Host:** `192.168.12.10` serving the subnet `192.168.12.0/24`.
2.  **Allocation Range:** Dynamic leases from `192.168.12.100` to `192.168.12.200`.
3.  **Client workstation:** Dynamic reservation mapped by MAC address to always receive IP `192.168.12.99`.

---

## 🛠️ Step-by-Step Implementation

### Step 1: Install DHCP Server Package
Run this command on the server host:
```bash
dnf install -y dhcp-server
```

### Step 2: Configure DHCP Daemon
Overwrite `/etc/dhcp/dhcpd.conf` with the subnet allocation rules:
```bash
cat <<EOF > /etc/dhcp/dhcpd.conf
# Domain settings
option domain-name "corp.local";
option domain-name-servers 192.168.12.10, 8.8.8.8;

# Default lease times (10 minutes defaults, 2 hours max)
default-lease-time 600;
max-lease-time 7200;

# Declare this server as authoritative for the local subnet
authoritative;

# Subnet parameters
subnet 192.168.12.0 netmask 255.255.255.0 {
    range 192.168.12.100 192.168.12.200;
    option routers 192.168.12.1;
    option broadcast-address 192.168.12.255;
}

# Static IP Reservation
host client-workstation {
    hardware ethernet 00:11:22:33:44:55;
    fixed-address 192.168.12.99;
}
EOF
```

### Step 3: Verify Configuration Syntax
Always verify the syntax before starting the service:
```bash
dhcpd -t -cf /etc/dhcp/dhcpd.conf
```
*Expected Output snippet:*
```
Internet Systems Consortium DHCP Server 4.2.5
Config file: /etc/dhcp/dhcpd.conf
Database file: /var/lib/dhcpd/dhcpd.leases
```

### Step 4: Configure Firewall and Start Daemon
```bash
# Allow DHCP traffic in firewall
firewall-cmd --permanent --add-service=dhcp
firewall-cmd --reload

# Start and enable the service
systemctl enable --now dhcpd
```

---

## 🔬 Verification & Diagnostics

### Audit Active Leases on Server
Check the lease database to track client IP allocations:
```bash
cat /var/lib/dhcpd/dhcpd.leases
```

### Test DHCP Client Request
On a client system located on the same network segment:
```bash
# Release current IP
dhclient -r

# Request a new dynamic IP address
dhclient -v
```
*Expected Output snippet:*
```
DHCPDISCOVER on eth0 to 255.255.255.255 port 67 interval 3
DHCPREQUEST on eth0 to 255.255.255.255 port 67
DHCPOFFER from 192.168.12.10
DHCPACK from 192.168.12.10 -- bound to 192.168.12.100
```
Verify the allocated IP parameters:
```bash
ip addr show eth0
cat /etc/resolv.conf
```
---
> [!NOTE]
> Ensure the DHCP server itself is configured with a static IP address in `/etc/sysconfig/network-scripts/ifcfg-eth0` to prevent service startup failures.
