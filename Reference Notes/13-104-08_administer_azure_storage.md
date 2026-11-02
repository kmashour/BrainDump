---
obsidianUIMode: preview
class: reference-note
tier: reference-note
domains:
  - "azure"
tags:
  - azure/az-104
  - azure/storage
  - azure/blob
  - azure/files
  - status/completed
---

# Module 13-104-08: Administer Azure Storage, Blob Tiers & Security

**Breadcrumbs:** [[13-Index - Azure|☁️ Azure Reference MOC]] > [[13-Index - AZ-104|📘 AZ-104 Exam Track]] > **08 - Administer Azure Storage**

---

## 🎯 Stage 1: Executive Overview & The Conceptual Lecture

### 1. The Zero-Knowledge Starting Point: What is Cloud Storage?
In traditional on-premises IT, storing files was anchored to physical hardware:
* If a company needed storage, they bought hard drives, installed them into physical servers, or purchased a multimillion-dollar **Storage Area Network (SAN)** rack from vendors like EMC or NetApp.
* If a physical disk died, a red LED flashed, an alarm sounded, and a sysadmin rushed to the datacenter to swap the drive.
* If the company ran out of disk space, they had to order new drive shelves, wait weeks for delivery, and manually re-partition logical unit numbers (LUNs).
* If a pipe burst or a fire broke out in the server room, every file was lost forever unless someone took tape backups offsite in a briefcase.

In Microsoft Azure, storage is treated as a **massively scalable, software-defined utility**:
* You do not buy disks, format partitions, or worry about bad sectors.
* You provision an **Azure Storage Account**, and Azure immediately provides an virtually limitless, highly durable, globally replicated storage namespace accessible over standard web protocols (HTTPS).
* Every single piece of data stored in Azure is automatically encrypted at rest and replicated multiple times to ensure it survives hardware failures, power outages, and natural disasters.

### 2. The Four Pillars of Azure Storage (Decoding the Core Services)
A single Azure Storage Account hosts four distinct storage services, each tailored for specific workload requirements:

```text
+-------------------------------------------------------------------------------------------------+
|                               THE 4 PILLARS OF AZURE STORAGE                                    |
+-------------------------------------------------------------------------------------------------+
|  1. Azure Blob Storage       |  2. Azure Files              |  3. Azure Queues & Tables         |
+------------------------------+------------------------------+-----------------------------------+
| - Type: Object Storage       | - Type: Managed File Shares  | - Type: Messaging & NoSQL Data    |
| - Protocol: HTTPS REST APIs  | - Protocol: SMB 3.0 / NFS    | - Protocol: HTTPS REST APIs       |
| - Analog: Amazon S3, Google  | - Analog: Windows Network    | - Analog: AWS SQS (Queues) and    |
|   Cloud Storage              |   Share (\\server\share)     |   DynamoDB / SimpleDB (Tables)    |
| - Use: Unstructured images,  | - Use: "Lift-and-shift" on-  | - Use: Decoupling application     |
|   videos, backups, logs,     |   prem VMs that need a shared|   components via messaging, fast  |
|   static web hosting, big    |   drive letter (Z:), FSLogix |   schemaless key-value storage    |
|   data lake analytics        |   VDI user profiles          |   for state metadata              |
+-------------------------------------------------------------------------------------------------+
```

### 3. Terminology Matrix: Zero-Knowledge to Enterprise Architect

