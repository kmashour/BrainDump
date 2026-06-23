---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
sub_type: deep-dive
source_type: youtube
parent_concept: "[[linux]]"
tags:
  - linux/storage
  - linux/lvm
---

# Linux - Logical Volume Manager (LVM)

**Breadcrumbs:** [[Main Notes/linux|🏠 Linux Landing]] > **Logical Volume Manager**

---

## 🏛️ LVM Architecture

The Logical Volume Manager (LVM) abstracts physical storage devices, allowing administrators to group drives and partition space dynamically. This avoids the limitations of traditional, static partitions (like MBR or GPT) where resizing require system unmounts or partition table writes.

```
+-----------------------------------------------------------------+
|                      Logical Volume (LV)                        |
|   - Mounted to a directory (e.g. /var/lib/mysql)                |
|   - Formatted with a filesystem (XFS, ext4)                     |
+-----------------------------------------------------------------+
                                |  Mapped allocation
+-----------------------------------------------------------------+
|                      Volume Group (VG)                          |
|   - Virtual pool of storage                                     |
|   - Aggregates all Physical Extents (PEs)                       |
+-----------------------------------------------------------------+
                                |  Pooled resources
+-----------------------------------------------------------------+
|                    Physical Volume (PV)                         |
|   - Physical block devices / partitions (e.g. /dev/sdb1, /dev/sdc1)|
|   - Segmented into Physical Extents (PE)                        |
+-----------------------------------------------------------------+
```

---

## ⚙️ Core Components

1.  **Physical Volume (PV):**
    *   The raw physical disk (e.g., `/dev/sdb`) or partition (e.g., `/dev/sdb1`) initialized for LVM use.
    *   LVM writes a header metadata label to the first sectors of the device.
2.  **Volume Group (VG):**
    *   The pool of storage created by combining one or more Physical Volumes.
    *   VGs segment storage into fixed-size chunks called **Physical Extents (PE)**, typically 4 MB by default.
3.  **Logical Volume (LV):**
    *   A virtual partition carved out of a Volume Group.
    *   An LV consists of a collection of **Logical Extents (LE)** that map directly to Physical Extents in the VG.
    *   LVs can be formatted with filesystems (XFS, ext4) and mounted like standard devices.

---

## 📈 Evolutionary Comparison: Static Partitions vs. LVM

| Feature | Static Partitioning (MBR/GPT) | Logical Volume Manager (LVM) |
| :--- | :--- | :--- |
| **Resizing** | Requires unmounting; offline expansion; risky partition boundaries adjustments. | **Online expansion** (filesystem dependent); sizes can span multiple physical disks. |
| **Spanning** | A partition must be contiguous on a single physical disk. | Volumes can span across multiple disks dynamically. |
| **Snapshots** | Not supported at partition level (requires external filesystem/hypervisor tools). | **Native copy-on-write (CoW) snapshots** supported for backups. |
| **RAID** | Requires hardware controller or manual `mdadm` software array assembly. | Supports native LVM striping (RAID 0) and mirroring (RAID 1) directly. |

---

## 🛠️ Operational Command Cheat Sheet

### 1. Creation Pipeline
```bash
# 1. Initialize PV
pvcreate /dev/sdb1 /dev/sdc1

# 2. Create VG named vg_data
vgcreate vg_data /dev/sdb1 /dev/sdc1

# 3. Create a 100GB LV named lv_reports
lvcreate -L 100G -n lv_reports vg_data
```

### 2. Extension Pipeline
```bash
# 1. Add new physical disk to PV pool
pvcreate /dev/sdd1

# 2. Extend Volume Group
vgextend vg_data /dev/sdd1

# 3. Extend Logical Volume online (add 50GB)
lvextend -L +50G /dev/vg_data/lv_reports

# 4. Grow the active filesystem (Ext4 example)
resize2fs /dev/vg_data/lv_reports

# 5. Grow the active filesystem (XFS example - requires mount path)
xfs_growfs /mnt/reports
```
