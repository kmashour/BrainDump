import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REF_DIR = "Reference Notes"

def enrich_file(file_name, new_section, citation_line):
    fpath = os.path.join(REF_DIR, file_name)
    if not os.path.exists(fpath):
        print(f"Error: {file_name} not found!")
        return
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "Scott Duffy Insights" in content:
        print(f"Skipping (already enriched): {file_name}")
        return

    # Append before ## 🌐 Authoritative References & Citations
    if "## 🌐 Authoritative References & Citations" in content:
        parts = content.split("## 🌐 Authoritative References & Citations")
        body = parts[0].rstrip()
        refs = parts[1].strip()
        
        # Add citation to references if not present
        if citation_line not in refs:
            refs = refs + f"\n- {citation_line}"
            
        updated = f"{body}\n\n{new_section}\n\n## 🌐 Authoritative References & Citations\n\n{refs}\n"
    else:
        updated = f"{content.rstrip()}\n\n{new_section}\n\n## 🌐 Authoritative References & Citations\n- {citation_line}\n"
        
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(updated)
    print(f"Enriched: {file_name}")

# ==============================================================================
# MODULE 01: Course Intro, Budgeting & Tooling
# ==============================================================================
mod01_text = """## 🛠️ Operational Tooling, Spending Caps & Cloud Shell Architecture (Scott Duffy Insights)

### 1. Azure Free Account Spending Guardrails & Tier Mechanics
*   **The Initial 30-Day Window:** Microsoft provides **$200 USD in cloud credits** valid for exactly 30 days.
*   **The Strict Spending Limit ($0 Guardrail):** By default, the free subscription includes a hard spending limit set to $0. If experimental workloads consume all $200 credits within 30 days, Azure automatically suspends all compute instances (VMs deallocate, websites stop responding) to prevent unauthorized credit card billing.
*   **12 Months Free Services & Always Free Tier:**
    *   *12 Months Free:* Standard B1s Linux/Windows VMs (up to 750 hours/month), 5 GB LRS Blob storage, 5 GB Azure Files.
    *   *Always Free Tier (55+ Services):* Azure App Services (up to 10 apps on F1 tier), Azure Functions (1,000,000 executions/month), Azure Cosmos DB (1,000 RU/s throughput + 25 GB storage), Azure Event Grid (100,000 operations/month).

### 2. Azure Cost Management Budgeting & Multi-Threshold Action Alerts
*   **Budget Scope:** Can be configured at the Management Group, Subscription, or Resource Group level.
*   **Evaluation Frequency:** Azure Cost Management evaluates accumulated billing data against the configured budget every 4 hours.
*   **Threshold Multi-Staging:** Best practice configures 4 progressive notification gates:
    *   `50% Forecasted/Actual`: Early warning notification sent to platform engineers.
    *   `75% Actual`: FinOps review alert dispatched to department lead.
    *   `90% Actual`: Automated scaling throttle or deployment pause notification.
    *   `100% Actual`: Automated Action Group trigger (e.g., executing an Azure Automation Runbook or Azure Logic App to deallocate non-production dev/test VMs).

### 3. PowerShell Core with `Az` Module Enterprise Setup
*   **PowerShell Core (`pwsh`):** Modern cross-platform automation engine (Linux, macOS, Windows).
*   **Installation Command:**
    ```powershell
    # Install Az module strictly for current user to avoid admin permission requirements
    Install-Module -Name Az -Scope CurrentUser -Repository PSGallery -Force -AllowClobber
    
    # Authenticate interactively to Microsoft Entra ID
    Connect-AzAccount
    
    # View all accessible subscriptions
    Get-AzSubscription | Select-Object Name, Id, State
    
    # Switch active subscription context
    Set-AzContext -SubscriptionId "00000000-0000-0000-0000-000000000000"
    ```
*   **Cloud Shell Storage Requirement:** When launching Azure Cloud Shell for the first time, ARM requires provisioning a standard LRS storage account and a dedicated `5 GB` Azure File Share. This share is mounted automatically to `/home/<username>` to persist scripts, SSH keys, and custom modules across ephemeral Cloud Shell sessions.
"""

enrich_file(
    "13-104-01_course_introduction_and_certification.md",
    mod01_text,
    "Udemy AZ-104 Microsoft Azure Administrator Course by Scott Duffy ([Inflow: Module 01](file:///F:/Dump%20one/BrainDump/inflow/AZ-104-ScottDuffy/01_Course_Introduction_Budgeting_and_Tooling.md))"
)

