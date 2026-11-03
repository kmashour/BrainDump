---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Azure Virtual Networking and Intersite Connectivity]]"
sub_type: architecture
source_type: gemini-chat
source_url: ""
author: "Antigravity"
course_title: "AZ-104 Masterclass"
tags:
  - azure/networking
  - azure/routing
  - azure/udr
  - azure/deep-dive
  - status/completed
---

# Azure Intersite Connectivity - Routing Engine Mechanics, Longest Prefix Match, and User-Defined Routes

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Azure Virtual Networking and Intersite Connectivity]] > **Routing Engine Mechanics, LPM & User-Defined Routes**

---

## 🎯 1. First Principles: How Azure SDN Decides Packet Trajectories

In a physical datacenter, routers examine their hardware routing tables (FIB / TCAM) to determine which egress interface to send an IP frame. 

In Microsoft Azure, there are no physical routers inside customer subnets. Routing is handled entirely by the **Software-Defined Networking (SDN) virtual filter driver** running on the host physical hypervisor. Every virtual machine network interface (vNIC) is programmed with a dynamic routing table by the Azure fabric.

Understanding how Azure evaluates competing routes, handles default traffic, and overrides system routes using **User-Defined Routes (UDRs)** is the foundation of enterprise cloud traffic engineering.

---

## 🏛️ 2. The Immutable System Default Routes

Every subnet created in an Azure Virtual Network is born with default, un-deletable **System Routes** injected directly by Microsoft:

| Destination Address Prefix | Next Hop Type | Platform Routing Behavior |
| :--- | :--- | :--- |
| **`Local VNet CIDR`** (e.g., `10.50.0.0/16`) | **`Virtual network`** | Routes packets directly between any subnets within the VNet at hypervisor line-rate speed. |
| **`0.0.0.0/0`** (Default Route) | **`Internet`** | Directs unmapped traffic to Microsoft's public internet edge gateway. |
| **`RFC 1918 Private Ranges`** (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) | **`None`** | Drops packets destined for unallocated private IP ranges into a black hole, preventing private IP leakage onto the internet. |

---

## ⚖️ 3. The Routing Decision Engine: The Two Universal Laws

When a virtual machine sends an IP packet, Azure evaluates its routing table against **two deterministic rules**:

### Rule 1: The Longest Prefix Match (LPM) Rule ALWAYS Wins!
Regardless of whether a route is a custom UDR, a BGP route from an ExpressRoute circuit, or an Azure system route, **the route with the most specific (longest) subnet mask always takes precedence**:

```text
Incoming Packet: Destination IP = 10.50.1.15
────────────────────────────────────────────────────────────────────────────────
Route A (System Route): Prefix = 10.50.0.0/16 | Next Hop = Virtual network
Route B (Custom UDR):   Prefix = 10.50.1.0/24 | Next Hop = VirtualAppliance (10.0.1.4)
────────────────────────────────────────────────────────────────────────────────
WINNER: Route B (/24)!
Because /24 specifies a smaller, more specific block of IPs than /16.
Traffic is successfully diverted to the Virtual Appliance!
```

### Rule 2: Precedence Order for Identical Prefixes
If two competing routes possess the **exact same destination prefix** (for example, both define `0.0.0.0/0`), Azure breaks the tie using a strict priority order:

$$\mathbf{\text{User-Defined Route (UDR)}} \succ \mathbf{\text{BGP Routes (ExpressRoute / VPN)}} \succ \mathbf{\text{System Default Routes}}$$

1. **User-Defined Routes (UDRs):** Always win over BGP and System routes for identical prefixes.
2. **BGP Routes:** Win over System default routes.
3. **System Default Routes:** Lowest priority fallback.

---

## 🎛️ 4. Next Hop Types in a Route Table (UDR)

When authoring a custom Route Table in the Azure Portal GUI or CLI, an administrator specifies the **Next hop type**:

```text
+---------------------------------------------------------------------------------------------------+
| NEXT HOP TYPE                | OPERATIONAL MECHANICS & USE CASES                                  |
+------------------------------+--------------------------------------------------------------------+
| 1. VirtualAppliance          | Directs packets to a private RFC 1918 IP address (e.g., 10.0.1.4)  |
|                              | representing an Azure Firewall or third-party NVA (Palo Alto, etc.)|
| 2. VirtualNetworkGateway     | Directs traffic through the local VNet's VPN or ExpressRoute GW.   |
| 3. VnetLocal                 | Forces packets to route directly within the local VNet,            |
|                              | effectively bypassing an overarching /16 firewall UDR.             |
| 4. Internet                  | Forces packets out to the public internet edge directly, bypassing|
|                              | a default 0.0.0.0/0 firewall inspection rule.                      |
| 5. None                      | Black-holes all matching packets (Drops traffic at hypervisor).    |
+---------------------------------------------------------------------------------------------------+
```

---

## 🔬 5. The Architect's Diagnostic Tool: "Effective Routes"

Because subnets inherit a combination of System Routes, BGP routes, and attached Route Tables, calculating the active route table manually in complex enterprise networks is prone to human error.

To determine the exact, living routing table enforced by the hypervisor:
1. In the Azure Portal, navigate to the target Virtual Machine.
2. Under **Networking**, click on the **Network Interface (NIC)**.
3. In the left navigation menu under **Help**, click **Effective routes**.

```text
+---------------------------------------------------------------------------------------------------+
| EFFECTIVE ROUTES BLADE (Portal Forensic Output)                                                    |
+---------------------------------------------------------------------------------------------------+
| Prefix            | Next Hop Type     | Next Hop IP       | User / Source      | State            |
+-------------------+-------------------+-------------------+--------------------+------------------+
| 10.50.0.0/16      | VnetLocal         | -                 | Default            | Active           |
| 0.0.0.0/0         | VirtualAppliance  | 10.0.1.4          | User (rt-hub)      | Active (Winner!) |
| 0.0.0.0/0         | Internet          | -                 | Default            | Invalid (Overridden)
+---------------------------------------------------------------------------------------------------+
```

* Notice that the default `Internet` route becomes **`Invalid` (Overridden)** because the custom User-Defined Route (`rt-hub`) has higher precedence!

---

*Read more in [[Reference Notes/13-104-06_administer_intersite_connectivity.md#2-azure-routing-engine--user-defined-routes-udr]]*
