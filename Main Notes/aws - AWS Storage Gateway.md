---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[aws - EBS and EFS Storage]]"
sub_type: core-concept
source_type: udemy
course_title: "AWS Certified Solutions Architect Associate"
tags:
  - aws/storage-gateway
  - aws/storage
  - aws/deep-dive
---

# aws - AWS Storage Gateway

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - EBS and EFS Storage]] > **AWS Storage Gateway**

---

## 📑 AWS Storage Gateway Foundations

**AWS Storage Gateway** is a managed hybrid storage service that connects on-premises application servers directly to AWS cloud storage. It provides low-latency access to data by caching frequently accessed files locally, while backup, archival, and primary datasets scale securely in AWS.

---

## ⚙️ Gateway Deployment & Hosting
*   **On-Premises Deployment:** Runs as a Virtual Machine (VM) on local hypervisors (VMware ESXi, Microsoft Hyper-V, Linux KVM).
*   **Cloud Deployment:** Can also run on an Amazon EC2 instance if cloud-native staging/gateway architecture is required.

---

## 🔄 Gateway Modes & Architectures

### 1. Amazon S3 File Gateway
*   **Access Protocol:** Exposes S3 buckets via Network File System (**NFS** v3/v4.1) or Server Message Block (**SMB**).
*   **Operational Mechanics:** App servers write files locally. The gateway translates files to S3 object API calls over HTTPS dynamically.
*   **Local Caching:** Holds a local disk cache of the most recently used files for sub-millisecond retrieval.
*   **Glacier Transition:** Cannot write directly to Glacier. Transition to Glacier requires configuring S3 Lifecycle Policies on the target S3 bucket.
*   **AD Integration:** Natively supports Active Directory for user authorization when using the SMB protocol.

### 2. Amazon FSx File Gateway
*   **Access Protocol:** Server Message Block (**SMB**).
*   **Operational Mechanics:** Natively exposes Windows File Server shares (from FSx for Windows File Server) to on-premises clients with a local cache for low-latency SMB access.

### 3. Volume Gateway
*   **Access Protocol:** Exposes block volumes over **iSCSI** targeting local application servers. Backed by S3 and managed via EBS snapshots.
*   **Cached Volumes:** Stores primary data in S3; frequently accessed data is cached locally on the VM. Cost-effective for expanding local storage.
*   **Stored Volumes:** Stores the entire dataset locally on-premises. Backs up snapshots asynchronously to S3 on a schedule, providing low-latency local access with cloud disaster recovery.
*   **Evolutionary Bridge:** Translates legacy physical SAN SCSI commands routed over TCP/IP (iSCSI protocol) to REST API payloads against S3 object store.

### 4. Tape Gateway
*   **Access Protocol:** Virtual Tape Library (VTL) interface exposed over **iSCSI** to backup servers (e.g., NetBackup, Veeam).
*   **Evolutionary Bridge:** Replaces legacy physical tape backup storage libraries (LTO cartridges) and media rotation systems with virtual cloud cartridges in S3 and S3 Glacier, eliminating offsite storage logistics.

*Read more in [[Reference Notes/3-5_aws_storage_extras.md#1-aws-storage-gateway|Module 3-5: AWS Storage Gateway]]*
