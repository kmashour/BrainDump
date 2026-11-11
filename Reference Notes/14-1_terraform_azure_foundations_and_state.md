---
obsidianUIMode: preview
class: reference-note
tier: reference-note
domains:
  - terraform
  - azure
tags:
  - terraform/azure
  - terraform/state
  - azure/iac
  - status/completed
---

# Module 14-1: Terraform Core Engine, AzureRM Provider & State Locking

**Breadcrumbs:** [[--Index--|🏠 Index]] > [[14-Index - Terraform on Azure|☁️ Terraform on Azure MOC]] > **Module 14-1: Foundations & State**

---

## 🎯 Architectural Overview & Cognitive Map

Terraform is HashiCorp's declarative Infrastructure as Code (IaC) tool. In Microsoft Azure environments, Terraform translates human-readable HCL (HashiCorp Configuration Language) declarations into native Azure Resource Manager (ARM) REST API calls via the **`azurerm`** provider plugin.

```mermaid
flowchart TD
    subgraph DeveloperZone ["Developer & CI/CD Pipeline"]
        HCL["1. Declarative HCL Code (*.tf)\n(Resources, Providers, Variables)"]
        CLI["2. Terraform CLI Core Engine (Go Binary)\n(Syntax Parsing, State Mapping, DAG Graph)"]
    end

    subgraph StateStorage ["Azure Storage Account: Remote State Fabric"]
        BlobContainer["3. Blob Container: tfstate"]
        StateBlob["prod.terraform.tfstate\n(Encrypted JSON Database: lineage, serial, resources)"]
        BlobLease["4. Native Blob Lease Concurrency Lock\n(HTTP ETag / Exclusive 60s Lease ID)"]
    end

    subgraph ProviderPlane ["Provider Plugin Framework"]
        AzureRM["5. AzureRM Provider Binary Plugin\n(Translates HCL to ARM HTTPS REST APIs)"]
    end

    subgraph AzureCloud ["Target Azure Subscription (ARM Control Plane)"]
        RG["Resource Group"]
        VNet["Virtual Networks & Subnets"]
        Compute["Virtual Machines / App Services / SQL"]
    end

    HCL -->|terraform init / plan / apply| CLI
    CLI <-->|Acquires Exclusive Lease (x-ms-lease-id)| BlobLease
    CLI <-->|Reads & Writes Current State| StateBlob
    CLI -->|Invokes RPC Calls over gRPC| AzureRM
    AzureRM -->|HTTPS REST APIs (PUT, PATCH, DELETE)| AzureCloud
```

---

## 1. Declarative IaC Foundations & Terraform Core Mechanics

### A. Declarative vs. Imperative Cloud Provisioning
Traditional cloud automation relied on **Imperative** scripting (Bash, PowerShell scripts, Azure CLI). Modern cloud engineering relies on **Declarative** definitions:

| Feature | Imperative Scripting (Azure CLI / Bash / PowerShell) | Declarative IaC (Terraform HCL / Bicep) |
| :--- | :--- | :--- |
| **Philosophy** | *"Tell the system HOW to do it step-by-step."* | *"Tell the system WHAT the end state must be."* |
| **Execution Model** | Sequential command execution (`az group create` then `az network vnet create`). | Graph execution engine constructs a Directed Acyclic Graph (DAG) and executes parallel requests where possible. |
| **Idempotency** | Difficult: Re-running a script midway often crashes due to resource naming conflicts or creates duplicate unmanaged resources. | Native: Running `terraform apply` multiple times produces zero changes if the cloud matches the declared configuration. |
| **State Awareness** | Blind: Scripts do not track previously created resources unless you write manual querying logic. | Aware: Maintains an explicit state database (`terraform.tfstate`) mapping declared HCL to physical Azure resource IDs. |
| **Drift Detection** | Manual: You must write scripts to audit whether settings changed in the portal. | Automated: `terraform plan` queries live Azure APIs via `GET` requests and calculates discrepancies against your code. |

---

