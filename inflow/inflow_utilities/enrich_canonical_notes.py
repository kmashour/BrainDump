import os

def update_file(file_path, marker, new_section):
    if not os.path.exists(file_path):
        print(f"ERROR: {file_path} does not exist.")
        return False
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "Going the Extra Mile: Architectural Deep Dive" in content:
        print(f"Skipping {file_path}: already enriched.")
        return True
        
    if marker in content:
        updated = content.replace(marker, new_section + "\n\n" + marker)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(updated)
        print(f"SUCCESS: Enriched {file_path}")
        return True
    else:
        print(f"ERROR: Marker '{marker}' not found in {file_path}")
        return False

# ==============================================================================
# 1. MODULE 07: NETWORK TRAFFIC & ADVANCED TRAFFIC ENGINEERING
# ==============================================================================
mod07_path = "Reference Notes/13-104-07_administer_network_traffic.md"
mod07_marker = "## 🌐 Authoritative References & Citations"
mod07_section = """---

## 🚀 Going the Extra Mile: Architectural Deep Dive - Advanced Traffic Engineering

> [!IMPORTANT]
> **Going the Extra Mile:** In this section, we are taking an extra mile on this topic and start deep diving into the foundational SDN packet transformations, bump-in-the-wire NVA chaining with Gateway Load Balancer, Azure Front Door Anycast split-TCP mechanics, and Application Gateway for Containers (ALB) based on John Savill's Azure Deep Dives Master Class.

### 1. Azure Load Balancer Under the Hood: SDN Multiplexing & Outbound SNAT

#### A. SDN Hypervisor-Level Multiplexing (No Physical Appliance)
* **The Non-Terminating Data Path:** Azure Load Balancer is **not** a physical or virtual machine sitting in the data path. It is a distributed Software Defined Network (SDN) component operating at the **SLB (Software Load Balancer) MUX** layer within the Azure host physical hypervisors.
* **Hash Tuple Computation:**
  * **5-Tuple:** Default distribution based on `{Source IP, Source Port, Destination IP, Destination Port, Protocol}`. Every new TCP connection or source port alteration lands on a newly calculated backend target.
  * **2-Tuple (`SourceIP`):** Directs all connections from a specific client IP to the exact same backend node, regardless of destination port.
  * **3-Tuple (`SourceIP, Protocol`):** Ensures all traffic from a client utilizing the same transport protocol reaches the same target.
* **HA Ports (`0` / `*`):** Available exclusively on Internal Standard Load Balancers. By setting Frontend Port to `0`, Protocol to `All`, and Backend Port to `0`, all TCP and UDP packets on all 65,535 ports are forwarded simultaneously. This is the cornerstone topology for active-passive or active-active Network Virtual Appliance (NVA) firewalls.

#### B. Outbound SNAT Port Allocation & Exhaustion Loops
* When backend instances without dedicated instance-level public IPs make outbound Internet requests, the Azure Load Balancer performs **Source Network Address Translation (SNAT)** using the frontend Public IP.
* **Pre-Allocated SNAT Ports:** By default, Azure statically assigns a fixed number of SNAT ports per backend VM based on pool size (e.g., 1,024 ports per VM for small pools).
* **SNAT Exhaustion Failure Loop:** If backend applications initiate rapid, short-lived outbound API connections without connection pooling (e.g., microservice REST calls or database egress), all assigned SNAT ports enter `TIME_WAIT` status. Subsequent outbound connection attempts are silently dropped with TCP handshake timeouts.
* **Remediation Architecture:** Eliminate SNAT allocation limits on the Load Balancer by deploying **Azure NAT Gateway** (`Microsoft.Network/natGateways`) to the subnet, providing 64,512 dynamic, shared SNAT ports per public IP.

---

### 2. Microsoft Azure Gateway Load Balancer (GWLB): Bump-in-the-Wire NVA Chaining

#### A. The NVA Architecture Problem
Historically, routing traffic through third-party Network Virtual Appliances (Palo Alto, Fortinet, Check Point) required complex User Defined Routes (UDRs), multiple network interfaces (Untrust, Trust, Management), source NAT configuration on the firewall to ensure symmetric return paths, and complex active-active clustering.

#### B. The Gateway Load Balancer Solution
Gateway Load Balancer is a specialized SKU of Azure Load Balancer deployed specifically for transparent, inline packet inspection.

```mermaid
flowchart LR
    Client["Client on Internet"] -->|Public Traffic| ExtLB["Standard Public Load Balancer\\n(Consumer Frontend IP)"]
    
    subgraph GWLB_Infra ["Gateway Load Balancer (Provider)"]
        GWLB["Gateway Load Balancer"]
        subgraph NVAPool ["NVA Backend Pool (Scale Set)"]
            NVA1["Firewall Appliance 1\\n(VXLAN Tunnel Endpoint)"]
            NVA2["Firewall Appliance 2\\n(VXLAN Tunnel Endpoint)"]
        end
    end

    subgraph WorkloadPool ["Workload Tier"]
        VM1["Backend App VM 1"]
        VM2["Backend App VM 2"]
    end

    ExtLB == "Chained via\\nGatewayLoadBalancerId" ==> GWLB
    GWLB -->|Encapsulates in VXLAN Tunnel (Port 2001)| NVA1
    NVA1 -->|Inspects, Decapsulates, Returns via VXLAN| GWLB
    GWLB -->|Delivers Clean Original Packet| WorkloadPool
```

* **Chained Architecture:** The consumer's public Load Balancer (or VM public IP) specifies a reference to the Gateway Load Balancer frontend via the `gatewayLoadBalancer` property.
* **VXLAN Tunnel Encapsulation (RFC 7348):**
  * Incoming packets hitting the public IP are **NOT rewritten** (Source IP and Destination IP remain 100% unaltered).
  * The GWLB encapsulates the entire raw IP packet inside a **VXLAN header** (UDP port 2001 or custom) containing a Virtual Network Identifier (VNI).
  * Two separate tunnel interfaces are established between GWLB and the NVA:
    1. **Internal Tunnel:** Transports traffic between GWLB and NVA.
    2. **External Tunnel:** Transports inspected return traffic.
* **Zero UDR Egress / Ingress:** The NVA inspects the payload and sends it right back over the VXLAN tunnel to the GWLB, which decapsulates the packet and delivers it directly to the target application VM. Routing tables require zero custom routes.

---

### 3. Microsoft Azure Front Door (AFD): Anycast Routing & Split-TCP Acceleration

Azure Front Door is Microsoft's global, modern cloud content delivery network (CDN) and Layer 7 edge routing platform operating across hundreds of Global Points of Presence (Edge POPs).

#### A. Split-TCP & Anycast BGP Acceleration
* **Anycast IP Distribution:** A single Anycast public VIP is advertised via BGP globally across all Microsoft edge locations. The client's DNS query resolves to the same Anycast IP, but BGP routes the client to the physically nearest edge point of presence (POP).
* **The Split-TCP Advantage:**
  * Rather than establishing a slow 3-way TCP handshake across the Atlantic/Pacific oceans directly to the Azure Region (150ms+ RTT), the client establishes the TCP connection and TLS handshake with the local Edge POP (5–10ms RTT).
  * Front Door then reuses warm, long-lived multiplexed TCP connections across the private Microsoft dark fiber backbone to the backend origin in the target Azure region.
  * This cuts round-trip negotiation latency by up to 75% for dynamic web content.

#### B. Private Link Origin Integration
In enterprise zero-trust postures, Front Door eliminates the requirement to expose backend web apps or internal load balancers to the public internet:
* Front Door Premium connects directly to the backend origin (App Service, Internal Load Balancer, or Container App) over an **Azure Private Endpoint** using Private Link.
* The backend firewall completely forbids public Internet ingress, accepting traffic exclusively from Microsoft's internal Front Door infrastructure tenant.

---

### 4. Application Gateway for Containers (ALB): The Next-Gen Kubernetes Ingress

John Savill highlights Microsoft's newly architected **Application Gateway for Containers (ALB)**, replacing the legacy AGIC (Application Gateway Ingress Controller):
* **Control Plane vs. Data Plane Decoupling:**
  * In legacy AGIC, changes to Kubernetes Ingress or Gateway API CRDs triggered slow ARM REST calls to update the monolithic Application Gateway v2 (causing 1–3 minute update latencies).
  * In Application Gateway for Containers, an in-cluster ALB Operator streams real-time updates directly to the distributed data-plane proxies via gRPC, achieving **sub-second route convergence**.
* **Traffic Management:** Supports Gateway API standards, weighted canary routing, header manipulation, and TLS termination with line-of-sight private pod IP routing without kube-proxy SNAT overhead.
"""