# ==============================================================================
# MODULE 02: Administer Identity (Entra ID)
# ==============================================================================
mod02_text = """## 🏢 Enterprise Identity Administration, Licensing & Device Governance (Scott Duffy Insights)

### 1. Microsoft Entra ID Licensing Tiers & Feature Matrix
| Capability | Entra ID Free | Entra ID P1 | Entra ID P2 |
| :--- | :--- | :--- | :--- |
| **User & Group Administration** | Core User/Group Management, Cloud sync | All Free features | All P1 features |
| **SSO Application Limit** | Up to 10 apps per user | **Unlimited SSO apps** | Unlimited SSO apps |
| **Self-Service Password Reset (SSPR)** | Cloud users only (no on-prem writeback) | **SSPR with On-Premises Password Writeback** | SSPR with Password Writeback |
| **Group Membership Engine** | Static membership only | **Dynamic Group Membership Rules** | Dynamic Group Membership Rules |
| **Conditional Access** | Security Defaults (binary on/off) | **Granular Conditional Access Policies** | Conditional Access Policies |
| **Identity Protection & Risk Engine** | None | None | **Real-Time Risk-Based Conditional Access** |
| **Privileged Access Governance** | None | None | **Privileged Identity Management (PIM)** |
| **Compliance & Auditing** | Basic sign-in & audit logs (7 days) | Advanced reporting & auditing (30 days) | **Entra Access Reviews & Entitlement Management** |

### 2. Custom Domain Verification Flow & Immutability Rules
*   **Default Suffix:** Every new Entra ID tenant starts with `<tenant-name>.onmicrosoft.com`.
*   **Verification Protocol:**
    1.  Add custom domain (e.g., `contoso.com`) in Entra ID.
    2.  Create a **DNS TXT record** (e.g., `MS=msXXXXXXXX`) at the domain registrar. Alternatively, an **MX record** can be used if TXT is unsupported.
    3.  Click **Verify** in the Azure Portal. Once verified, the domain status changes from `Unverified` to `Verified`.
    4.  Set as **Primary Domain** to automatically assign `@contoso.com` to new users.
*   **Deletion Immutability Law:** An administrator **CANNOT delete a custom domain** if any user, group, Microsoft 365 license, or app registration currently references that domain suffix. All user UPNs must be migrated back to `.onmicrosoft.com` before deletion is permitted.

### 3. Administrative Units (AUs) Regional Delegation
*   **Architectural Purpose:** Allows delegating administrative control over a subset of users and groups (e.g., European Staff) to regional administrators without granting global tenant-wide administrative roles.
*   **Key Operational Rules:**
    *   Administrators assigned roles at the AU scope (e.g., User Administrator on `AU-Europe`) can only modify passwords, profile attributes, and group memberships for users explicitly contained in that AU.
    *   *AU Membership is Not Transitive:* Nested groups do not inherit AU membership. If Group B is inside Group A, and Group A is in an AU, members of Group B are NOT managed by the AU admin!

### 4. Device Management Topology
```text
+-------------------+-----------------------------------+-----------------------------------+
| Device State      | Target Operating Systems          | Management & Ownership Model      |
+-------------------+-----------------------------------+-----------------------------------+
| Entra Registered  | Windows 10/11, iOS, Android, macOS| BYOD (Bring Your Own Device).     |
|                   |                                   | User signs in with local account; |
|                   |                                   | workplace account added for SSO.  |
+-------------------+-----------------------------------+-----------------------------------+
| Entra Joined      | Windows 10/11, Windows Server 2019| Corporate-owned, cloud-only.      |
|                   |                                   | User logs in using Entra UPN.     |
|                   |                                   | Managed natively via Intune MDM.  |
+-------------------+-----------------------------------+-----------------------------------+
| Entra Hybrid      | Windows 10/11, Windows Server     | Joined to on-premises AD DS domain|
| Joined            | Active Directory Domain Services  | and synchronized to Entra ID via  |
|                   |                                   | Microsoft Entra Connect sync.     |
+-------------------+-----------------------------------+-----------------------------------+
```
"""

enrich_file(
    "13-104-02_administer_identity.md",
    mod02_text,
    "Udemy AZ-104 Microsoft Azure Administrator Course by Scott Duffy ([Inflow: Module 02](file:///F:/Dump%20one/BrainDump/inflow/AZ-104-ScottDuffy/02_Administer_Identity_Entra_ID.md))"
)

