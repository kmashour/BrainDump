---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: network
domains:
  - "aws"
related_concepts:
  - "[[AWS NAT Gateway]]"
  - "[[Network Access Control List]]"
  - "[[VPC Peering]]"
  - "[[VPC Endpoint]]"
  - "[[Transit Gateway]]"
against: []
reference_guides:
  - "[[Reference Notes/3-9_aws_vpc_networking.md]]"
tags:
  - aws/networking
  - status/completed
---

# Amazon VPC

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[Reference Notes/3-Index - AWS|AWS]] > **Amazon VPC**

---

## 🎯 Purpose (Why it is used)
Amazon **Virtual Private Cloud (VPC)** is a fundamental networking service that provisions a logically isolated virtual network within an AWS region. It acts as the backbone infrastructure for running AWS compute, database, and load-balancing services, granting the customer complete control over their cloud network environment.

---

## ⚙️ Functionality (What it is doing)
- **IP Address Allocation:** Allows configuration of primary and secondary IPv4/IPv6 CIDR ranges (blocks between `/16` and `/28`).
- **Subnetting:** Segregates the VPC CIDR block into isolated, Availability Zone-confined subnets (public or private).
- **Implied Routing:** Provides an implicit, fully managed VPC router that automatically routes traffic between all internal subnets.
- **VPC Edge Gateways:** Supports attachment of Internet Gateways (IGW), Egress-Only IGWs, and Virtual Private Gateways (VGW) for outside connectivity.
- **Firewall Filtering:** Leverages Security Groups (stateful, instance-level) and Network Access Control Lists (stateless, subnet-level) to secure traffic flows.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Amazon VPC is region-specific and forms the foundational network boundary for resources like EC2, RDS, and ECS. By default, resources inside a VPC can communicate internally with each other using private IP addresses. External connections require explicit routing targets (e.g., routing internet-bound traffic through an attached Internet Gateway or NAT Gateway).

---

## 🧩 Problem Solver (What problem it solves)
Without a VPC, cloud resources would run on a shared, flat public network, exposing them to direct internet security threats and preventing custom IP address design. Amazon VPC solves the problem of network isolation, security control, and hybrid connectivity (allowing users to extend their on-premises data centers to the AWS cloud).

---

## 🟢 Operational Impact (What will happen with it operating)
Workloads communicate securely within low-latency internal pathways. Traffic flows can be inspected via VPC Flow Logs and Traffic Mirroring. Custom routing rules can redirect traffic to proxies, security appliances, or dedicated cloud connections like Direct Connect.

---

## 🔴 Failure Impact (What will happen without it)
If the VPC fails or is misconfigured (e.g., deleted routes, missing Internet Gateways, or misaligned subnets), all resources inside the VPC become isolated, and external users cannot access the applications. System integrations (database synchronization, API calls, and administrative access via Bastion hosts) will fail completely.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Amazon VPC**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[Amazon VPC]]
SORT file.name ASC
```
