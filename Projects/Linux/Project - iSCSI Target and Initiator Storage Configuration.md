---
obsidianUIMode: preview
class: project-playbook
tier: project-playbook
tags:
  - project
  - linux/storage
  - linux/iscsi
---

# Project: iSCSI Target and Initiator Storage Configuration

**Breadcrumbs:** [[8-Index - Linux and OS|🏠 Linux and OS Index]] > **Projects** > **iSCSI Target and Initiator Storage Configuration**

---

## 🎯 Project Objective
This playbook covers establishing a remote SAN (Storage Area Network) block storage mapping using iSCSI. It details configuring an iSCSI Target server to share raw block devices and an Initiator client to mount them persistently.

---

## 💻 Scenario
1.  **iSCSI Target Server:** Host `192.168.12.10` sharing raw block device `/dev/sdb1` as LUN 0 under IQN `iqn.2026-06.com.example:server`.
2.  **iSCSI Initiator Client:** Host `192.168.12.11` configuring IQN `iqn.2026-06.com.example:client1` to connect and format the remote storage volume.

---

## 🛠️ Step-by-Step Implementation

### Step 1: Configure the iSCSI Target (Server)
Run these commands on Target Server `192.168.12.10`:
```bash
# 1. Install target command line interface wrapper
dnf install -y targetcli

# 2. Open iSCSI ports in firewall
firewall-cmd --permanent --add-port=3260/tcp
firewall-cmd --reload

# 3. Start target CLI configuration utility
# (We run these commands using targetcli shell syntax)
targetcli /backstores/block create name=disk1_backstore dev=/dev/sdb1
targetcli /iscsi create iqn.2026-06.com.example:server
targetcli /iscsi/iqn.2026-06.com.example:server/tpg1/luns create /backstores/block/disk1_backstore
targetcli /iscsi/iqn.2026-06.com.example:server/tpg1/acls create iqn.2026-06.com.example:client1
targetcli /iscsi/iqn.2026-06.com.example:server/tpg1/portals create 192.168.12.10 3260

# 4. Enable target service daemon
systemctl enable --now target
```

### Step 2: Configure the iSCSI Initiator (Client)
Run these commands on Client Node `192.168.12.11`:
```bash
# 1. Install initiator utilities
dnf install -y iscsi-initiator-utils

# 2. Define client IQN name
echo "InitiatorName=iqn.2026-06.com.example:client1" > /etc/iscsi/initiatorname.iscsi

# 3. Discover remote iSCSI target portal
iscsiadm --mode discoverydb --type sendtargets --portal 192.168.12.10 --discover

# 4. Log in to the target to attach block device
iscsiadm --mode node --targetname iqn.2026-06.com.example:server --portal 192.168.12.10:3260 --login

# 5. Enable auto-start initiator service daemons
systemctl enable --now iscsid iscsi
```

### Step 3: Format and Mount the Remote Device (Client)
Once logged in, the remote volume appears as a local SCSI drive (e.g. `/dev/sdc`):
```bash
# 1. Verify device name in system
lsblk

# 2. Format with ext4 filesystem
mkfs.ext4 /dev/sdc

# 3. Create mount target and mount block device
mkdir -p /mnt/iscsi-volume
mount /dev/sdc /mnt/iscsi-volume

# 4. Set persistent mount in /etc/fstab
# (NOTE: _netdev option is CRITICAL to delay mounting until network stack initialized)
echo "/dev/sdc /mnt/iscsi-volume ext4 defaults,_netdev 0 0" >> /etc/fstab
```

---

## 🔬 Verification & Diagnostics

### Audit Target Portal Status
On Client:
```bash
# View active login sessions
iscsiadm --mode session
```
*Expected Output snippet:*
```
tcp: [1] 192.168.12.10:3260,1 iqn.2026-06.com.example:server (non-flash)
```

### Disconnect / Log Out iSCSI Target
To cleanly disconnect the storage device:
```bash
# 1. Unmount the path
umount /mnt/iscsi-volume

# 2. Log out initiator session
iscsiadm --mode node --targetname iqn.2026-06.com.example:server --portal 192.168.12.10:3260 --logout
```
---
> [!WARNING]
> Editing `/etc/fstab` for an iSCSI volume without the `_netdev` mount option will cause a boot hang, as the system will attempt to mount the device before networking starts.
