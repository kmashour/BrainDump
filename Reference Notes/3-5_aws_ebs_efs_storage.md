---
domains:
  - "aws"
class: reference-note
tier: reference-note
tags:
  - aws/storage
  - aws/ebs
  - aws/efs
  - aws/instance-store
---

# Module 3-5: AWS EBS & EFS Storage

This module details persistent block storage using **Amazon Elastic Block Store (EBS)**, local transient **Instance Store** drives, shared file systems using **Amazon Elastic File System (EFS)**, and RAID array configurations.

---

## 🗺️ Cognitive Map: Storage Topology & Lifecycle Comparison

```mermaid
graph TB
    subgraph RegionalScope ["Regional / VPC Scope (AWS Cloud)"]
        EFS["Amazon EFS (Shared NFSv4)"]
    end

    subgraph AZ_A ["Availability Zone A"]
        subgraph Host_Server_A ["Host Server (Physical Rack)"]
            EC2_A1["EC2 Instance A1"]
            EC2_A2["EC2 Instance A2"]
            InstStore_A["Instance Store (NVMe SSD - Local Bus)"]
        end
        EBS_zonal_A["EBS Volume A (gp3/io2 Block SAN)"]
    end

    subgraph AZ_B ["Availability Zone B"]
        EC2_B1["EC2 Instance B1"]
        EBS_zonal_B["EBS Volume B (Zonal SAN)"]
    end

    %% Network Mounts (EFS)
    EC2_A1 -->|POSIX NFSv4 Mount| EFS
    EC2_A2 -->|POSIX NFSv4 Mount| EFS
    EC2_B1 -->|POSIX NFSv4 Mount| EFS

    %% Block SAN Connections (EBS)
    EBS_zonal_A -.->|Attached via Network SAN| EC2_A1
    EBS_zonal_A -.->|Multi-Attach io1/io2 (max 16 instances)| EC2_A2

    %% Local Attached Disk (Instance Store)
    EC2_A1 ===|PCIe NVMe Physical Bus| InstStore_A

    %% Notes/Lifecycles
    style InstStore_A fill:#fbb,stroke:#333,stroke-width:2px;
    style EBS_zonal_A fill:#bbf,stroke:#333,stroke-width:2px;
    style EFS fill:#f9f,stroke:#333,stroke-width:2px;
```

### 📊 Quick Comparison Matrix

| Storage Option | Scope | Access Pattern | Durability & Lifecycle | Performance Profiles | Primary Use Cases |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Amazon EBS** | Zonal (Locked to AZ) | Single instance (Default); Multi-Attach (Optional for `io1`/`io2`) | Persists independently of EC2 instance termination. Highly durable, replicated in AZ. | gp2/gp3 (up to 16k IOPS), io1/io2 (up to 64k/256k IOPS). Sub-millisecond latency. | Boot volumes, transactional databases (RDS), general purpose VM disks. |
| **Instance Store** | Zonal (Host-local) | Single instance mounted to host server | Volatile/Ephemeral. Lost on Stop/Terminate or hardware failure. Survives OS reboots. | Ultra-high performance (millions of IOPS), raw host physical bus speed (NVMe). | Buffers, high-speed caches, scratch spaces, distributed DB replica members. |
| **Amazon EFS** | Regional (VPC) | Shared file access (thousands of Linux nodes concurrently) | Serverless, multi-AZ replication. Highly durable. Lifecycle rules move data to IA/Archive. | Dynamic scale, Elastic throughput up to 3 GB/s read, 1 GB/s write. POSIX compliant. | Web server content shares, CMS (WordPress), container log aggregation, big data ETL. |

---

## 1. Amazon EBS (Elastic Block Store)

Amazon EBS represents network-attached block storage designed for EC2 instances. Unlike local disks, EBS behaves like a Storage Area Network (SAN) drive connected over the network interface.