### B. Mutable vs. Immutable Infrastructure
* **Mutable Infrastructure:** Servers and services are patched and updated in-place (e.g., SSH into Linux VMs to install software, manually tweaking NSG rules in the Azure portal). Over time, configuration drift accumulates between staging and production instances, making incident triage unpredictable.
* **Immutable Infrastructure:** Cloud resources are treated as disposable artifacts. Upgrades are performed by provisioning brand new virtual machines, container apps, or storage instances from updated configurations, testing them, routing traffic over, and destroying the old ones. Terraform natively supports immutable patterns via lifecycle meta-arguments (`create_before_destroy`).

---

### C. Under-the-Hood Engine Architecture
Terraform is intentionally split into two distinct architectural layers:

```text
+-----------------------------------------------------------------------------------+
|                            TERRAFORM CORE (Go Binary)                             |
|  - Parses HCL syntax and configuration files (*.tf)                               |
|  - Manages the State File (terraform.tfstate)                                     |
|  - Builds the Directed Acyclic Graph (DAG) of resource dependencies               |
|  - Compares Desired State vs. Actual State to produce Execution Plans             |
+-----------------------------------------------------------------------------------+
                                       │
                                       ▼ (gRPC over local RPC socket)
+-----------------------------------------------------------------------------------+
|                        TERRAFORM PROVIDERS (Plugin Binaries)                      |
|  - azurerm (hashicorp/azurerm)                                                    |
|  - azuread (hashicorp/azuread)                                                    |
|  - random / null / external                                                       |
|  - Translates Core requests into target cloud HTTPS REST API calls (ARM / MS Graph)|
+-----------------------------------------------------------------------------------+
```

1. **Terraform Core:** The platform-agnostic engine. It does not know what an Azure Virtual Network or Storage Account is. It only understands graphs, variables, state diffs, and expressions.
2. **Terraform Providers:** Platform-specific executable plugins. The `azurerm` provider contains the schema definitions and API client logic to talk to Azure Resource Manager (`https://management.azure.com`).

---

## 2. HCL Syntax Anatomy: From Blocks to Attributes

Every Terraform file (`.tf`) is written in HashiCorp Configuration Language (HCL). To write and debug Terraform without confusion, you must understand the **four fundamental building blocks** of HCL syntax:

```text
block_type  "block_label_1"  "block_label_2"  {
  identifier = expression   # <-- Argument
}
```

```
┌─────────────────┐ ┌──────────────────────┐ ┌───────────────┐
│   block_type    │ │    block_label_1     │ │ block_label_2 │
│   (resource)    │ │(azurerm_storage_acc) │ │     (st)      │
└────────┬────────┘ └──────────┬───────────┘ └───────┬───────┘
         │                     │                     │
         ▼                     ▼                     ▼
      resource    "azurerm_storage_account"        "st"      {
        name                     = "stappdev001"             # <-- Argument (Input)
        resource_group_name      = "rg-app-dev"              # <-- Argument (Input)
        location                 = "eastus"                  # <-- Argument (Input)
        account_tier             = "Standard"                # <-- Argument (Input)
        account_replication_type = "LRS"                     # <-- Argument (Input)
      }
```

### A. The Core HCL Keywords (`block_type`)
Terraform configurations consist of only **7 core top-level block types**:

| Block Type | Purpose | Example Label Structure |
| :--- | :--- | :--- |
| **`terraform`** | Configures global engine settings, required CLI version, required providers, and remote state backend. | `terraform { ... }` (Takes NO labels) |
| **`provider`** | Configures credentials and runtime behavior for a cloud plugin. | `provider "azurerm" { ... }` (Takes 1 label: provider name) |
| **`resource`** | Declares a piece of infrastructure to create, manage, and destroy in Azure. | `resource "azurerm_resource_group" "rg" { ... }` (Takes 2 labels: resource type, local name) |
| **`data`** | Queries and reads an existing piece of infrastructure already present in Azure. | `data "azurerm_virtual_network" "vnet" { ... }` (Takes 2 labels: data type, local name) |
| **`variable`** | Declares an input parameter passed into the configuration from CLI, file, or environment. | `variable "environment" { ... }` (Takes 1 label: variable name) |
| **`output`** | Exposes computed values (IDs, connection strings, IPs) to the terminal or parent modules. | `output "storage_account_id" { ... }` (Takes 1 label: output name) |
| **`locals`** | Declares internal temporary variables / computed values within the module. | `locals { ... }` (Takes NO labels) |

---

### B. Arguments vs. Exported Attributes

A critical distinction that causes frequent beginner errors:

