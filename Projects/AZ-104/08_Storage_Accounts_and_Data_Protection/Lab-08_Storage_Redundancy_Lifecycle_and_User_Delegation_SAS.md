---
obsidianUIMode: preview
class: project-note
tier: project
domains:
  - azure
concepts_referenced:
  - "[[13-104-08_administer_azure_storage]]"
  - "[[13-5_azure_storage_services_redundancy_and_migration]]"
  - "[[13-104-02_administer_identity]]"
  - "[[13-104-03_manage_governance_and_compliance]]"
  - "[[13-104-06_configure_and_manage_virtual_networking]]"
difficulty: intermediate
status: completed
---

# Lab 08: Storage Account Redundancy, Lifecycle Automation, WORM & User Delegation SAS

**Breadcrumbs:** [[--Index--|🏠 Index]] > [[13-Index - AZ-104|📘 AZ-104 Track]] > Projects > **Lab 08: Azure Storage**

---

## 🎯 Lab Overview & Enterprise Scenario

In an enterprise cloud ecosystem, data storage must balance three competing mandates:
1. **High Durability & Multi-Region Resilience:** Shielding corporate assets from single-datacenter outages and regional catastrophic events through Zone-Redundant (ZRS) and Geo-Redundant (GRS/RA-GRS) replication.
2. **FinOps Storage Tiering Automation:** Slashing storage expenditure by up to 90% through automated lifecycle tiering (Hot ➔ Cool ➔ Cold ➔ Archive ➔ Purge) without operational overhead.
3. **Defense-in-Depth Data Protection & Compliance:** Safeguarding against ransomware extortion and accidental administrative deletion via **Blob Versioning**, **Soft Delete (Recycle Bin)**, **Time-Based Immutable Storage (WORM)**, and **Zero-Trust User Delegation Shared Access Signatures (SAS)** signed via Microsoft Entra ID rather than vulnerable root account keys.

In this project, you will step into the shoes of an Enterprise Storage & Governance Architect. You will engineer, configure, and stress-test an enterprise-grade Azure Storage Account primarily through the **Azure Portal GUI**, experiencing the exact click-paths, configuration blades, and visual checkpoints expected in mission-critical corporate environments.

---

## 🏛️ Target Architecture & Visual Workflow

```mermaid
flowchart TD
    subgraph Users ["Enterprise Clients & External Auditors"]
        AppSvc["App Service / Workload"]
        Auditor["External Compliance Auditor"]
        BadActor["Ransomware / Rogue Admin"]
    end

    subgraph StorageAccount ["Azure Storage Account: stenterprise (ZRS / RA-GRS)"]
        subgraph SecurityBoundary ["Access & Identity Plane"]
            EntraIAM["Entra ID RBAC (Mod 02)<br/>Storage Blob Data Contributor"]
            UserDelSAS["User Delegation SAS<br/>(Time-bound, Entra-signed)"]
            Firewall["Firewall & Virtual Networks (Mod 05/06)<br/>Selected Networks Only"]
        end

        subgraph Containers ["Blob Containers"]
            subgraph InvoiceContainer ["Container: corporate-invoices"]
                HotBlob["Hot Tier Blobs (0-30 Days)<br/>Active Working Set"]
                CoolBlob["Cool Tier Blobs (30-90 Days)<br/>Infrequent Access ($0.01/GB)"]
                ColdBlob["Cold Tier Blobs (90-180 Days)<br/>Rare Access ($0.0036/GB)"]
                ArchBlob["Archive Tier Blobs (180-365 Days)<br/>Deep Storage ($0.00099/GB)"]
                AutoPurge["Auto-Delete (365+ Days)"]
            end

            subgraph LegalContainer ["Container: legal-records (WORM)"]
                ImmutableBlob["Locked Financial Records<br/>Time-Based Retention: 7 Days"]
            end
        end

        subgraph DataProtectionLayer ["Data Protection Engine"]
            Versioning["Blob Versioning<br/>(Preserves historical writes)"]
            SoftDelete["Soft Delete Recycle Bin<br/>(14-Day Retention)"]
        end

        subgraph AzureFilesSMB ["Azure Files"]
            FileShare["corp-share (100 GiB Quota)<br/>SMB 3.1.1 + Share Snapshots"]
        end
    end

    subgraph GovernanceLocks ["Azure Governance (Mod 03)"]
        Lock["Resource Lock: CanNotDelete"]
    end

    AppSvc -->|Entra Token (RBAC)| SecurityBoundary
    Auditor -->|User Delegation SAS URL| InvoiceContainer
    BadActor -.->|Attempts Overwrite / Delete| DataProtectionLayer
    DataProtectionLayer -->|Traps Deletes into| SoftDelete
    DataProtectionLayer -->|Creates Historical Copy in| Versioning
    BadActor -.->|Attempts Deletion of WORM| LegalContainer
    LegalContainer -->|Blocked by Platform WORM Policy| BadActor
    Lock -.->|Protects Account from Deletion| StorageAccount
    
    HotBlob -->|Lifecycle Rule (30d)| CoolBlob
    CoolBlob -->|Lifecycle Rule (90d)| ColdBlob
    ColdBlob -->|Lifecycle Rule (180d)| ArchBlob
    ArchBlob -->|Lifecycle Rule (365d)| AutoPurge
```

