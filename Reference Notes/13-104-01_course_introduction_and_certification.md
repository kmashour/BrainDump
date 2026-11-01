---
obsidianUIMode: preview
class: reference-note
tier: reference-note
domains:
  - "azure"
tags:
  - azure/az-104
  - azure/certification
  - azure/administration
  - azure/architecture
  - status/completed
---

# Module 13-104-01: Azure Administration Architecture, Operations & Certification Framework

**Breadcrumbs:** [[13-Index - Azure|☁️ Azure Reference MOC]] > [[13-Index - AZ-104|📘 AZ-104 Exam Track]] > **01 - Azure Administration Architecture & Certification**

---

## 🎯 Executive Overview & First-Principles Architecture

The **Microsoft Certified: Azure Administrator Associate (AZ-104)** credential validates the foundational to intermediate engineering capabilities required to implement, operate, optimize, and govern Microsoft Azure environments. In real-world enterprise infrastructure, the Azure Administrator does not merely click buttons in a GUI; they are the custodian of the **Azure Resource Manager (ARM) Control Plane**, bridging business requirements, security baselines, developer velocity, and financial predictability.

```text
[ Actors & Callers ]
  ├── DevOps (CI/CD Pipelines)
  ├── SecOps (Compliance & Audit)
  ├── Cloud Platform Administrators
  └── FinOps (Cost Optimization)
        │
        ▼
[ Azure Resource Manager (ARM) Control Plane Gateway ]
  https://management.azure.com
        │
  ├── 1. Authentication (Microsoft Entra ID Token Verification)
  ├── 2. Authorization (Azure RBAC Scope & Action Evaluation)
  ├── 3. Guardrails (Azure Policy Engine Enforcement)
  └── 4. Immutability (Resource Locks: ReadOnly / CanNotDelete)
        │
        ▼
[ Azure Resource Providers (Data & Compute Fabric) ]
  ├── Microsoft.Compute (VMs, VMSS, Disks)
  ├── Microsoft.Network (VNets, NSGs, LBs, DNS)
  ├── Microsoft.Storage (Blob, Files, Tables, Queues)
  ├── Microsoft.Web     (App Services, Functions)
  └── Microsoft.Insights(Log Analytics, Alerts)
```

### The Azure Control Plane vs. Data Plane Mental Model
Understanding the separation between the **Control Plane** and the **Data Plane** is essential for diagnosing operational issues, configuring access controls, and designing enterprise architectures:

| Operational Dimension | Control Plane (Management Plane) | Data Plane (Runtime Plane) |
| :--- | :--- | :--- |
| **Primary Endpoint** | `https://management.azure.com` | Service-specific (e.g., `<account>.blob.core.windows.net`, `<app>.azurewebsites.net`) |
| **Governing Authority** | Azure Resource Manager (ARM) | Service Runtime Engine / Daemons / Hypervisor |
| **Authentication & Authorization** | Microsoft Entra ID + **Azure RBAC** (Actions: `Microsoft.Storage/storageAccounts/write`) | Service Keys, SAS Tokens, or Entra ID **DataActions** (`Microsoft.Storage/.../blobs/read`) |
| **Policy & Governance** | Enforced natively via Azure Policy initiatives and Resource Locks | Governed by service firewalls, TLS settings, and runtime access policies |
| **Operational Impact Example** | A `ReadOnly` lock at the resource group blocks modifying VM configurations or deleting disks. | The VM operating system, databases, and network packet flow continue serving traffic unimpeded. |

---

## 🏛️ The 4-Tier Hierarchy: Designing for Scale and Autonomy

When designing enterprise architectures, Azure enforces a strict 4-tier management hierarchy. Every architectural proposal, cost-allocation strategy, and security boundary relies on this structure:

```text
Tenant Root Group (One per Microsoft Entra ID Tenant)
  ├── Platform Management Group
  │     ├── Connectivity Subscription (Hub VNet, ExpressRoute, Azure Firewall)
  │     └── Management Subscription   (Log Analytics, Automation, Bastion)
  └── Workloads Management Group
        ├── Corporate Sub-MG ──► Prod Subscription ──► rg-prod-app01 ──► VMs, Storage
        └── Online Sub-MG    ──► Dev Subscription  ──► rg-dev-app01  ──► App Services
```

### Architectural Rationale & Design Trade-offs
1. **Tenant Root Group:** The absolute root of the management hierarchy. Policies assigned here propagate down to every subscription in the organization.
   * *Architectural Rule:* Assign only foundational guardrails at Root (e.g., restricting deployment regions to sovereign jurisdictions, enforcing minimum TLS 1.2). Never assign broad Contributor permissions at the Tenant Root Group.