update_file(mod07_path, mod07_marker, mod07_section)


# ==============================================================================
# 2. MODULE 02: IDENTITY & ENTRA ID
# ==============================================================================
mod02_path = "Reference Notes/13-104-02_administer_identity.md"
mod02_marker = "## 🌐 Authoritative References & Citations"
mod02_section = """---

## 🚀 Going the Extra Mile: Architectural Deep Dive - Advanced Entra ID Security & Resiliency

> [!IMPORTANT]
> **Going the Extra Mile:** In this section, we are taking an extra mile on this topic and start deep diving into the foundational security protocols, token lifecycles, cross-tenant boundary federation, Continuous Access Evaluation (CAE), and multi-cloud CIEM based on John Savill's Azure Deep Dives Master Class.

### 1. Microsoft Entra Privileged Identity Management (PIM)
* **Zero Permanent Standing Privileges:** Eliminates the vulnerability of having permanent Global Administrators or Subscription Owners. Users are configured as **Eligible** rather than **Active**.
* **Just-In-Time (JIT) Activation Engine:**
  * Requires explicit activation via the portal, CLI, or Microsoft Graph API.
  * Enforces mandatory **MFA re-authentication**, ticket numbering/business justification, and optional multi-stage managerial approval.
  * Time-bounded duration (e.g., maximum 4 to 8 hours), after which Entra automatically revokes the role assignment without administrator intervention.
* **Access Reviews & Blast-Radius Auditing:** Automated periodic re-certification workflows demanding resource owners to approve or revoke continuing role eligibility.

---

### 2. Entra ID Token Resiliency & Continuous Access Evaluation (CAE)
Historically, OAuth access tokens had a static 60-minute lifespan. If an employee was terminated or compromised 2 minutes into an active session, they could continue accessing data until the token expired.

```mermaid
flowchart TD
    Client["Client App (Teams / Outlook / Browser)"]
    STS["Entra ID Security Token Service (STS)"]
    Service["Resource Provider (Exchange / SharePoint / ARM)"]

    Client -->|1. Presents Valid PRT / CAE Token| Service
    Service -->|2. Grants Access Immediately| Client
    
    subgraph CriticalEvents ["Critical Security Events (Real-Time)"]
        E1["User Account Disabled or Deleted"]
        E2["Password Changed or Reset"]
        E3["MFA Enforced on User"]
        E4["High User Risk Detected by Identity Protection"]
        E5["Client IP Moves Outside Trusted IP Range"]
    end

    CriticalEvents -.->|Push Real-Time Revocation Event| Service
    Service -->|3. Event Interception: Rejects Token| Client
    Client -->|4. Directed Back for Fresh Auth| STS
```

* **Continuous Access Evaluation (CAE - RFC 8693):**
  * Microsoft Entra ID and supporting Microsoft 365 / Azure Resource Manager APIs communicate bidirectionally.
  * When a critical event occurs (User account disabled, password changed, high user risk detected, or user leaves a trusted IP range), the resource provider terminates the session **in real-time (sub-second)**, overriding the unexpired access token.

---

### 3. Microsoft Entra Identity Protection & Risk Engine
* **User Risk (Identity Posture):** Calculated asynchronously / offline by scanning the dark web, compromised credential feeds, and cross-enterprise attack patterns. Represents the probability that the identity's credentials have been leaked.
* **Sign-In Risk (Session Context):** Calculated in real-time during authentication. Factors include anonymous IP (Tor browser), unfamiliar sign-in properties, atypical travel speed (impossible velocity, e.g., logging in from New York and 10 minutes later from Tokyo), and malware-linked IP addresses.
* **Risk-Based Conditional Access Policies:**
  * *High Sign-In Risk:* Enforce step-up Multi-Factor Authentication.
  * *High User Risk:* Enforce secure password reset requiring self-service identity verification.

---

### 4. Cross-Tenant Access Settings & B2B Direct Connect
* **Inbound & Outbound Trust Boundaries:** Allows organizations to define granular trust relationships with specific external Entra ID tenants.
* **MFA and Compliance Trust:** Organizations can check `Trust multi-factor authentication from external Microsoft Entra tenants` and `Trust compliant devices`. When a partner engineer signs in, Azure accepts their home tenant's MFA claim rather than forcing them to register a second authenticator in the host tenant.
* **B2B Direct Connect (Teams Shared Channels):** Establishes mutual federated trust without provisioning guest user objects (`#EXT#`) in the host directory, enabling seamless cross-organization collaboration.

---

### 5. Microsoft Entra Application Proxy: Secure Hybrid Access
* **Architecture:** Provides secure remote access to on-premises legacy web applications (HTTP/HTTPS, Kerberos) without opening inbound firewall ports or deploying a perimeter DMZ reverse proxy.
* **Outbound-Only Connectors:** Lightweight connectors installed on-premises initiate **outbound-only HTTPS connections (port 443)** to the Entra Application Proxy cloud service.
* **Single Sign-On (SSO):** Pre-authenticates the user in the cloud using Entra ID (MFA, Conditional Access), converts the cloud SAML/OIDC claim into a local Kerberos ticket via **Kerberos Constrained Delegation (KCD)**, and forwards the request securely to internal IIS / Apache servers.

---

### 6. Cloud Infrastructure Entitlement Management (CIEM): Entra Permissions Management
* **Multi-Cloud Permission Sprawl:** Organizations running across Azure, AWS, and GCP face immense security debt from over-permissioned service principals, roles, and users.
* **Permission Creep Index (PCI):** Quantifies risk on a scale of 0 to 100 based on the gap between permissions granted and permissions actually exercised over 90 days.
* **Automated Least Privilege:** Identifies unused administrative privileges and generates right-sized role definitions to shrink the multi-cloud attack surface.
"""