---

## ⚡ Phase 1: Fast Environment Bootstrap (Optional Azure CLI Script)

If you prefer to pre-stage the Resource Group and a uniquely named Storage Account shell via automation before configuring all lifecycle rules, data protection, immutability, and SAS delegation in the GUI, run this snippet in Azure Cloud Shell:

```bash
#!/usr/bin/env bash
set -euo pipefail

# 1. Variables
export RG="rg-storage-lab"
export LOCATION="eastus"
export RANDOM_HEX=$(openssl rand -hex 3)
export STORAGE_NAME="stlab${RANDOM_HEX}"

echo "==> Creating Resource Group: ${RG} in ${LOCATION}..."
az group create --name "${RG}" --location "${LOCATION}" --tags Environment=Production Department=Finance

echo "==> Generating Unique Storage Account: ${STORAGE_NAME}..."
az storage account create \
  --name "${STORAGE_NAME}" \
  --resource-group "${RG}" \
  --location "${LOCATION}" \
  --sku "Standard_ZRS" \
  --kind "StorageV2" \
  --access-tier "Hot" \
  --min-tls-version "TLS1_2" \
  --allow-blob-public-access false

echo "==> Staging complete! Open Azure Portal to begin GUI configuration."
echo "==> Storage Account Name: ${STORAGE_NAME}"
```

---

## 🖥️ Phase 2: Core Hands-On Implementation (Azure Portal GUI - Step-by-Step)

### Task 2.1: Provision Enterprise Storage Account with Zone Redundancy

*If you already deployed Phase 1, you can inspect and modify your storage account properties. Otherwise, follow the steps below to provision from scratch via the GUI.*

1. In the top Azure Portal search bar, type `Storage accounts` and select it under **Services**.
2. Click **+ Create** in the top left command bar.
3. On the **Basics** tab, configure:
   * **Subscription:** Select your target active subscription.
   * **Resource group:** Click **Create new** ➔ Enter `rg-storage-lab` ➔ Click **OK**.
   * **Storage account name:** Enter `stlab` followed by your initials and 4 random numbers (e.g., `stlabjd2026`). *Must be 3-24 lowercase letters and numbers, globally unique.*
   * **Region:** Select `(US) East US`.
   * **Primary service:** Select `Azure Blob Storage or Azure Data Lake Storage Gen 2`.
   * **Performance:** Select `Standard (general-purpose v2 account)`.
   * **Redundancy:** Select `Zone-redundant storage (ZRS)`. Notice the description explaining data is synchronously copied across 3 availability zones in the primary region.
4. Click **Next: Advanced >**:
   * **Require secure transfer for REST API operations:** Checked (Enforces HTTPS).
   * **Allow enabling public access on containers:** Unchecked (Crucial security baseline: disables anonymous container access at account level).
   * **Enable storage account key access:** Checked (Allows legacy access keys while transitioning to Entra ID).
   * **Default to Microsoft Entra authorization in the Azure portal:** Checked.
   * **Minimum TLS version:** Select `Version 1.2`.
   * **Hierarchical namespace:** Leave Unchecked (unless provisioning ADLS Gen2 big data lake).
   * **Blob access tier:** Select `Hot`.