# ==============================================================================
# MODULE 03: Administer Governance and Compliance
# ==============================================================================
mod03_text = """## 📜 Operational Policy Automation, Resource Locks & Cross-RG Migration (Scott Duffy Insights)

### 1. Custom RBAC Role JSON Specification & The `NotActions` Trap
When defining an enterprise Custom RBAC role, the JSON definition adheres to strict schema constraints:
```json
{
  "Name": "Virtual Machine Operator Contributor",
  "IsCustom": true,
  "Description": "Allows managing VM power states without modifying compute configurations.",
  "Actions": [
    "Microsoft.Compute/*/read",
    "Microsoft.Compute/virtualMachines/start/action",
    "Microsoft.Compute/virtualMachines/restart/action",
    "Microsoft.Compute/virtualMachines/powerOff/action"
  ],
  "NotActions": [
    "Microsoft.Compute/virtualMachines/delete"
  ],
  "DataActions": [],
  "NotDataActions": [],
  "AssignableScopes": [
    "/subscriptions/00000000-0000-0000-0000-000000000000",
    "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg-workloads-prod"
  ]
}
```
*   **The `NotActions` Rule:** `NotActions` is **NOT a Deny rule**. It is purely a subtraction from the `Actions` array. If another role (such as `Contributor`) grants `Microsoft.Compute/virtualMachines/delete`, the user CAN still delete the VM!
*   **`AssignableScopes` Limitation:** You can assign multiple subscriptions or resource groups, but you **CANNOT** declare a Management Group scope in a custom role if the role is created via PowerShell in older API versions.

### 2. Resource Locks Operational Consequences
*   **`ReadOnly` Lock Side Effects:**
    *   *Storage Accounts:* Blocks listing access keys! In ARM, `listKeys` is an `HTTP POST` operation requiring write authorization (`Microsoft.Storage/storageAccounts/listkeys/action`), so ARM rejects it under a ReadOnly lock.
    *   *Virtual Machines:* Blocks starting or stopping the VM through the portal/CLI because updating the power state modifies compute runtime metadata.
*   **`CanNotDelete` Lock:** Allows modifying properties, scaling, adding data disks, and restarting compute instances, but blocks deleting the resource or its parent resource group.

### 3. Resource Migration (Move) Prerequisites & Constraints
When migrating resources across Resource Groups or Subscriptions:
1.  **Dependency Bundling:** Child resources must move together with their parent. For a Virtual Machine, you must select the VM, OS disk, data disks, network interface (NIC), and attached public IP in the same move operation.
2.  **Lock Clearance:** Both the source resource group and target resource group must have all Resource Locks temporarily removed.
3.  **Tenant Boundary Law:** Resources cannot move directly across different Microsoft Entra ID tenants. The subscription containing the resources must first have its directory changed via Azure Portal.
"""

enrich_file(
    "13-104-03_administer_governance_and_compliance.md",
    mod03_text,
    "Udemy AZ-104 Microsoft Azure Administrator Course by Scott Duffy ([Inflow: Module 03](file:///F:/Dump%20one/BrainDump/inflow/AZ-104-ScottDuffy/03_Administer_Governance_and_Compliance.md))"
)

# ==============================================================================
# MODULE 04: Administer Azure Resources (ARM & Bicep)
# ==============================================================================
mod04_text = """## 🚀 ARM Template Specs, Custom Script Extensions & Bicep Tooling (Scott Duffy Insights)

### 1. ARM Template Specs (Enterprise Template Sharing)
*   **What are Template Specs?** Instead of storing ARM templates in public GitHub repos or SAS-protected storage blobs, **Template Specs** (`Microsoft.Resources/templateSpecs`) store templates natively as first-class securable Azure resources.
*   **Benefits:**
    *   Protected by standard Azure RBAC (Reader/Contributor permissions).
    *   Supports native semantic versioning (e.g., `1.0.0`, `1.1.0`, `2.0.0`).
    *   Direct deployment via Portal, CLI, or PowerShell:
        ```bash
        az deployment group create \\
          --resource-group rg-production \\
          --template-spec "/subscriptions/xxx/resourceGroups/rg-templates/providers/Microsoft.Resources/templateSpecs/baselineVNet/versions/1.0"
        ```

### 2. Custom Script Extensions (CSE) Runtime Rules
*   **Execution Timeout:** Maximum runtime execution limit is **90 minutes**. If scripts exceed 90 minutes, ARM marks the deployment as `Failed`.
*   **Exit Code 0 Contract:** The extension expects the script to exit with code `0`. Any non-zero exit code indicates failure and stops dependent resources.
*   **Reboot Handling:** If a script requires a VM reboot, it must be structured to handle the reboot gracefully or execute in two separate script extensions.

### 3. Azure Bicep Authoring, Compilation & Decompilation
*   **Bicep vs. ARM JSON:** Bicep is a domain-specific language (DSL) that compiles transparently into ARM JSON (`az bicep build --file main.bicep`).
*   **Decompiling Legacy ARM Templates:** You can reverse-engineer any existing ARM template into clean Bicep code using the Azure CLI:
    ```bash
    az bicep decompile --file template.json
    ```
    This outputs `template.bicep` with cleaned parameter types, variables, and resource dependencies!
"""

enrich_file(
    "13-104-04_administer_azure_resources.md",
    mod04_text,
    "Udemy AZ-104 Microsoft Azure Administrator Course by Scott Duffy ([Inflow: Module 06](file:///F:/Dump%20one/BrainDump/inflow/AZ-104-ScottDuffy/06_Administer_Automation_ARM_Templates_and_Bicep.md))"
)