* **Arguments (Inputs):** Values you supply *inside* the resource block to configure it (e.g., `location = "eastus"`, `account_tier = "Standard"`).
* **Exported Attributes (Outputs / Computed Values):** Values that **Azure generates** after the resource is created. You cannot configure them directly, but you can *read* them elsewhere in your code:
  * `id`: The full Azure Resource Manager resource ID (`/subscriptions/.../resourceGroups/...`).
  * `primary_blob_endpoint`: `https://stappdev001.blob.core.windows.net/`.
  * `fully_qualified_domain_name`: `oh-sql-dev.database.windows.net`.

### C. Resource Addressing & The Dot (`.`) Operator
To reference an attribute from another resource, use the standard resource address syntax:

```text
<RESOURCE_TYPE>.<LOCAL_NAME>.<ATTRIBUTE>
       │              │            │
azurerm_storage_account.st.primary_blob_endpoint
```

```hcl
resource "azurerm_resource_group" "rg" {
  name     = "rg-outcomeshub-dev"
  location = "eastus"
}

resource "azurerm_storage_account" "st" {
  name                = "stohtfstate001"
  # Referencing arguments & attributes from the resource group above:
  resource_group_name = azurerm_resource_group.rg.name     # <-- Implicit Dependency Created!
  location            = azurerm_resource_group.rg.location # <-- Implicit Dependency Created!
  account_tier        = "Standard"
  account_replication_type = "LRS"
}
```

> [!TIP]
> **Implicit Dependency Creation:** Notice that we did not tell Terraform which resource to create first. Because `azurerm_storage_account.st` references `azurerm_resource_group.rg.name`, Terraform automatically builds a dependency graph ensuring the Resource Group is provisioned **before** the Storage Account.

---

## 3. The Terraform CLI Lifecycle & Command Workflow

Every Terraform deployment follows a strict, repeatable 5-phase lifecycle:

```text
[ terraform init ]  ──►  [ terraform validate ]  ──►  [ terraform plan ]  ──►  [ terraform apply ]  ──►  [ terraform destroy ]
  (Download Plugins)        (Static Syntax Check)         (Preview Delta)          (Execute against Azure)   (Tear down infrastructure)
```

### 1. `terraform init` (Initialization Phase)
Before Terraform can do anything, you must initialize the working directory.
* **What it does:**
  1. Scans all `*.tf` files for `required_providers`.
  2. Queries the HashiCorp Registry (`registry.terraform.io`) for the requested providers.
  3. Downloads the provider binaries into a local directory: `.terraform/providers/`.
  4. Generates or updates the dependency lock file: `.terraform.lock.hcl`.
  5. Connects to and configures the remote state backend (Azure Blob Storage).

### 2. `terraform fmt` & `terraform validate` (Verification Phase)
* **`terraform fmt -recursive`:** Formats all code to HashiCorp's canonical style guidelines (standardizes indentation, variable alignments, and line breaks).
* **`terraform validate`:** Checks your code for syntactical correctness, attribute typos, and type constraint mismatches **without contacting Azure APIs or incurring costs**.

### 3. `terraform plan` (Speculative Execution Phase)
* **What it does:**
  1. Acquires a temporary read lock on the remote state.
  2. Issues `GET` requests to Azure Resource Manager to inspect the actual live status of every resource in the state file (Refreshing State).
  3. Calculates the delta between your desired HCL configuration and live reality.
  4. Prints an execution plan using standard visual diff symbols:
     * `+ create`: Resource does not exist; Terraform will create it.
     * `~ update in-place`: Resource exists, but non-destructive attributes changed.
     * `- destroy`: Resource exists in state/Azure, but was deleted from HCL code.
     * `-/+` or `+/-` **replace**: Changing this attribute forces Azure to delete the existing resource and create a new one (e.g., changing a Storage Account name or VNet address space!).

### 4. `terraform apply` (Execution Phase)
* **What it does:**
  1. Acquires an exclusive write lease/lock on the state file.
  2. Converts the execution plan into live HTTPS REST calls against Azure (`PUT`, `POST`, `PATCH`, `DELETE`).
  3. Incrementally commits updated Resource IDs and metadata into the state file as each resource finishes provisioning.
  4. Releases the state lock.