| Terminology | What It Means to a Beginner | Real-World Analog | Enterprise Architecture Reality |
| :--- | :--- | :--- | :--- |
| **Storage Account** | A master account that holds all your cloud files. | A safe deposit box container at a bank. | A unified HTTP/HTTPS endpoint namespace (`https://<account>.*.core.windows.net`) providing multi-service data persistence. |
| **Blob (Binary Large Object)** | Any unstructured file (video, PDF, zip, image). | An unformatted digital document in a drawer. | Object storage organized into Account $\rightarrow$ Container $\rightarrow$ Blob, accessible globally via URL. |
| **LRS (Locally Redundant)** | Saving 3 copies in one building. | Keeping 3 photocopies of a birth certificate in 3 different drawers in your house. | 3 synchronous data copies within a single physical Azure datacenter (11 nines durability). |
| **ZRS (Zone-Redundant)** | Saving 3 copies across 3 separate buildings. | Keeping one photocopy at home, one at the bank, and one at your parents' house. | 3 synchronous copies distributed across 3 distinct Availability Zones in the primary region (12 nines durability). |
| **GRS (Geo-Redundant)** | Saving copies in another city 500 miles away. | Sending a duplicate archive box to an earthquake-proof bunker in another state. | LRS in primary region + asynchronous replication to a paired secondary region (16 nines durability). |
| **Lifecycle Management** | An automated rule that moves old files to cheaper storage. | A cleaning service that moves 1-month-old papers to the basement and shreds 7-year-old tax forms. | An ARM-integrated policy engine evaluating blob metadata daily to transition blobs between Hot, Cool, Cold, and Archive tiers. |
| **SAS (Shared Access Signature)** | A temporary, restricted URL key for a file. | A guest hotel keycard that only unlocks Room 304 and expires at 11:00 AM tomorrow. | A signed URI granting granular, time-bound, IP-restricted read/write access to storage resources without exposing root account keys. |
| **User Delegation SAS** | A temporary key signed with your employee ID instead of the master key. | A visitor pass signed by an authenticated security officer with an audit trail. | A Zero-Trust SAS token signed via Microsoft Entra ID credentials, revocable instantly without regenerating master storage keys. |

---

## 🏛️ Stage 2: Core Mental Model & Component Architecture

### 1. Storage Account Kinds & Performance Tiers
When creating an Azure Storage Account, choosing the correct account type is critical for cost optimization and capability:

```text
General-Purpose v2 (GPv2) - The Default Enterprise Choice
├── Storage Media: Standard (Magnetic HDD) or Premium (Solid State SSD)
├── Supported Services: Blobs, Files, Queues, Tables, and Data Lake Gen2
├── Access Tiers: Hot, Cool, Cold, and Archive
└── Redundancy Options: LRS, ZRS, GRS, RA-GRS, GZRS, RA-GZRS

Specialized Premium Accounts (SSD Only - High Throughput / Low Latency)
├── BlockBlobStorage: High-transaction containerized apps, low-latency analytics
├── FileStorage: High-IOPS enterprise file shares, FSLogix virtual desktop profiles
└── PageBlobStorage: Legacy unmanaged OS and data disks for VMs
```

---

### 2. The Data Redundancy Hierarchy & Durability Math
Azure Storage guarantees industry-leading durability by automatically maintaining multiple replicas of every file:

```mermaid
flowchart TD
    subgraph PrimaryRegion ["Primary Azure Region (e.g., East US)"]
        subgraph LRS_Scope ["Locally Redundant Storage (LRS)"]
            DC1["Single Datacenter (3 Synchronous Replicas)\nDurability: 99.999999999% (11 9s)\nGuards against: Server rack, disk, PSU failure"]
        end

        subgraph ZRS_Scope ["Zone-Redundant Storage (ZRS)"]
            AZ1["AZ 1 (Replica 1)"] <-->|Sync Write| AZ2["AZ 2 (Replica 2)"]
            AZ2 <-->|Sync Write| AZ3["AZ 3 (Replica 3)"]
            NoteZRS["Durability: 99.9999999999% (12 9s)\nGuards against: Complete Datacenter Flood / Fire"]
        end
    end

    subgraph SecondaryRegion ["Secondary Paired Region (e.g., West US)"]
        subgraph GeoReplication ["Geo-Redundancy (GRS / GZRS)"]
            SecDC["Secondary Datacenter (3 Replicas)\nDurability: 99.99999999999999% (16 9s)\nGuards against: Regional Catastrophe"]
        end
        RA_Endpoint["Read-Access Secondary Endpoint\n(<account>-secondary.blob.core.windows.net)"]
    end

    LRS_Scope -.->|Asynchronous Geo-Replication| SecDC
    ZRS_Scope -.->|Asynchronous Geo-Replication| SecDC
    SecDC --- RA_Endpoint
```

#### Detailed Redundancy Comparison Matrix:

| Redundancy Option | Primary Region Placement | Secondary Region Placement | Durability SLA | Secondary Read Access | Customer Failover Support |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **LRS** | 3 copies in 1 Datacenter | None | **11 9s** ($10^{-11}$) | ❌ No | N/A |
| **ZRS** | 3 copies across 3 AZs | None | **12 9s** ($10^{-12}$) | ❌ No | N/A (Survives AZ loss) |
| **GRS** | 3 copies via LRS | 3 copies via LRS | **16 9s** ($10^{-16}$) | ❌ No | ✅ Yes (Account Failover) |
| **RA-GRS** | 3 copies via LRS | 3 copies via LRS | **16 9s** ($10^{-16}$) | ✅ **Yes** (`-secondary`) | ✅ Yes (Account Failover) |
| **GZRS** | 3 copies across 3 AZs | 3 copies via LRS | **16 9s** ($10^{-16}$) | ❌ No | ✅ Yes (Account Failover) |
| **RA-GZRS** | 3 copies across 3 AZs | 3 copies via LRS | **16 9s** ($10^{-16}$) | ✅ **Yes** (`-secondary`) | ✅ Yes (Account Failover) |

> [!IMPORTANT]
> **RPO and Asynchronous Replication Law:**
> Replication within the primary region (LRS and ZRS) is **synchronous**: a write operation is acknowledged only when committed to all 3 local replicas.
> Replication to the secondary region (GRS and GZRS) is **asynchronous**: data is replicated in the background with a Recovery Point Objective (RPO) typically under **15 minutes**. If a regional disaster occurs and you initiate account failover, up to 15 minutes of recently written data may be lost!

---

### 3. Blob Access Tiers & FinOps Economics
Azure Blob Storage provides four storage tiers to balance storage cost versus access latency:

```text
Hot Tier (Active Working Set)
├── Cost: Highest storage cost ($0.018/GB), lowest access cost
├── Latency: Milliseconds (Online)
└── Minimum Retention: None (0 days)
       │
       │ Inactive for 30 days
       ▼
Cool Tier (Infrequently Accessed Data)
├── Cost: Lower storage cost ($0.010/GB), higher access cost
├── Latency: Milliseconds (Online)
└── Minimum Retention: 30 DAYS (Early deletion incurs prorated penalty!)
       │
       │ Inactive for 90 days
       ▼
Cold Tier (Rarely Accessed Data)
├── Cost: Very low storage cost ($0.0036/GB), higher access cost
├── Latency: Milliseconds (Online)
└── Minimum Retention: 90 DAYS (Early deletion incurs prorated penalty!)
       │
       │ Inactive for 180 days
       ▼
Archive Tier (Deep Offline Storage)
├── Cost: Lowest possible storage cost ($0.00099/GB - 90% cheaper than Hot!)
├── Latency: 1 TO 15 HOURS (Blobs are OFFLINE and cannot be read directly!)
├── Minimum Retention: 180 DAYS (Early deletion incurs prorated penalty!)
└── Rehydration Required: Must set tier to Hot or Cool before reading!
```

---

## 🏢 Stage 3: Deep-Intuition Platform Mechanics & Topology

### 1. Storage Access Security Triad: Keys vs. SAS vs. Entra ID
Securing Azure Storage is a core responsibility on the AZ-104 exam. There are three primary access mechanisms:

```text
1. Storage Account Access Keys (Master Root Keys: Key 1 & Key 2)
   ├── Full superuser administrative control over EVERYTHING in the account!
   ├── Bypasses all Azure RBAC data roles and network controls.
   └── Severe Security Hazard: If a developer leaks an access key, attackers have total control.
       (Enterprise Best Practice: Disable shared key access via 'allowSharedKeyAccess: false').

2. Shared Access Signatures (SAS)
   ├── Temporary, time-bound, IP-restricted URL tokens granting scoped permissions (Read/Write).
   ├── Account SAS: Spans multiple services (Blob, File, Queue). Signed by Master Key.
   ├── Service SAS: Scoped to one container or blob. Signed by Master Key.
   └── User Delegation SAS: Signed via Microsoft Entra ID OAuth credentials!
       (Enterprise Standard: Can be revoked instantly without rotating master keys).

3. Microsoft Entra ID (Azure RBAC Data Plane Roles)
   ├── Zero secrets or tokens to manage.
   ├── Uses Azure RBAC identities (Users, Groups, Managed Identities).
   └── Built-In Roles:
       - 'Storage Blob Data Reader': Read blob contents and metadata.
       - 'Storage Blob Data Contributor': Read, write, and delete blobs.
       - 'Storage Blob Data Owner': Full data control + grant RBAC roles.
```