# ==============================================================================
# MODULE 05: Administer Virtual Networking
# ==============================================================================
mod05_text = """## 🌐 Public IP SKUs, Subnet Security & Network Watcher Diagnostics (Scott Duffy Insights)

### 1. Basic vs. Standard Public IP SKUs: Architectural Differences
| Architectural Property | Basic SKU Public IP | Standard SKU Public IP (Mandatory for Modern Workloads) |
| :--- | :--- | :--- |
| **Allocation Method** | Dynamic or Static | **Static Only** |
| **Default Security Posture**| Open to Internet by default (NSG recommended) | **Closed by default (Secure)**; traffic rejected until NSG allows |
| **Zone Resiliency** | No Availability Zone support | **Zone-Redundant, Zonal, or No Zone** |
| **Load Balancer Pairing** | Basic Load Balancer only | **Standard Load Balancer only** (SKUs cannot be mixed!) |
| **Routing Preference** | Microsoft Global Network only | Microsoft Global Network or Transit ISP Internet |

### 2. NSG Default Security Rules Architecture
Every Network Security Group comes with 3 immutable inbound and 3 immutable outbound default rules:
*   `65000: AllowVNetInBound` (Allows traffic originating anywhere inside the VNet address space).
*   `65001: AllowAzureLoadBalancerInBound` (Allows health probes from Azure infrastructure IP `168.63.129.16`).
*   `65500: DenyAllInBound` (Blocks all other inbound traffic from any source).
*   *Key Rule:* Default rules **CANNOT be deleted**. They can only be overridden by creating custom rules with priority numbers between `100` and `4096`.

### 3. Network Watcher Diagnostic Recipes
*   **IP Flow Verify:** Simulates a 5-tuple packet (Protocol, Source IP, Source Port, Destination IP, Destination Port) to determine whether access is `Allowed` or `Denied`, identifying the exact NSG rule responsible.
*   **Next Hop:** Diagnoses asymmetric or broken routing by querying what next hop type Azure SDN will use (`VirtualNetwork`, `Internet`, `VirtualAppliance`, `None`).
"""

enrich_file(
    "13-104-05_administer_virtual_networking.md",
    mod05_text,
    "Udemy AZ-104 Microsoft Azure Administrator Course by Scott Duffy ([Inflow: Module 08](file:///F:/Dump%20one/BrainDump/inflow/AZ-104-ScottDuffy/08_Administer_Virtual_Networking_and_InterSite_Connectivity.md))"
)

# ==============================================================================
# MODULE 06: Administer Intersite Connectivity
# ==============================================================================
mod06_text = """## 🔄 Global VNet Peering vs. VNet-to-VNet Gateways (Scott Duffy Insights)

### 1. Intersite Architectural Trade-offs
```text
+-----------------------+---------------------------------------+---------------------------------------+
| Feature               | Virtual Network Peering (Recommended) | VNet-to-VNet VPN Gateway              |
+-----------------------+---------------------------------------+---------------------------------------+
| Performance           | Line-rate Microsoft Optical WAN speed | Limited by Gateway SKU (650M - 1.25G) |
| Latency               | Lowest possible (Zero gateway hops)   | Higher (Packets processed by gateway) |
| Encryption            | Azure physical optical layer MACsec   | IPsec / IKE tunnel encryption         |
| Gateway Transit       | Supports sharing Hub VPN / ER Gateway | Requires complex mesh configuration   |
| IP Overlap Support    | STRICT NO (CIDRs must not overlap)    | Supported via NAT on Gateway          |
| Billing Model         | Ingress & Egress per-GB data transfer | Gateway hourly uptime + egress data   |
+-----------------------+---------------------------------------+---------------------------------------+
```

### 2. Azure Private DNS Zone Resolution vs. Auto-Registration
*   **Virtual Network Link:** Binds a Private DNS Zone (`privatelink.blob.core.windows.net` or `corp.internal`) to a VNet.
*   **Registration Enabled (`true`):** Azure automatically creates and manages DNS `A` records for VMs deployed in that VNet. (Limit: Only 1 auto-registration VNet per private DNS zone).
*   **Resolution Only (`false`):** VMs in this VNet can resolve DNS names in the zone, but their own hostnames are not registered. (Supports up to 1,000 VNets linked to a single private zone).
"""

enrich_file(
    "13-104-06_administer_intersite_connectivity.md",
    mod06_text,
    "Udemy AZ-104 Microsoft Azure Administrator Course by Scott Duffy ([Inflow: Module 08](file:///F:/Dump%20one/BrainDump/inflow/AZ-104-ScottDuffy/08_Administer_Virtual_Networking_and_InterSite_Connectivity.md))"
)

