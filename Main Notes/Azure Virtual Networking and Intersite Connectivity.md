---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: network
domains:
  - "azure"
  - "networking"
related_concepts:
  - "[[Reference Notes/13-104-05_administer_virtual_networking.md]]"
  - "[[Reference Notes/13-104-06_administer_intersite_connectivity.md]]"
against: []
reference_guides:
  - "[[Reference Notes/13-104-05_administer_virtual_networking.md]]"
  - "[[Reference Notes/13-104-06_administer_intersite_connectivity.md]]"
tags:
  - azure/networking
  - azure/vnet
  - azure/peering
  - status/completed
---

# Azure Virtual Networking and Intersite Connectivity

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Azure Networking > **Azure Virtual Networking and Intersite Connectivity**

---

## 🎯 Purpose (Why it is used)

In traditional on-premises enterprise datacenters, network isolation depended entirely on physical cabling, Top-of-Rack (ToR) switches, 802.1Q VLAN tagging, and dedicated hardware appliances (firewalls, routers, and VPN concentrators). However, deploying physical broadcast domains at hyperscale cloud capacity is impossible: if thousands of enterprise tenants sharing physical hypervisor hosts shouted Ethernet ARP broadcasts across common datacenter switches, the physical infrastructure would immediately collapse under a catastrophic **broadcast storm**. Furthermore, multiple tenants concurrently require standard RFC 1918 private address blocks (such as `10.0.0.0/16`), creating inevitable IP collision conflicts on shared hardware.

**Azure Virtual Networking (VNet)** and its associated **Intersite Connectivity** fabric solve this fundamental challenge through high-performance **Software-Defined Networking (SDN)**. An Azure Virtual Network provides a secure, completely isolated Layer 3 overlay network running on Microsoft's global physical fiber backbone. It enables enterprise workloads—ranging from virtual machines and container clusters to PaaS databases—to communicate internally with ultra-low latency, while remaining entirely invisible and unreachable to other cloud tenants sharing the same physical datacenters. Intersite connectivity mechanisms (such as **VNet Peering**, **Hub-and-Spoke Topologies**, **User-Defined Routes**, and **Azure Private Link**) allow organizations to interconnect distinct business units, shared services, on-premises datacenters, and PaaS endpoints without exposing sensitive data traffic to the public internet.

---

## ⚙️ Functionality (What it is doing)

Azure Virtual Networking and Intersite Connectivity deliver enterprise-grade networking through five core control and data plane capabilities:

1. **Private Subnet Topography & Address Allocation:** Carves out contiguous CIDR address blocks (`/8` through `/29`) from private RFC 1918 ranges, managing the platform's **5 reserved IP addresses** per subnet (`.0`, `.1`, `.2`, `.3`, and `.255`) and housing specialized system subnets (`GatewaySubnet`, `AzureBastionSubnet`, `AzureFirewallSubnet`).
2. **Hypervisor Wire Server & Stateful Security Filtering:** Implements the platform-wide **`168.63.129.16` Anycast Wire Server** directly in hypervisor vSwitch code to orchestrate DHCP lease renewals, recursive DNS lookups, and load balancer health probes. Enforces microsegmentation through a **two-tier stateful Network Security Group (NSG)** pipeline (Subnet NSG $\rightarrow$ NIC NSG) paired with declarative **Application Security Groups (ASGs)**.
3. **Line-Rate Private Interconnects (VNet Peering):** Interconnects Virtual Networks within the same region (**Regional Peering**) or across geographic continents (**Global VNet Peering**) directly at the SDN hypervisor layer over Microsoft's private optical WAN backbone, achieving wire-speed throughput (up to 100 Gbps) with zero gateway bottlenecks.
4. **Traffic Steering & Hub-and-Spoke Transitivity:** Overrides default system routing using custom **User-Defined Routes (UDRs)** governed by Longest Prefix Match (LPM) logic. When paired with **Allow Forwarded Traffic** and Network Virtual Appliances (NVAs) or Azure Firewall, it overcomes the non-transitive nature of peering to funnel spoke-to-spoke and egress traffic through centralized inspection checkpoints.
5. **Private PaaS Ingestion (Azure Private Link & Private Endpoints):** Replaces public VIP routing with unmanaged virtual network interfaces (NICs) assigned private IP addresses directly within customer subnets. Uses Source NAT (SNAT) proxying behind Standard Load Balancers to allow secure connections between overlapping CIDR address spaces while completely neutralizing data exfiltration hazards.

