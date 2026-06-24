---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[aws - EBS and EFS Storage]]"
sub_type: core-concept
source_type: udemy
course_title: "AWS Certified Solutions Architect Associate"
tags:
  - aws/compute
  - aws/storage
  - aws/deep-dive
---

# aws - Instance Store

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - EBS and EFS Storage]] > **Instance Store**

---

## 📑 EC2 Instance Store Foundations

An **Instance Store** provides temporary block-level storage physically attached to the host hardware running the virtual EC2 instance. Unlike Amazon EBS volumes which communicate over the network SAN, Instance Store disks connect directly to the physical host bus (SATA, SAS, or PCIe/NVMe).

---

## ⚡ Performance Profile vs. EBS

Because it bypasses the virtual network interface and accesses the physical host bus directly, Instance Store delivers ultra-high I/O performance and low latency.
*   **Performance Metrics:** Capable of delivering **millions of IOPS** (e.g. 3.3 million read IOPS on `i3` instance types) and gigabytes of sequential throughput.
*   **EBS Comparison:** EBS maxes out at 16,000 IOPS (gp3) or 64,000/256,000 IOPS (io1/io2 Block Express).

---

## 🔄 Lifecycle & Ephemeral Constraints

Storage on an Instance Store is **volatile/ephemeral**, meaning data is lost in the following events:
1.  **Stop:** The instance is stopped (the underlying virtual machine moves to a different physical host).
2.  **Termination:** The instance is deleted.
3.  **Host Failure:** The underlying physical server hardware fails.

### 💾 Survival Attributes
*   **Reboot:** Data **survives** operating system reboots.
*   **Replication Strategy:** Because of its volatile nature, applications running on Instance Store must replicate data dynamically at the software level. For example, database clusters (Cassandra, MongoDB, Elasticsearch) replicate state across multiple EC2 instances to compensate for local host disk failures while taking advantage of local bus read/write speeds.

### 🎯 Primary Use Cases
*   Temporary cache directories and buffer pools.
*   Application scratch spaces.
*   Temporary web server assets.
*   Distributed transactional databases with application-level data replication.

*Read more in [[Reference Notes/3-5_aws_ebs_efs_storage.md#4. ec2-instance-store-ephemeral-block-storage]]*