### 5. `terraform destroy` (Decommissioning Phase)
* Generates a reverse-order execution plan to delete all resources tracked by the state file. Dependencies are respected in reverse: virtual machines are destroyed before the subnets they are attached to.

---

## 4. The `azurerm` Provider & Authentication Architecture

### A. Provider Configuration & The Mandatory `features {}` Block
In Terraform, the AzureRM provider requires an explicit configuration block. A unique syntactical requirement of `azurerm` is the mandatory **`features {}`** block:

```hcl
terraform {
  required_version = ">= 1.5.0"
  
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.117.0"
    }
    azuread = {
      source  = "hashicorp/azuread"
      version = "~> 2.47.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.6.0"
    }
  }
}

provider "azurerm" {
  # The features block is MANDATORY. Even if empty, it configures provider runtime behavior.
  features {
    resource_group {
      prevent_deletion_if_contains_resources = false
    }
    virtual_machine {
      delete_os_disk_on_deletion     = true
      graceful_shutdown              = false
      skip_shutdown_and_force_delete = false
    }
    key_vault {
      purge_soft_delete_on_destroy    = false
      recover_soft_deleted_key_vaults = true
    }
  }
}
```

> [!IMPORTANT]
> **Why is `features {}` mandatory?**
> Azure services frequently have cascading deletion and recovery behaviors (e.g., Key Vault 90-day soft delete, VM OS disk detachment vs deletion). The `features {}` block tells the provider how to handle these Azure-specific control-plane behaviors when resources are modified or destroyed.

---

### B. Provider Version Constraints Explained
In the `required_providers` block, versioning controls stability:

| Version Syntax | Meaning | Real-World Behavior |
| :--- | :--- | :--- |
| `version = "3.117.0"` | Exact pinning | Installs only version `3.117.0`. Fails if unavailable. |
| `version = ">= 3.100.0"` | Minimum version | Installs `3.100.0` or any newer version, including breaking major releases like `4.0.0`! (Dangerous in production). |
| `version = ">= 3.100.0, < 4.0.0"` | Range constraint | Allows any minor update in version 3, but blocks breaking version 4. |
| `version = "~> 3.117.0"` | **Pessimistic constraint (3 digits)** | Allows patch updates: `>= 3.117.0` and `< 3.118.0`. Safest for production. |
| `version = "~> 3.117"` | **Pessimistic constraint (2 digits)** | Allows minor updates: `>= 3.117.0` and `< 4.0.0`. |

### C. The Dependency Lock File (`.terraform.lock.hcl`)
When you run `terraform init`, Terraform generates a `.terraform.lock.hcl` file containing cryptographic checksums (`h1:...`) of the downloaded provider binaries.
* **Why it matters:** It guarantees that every developer on the team and every CI/CD runner downloads the **exact identical binary** byte-for-byte.
* **Best Practice:** Always commit `.terraform.lock.hcl` to Git!

---

### D. Multiple Provider Instances (`alias`)
When you need to deploy resources across multiple Azure subscriptions or multiple regions in a single configuration, use the **`alias`** meta-argument:

```hcl
# Default Provider: Workload Subscription
provider "azurerm" {
  features {}
  subscription_id = "11111111-1111-1111-1111-111111111111"
}

# Aliased Provider: Central Hub / DNS Subscription
provider "azurerm" {
  alias           = "hub_dns"
  features {}
  subscription_id = "c72daa19-9a38-4155-b2c6-9121045a0fdc" # Central DNS Subscription
}

# Workload Resource Group (uses default provider)
resource "azurerm_resource_group" "workload_rg" {
  name     = "rg-workload-dev"
  location = "eastus"
}

# Central Private DNS Zone (explicitly targets aliased provider)
resource "azurerm_private_dns_zone" "sql_dns" {
  provider            = azurerm.hub_dns # <-- Explicit Provider Mapping
  name                = "privatelink.database.windows.net"
  resource_group_name = "rg-central-dns"
}
```

---

### E. Azure Authentication Models
Terraform supports five primary authentication mechanisms to connect to Azure:

| Authentication Method | Ideal Use Case | Security Characteristics | Required Configuration / Environment Variables |
| :--- | :--- | :--- | :--- |
| **1. Azure CLI (`az login`)** | Local development and workstation testing. | Uses developer's personal Entra ID credentials; interactive MFA. | No credentials in code. Relies on active `az account show` session. |
| **2. Service Principal with Secret** | Legacy CI/CD automation pipelines. | Long-lived secret string; security risk if leaked. | `ARM_CLIENT_ID`, `ARM_CLIENT_SECRET`, `ARM_TENANT_ID`, `ARM_SUBSCRIPTION_ID`. |
| **3. Service Principal with Certificate** | Enterprise automation requiring PKI compliance. | Cryptographically strong; certificate rotated via enterprise CA. | `ARM_CLIENT_CERTIFICATE_PATH`, `ARM_CLIENT_CERTIFICATE_PASSWORD`. |
| **4. Managed Identity (MSI)** | Terraform running inside Azure VMs, Container Instances, or VMSS. | **Passwordless & Zero-Trust.** Azure hypervisor automatically manages token acquisition via IMDS (`169.254.169.254`). | Set `use_msi = true` in provider block. |
| **5. Workload Identity Federation (OIDC)** | Modern GitHub Actions / Azure DevOps CI/CD. | **Passwordless & Secret-free.** Cloud provider exchanges short-lived OIDC tokens directly with Microsoft Entra ID. | Set `use_oidc = true`. Requires federated credential link in Entra ID. |

---

## 5. Remote State Management & Azure Blob Concurrency Locking

The Terraform state file (`terraform.tfstate`) is an encrypted JSON database representing the single source of truth mapping declared HCL code to physical Azure Resource IDs.

### A. Anatomy of the State File
Inside `.tfstate`, Terraform records metadata crucial for graph calculation:

```json
{
  "version": 4,
  "terraform_version": "1.5.7",
  "serial": 12,
  "lineage": "a89d24f0-4382-78d1-bc93-68d18402bcde",
  "resources": [
    {
      "mode": "managed",
      "type": "azurerm_resource_group",
      "name": "rg",
      "provider": "provider[\"registry.terraform.io/hashicorp/azurerm\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "id": "/subscriptions/f28a6419-.../resourceGroups/outcomeshub-dev",
            "location": "eastus",
            "name": "outcomeshub-dev",
            "tags": { "Environment": "dev" }
          }
        }
      ]
    }
  ]
}
```

* **`serial`**: Monotonically increasing integer. Incremented every time state is modified. If two operations run simultaneously, Terraform detects mismatched serial numbers and prevents overwrites.
* **`lineage`**: A unique GUID assigned when the state file is first created. It guarantees that Terraform never accidentally applies a plan against the state of a different project or environment!

---

### B. Remote Backend Architecture: Azure Storage Account
In production, state must **never** be stored locally on developer laptops. It must reside centrally in an **Azure Storage Account Blob Container**:

```hcl
# backend.tf or backend.hcl
terraform {
  backend "azurerm" {
    resource_group_name  = "outcomeshub-tfstate-dev-rg"
    storage_account_name = "ohtfstatedev"
    container_name       = "tfstate"
    key                  = "dev.terraform.tfstate"
    
    # Enforce Zero-Trust Entra ID auth instead of access keys:
    use_azuread_auth     = true
    use_oidc             = true
  }
}
```

---

### C. Concurrency Locking: Azure Blob Lease Mechanism
A major architectural difference between cloud providers is how state concurrency locking is achieved:

* **AWS:** Requires deploying an external **Amazon DynamoDB table** alongside an S3 bucket to track lock items.
* **Azure:** Terraform leverages Azure Blob Storage's **Native Blob Lease mechanism**.

```text
+-------------------------------------------------------------------------------------------------+
|                                 Azure Blob Lease Locking Loop                                   |
|                                                                                                 |
|   Engineer A: terraform apply                                                                   |
|         │                                                                                       |
|         ├───► Acquires Blob Lease (HTTP PUT x-ms-lease-action: acquire)                         |
|         │     Azure grants 60s lease (x-ms-lease-id: a1b2c3d4) ──► Blob Status: Leased          |
|         │     Terraform applies updates against Azure Subscription...                           |
|         │                                                                                       |
|   Engineer B: terraform apply (Simultaneous Run)                                                |
|         │                                                                                       |
|         └───► Attempts to acquire lease on dev.terraform.tfstate                                |
|               Azure Storage rejects request with HTTP 412 (Precondition Failed)!                |
|               "There is currently a lease on the blob and no lease ID was specified."           |
|               Engineer B is immediately safely terminated without corrupting state.             |
|                                                                                                 |
|   Engineer A finishes ──► Releases Lease (x-ms-lease-action: release) ──► Status: Available    |
+-------------------------------------------------------------------------------------------------+
```