# ==============================================================================
# MODULE 07: Administer Network Traffic
# ==============================================================================
mod07_text = """## ⚖️ Load Balancer Health Probes, ASGs & App Gateway v2 Routing (Scott Duffy Insights)

### 1. Application Security Groups (ASGs) Micro-Segmentation
*   **The Operational Advantage:** Instead of hardcoding VM private IP addresses into NSG rules, you associate the VM's Network Interface (NIC) with an Application Security Group (e.g., `asg-web` or `asg-sql`).
*   **Clean Declarative Rule:**
    *   Source: `asg-web`
    *   Destination: `asg-sql`
    *   Port: `1433` | Action: `Allow`
    *   *Result:* When scaling out web servers from 2 to 20 instances, newly deployed NICs added to `asg-web` automatically inherit database access without touching the NSG!

### 2. Standard Load Balancer Health Probes Mechanics
*   **HTTP/HTTPS Probes:** Expect an `HTTP 200 OK` response. Any redirect (`HTTP 301/302`) or server error (`HTTP 500`) causes the probe to fail.
*   **TCP Probes:** Simply performs a 3-way TCP handshake (`SYN`, `SYN-ACK`, `ACK`). If the port is open and listening, the backend instance is marked healthy.
*   **Unhealthy Threshold:** By default, 2 consecutive probe failures mark the VM down, instantly removing it from backend pool distribution with zero dropped packets for existing sessions.

### 3. Application Gateway v2 Multi-Site & Path-Based Routing
*   **Multi-Site Listeners:** Evaluates the `Host:` HTTP header to route traffic for multiple distinct domain names (e.g., `billing.contoso.com` and `support.contoso.com`) through a single public IP.
*   **Path-Based Routing Rules:** Evaluates URL request paths (e.g., `/images/*` directed to a Storage Account backend pool, and `/api/*` directed to an App Service VMSS backend pool).
"""

enrich_file(
    "13-104-07_administer_network_traffic.md",
    mod07_text,
    "Udemy AZ-104 Microsoft Azure Administrator Course by Scott Duffy ([Inflow: Module 09](file:///F:/Dump%20one/BrainDump/inflow/AZ-104-ScottDuffy/09_Administer_Network_Traffic_Security_and_Load_Balancing.md))"
)

# ==============================================================================
# MODULE 08: Administer Azure Storage
# ==============================================================================
mod08_text = """## 📦 Access Tiers, Stored Access Policies & Object Replication (Scott Duffy Insights)

### 1. Storage Access Tiers Cost & Latency Comparison
```text
+-----------------------+-------------------+-------------------+-------------------+-------------------+
| Tier                  | Hot Tier          | Cool Tier         | Cold Tier         | Archive Tier      |
+-----------------------+-------------------+-------------------+-------------------+-------------------+
| Storage Cost          | Highest           | Moderate          | Low               | Lowest            |
| Data Access Cost      | Lowest            | Moderate          | High              | Highest           |
| Minimum Retention     | None              | 30 Days           | 90 Days           | 180 Days          |
| Retrieval Latency     | Milliseconds      | Milliseconds      | Milliseconds      | Hours (Offline)   |
| Early Deletion Fee    | No                | Prorated (30 days)| Prorated (90 days)| Prorated (180 days|
+-----------------------+-------------------+-------------------+-------------------+-------------------+
```
*   **Archive Rehydration:** Blobs in Archive cannot be read directly. They must be rehydrated back to Hot or Cool:
    *   *Standard Priority:* Rehydration takes up to 15 hours.
    *   *High Priority:* Expedited rehydration for blobs < 10 GB completes in under 1 hour (higher cost).

### 2. Stored Access Policies: The Only Way to Revoke a Service SAS
*   **The SAS Revocation Problem:** Once an ad-hoc Shared Access Signature (SAS) is issued with an expiration date, it **CANNOT be revoked** without regenerating the storage account's master access keys (which breaks all other applications using those keys!).
*   **The Enterprise Fix:** Associate the SAS with a **Stored Access Policy (SAP)** defined on the container. If a SAS token is compromised, an administrator simply deletes or edits the Stored Access Policy, instantly invalidating the SAS token without affecting master keys!

### 3. Cross-Region Object Replication Prerequisites
*   Source and destination storage accounts must both have **Blob Versioning** and **Change Feed** enabled.
*   Destination account must be in a different region.
*   Blobs in the Archive tier cannot be replicated.
"""

enrich_file(
    "13-104-08_administer_azure_storage.md",
    mod08_text,
    "Udemy AZ-104 Microsoft Azure Administrator Course by Scott Duffy ([Inflow: Module 04](file:///F:/Dump%20one/BrainDump/inflow/AZ-104-ScottDuffy/04_Administer_Azure_Storage.md))"
)

