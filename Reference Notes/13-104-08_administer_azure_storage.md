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

## 🎯 Executive Overview & Storage Architecture

Azure Storage is Microsoft's cloud storage platform providing highly available, massively scalable, durable, and secure storage for data objects, virtual machine disks, managed file shares, messaging queues, and NoSQL tables. Azure Storage accounts expose a unified namespace across five core storage services:

```mermaid
flowchart TD
    subgraph StorageAccountRoot ["Azure Storage Account Namespace (https://<account>.*.core.windows.net)"]
        BlobSvc["Azure Blob Storage\n(https://<acc>.blob.core.windows.net)\n- Block Blobs (Unstructured Data, Media)\n- Append Blobs (Logs)\n- Page Blobs (VM VHD Disks)"]
        FileSvc["Azure Files\n(https://<acc>.file.core.windows.net)\n- Fully Managed SMB 3.0 / NFS 4.1 Shares\n- Azure File Sync Integration"]
        QueueSvc["Azure Queues\n(https://<acc>.queue.core.windows.net)\n- Asynchronous Workload Messaging"]
        TableSvc["Azure Tables\n(https://<acc>.table.core.windows.net)\n- NoSQL Key-Attribute Data Store"]
        DLSvc["Azure Data Lake Storage Gen2\n(https://<acc>.dfs.core.windows.net)\n- Hierarchical Namespace & Big Data Analytics"]
    end

    subgraph SecurityControls ["Storage Security & Access Perimeter"]
        FW["Storage Firewall & VNets\n(Private Endpoints / Service Endpoints)"]
        Authn["Authentication Tiers\n(Entra ID RBAC vs. SAS Tokens vs. Access Keys)"]
        Crypt["Encryption at Rest\n(SSE with PMK or CMK in Key Vault)"]
    end

    SecurityControls --> StorageAccountRoot
```

---

## 🏛️ Storage Account Kinds & Performance Tiers

| Storage Account Kind | Supported Services | Performance Tiers | Target Workloads & Architecture |
| :--- | :--- | :---: | :--- |
| **General-purpose v2 (GPv2)** | Blobs, Files, Queues, Tables, Data Lake Gen2 | Standard (HDD) / Premium (SSD) | **Default choice for modern workloads.** Delivers the lowest per-gigabyte storage costs and full support for all replication tiers and lifecycle management. |
| **BlockBlobStorage** | Block Blobs, Append Blobs | **Premium Only** (SSD) | High-transaction workloads, low-latency analytics, processing small files with sustained high I/O throughput. |
| **FileStorage** | Azure Files Only | **Premium Only** (SSD) | Enterprise I/O-intensive file sharing, virtual desktop infrastructure (FSLogix profiles), high-performance databases over SMB/NFS. |
| **PageBlobStorage** | Page Blobs Only | **Premium Only** (SSD) | Unmanaged VM OS and data disks (legacy; modern architectures prioritize Managed Disks). |

---

## 🔄 Data Redundancy Strategies & Durability SLA

Azure Storage automatically replicates data to guard against transient hardware failures, datacenter network/power outages, and regional natural disasters:

```mermaid
flowchart LR
    subgraph LocalRedundancy ["Primary Region (Region A)"]
        subgraph Datacenter1 ["Datacenter (Fault Domain 1-3)"]
            LRS_Copy["LRS: 3 Replicas in 1 Datacenter\n(11 9s Durability)"]
        end
        subgraph AZs ["Availability Zones (AZ 1, 2, 3)"]
            ZRS_Copy["ZRS: 3 Replicas across 3 AZs\n(12 9s Durability)"]
        end
    end

    subgraph GeoRedundancy ["Secondary Paired Region (Region B)"]
        GRS_Copy["GRS / GZRS Secondary\n(Asynchronously replicated 3 copies via LRS)\n(16 9s Durability)"]
        RAGRS_Copy["RA-GRS / RA-GZRS Endpoint\n(Read-only secondary access: <acc>-secondary.blob)"]
    end

    LRS_Copy -.->|Async Geo-Replication| GRS_Copy
    ZRS_Copy -.->|Async Geo-Replication| GZRS_Copy
    GRS_Copy --- RAGRS_Copy
```