update_file(mod02_path, mod02_marker, mod02_section)


# ==============================================================================
# 3. MODULE 06: INTERSITE CONNECTIVITY & HYBRID NETWORKING
# ==============================================================================
mod06_path = "Reference Notes/13-104-06_administer_intersite_connectivity.md"
mod06_marker = "## 🌐 Authoritative References & Citations"
mod06_section = """---

## 🚀 Going the Extra Mile: Architectural Deep Dive - Enterprise Hybrid & Core Connectivity

> [!IMPORTANT]
> **Going the Extra Mile:** In this section, we are taking an extra mile on this topic and start deep diving into the under-the-hood packet flow of ExpressRoute FastPath, Azure Virtual Network Manager (AVNM) Security Admin Rules, Private Link TCP proxy v2 mechanics, and Azure Firewall deep inspection based on John Savill's Azure Deep Dives Master Class.

### 1. ExpressRoute Deep Dive: Architecture, Peering & FastPath

#### A. The Physical Interconnect Architecture
ExpressRoute provides dedicated, private optical connectivity to Microsoft Cloud services without traversing the public internet.

```mermaid
flowchart LR
    OnPrem["Enterprise On-Premises Datacenter\n(Customer Edge - CE Routers)"]
    MeetMe["Carrier Meet-Me Location\n(Colocation / Exchange Provider)"]
    MSEE["Microsoft Enterprise Edge Routers\n(MSEE)"]
    AzureBackbone["Microsoft Global Optical Backbone"]
    
    OnPrem -->|Private Leased Line / MPLS| MeetMe
    MeetMe -->|Cross-Connect Optical Patch| MSEE
    MSEE --> AzureBackbone
```

* **Meet-Me Exchange:** Connectivity is terminated at a carrier colocation facility (Equinix, Megaport, AT&T) onto redundant **Microsoft Enterprise Edge (MSEE)** routers.
* **Peering Models:**
  * **Private Peering:** Connects on-premises directly to private VNets (RFC 1918 space). Requires an Azure Virtual Network Gateway (`VpnGw` or `ErGw`).
  * **Microsoft Peering:** Connects to Microsoft public PaaS services (Storage, SQL, Cosmos DB) and Microsoft 365 over private BGP route filters using registered public ASNs.

#### B. ExpressRoute FastPath: Bypassing the Gateway CPU Bottleneck
* **The Traditional Bottleneck:** In standard ExpressRoute setups, every packet between on-premises and an Azure VM must traverse the Virtual Network Gateway compute instances, which caps maximum throughput to 10 Gbps (`ErGw3AZ`) and adds serialization latency.
* **The FastPath Optimization:** FastPath configures the MSEE routers to inject routes directly into the Azure physical hypervisors hosting the workload VMs.
* **Data Path:** Packets flow directly from MSEE to the VM hypervisor network interface, **completely bypassing the gateway CPU**, achieving up to 100 Gbps line-rate throughput with microsecond latency.

---

### 2. Azure Virtual Network Manager (AVNM): Enterprise Scale Mesh & Security Enforcement

At enterprise scale with hundreds of subscriptions and VNets, managing manual peering connections and decentralized NSGs becomes unmanageable.

#### A. Automated Connectivity Topologies
* **Network Groups:** Dynamic collections of VNets aggregated via Azure Resource Graph queries (e.g., all VNets with tag `Environment = Production`).
* **Hub-and-Spoke Automation:** Automatically establishes and tears down peering links, Gateway Transit, and direct spoke-to-spoke connectivity without manual script orchestration.
* **Global Mesh:** With a single configuration click, AVNM configures full-mesh peering across all member VNets within or across Azure regions.

#### B. Security Admin Rules (SAR) vs. Network Security Groups (NSG)
AVNM introduces a new administrative security layer that executes **before** local subnet NSGs:

```text
[Inbound Packet]
       │
       ▼
[AVNM Security Admin Rules (SAR)]  <── Enforced by Central Cloud SecOps Team
       │
       ├── Match: Action = "Deny"   ──► DROPPED IMMEDIATELY (Local NSG cannot allow!)
       ├── Match: Action = "Allow"  ──► ALLOWED DIRECTLY (Bypasses lower NSG rules)
       └── Match: Action = "Pass"   ──► Passes down to lower layers
               │
               ▼
[Subnet Network Security Group (NSG)]  <── Managed by Application Team
               │
               ▼
[NIC Network Security Group (NSG)]
               │
               ▼
[Virtual Machine Workload]
```

* **The Guardrail Advantage:** A centralized security administrator can deploy a Security Admin Rule denying inbound SSH (Port 22) from the internet across all 500 company VNets. Even if a local project team creates an NSG rule with priority `100` allowing port 22, the SAR intercepts and drops the packet.

---

### 3. Microsoft Azure Private Link: Under the Hood

Private Link enables private access to Azure PaaS services, customer-owned services, or third-party Marketplace SaaS:
* **The Private Endpoint:** An unmanaged Virtual Network Interface (NIC) allocated directly inside your private subnet with a private IPv4 address.
* **Private Link Service (Provider Plane):** The service owner provisions a Standard Internal Load Balancer in front of their backend workloads and binds it to a Private Link Service.
* **TCP Proxy v2 Header (Preserving Client IP):**
  * When client traffic enters a Private Endpoint, the Private Link software switch performs **Source NAT** to a private IP from the provider's subnet.
  * To prevent the backend service from losing the client's original identity, Private Link encapsulates the client's actual Source IP and Source Port inside a **Proxy Protocol v2 header** prepended to the TCP packet.

---

### 4. Azure Firewall Deep-Dive: Enterprise Inspection Engine
* **TLS Inspection (Premium SKU):** Performs complete SSL/TLS decryption and re-encryption. Azure Firewall acts as an intermediate Certificate Authority (using enterprise root certificates in Key Vault), decrypting outbound traffic to inspect cleartext payloads for malware signatures.
* **Intrusion Detection and Prevention System (IDPS):** Signature-based deep packet inspection monitoring exploit attempts across thousands of CVE vulnerabilities in real time.
* **DNS Proxy & FQDN Filtering:** Listens as a local DNS resolver on the VNet, forwarding queries to Azure DNS or custom resolvers while intercepting malicious domain name lookups before network egress occurs.
"""

