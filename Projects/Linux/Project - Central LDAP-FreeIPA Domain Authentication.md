---
obsidianUIMode: preview
class: project-playbook
tier: project-playbook
tags:
  - project
  - linux/services
  - linux/ldap
  - linux/freeipa
---

# Project: Central LDAP/FreeIPA Domain Authentication

**Breadcrumbs:** [[8-Index - Linux and OS|🏠 Linux and OS Index]] > **Projects** > **Central LDAP-FreeIPA Domain Authentication**

---

## 🎯 Project Objective
This playbook covers establishing a centralized user identity directory using FreeIPA (which bundles LDAP, Kerberos, DNS, and Certificate Authority). It details server installations and configuring client systems enrollment procedures.

---

## 💻 Scenario
1.  **Server System:** Install and configure FreeIPA server on host `ipa.corp.local` (IP `192.168.12.10`).
2.  **Client System:** Enroll client node `client.corp.local` (IP `192.168.12.20`) to authenticate system logins against the central FreeIPA directory.

---

## 🛠️ Step-by-Step Implementation

### Step 1: FreeIPA Server Preparation and Installation
Run these steps on server `ipa.corp.local`:
```bash
# 1. Set hostname persistently
hostnamectl set-hostname ipa.corp.local

# 2. Add local host resolution map
echo "192.168.12.10 ipa.corp.local ipa" >> /etc/hosts

# 3. Install FreeIPA server packages
# (Requires RHEL Identity Management - IdM group repo subscription)
yum install -y ipa-server bind-dyndb-ldap ipa-server-dns

# 4. Install FreeIPA Server (Interactive setup configuration wrapper)
# We execute with automated options:
ipa-server-install \
  --realm=CORP.LOCAL \
  --domain=corp.local \
  --ds-password=DirectoryManagerPass123! \
  --admin-password=AdminUserPass123! \
  --no-ntp \
  --unattended

# 5. Open security ports in firewall
firewall-cmd --permanent --add-service=freeipa
firewall-cmd --reload
```

### Step 2: Enroll Client Systems
Run these steps on target node `client.corp.local`:
```bash
# 1. Install LDAP client enrollment utility
yum install -y ipa-client

# 2. Set client hostname
hostnamectl set-hostname client.corp.local

# 3. Ensure DNS resolves server hostname
echo "nameserver 192.168.12.10" > /etc/resolv.conf

# 4. Execute central domain enrollment script
ipa-client-install \
  --domain=corp.local \
  --server=ipa.corp.local \
  --realm=CORP.LOCAL \
  --principal=admin \
  --password=AdminUserPass123! \
  --mkhomedir \
  --unattended
```

---

## 🔬 Verification & Diagnostics

### Authenticate Admin Sessions
```bash
# 1. Request a Kerberos ticket for the admin account
kinit admin
# (Will prompt for: AdminUserPass123!)

# 2. Inspect active Kerberos ticket mappings
klist
```
*Expected klist Output snippet:*
```
Ticket cache: KEYRING:persistent:0:0
Default principal: admin@CORP.LOCAL

Valid starting       Expires              Service principal
23/06/2026 13:00:00  24/06/2026 13:00:00  krbtgt/CORP.LOCAL@CORP.LOCAL
```

### Test LDAP Directory Sync
On client node:
```bash
# 1. On the server, create a test directory account
ipa user-add ipatester --first=Test --last=User --password

# 2. On the client, search LDAP identity provider maps
getent passwd ipatester

# 3. Attempt SSH session login as the new user from another system
ssh ipatester@client.corp.local
# (Verify that the system automatically configures home folders on first login)
```
---
> [!IMPORTANT]
> Verify SSSD (System Security Services Daemon) is running on the client to handle offline caching:
> `systemctl status sssd`
