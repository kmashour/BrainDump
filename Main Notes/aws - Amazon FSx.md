---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[aws - EBS and EFS Storage]]"
sub_type: core-concept
source_type: udemy
course_title: "AWS Certified Solutions Architect Associate"
tags:
  - aws/fsx
  - aws/storage
  - aws/deep-dive
---

# aws - Amazon FSx

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - EBS and EFS Storage]] > **Amazon FSx**

---

## 📑 Amazon FSx Foundations

**Amazon FSx** provides fully managed, high-performance file systems powered by third-party enterprise and open-source storage architectures (Windows File Server, NetApp ONTAP, Lustre, OpenZFS). It is analogous to RDS but for file systems, handling deployment, patch management, scaling, and backups transparently.

---

## 📊 FSx File System Types & Protocols

### 1. FSx for Windows File Server
*   **Protocols:** Server Message Block (**SMB** v2.0 - v3.1.1) and Windows **NTFS**.
*   **Access Rules:** Built-in integration with **Microsoft Active Directory** (AWS Directory Service or on-premises AD). Supports NTFS Access Control Lists (ACLs) and user quotas.
*   **DFS Namespaces:** Supports Distributed File System (DFS) Namespaces to group multiple file servers into a single logical folder structure.
*   **OS Compatibility:** Natively integrated with Windows, but **can also be mounted on Linux EC2 instances** supporting SMB client utilities.
*   **Storage Profiles:** SSD (low-latency, database/analytics workloads) or HDD (home directories, CMS content).
*   **Deployment Scope:** Replicated Multi-AZ or Single-AZ. Automatically performs daily S3-backed backups.

### 2. FSx for Lustre
*   **Protocols:** POSIX-compliant Lustre high-performance client.
*   **Use Cases:** Machine Learning (ML), High-Performance Computing (HPC), video transcoding, and financial modeling.
*   **S3 Integration:** Bidirectional syncing with Amazon S3. Can read S3 datasets as active file systems (lazy-loading file data on-demand), perform local parallel cluster executions, and write computed outputs back to S3.
*   **Deployment Options:**
    *   *Scratch File System:* Temporary storage with no data replication (single copy of data). Delivers 6x burst performance at a lower cost. Server failure results in data loss.
    *   *Persistent File System:* Long-term processing. Replicates data within a single Availability Zone (not cross-AZ). Automatically replaces failed underlying hardware in minutes (maintaining 2 copies of data).

### 3. FSx for NetApp ONTAP
*   **Protocols:** Multi-protocol support across **NFS**, **SMB**, and **iSCSI** block storage.
*   **OS Compatibility:** Wide support for Linux, Windows, macOS, VMware Cloud on AWS, WorkSpaces, AppStream, EC2, ECS, and EKS.
*   **Key Features:** Automated storage auto-scaling, data snapshots, inline data compression/deduplication/compaction, and point-in-time instantaneous filesystem cloning.
*   **Evolutionary Bridge:** Transitions legacy on-premises SAN/NAS hardware running NetApp's **WAFL (Write Anywhere File Layout)** filesystem directly to AWS managed cloud storage blocks without manual clustering or hardware configuration.

### 4. FSx for OpenZFS
*   **Protocols:** Compatible with **NFS** (v3, v4, v4.1, v4.2).
*   **Performance:** Scalable up to 1 million IOPS with latency under 0.5 ms.
*   **Features:** Managed OpenZFS engine. Supports zpools, dataset management, snapshots, compression, and point-in-time cloning. **Does not support data deduplication** (unlike ONTAP).
*   **Use Cases:** Lifting and shifting legacy ZFS file systems to AWS.

*Read more in [[Reference Notes/3-5_aws_storage_extras.md#3-amazon-fsx-family|Module 3-5: Amazon FSx]]*