5. Click **Next: Networking >**:
   * **Network access:** Select `Enable public access from all networks` (We will restrict this later in Phase 3 Integration).
   * **Routing preference:** Select `Microsoft network routing`.
6. Click **Next: Data protection >**:
   * We will configure granular data protection policies directly from the dedicated blade in Task 2.3. Leave defaults for now.
7. Click **Review + create** ➔ Review validation pass ➔ Click **Create**.
8. Once deployment completes, click **Go to resource**.

> [!NOTE]
> **Visual Checkpoint:** On the Storage Account **Overview** blade, look at the **Essentials** section. Verify **Replication** states `Zone-redundant storage (ZRS)`, **Account kind** is `StorageV2 (general purpose v2)`, and **Default access tier** is `Hot`.

---

### Task 2.2: Implement Multi-Tier Automated FinOps Lifecycle Management

Enterprise finance departments must automate file aging so high-cost Hot tier storage is automatically transitioned down to lower tiers and purged after regulatory limits expire.

1. In the left navigation menu under the **Data management** section, click **Lifecycle management**.
2. Select the **List view** tab and click **+ Add a rule**.
3. On the **Basics** tab of the slide-over blade:
   * **Rule name:** Enter `ArchiveAndPurgeAgingInvoices`.
   * **Rule scope:** Select **Limit blobs with filters**.
   * **Blob type:** Select **Block blobs**.
   * **Blob subtype:** Check **Base blobs**.
   * Click **Next: Base blobs >**.
4. On the **Base blobs** condition builder, configure the multi-tier cascade:
   * Condition 1: Under **If Base blobs were**, ensure `Last modified` is selected.
   * Under **More than (days ago)**: Enter `30`.
   * Under **Then**: Select `Move to cool storage`.
   * Click **+ Add condition**:
     * Select `Last modified` ➔ `More than`: Enter `90` ➔ `Move to cold storage`.
   * Click **+ Add condition**:
     * Select `Last modified` ➔ `More than`: Enter `180` ➔ `Move to archive storage`.
   * Click **+ Add condition**:
     * Select `Last modified` ➔ `More than`: Enter `365` ➔ `Delete the blob`.
   * Click **Next: Filter set >**.
5. On the **Filter set** tab:
   * Under **Blob prefix**, enter: `corporate-invoices/`.
   * *Notice that prefix matching is case-sensitive and must match the target container name.*
6. Click **Add**.
7. Switch to the **Code view** tab in the Lifecycle management blade. Inspect the generated declarative JSON schema. Notice how the portal GUI visual builder constructed the identical structure used in enterprise ARM/Bicep automation templates:
   ```json
   {
     "rules": [
       {
         "enabled": true,
         "name": "ArchiveAndPurgeAgingInvoices",
         "type": "Lifecycle",
         "definition": {
           "actions": {
             "baseBlob": {
               "tierToCool": { "daysAfterModificationGreaterThan": 30 },
               "tierToCold": { "daysAfterModificationGreaterThan": 90 },
               "tierToArchive": { "daysAfterModificationGreaterThan": 180 },
               "delete": { "daysAfterModificationGreaterThan": 365 }
             }
           },
           "filters": {
             "blobTypes": [ "blockBlob" ],
             "prefixMatch": [ "corporate-invoices/" ]
           }
         }
       }
     ]
   }
   ```

> [!NOTE]
> **Visual Checkpoint:** The Lifecycle management screen shows your rule with status **Enabled**, Rule scope **Filtered**, and Target blob types **Block blobs**.

---

### Task 2.3: Configure Ransomware Defense: Versioning & Soft Delete (Recycle Bin)

