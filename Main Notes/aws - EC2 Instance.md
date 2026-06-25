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

# aws - EC2 Instance

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - EC2 and Elastic Load Balancing]] > **EC2 Instance**

---

## 📑 EC2 Instance Foundations & Operations

An **EC2 Instance** is a resizable virtual machine running inside AWS's infrastructure, representing the core compute block of Infrastructure as a Service (IaaS) on AWS.

### ⚙️ Core Parameters & Sizing
*   **Operating System (OS):** Loaded from an AMI (Amazon Linux, Windows Server, macOS, Ubuntu, RedHat).
*   **Compute (vCPUs) & RAM:** Sized based on optimization classes (e.g., General Purpose `T/M`, Compute Optimized `C`, Memory Optimized `R/X`, Storage Optimized `I/D/H`).
*   **Networking (ENI):** Bound to an Elastic Network Interface (ENI) with private and optionally public or Elastic IPs. Bound to a specific AZ.
*   **Firewall:** Governed by stateful Security Groups.
*   **Bootstrapping:** User Data script executed with `root` privileges once during initial start (16 KB size limit).

### 🔄 Lifecycle States & Billing Impact
*   **Pending:** Launch preparation by host hypervisor (No compute charge).
*   **Running:** Active CPU/RAM execution (Compute charges apply). Billed per second (Linux/Windows/macOS after first minute) or per hour.
*   **Stopping/Stopped:** Virtual machine is shut down (No compute charge, but attached EBS volumes and EIPs incur charges).
*   **Terminated:** Permanently deleted; resources are reclaimed. By default, primary ENI and root EBS volume marked with "Delete on Termination" are destroyed.
*   **Rebooting:** Restarting OS without losing hardware association (Compute charges apply).
*   **Stop-Hibernate (EC2 Hibernation):** Freeze state. Active RAM is dumped into a file on the root EBS volume.
    *   *Prerequisites:* Root volume must be an encrypted EBS volume. Root volume must be large enough to contain the RAM dump. RAM size limit < 150 GB. Available for On-Demand, Reserved, and Spot instances. Maximum duration is 60 days. Not supported on bare-metal instances.

### 💰 Purchasing & Capacity Models
*   **On-Demand:** Pay by the second/hour. High flexibility, no commitment. Billed per second (Linux/Windows/macOS) or hour. Good for short-term, unpredictable workloads that cannot handle interruptions.
*   **Reserved Instances (RIs):** Commit to 1-year or 3-year term. Billed in All Upfront, Partial Upfront, or No Upfront.
    *   *Standard RIs:* Up to 72% discount. Standard attributes (can modify AZ, size within family, scope, can sell on RI marketplace).
    *   *Convertible RIs:* Up to 54% discount. Can exchange for different instance class, family, OS, tenancy, or scope.
    *   *Scheduled RIs:* Reserve capacity for recurring scheduled blocks of time (daily, weekly, monthly) for 1-year commitment. Billed only for scheduled duration.
*   **Savings Plans:** Dollar spend commitment per hour (e.g., $10/hr) for 1 or 3 years. Billed at discount rate up to committed amount, standard rate for excess.
    *   *EC2 Instance Savings Plans:* Up to 72% discount. Binds to a specific instance family in a region. Flexible across sizes, OS, tenancy.
    *   *Compute Savings Plans:* Up to 66% discount. Most flexible; applies to EC2 (any family, size, OS, tenancy, region), AWS Fargate, and AWS Lambda.
*   **Spot Instances:** Up to 90% discount by bidding on spare capacity. Subject to reclamation by AWS with a 2-minute warning.
    *   *Spot Block:* Previously allowed reserving Spot Instances for a fixed duration of 1 to 6 hours. AWS has **deprecated and withdrawn** Spot Blocks since 2021.
    *   *Spot Requests:* One-Time requests (expire when fulfilled) vs. Persistent requests (re-launch instances if terminated).
    *   *Spot Cancel Workflow:* To permanently delete a persistent spot setup, you **must cancel the Spot Request first**, and then terminate the running instances. Terminating the instances first will prompt the persistent request to launch a replacement instance.
*   **Spot Fleet:** A fleet of spot (and optionally on-demand) instances. Uses allocation strategies: `lowestPrice` (cheapest pool), `diversified` (distributed across pools), `capacityOptimized` (lowest termination rates), `priceCapacityOptimized` (recommended default).
*   **Dedicated Infrastructure:**
    *   *Dedicated Hosts:* Physical server dedicated to a single customer. Billed per physical host. Good for regulatory compliance and BYOL socket/core-bound licensing. Provides full control over instance placement.
    *   *Dedicated Instances:* Virtual hardware dedicated to you, but shared internally with other instances of the same AWS account. No control over physical placement on the hardware.
*   **Capacity Reservations:** Reserves on-demand instance capacity in a specific AZ for any duration. Billed at On-Demand rates regardless of whether the instance is running or idle.

*Read more in [[Reference Notes/3-4_aws_ec2_compute.md#4. EC2 Purchasing & Launch Models]]*

