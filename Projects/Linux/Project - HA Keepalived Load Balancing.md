---
obsidianUIMode: preview
class: project-note
tier: project
domains: ["linux", "networking"]
concepts_referenced: ["[[init]]", "[[bgp]]"]
difficulty: "intermediate"
status: "completed"
---

# Project: High-Availability Keepalived Load Balancing

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Projects > **HA Keepalived Load Balancing**

---

## 🎯 Project Overview
This project provides a complete configuration playbook to establish a High-Availability (HA) load balancing layer using two Linux servers running **Keepalived** and the **Virtual Router Redundancy Protocol (VRRP)**. 

By completing this PoC:
1. Two active nodes (Primary and Backup) share a single **Virtual IP (VIP)**.
2. Clients target the VIP (rather than individual node IPs) to access a backend service (e.g. Nginx).
3. If the Primary node suffers a network or service failure, the Backup node automatically assumes the VIP in under 2 seconds.
4. A custom health check script automatically demotes nodes if the local backend service crashes.

---

## 🏛️ Target Architecture

```
        Client Traffic (Virtual IP: 192.168.1.100)
                         |
           +-------------+-------------+
           | (VRRP Heartbeat over eth0)|
           v                           v
  +------------------+        +------------------+
  |   Primary Node   |        |   Backup Node    |
  |  (State: MASTER) |        |  (State: BACKUP) |
  |   Priority: 101  |        |   Priority: 100  |
  |   IP: 192.168.1.11|        |   IP: 192.168.1.12|
  +------------------+        +------------------+
```

---

## 🛠️ Step-by-Step Implementation & Configuration

### 1. Installing Keepalived and Nginx
Install Keepalived and Nginx (acting as our target application service) on both cluster nodes.

#### The Answer:
Run on both nodes:
```bash
sudo apt update && sudo apt install -y keepalived nginx
```

#### The Assumptions:
* You are using Debian/Ubuntu-based servers with internet access.
* The nodes are located on the same Layer 2 broadcast domain (IP subnet `192.168.1.0/24`).
* Primary Node IP is `192.168.1.11`.
* Backup Node IP is `192.168.1.12`.
* Virtual IP is `192.168.1.100`.

---

### 2. Configuring Keepalived on the Primary Node
Configure Keepalived on the Primary node to act as the VRRP **MASTER**.

#### The Answer:
Create and edit `/etc/keepalived/keepalived.conf` on the Primary node:
```ini
# Script block to monitor Nginx daemon health
vrrp_script check_nginx {
    script "/usr/bin/killall -0 nginx"
    interval 2                         # Run check every 2 seconds
    weight -20                         # Subtract 20 from priority if script fails
}

vrrp_instance VI_1 {
    state MASTER
    interface eth0                     # Physical interface binding
    virtual_router_id 51               # Must match across MASTER and BACKUP
    priority 101                       # Highest priority wins master status
    advert_int 1                       # Broadcast advertisements every 1s

    authentication {
        auth_type PASS
        auth_pass SecretClusterToken123
    }

    virtual_ipaddress {
        192.168.1.100/24               # Shared Virtual IP
    }

    track_script {
        check_nginx
    }
}
```

#### The Rationale (Why):
* `killall -0 nginx` checks if the Nginx process exists without sending a termination signal.
* `weight -20` ensures that if Nginx crashes on the Primary, its active priority drops from `101` to `81`. Since the Backup has a priority of `100`, the Backup will immediately preempt and assume Master status.

---

### 3. Configuring Keepalived on the Backup Node
Configure Keepalived on the Backup node to act as the VRRP **BACKUP**.

#### The Answer:
Create and edit `/etc/keepalived/keepalived.conf` on the Backup node:
```ini
vrrp_script check_nginx {
    script "/usr/bin/killall -0 nginx"
    interval 2
    weight -20
}

vrrp_instance VI_1 {
    state BACKUP
    interface eth0
    virtual_router_id 51
    priority 100                       # Lower priority than Master (101)
    advert_int 1

    authentication {
        auth_type PASS
        auth_pass SecretClusterToken123
    }

    virtual_ipaddress {
        192.168.1.100/24
    }

    track_script {
        check_nginx
    }
}
```

---

### 4. Adjusting Kernel Binding Parameters
If a node is in Backup mode, Nginx will try to bind to the VIP (`192.168.1.100`) which is not yet present on its interfaces. To prevent Nginx from failing to start, we must enable non-local binding in the kernel.

#### The Answer:
Run on both nodes to enable non-local socket binding:
```bash
echo "net.ipv4.ip_nonlocal_bind=1" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

#### The Failure Loop (What if not):
If `ip_nonlocal_bind` is disabled, starting Nginx on the Backup node will crash with the error:
`nginx: [emerg] bind() to 192.168.1.100:80 failed (Cannot assign requested address)`.

---

### 5. Starting the Services
Start and enable both services.

#### The Answer:
Run on both nodes:
```bash
sudo systemctl enable --now nginx keepalived
```

---

## 🔍 Verification & Diagnostics

### 1. Inspecting Virtual IP Bindings
Verify that the Primary node has bound the Virtual IP.
```bash
# Run on Primary Node (192.168.1.11)
ip addr show eth0
```
*Expected Output:*
```
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    inet 192.168.1.11/24 brd 192.168.1.255 scope global eth0
    inet 192.168.1.100/24 scope global secondary eth0
```

```bash
# Run on Backup Node (192.168.1.12)
ip addr show eth0
```
*Expected Output:*
```
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    inet 192.168.1.12/24 brd 192.168.1.255 scope global eth0
```

---

### 2. Testing Failover Mechanics
Simulate a service crash on the Primary node and monitor the IP takeover.

#### Step A: Stop Nginx on the Primary
```bash
# Run on Primary Node
sudo systemctl stop nginx
```

#### Step B: Query Keepalived Logs on Backup
Check journal logs on the Backup node to verify state transition:
```bash
# Run on Backup Node
journalctl -u keepalived -n 20
```
*Expected Output:*
```
Keepalived_vrrp[1243]: VRRP_Instance(VI_1) Entering MASTER STATE
Keepalived_vrrp[1243]: VRRP_Instance(VI_1) setting protocol VIPs.
Keepalived_vrrp[1243]: Sending gratuitous ARP on eth0 for 192.168.1.100
```

#### Step C: Verify IP Migration
```bash
# Run on Backup Node
ip addr show eth0
# Expected: Now displays 'inet 192.168.1.100/24 scope global secondary eth0'
```

#### Step D: Recover the Primary Service
```bash
# Run on Primary Node
sudo systemctl start nginx
```
Keepalived will restart, restore priority to `101`, and preempt back the VIP from the Backup node, displaying `Entering MASTER STATE` in the logs.
