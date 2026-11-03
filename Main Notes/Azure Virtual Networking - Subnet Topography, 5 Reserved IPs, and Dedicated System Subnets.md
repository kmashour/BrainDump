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
  - azure/subnets
  - azure/cidr
  - azure/deep-dive
  - status/completed
---

# Azure Virtual Networking - Subnet Topography, 5 Reserved IPs, and Dedicated System Subnets

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Azure Virtual Networking and Intersite Connectivity]] > **Subnet Topography, 5 Reserved IPs, and Dedicated System Subnets**

---

## 🎯 1. First Principles: CIDR Addressing & Subnet Mathematics in Azure SDN

In traditional on-premises networking, subnets are carved out of IPv4 address space using standard Classless Inter-Domain Routing (CIDR) notation. In a physical subnet, exactly **two IP addresses** are unusable by hosts according to RFC 1122 and RFC 919/922: the **Network ID** (the first address) and the **Broadcast Address** (the last address).

In Microsoft Azure's Software-Defined Networking (SDN) architecture, however, the underlying physical hypervisors, virtual switches (vSwitches), and management fabric intercept network traffic directly in software. Azure enforces strict constraints on subnet sizing, address reservation, and delegation that deviate from physical data center norms.

```text
+---------------------------------------------------------------------------------------------------+
|                        AZURE SUBNET ADDRESS ALLOCATION ARCHITECTURE                               |
+---------------------------------------------------------------------------------------------------+
| Example Subnet: 10.0.1.0/24 (Total: 256 IP Addresses)                                            |
|                                                                                                   |
|  [ 10.0.1.0 ] ──► Reserved: Subnet Network ID (RFC 1122 protocol boundary)                        |
|  [ 10.0.1.1 ] ──► Reserved: Azure Default Gateway (vSwitch virtual router interface)              |
|  [ 10.0.1.2 ] ──► Reserved: Azure Primary DNS Resolver (Virtual mapping to 168.63.129.16)        |
|  [ 10.0.1.3 ] ──► Reserved: Azure Secondary DNS Resolver (HA secondary resolver mapping)          |
|  [ 10.0.1.4 ] ──► FIRST USABLE IP: Assigned to the very first VM NIC or resource deployed!        |
|  [ 10.0.1.5 ] ──► Usable IP: VM 2 / Service NIC                                                   |
|      ...                                                                                          |
|  [ 10.0.1.254] ──► Usable IP: VM 251 / Service NIC                                                |
|  [ 10.0.1.255] ──► Reserved: Subnet Broadcast Address (SDN fabric drops all L2 broadcast)         |
+---------------------------------------------------------------------------------------------------+
```

### The Subnet Sizing Formulas:
Azure Virtual Networks support CIDR prefixes from `/8` (16,777,216 addresses) down to `/29` (8 addresses). A `/29` subnet is the **absolute smallest permissible subnet** in Azure. Any attempt to provision a `/30` (4 addresses) or `/31` (2 addresses) subnet is rejected by the Azure Resource Manager (ARM) control plane because it cannot satisfy the mandatory 5-IP platform reservation.

$$\text{Host Bits} = 32 - \text{Prefix Length}$$
$$\text{Total Addresses} = 2^{\text{Host Bits}}$$
$$\text{Usable Host Count} = 2^{(32 - \text{Prefix Length})} - 5$$

### Standard Subnet Sizing Reference:

| Prefix | Host Bits | Total IP Addresses | Azure Reserved IPs | Usable IP Addresses | Primary Enterprise Use Cases |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **`/24`** | 8 | 256 | 5 | **251** | Standard application, web, and database workload tiers |
| **`/26`** | 6 | 64 | 5 | **59** | Dedicated system subnets (`AzureBastionSubnet`, `AzureFirewallSubnet`) |
| **`/27`** | 5 | 32 | 5 | **27** | Recommended minimum for `GatewaySubnet`, `RouteServerSubnet` |
| **`/28`** | 4 | 16 | 5 | **11** | Small specialized utility pools, testing environments |
| **`/29`** | 3 | 8 | 5 | **3** | **Absolute minimum subnet in Azure** (Micro-pools, single NVA pairs) |

---

## 🔒 2. The 5 Azure Reserved IP Addresses (First-Principles Breakdown)

In **every single subnet** created within an Azure Virtual Network, exactly **5 IP addresses** are permanently reserved by the platform fabric and can never be assigned to a virtual machine, network interface card (NIC), or private endpoint:

1. **First Address (`.0` in `/24` — Subnet Network Address):**
   * *Purpose:* Adheres strictly to RFC 1122. It identifies the network boundary itself.
   * *Why it is reserved:* Standard IP routing stacks require the base wire identifier for route computation and subnet prefix identification.
2. **Second Address (`.1` in `/24` — Azure Default Gateway):**
   * *Purpose:* Represents the virtual default router for all network interfaces residing within the subnet.
   * *Why it is reserved:* In Azure SDN, there is no physical router sitting in the rack. Instead, the local hypervisor vSwitch intercepts all outbound packets addressed to `.1` and evaluates Azure's SDN routing flow tables (System Routes and User-Defined Routes) directly in the hypervisor kernel driver.
