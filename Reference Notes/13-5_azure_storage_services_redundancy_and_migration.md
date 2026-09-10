---
obsidianUIMode: preview
class: reference-note
tier: reference-note
tags:
  - azure/storage
  - azure/az-900
  - azure/redundancy
  - azure/migration
---

# Module 13-5: Storage Accounts, Data Redundancy & Migration

**Breadcrumbs:** [[--Index--|🏠 Index]] > [[13-Index - Azure|☁️ Azure Reference MOC]] > **Module 13-5**

---

## 1. The Azure Storage Account Architecture

An **Azure Storage Account** provides a unique global namespace in the cloud for your data. Every object stored in Azure Storage has an address that includes your unique account name (e.g. `https://mystorageaccount.blob.core.windows.net`).

```mermaid
flowchart TD
    subgraph StorageAccount ["Azure Storage Account Namespace (mystorageaccount)"]
        Blob["🪣 Azure Blobs<br/>(Massive Unstructured Data,<br/>Containers, Data Lake Gen2)"]
        File["📁 Azure Files<br/>(Managed SMB 3.0 / NFS Shares,<br/>Multi-VM Mountable)"]
        Queue["📬 Azure Queues<br/>(Asynchronous Messaging Store,<br/>Decoupled Workflows)"]
        Table["🗂️ Azure Tables<br/>(NoSQL Key-Value Store,<br/>Schema-less Datasets)"]
    end
```

### 1.1 The Four Core Storage Services
1. **Azure Blob Storage:**
   - Object storage solution optimized for storing massive amounts of unstructured data (text or binary).
   - Structured into **Storage Account ➔ Container ➔ Blob**.
   - **Blob Types:**
     - **Block Blobs:** Standard files, documents, media streams, and backups (up to ~190.7 TiB).
     - **Append Blobs:** Optimized for append operations (e.g., continuous log files).
     - **Page Blobs:** Random-access 512-byte pages used for Azure Virtual Machine Virtual Hard Disks (VHDs).
2. **Azure Files:**
   - Fully managed file shares in the cloud accessible via industry-standard **SMB (Server Message Block) 3.0** and **NFS (Network File System)** protocols.
   - Can be mounted concurrently by cloud VMs (Windows, Linux, macOS) or on-premises servers without running a dedicated file server VM.
3. **Azure Queues:**
   - Reliable messaging store capable of storing millions of messages (up to 64 KB each) for asynchronous task processing between application components.
4. **Azure Tables:**
   - Low-cost NoSQL key-value store for rapid development with massive semi-structured datasets.

---

## 2. Blob Access Tiers & Lifecycle Management

Azure provides four distinct access tiers for Blob Storage to optimize costs based on access frequency:

```mermaid
graph LR
    Hot["🔥 Hot Tier<br/>• Active data<br/>• Low access cost<br/>• High storage cost"]
    Cool["❄️ Cool Tier<br/>• Infrequent access<br/>• 30-day min retention<br/>• Lower storage cost"]
    Cold["🧊 Cold Tier<br/>• Rare access<br/>• 90-day min retention<br/>• Very low storage cost"]
    Archive["📦 Archive Tier<br/>• Offline long-term<br/>• 180-day min retention<br/>• Hours rehydration"]

    Hot -->|"Auto-Transition (Lifecycle Policy)"| Cool
    Cool --> Cold
    Cold --> Archive
```

| Access Tier | Typical Access Frequency | Minimum Storage Duration | Rehydration Latency | Primary Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **Hot** | Frequent / Daily | None | Immediate (ms) | Active websites, live media streaming, active processing. |
| **Cool** | Infrequent (Monthly) | 30 days | Immediate (ms) | Short-term backups, older telemetry, staging data. |
| **Cold** | Rare (Quarterly) | 90 days | Immediate (ms) | Secondary backups, compliance logs accessed rarely. |
| **Archive** | Exceptional (Years) | 180 days | **Hours (High/Standard Priority)** | Long-term legal retention, regulatory compliance archives. |

> [!CAUTION]
> **Archive Rehydration Trap:** Data in the Archive tier is **offline** and cannot be read directly. To read an archived blob, you must first **rehydrate** it to the Hot, Cool, or Cold tier (which takes several hours). Attempting an immediate read API call fails with `BlobArchived`.

---

## 3. Data Redundancy Strategies

Azure Storage always replicates multiple copies of your data to protect against planned and unplanned events (hardware failures, power outages, natural disasters):

```mermaid
graph TD
    subgraph PrimaryRegion ["Primary Region"]
        subgraph LRS_Design ["LRS (Locally Redundant)"]
            DC1["Datacenter A<br/>[Copy 1] [Copy 2] [Copy 3]"]
        end
        subgraph ZRS_Design ["ZRS (Zone-Redundant)"]
            AZ1["AZ 1 [Copy 1]"]
            AZ2["AZ 2 [Copy 2]"]
            AZ3["AZ 3 [Copy 3]"]
        end
    end

    subgraph SecondaryRegion ["Secondary Paired Region (>300 miles)"]
        subgraph GRS_Design ["GRS / GZRS Replica"]
            SecDC["Secondary Datacenter<br/>[Copy 4] [Copy 5] [Copy 6]"]
        end
    end

    LRS_Design -->|"Asynchronous Geo-Replication"| GRS_Design
    ZRS_Design -->|"Asynchronous Geo-Replication"| GRS_Design
```

