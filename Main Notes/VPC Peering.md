---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: network
domains:
  - "aws"
related_concepts:
  - "[[Amazon VPC]]"
  - "[[Transit Gateway]]"
against:
  - "[[Transit Gateway]]"
reference_guides:
  - "[[Reference Notes/3-9_aws_vpc_networking.md]]"
tags:
  - aws/networking
  - status/completed
---

# VPC Peering

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Reference Notes/3-Index - AWS|AWS]] > [[Amazon VPC]] > **VPC Peering**

---

## 🎯 Purpose (Why it is used)
A **VPC Peering** connection is a networking connection between two VPCs that enables them to route traffic directly using private IP addresses. It allows resources in either VPC to communicate as if they were on the same network, utilizing AWS's high-speed, secure private backbone infrastructure.

---

## ⚙️ Functionality (What it is doing)
- **Private Backbone Routing:** Interconnects two VPCs directly without routing traffic over the public internet.
- **Cross-Account & Cross-Region Support:** Peering can cross AWS accounts and geographic regions.
- **Security Group Referencing:** Allows security groups to reference security groups in the peered VPC (same region only).
- **VPC Endpoint Alternative:** Provides high-throughput, private channels between workloads in different VPCs.

---

## 🏛️ Architectural Context (How it fits in the architecture)
VPC Peering is strictly **non-transitive**. If VPC A is peered with VPC B, and VPC B is peered with VPC C, VPC A cannot route traffic to VPC C through VPC B. Peering requires that both VPCs have **non-overlapping CIDR blocks**. Route tables in both VPCs must have explicit route entries targeting the peering connection ID (`pcx-xxxxxx`).

---

## 🧩 Problem Solver (What problem it solves)
Before VPC Peering, connecting separate VPCs required routing traffic over the public internet (using NAT and public IPs) or deploying site-to-site VPN tunnels, which introduced latency, security exposure, and data transfer costs. VPC Peering solves this by offering native, high-bandwidth private routing with no gateway bottleneck.

---

## 🟢 Operational Impact (What will happen with it operating)
Workloads communicate privately across VPC boundaries with low latency. Data transfer costs apply for traffic traversing peering connections, following standard cross-AZ/cross-region rules. Mesh topologies must be managed carefully as the number of peered VPCs increases.

---

## 🔴 Failure Impact (What will happen without it)
If a peering connection is deleted or the route table configurations are missing, inter-VPC traffic is cut off immediately. Peering deletion leaves "black hole" routes in the associated route tables, causing outbound packets targeting the peered VPC to be dropped.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **VPC Peering**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[VPC Peering]]
SORT file.name ASC
```