update_file(mod06_path, mod06_marker, mod06_section)


# ==============================================================================
# 4. MODULE 08: STORAGE ACCOUNTS & ADVANCED DATA FABRICS
# ==============================================================================
mod08_path = "Reference Notes/13-104-08_administer_azure_storage.md"
mod08_marker = "## 🌐 Authoritative References & Citations"
mod08_section = """---

## 🚀 Going the Extra Mile: Architectural Deep Dive - Enterprise Storage Fabrics

> [!IMPORTANT]
> **Going the Extra Mile:** In this section, we are taking an extra mile on this topic and start deep diving into the cloud-native iSCSI block storage fabric of Azure Elastic SAN, granular POSIX permissions in ADLS Gen2, and cryptographic immutability with Azure Confidential Ledger based on John Savill's Azure Deep Dives Master Class.

### 1. Azure Elastic SAN: Cloud-Native Block Storage Area Network

High-performance clustered workloads (SQL Server Failover Clusters, Oracle DB, SAP HANA, Azure VMware Solution) traditionally required running complex virtual SAN appliances or provisioning dozens of expensive Ultra Disks.

```mermaid
flowchart TD
    subgraph ComputeClients ["Compute Clients"]
        VM1["Clustered SQL Node 1"]
        VM2["Clustered SQL Node 2"]
        AVS["Azure VMware Solution (ESXi Hosts)"]
        AKS["AKS Worker Nodes (StatefulSets)"]
    end

    subgraph ElasticSAN ["Azure Elastic SAN Resource Group"]
        subgraph SanVolumeGroup ["Elastic SAN Volume Group (Encryption, Network Rules)"]
            Vol1["Volume 1: sql-data-01 (iSCSI Target)"]
            Vol2["Volume 2: sql-log-01 (iSCSI Target)"]
            Vol3["Volume 3: vmware-datastore (iSCSI Target)"]
        end
        BaseSAN["Base SAN Provisioned Capacity (e.g., 100 TB, 50,000 IOPS, 800 MB/s)"]
    end

    VM1 ==>|iSCSI Protocol over Private VNet| Vol1
    VM2 ==>|iSCSI Protocol over Private VNet| Vol1
    AVS ==>|iSCSI VMFS Datastore| Vol3
    AKS ==>|Container Storage Interface CSI| Vol2
```

#### A. Core Architectural Differentiators
* **Native iSCSI Block Storage:** Unlike Azure Files (SMB/NFS) or Blob storage (REST), Elastic SAN exposes pure block-level **iSCSI targets** directly over the Azure VNet fabric.
* **Shared Storage Clustering:** Multiple independent virtual machines or ESXi hosts can attach to the same volume concurrently with SCSI-3 persistent reservations, enabling true clustered shared volumes.
* **Elastic Pool Economics:** Capacity and performance (IOPS and throughput) are pooled across the entire SAN rather than provisioned per individual disk. You scale the base SAN, and dozens of volumes share the underlying IOPS burst capacity.

---

### 2. Azure Blob Data Permissions Deep Dive: Control Plane vs. Data Plane

A frequent source of enterprise cloud outages and data exfiltration stems from conflating the Azure control plane with the storage data plane:

| Access Method | Protocol / Mechanism | Scope & Boundary | Security Posture |
| :--- | :--- | :--- | :--- |
| **Storage Account Access Keys** | Master symmetric 512-bit HMAC shared secret. | Grants full, unrestricted root superuser access across ALL services (Blob, File, Queue, Table). | **High Risk:** Keys bypass RBAC and lack audit identity logging. Must be disabled (`allowSharedKeyAccess: false`). |
| **Service SAS Token** | Signed with Storage Account Key. | Scoped to a specific service and container; valid for hours/days. | Medium Risk: If leaked, valid until expiration timestamp. |
| **User Delegation SAS Token** | Signed using an Entra ID user/managed identity OAuth token. | Scoped strictly to blob containers; maximum lifetime capped at 7 days. | **Enterprise Standard:** Revocable immediately by revoking the user's Entra credentials. |
| **Azure RBAC Data Roles** | Direct Entra ID role assignment (`Storage Blob Data Contributor`). | Scoped at Subscription, Resource Group, Account, or Container. | **Recommended:** Fully audited in Azure Monitor and integrated with Conditional Access. |
| **POSIX ACLs (ADLS Gen2)** | Read/Write/Execute permissions applied to specific directories and files. | Evaluated directly inside the Hierarchical Namespace. | Essential for big data (Synapse, Databricks) granular directory access. |

---

### 3. Azure Confidential Ledger: Cryptographic Tamper-Proof Immutability

For mission-critical audit trails, financial transactions, and regulatory compliance logs, standard storage accounts with WORM policies can still be vulnerable to administrative tenant destruction.

#### A. Hardware Enclave Security (AMD SEV-SNP / Intel SGX)
* Azure Confidential Ledger runs exclusively inside hardware-enforced **Confidential Computing Enclaves**.
* Memory encryption ensures that neither cloud administrators, hypervisor hosts, nor compromised subscription Owners can inspect or alter data residing in memory.

#### B. Confidential Consortium Framework (CCF)
* Powered by an open-source decentralized ledger governance engine.
* Every transaction produces a cryptographic receipt containing a **Merkle tree root hash proof**.
* Any third-party auditor can cryptographically prove that the ledger history has not been altered, deleted, or rolled back since inception.
"""