2. **Management Groups (Up to 6 levels deep):** Organizational containers used to govern multiple subscriptions. They allow centralized billing categorization, compliance enforcement, and access delegation.
3. **Subscriptions (The Fundamental Isolation Boundary):** Subscriptions serve three distinct functions:
   * **Financial Boundary:** Azure cost invoicing, billing accounts, and spending limits operate at the subscription level.
   * **Quota Boundary:** Core counts, public IP addresses, and service limits (e.g., maximum 800 Resource Groups per subscription) are tracked and enforced per subscription.
   * **Administrative Boundary:** Provides complete control-plane isolation between operational environments (e.g., Production vs. Staging vs. Sandboxes).
4. **Resource Groups (Lifecycle Containers):** A logical container for resources that share the same lifecycle, deployment cadence, and operational management.
   * *Best Practice:* Group resources by lifecycle (e.g., app servers and their specific disks together), rather than grouping all databases in one resource group and all VMs in another.

---

## 📊 Exam Objective Domains & Weightings

```text
[ Functional Domains & Weightings ]
  ├── Manage Azure Identities & Governance : 20–25%
  ├── Deploy & Manage Azure Compute        : 20–25%
  ├── Implement & Maintain Virtual Network : 15–20%
  ├── Implement & Manage Storage           : 15–20%
  └── Monitor & Maintain Azure Resources   : 10–15%
```

| Functional Domain | Exam Weight | Core Architectural Competencies & Production Nuances |
| :--- | :---: | :--- |
| **Manage Azure Identities & Governance** | **20–25%** | Microsoft Entra ID tenants, user/group lifecycle, Administrative Units, SSPR writeback, hybrid directory sync (PHS vs. PTA vs. ADFS), Azure RBAC custom role authoring, Azure Policy effects (`Deny`, `Modify`, `DeployIfNotExists`), and Resource Locks. |
| **Deploy & Manage Azure Compute Resources** | **20–25%** | VM sizing and compute tiers (burstable vs. memory-optimized), Managed Disk performance provisioning, Host Caching rules, Azure Bastion architecture, Availability Sets vs. Availability Zones, VMSS autoscaling, App Service plans and deployment slots, Azure Container Instances (ACI), and Azure Container Apps (ACA). |
| **Implement & Maintain Virtual Networking** | **15–20%** | Virtual Network (VNet) topology, RFC 1918 CIDR subnetting (5 reserved IPs), NSGs and ASGs, Private/Public DNS resolution, VNet Peering and Gateway Transit, User-Defined Routes (UDRs), NVAs, Azure Load Balancer, and Layer 7 Application Gateway (WAF v2). |
| **Implement & Manage Storage** | **15–20%** | Storage accounts (General Purpose v2 vs. Premium), data redundancy (LRS, ZRS, GRS, GZRS), Blob lifecycle management rules, Blob versioning and soft delete, immutable WORM storage, Azure Files SMB/NFS, and Shared Access Signatures (Account vs. Service vs. User Delegation SAS). |
| **Monitor & Maintain Azure Resources** | **10–15%** | Full-stack observability with Azure Monitor, Metrics vs. Logs, Activity Log retention & diagnostic export, Log Analytics Workspaces, Kusto Query Language (KQL), Azure Monitor Agent (AMA) + Data Collection Rules (DCRs), Metric Alerts, Action Groups, Alert Processing Rules, Azure Backup, and Azure Site Recovery (ASR). |

---

## ⚙️ Administration Tooling & Automation Setup

Enterprise Azure administrators leverage a multi-tool chain depending on the automation task, platform, and operational context:

```text
[ Visual & Ad-Hoc Management ]
  ├── Azure Portal (Web UI, Interactive Dashboards, Resource Exploration)
  └── Azure Cloud Shell (Browser-based Bash / PowerShell with persistent Azure Files)
        │
        ▼
[ Automated & Programmatic Management ]
  ├── Azure CLI (`az`) ──► Cross-platform, Linux/macOS, CI/CD pipelines, JSON/JMESPath
  ├── Azure PowerShell (`Az`) ──► Object pipeline, Windows automation, .NET objects
  └── Declarative IaC ──► Azure Bicep DSL & ARM Templates (idempotent state)
```

### 1. Azure CLI (`az`) Production Baseline
Azure CLI outputs JSON by default, making it ideal for Linux environments, Bash scripting, and modern CI/CD pipelines (e.g., GitHub Actions, GitLab CI).

```bash
# Verify CLI installation and active version
az version

# Authenticate interactively or via managed identity / service principal
az login

# List all available subscriptions and verify current context
az account list --output table
az account show --output jsonc

# Set default subscription context to avoid accidental deployments to wrong tenant/sub
az account set --subscription "Production-Core-Infrastructure"

# Configure persistent CLI defaults (region and resource group)
az configure --defaults location=eastus group=rg-production-networking
```