#### The Stored Access Policy (SAP) Revocation Problem:
* When an ad-hoc SAS token is generated using the master storage key, **it CANNOT be revoked early!** It remains valid until its expiration date arrives, unless you regenerate the master storage key (which breaks all other applications using that key).
* **The Solution:** Associate the Service SAS with a **Stored Access Policy (SAP)** on the container. If the SAS token is leaked or compromised, an administrator simply deletes or edits the Stored Access Policy, **instantly invalidating the SAS token** without affecting account keys!

---

### 2. Data Protection: Soft Delete, Versioning & Immutability (WORM)
* **Blob Versioning:** Automatically creates a read-only historical version stamped with a UTC timestamp whenever a blob is overwritten. You can revert to any prior version at any time.
* **Blob Soft Delete (The Recycle Bin):** Retains deleted blobs and versions for a configurable retention window (e.g., 7 to 365 days). During this period, deleted blobs can be un-deleted directly from the Azure Portal with a single click.
* **Immutable Blob Storage (WORM - Write Once, Read Many):**
  * *Time-Based Retention:* Blobs can be written and read, but **cannot be modified or deleted** for a mandatory time window (e.g., 7 years for SEC/FINRA compliance).
  * *Legal Hold:* Freezes data indefinitely until an ongoing litigation or audit tag is explicitly cleared.

---

### 3. Azure Files & Azure File Sync: Hybrid File Tiering
* **Azure Files:** Fully managed serverless file shares accessible concurrently from Windows, Linux, and macOS via industry-standard **SMB 3.0** and **NFS 4.1** protocols. Integrates with Active Directory Domain Services (AD DS) for native NTFS permissions.
* **Azure File Sync:** Transforms local on-premises Windows File Servers into high-speed caches while replicating all files centrally to an Azure Files share:
  * **Cloud Tiering:** Local Windows servers cache frequently accessed "hot" files locally, while infrequently accessed "cold" files are replaced with lightweight pointer stubs. When an on-premises user double-clicks a stub file, the Azure File Sync agent seamlessly streams the file content from Azure Files over HTTPS!

---

## ⚙️ Stage 4: Declarative & Automation Engine (CLI & PowerShell Core)

### 1. Azure CLI: Storage Account & Lifecycle Management Recipes

```bash
# ==============================================================================
# 1. CREATE ENTERPRISE STORAGE ACCOUNT WITH REDUNDANCY & SECURITY
# ==============================================================================
az storage account create \
  --resource-group "rg-storage-lab" \
  --name "stenterpriseblob2026" \
  --location "eastus" \
  --sku "Standard_ZRS" \
  --kind "StorageV2" \
  --access-tier "Hot" \
  --min-tls-version "TLS1_2" \
  --allow-blob-public-access false

# ==============================================================================
# 2. CONFIGURE BLOB SOFT DELETE & VERSIONING
# ==============================================================================
az storage account blob-service-properties update \
  --resource-group "rg-storage-lab" \
  --account-name "stenterpriseblob2026" \
  --enable-versioning true \
  --enable-delete-retention true \
  --delete-retention-days 14 \
  --enable-container-delete-retention true \
  --container-delete-retention-days 14

# ==============================================================================
# 3. APPLY AUTOMATED LIFECYCLE MANAGEMENT POLICY
# ==============================================================================
cat << 'EOF' > lifecycle-policy.json
{
  "rules": [
    {
      "enabled": true,
      "name": "TierInvoicesToCoolAndArchive",
      "type": "Lifecycle",
      "definition": {
        "filters": {
          "blobTypes": ["blockBlob"],
          "prefixMatch": ["invoices/"]
        },
        "actions": {
          "baseBlob": {
            "tierToCool": { "daysAfterModificationGreaterThan": 30 },
            "tierToCold": { "daysAfterModificationGreaterThan": 90 },
            "tierToArchive": { "daysAfterModificationGreaterThan": 180 },
            "delete": { "daysAfterModificationGreaterThan": 365 }
          }
        }
      }
    }
  ]
}
EOF

az storage account management-policy create \
  --resource-group "rg-storage-lab" \
  --account-name "stenterpriseblob2026" \
  --policy @lifecycle-policy.json
```

