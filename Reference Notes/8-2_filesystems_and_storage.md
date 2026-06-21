---
obsidianUIMode: preview
class: reference-note
tier: reference-note
tags:
  - linux/vfs
  - linux/filesystems
  - linux/storage
  - linux/lvm
---

# Module 8-2: File Systems & Advanced Storage

**Breadcrumbs:** [[8-Index - Linux and OS|🏠 Linux and OS Index]] > **File Systems & Storage**

---

## 🏛️ File System Internals & VFS Architecture

The Linux kernel interacts with filesystems through an abstraction layer called the **Virtual File System (VFS)**. This allows the system to access different underlying file systems (ext4, XFS, NFS) using a single, unified POSIX system call interface (`open`, `read`, `write`).

```
+--------------------------------------------------------+
|                      System Calls                      |
|                  (open, read, write)                   |
+--------------------------------------------------------+
|             VFS (Virtual File System Layer)            |
|       Superblock | Inode | Dentry | File Objects       |
+--------------------------------------------------------+
|       ext4       |       XFS       |       NFS         |
+------------------+-----------------+-------------------+
|                   Block Device Layer                   |
+--------------------------------------------------------+
|                    Physical Disk                       |
+--------------------------------------------------------+
```

### VFS Core Objects
*   **Superblock:** Represents a specific mounted filesystem. Stores global metadata like block size, mount status, and filesystem type.
*   **Inode (Index Node):** Represents a specific file on disk. Contains file metadata (permissions, owner, size, timestamps, block pointers) but **not** the filename.
*   **Dentry (Directory Entry):** Links an inode to a human-readable filename, acting as a cache for directory structures to speed up file paths lookup.
*   **File Object:** Represents a specific open file instance associated with a process (stores file offset/cursor, open flags).

### Inode Mechanics & Links
A directory is a special file containing a list of filename-to-inode mappings.
*   **Hard Links:**
    *   Multiple filenames pointing to the exact same inode.
    *   Since they point directly to the inode, they cannot cross filesystem boundaries.
    *   Cannot link to directories (prevents circular loops).
    *   Deleting a file only removes its dentry mapping. The data is only deleted from disk when the inode's link count drops to `0`.
*   **Symbolic Links (Symlinks):**
    *   A unique file containing a text string of the path to another file.
    *   Can cross filesystem boundaries and link to directories.
    *   If the target file is deleted or moved, the symlink becomes "broken" (dangling).

### Journaling File Systems
To prevent data corruption during unexpected power losses, modern Linux filesystems use journaling (writing metadata changes to a log before writing them to the main filesystem blocks).
*   **Journaling Modes:**
    1.  **Metadata Journaling (default):** Only logs filesystem metadata updates. Fast but user data may be lost or corrupted.
    2.  **Full Data Journaling:** Logs both metadata and file data changes. Very safe but introduces high write overhead.
    3.  **Ordered Mode:** Writes file data to disk first, then writes metadata updates to the journal. Combines safety and performance.

### Extended Attributes & Access Control Lists (ACLs)
Standard Linux permissions only support Owner, Group, and Others. Extended Attributes (xattr) and ACLs support fine-grained permission control.
*   **Access Control Lists (ACLs):**
```bash
# Allow specific user read-write-execute on a file
setfacl -m u:username:rwx configuration.conf

# View active ACL mappings
getfacl configuration.conf

# Remove ACL settings for a user
setfacl -x u:username configuration.conf
```

---

## 💾 Storage Volume Management (LVM & Software RAID)

### Logical Volume Manager (LVM)
LVM abstract physical storage devices, allowing partitions (Logical Volumes) to be resized dynamically, pooled, or snapshotted.

```
+---------------------------------------------+
|               Logical Volume                | <-- Mountable Partition (/dev/vg0/lv_data)
+---------------------------------------------+
|                Volume Group                 | <-- Pooled Disk Space (vg0)
+---------------------------------------------+
|  Physical Volume   |    Physical Volume     | <-- Partition / Disk (/dev/sdb1, /dev/sdc)
+--------------------+------------------------+
```

