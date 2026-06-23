---
obsidianUIMode: preview
class: project-playbook
tier: project-playbook
tags:
  - project
  - linux/services
  - linux/sharing
---

# Project: NFS and FTP Secure Network File Shares

**Breadcrumbs:** [[8-Index - Linux and OS|🏠 Linux and OS Index]] > **Projects** > **NFS and FTP Secure Network File Shares**

---

## 🎯 Project Objective
This project demonstrates configuring secure file-sharing systems: setting up NFS servers, client automount maps (`autofs`), configuring secure `vsftpd` servers, and configuring firewalls/SELinux parameters.

---

## 💻 Scenario
1.  **NFS Share:** Export `/srv/shares/documents` to client subnet `192.168.12.0/24` with read-write permissions, synchronizing operations.
2.  **Autofs Client Mounts:** Set up the client machine to dynamically automount the NFS share to `/mnt/auto/documents` only when accessed.
3.  **FTP Server:** Setup a vsftpd file server: disable anonymous logins, jail local system accounts to home folders, and configure firewalls.

---

## 🛠️ Step-by-Step Implementation

### Part 1: NFS Server Configuration
```bash
# 1. Install nfs utility package
yum install -y nfs-utils

# 2. Create the target share directory
mkdir -p /srv/shares/documents
chown -R nfsnobody:nfsnobody /srv/shares/documents
chmod 775 /srv/shares/documents

# 3. Add export configuration line to /etc/exports
echo "/srv/shares/documents 192.168.12.0/24(rw,sync,no_root_squash)" >> /etc/exports

# 4. Activate NFS services
systemctl enable --now rpcbind
systemctl enable --now nfs-server

# 5. Open firewall ports for NFS, Mountd, and RPC
firewall-cmd --permanent --add-service=nfs
firewall-cmd --permanent --add-service=mountd
firewall-cmd --permanent --add-service=rpc-bind
firewall-cmd --reload
```

### Part 2: Client Autofs Automount Configuration
Run these sequences on the client system:
```bash
# 1. Install autofs
yum install -y autofs nfs-utils

# 2. Define master map configuration in /etc/auto.master
# Append:
# /mnt/auto /etc/auto.documents --timeout=60

# 3. Create map file /etc/auto.documents
echo "documents -rw,sync 192.168.12.10:/srv/shares/documents" > /etc/auto.documents

# 4. Enable and start autofs
systemctl enable --now autofs
```

### Part 3: Secure FTP (vsftpd) Server
```bash
# 1. Install ftp server package
yum install -y vsftpd

# 2. Configure /etc/vsftpd/vsftpd.conf
# Enforce secure configuration parameters:
sed -i 's/anonymous_enable=YES/anonymous_enable=NO/' /etc/vsftpd/vsftpd.conf
sed -i 's/#chroot_local_user=YES/chroot_local_user=YES/' /etc/vsftpd/vsftpd.conf

# Append security parameters:
cat <<EOF >> /etc/vsftpd/vsftpd.conf
allow_writeable_chroot=YES
pasv_min_port=30000
pasv_max_port=30100
EOF

# 3. Configure SELinux: allow FTP daemon to read/write home directories
setsebool -P ftp_home_dir 1
# Allow full write capabilities to files
setsebool -P ftpd_full_access 1

# 4. Configure firewall ports
firewall-cmd --permanent --add-service=ftp
firewall-cmd --permanent --add-port=30000-30100/tcp
firewall-cmd --reload

# 5. Start vsftpd service
systemctl enable --now vsftpd
```

---

## 🔬 Verification & Diagnostics

### Verify NFS Mounts
```bash
# 1. Query active exports on NFS server
showmount -e localhost

# 2. On the client, access the autofs directory to trigger mount
cd /mnt/auto/documents
df -hT .
# (Verify that df lists active NFS mapping)
```

### Verify FTP Server Hardening
```bash
# Test anonymous login (should fail)
curl -u anonymous:password ftp://localhost/

# Test local user authenticated session
useradd ftpuser
echo "Password123" | passwd --stdin ftpuser
curl -u ftpuser:Password123 -T /etc/hosts ftp://localhost/
```
---
> [!IMPORTANT]
> If vsftpd client connections hang on file retrievals, verify that passive port ranges `30000-30100` are correctly open in the firewall.