### 3.1 Primary Region Redundancy
1. **Locally Redundant Storage (LRS):**
   - Replicates your data **three times within a single physical datacenter**.
   - Lowest-cost redundancy option; provides at least **99.999999999% (11 nines)** of durability over a given year.
   - Vulnerable if an entire datacenter suffers a catastrophic flood or fire.
2. **Zone-Redundant Storage (ZRS):**
   - Replicates data synchronously across **three distinct Azure Availability Zones** in the primary region.
   - Provides at least **12 nines** of durability. Withstands datacenter-level outages.

### 3.2 Secondary Region Redundancy (Disaster Recovery)
3. **Geo-Redundant Storage (GRS):**
   - Combines **LRS in the primary region** (3 copies) with **LRS in a secondary paired region** (3 copies asynchronously replicated >300 miles away).
   - Provides **16 nines** of durability.
4. **Geo-Zone-Redundant Storage (GZRS):**
   - Combines **ZRS in the primary region** (3 copies across 3 AZs) with **LRS in the secondary paired region**.
   - Maximum enterprise resiliency; provides **16 nines** of durability and protection against both regional disasters and zone failures.
5. **Read-Access Options (RA-GRS & RA-GZRS):**
   - By default, the secondary region in GRS/GZRS is dark until Microsoft initiates a failover.
   - Enabling **Read-Access** provides a secondary read-only DNS endpoint (`mystorageaccount-secondary.blob.core.windows.net`), allowing applications to read data from the secondary region during primary degradation.

---

## 4. Migration & Bulk Data Transfer Options

### 4.1 Azure Migrate
A centralized hub to discover, assess, and migrate on-premises workloads, virtual machines (VMware, Hyper-V, physical servers), databases, and web applications to Azure with automated readiness reports and cost estimations.

### 4.2 The Azure Data Box Family (Physical Appliances)
For transferring terabytes or petabytes of data where internet network upload would take weeks or months:

| Appliance | Usable Capacity | Form Factor | Connection Interface |
| :--- | :--- | :--- | :--- |
| **Data Box Disk** | 8 TB per disk (up to 35 TB pack) | Ruggedized SSDs | USB 3.0 / SATA |
| **Data Box** | 80 TB usable (100 TB raw) | 50 lb Ruggedized Box | 1x 1GbE / 2x 10GbE RJ45/SFP+ |
| **Data Box Heavy** | 800 TB usable (1 PB raw) | 500 lb Wheeled Case | Multiple 40 GbE optical ports |

### 4.3 Command-Line & Desktop Utilities
- **AzCopy:** High-performance command-line utility optimized for copying blobs or files to and from a storage account via SAS tokens.
- **Azure Storage Explorer:** Free standalone GUI application for Windows, macOS, and Linux to easily manage Azure storage resources.

---

## 5. 🌉 Cognitive Comparative Bridge: Azure Storage vs. AWS

```mermaid
flowchart LR
    subgraph AzureStorage ["Azure Storage"]
        AzAccount["Unified Storage Account"]
        AzBlob["Azure Blob (Containers)"]
        AzFile["Azure Files (SMB / NFS)"]
        AzTiers["Hot / Cool / Cold / Archive"]
        AzRedundancy["LRS / ZRS / GRS / GZRS"]
        AzBox["Azure Data Box Family"]
    end

    subgraph AWSStorage ["AWS Storage"]
        AWSNone["❌ No Single Namespace Container"]
        AWSS3["Amazon S3 (Buckets)"]
        AWSEFS["Amazon EFS / FSx"]
        AWSTiers["S3 Standard / IA / Glacier"]
        AWSRedundancy["Standard / OneZone / CRR"]
        AWSSnow["AWS Snowball / Snowmobile"]
    end

    AzAccount -.-> AWSNone
    AzBlob <--> AWSS3
    AzFile <--> AWSEFS
    AzTiers <--> AWSTiers
    AzRedundancy <--> AWSRedundancy
    AzBox <--> AWSSnow
```

### Key Differences to Note:
1. **The Unified Namespace Concept:** In AWS, S3 (object), EFS (file), and SQS (queue) are entirely distinct services with separate consoles and authorization models. In Azure, a **Storage Account** is a single overarching administrative boundary that unifies Blobs, Files, Queues, and Tables under one encryption key, one network firewall, and one redundancy configuration.
2. **Azure Files SMB Compatibility:** Azure Files supports direct mounting via standard SMB 3.0 over internet port 445 (with encryption), allowing on-premises legacy desktop apps to connect directly to cloud file shares without a dedicated VPN gateway.

<!-- Documentation References -->
[Microsoft Learn: Azure Storage account overview](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview)
[Microsoft Learn: Azure Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)
[Microsoft Learn: Blob storage access tiers](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview)
