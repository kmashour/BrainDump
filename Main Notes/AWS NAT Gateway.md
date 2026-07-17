---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[Amazon VPC]]"
against: []
reference_guides:
  - "[[Reference Notes/3-9_aws_vpc_networking.md]]"
tags:
  - aws/networking
  - status/completed
---

# AWS NAT Gateway

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Reference Notes/3-Index - AWS|AWS]] > [[Amazon VPC]] > **AWS NAT Gateway**

---

## 🎯 Purpose (Why it is used)
The **AWS NAT Gateway** is a fully managed Network Address Translation (NAT) service designed to provide private subnet resources (such as database or backend EC2 instances) with outbound-only internet connectivity. It allows resources to connect to external endpoints to download patches or consume external APIs while preventing the public internet from initiating inbound sessions to them.

---

## ⚙️ Functionality (What it is doing)
- **Outbound Traffic Translation:** Maps private IPv4 addresses from private subnets to a public Elastic IP (EIP) address.
- **Auto-Scaling Throughput:** Automatically scales bandwidth dynamically up to 45 Gbps without user intervention.
- **Managed Lifecycle:** AWS handles all system patching, OS administration, and physical hardware maintenance.
- **Stateless/Stateful Processing:** Automatically tracks translation tables to route returning traffic back to the originating instance.

---

## 🏛️ Architectural Context (How it fits in the architecture)
A NAT Gateway must be launched in a **public subnet** and requires an associated Elastic IP. The route tables of private subnets are updated to target the NAT Gateway ID (`nat-xxxxxx`) for all non-local outbound traffic (`0.0.0.0/0`). It acts as an intermediate router forwarding traffic to the Internet Gateway.

---

## 🧩 Problem Solver (What problem it solves)
Legacy configurations relied on custom EC2 **NAT Instances**, which acted as single points of failure, required manual failover scripts, and limited bandwidth to instance sizes. AWS NAT Gateway solves these problems by providing built-in high availability, native scaling, and eliminating the administrative overhead of patching and maintaining routing instances.

---

## 🟢 Operational Impact (What will happen with it operating)
Private subnets gain reliable, high-speed access to the internet. Because NAT Gateways do not support Security Groups, they cannot block traffic directly; security filtering must be managed at the EC2 instance Security Group level or subnet NACL level. Data processing charges ($0.045/GB) apply for all data traversing the NAT Gateway.

---

## 🔴 Failure Impact (What will happen without it)
If the NAT Gateway fails (or if the specific Availability Zone hosting it goes down), all private subnets dependent on its route table lose outbound internet connectivity. Database replicas cannot synchronize across regions, application APIs fail to contact external services, and automated software updates fail. 

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **AWS NAT Gateway**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[AWS NAT Gateway]]
SORT file.name ASC
```
