---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[aws - EBS and EFS Storage]]"
sub_type: core-concept
source_type: udemy
course_title: "AWS Certified Solutions Architect Associate"
tags:
  - aws/efs
  - aws/storage
  - aws/deep-dive
---

# aws - Amazon EFS

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - EBS and EFS Storage]] > **Amazon EFS**

---

## 📑 Amazon EFS (Elastic File System) Foundations

**Amazon Elastic File System (EFS)** is a serverless, fully managed network file system (NFS) designed to offer shared file access across hundreds or thousands of Linux-based EC2 instances concurrently.

### ⚙️ Architectural Characteristics
*   **Protocol:** Uses standard Network File System version 4 (**NFSv4**).
*   **Linux Only:** Compatible with Linux-based AMIs using the POSIX standard file system API. Not supported on Windows.
*   **VPC & Regional Scope:** Operates at the VPC level. Mount targets are placed in subnets across multiple Availability Zones, allowing instances across the entire region to mount the shared directory.
*   **Serverless Scaling:** Automatically scales capacity up or down as files are added or deleted. Pay-per-use model with no provisioned volume size required. Storage costs roughly **3x** the price of gp2 EBS volumes.
*   **Network Security:** Security group rules must allow NFS traffic on TCP port **2049** between instance security groups and EFS mount targets.

---

## 📈 Performance & Throughput Options

### 1. Performance Modes
*   **General Purpose (Default):** Low latency, optimized for latency-sensitive applications like web serving, Content Management Systems (WordPress), or data sharing.
*   **Max I/O:** Higher latency overhead but scales to high aggregate throughput and IOPS. Optimized for parallel workloads (e.g. big data processing, media transcoding).

### 2. Throughput Modes
*   **Elastic (Recommended):** Automatically scales read/write throughput up and down based on active workloads (reads up to 3 GB/s, writes up to 1 GB/s). Billed per gigabyte transferred.
*   **Bursting:** Throughput scales proportionally to the filesystem storage size.
*   **Provisioned:** Forces a baseline throughput regardless of storage size.

---

## 🔄 Storage Classes & Lifecycle Management

EFS implements lifecycle policies to move files to cheaper tiers based on access patterns:
*   **EFS Standard:** Replicated across multiple AZs. Optimized for frequently accessed files.
*   **EFS Infrequent Access (EFS-IA):** Moves files not accessed for a specified period (e.g. 30 days). Offers cheaper storage but charges a retrieval fee.
*   **EFS Archive:** Lowest cost storage class, optimized for files accessed only a few times a year.
*   **Transition Policy:** Transitions files to IA/Archive on inactivity, and returns them to Standard immediately upon first read/write.
*   **Availability Tenancy:**
    *   *Regional (Multi-AZ):* Standard production availability replicating data across multiple AZs.
    *   *One Zone (Single AZ):* Stores data in one AZ (up to **47% cheaper**). Good for dev/test but lacks disaster durability.

*Read more in [[Reference Notes/3-5_aws_ebs_efs_storage.md#5. amazon-efs-elastic-file-system]]*