### 2. Azure CLI: Stored Access Policy & User Delegation SAS

```bash
# ==============================================================================
# 4. STORED ACCESS POLICY (REVOCABLE SAS)
# ==============================================================================

# Create container
az storage container create \
  --account-name "stenterpriseblob2026" \
  --name "corporate-invoices" \
  --auth-mode login

# Create Stored Access Policy on the container
az storage container policy create \
  --account-name "stenterpriseblob2026" \
  --container-name "corporate-invoices" \
  --name "Policy-Auditor-Read" \
  --permissions "r" \
  --expiry "2026-12-31T23:59:59Z" \
  --auth-mode key

# Generate Service SAS linked to the Stored Access Policy
az storage container generate-sas \
  --account-name "stenterpriseblob2026" \
  --name "corporate-invoices" \
  --policy-name "Policy-Auditor-Read" \
  --output tsv
```

---

## 🖥️ Stage 5: Step-by-Step Azure Portal GUI Walkthrough

Follow these exact navigation steps in the **Azure Portal** (`https://portal.azure.com`) to master storage administration:

### Task 1: Provisioning a Secure Storage Account in the GUI
1. In the top search bar, type **Storage accounts** and select it.
2. Click **+ Create** on the command bar:
   - **Resource group:** Select `rg-storage-lab`.
   - **Storage account name:** Enter a globally unique name (3–24 lowercase letters/numbers, e.g., `staz104corpstore`).
   - **Region:** `East US`.
   - **Primary service:** Select *Azure Blob Storage or Azure Data Lake Storage Gen 2*.
   - **Performance:** Select **Standard**.
   - **Redundancy:** Select **Zone-redundant storage (ZRS)**.
3. In the **Security** tab:
   - Ensure *Require secure transfer for REST API operations* is checked.
   - Set *Minimum TLS version* to **Version 1.2**.
   - Uncheck *Allow enabling public access on individual containers* (disables public access tenant-wide!).
4. Click **Review + create** $\rightarrow$ **Create**.

### Task 2: Configuring Lifecycle Management via the Visual Rule Builder
1. Open your newly created storage account.
2. In the left navigation menu under **Data management**, click **Lifecycle management**.
3. On the top command bar, click **+ Add a rule**:
   - **Rule name:** `TierAndPurgeLogs`.
   - **Rule scope:** Select **Limit blobs with filters**.
   - **Blob type:** Select **Block blobs** $\rightarrow$ check **Base blobs**.
4. In the **Base blobs** rule builder tab:
   - *If Base blobs were last modified more than:* Enter `30` days $\rightarrow$ Action: **Move to cool storage**.
   - Click **+ Add condition**:
     - *If Base blobs were last modified more than:* Enter `90` days $\rightarrow$ Action: **Move to archive storage**.
   - Click **+ Add condition**:
     - *If Base blobs were last modified more than:* Enter `365` days $\rightarrow$ Action: **Delete the blob**.
5. In the **Filter set** tab:
   - Under *Blob prefix*, type `logs/`.
6. Click **Add**. Azure will now automatically evaluate and transition matching blobs every 24 hours!

### Task 3: Enabling Data Protection (Versioning & Soft Delete)
1. In the left navigation menu under **Data management**, click **Data protection**.
2. Configure recovery settings:
   - Check **Enable soft delete for blobs** $\rightarrow$ set retention to `14` days.
   - Check **Enable soft delete for containers** $\rightarrow$ set retention to `14` days.
   - Check **Enable versioning for blobs** $\rightarrow$ select *Keep all versions*.
3. Click **Save** on the top toolbar.

### Task 4: Creating a File Share with SMB Protocol
1. In the left navigation menu under **Data storage**, click **File shares**.
2. Click **+ File share**:
   - **Name:** `corp-payroll-share`.
   - **Access tier:** Select **Transaction optimized** (or Hot).
