---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[aws]]"
sub_type: core-concept
source_type: documentation
source_url: "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html"
author: "AWS Documentation"
course_title: "AWS Elastic Block Store & EFS Storage Guides"
tags:
  - aws/ebs
  - aws/efs
  - aws/storage
  - aws/deep-dive
---

# aws - EBS and EFS Storage

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[aws]] > **EBS and EFS Storage**

---

## 📑 Block Storage: EBS vs. Instance Store

*   **Amazon Elastic Block Store (EBS):** Zonal, durable network-attached block storage. EBS volumes persist independently of the EC2 instance lifecycle. Replicated in a single AZ. Supports snapshots (sent to S3), dynamic volume expansion, and Multi-Attach (for `io1`/`io2` volumes).
*   **EC2 Instance Store:** Zonal, volatile, physically attached NVMe/SSD host drives. Provides extremely high performance (millions of IOPS) and low latency. However, data is lost if the instance stops, terminates, or host hardware fails. Ideal for temporary scratch space, cache layers, or distributed database clusters with internal replication.

---

## 📑 File Storage: Elastic File System (EFS)

*   **Amazon EFS:** Managed, serverless network file system offering shared access using the NFSv4 protocol.
*   **VPC and Multi-AZ Scope:** Unlike zonal EBS, EFS operates at a VPC level. Mount targets are created in multiple subnets across different AZs, allowing thousands of EC2 instances to read/write concurrently to the same shared directory.
*   **Scaling:** Automatically scales storage capacity up or down as files are added or deleted, with pay-as-you-go billing.

---

## 📑 EBS Encryption & Snapshot Restores

*   **In-Transit and At-Rest Encryption:** EBS volumes support KMS-backed symmetric encryption. Data is encrypted on the host running the EC2 instance, securing both data-at-rest on the volume and data-in-transit between the instance and the EBS SAN.
*   **Snapshots:** Point-in-time incremental backups stored in S3. Restoring an EBS volume from a snapshot requires creating a new volume of equal or greater size in the same availability zone.

*Read more in [3-5_aws_ebs_efs_storage.md](../Reference%20Notes/3-5_aws_ebs_efs_storage.md#1-amazon-ebs--storage-options)*