### ⚙️ Core Characteristics
*   **Network Bound:** Communicates with the EC2 instance via the network, resulting in minor latency overhead compared to physically attached drives.
*   **Zonal Scope:** An EBS volume is provisioned within a specific **Availability Zone (AZ)**. An EC2 instance in `eu-west-1a` cannot mount an EBS volume created in `eu-west-1b` directly. 
*   **Detaching and Migration:** Can be detached and attached to another instance in the same AZ dynamically (useful for active-passive failover). Migration across AZs or Regions requires taking a **Snapshot**, copying it, and creating a new volume in the target zone.
*   **Provisioned Capacity:** Size (GB) and performance characteristics (IOPS/Throughput) must be specified in advance. Size can be dynamically increased but never decreased.

### 🔄 Delete on Termination Attribute
*   This attribute controls what happens to the attached EBS volumes when their parent EC2 instance is terminated.
*   **Root Volume:** Enabled (`DeleteOnTermination = True`) by default. The root volume is destroyed alongside the instance.
*   **Non-Root Data Volumes:** Disabled (`DeleteOnTermination = False`) by default. Volumes persist after instance termination, keeping data intact.
*   **Customization:** Can be toggled at launch or runtime via CLI/Console to preserve root data or auto-clean data volumes.

---

## 2. EBS Volume Types

EBS volumes are split into Solid State Drives (SSD) for transaction-heavy database operations and Hard Disk Drives (HDD) for large throughput-oriented workloads.

### 🟢 Solid State Drives (SSD)

SSD volumes are optimized for small, random I/O operations and transactional database workloads. They can be used as boot/root volumes.

#### 1. General Purpose SSD (gp2 / gp3)
*   **Use Cases:** System boot volumes, virtual desktops, dev/test environments, small databases, and general-purpose workloads.
*   **gp3 (Newer Generation):** 
    *   Baseline performance of **3,000 IOPS** and **125 MB/s throughput** is included free with the volume.
    *   Allows provision of IOPS (up to 16,000) and throughput (up to 1,000 MB/s) **independently** from storage size.
*   **gp2 (Older Generation):** 
    *   Performance and size are linked: **3 IOPS per GB** provisioned.
    *   Small volumes can burst up to 3,000 IOPS using a burst credit balance.
    *   Maxes out performance at **16,000 IOPS** which requires provision of **5,334 GB** ($5334 \times 3 = 16,002$ IOPS).

#### 2. Provisioned IOPS SSD (io1 / io2 Block Express)
*   **Use Cases:** Large, latency-sensitive database workloads (MongoDB, Oracle, SQL Server) requiring sustained performance above 16,000 IOPS.
*   **io1:** 
    *   Max provisioned IOPS of **64,000** for EBS-Optimized instances (32,000 for standard instances).
    *   IOPS can be configured independently of storage size.
*   **io2 Block Express:** 
    *   Designed for sub-millisecond latency and high durability (99.999%).
    *   Supports volumes up to **64 TB**.
    *   Offers up to **256,000 IOPS** with an IOPS-to-GB ratio of **1,000:1**.
*   **EBS Multi-Attach:** Only `io1` and `io2` volumes support being attached to up to **16 instances** concurrently within the *same* AZ. Requires a cluster-aware file system (e.g., OCFS2, GFS2) to prevent write-collisions and data corruption.

---

### 🔵 Hard Disk Drives (HDD)

HDD volumes are optimized for large, sequential read/write operations. They **cannot** be used as root/boot volumes.

#### 1. Throughput Optimized HDD (st1)
*   **Use Cases:** Big Data analytics (Amazon EMR, Hadoop), MapReduce, Data Warehouses, ETL pipelines, and log processing servers.
*   **Performance:** High throughput (up to 500 MB/s) and a max IOPS of 500. Optimized for sequential data streaming at a low price point.

#### 2. Cold HDD (sc1)
*   **Use Cases:** Infrequently accessed archival data, backup storage, or massive filesystems where lowest storage cost is the primary metric.
*   **Performance:** Max throughput of 250 MB/s and a max IOPS of 250. Offers the lowest storage tier cost.

---

## 3. EBS Snapshots, Encryption, and Sharing

### 📸 EBS Snapshots Mechanics
*   **Incremental Backups:** Point-in-time backups of EBS volumes stored in Amazon S3. Only modified blocks are copied on subsequent snapshots to minimize storage charges.
*   **Consistency:** While a snapshot can be taken while the volume is actively mounted, it is highly recommended to detach the volume or freeze the filesystem first to ensure absolute data integrity.
*   **Regional Scope:** Snapshots reside at the Region level. They can be used to restore new EBS volumes to any Availability Zone within that region.