3. Click **Review + create** $\rightarrow$ **Create**.
4. Click on `corp-payroll-share` $\rightarrow$ click **Connect** on the toolbar:
   - Select **Windows**, **Linux**, or **macOS**.
   - Notice that Azure generates a complete ready-to-run PowerShell script that maps drive `Z:` to the cloud share using SMB port 445!

---

## 🔬 Stage 6: Hands-On Enterprise Lab Bridge

To apply these storage principles, configure lifecycle rules, test blob versioning, and generate revocable SAS tokens, proceed directly to the comprehensive practical lab:

> [!TIP]
> **Practical Implementation Companion:**
> Access the comprehensive engineering lab at:
> **[[Lab-08_Storage_Redundancy_Lifecycle_and_User_Delegation_SAS|Lab 08: Storage Account Redundancy, Lifecycle Automation, WORM & User Delegation SAS]]**
> 
> *Target Lab File:* `Projects/AZ-104/08_Storage_Accounts_and_Data_Protection/Lab-08_Storage_Redundancy_Lifecycle_and_User_Delegation_SAS.md`

### Lab Objectives Matrix:

```text
+-----------------------------------------------------------------------------------------+
| Lab 08 Enterprise Milestone Goals                                                       |
+-----------------------------------------------------------------------------------------+
| 1. Provision an Azure Storage Account with Zone-Redundant Storage (ZRS)                 |
| 2. Deploy Lifecycle Management rules to automate Hot -> Cool -> Archive -> Delete tiers |
| 3. Configure Blob Versioning and test 14-day Soft Delete recovery directly in GUI      |
| 4. Generate User Delegation SAS tokens signed via Microsoft Entra ID                    |
| 5. Deploy an Azure File Share and inspect SMB 3.0 mount commands                        |
+-----------------------------------------------------------------------------------------+
```

---

## ⚠️ Stage 7: "See It in Action" Real-World Failure & Recovery Loop (AARF)

### Scenario: The "Inaccessible Archived Blob" Production Outage

#### 1. The Architectural Setup & Assumptions
A financial institution archives customer tax returns into an Azure Blob Storage container (`tax-returns`). An automated Lifecycle Management policy runs daily and moves any PDF untouched for 90 days into the **Archive** access tier to slash storage costs.

#### 2. The Production Failure Manifestation
An auditor requests a tax return from 2 years ago (`return_2024_0912.pdf`). A customer service representative searches the internal CRM, finds the file link, and clicks *Download*. The application crashes with the following error:

```text
HTTP 409 Conflict
ErrorCode: BlobArchived
ErrorMessage: This operation is not permitted on an archived blob.
RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

The representative panics, believing the customer's financial record was corrupted or lost!

#### 3. Root Cause Analysis (RCA) & Deep Investigation
Why did the download fail with `HTTP 409 Conflict`?
1. **The Nature of the Archive Tier:** The Archive tier is an **offline storage medium**. The underlying storage blocks are unmounted and spun down to minimize electrical power and hardware costs.
2. **Direct Read Impossibility:** While a blob is in the Archive tier, it **CANNOT be read, downloaded, or copied directly** over HTTP GET.
3. **The Mandatory Rehydration Step:** To read an archived blob, the blob must first be **rehydrated** back to an online access tier (Hot or Cool).
4. **The Latency Window:** Standard priority rehydration takes **up to 15 hours**. High-priority rehydration takes **under 1 hour** for blobs smaller than 10 GB.

#### 4. Remediation & Diagnostic Verification Loop

```mermaid
flowchart TD
    Error409["Application Error: HTTP 409 BlobArchived"] --> Step1["Check Blob Properties: Access Tier = Archive"]
    Step1 --> Step2["Initiate Rehydration: Change Tier back to Hot or Cool"]
    
    Step2 --> Choice{"Choose Rehydration Priority"}
    Choice -->|Standard Priority (Free / Default)| P1["Takes up to 15 hours"]
    Choice -->|High Priority (Expedited / Paid)| P2["Completes in < 1 hour for blobs < 10GB"]
    
    P1 --> StatusCheck["Monitor Archive Status: 'rehydrate-pending-to-hot'"]
    P2 --> StatusCheck
    
    StatusCheck --> Complete["Rehydration Complete: Blob status returns to 'Hot'"]
    Complete --> Restored["Application executes HTTP GET -> Download Succeeds!"]