### 2. Azure PowerShell (`Az` Module) Production Baseline
PowerShell processes structured .NET objects rather than raw text streams, allowing granular pipeline filtering and deep integration with Windows administration.

```powershell
# Verify installed Az module and update check
Get-InstalledModule -Name Az -AllVersions

# Interactive login
Connect-AzAccount

# Query and set subscription context
Get-AzSubscription | Select-Object Name, Id, State | Format-Table
Set-AzContext -SubscriptionId "11111111-2222-3333-4444-555555555555"

# Pipeline object querying example: Find all unattached Managed Disks (cost leak detection)
Get-AzDisk | Where-Object { $_.ManagedBy -eq $null } | Select-Object Name, ResourceGroupName, DiskSizeGB
```

---

## 🏛️ How to Articulate Solutions: From Admin to Architect

When presenting technical proposals to leadership, engineering teams, or certification panels, structure your articulation around four pillars:

```text
[ Architectural Pillars for Enterprise Solution Articulation ]
  ├── 1. Security & Identity Boundary (Zero Trust, Least Privilege, Microsoft Entra ID)
  ├── 2. Resilience & High Availability (SLA math, RTO/RPO, Multi-Zone, Regional Pairs)
  ├── 3. Performance & Scalability (Autoscaling, Caching, Microsoft Global Backbone)
  └── 4. Financial & Operational Governance (Azure Policy, Reserved Instances, FinOps)
```

### Articulation Frameworks by Scenario
1. **Scenario: Securing Administrative Access to Virtual Machines**
   * *Weak Response:* "I will open port 22 or 3389 and use a strong password."
   * *Architectural Articulation:* "Deploy **Azure Bastion** into a dedicated `AzureBastionSubnet` (`/26` minimum). This provides browser-based, HTML5 TLS 443 tunneling directly to private VM IPs inside the VNet. It eliminates the need for Public IP addresses on VMs, protects against port-scanning attacks on ports 22 and 3389, and integrates with Microsoft Entra ID MFA and Conditional Access."
2. **Scenario: Preventing Critical Data Loss in Storage Accounts**
   * *Weak Response:* "I will make backups every night."
   * *Architectural Articulation:* "Implement a defense-in-depth data protection strategy:
     1. Enable **Blob Versioning** and **Blob Soft Delete** (14 to 365 days retention) to protect against accidental client-side modifications or ransomware deletion.
     2. Apply a `CanNotDelete` **Resource Lock** at the Storage Account scope to prevent unauthorized ARM control-plane deletion.
     3. For disaster recovery across regions, configure **Geo-Redundant Storage (GRS)** or **Geo-Zone-Redundant Storage (GZRS)**, providing a secondary recovery point objective (RPO < 15 minutes) with asynchronous replication to the paired region."

---

## 💡 AZ-104 Exam Strategy & Tactical Blueprint

> [!IMPORTANT]
> **Exam Mechanics & Constraints:**
> - **Passing Score:** 700 / 1000 (Scaled score).
> - **Time Limit:** 100 to 120 minutes for 40 to 60 questions.
> - **Question Types:** Multiple choice, drag-and-drop build lists, drop-down code completions, repeated scenario questions, and comprehensive case studies.

### Tactical Execution Plan
1. **The Case Study Gauntlet:**
   * Case studies present 4 to 8 tabs containing company background, current infrastructure, planned changes, business requirements, technical requirements, and security policies.
   * *Tactical Rule:* **Do not read the case study from start to finish initially.** Jump directly to Question 1, identify the specific technical requirement (e.g., "minimize costs", "ensure zero downtime during OS updates", "allow delegated user password resets"), and navigate directly to the relevant requirement tab.
   * *Unidirectional Lock:* Once you submit the Case Study section, the testing software permanently locks those questions. You cannot return to review them later. Allocate 25–30 minutes exclusively for case studies.
2. **Repeated Scenario Questions (Yes/No Series):**
   * A business problem is presented, followed by a proposed solution. You must evaluate whether the solution meets the goal (*Yes* or *No*).
   * Once answered and advanced, you **cannot backtrack**. Evaluate each proposed solution strictly on its own merits without guessing what subsequent questions might offer.
3. **Keyword Decoupling Cheat-Sheet:**
   * *"Minimize administrative effort"* $\rightarrow$ Prefer Azure built-in features, Azure Policy, or PaaS services over custom scripts or IaaS VMs.
   * *"Lowest cost solution with redundancy"* $\rightarrow$ Prefer LRS or ZRS over GRS; prefer Standard SSD over Premium SSD v2/Ultra Disk.
   * *"Zero downtime deployment"* $\rightarrow$ Prefer Azure App Service **Deployment Slots** with warm swap over manual container re-deployments.

---

## 🏛️ Deep-Dive Architecture & Physical Topology (John Savill Master Class Insights)

