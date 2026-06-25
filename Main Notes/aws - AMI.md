---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[aws - EC2 and Elastic Load Balancing]]"
sub_type: core-concept
source_type: udemy
course_title: "AWS Certified Solutions Architect Associate"
tags:
  - aws/compute
  - aws/deep-dive
---

# aws - AMI

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - EC2 and Elastic Load Balancing]] > **AMI**

---

## 📑 Amazon Machine Image (AMI) Architecture

An **AMI (Amazon Machine Image)** is a packaged template containing the pre-configured operating system, boot volume settings, and software stacks required to instantiate an EC2 instance.

### ⚙️ Key Attributes & Anatomy
*   **Root Volume Template:** Contains the root operating system configuration (e.g., Linux, Windows) and pre-installed application packages.
*   **Block Device Mapping:** Specifies which virtual drives (EBS volumes or Instance Store volumes) should attach to the instance upon launch.
*   **Launch Permissions:** Controls access to the image:
    *   *Public:* Shared with all AWS accounts.
    *   *Private:* Visible only to the owner account.
    *   *Explicit:* Shared with specific external AWS account IDs.
*   **Region Constraint:** AMIs are strictly **Region-scoped** resources. An AMI ID in `us-east-1` cannot be launched directly in `eu-west-1`.

### 🔄 Creation, Sharing, and Region Copying Mechanics
*   **AMI Creation:** Created from a running or stopped EC2 instance. AWS takes a snapshot of the root volume and other EBS volumes and registers it as a reusable template. *Best practice* is to stop the instance before creation to guarantee filesystem consistency and data integrity.
*   **AMI Sharing:** AMIs are shared by adding the target AWS Account IDs to the launch permissions.
    *   *Encryption Constraint:* If the AMI is backed by an encrypted EBS snapshot, you must also grant target accounts access to the KMS Customer Managed Key (CMK) used to encrypt the source snapshot.
*   **Region Copying:** To use an AMI in another region, it must be copied. The copy operation copies the underlying EBS snapshots to the target region and registers a new region-scoped AMI.

### 🧩 Types of AMIs
1.  **AWS Quick Start AMIs:** Pre-built and hardened images provided by AWS (e.g., Amazon Linux 2, Windows Server 2022).
2.  **AWS Marketplace AMIs:** Pre-configured commercial software packages sold by third-party vendors (e.g., firewall virtual appliances, pre-bundled web stacks).
3.  **Custom/Private AMIs:** Images created by the customer from a stopped or running EC2 instance. Useful for fast auto-scaling since the application packages and dependencies are pre-installed ("golden image").
4.  **Community AMIs:** Free images shared publicly by other AWS users.

*Read more in [[Reference Notes/3-4_aws_ec2_compute.md#7. Amazon Machine Image (AMI) Lifecycle]]*

