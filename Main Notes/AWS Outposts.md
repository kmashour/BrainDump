---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[aws]]"
  - "[[aws - EC2 Instance]]"
  - "[[Amazon S3]]"
against:
  - "[[aws]]"
reference_guides:
  - "[[Reference Notes/3-20_other_services_whitepapers.md]]"
tags:
  - aws/outposts
  - infra/hybrid
  - status/completed
---

# AWS Outposts

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **AWS Outposts**

---

## 🎯 Purpose (Why it is used)
AWS Outposts is a managed hybrid cloud service that delivers AWS hardware racks directly to a customer's on-premises data center. It provides the same AWS APIs, tools, and services on-premises as in the public cloud, enabling applications with low-latency or local data residency requirements.

---

## ⚙️ Functionality (What it is doing)
*   **On-Premises Hardware Hosting:** Installs physical, AWS-configured server racks inside customer data centers.
*   **AWS Service Extension:** Runs standard AWS services (EC2, EBS, S3, ECS, EKS, RDS, EMR) locally on the Outposts hardware.
*   **Managed Operations:** Monitors, updates, patches, and maintains the Outposts hardware server rack automatically from the cloud.
*   **Local Processing:** Routes traffic directly to local network gateways, allowing data processing without cloud round-trips.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Outposts connects to the nearest AWS Region over Direct Connect or VPN. In the console, the Outposts rack is defined as a subnet in a VPC, enabling unified cloud management of local hardware.

---

## 🧩 Problem Solver (What problem it solves)
Running workloads on-premises while managing cloud workloads requires maintaining separate APIs, tools, and platforms. Outposts solves this by bringing standard AWS infrastructure and APIs directly to the local data center.

---

## 🟢 Operational Impact (What will happen with it operating)
Workloads benefit from sub-millisecond latency to local systems, and data stays on-premises. Note: **The customer is responsible for the physical security and power of the server rack**.

---

## 🔴 Failure Impact (What will happen without it)
Without Outposts, hybrid applications must run on legacy on-premises virtualization platforms (VMware, OpenStack) while public cloud components use AWS APIs, forcing teams to maintain separate engineering skillsets.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **AWS Outposts**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