# ==============================================================================
# MODULE 09: Administer Virtual Machines & VMSS
# ==============================================================================
mod09_text = """## 🖥️ VM Resizing Gotchas, Disk Caching Rules & Azure Bastion (Scott Duffy Insights)

### 1. Resizing Azure VMs & The Temporary Disk Hazard
*   **Hardware Cluster Limitations:** If you resize a VM to a SKU family that is not available on the physical hardware rack hosting the VM, Azure returns an `AllocationFailed` error.
*   **The Fix:** You must first **Deallocate** the VM (`az vm deallocate`), allowing Azure to relocate the compute allocation to a hardware cluster supporting the target SKU, then resize and start.
*   **Temporary Disk Wiped:** Azure VMs include a temporary local disk (`D:` on Windows, `/dev/sdb1` on Linux) backed by physical host SSDs. **Any data stored on the temporary disk is permanently lost when a VM is resized, stopped/deallocated, or rebooted for service healing.**

### 2. Virtual Machine Disk Host Caching Matrix
*   **ReadWrite (Default OS Disk):** Caches reads and writes in host RAM. Suitable for general OS operations.
*   **ReadOnly:** Caches reads only. **Recommended for SQL Server data files (`.mdf`)** and read-heavy reporting systems.
*   **None (No Caching):** Mandatory for **SQL Server transaction log files (`.ldf`)** and high-transaction write workloads to eliminate the risk of data loss or write-ordering corruption during physical host power failure.
*   *Note:* Data disks larger than 4 TiB (4096 GiB) do not support host caching.

### 3. Azure Bastion Deployment Baseline
*   Must reside in a dedicated subnet named strictly: `AzureBastionSubnet`.
*   Subnet prefix must be `/26` or larger (`/26`, `/25`, `/24`) to accommodate scale-out instances.
*   Does not support UDRs (User-Defined Routes) directing traffic to virtual appliances.
"""

enrich_file(
    "13-104-09_administer_azure_virtual_machines.md",
    mod09_text,
    "Udemy AZ-104 Microsoft Azure Administrator Course by Scott Duffy ([Inflow: Module 05](file:///F:/Dump%20one/BrainDump/inflow/AZ-104-ScottDuffy/05_Administer_Azure_Virtual_Machines_and_VMSS.md))"
)

# ==============================================================================
# MODULE 10: Administer PaaS Compute (App Services & Containers)
# ==============================================================================
mod10_text = """## 🐳 App Service Scaling, Slot Swaps & Container Workloads (Scott Duffy Insights)

### 1. App Service Plan Scaling Paradigms
*   **Scale Up (Vertical):** Changing the tier/SKU (e.g., migrating from Basic `B1` to Standard `S1` or Premium `P1v3`) to increase CPU cores, RAM, dedicated storage, or unlock features (slots, backups, VNet integration).
*   **Scale Out (Horizontal):** Adding identical VM instances to the App Service Plan (up to 3 in Basic, up to 10 in Standard, up to 30 in Premium v3).
*   **Autoscale Rules:** Can scale out automatically based on average CPU > 70% over 10 minutes, with a configured cooldown window (e.g., 5 minutes) to prevent scaling oscillation.

### 2. App Service Deployment Slot Swap Mechanics
*   **Pre-Swap Warm-up:** Azure sends an HTTP request to the root path of the staging slot before swapping traffic. If the application takes 30 seconds to compile or warm up caches, this ensures end users never experience cold-start latency.
*   **Sticky vs. Swapped Settings:**
    *   *Swapped Settings:* Application code, framework versions, default connection strings.
    *   *Sticky Settings (Pinned to Slot):* Database connection strings for staging, custom domain names, SSL certificates, publishing credentials. Configured using `Deployment slot setting = true`.

### 3. Azure Container Instances (ACI) vs. Azure Container Apps (ACA)
*   **ACI (Azure Container Instances):** Simplest, fastest way to run isolated Docker containers without managing VM infrastructure. Billed per-second. Supports **Container Groups** (multiple co-scheduled containers sharing localhost networking and storage volumes).
*   **ACA (Azure Container Apps):** Serverless platform built on Kubernetes and KEDA. Designed for microservices, background job processing, built-in ingress, and scale-to-zero capabilities based on HTTP traffic or Azure Service Bus queue depth.
"""

enrich_file(
    "13-104-10_administer_paas_compute_options.md",
    mod10_text,
    "Udemy AZ-104 Microsoft Azure Administrator Course by Scott Duffy ([Inflow: Module 07](file:///F:/Dump%20one/BrainDump/inflow/AZ-104-ScottDuffy/07_Administer_PaaS_Compute_App_Services_and_Containers.md))"
)

# ==============================================================================
# MODULE 11: Administer Data Protection (Backup & Site Recovery)
# ==============================================================================
mod11_text = """## 🛡️ Recovery Services Vault, Instant Restore & Azure Site Recovery (Scott Duffy Insights)

### 1. Azure Backup: Instant Restore Snapshot Retention
*   **Instant Restore Tier:** When Azure Backup backs up an Azure VM, it takes an application-consistent snapshot of the managed disks. This snapshot is retained in the **local storage tier for 1 to 5 days** (default 2 days).
*   **Operational Benefit:** If an admin needs to restore a VM that crashed 2 hours ago, Azure restores directly from the local snapshot in **under 2 minutes**, avoiding long download delays from the vault tier!
*   **Vault Tier:** Snapshots are transferred in the background to the Recovery Services Vault, compressed and deduplicated for long-term retention (weeks, months, or years).

### 2. File-Level Recovery (FLR) via iSCSI Mount Script
*   Instead of restoring an entire 500 GB virtual machine to recover a single corrupted configuration file:
    1.  Click **File Recovery** in the Azure Portal for the selected recovery point.
    2.  Azure generates an executable script (`.exe` for Windows, `.sh` for Linux) containing a unique password.
    3.  Run the script on any machine (or the target VM): It establishes an **iSCSI connection** directly to the backup snapshot recovery point.
    4.  The backup disks are mounted as local drive letters, allowing the engineer to copy and paste the needed files directly before unmounting!

### 3. Azure Site Recovery (ASR) Disaster Recovery Drills
*   **Continuous Replication:** ASR uses the Mobility Service extension to capture block-level disk changes in real-time and stream them to a cache storage account in the secondary region.
*   **Test Failover (Zero Production Impact):** Allows executing a scheduled disaster recovery drill. Azure spins up replica VMs in an **isolated test virtual network** without stopping ongoing replication or impacting the primary production site!
"""

enrich_file(
    "13-104-11_administer_data_protection.md",
    mod11_text,
    "Udemy AZ-104 Microsoft Azure Administrator Course by Scott Duffy ([Inflow: Module 11](file:///F:/Dump%20one/BrainDump/inflow/AZ-104-ScottDuffy/11_Administer_Data_Protection_Backup_and_Recovery.md))"
)

# ==============================================================================
# MODULE 12: Administer Monitoring & Log Analytics
# ==============================================================================
mod12_text = """## 📊 Azure Monitor Agent, DCR Ingestion Governance & KQL (Scott Duffy Insights)

### 1. Modern Azure Monitor Agent (AMA) vs. Legacy MMA Agent
*   **Legacy Log Analytics Agent (MMA/OMS):** Monolithic agent that ingested all Windows event logs or Syslog streams without filtering, leading to bloated data volume and unexpected billing. (Retired August 2024).
*   **Modern Azure Monitor Agent (AMA):** Uses centralized **Data Collection Rules (DCR)** to filter logs at the client operating system before transmission over the network.
*   **DCR Filtering Power:** An administrator can specify an XPath query to ingest *only* `Error` and `Critical` events from the `System` and `Application` logs, reducing ingested log volume by up to 85%!

### 2. Essential Kusto Query Language (KQL) Production Recipes
```kql
// 1. Audit all resource deletions across the entire subscription in the last 7 days
AzureActivity
| where TimeGenerated >= ago(7d)
| where OperationNameValue has "delete" and ActivityStatusValue == "Success"
| project TimeGenerated, Caller, ResourceGroup, OperationNameValue, ActivitySubstatusValue

// 2. Query top 5 virtual machines by Average CPU utilization over the past 24 hours
Perf
| where TimeGenerated >= ago(24h)
| where ObjectName == "Processor" and CounterName == "% Processor Time" and InstanceName == "_Total"
| summarize AvgCPU = avg(CounterValue) by Computer, bin(TimeGenerated, 1h)
| top 5 by AvgCPU desc

// 3. Detect failed SSH and RDP brute force attempts on virtual machines
SecurityEvent
| where TimeGenerated >= ago(24h)
| where EventID in (4625) // Failed Windows logon
| summarize FailedCount = count() by TargetUserName, IpAddress
| where FailedCount > 10
| order by FailedCount desc
```
"""

enrich_file(
    "13-104-12_administer_monitoring.md",
    mod12_text,
    "Udemy AZ-104 Microsoft Azure Administrator Course by Scott Duffy ([Inflow: Module 10](file:///F:/Dump%20one/BrainDump/inflow/AZ-104-ScottDuffy/10_Administer_Monitoring_and_Log_Analytics.md))"
)

# ==============================================================================
# UPDATE BACKLOG WITH SCOTT DUFFY INGESTION
# ==============================================================================
print("\nUpdating backlog.md...")
backlog_path = "backlog.md"
with open(backlog_path, "r", encoding="utf-8") as f:
    backlog_content = f.read()

