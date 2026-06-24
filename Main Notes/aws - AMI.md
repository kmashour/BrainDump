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
*   **Region Constraint:** AMIs are strictly **Region-scoped** resources. An AMI ID in `us-east-1` cannot be launched directly in `eu-west-1`. To launch in a different region, the AMI must be copied across regional boundaries.

### 🧩 Types of AMIs
1.  **AWS Quick Start AMIs:** Pre-built and hardened images provided by AWS (e.g., Amazon Linux 2, Windows Server 2022).
2.  **AWS Marketplace AMIs:** Pre-configured commercial software packages sold by third-party vendors (e.g., firewall virtual appliances, pre-bundled web stacks).
3.  **Custom/Private AMIs:** Images created by the customer from a stopped or running EC2 instance. Useful for fast auto-scaling since the application packages and dependencies are pre-installed ("golden image").
4.  **Community AMIs:** Free images shared publicly by other AWS users.

*Read more in [[Reference Notes/3-4_aws_ec2_compute.md#1. Amazon EC2 Compute Architecture & Foundations]]*