3. **Third Address (`.2` in `/24` — Azure Primary DNS Resolver):**
   * *Purpose:* Maps to the Azure platform recursive DNS service.
   * *Why it is reserved:* When a virtual machine boots and initializes its network interface via DHCP, Azure configures `.2` as the primary DNS server. This address acts as an internal proxy pointer to the underlying Azure Wire Server (`168.63.129.16`), enabling seamless resolution of internal hostname records, Azure Private DNS Zones, and public internet domains.
4. **Fourth Address (`.3` in `/24` — Azure Secondary DNS Resolver):**
   * *Purpose:* Provides a secondary, highly available DNS resolver address.
   * *Why it is reserved:* Redundant DNS mapping ensuring that guest operating systems configured with primary and secondary resolvers maintain high availability for name resolution without downtime.
5. **Last Address (`.255` in `/24` — Subnet Broadcast Address):**
   * *Purpose:* Adheres to RFC 919/922 network broadcast conventions.
   * *Why it is reserved:* Traditional physical networks use the broadcast address to flood packets to every switch port. Azure SDN **drops all Layer 2 broadcast and multicast traffic** at the hypervisor virtual filter driver to prevent broadcast storms. This address is reserved to maintain compatibility with standard RFC network stacks.

> [!IMPORTANT]
> **The First Usable IP Rule:**
> Because addresses `.0` through `.3` are permanently consumed by the Azure platform, the **very first virtual machine or network interface card** provisioned into any Azure subnet will **always receive IP `.4`** (e.g., `10.0.1.4` in `10.0.1.0/24`)!

---

## 🏛️ 3. Dedicated System Subnets: Sizing Constraints & Operational Rules

Azure provisions managed PaaS networking components directly into your private Virtual Network. These managed services require **dedicated system subnets** that adhere to strict naming conventions, prefix sizes, and security constraints. Violating these rules results in deployment failures or platform-level routing outages.

```text
+---------------------------------------------------------------------------------------------------+
|                            AZURE DEDICATED SYSTEM SUBNETS ARCHITECTURE                            |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|  [ GatewaySubnet ] ──────────► Sizing: /27 recommended (min /29)                                  |
|                                Constraints: NO Network Security Groups (NSGs)!                    |
|                                             NO User-Defined Routes (UDRs) for 0.0.0.0/0 to NVA!   |
|                                                                                                   |
|  [ AzureBastionSubnet ] ─────► Sizing: /26 minimum                                                |
|                                Constraints: MUST be named exactly 'AzureBastionSubnet'           |
|                                             Strict Inbound NSG: Port 443 from Internet            |
|                                             NO User-Defined Route altering default gateway!       |
|                                                                                                   |
|  [ AzureFirewallSubnet ] ────► Sizing: /26 minimum                                                |
|                                Constraints: MUST be named exactly 'AzureFirewallSubnet'          |
|                                             ARM blocks NSG attachment completely!                 |
|                                                                                                   |
|  [ RouteServerSubnet ] ──────► Sizing: /27 minimum                                                |
|                                Constraints: MUST be named exactly 'RouteServerSubnet'            |
|                                             Dedicated to Azure Route Server BGP speakers          |
+---------------------------------------------------------------------------------------------------+
```

### 1. `GatewaySubnet`: Virtual Network Gateway Host
* **Purpose:** Houses the virtual machine instances running Azure Virtual Network Gateways (Site-to-Site IPsec VPN, Point-to-Site VPN, and ExpressRoute Gateways).
* **Naming Constraint:** Must be named **strictly and case-sensitively** `GatewaySubnet`.
* **Sizing Requirements:**
  * Absolute minimum prefix: `/29` (8 IPs, 3 usable).
  * **Enterprise Recommended Minimum: `/27` (32 IPs, 27 usable)** or larger.
  * *Why `/27` is required:* If an organization provisions both a VPN Gateway and an ExpressRoute Gateway in the same VNet, or plans to execute zero-downtime gateway SKU resizing/maintenance, Azure temporarily provisions duplicate gateway instances. A `/29` will run out of IPs and cause upgrade failures.
* **Critical Operational Guardrails:**
  * **NEVER attach an NSG to `GatewaySubnet`:** Applying a Network Security Group to the GatewaySubnet will block internal control-plane traffic, BGP keepalives, and gateway health probes, causing intermittent or total VPN/ExpressRoute tunnel collapse.
  * **NEVER attach a UDR with `0.0.0.0/0` targeting an NVA to `GatewaySubnet`:** Routing gateway egress through an NVA breaks IPsec tunnel establishment to public IP endpoints.