*   **Physical Volumes (PV):** Represents a raw disk or partition formatted for LVM.
*   **Volume Groups (VG):** Pools multiple Physical Volumes together into a single administrative storage block.
*   **Logical Volumes (LV):** Partitions carved out of a Volume Group. These are formatted with filesystems and mounted.

**Common LVM Execution Commands:**
```bash
# Initialize disk partitions as LVM Physical Volumes
pvcreate /dev/sdb1 /dev/sdc1

# Create a Volume Group named 'vg_storage' pooling the PVs
vgcreate vg_storage /dev/sdb1 /dev/sdc1

# Create a 50GB Logical Volume named 'lv_data' out of the VG
lvcreate -L 50G -n lv_data vg_storage

# Format and Mount
mkfs.ext4 /dev/vg_storage/lv_data
mount /dev/vg_storage/lv_data /mnt/data

# Dynamically Extend the LV by 20GB and resize the ext4 filesystem online
lvextend -L +20G /dev/vg_storage/lv_data
resize2fs /dev/vg_storage/lv_data
```

### Device Mapper
The **Device Mapper** is the kernel framework underneath LVM, Multipath, and LUKS encryption. It maps physical block devices to virtual block devices.

### Software RAID (mdadm)
Standard Linux software RAID configurations allow storage combining for performance or redundancy:
*   **RAID 0 (Striping):** Combines drives for performance; no redundancy.
*   **RAID 1 (Mirroring):** Duplicates data across drives; high redundancy.
*   **RAID 5 (Parity):** Distributed parity across 3+ drives; tolerates 1 drive failure.
*   **RAID 6 (Double Parity):** Tolerates 2 simultaneous drive failures.
*   **RAID 10 (1+0):** Striped mirrors; high performance and redundancy.

---

## 🔒 LUKS Disk Encryption (Data at Rest)

Linux Unified Key Setup (LUKS) is the standard for Linux disk encryption, managed via the `cryptsetup` command using the `dm-crypt` kernel module.

```bash
# Format the block device with LUKS encryption (will prompt for passphrase)
cryptsetup luksFormat /dev/sdb1

# Open the encrypted device, mapping it to a virtual block device named 'secure_disk'
cryptsetup luksOpen /dev/sdb1 secure_disk

# Format the mapped virtual device (now visible under /dev/mapper/secure_disk)
mkfs.xfs /dev/mapper/secure_disk

# Mount the decrypted volume
mount /dev/mapper/secure_disk /mnt/secured_data

# Close the volume, locking it and removing the mapping
umount /mnt/secured_data
cryptsetup luksClose secure_disk
```

---

## 🚀 I/O Tuning & Mount Options

### I/O Schedulers
Governs how read and write requests are queue-scheduled and sent to physical storage media:
*   **`noop` / `none` (FIFO):** Simple FIFO queue. Ideal for SSDs/NVMe drives and Virtual Machines where the underlying hypervisor handles disk scheduling.
*   **`deadline` / `mq-deadline`:** Prevents request starvation by enforcing a strict time expiration deadline on read/write operations. Highly suitable for database workloads.
*   **`cfq` (Completely Fair Queuing):** Distributes I/O bandwidth fairly among all processes.

### Mount Tuning Parameters
Mount flags in `/etc/fstab` heavily impact write performance and safety:
*   **`noatime`:** Prevents the kernel from writing access timestamps to files when read. This significantly cuts disk write operations.
*   **`nodiratime`:** Prevents access timestamps updates on directory nodes.
*   **`noexec`:** Prevents execution of binaries on the mounted filesystem (important security hardening tool for `/tmp` or shared storage).
*   **`nosuid`:** Ignores SUID/SGID execution bits.
*   **`nodev`:** Prevents character or block special devices creation/interpretation.
