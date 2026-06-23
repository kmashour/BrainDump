---
obsidianUIMode: preview
class: project-playbook
tier: project-playbook
tags:
  - project
  - linux/storage
  - linux/lvm
  - linux/raid
---

# Project: Disk Partitioning, Software RAID & LVM Volume Expansion

**Breadcrumbs:** [[8-Index - Linux and OS|🏠 Linux and OS Index]] > **Projects** > **Disk Partitioning, Software RAID & LVM Volume Expansion**

---

## 🎯 Project Objective
This playbook details how to format raw storage media, assemble redundant RAID arrays using `mdadm`, configure Logical Volume Management (LVM) volume pools, and dynamically expand active filesystems online without data corruption.

---

## 💻 Scenario
A database storage directory `/var/lib/mysql/` is currently running out of space. You are provided with 4 raw physical block devices: `/dev/sdb`, `/dev/sdc`, `/dev/sdd`, and `/dev/sde`.
1.  Use the first 3 disks to build a redundant software RAID 5 array named `/dev/md0` with `/dev/sde` as a spare.
2.  Initialize the RAID device as a Physical Volume (PV) under LVM.
3.  Pool it into a Volume Group named `vg_database`.
4.  Allocate a 50 GB Logical Volume named `lv_mysql` and format it with XFS.
5.  Simulate a dynamic expansion requirement: add another disk (`/dev/sdf`) to the pool, extend the Volume Group, grow `lv_mysql` by 20 GB, and resize the live XFS filesystem online.

---

## 🛠️ Step-by-Step Implementation

### Step 1: Design Partitions & Initialize RAID 5 Array
Verify your disk topology and run the RAID assembly sequence.
```bash
# Verify raw disk paths
lsblk

# Partition disks sdb, sdc, sdd, sde (set type to 'Linux raid autodetect' - FD00)
# (Here we use gdisk for GPT partitions)
for disk in sdb sdc sdd sde; do
  gdisk /dev/$disk <<EOF
n
1


fd00
w
Y
EOF
done

# Create RAID 5 Array with 3 active devices and 1 hot spare
mdadm --create /dev/md0 --level=5 --raid-devices=3 /dev/sdb1 /dev/sdc1 /dev/sdd1 --spare-devices=1 /dev/sde1

# Monitor active synchronization progress
cat /proc/mdstat
```

### Step 2: Build the LVM Hierarchy
Convert the RAID array block device `/dev/md0` into virtual storage pools.
```bash
# Initialize Physical Volume (PV)
pvcreate /dev/md0

# Verify PV details
pvdisplay /dev/md0

# Create Volume Group (VG) pooling the PV
vgcreate vg_database /dev/md0

# Allocate Logical Volume (LV)
lvcreate -L 50G -n lv_mysql vg_database

# Format the Logical Volume with XFS
mkfs.xfs /dev/vg_database/lv_mysql

# Create target directory and mount it
mkdir -p /var/lib/mysql
mount /dev/vg_database/lv_mysql /var/lib/mysql
```

### Step 3: Configure Persistent Mounting
Ensure the filesystem automatically mounts on system startup.
```bash
# 1. Fetch UUID of the newly created Logical Volume
blkid /dev/vg_database/lv_mysql

# 2. Add entry in /etc/fstab
# Append:
# UUID=[UUID-value-here] /var/lib/mysql xfs defaults 0 0

# 3. Validate mount syntax
mount -a
```

### Step 4: Online LVM Volume Group and Filesystem Expansion
When database utilization spikes, execute dynamic expansion.
```bash
# Assume a new disk /dev/sdf is attached to the server.
# 1. Partition /dev/sdf
gdisk /dev/sdf <<EOF
n
1


8e00
w
Y
EOF

# 2. Create PV on the new partition
pvcreate /dev/sdf1

# 3. Add the PV to our existing Volume Group
vgextend vg_database /dev/sdf1

# 4. Expand Logical Volume by adding 20 GB
lvextend -L +20G /dev/vg_database/lv_mysql

# 5. Expand the live XFS filesystem online
# (Note: XFS requires the mount path as argument, unlike ext4 which uses the device path)
xfs_growfs /var/lib/mysql
```

---

## 🔬 Verification & Diagnostics
```bash
# 1. Inspect partition alignment and block mappings
lsblk -f

# 2. Check filesystem sizing
df -hT /var/lib/mysql

# 3. Inspect LVM statuses
vgdisplay vg_database
lvdisplay /dev/vg_database/lv_mysql

# 4. Monitor RAID array health and verify spare disk status
mdadm --detail /dev/md0
```
*Expected Output check:* The `/var/lib/mysql` filesystem size must reflect 70 GB and should remain mounted during execution.
