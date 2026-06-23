---
obsidianUIMode: preview
class: project-playbook
tier: project-playbook
tags:
  - project
  - linux/services
  - linux/dns
---

# Project: BIND DNS Server Installation and Caching Name Server

**Breadcrumbs:** [[8-Index - Linux and OS|🏠 Linux and OS Index]] > **Projects** > **BIND DNS Server Installation and Caching Name Server**

---

## 🎯 Project Objective
This project walks through installing and configuring BIND DNS server, creating forward/reverse zones mapping records, and setting up a secure caching-only DNS server.

---

## 💻 Scenario
Design a private sub-network lookup environment:
1.  Configure BIND DNS (`named`) on host `192.168.12.10` serving domain `corp.local`.
2.  Enable caching capabilities: query forwarding settings routing lookup requests to public resolver `8.8.8.8`.
3.  Establish forward and reverse zone map records.

---

## 🛠️ Step-by-Step Implementation

### Step 1: Install BIND Packages
```bash
# Install named daemon and resolution tools
yum install -y bind bind-utils
```

### Step 2: Configure named.conf
Modify `/etc/named.conf` to bind listeners to host networking interfaces and enable queries.
```bash
# Backup original configuration file
cp /etc/named.conf /etc/named.conf.bak

# Override /etc/named.conf configurations
cat <<EOF > /etc/named.conf
options {
    listen-on port 53 { 127.0.0.1; 192.168.12.10; };
    directory       "/var/named";
    dump-file       "/var/named/data/cache_dump.db";
    statistics-file "/var/named/data/named_stats.txt";
    memstatistics-file "/var/named/data/named_mem_stats.txt";
    allow-query     { any; };

    # Enable query forwarding settings (Caching resolver mode)
    forwarders      { 8.8.8.8; 8.8.4.4; };
    recursion yes;

    dnssec-enable yes;
    dnssec-validation yes;

    /* Path to ISC DLV key */
    bindkeys-file "/etc/named.iscdlv.key";
    managed-keys-directory "/var/named/dynamic";
};

logging {
        channel default_debug {
                file "data/named.run";
                severity dynamic;
        };
};

# Define Forward Lookup Zone Mapping
zone "corp.local" IN {
    type master;
    file "corp.local.db";
    allow-update { none; };
};

# Define Reverse Lookup Zone Mapping
zone "12.168.192.in-addr.arpa" IN {
    type master;
    file "12.168.192.db";
    allow-update { none; };
};

include "/etc/named.rfc1912.zones";
include "/etc/named.root.key";
EOF
```

### Step 3: Write Zone Database Files
Create zone directories under `/var/named/`.

#### Forward Lookup Database `/var/named/corp.local.db`
```bash
cat <<EOF > /var/named/corp.local.db
$TTL 86400
@   IN  SOA  ns1.corp.local. admin.corp.local. (
                  2026062301 ; Serial
                  3600       ; Refresh
                  1800       ; Retry
                  604800     ; Expire
                  86400 )    ; Minimum
; NS Record
@      IN  NS   ns1.corp.local.

; Host IP A-records mappings
ns1    IN  A    192.168.12.10
web    IN  A    192.168.12.20
db     IN  A    192.168.12.30
EOF
```

#### Reverse Lookup Database `/var/named/12.168.192.db`
```bash
cat <<EOF > /var/named/12.168.192.db
$TTL 86400
@   IN  SOA  ns1.corp.local. admin.corp.local. (
                  2026062301 ; Serial
                  3600       ; Refresh
                  1800       ; Retry
                  604800     ; Expire
                  86400 )    ; Minimum
; NS Record
@      IN  NS   ns1.corp.local.

; PTR records mappings
10     IN  PTR  ns1.corp.local.
20     IN  PTR  web.corp.local.
30     IN  PTR  db.corp.local.
EOF
```

### Step 4: Secure File Permissions, Verify Configurations & Launch Service
Ensure files are owned by the `named` group and check files syntax.
```bash
# Apply owners
chown root:named /var/named/corp.local.db
chown root:named /var/named/12.168.192.db

# Verify configuration parsing syntaxes
named-checkconf /etc/named.conf
named-checkzone corp.local /var/named/corp.local.db
named-checkzone 12.168.192.in-addr.arpa /var/named/12.168.192.db

# Open DNS ports in firewall
firewall-cmd --permanent --add-service=dns
firewall-cmd --reload

# Start service
systemctl enable --now named
```

---

## 🔬 Verification & Diagnostics
Configure client system `/etc/resolv.conf` to target `nameserver 192.168.12.10`.
```bash
# 1. Test Forward Lookups
dig web.corp.local +short
# (Should return: 192.168.12.20)

# 2. Test Reverse Lookups
dig -x 192.168.12.30 +short
# (Should return: db.corp.local.)

# 3. Test Caching Resolution (Internet Access Query check)
dig google.com +short
# (Should resolve using public forwarders)
```
---
> [!TIP]
> Use `named-checkconf -z` to check all zone files configured in named config.