```

```bash
# Diagnostic & Remediation Script (Azure CLI)

# 1. Inspect blob tier and rehydration status
az storage blob show \
  --account-name "stenterpriseblob2026" \
  --container-name "tax-returns" \
  --name "return_2024_0912.pdf" \
  --query "{Tier:properties.blobTier, Status:properties.rehydrationStatus}"

# 2. Initiate High-Priority Rehydration to Hot Tier
az storage blob set-tier \
  --account-name "stenterpriseblob2026" \
  --container-name "tax-returns" \
  --name "return_2024_0912.pdf" \
  --tier "Hot" \
  --rehydrate-priority "High"
```

---

## 💡 Stage 8: High-Yield AZ-104 Exam Scenarios & Trick Question Traps

### Trick Question Trap 1: The Only Way to Revoke a Leaked Service SAS
* **The Scenario:** A contractor is given a Service SAS token valid for 6 months. After 2 weeks, the contractor leaves the company. You must immediately invalidate their SAS token without impacting other production applications using the storage account.
* **The Trap:** The exam suggests "Delete the user account" or "Change the container permissions".
* **The Ground Truth:** If the SAS was generated as an ad-hoc SAS, the ONLY way to revoke it is to rotate the master storage account key (which breaks all other apps!). However, if the SAS was associated with a **Stored Access Policy (SAP)**, you simply **delete or modify the Stored Access Policy**, which immediately invalidates the SAS token without affecting master keys!

### Trick Question Trap 2: Early Deletion Penalties in Cool and Archive Tiers
* **The Scenario:** An administrator creates a blob in the **Cool** tier. Five days later, the application deletes the blob.
* **The Question:** How is the company billed?
* **The Ground Truth:** The Cool tier has a **30-day minimum retention period**. If a blob is deleted after 5 days, Azure bills you for the 5 days of actual storage PLUS a **prorated early deletion fee for the remaining 25 days**! (Archive tier has a 180-day minimum, Cold has a 90-day minimum).

### Trick Question Trap 3: Storage Account Level Public Access Override
* **The Scenario:** An administrator sets a container's access level to `Container (anonymous read access for containers and blobs)`. However, external anonymous web users still receive `HTTP 403 Forbidden` when attempting to access blobs.
* **The Trap:** Why are external users blocked?
* **The Ground Truth:** In modern storage accounts, the account-level setting **"Allow Blob public access"** defaults to `Disabled`. If disabled at the storage account level, it strictly overrides and blocks all container-level anonymous access!

### Trick Question Trap 4: Azure Files SMB Port 445 Blocking
* **The Scenario:** An employee attempts to mount an Azure Files SMB share (`\\stacc.file.core.windows.net\share`) from their home office Wi-Fi, but the connection times out.
* **The Trap:** Why does it fail from home but work from the corporate office?
* **The Ground Truth:** SMB 3.0 communicates over **TCP port 445**. Most residential Internet Service Providers (ISPs) block outbound port 445 by default to prevent legacy SMB malware attacks. To access Azure Files from home, users must use a VPN, ExpressRoute, or switch to Azure File Sync / REST endpoints.

---

## 🌐 Authoritative References & Inflow Citations

* **Udemy AZ-104 Master Class by Scott Duffy:** [Inflow: Module 04 - Administer Azure Storage](file:///F:/Dump%20one/BrainDump/inflow/AZ-104-ScottDuffy/04_Administer_Azure_Storage.md)
* **John Savill’s Azure Master Class & Deep Dives:** Storage Redundancy Mathematics, Synchronous vs. Asynchronous Replication, Elastic SAN, and User Delegation SAS.
* **Moe Intelligence AZ-104 Video Curriculum:** Lessons 30 through 34 (Storage Accounts, Replication, Blob Tiers, Lifecycle Rules).
* **KodeKloud AZ-104 Course:** [Administer Azure Storage Module](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Module-Introduction/page.md)
* **Official Microsoft Learn Documentation:**
  - [Azure Storage account overview](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview)
  - [Azure Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)
  - [Optimize costs by automatically managing the data lifecycle](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)
  - [Grant limited access to Azure Storage resources using SAS](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview)