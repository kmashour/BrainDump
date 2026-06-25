---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: network
domains:
  - "aws"
related_concepts:
  - "[[Amazon VPC]]"
  - "[[VPC Peering]]"
against:
  - "[[VPC Peering]]"
reference_guides:
  - "[[Reference Notes/3-9_aws_vpc_networking.md]]"
tags:
  - aws/networking
  - status/completed
---

# Transit Gateway

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[Reference Notes/3-Index - AWS|AWS]] > [[Amazon VPC]] > **Transit Gateway**

---

## 🎯 Purpose (Why it is used)
AWS **Transit Gateway (TGW)** is a fully managed cloud router that connects multiple VPCs, on-premises networks (via VPN), and Direct Connect connections in a central **hub-and-spoke** topology. It is used to simplify routing architectures, establish transitive routing, and centralize network management for large scale cloud environments.

---

## ⚙️ Functionality (What it is doing)
- **Centralized Transit Routing:** Directs network packets transitively between any attached VPC, VPN, or Direct Connect connection in a star topology.
- **TGW Route Tables:** Provides dynamic or static routing tables that can be edited to segment or route traffic between specific attachments.
- **Cross-Region Peering:** Interconnects Transit Gateways in different AWS Regions to establish global private networks.
- **Multicast Support:** Supports IP multicast traffic (the only AWS service to natively support multicast).
- **Equal-Cost Multi-Path (ECMP):** Supports ECMP to scale VPN bandwidth beyond the default 1.25 Gbps per tunnel by dynamically load-balancing traffic across multiple active tunnels (up to 2.5 Gbps or more).
- **Cross-Account Sharing:** Integrated with AWS Resource Access Manager (RAM) to share Transit Gateways across multiple AWS accounts in an organization.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Transit Gateway is a regional resource that interfaces with VPC subnets through Transit Gateway Elastic Network Interfaces. VPC route tables are updated to direct traffic for other VPCs or on-premises networks to the Transit Gateway ID (`tgw-xxxxxx`). TGW route tables are then evaluated to determine the final destination attachment.

---

## 🧩 Problem Solver (What problem it solves)
As organizations grow, the number of VPCs increases, leading to a complex web of VPC Peering connections (non-transitive mesh) and duplicate VPN/Direct Connect connections to each VPC. Transit Gateway solves this "spaghetti routing" problem by providing a central hub, enabling transitive routing, and scaling to thousands of attachments.

---

## 🟢 Operational Impact (What will happen with it operating)
Routing logic is simplified and centralized in TGW route tables. New VPCs can be quickly integrated into the network by attaching them to the TGW without updating peers. Organization-wide network policies (such as routing all internet traffic through a central inspection VPC) can be easily enforced. Data transfer fees apply per GB processed.

---

## 🔴 Failure Impact (What will happen without it)
If the Transit Gateway is deleted or suffers an outage, all inter-VPC and hybrid communications traversing the hub are terminated. VPCs become isolated from each other and from the corporate data center, while internet-bound traffic utilizing a centralized firewall VPC fails.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Transit Gateway**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[Transit Gateway]]
SORT file.name ASC
```