update_file(mod08_path, mod08_marker, mod08_section)


# ==============================================================================
# 5. MODULE 09: VIRTUAL MACHINES & ADVANCED COMPUTE
# ==============================================================================
mod09_path = "Reference Notes/13-104-09_administer_azure_virtual_machines.md"
mod09_marker = "## 🌐 Authoritative References & Citations"
mod09_section = """---

## 🚀 Going the Extra Mile: Architectural Deep Dive - Enterprise Compute & Hybrid VMware

> [!IMPORTANT]
> **Going the Extra Mile:** In this section, we are taking an extra mile on this topic and start deep diving into the physical storage abstractions of Azure Managed Disks (bursting, Premium v2, shared disks) and the bare-metal virtualization fabric of Azure VMware Solution (AVS) based on John Savill's Azure Deep Dives Master Class.

### 1. Azure Managed Disks Under the Hood: Tiers, Bursting & Shared Disks

#### A. Storage Fabric Architecture
* Managed Disks are not physical hard drives sitting inside the server chassis running your VM. They are virtualized block abstractions backed by **Azure Blob Storage page blobs** Triple-replicated within the datacenter (LRS) or across availability zones (ZRS).
* The physical hypervisor communicates with the storage cluster over high-speed redundant 40/100 Gbps network fabrics.

#### B. Premium SSD v1 vs. Premium SSD v2 vs. Ultra Disk
* **Premium SSD v1:** Disk performance (IOPS and throughput) is strictly coupled to disk capacity (e.g., a P30 1TB disk gives 5,000 IOPS and 200 MB/s). If an application requires 15,000 IOPS, you must provision an expensive 4TB P50 disk even if you only need 200 GB of data.
* **Premium SSD v2:** Decouples capacity from performance! You can provision a 100 GB disk with 20,000 IOPS and 600 MB/s throughput, paying independently for size, IOPS, and MB/s.
* **Ultra Disk:** The lowest-latency tier (sub-millisecond), dynamically tunable on-the-fly without detaching the disk or rebooting the VM.

#### C. Credit-Based vs. On-Demand Bursting
* **Credit-Based Bursting:** Small disks (P1 to P20) accumulate burst credits when running below their baseline IOPS limit. During workload spikes (booting OS or loading batch jobs), disks can burst up to 3,500 IOPS and 170 MB/s for up to 30 minutes.
* **On-Demand Bursting:** For unpredictable production workloads, enables continuous bursting up to 30,000 IOPS, billed on a per-burst-transaction model to guarantee zero I/O throttling.

#### D. Azure Shared Disks for Enterprise Clustering
* Attaches a single Managed Disk (Premium SSD or Ultra Disk) to multiple virtual machines concurrently.
* Utilizes **SCSI-3 Persistent Reservations (SCSI PR)**, allowing multi-node clusters (SQL Server Failover Cluster Instances, SAP ASCS) to arbitrate node fencing without software replication overhead.

---

### 2. Azure VMware Solution (AVS): Bare-Metal Hybrid Cloud

Enterprise workloads deeply entrenched in VMware ecosystems (vSphere, vCenter, vSAN, NSX-T) cannot always be rapidly containerized or converted to Azure VMs.

```mermaid
flowchart LR
    subgraph OnPrem ["On-Premises Datacenter"]
        vSphereOnPrem["vSphere Workloads"]
        HCX["VMware HCX (Hybrid Cloud Extension)"]
    end

    subgraph AVS_Cloud ["Azure Datacenter: Azure VMware Solution (AVS) Private Cloud"]
        subgraph BareMetal ["Dedicated Bare-Metal Hosts (Zero Hyper-V)"]
            ESXi1["ESXi Node 1"]
            ESXi2["ESXi Node 2"]
            ESXi3["ESXi Node 3 (Minimum 3 Nodes)"]
        end
        vSAN["All-Flash NVMe vSAN Storage"]
        NSX["NSX-T Software Defined Networking"]
    end

    subgraph NativeAzure ["Native Azure Ecosystem"]
        VNet["Azure Native Virtual Network"]
        Services["Native Azure Services (Blob, SQL, Entra ID)"]
    end

    HCX ==>|ExpressRoute Dedicated Circuits| NSX
    NSX ==>|Ultra-Low Latency ExpressRoute FastPath| VNet
    VNet --- Services
```

* **Zero Hypervisor Emulation:** Microsoft deploys dedicated, bare-metal physical servers inside Azure datacenters running VMware ESXi directly (zero Hyper-V nested virtualization).
* **VMware HCX Seamless Migration:** Enables live **vMotion** of running workloads from on-premises datacenters into Azure over dedicated ExpressRoute interconnects with zero application downtime.
* **Unified Management:** Systems engineers manage clusters using native vCenter Server, while Azure operations manage lifecycle, hardware replacement, and vSphere version upgrades.
"""