### Redundancy Model Comparison Table

| Replication Strategy | Primary Region Copies | Secondary Region Copies | Durability (Annual SLA) | Secondary Read Access | Failover Mechanics |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Locally Redundant (LRS)** | 3 copies in single DC | None | 99.999999999% (11 9s) | ❌ No | N/A |
| **Zone-Redundant (ZRS)** | 3 copies across 3 AZs | None | 99.9999999999% (12 9s) | ❌ No | N/A (Survives single AZ outage) |
| **Geo-Redundant (GRS)** | 3 copies via LRS | 3 copies via LRS | 99.99999999999999% (16 9s)| ❌ No (Write/Read primary only) | Customer-initiated account failover |
| **Read-Access GRS (RA-GRS)**| 3 copies via LRS | 3 copies via LRS | 99.99999999999999% (16 9s)| ✅ **Yes** (`<acc>-secondary`) | Secondary read-only without failover |
| **Geo-Zone-Redundant (GZRS)**| 3 copies across 3 AZs | 3 copies via LRS | 99.99999999999999% (16 9s)| ❌ No | Customer-initiated account failover |
| **Read-Access GZRS (RA-GZRS)**| 3 copies across 3 AZs | 3 copies via LRS | 99.99999999999999% (16 9s)| ✅ **Yes** (`<acc>-secondary`) | Secondary read-only without failover |

---

## 📦 Blob Storage Access Tiers & Lifecycle Management

Azure Blob Storage provides four distinct storage access tiers tailored to data access patterns and retention costs:

```mermaid
flowchart LR
    HotTier["Hot Access Tier\n(Frequent Access)\n- Highest storage cost\n- Lowest access cost\n- 0 days minimum"]
    CoolTier["Cool Access Tier\n(Infrequent Access)\n- Lower storage cost\n- Higher access cost\n- 30 days minimum"]
    ColdTier["Cold Access Tier\n(Rare Access)\n- Much lower storage cost\n- Higher access cost\n- 90 days minimum"]
    ArchiveTier["Archive Access Tier\n(Offline Long-term)\n- Lowest storage cost\n- Highest access cost\n- 180 days minimum\n- Blobs are OFFLINE"]

    HotTier -->|After 30 Days Inactive| CoolTier
    CoolTier -->|After 90 Days Inactive| ColdTier
    ColdTier -->|After 180 Days Inactive| ArchiveTier
    ArchiveTier -.->|Rehydration (Standard: 15h / High: <1h)| HotTier
```

### Tier Comparison Details

| Tier Name | Online Status | Minimum Retention | Early Deletion Penalty | Rehydration Latency | Ideal Use Case |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Hot** | Online | None | None | Instantaneous | Actively read/written data, application assets, active databases. |
| **Cool** | Online | **30 days** | Yes (Pro-rated for 30 days) | Instantaneous | Short-term backups, raw data to be processed later, monthly reports. |
| **Cold** | Online | **90 days** | Yes (Pro-rated for 90 days) | Instantaneous | Access once or twice a year, archival data requiring fast search. |
| **Archive** | **Offline** | **180 days** | Yes (Pro-rated for 180 days)| **1 to 15 hours** | Regulatory compliance, healthcare records, long-term backups. |

### Lifecycle Management JSON Rule
Lifecycle management runs once every 24 hours to automatically transition or purge blobs:

```json
{
  "rules": [
    {
      "enabled": true,
      "name": "ArchiveAndPurgeComplianceLogs",
      "type": "Lifecycle",
      "definition": {
        "filters": {
          "blobTypes": ["blockBlob"],
          "prefixMatch": ["auditlogs/"]
        },
        "actions": {
          "baseBlob": {
            "tierToCool": { "daysAfterModificationGreaterThan": 30 },
            "tierToArchive": { "daysAfterModificationGreaterThan": 90 },
            "delete": { "daysAfterModificationGreaterThan": 2555 }
          }
        }
      }
    }
  ]
}
```

