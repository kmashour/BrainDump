---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: network
domains:
  - "azure"
  - "networking"
related_concepts:
  - "[[Microsoft Azure]]"
  - "[[Azure Resource Manager]]"
against:
  - "[[Classic Virtual Network]]"
reference_guides:
  - "[[Reference Notes/13-4_azure_virtual_networking_and_hybrid_connectivity.md]]"
tags:
  - azure/networking
  - status/completed
---

# Azure Virtual Network

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Networking > **Azure Virtual Network**

---

## 🎯 Purpose (Why it is used)
An **Azure Virtual Network (VNet)** is the core software-defined networking construct in Azure that provides private, isolated networking for cloud workloads. VNets enable Azure resources (Virtual Machines, scale sets, databases) to communicate privately with each other, the public internet, and on-premises corporate datacenters.

---

## ⚙️ Functionality (What it is doing)
1. **Private Address Allocation:** Carves out private RFC 1918 CIDR blocks (`10.0.0.0/16`) subdivided into subnets.
2. **Internal Routing:** Provides built-in system routing across subnets with 5 reserved management IP addresses per subnet (`.0`, `.1`, `.2`, `.3`, `.255`).
3. **Traffic Segmentation:** Applies Network Security Groups (NSGs) with stateful 5-tuple filtering rules to subnets and network interfaces.
4. **VNet Peering:** Interconnects multiple VNets across the high-speed Microsoft private fiber backbone without public internet traversal.

---

## 🏛️ Architectural Context (How it fits in the architecture)
- Resides strictly within a single Azure region, but its subnets inherently span all Availability Zones within that region.
- Connects to on-premises infrastructure via VPN Gateways or ExpressRoute circuits.

---

## 🧩 Problem Solver (What problem it solves)
- Prevents public internet exposure of sensitive database and application tiers.
- Solves inter-workload isolation and micro-segmentation challenges in multi-tier architectures.

---

## 🟢 Operational Impact (What will happen with it operating)
- Workloads communicate over private, low-latency virtual network interfaces (NICs).
- Security perimeters are enforced through Network Security Groups and User Defined Routes (UDRs).

---

## 🔴 Failure Impact (What will happen without it)
- Cloud compute instances cannot obtain private IPs or communicate with other services.

---

## 🔍 Deeper Dive Notes
```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