### ⚙️ Snapshot Lifecycle Features
1.  **Amazon Data Lifecycle Manager (DLM):** Automates the creation, retention, and deletion of EBS snapshots via resource tags.
2.  **Recycle Bin for EBS Snapshots:** Protects against accidental deletion. Deleted snapshots are moved to the Recycle Bin and can be restored within a retention window of **1 day to 1 year**.
3.  **Fast Snapshot Restore (FSR):** Forces full initialization of the restored EBS volume directly from S3, eliminating the baseline reading latency ("warming up") during the first read of each block. High operational cost.
4.  **Snapshot Archive:** Moves snapshots to a low-cost archive tier (up to **75% cheaper**). Restoring from archive is not immediate, taking **24 to 72 hours**.

### 🔒 EBS Encryption & Key Infrastructure
*   **Transparent Security:** Handled dynamically at the host level of the EC2 instance using **KMS (Key Management Service)** keys with **AES-256** encryption.
*   **Scope of Encryption:** Once enabled, data at rest inside the volume, data in-transit between instance and volume, snapshots, and volumes restored from those snapshots are encrypted transparently.
*   **Encryption Migration Workflow:** 
    *   There is no direct command to encrypt an existing unencrypted volume or change its KMS key.
    *   **Workaround:** Create a Snapshot of the unencrypted volume -> Copy the Snapshot while checking the "Enable Encryption" box and selecting a KMS Customer Managed Key (CMK) -> Restore the copied snapshot to a new EBS volume (which will be encrypted) -> Swap the volumes on the instance.
    *   **Shortcut:** A volume can be encrypted on-the-fly when creating it directly from an unencrypted snapshot in the console.

### 🤝 Sharing EBS Snapshots
*   **Unencrypted Snapshots:** Can be shared with individual AWS accounts or made public to the entire AWS community.
*   **Encrypted Snapshots:** Cannot be made public. They can only be shared with specific accounts.
*   **CMK Sharing Requirement:** The source account must grant permission on the Customer Managed Key (CMK) used to encrypt the snapshot to the target account. Snapshots encrypted with the default AWS Managed key (`aws/ebs`) **cannot** be shared across accounts.
*   **Cross-Region Sharing:** To share a snapshot with an account in a different region, the snapshot must first be copied to that target region.

---

## 4. EC2 Instance Store (Ephemeral Block Storage)

An **Instance Store** provides temporary block-level storage physically attached to the host hardware running the virtual EC2 instance.

### ⚙️ Mechanics & Performance
*   **Hardware Attached:** Bypasses the network interface, linking directly via the host's physical bus (SATA, SAS, or PCIe/NVMe).
*   **Ultra-High IOPS:** Capable of delivering **millions of IOPS** (e.g. 3.3 million read IOPS on `i3` instances) and massive throughput, whereas EBS has limits of 16k (gp3) or 64k/256k (io1/io2).

### 🔄 Lifecycle & Volatility Constraints
*   **Ephemeral Nature:** Storage is volatile. Data is lost if:
    *   The instance is **Stopped** (virtual machine is moved to another physical host).
    *   The instance is **Terminated**.
    *   The underlying host hardware fails.
*   **Persistence:** Data survives operating system **Reboots**.
*   **Replication Strategy:** Use cases must leverage software-level cluster replication (e.g. Cassandra, MongoDB, Elasticsearch clusters, OLTP DB replication) to replicate state dynamically across instances, compensating for the ephemeral storage model.

---

## 5. Amazon EFS (Elastic File System)

Amazon EFS is a serverless, fully managed network file system (NFS) offering shared file storage accessible by thousands of Linux EC2 instances concurrently.

