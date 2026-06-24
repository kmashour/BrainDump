---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: network
domains:
  - "aws"
related_concepts:
  - "[[aws - Elastic Load Balancer]]"
  - "[[aws - Application Load Balancer]]"
  - "[[aws - Network Load Balancer]]"
against: []
reference_guides:
  - "[[Reference Notes/3-10_aws_elb_load_balancing.md]]"
tags:
  - aws/loadbalancing
  - status/completed
---

# aws - Gateway Load Balancer

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - Elastic Load Balancer]] > **Gateway Load Balancer**

---

## 🎯 Purpose (Why it is used)
The Gateway Load Balancer (GWLB) is a Layer 3 load balancer designed to deploy, scale, and manage a fleet of third-party network virtual appliances (such as firewalls, intrusion detection/prevention systems (IDS/IPS), and deep packet inspection). It is used to transparently intercept and inspect network traffic in the VPC before forwarding it to its final destination.

---

## ⚙️ Functionality (What it is doing)
- **Layer 3 Packet Routing:** Intercepts and routes raw IP packets at the network layer.
- **Transparent Gateway:** Functions as a single entry and exit point for VPC traffic, making inspection completely transparent to the client and destination application.
- **GENEVE Protocol Encapsulation:** Encapsulates the original IP packet in a GENEVE tunnel wrapper (on UDP port 6081) to preserve original connection metadata (IP/Port) during appliance processing.
- **Health Monitoring:** Frequently tests the health of target virtual appliances, dynamically routing packets around failed appliances.
- **Target Groups:** Supports appliances registered as targets by Instance ID or private IP addresses.

---

## 🏛️ Architectural Context (How it fits in the architecture)
GWLB works at the subnet route table level. Traffic entering the VPC via the Internet Gateway (IGW) or Transit Gateway is routed to a Gateway Load Balancer Endpoint (GWLBE). The GWLBE redirects traffic to the GWLB, which routes it through the virtual appliance fleet for inspection. Once accepted, the traffic returns through the GWLB to the GWLBE, which routes it to the target application servers.

---

## 🧩 Problem Solver (What problem it solves)
Deploying firewalls and IDS/IPS inline within a cloud environment was historically complex, requiring complex routing tables, source NATing, or complex VPN overlays. GWLB solves this by acting as a transparent bump-in-the-wire, scaling appliances horizontally based on traffic load and ensuring automatic failover.

---

## 🟢 Operational Impact (What will happen with it operating)
All inbound and outbound traffic is securely inspected by a firewall cluster. Inter-AZ data transfer is chargeable, as GWLB cross-zone load balancing is disabled by default.

---

## 🔴 Failure Impact (What will happen without it)
If the GWLB or its endpoint fails, route table paths are broken, and all VPC traffic directed to the inspection endpoint will be dropped. If all targets in the virtual appliance group are unhealthy, the GWLB drops the traffic rather than failing open (depending on routing configuration).

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Gateway Load Balancer**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