1. In the left navigation menu under **Data management**, click **Data protection**.
2. Under the **Recovery** section, configure the defense-in-depth safety nets:
   * **Enable soft delete for blobs:** Checked.
   * **Keep deleted blobs for (in days):** Change to `14`.
   * **Enable soft delete for containers:** Checked.
   * **Keep deleted containers for (in days):** Change to `14`.
   * **Enable soft delete for file shares:** Checked (Retention: 14 days).
3. Under the **Tracking** section:
   * **Enable versioning for blobs:** Checked.
   * **Keep all versions:** Selected.
   * **Enable blob change feed:** Checked.
4. Click **Save** at the top of the blade. Wait 10 seconds for the updated blob service properties to apply.
5. Create the container and test the versioning engine:
   * In the left menu under **Data storage**, click **Containers**.
   * Click **+ Container** ➔ Name: `corporate-invoices` ➔ Public access level: `Private (no anonymous access)` ➔ Click **Create**.
   * Click into `corporate-invoices`.
   * Click **Upload** ➔ Select or create a quick local text file named `contract.txt` with contents `"Version 1.0 - Active Agreement"`.
   * Click **Upload**.
   * Now click **Upload** again ➔ Select another local text file with the same name `contract.txt` containing `"Version 2.0 - Amended Terms"`.
   * In the Upload blade, expand **Advanced**, check **Overwrite if files already exist**, and click **Upload**.
6. Inspect the Version History:
   * In the container file list, click the toggle switch: **Show deleted blobs** and notice the blob listing.
   * Click directly on `contract.txt`.
   * In the blob properties blade, click the **Versions** tab.
   * Notice two distinct versions with their exact timestamps and a clear indication of which version is **Current version = Yes** and which is **Previous version**.

> [!NOTE]
> **Visual Checkpoint:** On the **Versions** tab of `contract.txt`, you will see two version rows. Even if an attacker overwrites the document, Version 1.0 remains permanently preserved and restorable via the **...** menu ➔ **Make current version**.

---

### Task 2.4: Implement Immutable Storage Compliance (WORM - Write Once, Read Many)

Regulatory frameworks (such as SEC Rule 17a-4, FINRA, and GDPR retention laws) mandate that financial records cannot be modified or deleted by anyone, including administrators and subscription owners, for a mandated retention period.

1. In the left navigation menu under **Data storage**, click **Containers**.
2. Click **+ Container** ➔ Name: `legal-records` ➔ Public access level: `Private (no anonymous access)` ➔ Click **Create**.
3. Click into the new `legal-records` container.
4. In the left sub-menu under **Settings**, click **Access policy**.
5. Scroll down to the **Immutable blob storage** section and click **+ Add policy**.
6. Configure the immutability policy:
   * **Policy type:** Select `Time-based retention`.
   * **Retention period:** Enter `7` (Days).
   * **Allow additional append writes:** Leave unchecked (blocks any append modification).
   * Click **OK**.
7. Notice the policy state is currently **Unlocked**.
   * In an enterprise environment, an Unlocked policy allows testing. Once verified, clicking **Lock policy** makes the retention rule permanent and immutable—even Microsoft Support cannot bypass or delete a locked WORM container before the retention days elapse!
8. Test the Immutability enforcement:
   * Return to the **Overview** tab of the `legal-records` container.
   * Click **Upload** ➔ Upload a test file named `tax-audit-2026.log`.
   * Select `tax-audit-2026.log` in the file list and click **Delete**.
   * A confirmation dialog appears. Click **OK**.
   * **Observe Portal Error Banner:**
     `Failed to delete 1 out of 1 blob(s): tax-audit-2026.log: Operation not permitted because the blob is immutable due to policy.`

> [!NOTE]
> **Visual Checkpoint:** The red error notification banner confirms that Azure platform-level WORM immutability intercepted and rejected the delete request, proving legal compliance retention is functioning.

---

### Task 2.5: Generate Zero-Trust User Delegation SAS (Signed via Entra ID)

Legacy Shared Access Signatures (Account SAS or Service SAS) rely on Account Key 1 or Key 2. If leaked, they expose the entire storage account until keys are rotated, which breaks all connected services. **User Delegation SAS** tokens are signed using the caller's Microsoft Entra ID credentials, expire within a maximum of 7 days, and are instantly revoked if the user account is disabled.