---

## 📁 Azure Files & Azure File Sync

### Azure Files Protocol Support
- **SMB 3.0:** Native Windows, Linux, and macOS file share integration with Active Directory Domain Services (AD DS) and Microsoft Entra Kerberos authentication.
- **NFS 4.1:** Native Linux enterprise file sharing (requires Premium FileStorage accounts and VNet Private Endpoints).

### Azure File Sync Architecture
Azure File Sync enables centralizing an organization's file shares in Azure Files while preserving local caching performance on Windows File Servers:

```mermaid
flowchart TD
    CloudShare["Azure Files Cloud Endpoint\n(Master Central Repository)"]
    
    SyncGroup["Sync Group"]
    CloudShare --- SyncGroup

    subgraph BranchA ["Branch Office New York"]
        Server1["Windows Server A (Server Endpoint)\n- Local Cache: D:\Shares\Corp\n- Cloud Tiering: ENABLED (20% free space buffer)"]
    end

    subgraph BranchB ["Branch Office London"]
        Server2["Windows Server B (Server Endpoint)\n- Local Cache: E:\Shares\Corp\n- Cloud Tiering: ENABLED"]
    end

    SyncGroup <-->|Sync Agent over TLS 443| Server1
    SyncGroup <-->|Sync Agent over TLS 443| Server2
```

- **Cloud Tiering:** Separates frequently accessed "hot" files (cached locally on the server) from infrequently accessed "cold" files (tiered to Azure Files as pointer stubs). Saves substantial on-premises disk storage without breaking file system paths.

---

## 🔐 Securing Azure Storage: Access Keys, SAS & Entra ID

Azure Storage provides three distinct authentication and authorization tiers:

```mermaid
flowchart TD
    AuthMethod{"Choose Storage Access Method"}
    
    AuthMethod -->|Root Control / Automation| Keys["1. Storage Account Access Keys (Key 1 & Key 2)\n- Complete administrative control\n- Full read/write/delete to all services\n- High security risk if leaked"]
    AuthMethod -->|Delegated Scoped Access| SAS["2. Shared Access Signatures (SAS)\n- Time-limited (Start / Expiry)\n- Restricted IP addresses\n- Read, Write, or Delete permissions"]
    AuthMethod -->|Enterprise Zero-Trust| Entra["3. Microsoft Entra ID (Azure RBAC)\n- Granular data plane roles\n- MFA & Conditional Access\n- Audit logging in Entra ID"]
    
    SAS --> SASType{"SAS Types"}
    SASType --> UserDelegationSAS["User Delegation SAS (Most Secure - Signed with Entra ID)"]
    SASType --> ServiceSAS["Service SAS (Scoped to 1 resource, e.g. 1 container)"]
    SASType --> AccountSAS["Account SAS (Scoped across account services)"]
```

### Shared Access Signature (SAS) Types & Revocation
1. **User Delegation SAS:** Signed using **Microsoft Entra ID credentials** rather than the account root key. If an administrator revokes the user's role or password, the SAS token is immediately invalidated.
2. **Service SAS & Account SAS:** Signed using the primary or secondary storage access key.
3. **Stored Access Policy:** Configured on a container or file share to manage Service SAS tokens. Allows administrators to **change start/expiry times or revoke access immediately** without rotating the entire storage account key.

### Data Plane RBAC Roles vs. Management Roles
- **Contributor:** Can manage storage account properties (replication, firewall, keys), but **CANNOT read blob data**.
- **Storage Blob Data Contributor:** Can read, write, and delete blobs within containers.
- **Storage Blob Data Reader:** Can read blob contents and metadata.

---

## 🛠️ Contextual Proof of Concept: CLI Automation