update_file(mod09_path, mod09_marker, mod09_section)


# ==============================================================================
# 6. MODULE 10: PAAS COMPUTE & CONTAINERS
# ==============================================================================
mod10_path = "Reference Notes/13-104-10_administer_paas_compute_options.md"
mod10_marker = "## 🌐 Authoritative References & Citations"
mod10_section = """---

## 🚀 Going the Extra Mile: Architectural Deep Dive - Container Networking, GenAI & Hyperscale Data

> [!IMPORTANT]
> **Going the Extra Mile:** In this section, we are taking an extra mile on this topic and start deep diving into the foundational networking models of Azure Kubernetes Service (AKS), Azure API Management Generative AI Gateways, and Azure SQL Hyperscale storage separation based on John Savill's Azure Deep Dives Master Class.

### 1. Azure Kubernetes Service (AKS) Networking Deep Dive

Choosing the correct CNI (Container Network Interface) plugins governs pod scalability, subnet sizing, and throughput:

| Network Model | IP Address Allocation | Pod IP Accessibility | Scalability Limits | Performance Profile |
| :--- | :--- | :--- | :--- | :--- |
| **Kubenet** | Pods receive private overlay IPs from a virtual CIDR (`10.244.0.0/16`). | Pods are not directly routable from outside the node. Node performs SNAT. | Limited by UDR route table limits (maximum 400 nodes). | Slight CPU overhead from iptables NAT forwarding. |
| **Azure CNI (Traditional)** | Every Pod receives a real, routable IP directly from the VNet subnet. | Directly accessible across VNet and on-premises without NAT. | **High VNet IP exhaustion:** Requires allocating 30–110 VNet IPs per node upfront. | Native line-rate hypervisor throughput. |
| **Azure CNI Overlay** | Nodes receive VNet IPs; Pods receive IPs from a private secondary CIDR overlay. | Pods can route across the entire AKS cluster and VNet via Geneve encapsulation. | **Virtually infinite scale:** Resolves VNet IP exhaustion while maintaining cloud routing. | High-speed encapsulation. |
| **Azure CNI Powered by Cilium** | Replaces Linux `iptables` and `kube-proxy` with **eBPF** (Extended Berkeley Packet Filter) in the Linux kernel. | Native IP routing with kernel-level packet inspection. | Extreme scale (thousands of pods and services). | **Ultra-high throughput:** Bypasses linear iptables rule evaluation; provides native WireGuard node-to-node encryption. |

---

### 2. Azure API Management (APIM): Enterprise API & Generative AI Gateway

APIM serves as the front door for backend microservices, serverless functions, and enterprise AI models:

```mermaid
flowchart LR
    Client["Client App / Web Frontend"] -->|HTTPS Inbound| APIM_Gateway["Azure API Management Gateway"]
    
    subgraph APIM_Policies ["Policy Processing Pipeline"]
        P1["1. Inbound: JWT Token Validation & Rate Limiting"]
        P2["2. GenAI Token Throttling & Semantic Cache"]
        P3["3. Backend: Dynamic Routing & Failover Pool"]
        P4["4. Outbound: Header Stripping & Telemetry Log"]
    end

    subgraph BackendOrigins ["Backend Origins"]
        AOAI_East["Azure OpenAI (East US)\nStatus: 429 Throttle"]
        AOAI_West["Azure OpenAI (West US)\nStatus: Healthy (200 OK)"]
        AKS_Svc["Internal AKS Microservice"]
    end

    APIM_Gateway --> P1
    P1 --> P2
    P2 --> P3
    P3 -->|Detects 429 Throttle| AOAI_East
    P3 -->|Smart Failover Retry| AOAI_West
    P3 --> AKS_Svc
```

#### A. APIM Generative AI Gateway Capabilities
* **Model Load Balancing & Smart Fallback:** When distributing workloads across Azure OpenAI service instances, APIM intercepts HTTP 429 (Rate Limit Exceeded) responses and automatically retries requests against secondary regional deployments.
* **Semantic Caching:** Integrates with Azure Managed Redis to cache embeddings and common model completions, eliminating redundant token costs and slashing inference latency.
* **Token Quota Consumption:** Enforces fine-grained token-based rate limits (e.g., maximum 50,000 tokens per minute per consumer subscription key) rather than primitive HTTP call counting.

---

### 3. Azure SQL Hyperscale: Architectural Storage Decoupling

Traditional relational databases tie storage capacity directly to compute node disks, limiting maximum database size and forcing long restoration windows.

#### A. Separation of Compute and Storage
* **Compute Nodes (Stateless):** Run the SQL database engine query processor. Compute nodes can scale up or scale out (adding read replicas) in minutes without moving data.
* **Log Service (Low-Latency WAL):** A high-throughput, low-latency transaction log engine that persists Write-Ahead Logs (WAL) across redundant storage rings.
* **Page Servers (Distributed Cache):** Multi-tiered distributed caching nodes that maintain the database pages. Each Page Server manages a slice of database data and caches hot pages on high-speed local NVMe SSDs (RBPEX cache).
* **Azure Storage Blobs (Infinite Storage):** Cold data pages reside in durable Azure Blob storage, allowing databases to grow seamlessly up to 100+ Terabytes with near-instantaneous backups and restores regardless of database size.
"""

