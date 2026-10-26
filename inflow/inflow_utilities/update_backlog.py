import os

inflow_dir = "inflow/AZ-104-JohnSavill-DeepDives"
files = sorted([f for f in os.listdir(inflow_dir) if f.endswith(".md")])

lines = [
    "## [2026-10-21] - Ingestion & Deep-Dive Enrichment: John Savill Azure Deep Dives Master Class (33 Lectures)\n\n",
    "### 📥 Inflow Extraction & Preservation\n",
    "- **Source Playlist:** [John Savill's Azure Deep Dives Playlist](https://www.youtube.com/playlist?list=PLlVtbbG169nGekKEV-l3TOXDLLEAj8jU2)\n",
    "- **Catalog:** 33 architectural deep-dive lectures on core infrastructure, advanced networking, security, data platforms, and multi-cloud governance.\n",
    "- **Inflow Archive:**\n",
    "  - `inflow/AZ-104-JohnSavill-DeepDives/` (33 individual metadata & curriculum breakdown notes).\n",
    "  - `inflow/AZ-104-JohnSavill_DeepDives_Master_Transcript.md` (Consolidated master curriculum and video index).\n",
    "- **Preserved Inflow Files:**\n"
]

for f in files:
    lines.append(f"  - `inflow/AZ-104-JohnSavill-DeepDives/{f}`\n")

lines.append("\n### 🚀 Going the Extra Mile: Deep In-Place Enrichment Across Canonical Modules\n")
lines.append("Appended dedicated 'Going the Extra Mile: Architectural Deep Dive' sections across the canonical AZ-104 reference notes:\n")
lines.append("- **Module 13-104-01:** Azure Cost Optimization (Reservations vs Savings Plans, Spot eviction mechanics, hunting orphaned disks/IPs/NICs) & WSL2 Hyper-V kernel tooling architecture.\n")
lines.append("- **Module 13-104-02:** Entra Privileged Identity Management (PIM), Continuous Access Evaluation (CAE) real-time token revocation, Identity Protection risk engine, Cross-Tenant Access Settings, Application Proxy hybrid reverse proxy, and Entra Permissions Management (CIEM Permission Creep Index).\n")
lines.append("- **Module 13-104-03:** Azure RBAC internal schema (Actions vs NotActions additive evaluation), Azure Key Vault HSM vs Software boundaries and RBAC permissions, and Microsoft Defender for Multi-Cloud (AWS/GCP CSPM).\n")
lines.append("- **Module 13-104-06:** ExpressRoute physical Meet-Me peering & FastPath hypervisor bypass, Azure Virtual Network Manager (AVNM) Security Admin Rules (SAR) overriding NSGs, Private Link TCP proxy v2 header preservation, and Azure Firewall TLS inspection & IDPS.\n")
lines.append("- **Module 13-104-07:** Azure Load Balancer hypervisor SDN multiplexer, hash tuples, HA Ports, SNAT exhaustion & NAT Gateway, Gateway Load Balancer (GWLB) bump-in-the-wire VXLAN tunneling, Azure Front Door Anycast split-TCP acceleration & Private Link origins, and Application Gateway for Containers (ALB) split-plane ingress.\n")
lines.append("- **Module 13-104-08:** Azure Elastic SAN native iSCSI shared storage pools, Blob data permissions hierarchy (Control Plane vs Data Plane vs POSIX ACLs vs SAS), and Azure Confidential Ledger hardware enclave immutability.\n")
lines.append("- **Module 13-104-09:** Managed Disks storage page blob architecture, Premium v2 decoupled scaling, on-demand bursting, shared disks for clustering, and Azure VMware Solution (AVS) bare-metal ESXi fabric.\n")
lines.append("- **Module 13-104-10:** AKS Networking models (Kubenet vs Azure CNI vs Azure CNI Overlay vs Cilium eBPF), Azure API Management Generative AI Gateway (model failover, semantic caching, token rate limits), and Azure SQL Hyperscale storage-compute separation.\n\n")

backlog_entry = "".join(lines)

with open("backlog.md", "r", encoding="utf-8") as f:
    original = f.read()

# Insert right after header
header_marker = "This backlog tracks all updates, modifications, and restructuring activities performed in this CKA study knowledge base.\n\n"
if header_marker in original:
    new_backlog = original.replace(header_marker, header_marker + backlog_entry)
else:
    # fallback
    parts = original.split("\n## ", 1)
    new_backlog = parts[0] + "\n\n" + backlog_entry + "## " + parts[1]

with open("backlog.md", "w", encoding="utf-8") as f:
    f.write(new_backlog)

print("Updated backlog.md successfully!")