duffy_backlog_entry = """## [2026-11-01] - Ingestion & Synthesis: Scott Duffy AZ-104 Complete Course (12 Modules)

### 📥 Inflow Extraction & Progressive Chunking
- **Source Course:** Udemy - AZ-104 Microsoft Azure Administrator by Scott Duffy (Master Transcript: `inflow/udemy_transcript_802576.txt`, 24,731 lines).
- **Progressive Chunking:** Segmented into 12 structured, cleaned markdown files under `inflow/AZ-104-ScottDuffy/`:
  - `inflow/AZ-104-ScottDuffy/01_Course_Introduction_Budgeting_and_Tooling.md`
  - `inflow/AZ-104-ScottDuffy/02_Administer_Identity_Entra_ID.md`
  - `inflow/AZ-104-ScottDuffy/03_Administer_Governance_and_Compliance.md`
  - `inflow/AZ-104-ScottDuffy/04_Administer_Azure_Storage.md`
  - `inflow/AZ-104-ScottDuffy/05_Administer_Azure_Virtual_Machines_and_VMSS.md`
  - `inflow/AZ-104-ScottDuffy/06_Administer_Automation_ARM_Templates_and_Bicep.md`
  - `inflow/AZ-104-ScottDuffy/07_Administer_PaaS_Compute_App_Services_and_Containers.md`
  - `inflow/AZ-104-ScottDuffy/08_Administer_Virtual_Networking_and_InterSite_Connectivity.md`
  - `inflow/AZ-104-ScottDuffy/09_Administer_Network_Traffic_Security_and_Load_Balancing.md`
  - `inflow/AZ-104-ScottDuffy/10_Administer_Monitoring_and_Log_Analytics.md`
  - `inflow/AZ-104-ScottDuffy/11_Administer_Data_Protection_Backup_and_Recovery.md`
  - `inflow/AZ-104-ScottDuffy/12_AZ104_Last_Minute_Study_Review_and_Exam_Strategies.md`

### 🏛️ Canonical Reference Notes In-Place Synthesis
Enriched all canonical AZ-104 reference notes with Scott Duffy's practical operational recipes, CLI/PowerShell workflows, and real-world gotchas:
- **Module 13-104-01:** Azure Free Account credit limits ($0 spending cap), Cost Management multi-threshold budgets, PowerShell Core `Az` module setup, Cloud Shell persistence storage architecture.
- **Module 13-104-02:** Entra ID Free vs P1 vs P2 licensing comparison, Custom Domain TXT/MX verification & deletion immutability laws, Administrative Units (AUs) non-transitive rules, Device management states (Registered vs Joined vs Hybrid Joined).
- **Module 13-104-03:** Custom RBAC role JSON specification (`AssignableScopes`, `NotActions` subtraction rule), Resource Locks operational consequences (`ReadOnly` blocking Storage `listKeys`), Resource move dependency bundling and tenant constraints.
- **Module 13-104-04:** ARM Template Specs versioning and RBAC sharing, Custom Script Extensions (CSE) 90-minute timeout and exit code 0 contract, Azure Bicep VS Code workflow and decompilation (`az bicep decompile`).
- **Module 13-104-05:** Basic vs Standard Public IP SKUs, NSG default security rules immutability, Network Watcher IP Flow Verify and Next Hop diagnostics.
- **Module 13-104-06:** Global VNet Peering vs VNet-to-VNet VPN Gateways architectural trade-offs, Azure Private DNS Zones auto-registration vs resolution-only virtual network links.
- **Module 13-104-07:** Application Security Groups (ASGs) micro-segmentation, Standard Load Balancer health probe thresholds, Application Gateway v2 multi-site and path-based routing rules.
- **Module 13-104-08:** Blob access tiers retention and rehydration mechanics (Standard vs High Priority), Stored Access Policies (SAP) as the prerequisite for SAS revocation, Object Replication change feed and versioning requirements.
- **Module 13-104-09:** VM resizing cluster allocation limits and temporary disk wiping hazard, host disk caching rules (`ReadOnly` for SQL data vs `None` for transaction logs), Azure Bastion `/26` subnet baseline.
- **Module 13-104-10:** App Service Plan vertical vs horizontal scaling, deployment slot warm-up request cycles and sticky slot settings, ACI Container Groups vs Azure Container Apps (ACA) microservices.
- **Module 13-104-11:** Recovery Services Vault Instant Restore snapshot retention (1-5 days), File-Level Recovery (FLR) iSCSI executable mount scripts, Azure Site Recovery (ASR) non-disruptive test failovers in isolated VNets.
- **Module 13-104-12:** Azure Monitor Agent (AMA) and Data Collection Rules (DCR) log filtering, essential KQL production query recipes for auditing, performance, and security events.

"""

if "## [2026-11-01] - Ingestion & Synthesis: Scott Duffy AZ-104" not in backlog_content:
    header_end = backlog_content.find("\n\n## ")
    if header_end != -1:
        new_backlog = backlog_content[:header_end] + "\n\n" + duffy_backlog_entry + backlog_content[header_end+2:]
    else:
        new_backlog = backlog_content + "\n\n" + duffy_backlog_entry
    with open(backlog_path, "w", encoding="utf-8") as f:
        f.write(new_backlog)
    print("backlog.md updated successfully.")
else:
    print("backlog.md already contains this entry.")

print("\nSynthesis complete!")