### ⚙️ Core Architecture
*   **Protocol:** Uses standard Network File System version 4 (**NFSv4**).
*   **Compatibility:** Linux-based AMIs only (Not compatible with Windows Server).
*   **VPC & Multi-AZ Scope:** Mount targets are created inside target subnets across different Availability Zones within a VPC.
*   **Elastic Scaling:** Capacity scales automatically up to petabytes as files are added or deleted. Pay-per-use model (no provisioned size required). EFS storage costs roughly **3x** the price of gp2 EBS volumes.
*   **Security:** Governed by EFS security groups (port **2049** for NFS access must be open from instance security groups). Supports KMS data encryption at rest.

### 📈 Performance and Throughput Modes

#### 1. Performance Modes
*   **General Purpose (Default):** Optimized for latency-sensitive applications like web serving, content management (WordPress), and general file shares.
*   **Max I/O:** High latency overhead but scales to massive concurrent throughput and I/O. Ideal for parallelized workloads like big data processing or media transcoding.

#### 2. Throughput Modes
*   **Elastic (Recommended):** Automatically scales read/write throughput up and down based on the workload (reads up to 3 GB/s, writes up to 1 GB/s). Pay-per-use.
*   **Bursting:** Throughput scales proportionally to the size of the stored data filesystem.
*   **Provisioned:** Forces a baseline throughput regardless of the storage volume size. High cost, billed for the throughput itself.

### 🔄 Storage Classes and Lifecycle Management
EFS uses lifecycle policies to automatically transition files to cheaper storage tiers based on access patterns:
*   **EFS Standard (Frequent Access):** Optimized for active files.
*   **EFS Infrequent Access (EFS-IA):** Optimized for files not accessed in 7, 14, 30, 60, or 90 days. Offers cheaper storage but charges a retrieval fee per gigabyte.
*   **EFS Archive:** Optimized for rarely accessed files (few times a year). Lowest cost tier.
*   **Transition Policy:** Transition rules automatically move files to IA or Archive based on elapsed time, and transition them back to Standard immediately upon first access.
*   **Deployment Options:**
    *   **Regional (Multi-AZ):** Replicates data across multiple AZs. Recommended for production.
    *   **One Zone (Single AZ):** Stores data in one AZ. Up to **47% cheaper** than Regional. Ideal for development/testing but vulnerable to AZ failure.

---

## 6. RAID Configurations on EBS Volumes

If an application requires performance or redundancy beyond the capabilities of a single EBS volume, RAID can be configured within the guest OS:

*   **RAID 0 (Striping):** Combines volumes to increase read/write throughput and IOPS (sum of all volume capacities and performance). No redundancy; a single disk failure corrupts the entire array.
*   **RAID 1 (Mirroring):** Duplicates data on multiple volumes. Provides fault tolerance; slower write speeds.
*   **RAID 10 (Striped Mirroring):** Combines RAID 0 and RAID 1. High I/O performance and redundancy at double the storage cost.

> [!IMPORTANT]
> RAID configurations are performed at the Guest OS level (Software RAID) and are not recommended by AWS to be used as root/boot volumes.

---

## 7. Deep-Intuition (AARF) Breakdowns

### AARF Breakdown: EBS gp3 vs. io2 Volume Selection
1.  **The Answer (Core Pattern):** Utilize EBS gp3 for standard applications and database instances. Transition to io2 Block Express only when baseline storage performance requires sustained IOPS above 16,000 or absolute sub-millisecond write performance.
2.  **The Assumptions (Context):** The instance type must support EBS Optimization to utilize the dedicated network bandwidth to the storage system without saturating VM network interfaces.
3.  **The Rationale (Why):** gp3 provides independent performance configuration (3,000 IOPS and 125 MB/s baseline included free) which is highly cost-efficient. io2 offers 99.999% durability and consistent provisioned performance but at a steep pricing tier, which is wasted if the database is throttled by CPU or memory limits rather than storage bottlenecks.
4.  **The Failure Loop (What if not):** Provisioning high IOPS on gp2 volumes relies on a "burst credit balance" model. When credits are exhausted during peak database writes, the volume throttles to a baseline of 100 IOPS, database connections saturate, query latency spikes to seconds, and the app server connection pools fail.
5.  **Alternative Case (When to use 'if not'):** For distributed, scratch-pad filesystems or cache clusters requiring maximum read/write performance without persistence, deploy Instance Store NVMe disks.