update_file(mod10_path, mod10_marker, mod10_section)


# ==============================================================================
# 7. MODULE 01: GOVERNANCE, FINOPS & TOOLING
# ==============================================================================
mod01_path = "Reference Notes/13-104-01_course_introduction_and_certification.md"
mod01_marker = "## 🌐 Authoritative References & Citations"
mod01_section = """---

## 🚀 Going the Extra Mile: Architectural Deep Dive - Cloud FinOps & Administrator Tooling

> [!IMPORTANT]
> **Going the Extra Mile:** In this section, we are taking an extra mile on this topic and start deep diving into the financial mechanics of Azure Reservations, Spot VM eviction probability algorithms, orphaned cloud asset discovery, and WSL2 virtualization internals based on John Savill's Azure Deep Dives Master Class.

### 1. Azure Cost Optimization Deep Dive: Enterprise FinOps Disciplines

Cost optimization in Azure is not a one-time exercise; it is a continuous operational discipline balancing commitments, spot elasticity, and waste elimination.

#### A. Reservations vs. Azure Savings Plans for Compute
* **Azure Reserved Instances (RIs):** Requires committing to a specific VM size series within a single region (e.g., `Dsv5-series` in `East US`) for 1 or 3 years. Provides up to 72% cost reduction. Best for steady-state databases and static workloads.
* **Azure Savings Plans for Compute:** A more flexible, dollar-per-hour commitment across compute types (e.g., committing to spend $20/hour across VMs, App Services, and Container Apps across any global region). Provides up to 65% cost reduction. Ideal for dynamic, evolving containerized environments.

#### B. Spot VM Eviction Mechanics
* Spot instances allow purchasing surplus Azure compute capacity at discounts of up to 90%.
* **Eviction Policies:**
  * *Capacity-only:* The VM is evicted solely when Azure requires physical hardware capacity back for full-price customers.
  * *Price or Capacity:* The VM is evicted if capacity is needed OR if the spot market price rises above the customer's maximum configured bid.
* **Eviction Notice:** Azure broadcasts a 30-second pre-eviction signal via the Azure Instance Metadata Service (IMDS) at `http://169.254.169.254/metadata/scheduledevents`. Workload automation scripts can trap this event and cleanly drain traffic or persist state before termination.

#### C. Hunting Orphaned Cloud Waste
* **Unattached Managed Disks:** When a VM is deleted, its OS and Data disks remain in the resource group, continuing to bill full monthly capacity.
* **Disassociated Public IPs:** Standard Public IPs bill hourly whether attached to a running resource or sitting idle.
* **Orphaned Network Interfaces (NICs):** Virtual NICs left behind after VM deletion retain IP configurations and NSG associations.
* **Empty App Service Plans:** An App Service Plan bills for the underlying dedicated VM instances 24/7 even if zero web applications are deployed to it.

---

### 2. Administrator Workstation Tooling: WSL2 Architecture

John Savill emphasizes that modern Azure administration requires a unified multi-OS tooling environment:
* **WSL2 Virtualization Model:** Unlike WSL1 (which translated Linux system calls to Windows NT kernel calls), WSL2 runs a true, complete Linux kernel inside a lightweight, managed Hyper-V utility virtual machine.
* **Systemd Integration:** Enables running standard Linux background daemons (Docker engine, Podman, SSH agents) natively within the Windows desktop without third-party desktop wrappers.
* **Cross-OS File System Performance:** Best practice requires placing code repositories and Bicep projects inside the Linux file system (`/home/user/`) rather than the mounted Windows drive (`/mnt/c/`) to avoid cross-OS serialization overhead.
"""

