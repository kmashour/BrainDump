---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Azure Virtual Networking and Intersite Connectivity]]"
sub_type: pitfall
source_type: gemini-chat
source_url: ""
author: "Antigravity"
course_title: "AZ-104 Masterclass"
tags:
  - azure/networking
  - azure/routing
  - azure/nva
  - azure/troubleshooting
  - azure/deep-dive
  - status/completed
---

# Azure Intersite Connectivity - Asymmetric Routing Traps, Stateful NVA Packet Drops, and Return Path Black Holes

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Azure Virtual Networking and Intersite Connectivity]] > **Asymmetric Routing Traps & NVA Packet Drops**

---

## 💥 Incident Forensics: The Silent Cross-Spoke Connection Outage

In Hub-and-Spoke enterprise topologies, the single most common cause of mysterious, intermittent application timeouts is **Asymmetric Routing**. 

When traffic flows forward through a stateful firewall appliance but returns through a different path that bypasses the firewall, the firewall’s state table is violated and the connection is silently killed.

---

## 🏛️ 1. The Architectural Setup & Engineering Assumptions

A cloud engineering team deploys a standard enterprise Hub-and-Spoke network:
* **Hub VNet (`vnet-hub`):** Contains a centralized **Azure Firewall / Network Virtual Appliance (NVA)** at IP `10.0.1.4`.
* **Spoke 1 (`vnet-app: 10.1.0.0/16`):** Contains frontend web applications.
* **Spoke 2 (`vnet-db: 10.2.0.0/16`):** Contains database servers.

To force all traffic from Spoke 1 through the firewall:
1. The engineer creates a Route Table attached to Spoke 1's subnet:
   * **Route:** `10.2.0.0/16` ➔ **Next Hop:** `VirtualAppliance` (`10.0.1.4`).
2. **The Flawed Engineering Assumption:**
   The engineer assumes that because Spoke 1 has a route pointing to the Firewall, any conversation between Spoke 1 and Spoke 2 will automatically be handled and returned properly.

---

## 💀 2. The Failure Loop: The Half-Open TCP Handshake

When an application server in Spoke 1 attempts to open a database connection to Spoke 2 on TCP port 1433, the connection hangs and eventually terminates with `Connection Timed Out`.

```text
               FORWARD PATH (SYN Packet)                        RETURN PATH (SYN-ACK Packet)
               ─────────────────────────                        ────────────────────────────
 [ Spoke 1: App VM (10.1.1.4) ]                   [ Spoke 1: App VM (10.1.1.4) ]
               │                                                ▲
    (1. Evaluates UDR: 10.2.0.0/16 -> NVA)                      │ (4. Rejects or never received!)
               ▼                                                │
 [ Hub NVA / Firewall (10.0.1.4) ]                              │
   - Inspects SYN packet                                        │ (Bypasses Firewall completely!)
   - Creates entry in State Table: [HALF-OPEN]                  │
               │                                                │
               ▼ (Peering Link)                                 │ (Peering Link: Spoke 2 -> Spoke 1)
 [ Spoke 2: DB VM (10.2.1.4) ] ─────────────────────────────────┘
   - Receives SYN packet from 10.1.1.4
   - Generates return SYN-ACK packet
   - Evaluates Spoke 2 Route Table:
     No UDR for 10.1.0.0/16!
     Uses System Default Route (Direct Peering)!
   - Sends SYN-ACK DIRECTLY to Spoke 1, BYPASSING THE FIREWALL!
```

### The Outage Mechanics:
1. **Forward Path:** Spoke 1 sends a TCP `SYN` packet. The UDR routes it to the Hub Firewall (`10.0.1.4`). The firewall logs the packet and adds an entry to its connection state table: `SYN_SENT (Expecting return SYN-ACK from 10.2.1.4)`. The firewall then forwards the packet to Spoke 2.
2. **Return Path:** Spoke 2 receives the packet and generates a `SYN-ACK`. It checks its local routing table. Because Spoke 2 has **no custom route table**, it defaults to Azure's System Route: `10.1.0.0/16 -> VNet Peering`.
3. **The Bypass:** The return packet flies directly across the peering link to Spoke 1, **completely bypassing the Hub Firewall**.
4. **The Firewall Timeout & Drop:** 
   * The Hub Firewall never receives the `SYN-ACK`.
   * After a brief timeout, the stateful firewall marks the connection as orphaned and drops any future data packets from Spoke 1.
   * If any return packets do hit the firewall later, the firewall drops them immediately with a `TCP Reset (RST)` because it violates state tracking!

---

## 🔬 3. Root Cause Analysis (RCA): Stateful Firewalls Mandate Symmetry

A stateful firewall (whether Azure Firewall, Palo Alto, Fortinet, or Check Point) does not evaluate packets in isolation; it tracks the complete TCP state machine:

$$\text{Valid Stateful Connection} = \text{Forward Path (NVA)} \cap \text{Return Path (NVA)}$$

If:
$$\text{Forward Path} \neq \text{Return Path}$$

The firewall detects an **Asymmetric Route**. To prevent TCP sequence prediction and session hijacking attacks, the firewall’s stateful engine is hardwired to **drop all packets** that do not traverse both directions symmetrically.

---

## 🛡️ 4. Remediation: Two Architectural Solutions

To permanently resolve asymmetric routing in Hub-and-Spoke networks, architects implement one of two proven solutions:

### Solution A: Symmetric User-Defined Routes (The Standard Approach)
Every spoke in the enterprise must possess a matching Route Table that symmetrically points back to the Hub Firewall:
* On Spoke 1 Subnet: `10.2.0.0/16` ➔ `VirtualAppliance (10.0.1.4)`
* On Spoke 2 Subnet: `10.1.0.0/16` ➔ `VirtualAppliance (10.0.1.4)`

Now, both the forward `SYN` and the return `SYN-ACK` pass through `10.0.1.4`. The firewall verifies the two-way handshake and keeps the connection alive.

### Solution B: Source Network Address Translation (SNAT) on the NVA
If managing symmetric route tables across 100 spokes is too complex:
* Configure the Hub NVA / Azure Firewall to perform **Source NAT (SNAT)** on all forwarded cross-spoke traffic.
* When the NVA forwards Spoke 1's packet to Spoke 2, it replaces Spoke 1's source IP (`10.1.1.4`) with **the NVA's own internal IP (`10.0.1.4`)**.
* When Spoke 2 replies, it sees the destination as `10.0.1.4`. It has no choice but to send the return packet directly back to the NVA, forcing perfect routing symmetry automatically!

---

*Read more in [[Reference Notes/13-104-06_administer_intersite_connectivity.md#3-gateway-transit--spoke-to-spoke-transitivity]]*
