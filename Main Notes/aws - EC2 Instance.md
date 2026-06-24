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

### ⚙️ Core Parameters
*   **Operating System (OS):** Loaded from an AMI (Amazon Linux, Windows Server, macOS, Ubuntu, RedHat).
*   **Compute (vCPUs) & RAM:** Tailored based on hardware generation and instance sizing class (e.g., General Purpose, Compute Optimized, Memory Optimized, Storage Optimized).
*   **Networking:** Bound to an Elastic Network Interface (ENI) with private and optionally public or Elastic IPs.
*   **Firewall:** Governed by stateful Security Groups.
*   **Bootstrapping:** User Data script executed with `root` privileges once during initial start.

### 🔄 Lifecycle States & Billing Impact
*   **Pending:** Launch preparation by host hypervisor (No compute charge).
*   **Running:** Active CPU/RAM execution (Compute charges apply).
*   **Stopping/Stopped:** Virtual machine is shut down (No compute charge, but attached EBS volumes and EIPs incur charges).
*   **Terminated:** Permanently deleted; resources are reclaimed.
*   **Rebooting:** Restarting OS without losing hardware association (Compute charges apply).
*   **Stop-Hibernate:** Freeze state. Active RAM is dumped into an encrypted root EBS volume. On restart, the RAM state is loaded back, keeping processes and application caches warm (No compute charge; only EBS and associated EIPs are billed).

### 💰 Purchasing & Capacity Models
*   **On-Demand:** Pay by the second/hour. High flexibility, no commitment. Good for short-term, unpredictable workloads.
*   **Reserved Instances (RIs):** Commit to 1-year or 3-year term. Up to 72% discount. Standard (strict attributes) vs. Convertible (can exchange for different instance class/OS).
*   **Savings Plans:** Dollar spend commitment per hour (e.g., $10/hr) for 1 or 3 years. Up to 72% savings. Flexible across sizes, OS, tenancy, and region.
*   **Spot Instances:** Up to 90% discount by bidding on spare capacity. Subject to reclamation by AWS with a 2-minute warning.
*   **Dedicated Infrastructure:** Dedicated Hosts (physical server dedicated to client, good for compliance and BYOL) vs. Dedicated Instances (hardware dedicated to account but shared internally, no control over hardware placement).
*   **Capacity Reservations:** Reserves on-demand instance capacity in a specific AZ for any duration.

*Read more in [[Reference Notes/3-4_aws_ec2_compute.md#1. Amazon EC2 Compute Architecture & Foundations]]*