---

## 🏛️ Architectural Context (How it fits in the architecture)

Azure networking sits at the foundation of all cloud workloads. It acts as the transport and isolation fabric connecting compute instances, storage accounts, databases, security perimeters, and on-premises enterprise sites.

```text
+---------------------------------------------------------------------------------------------------+
|                        AZURE ENTERPRISE VIRTUAL NETWORKING TOPOLOGY                               |
+---------------------------------------------------------------------------------------------------+
                               [ On-Premises Corporate Headquarters ]
                                                 │
                                                 │ Site-to-Site IPsec VPN / ExpressRoute
                                                 ▼
+---------------------------------------------------------------------------------------------------+
| HUB VIRTUAL NETWORK (vnet-hub: 10.0.0.0/16)                                                       |
|                                                                                                   |
|  [ GatewaySubnet (10.0.0.0/27) ]              [ AzureFirewallSubnet (10.0.1.0/26) ]              |
|  └── Virtual Network Gateway (VPN / ER)       └── Azure Firewall / NVA (10.0.1.4)                 |
|      (Gateway Transit: ENABLED)                   (Central Traffic Inspection & Routing)          |
+---------------------------------------------------------------------------------------------------+
                ▲                                                                   ▲
                │ Bidirectional VNet Peering                                        │ Bidirectional VNet Peering
                │ (Allow Forwarded Traffic: TRUE)                                   │ (Allow Forwarded Traffic: TRUE)
                ▼                                                                   ▼
+-----------------------------------------------+   +-----------------------------------------------+
| SPOKE 1: APPLICATION TIER (vnet-app: 10.1.0.0/16)|   | SPOKE 2: DATA TIER (vnet-data: 10.2.0.0/16)   |
|                                               |   |                                               |
|  [ snet-workload (10.1.1.0/24) ]              |   |  [ snet-endpoints (10.2.1.0/24) ]             |
|  ├── App VM (10.1.1.4)                        |   |  ├── Database VM (10.2.1.4)                   |
|  ├── Wire Server: 168.63.129.16               |   |  └── Private Endpoint (10.2.1.10)             |
|  ├── Two-Tier NSG (Subnet NSG + NIC NSG)      |   |      └── Azure Storage Account (Blob)         |
|  └── UDR: 0.0.0.0/0 -> Next Hop: 10.0.1.4     |   |          (Public Access: 100% DISABLED)       |
+-----------------------------------------------+   +-----------------------------------------------+
                │                                                                   ▲
                └────────────────────────── BLOCKED ────────────────────────────────┘
                                  (Peering is Non-Transitive!)
                        Spoke 1 cannot talk directly to Spoke 2
                        without routing through the Hub Firewall NVA!
```

---

## 🧩 Problem Solver (What problem it solves)

* **Prevents Multi-Tenant Datacenter Collapses:** Replaces unscalable Layer 2 physical broadcast domains with an encapsulated SDN overlay (using Geneve/VXLAN encapsulation), eliminating ARP broadcast storms across cloud regions.
* **Eliminates Public Surface Exposure for Cloud PaaS:** Azure Private Endpoints eliminate the requirement of exposing public IP addresses for sensitive databases, key vaults, and storage accounts, restricting all access strictly to private IP tunnels.
* **Solves Address Space Exhaustion & Overlapping CIDRs:** Through Private Link Service NAT IP masking, partner organizations and merged entities with conflicting RFC 1918 CIDR blocks (e.g., both utilizing `10.0.0.0/16`) can seamlessly consume services without re-architecting their IP plans.
* **Centralizes Security Governance & Egress Control:** Enables centralized inspection of all enterprise egress and spoke-to-spoke communication via a central Hub NVA or Azure Firewall, avoiding decentralized, costly standalone firewalls in every application team's network.
* **Delivers Predictable, Granular Microsegmentation:** Application Security Groups (ASGs) decouple firewall policy maintenance from volatile IP addresses, allowing security rules to adapt dynamically as workloads autoscale.