### 1. Azure Physical Topology & Global Footprint
To articulate high-availability architectures and explain latency constraints, administrators must understand Microsoft's physical infrastructure:

```text
Geographies (e.g., United States, Europe, Asia Pacific)
  │  (Data sovereignty, geopolitical compliance boundaries)
  │
  ├── Regional Pairs (Separated by hundreds of miles, e.g., East US ◄─► West US)
  │     │  (Phased sequential platform patching; pairs are never updated concurrently)
  │     │
  │     ├── Region A (e.g., East US)
  │     │     ├── Availability Zone 1 (Independent datacenter: power, cooling, fiber)
  │     │     ├── Availability Zone 2 (Independent datacenter: < 2ms latency from AZ1)
  │     │     └── Availability Zone 3 (Independent datacenter: private optical ring)
  │     │
  │     └── Region B (e.g., West US - Paired Region for GRS replication)
  │           └── Availability Zones 1, 2, 3
```

- **Geographies:** Ensure regulatory compliance, data residency, and tax/jurisdictional boundaries are preserved (e.g., data residing within UK borders).
- **Regions:** A collection of datacenters connected through a dedicated low-latency optical network within a defined perimeter.
- **Regional Pairs:** Each region is hard-paired with another region at least 300 miles away. Microsoft applies Azure platform host updates sequentially across paired regions—ensuring host maintenance never impacts both paired regions simultaneously.
- **Availability Zones:** Physically separate datacenter buildings with independent utility feeds, backup generators, and network paths. Latency between zones in the same region is strictly under 2 milliseconds.

### 2. The Resource Group Metadata vs. Resource Location Paradigm
A frequent point of confusion among cloud engineers:
- **Resource Group Location:** Specifies where the Resource Group's **management metadata** is stored.
- **Resource Location:** A Resource Group located in `East US` can contain a Virtual Machine located in `West Europe` and a Storage Account in `Southeast Asia`.
- **Architectural Failure Mode:** If the region hosting the Resource Group's metadata suffers an outage, the resources within that group continue running and serving production traffic unimpeded (Data Plane continuity), but administrators cannot update or delete those resources via ARM until the metadata region recovers (Control Plane impact).

### 3. FinOps & Cloud Economics: Cost Optimization Engineering
John Savill emphasizes that cost optimization is a first-class engineering discipline in Azure:
- **Pricing Calculator vs. TCO Calculator:**
  - *Pricing Calculator:* Estimates ongoing operating expenses (OpEx) for proposed Azure deployments.
  - *Total Cost of Ownership (TCO) Calculator:* Compares existing on-premises datacenter costs (hardware, power, cooling, real estate, server virtualization licenses, rack administration labor) against equivalent Azure services.
- **Compute Cost Optimization Hierarchy:**
  1. *Pay-As-You-Go:* Maximum flexibility, highest hourly cost.
  2. *Azure Reserved Instances (RIs):* 1-year or 3-year commitments on predictable baseline compute, saving up to 72% compared to Pay-As-You-Go. Can be exchanged or canceled with a pro-rated fee.
  3. *Azure Hybrid Benefit (AHB):* Reuses existing on-premises Windows Server and SQL Server licenses covered by Software Assurance (SA). When combined with 3-year Reserved Instances, compute costs drop by up to 80–85%.
  4. *Azure Spot Virtual Machines:* Utilizes unused Azure spare compute capacity at up to 90% discount. Ideal for batch jobs, video transcoding, and stateless dev/test workloads that can tolerate unexpected evictions (evicted with a 30-second warning when Azure requires capacity back).

---

---

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

## 🛠️ Operational Tooling, Spending Caps & Cloud Shell Architecture (Scott Duffy Insights)

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


## 🌐 Authoritative References & Citations

- [Microsoft Learn: Study Guide for Exam AZ-104: Microsoft Azure Administrator](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104)
- [Microsoft Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)
- [Microsoft Cloud Adoption Framework (CAF) for Azure](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/)
- [John Savill: AZ-104 Administrator Certification Study Playlist & Master Class](https://www.youtube.com/playlist?list=PLlVtbbG169nGlGPWs9xaLKT1KfwqREHbs)
- [KodeKloud AZ-104: Microsoft Azure Administrator Complete Course](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Introduction/Course-Introduction/page)
- [Moe Intelligence: Comprehensive AZ-104 & Cloud Engineering Lecture Series](https://www.youtube.com/playlist?list=PLczK3J2J4clmeh328CC13dJrcALcSFZFb)
- [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/)
- Udemy AZ-104 Microsoft Azure Administrator Course by Scott Duffy ([Inflow: Module 01](file:///F:/Dump%20one/BrainDump/inflow/AZ-104-ScottDuffy/01_Course_Introduction_Budgeting_and_Tooling.md))