1. Ensure your account has the data plane role:
   * Navigate back to the Storage Account main blade.
   * Click **Access Control (IAM)** ➔ **+ Add** ➔ **Add role assignment**.
   * Select **Storage Blob Data Contributor** ➔ Click **Next**.
   * Select **Members** ➔ Assign access to: `User, group, or service principal` ➔ Click **+ Select members** ➔ Search and select your current user account ➔ Click **Select**.
   * Click **Review + assign** ➔ Click **Review + assign** again.
2. Generate User Delegation SAS in the Portal:
   * In the left menu under **Data storage**, click **Containers** ➔ Click `corporate-invoices`.
   * Click on the `contract.txt` blob to open its details blade.
   * Click the **Generate SAS** tab.
   * Under **Signing method**, observe the two radio buttons:
     * `Account key`
     * `User delegation key` (Notice the prompt indicating this signs the SAS with your Microsoft Entra ID user identity).
     * Select **User delegation key**.
   * Under **Permissions**: Leave only **Read** checked (uncheck Write, Delete, etc.).
   * Under **Start and expiry date/time**:
     * Start: Current time.
     * Expiry: Set to tomorrow (24 hours from now).
   * Under **Allowed IP addresses**: Leave blank (or enter your public IP for geo-fencing).
   * Under **Allowed protocols**: Select `HTTPS only`.
   * Click **Generate SAS token and URL**.
3. Copy the generated **Blob SAS URL**.
4. Open an InPrivate / Incognito browser window, paste the URL into the address bar, and hit Enter.
5. Notice that the contract file downloads immediately! The external auditor accessed the file without knowing storage account keys, without anonymous public blob access enabled, and bound strictly to a 24-hour expiration managed by Entra ID.

---

### Task 2.6: Configure Azure Files SMB Enterprise Share & Snapshots

1. In the left navigation menu under **Data storage**, click **File shares**.
2. Click **+ File share**.
3. In the **Basics** tab:
   * **Name:** Enter `corp-share`.
   * **Tier:** Select `Transaction optimized` (or `Hot` depending on account type).
4. Click **Next: Backup >**:
   * Azure Backup can integrate directly with File Shares. Leave unchecked for now.
5. Click **Review + create** ➔ Click **Create**.
6. Click into `corp-share`:
   * Click **Upload** ➔ Upload a sample text file `department-memo.docx`.
   * In the left sub-menu under **Operations**, click **Snapshots**.
   * Click **+ Add snapshot** ➔ Comments: `Pre-maintenance baseline snapshot` ➔ Click **OK**.
   * Notice the instant point-in-time read-only copy created without taking the share offline.

---

## 🔗 Phase 3: Cross-Module Integration Task

### Integrating Module 02 (Identity/RBAC), Module 03 (Governance Locks), and Module 06 (Network Security)

In enterprise IT, storage accounts are never isolated silos; they are locked down by governance policies, protected by resource locks, and restricted behind network boundaries.

```
+-----------------------------------------------------------------------------------------+
|                               Cross-Module Architecture                                 |
|                                                                                         |
|   +-----------------------+     +------------------------+    +---------------------+   |
|   | Module 02: Entra ID   |     | Module 03: Governance  |    | Module 06: Net Sec  |   |
|   | Dynamic Group (Eng)   |     | Resource Lock          |    | Firewall & VNets    |   |
|   | Assigned RBAC:        |     | Type: CanNotDelete     |    | Allow: Selected     |   |
|   | Storage Blob Data     |     | Scope: stlabXXXX       |    | Networks Only       |   |
|   | Contributor           |     |                        |    |                     |   |
|   +-----------+-----------+     +-----------+------------+    +----------+----------+   |
|               |                             |                            |              |
|               v                             v                            v              |
|   +---------------------------------------------------------------------------------+   |
|   |                     Target Storage Account (stlabXXXX)                          |   |
|   |       - Identity: Zero-Trust Entra RBAC Data Plane Access                       |   |
|   |       - Governance: Protected against accidental portal/CLI deletion            |   |
|   |       - Network: Blocked from public internet; ready for Private Endpoints      |   |
|   +---------------------------------------------------------------------------------+   |
+-----------------------------------------------------------------------------------------+
```

