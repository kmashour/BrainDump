---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[aws - EBS and EFS Storage]]"
sub_type: core-concept
source_type: udemy
course_title: "AWS Certified Solutions Architect Associate"
tags:
  - aws/ebs
  - aws/storage
  - aws/deep-dive
---

# aws - Amazon EBS

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - EBS and EFS Storage]] > **Amazon EBS**

---

## 📑 Amazon EBS (Elastic Block Store) Foundations

**Amazon Elastic Block Store (EBS)** provides network-attached block-level storage volumes for use with EC2 instances. It acts as a Storage Area Network (SAN) drive, communicating with instances via the AWS network interface, which introduces a minor latency compared to physically attached local disks.

### ⚙️ Operational Mechanics
*   **Zonal Scope:** EBS volumes are bound to a single Availability Zone (AZ). To mount a volume to an instance, both must reside in the same AZ (e.g. `eu-west-1b`).
*   **Elastic Resizing:** Volumes can be resized dynamically (both capacity in GB and performance parameters like IOPS/throughput) without downtime. However, size can only be increased, not decreased.
*   **Delete on Termination:** Controls the lifecycle of the EBS volume when its EC2 instance is terminated.
    *   *Root Volumes:* Billed and deleted by default (`DeleteOnTermination = True`).
    *   *Data Volumes:* Kept intact by default (`DeleteOnTermination = False`), allowing the volume to be attached to a new instance later.

---

## 📊 EBS Volume Types & Performance Sizing

EBS volumes are categorized by SSD (Solid State Drives) optimized for random transactional IOPS and HDD (Hard Disk Drives) optimized for high-throughput sequential data streaming.

### 1. General Purpose SSD (gp2 / gp3)
*   **gp3 (Newer Generation):** 
    *   Baseline performance of **3,000 IOPS** and **125 MB/s throughput** is included free with the volume.
    *   Allows configuration of IOPS (up to 16,000) and throughput (up to 1,000 MB/s) **independently** from storage size.
*   **gp2 (Older Generation):** 
    *   Performance and size are linked: **3 IOPS per GB** provisioned.
    *   Small volumes can burst up to 3,000 IOPS using burst credits.
    *   Maxes out at **16,000 IOPS** which requires a volume size of **5,334 GB**.

### 2. Provisioned IOPS SSD (io1 / io2 Block Express)
*   *Use Cases:* High-performance databases (MongoDB, Oracle, SQL Server) requiring sustained performance above 16,000 IOPS.
*   **io1:** Max provisioned IOPS of **64,000** for EBS-Optimized instances (32,000 for standard instances).
*   **io2 Block Express:** High durability (99.999%), sub-millisecond latency, and support for up to **256,000 IOPS** with an IOPS-to-GB ratio of **1,000:1**.
*   **EBS Multi-Attach:** Only `io1` and `io2` volumes support attachment to up to **16 instances** concurrently within the *same* AZ. Requires a cluster-aware file system (e.g., OCFS2, GFS2) to prevent write-collisions and data corruption.

### 3. Throughput-Optimized HDD (st1) & Cold HDD (sc1)
*   *Restrictions:* Cannot be used as root/boot volumes.
*   **st1:** Optimized for large, sequential workloads (Hadoop, EMR, Big Data, log processing) with up to 500 MB/s throughput. Billed for throughput.
*   **sc1:** Lowest storage tier cost, optimized for large volume cold/archival data that is infrequently accessed.

*Read more in [[Reference Notes/3-5_aws_ebs_efs_storage.md#1. amazon-ebs-elastic-block-store]] and [[Reference Notes/3-5_aws_ebs_efs_storage.md#2. ebs-volume-types]]*