### 2. `AzureBastionSubnet`: Managed Zero-Trust Bastion Host
* **Purpose:** Hosts the managed Azure Bastion PaaS instance that provides browser-based, clientless RDP and SSH connectivity to VMs over TLS port 443.
* **Naming Constraint:** Must be named **strictly** `AzureBastionSubnet`.
* **Sizing Requirements:**
  * **Minimum prefix: `/26` (64 IPs, 59 usable)**.
  * *Why `/26` is required:* Azure Bastion v2/v3 architecture supports dynamic autoscaling (from 2 up to 50 scale units to accommodate concurrent administrative sessions). Smaller subnets like `/27` are rejected during Bastion creation.
* **Strict NSG Rules Mandate:**
  * Bastion requires an NSG with mandatory baseline rules:
    - *Inbound:* Allow TCP 443 from `Internet` (for admin browser sessions), TCP 443 from `GatewayManager` (for platform health checks).
    - *Outbound:* Allow TCP 3389/22 to `VirtualNetwork` (to reach target VMs), TCP 443 to `AzureCloud` (for telemetry and storage).
  * **No Custom Default Routing:** A custom UDR redirecting `0.0.0.0/0` away from `Internet` is unsupported and will break the Bastion service.

### 3. `AzureFirewallSubnet` & `AzureFirewallManagementSubnet`:
* **Purpose:** Houses the managed active-active stateful packet inspection instances of Azure Firewall.
* **Naming Constraint:** Must be named **strictly** `AzureFirewallSubnet` (and `AzureFirewallManagementSubnet` when using Forced Tunneling).
* **Sizing Requirements:**
  * **Minimum prefix: `/26` (64 IPs, 59 usable)** for each subnet.
  * *Why `/26` is required:* Azure Firewall dynamically scales out its underlying compute nodes during traffic spikes.
* **Critical Constraint:** Azure Resource Manager actively blocks associating an NSG with `AzureFirewallSubnet`.

### 4. `RouteServerSubnet`:
* **Purpose:** Dedicated to the active-active BGP route engines of **Azure Route Server**.
* **Naming Constraint:** Must be named **strictly** `RouteServerSubnet`.
* **Sizing Requirements:** Minimum `/27`. Cannot contain user VMs or other services.

---

## 🔀 4. Delegated Subnets: PaaS Injection & Network Intent Policies

In modern cloud architecture, managed PaaS services frequently need to inject their backend worker instances directly into your private Virtual Network (e.g., Azure App Service, Azure PostgreSQL Flexible Server, Azure Container Instances). To support this securely, Azure introduces **Subnet Delegation**.

```text
+---------------------------------------------------------------------------------------------------+
|                                  SUBNET DELEGATION ARCHITECTURE                                   |
+---------------------------------------------------------------------------------------------------+
|  Subnet: snet-appservice (10.0.5.0/24)                                                            |
|  Delegation: Microsoft.Web/serverFarms                                                            |
|                                                                                                   |
|  [ Azure App Service Plan ] ────► Injects Private Worker NICs directly into snet-appservice      |
|                                   ├── Accesses internal VMs (10.0.1.4) over private VNet fabric   |
|                                   ├── Reaches Private Endpoints (10.2.1.10) securely              |
|                                   └── Obtains private IP from snet-appservice pool                |
|                                                                                                   |
|  [ Standard Virtual Machine ] ──► ❌ BLOCKED FROM DEPLOYMENT!                                     |
|                                   Subnet is exclusively dedicated to Microsoft.Web/serverFarms    |
+---------------------------------------------------------------------------------------------------+
```

### Delegation Mechanics & Security Guardrails:
1. **Resource Provider Handover:** When a subnet is delegated (e.g., to `Microsoft.Web/serverFarms`), Azure transfers the right to create network interfaces within that subnet to the specified resource provider.
2. **Exclusion of Heterogeneous Workloads:** Once a subnet is delegated, standard virtual machines, independent network interfaces, and unmanaged workloads **cannot be provisioned into that subnet**. The subnet is 100% reserved for the designated PaaS resource type.
3. **Network Intent Policies (NIP):** The delegated resource provider automatically applies Network Intent Policies to the subnet. These policies ensure that the necessary routing rules and port configurations required by the PaaS service cannot be inadvertently severed by customer administrators.
4. **Lifecycle Lock:** A delegated subnet cannot be deleted, modified, or have its address prefix changed while resources belonging to the delegated PaaS service exist within it. The PaaS integration must be unlinked or destroyed before subnet properties can be altered.

### Common Delegation Target Resource Providers:
* `Microsoft.Web/serverFarms` — Azure App Service Regional VNet Integration.
* `Microsoft.DBforPostgreSQL/flexibleServers` — Azure Database for PostgreSQL Flexible Server private networking.
* `Microsoft.ContainerInstance/containerGroups` — Azure Container Instances (ACI) private virtual network deployment.
* `Microsoft.NetApp/volumes` — Azure NetApp Files storage volume mounts.

---

*Read more in [[Reference Notes/13-104-05_administer_virtual_networking.md#stage-2-core-mental-model--component-architecture]]*