```bash
# 1. Create a General Purpose v2 Storage Account with GZRS redundancy and TLS 1.2
az storage account create \
  --resource-group "rg-enterprise-core" \
  --name "staz104corpstore" \
  --location "eastus" \
  --sku "Standard_GZRS" \
  --kind "StorageV2" \
  --access-tier "Hot" \
  --min-tls-version "TLS1_2" \
  --allow-blob-public-access false

# 2. Create a private Blob Container
az storage container create \
  --account-name "staz104corpstore" \
  --name "confidential-assets" \
  --auth-mode login

# 3. Create a Stored Access Policy on the container
az storage container policy create \
  --account-name "staz104corpstore" \
  --container-name "confidential-assets" \
  --name "Policy-AuditTeam-Read" \
  --permissions "r" \
  --expiry "2026-12-31T23:59:59Z" \
  --auth-mode key

# 4. Generate a Service SAS token bound to the Stored Access Policy
az storage container generate-sas \
  --account-name "staz104corpstore" \
  --name "confidential-assets" \
  --policy-name "Policy-AuditTeam-Read" \
  --output tsv
```

---

## 🔍 Deep-Intuition AARF Framework

### Scenario: Diagnosing Inaccessible Blobs in the Archive Access Tier

- **The Answer (Core Configuration):** Initiate blob rehydration by changing the blob's access tier back to `Hot` or `Cool` using `az storage blob set-tier --account-name "stprod" --container-name "data" --name "archive.tar.gz" --tier "Hot" --rehydrate-priority "High"`.
- **The Assumptions (Prerequisites):** 
  - Blob is currently residing in the `Archive` access tier.
  - Client application requires reading or downloading the blob content.
- **The Rationale (Why):** The Archive access tier is an offline storage medium (similar to tape or deep cold storage disks). When a blob is tiered to Archive, its data blocks are taken completely offline. The storage engine does not support direct streaming or reads while a blob is archived.
- **The Failure Loop (What if misconfigured):**
  - *Symptom:* Application attempts to read or download an archived blob via HTTP GET.
  - *HTTP Status Code:* `409 Conflict`.
  - *Error Response:* `<Error><Code>BlobArchived</Code><Message>This operation is not permitted on an archived blob.</Message></Error>`.
- **The Alternative Case (When to use 'if not'):** If the application requires low-latency, immediate read access while still minimizing storage costs, store the data in the **Cold** tier (90-day minimum retention) or **Cool** tier (30-day minimum retention), both of which support instantaneous online access without rehydration delays.

---

## 💡 AZ-104 Exam Tips & Gotchas

> [!TIP]
> **Zero Downtime Access Key Rotation Procedure:**
> 1. Applications are configured to use **Key 1**.
> 2. Update application configuration connection strings to use **Key 2**.
> 3. Regenerate **Key 1** in the portal or via CLI (`az storage account keys renew --key primary`).
> 4. Update applications to use the newly regenerated **Key 1**.
> 5. Regenerate **Key 2** (`az storage account keys renew --key secondary`).

> [!WARNING]
> **Public Access vs. Container Access Levels:**
> - In modern Azure Storage accounts, the account-level setting **"Allow Blob public access"** defaults to `Disabled`.
> - If public access is disabled at the storage account level, even if an administrator sets a container's access level to `Container (anonymous read access for containers and blobs)`, anonymous requests will be **blocked by the account-level policy**.

---

## 🌐 Authoritative References & Citations

- [KodeKloud AZ-104 Course - Administer Azure Storage Module](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Module-Introduction/page.md)
- [Microsoft Learn: Configure storage accounts and blob storage](https://learn.microsoft.com/en-us/training/modules/configure-storage-accounts/)
- [Microsoft Learn: Secure your Azure Storage data](https://learn.microsoft.com/en-us/training/modules/secure-azure-storage-account/)
- [Azure Storage Redundancy Technical Documentation](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)