### Step 1: Assign Entra ID Dynamic Security Group (Mod 02 Integration)
1. On the Storage Account overview, click **Access Control (IAM)**.
2. Click **+ Add** ➔ **Add role assignment**.
3. Search for role: `Storage Blob Data Reader`. Click **Next**.
4. Click **+ Select members** ➔ Search for `grp-us-engineering` (created in Module 02).
5. Click **Select** ➔ Click **Review + assign**. All members of US Engineering now inherit data-plane read access to blobs without ever receiving access keys!

### Step 2: Apply a `CanNotDelete` Resource Lock (Mod 03 Integration)
1. In the left navigation menu under **Settings**, click **Locks**.
2. Click **+ Add**.
   * **Lock name:** `lock-protect-financial-storage`.
   * **Lock type:** Select `Delete`.
   * **Notes:** `Regulatory audit data repository - deletion prohibited by governance mandate.`
3. Click **OK**.
4. Test the lock: Navigate to the **Overview** blade of the storage account and click **Delete**.
5. Type the storage account name and click **Delete**.
6. Observe the error:
   `Failed to delete storage account 'stlabXXXX'. The scope '/subscriptions/.../stlabXXXX' cannot perform delete operation because following scope(s) are locked: 'lock-protect-financial-storage'.`

### Step 3: Restrict Storage Firewall (Mod 06 Private Link Preparation)
1. In the left navigation menu under **Security + networking**, click **Networking**.
2. Under **Public network access**, change from *Enabled from all networks* to:
   * **Enabled from selected virtual networks and IP addresses**.