---

## 🟢 Operational Impact (What will happen with it operating)

* Applications communicate across subnets, peered VNets, and cloud regions at wire speed (up to 100 Gbps) with sub-millisecond round-trip times and zero gateway hop serialization delays.
* Security operations teams enforce unified zero-trust egress policies at the central Hub firewall, capturing comprehensive diagnostic logs and intrusion telemetry for compliance auditing.
* Virtual machines securely and automatically obtain IP configurations, resolve private and internal DNS names via Private DNS Zones, and report health metrics to load balancers through the transparent Wire Server (`168.63.129.16`).
* Spoke networks consume centralized VPN and ExpressRoute gateways located in the Hub via **Gateway Transit**, dramatically reducing infrastructure expenditure and administrative overhead.

---

## 🔴 Failure Impact (What will happen without it)

* **Uncontrolled Cloud Sprawl & Security Breaches:** Workloads deployed in unmanaged, isolated networks either expose raw management ports (RDP 3389, SSH 22) to the public internet or rely on insecure public endpoints for backend databases.
* **Silent Packet Drops & Asymmetric Routing Outages:** Misunderstanding peering non-transitivity, omitting the `AllowForwardedTraffic` flag, or neglecting return UDRs causes complete inter-spoke communication failures, stranding application tiers.
* **Catastrophic Infrastructure Lockout:** Blocking the `168.63.129.16` Wire Server inside guest OS firewalls or third-party endpoint agents causes failed load balancer health probes, unrenewed DHCP leases, and complete network interface collapse.
* **Cost Inefficiencies & Multi-Gateway Redundancy:** Provisioning duplicate Virtual Network Gateways in every spoke network instead of using Gateway Transit wastes thousands of dollars monthly in idle gateway SKU billing.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, architectural mechanics, and failure modes associated with **Azure Virtual Networking and Intersite Connectivity**:

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
FROM "Main Notes"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

### Core Architecture & Mechanics
- [[Main Notes/Azure Virtual Networking - Subnet Topography, 5 Reserved IPs, and Dedicated System Subnets.md|Azure Virtual Networking: Subnet Topography, 5 Reserved IPs, and Dedicated System Subnets]]
- [[Main Notes/Azure Virtual Networking - Wire Server Mechanics, Subnet DNS Proxies, and Stateful NSG Inspection.md|Azure Virtual Networking: Wire Server Mechanics, Subnet DNS Proxies, and Stateful NSG Inspection]]
- [[Main Notes/Azure Virtual Networking - Non-Transitive Peering Invariants, Forwarded Traffic Mechanics, and Virtual WAN.md|Azure Virtual Networking: Non-Transitive Peering Invariants, Forwarded Traffic Mechanics, and Virtual WAN]]
- [[Main Notes/Azure Virtual Networking - Private Link vs Private Endpoints, and VNet-to-VNet VPN Tradeoffs.md|Azure Virtual Networking: Private Link vs Private Endpoints, and VNet-to-VNet VPN Tradeoffs]]

*Related Reference Modules:* 
- [[Reference Notes/13-104-05_administer_virtual_networking.md|Module 13-104-05: Administer Azure Virtual Networking, NSGs & DNS]]
- [[Reference Notes/13-104-06_administer_intersite_connectivity.md|Module 13-104-06: Administer Intersite Connectivity, Routing & Private Link]]