update_file(mod01_path, mod01_marker, mod01_section)


# ==============================================================================
# 8. MODULE 03: GOVERNANCE, RBAC & KEY MANAGEMENT
# ==============================================================================
mod03_path = "Reference Notes/13-104-03_administer_governance_and_compliance.md"
mod03_marker = "## 🌐 Authoritative References & Citations"
mod03_section = """---

## 🚀 Going the Extra Mile: Architectural Deep Dive - Least Privilege, Key Vault & Multi-Cloud Posture

> [!IMPORTANT]
> **Going the Extra Mile:** In this section, we are taking an extra mile on this topic and start deep diving into the underlying schema mechanics of Azure RBAC, Hardware Security Module (HSM) key boundaries in Azure Key Vault, and multi-cloud security governance via Defender for Cloud based on John Savill's Azure Deep Dives Master Class.

### 1. Azure RBAC Under the Hood: The Action vs. NotAction Reality

A critical architectural pitfall in Azure authorization is misunderstanding the `notActions` block in custom role definitions:

```json
{
  "Name": "Custom Operator",
  "IsCustom": true,
  "Actions": [
    "Microsoft.Compute/*"
  ],
  "NotActions": [
    "Microsoft.Compute/virtualMachines/delete"
  ],
  "AssignableScopes": [
    "/subscriptions/00000000-0000-0000-0000-000000000000"
  ]
}
```

* **The NotActions Trap:** `NotActions` is **NOT a Deny rule!** It is strictly an exclusion mechanism from the `Actions` array:
  $$\text{Effective Permissions} = \text{Actions} - \text{NotActions}$$
* If the user is assigned another role (such as Contributor) that includes `Microsoft.Compute/virtualMachines/delete`, the user **CAN delete the VM**. Azure RBAC is strictly additive; allow permissions always win across role assignments.
* **True Deny Assignments:** Deny assignments can only be created by Microsoft internal systems (such as Azure Blueprints or Azure Deployment Stacks) and strictly override any grant.

---

### 2. Azure Key Vault Deep Dive: HSMs, Secrets & RBAC Boundaries

#### A. Storage Types & Security Boundaries
* **Standard Key Vault (Software-Protected):** Cryptographic keys are protected using software algorithms inside multi-tenant hardware. FIPS 140-2 Level 2 validated.
* **Premium Key Vault & Managed HSM:** Cryptographic operations execute inside dedicated, FIPS 140-2 Level 3 validated Hardware Security Modules (HSMs). Keys cannot be extracted in plaintext under any circumstances.

#### B. Access Policies vs. Azure RBAC for Key Vault
* **Legacy Key Vault Access Policies:** Flat, all-or-nothing permissions configured on the vault itself. If a user is granted "Get Secrets", they can read **every single secret** in the vault.
* **Azure RBAC for Key Vault (Recommended):** Enables assigning fine-grained roles (`Key Vault Secrets User`, `Key Vault Crypto Officer`) at the scope of an **individual secret, key, or certificate**, establishing true least privilege.

---

### 3. Microsoft Defender for Multi-Cloud Governance (AWS & GCP)

Enterprise governance frequently extends beyond Azure subscriptions:
* **Multi-Cloud Connectors:** Connects to AWS accounts and Google Cloud projects using native IAM federation (OIDC) without long-lived secret access keys.
* **Cloud Security Posture Management (CSPM):** Audits AWS IAM policies, S3 bucket public access, and GCP service account keys against unified regulatory standards (CIS Benchmark, NIST SP 800-53, ISO 27001).
"""

update_file(mod03_path, mod03_marker, mod03_section)

print("Enrichment run complete!")