> [!WARNING]
> **What happens if a CI runner crashes midway?**
> If a runner hard-crashes while holding a state lock, the blob may stay leased. Terraform provides an administrative command to break the deadlock:
> ```bash
> terraform force-unlock <LOCK_ID>
> ```
> *(Use with extreme caution: only run this when you have verified that no other pipeline or engineer is actively running).*

---

## 6. Deep-Intuition (AARF) Failure-Loop Breakdowns

### Failure Loop 1: The In-Azure Runner Egress Trap
* **The Architecture:** GitHub Actions self-hosted runners run inside an Azure VNet (`pzi-t58kh-dev-vnt`). The Terraform state storage account is configured with `default_action = "Deny"` and has the runner's public IP explicitly allowed in `ip_rules`.
* **The Symptom:** When the pipeline runs `terraform init`, it fails immediately with:
  ```text
  Error: Failed to get existing workspaces: containers.Client#ListBlobs:
  Failure responding to request: StatusCode=403 -- Original Error: autorest/azure:
  service returned an error. Status=412 Code="AuthorizationFailure"
  This request is not authorized to perform this operation.
  ```
* **The Root Cause:** **Azure Storage Public IP Firewall Bypass Law**. Requests originating from within Azure (even from another subscription) traverse the Microsoft backbone. Azure Storage evaluates the caller's source and determines it is inside Azure. Azure Storage **completely ignores public IP firewall rules for intra-Azure traffic**! Allow-listing the runner's public IP does nothing.
* **The Remediation:**
  The Storage Account firewall must be configured with a **Virtual Network Service Endpoint rule** targeting the runner subnet:
  ```bash
  az storage account network-rule add \
    --account-name "ohtfstatedev" \
    --resource-group "outcomeshub-tfstate-dev-rg" \
    --subnet "/subscriptions/.../subnets/snt-runners-001"
  ```

---

### Failure Loop 2: Leaked Storage Account Access Key
* **The Architecture:** An engineering team configures `backend "azurerm"` using storage account access key 1 (`account_key = "..."`).
* **The Failure Loop:**
  * The configuration containing the storage key is inadvertently pushed to a Git repository.
  * An adversary downloads `dev.terraform.tfstate`, which contains decrypted database administrator passwords, TLS private keys, and service principal secrets.
* **The Remediation:**
  1. Disable Shared Key access on the Storage Account:
     ```bash
     az storage account update \
       --name "ohtfstatedev" \
       --resource-group "outcomeshub-tfstate-dev-rg" \
       --allow-shared-key-access false
     ```
  2. Set `use_azuread_auth = true` in the backend configuration.
  3. Assign the deploying Managed Identity the **`Storage Blob Data Owner`** role via Entra ID RBAC.

---

## 7. Hands-On Verification Recipe: First Azure Resource

Save this as `main.tf` to test and verify your core foundations understanding:

```hcl
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.117.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# 1. Resource Group
resource "azurerm_resource_group" "demo_rg" {
  name     = "rg-terraform-foundations-dev"
  location = "eastus"
  tags = {
    Environment = "dev"
    ManagedBy   = "Terraform"
  }
}

# 2. Storage Account with strict security guardrails
resource "azurerm_storage_account" "demo_st" {
  name                     = "stfoundationsdemo001"
  resource_group_name      = azurerm_resource_group.demo_rg.name     # Implicit Dependency
  location                 = azurerm_resource_group.demo_rg.location # Implicit Dependency
  account_tier             = "Standard"
  account_replication_type = "LRS"
  min_tls_version          = "TLS1_2"
  enable_https_traffic_only = true

  tags = azurerm_resource_group.demo_rg.tags
}

# 3. Output Exported Computed Attribute
output "storage_account_id" {
  description = "The Azure Resource Manager ID of the storage account."
  value       = azurerm_storage_account.demo_st.id
}
```

```bash
# Verification commands:
terraform fmt -check
terraform init
terraform validate
terraform plan
```
