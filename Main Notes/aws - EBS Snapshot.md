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

# aws - EBS Snapshot

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - EBS and EFS Storage]] > **EBS Snapshot**

---

## 📑 EBS Snapshot Mechanics

An **EBS Snapshot** is a point-in-time incremental backup of an EBS volume, stored natively in Amazon S3. 

### ⚙️ Operational Principles
*   **Incremental Backups:** Only changed blocks since the last snapshot are backed up to minimize S3 storage costs.
*   **Consistency:** Although snapshots can be taken while the volume is actively mounted, detaching the volume or pausing I/O is recommended to ensure filesystem consistency.
*   **Regional Scope:** Snapshots reside at the AWS Region level and can be restored as new EBS volumes in any Availability Zone within that region.

---

## ⚙️ Snapshot Lifecycle & Archiving Features

1.  **Amazon Data Lifecycle Manager (DLM):** Automates snapshot creation, retention, and deletion using resource tags.
2.  **Recycle Bin:** Protects against accidental deletion. Bins retain deleted snapshots for **1 day to 1 year**, allowing restoration.
3.  **Fast Snapshot Restore (FSR):** Eliminates block-initialization latency during the first read from a restored volume. It pre-warms the restored volume from S3 immediately upon creation (highly expensive).
4.  **Snapshot Archive:** Moves snapshots to a cold archive storage tier that is up to **75% cheaper**. Restores from this tier are not immediate and require **24 to 72 hours**.

---

## 🔒 EBS Encryption & Cross-Account Sharing

### 🔑 Encryption Workarounds
EBS volumes utilize KMS AES-256 key encryption transparently at the EC2 host level. If a volume is unencrypted:
*   You cannot directly encrypt an existing volume.
*   **Workaround:** Create a Snapshot of the unencrypted volume -> Copy the Snapshot with encryption enabled using a KMS Customer Managed Key (CMK) -> Restore the copied snapshot to a new EBS volume (which will be encrypted).
*   **Console Shortcut:** You can choose to encrypt a volume directly during restore from an unencrypted snapshot without copying it first.

### 🤝 Sharing Permissions
*   **Unencrypted Snapshots:** Can be shared publicly with the entire AWS community or privately with select AWS accounts.
*   **Encrypted Snapshots:** Can only be shared with specific accounts. They cannot be made public.
*   **KMS CMK Requirement:** The recipient account must be granted permissions on the KMS Customer Managed Key used to encrypt the snapshot. Snapshots encrypted using the default AWS Managed key (`aws/ebs`) **cannot** be shared across accounts.
*   **Cross-Region Transfer:** Sharing across different Regions requires copying the snapshot to the target region first.

*Read more in [[Reference Notes/3-5_aws_ebs_efs_storage.md#3. EBS Snapshots, Encryption, and Sharing]]*