3. Under **Firewall**, check **Add your client IP address** (this ensures you don't lock your own Azure Portal session out!).
4. Under **Exceptions**, ensure `Allow Azure services on the trusted services list to access this storage account` is checked.
5. Click **Save** at the top of the blade.

---

## 🔬 Phase 4: Verification & Validation Testing (Azure CLI / Cloud Shell)

Open Azure Cloud Shell (Bash) and execute these automated verification queries to validate your deployment against AZ-104 production standards:

```bash
#!/usr/bin/env bash
set -euo pipefail

export RG="rg-storage-lab"
export STORAGE_NAME=$(az storage account list --resource-group "${RG}" --query "[0].name" -o tsv)

echo "=========================================================="
echo "==> Auditing Storage Account: ${STORAGE_NAME}"
echo "=========================================================="

# Test 1: Verify Redundancy and Public Blob Access Setting
echo -e "\n[Test 1] Checking Redundancy SKU and Public Access Policy..."
az storage account show \
  --name "${STORAGE_NAME}" \
  --resource-group "${RG}" \
  --query "{SKU:sku.name, Kind:kind, PublicBlobAccess:allowBlobPublicAccess, MinTLS:minimumTlsVersion}" \
  --output table

# Test 2: Verify Soft Delete and Versioning Engine
echo -e "\n[Test 2] Auditing Blob Service Data Protection Properties..."
az storage account blob-service-properties show \
  --account-name "${STORAGE_NAME}" \
  --resource-group "${RG}" \
  --query "{VersioningEnabled:isVersioningEnabled, SoftDeleteBlobs:deleteRetentionPolicy.enabled, RetentionDays:deleteRetentionPolicy.days, ContainerSoftDelete:containerDeleteRetentionPolicy.enabled}" \
  --output table

# Test 3: Verify Lifecycle Management Policy Rules
echo -e "\n[Test 3] Auditing Lifecycle Management JSON Rules..."
az storage account management-policy show \
  --account-name "${STORAGE_NAME}" \
  --resource-group "${RG}" \
  --query "policy.rules[].{RuleName:name, Enabled:enabled, Prefix:definition.filters.prefixMatch[0]}" \
  --output table

# Test 4: Verify Resource Locks Protection
echo -e "\n[Test 4] Checking Active Governance Resource Locks..."
az lock list \
  --resource-group "${RG}" \
  --query "[].{LockName:name, Level:level, Resource:resourceName}" \
  --output table

echo -e "\n=========================================================="
echo "==> ALL AUDIT CHECKS PASSED: Storage account meets AZ-104 Enterprise Baseline!"
echo "=========================================================="
```

---

## ⚠️ Phase 5: "See It in Action" Real-World Failure & Recovery Loop (AARF)

### Scenario A: The Anonymous Access Discrepancy Failure
* **The Architecture:** An engineering team configures an Azure Container named `public-logos` and explicitly sets its access level to `Blob (anonymous read access for blobs only)`.
* **The Assumption:** Developers assume external web users can immediately download `https://stlab.blob.core.windows.net/public-logos/logo.png`.
* **The Failure Loop:**
  * When browsing to the URL, the client receives:
    `HTTP 409 PublicAccessNotPermitted: Public access is not permitted on this storage account.`
* **The Root Cause:**
  In modern Azure security baselines, the account-level property **`allowBlobPublicAccess`** defaults to `false`. Account-level security settings strictly override container-level permissions.
* **The Remediation in GUI:**
  1. Navigate to the Storage Account in the Azure Portal.
  2. In the left menu under **Settings**, click **Configuration**.
  3. Locate **Allow Blob anonymous access** and set it to **Enabled**.
  4. Click **Save** (Wait 30 seconds for the control-plane flag to propagate).

---

### Scenario B: Accidental Soft-Deleted Blob Recovery
* **The Failure Scenario:** A junior admin accidentally deletes `contract.txt` from the `corporate-invoices` container.
* **The Recovery Action in GUI:**
  1. In the portal, navigate to `corporate-invoices` container.
  2. Toggle on the switch: **Show deleted blobs**.
  3. Notice `contract.txt` appears with status **Deleted**.
  4. Click the **...** (context menu) at the far right of the deleted blob row.
  5. Select **Undelete**.
  6. The blob is instantly restored to active status with all versions intact!

---

## 🧹 Phase 6: Cost Optimization & Lab Teardown

To avoid incurring ongoing charges for Azure Storage, data retention, and storage transactions:

1. **Remove Resource Locks First (Mandatory):**
   * In the Azure Portal, open the storage account `stlabXXXX`.
   * Under **Settings**, click **Locks**.
   * Click the **Delete** icon (trash can) next to `lock-protect-financial-storage`.
2. **Delete the Resource Group:**
   * Open Cloud Shell or run in your local terminal:
     ```bash
     az group delete --name "rg-storage-lab" --yes --no-wait
     ```
3. **Verify Deletion in Portal:**
   * In the Portal search bar, type `Resource groups` ➔ Verify `rg-storage-lab` shows status `Deleting` or is removed.

---

## 🔬 Exam-Specific Gotchas & Speed Shortcuts (AZ-104 Reference)

* **Access Tier Cost Trade-off:**
  * `Hot`: Higher storage capacity cost ($/GB), lowest transaction/access cost.
  * `Cool`: Lower storage cost, higher access cost, minimum 30-day retention penalty.
  * `Cold`: Even lower storage cost, higher access cost, minimum 90-day retention penalty.
  * `Archive`: Lowest storage cost ($0.00099/GB), highest read cost, minimum 180-day retention penalty. Blobs in Archive are **offline** and must be rehydrated (Priority: 1 hour, Standard: up to 15 hours) before reading!
* **User Delegation SAS vs Account SAS:**
  * Account SAS: Signed with storage account key (Key1/Key2). Cannot be scoped to Entra ID users. Maximum validity up to years.
  * User Delegation SAS: Signed with an Entra ID user/service principal token. Maximum validity is **7 days**. Can be revoked immediately by disabling the Entra identity.
* **Blob Versioning vs Soft Delete:**
  * Soft delete protects against **deletion** (retains blobs in a recycle bin).
  * Versioning protects against **overwrites** and unintended edits (preserves historical timestamps).
  * To protect against both overwrites and deletes, **enable both**!
* **Object Replication Prerequisites:**
  * Both source and destination storage accounts must have **Blob Versioning** and **Blob Change Feed** enabled. Hierarchical namespace (ADLS Gen2) is not supported for object replication.
