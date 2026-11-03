---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Azure Virtual Networking and Intersite Connectivity]]"
sub_type: mechanics
source_type: gemini-chat
source_url: ""
author: "Antigravity"
course_title: "AZ-104 Masterclass"
tags:
  - azure/networking
  - azure/private-link
  - azure/dns
  - azure/tls
  - azure/deep-dive
  - status/completed
---

# Azure Intersite Connectivity - Private Endpoint Split-Horizon DNS, TLS Certificate Invariants, and CNAME Routing

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Azure Virtual Networking and Intersite Connectivity]] > **Private Endpoint Split-Horizon DNS & TLS Invariants**

---

## 🎯 1. First Principles: Why Direct IP Calls Fail for Cloud PaaS

When an engineer deploys an **Azure Private Endpoint**, Azure assigns an unmanaged virtual network interface (NIC) with a private RFC 1918 IP address (e.g., `10.50.2.15`) directly into their subnet, tunneling traffic to an Azure PaaS service (such as Azure Blob Storage or Azure SQL Database).

A junior engineer's immediate intuition is often to configure client applications to connect directly to that private IP:
```bash
curl https://10.50.2.15/data/financial_records.csv
```

In production, **this call will fail immediately** due to two hard cryptographic and platform constraints:

1. **TLS / SSL Server Name Indication (SNI) Failure:**
   The TLS certificate presented by the Azure Storage cluster is issued to `*.blob.core.windows.net`. It does **not** contain the private IP `10.50.2.15`. When the client’s TLS handshake verifies the server certificate, it throws a fatal validation error:
   ```text
   SSL: Certificate Subject Alternative Name (SAN) mismatch!
   Target IP 10.50.2.15 does not match certificate *.blob.core.windows.net.
   ```
2. **Multi-Tenant Gateway Routing (HTTP Host Header):**
   Azure PaaS gateways host thousands of customer accounts on shared physical frontend clusters. The cluster relies on the HTTP `Host:` header (e.g., `stenterprise.blob.core.windows.net`) to demultiplex the connection to the correct tenant storage container. Connecting to an IP address directly prevents the cluster from identifying the target storage account.

---

## 🏛️ 2. The Solution: The Split-Horizon CNAME Redirection Chain

To preserve valid TLS certificates and multi-tenant HTTP headers while forcing packets to route over the private network, Azure implements a **Split-Horizon DNS Redirection Chain**:

```text
Application Client initiates HTTPS request:
"https://stenterprise.blob.core.windows.net"
                    │
                    ▼
[ STEP 1: Azure Public DNS Resolution ]
- Client queries: "stenterprise.blob.core.windows.net"
- Microsoft authoritative DNS responds with a canonical name (CNAME) record:
  "stenterprise.privatelink.blob.core.windows.net"
                    │
                    ▼
[ STEP 2: Azure Private DNS Interception ]
- Client hypervisor queries the linked Azure Private DNS Zone:
  "privatelink.blob.core.windows.net"
- The zone contains an authoritative 'A' record:
  "stenterprise" ──► 10.50.2.15 (Private Endpoint IP)
                    │
                    ▼
[ STEP 3: The Cryptographically Clean Connection ]
- Client connects to destination IP: 10.50.2.15
- Client TLS SNI header presents: "stenterprise.blob.core.windows.net"
- Result: 
  ✅ SSL Certificate matches!
  ✅ HTTP Host header is correct!
  ✅ Traffic flows 100% privately across the subnet VNet without public internet exposure!
```

---

## 🌐 3. Public Clients vs. Private Clients (Split-Horizon Behavior)

The brilliance of the `privatelink` CNAME architecture is that it cleanly bifurcates public and private consumers without requiring two different application URLs:

| Client Location | DNS Resolution Path | Resulting IP | Network Path |
| :--- | :--- | :--- | :--- |
| **Inside the Azure VNet** | Resolves `privatelink.blob.core.windows.net` via linked **Private DNS Zone**. | **`10.50.2.15`** (Private Endpoint) | **Private VNet SDN tunnel** (Zero internet). |
| **External Internet User** | Resolves `privatelink.blob.core.windows.net` via **Public Internet DNS**. | **`20.150.12.33`** (Public VIP) | **Public Web** *(Rejected if firewall rule blocks public access)*. |

Both clients use the exact same code and connection string:
`https://stenterprise.blob.core.windows.net`

---

## 🔗 4. Private DNS Zone Links: The Registration vs. Resolution Boundary

When connecting Azure Virtual Networks to a Private DNS Zone, Azure enforces strict link quotas:

```text
[ Private DNS Zone: privatelink.blob.core.windows.net ]
                    │
       ┌────────────┴────────────┐
       ▼                         ▼
[ REGISTRATION LINK ]     [ RESOLUTION LINK ]
- Maximum: Exactly 1 VNet - Maximum: Up to 1,000 VNets
- Auto-registers VM names - Resolution ONLY (Queries A records)
```

* **For Private Endpoints:** Private DNS Zones (such as `privatelink.blob.core.windows.net`) should be linked to your Hub and Spoke VNets with **Auto-registration DISABLED** (Resolution Only).
* Private Endpoints create static `A` records manually or via ARM deployment; they do not require dynamic VM registration.

---

*Read more in [[Reference Notes/13-104-06_administer_intersite_connectivity.md#4-azure-private-link--private-endpoints-secure-paas-access]]*
