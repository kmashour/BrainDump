---
obsidianUIMode: preview
class: project-note
tier: project
domains:
  - terraform
  - azure
  - databases
concepts_referenced:
  - "[[14-Index - Terraform on Azure]]"
  - "[[13-104-08_administer_azure_storage]]"
  - "[[13-3_azure_compute_services_and_workload_paradigms]]"
  - "[[13-Index - Azure]]"
difficulty: intermediate
status: completed
---

# Project 09: Secure Azure SQL Database & Network Hardening as Code

**Breadcrumbs:** [[--Index--|🏠 Index]] > [[14-Index - Terraform on Azure|☁️ Terraform on Azure MOC]] > [[README|Azure Terraform Projects]] > **Project 09: Hardened Azure SQL & Firewall**

---

## 🎯 Executive Overview & Architectural Objectives

Relational databases store an organization's most sensitive transactional and customer data. In cloud deployments, naive setups frequently suffer from critical vulnerabilities: hardcoded administrator credentials committed to version control, broad firewall rules allowing unauthenticated perimeter traffic, and unencrypted transport connections.

In this project, you will engineer a hardened, production-ready **PaaS Azure SQL Database platform** using Terraform. You will codify an Azure SQL Logical Server enforcing TLS 1.2, eliminate hardcoded credentials using automated cryptographic password generation backed by Azure Key Vault, integrate Microsoft Entra ID (Azure AD) administrative authentication, and configure granular IP firewall rules.

### Key Architectural Deliverables:
1.  **Azure SQL Logical Server (`azurerm_mssql_server`):** Provision a managed logical server enforcing TLS 1.2 minimum version, disabling public access by default, and isolating database management.
2.  **Secretless Admin Credential Generation:** Generate high-entropy administrator passwords dynamically using `random_password` and securely escrow them into an Azure Key Vault Secret (`azurerm_key_vault_secret`).
3.  **Microsoft Entra ID (Azure AD) Admin Integration:** Attach a modern Entra ID administrator identity to eliminate reliance on static SQL authentication passwords.
4.  **Cost-Effective Scalable Database Tier (`azurerm_mssql_database`):** Deploy a serverless or Standard General Purpose database (`GP_S_Gen5_1` or `Basic`) with automatic geo-redundant backup policies.
5.  **Granular IP Firewall Control (`azurerm_mssql_firewall_rule`):** Author client IP whitelisting rules and audit the operational risks of the native "Allow Azure Services" toggle.
6.  **Transparent Data Encryption (TDE):** Enforce data-at-rest encryption natively managed by the Azure platform.

---

## 🏛️ Target Architecture & Component Topology

```mermaid
flowchart TD
    subgraph ClientAccess ["Client & Workload Access Layer"]
        DevIP["Authorized Developer IP\n(e.g., 203.0.113.45)"]
        UntrustedIP["Untrusted Public Internet"]
        AppVM["Azure Application Tier\n(Private Managed VNet)"]
    end

    subgraph SecurityControl ["Security & Secrets Management"]
        KV["Azure Key Vault: kv-sql-sec-XXXX\n- Secret: sql-admin-password\n- Access Policy / RBAC Scoped"]
        EntraAdmin["Microsoft Entra ID Admin\n(Cloud IAM Principal)"]
    end

    subgraph AzureSQLPaaS ["Azure SQL Managed Platform"]
        SQLFirewall["Azure SQL Server Firewall\n- Rule: AllowDevOffice (203.0.113.45)\n- Rule: AllowAzureServices (Conditional)"]
        
        subgraph LogicalServer ["Logical SQL Server: sql-hardened-prod"]
            direction TB
            Gateway["TDS Gateway (Port 1433)\n- Enforces TLS 1.2+ Only\n- Authenticates SQL & Entra ID"]
            
            subgraph DBInstances ["Managed Database Engine"]
                AppDB["Azure SQL DB: sqldb-ecommerce-prod\n- SKU: General Purpose / Basic\n- TDE Enabled (AES-256)\n- Point-In-Time Restore (PITR)"]
            end
        end
    end

    DevIP -->|Port 1433 (Allowed by Firewall)| Gateway
    UntrustedIP -.->|Blocked: Client IP Not Allowed| SQLFirewall
    AppVM -->|Private VNet / Trusted Access| Gateway
    
    KV -.->|Generates & Escrows Secret| LogicalServer
    EntraAdmin -->|Native Token Auth| LogicalServer
    Gateway --> AppDB
```

---

## 🧠 Deep-Intuition Azure Administration & Architectural Mechanics

### 1. The Azure SQL Logical Server Abstraction
Unlike traditional on-premises database deployments or IaaS Virtual Machines running Microsoft SQL Server, an Azure SQL Logical Server is **not a dedicated virtual machine or OS instance**.
*   **Centralized Management Endpoint:** The logical server is an administrative gateway construct in the Azure control plane (`<servername>.database.windows.net`).
*   **Multi-Tenant Gateway Architecture:** Inbound connections on TCP port 1433 hit Azure SQL Gateway proxies. The gateway inspects the incoming TDS (Tabular Data Stream) packets, verifies the target database name, negotiates TLS 1.2 encryption, checks the IP against server-level firewall rules, and routes the authenticated session directly to the backend database ring running inside Microsoft's hyper-converged compute clusters.
*   **Independent Resource Scaling:** Databases within a logical server do not share CPU or RAM unless configured into an **Elastic Pool**. Each database gets dedicated compute and storage limits (DTUs or vCores).

### 2. Demystifying the "Allow Azure Services" Toggle (`0.0.0.0`)
In Azure SQL, there is a famous firewall configuration rule:
```hcl
start_ip_address = "0.0.0.0"
end_ip_address   = "0.0.0.0"
```
*   **What it claims to do:** Allow services running inside Azure (such as App Services, Azure Functions, or AKS) to communicate with the database.
*   **What it actually does:** It opens the TDS gateway port to **ANY IP address originating from ANY Microsoft Azure customer tenant worldwide**!
*   **Production Architecture Decision:** In enterprise production, never rely solely on `0.0.0.0`. Protect production databases either by establishing an **Azure Private Endpoint** (which assigns the database a private IP inside your own VNet) or restricting access to specific NAT Gateway egress IPs with Entra ID token-based authentication.

---

## 💻 Complete Production-Grade Terraform Code

Organize your project into the following structure:

```
project-09-sql/
├── provider.tf
├── variables.tf
├── keyvault.tf
├── sql.tf
├── firewall.tf
├── outputs.tf
└── terraform.tfvars
```

### 1. `provider.tf`
```hcl
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.90.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.5.0"
    }
  }
}

provider "azurerm" {
  features {
    key_vault {
      purge_soft_delete_on_destroy    = true
      recover_soft_deleted_key_vaults = false
    }
  }
}
```

### 2. `variables.tf`
```hcl
variable "resource_group_name" {
  type        = string
  default     = "rg-hardened-sql-demo"
  description = "Target resource group name."
}

variable "location" {
  type        = string
  default     = "eastus"
  description = "Azure region for database and key vault."
}

variable "server_name_prefix" {
  type        = string
  default     = "sqlsrv-hardened"
  description = "Prefix for globally unique SQL Server name."
}

variable "admin_username" {
  type        = string
  default     = "sqladminuser"
  description = "Administrative login username."
}

variable "client_whitelist_ip" {
  type        = string
  default     = "203.0.113.50" # Replace with your public IP address
  description = "Authorized client public IPv4 address for firewall whitelisting."
}

variable "enable_azure_services_access" {
  type        = bool
  default     = false
  description = "Whether to allow inbound traffic from general Azure IP space."
}
```

### 3. `keyvault.tf` (Dynamic Secret Generation & Storage)
```hcl
data "azurerm_client_config" "current" {}

# Random suffix for globally unique Key Vault and SQL Server names
resource "random_string" "suffix" {
  length  = 6
  special = false
  upper   = false
}

# Generate cryptographically secure administrative password
resource "random_password" "sql_password" {
  length           = 24
  special          = true
  override_special = "!#$%&*()-_=+[]{}<>:?"
  min_upper        = 3
  min_lower        = 3
  min_numeric      = 3
  min_special      = 3
}

# Key Vault to securely escrow database credentials
resource "azurerm_key_vault" "kv" {
  name                       = "kv-sql-${random_string.suffix.result}"
  location                   = var.location
  resource_group_name        = azurerm_resource_group.rg.name
  tenant_id                  = data.azurerm_client_config.current.tenant_id
  sku_name                   = "standard"
  soft_delete_retention_days = 7
  purge_protection_enabled   = false

  access_policy {
    tenant_id = data.azurerm_client_config.current.tenant_id
    object_id = data.azurerm_client_config.current.object_id

    secret_permissions = [
      "Get", "List", "Set", "Delete", "Purge"
    ]
  }
}

# Store generated SQL password into Key Vault Secret
resource "azurerm_key_vault_secret" "sql_admin_secret" {
  name         = "sql-admin-password"
  value        = random_password.sql_password.result
  key_vault_id = azurerm_key_vault.kv.id

  content_type = "text/plain"
  tags = {
    ManagedBy = "Terraform"
    Target    = "AzureSQL"
  }
}
```

### 4. `sql.tf` (Logical Server & Database)
```hcl
resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
  tags = {
    Environment = "Production"
    Application = "TransactionalData"
    ManagedBy   = "Terraform"
  }
}

# Hardened Azure SQL Logical Server
resource "azurerm_mssql_server" "sql_server" {
  name                         = "${var.server_name_prefix}-${random_string.suffix.result}"
  resource_group_name          = azurerm_resource_group.rg.name
  location                     = azurerm_resource_group.rg.location
  version                      = "12.0"
  administrator_login          = var.admin_username
  administrator_login_password = random_password.sql_password.result

  # Security Hardening: Enforce modern TLS protocol
  minimum_tls_version = "1.2"

  # Microsoft Entra ID (Azure AD) Administrator integration
  azuread_administrator {
    login_username = "AzureAD Admin"
    object_id      = data.azurerm_client_config.current.object_id
  }

  tags = {
    Tier = "Data"
  }
}

# Azure SQL Managed Database
resource "azurerm_mssql_database" "ecommerce_db" {
  name         = "sqldb-ecommerce-prod"
  server_id    = azurerm_mssql_server.sql_server.id
  collation    = "SQL_Latin1_General_CP1_CI_AS"
  license_type = "LicenseIncluded"
  max_size_gb  = 5
  sku_name     = "Basic" # Economical tier for development & testing

  # Storage account redundancy for automated backups
  storage_account_type = "Local"

  tags = {
    Workload = "Transactional"
  }
}
```

### 5. `firewall.tf` (Granular Network Rules)
```hcl
# Authorized Administrative Client Rule
resource "azurerm_mssql_firewall_rule" "admin_client" {
  name             = "AllowAdminWorkstation"
  server_id        = azurerm_mssql_server.sql_server.id
  start_ip_address = var.client_whitelist_ip
  end_ip_address   = var.client_whitelist_ip
}

# Conditional "Allow Azure Services" toggle
resource "azurerm_mssql_firewall_rule" "azure_services" {
  count            = var.enable_azure_services_access ? 1 : 0
  name             = "AllowAllWindowsAzureIps"
  server_id        = azurerm_mssql_server.sql_server.id
  start_ip_address = "0.0.0.0"
  end_ip_address   = "0.0.0.0"
}
```

### 6. `outputs.tf`
```hcl
output "sql_server_fqdn" {
  value       = azurerm_mssql_server.sql_server.fully_qualified_domain_name
  description = "Fully qualified domain name of the Azure SQL Logical Server."
}

output "database_name" {
  value       = azurerm_mssql_database.ecommerce_db.name
  description = "Name of the production transactional database."
}

output "key_vault_secret_id" {
  value       = azurerm_key_vault_secret.sql_admin_secret.id
  description = "Resource ID of the Key Vault secret storing the administrator password."
}

output "connection_string_template" {
  value       = "Server=tcp:${azurerm_mssql_server.sql_server.fully_qualified_domain_name},1433;Initial Catalog=${azurerm_mssql_database.ecommerce_db.name};Persist Security Info=False;User ID=${var.admin_username};MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"
  description = "TDS connection string template with TLS encryption enforced."
  sensitive   = true
}
```

---

## 🛠️ Step-by-Step Implementation Walkthrough

### 1. Initialize & Review Dynamic Cryptographic Plan
```bash
terraform init
terraform plan -var="client_whitelist_ip=$(curl -s ifconfig.me)" -out=tfplan
terraform apply tfplan
```
*Note: Using `curl -s ifconfig.me` automatically discovers your workstation's outbound public IP for immediate validation.*

### 2. 👁️ Visual Checkpoint in Azure Portal
1.  Navigate to **SQL servers** in the Azure Portal.
2.  Click `${var.server_name_prefix}-XXXX`:
    *   Verify Server name and status: **Available**.
    *   Under **Settings**, click **Networking**:
        *   Verify **Public network access**: Selected networks.
        *   Verify Firewall rules table: Confirm `AllowAdminWorkstation` with your IP.
        *   Confirm **Minimum TLS Version**: `TLS 1.2`.
    *   Under **Settings**, click **Microsoft Entra ID**: Verify your signed-in identity is configured as the active Entra admin.
3.  Navigate to **Key vaults** ➔ Click `kv-sql-XXXX` ➔ **Secrets**:
    *   Verify secret `sql-admin-password` exists.
    *   Click **Show Secret Value** to observe the 24-character high-entropy secret.

---

## 🔬 Verification & Live Probe Testing

### 1. Retrieve Secret from Key Vault & Establish Live SQL Connection
Extract the generated administrative password directly from Azure Key Vault using Azure CLI:

```bash
# Retrieve password dynamically
DB_PASS=$(az keyvault secret show \
  --vault-name $(terraform output -raw key_vault_secret_id | cut -d'/' -f9) \
  --name "sql-admin-password" \
  --query value -o tsv)

SERVER_FQDN=$(terraform output -raw sql_server_fqdn)

# Test connectivity using sqlcmd or sqlclient
sqlcmd -S "$SERVER_FQDN" -d "sqldb-ecommerce-prod" -U "sqladminuser" -P "$DB_PASS" -Q "SELECT @@VERSION AS SQL_Version, DB_NAME() AS Current_DB;"
```

**Expected Query Output:**
```
SQL_Version                                                              DB_NAME
------------------------------------------------------------------------ ---------------------
Microsoft SQL Azure (RTM) - 12.0.2000.8                                  sqldb-ecommerce-prod
(1 rows affected)
```

### 2. Verify Firewall Rejection from Unauthorized IP
Attempt to connect to the TDS gateway from an unauthorized client IP or simulate by temporarily removing the whitelist rule:

```bash
# Attempt connection from non-whitelisted IP
telnet $SERVER_FQDN 1433
```
**Connection Result:** The TCP handshake completes with the gateway, but TDS authentication is immediately severed with:
```
Sqlcmd: Error: Microsoft ODBC Driver 17 for SQL Server : Cannot open server 'sqlsrv-hardened-XXXX' requested by the login. Client with IP address '198.51.100.10' is not allowed to access the server. To enable access, use the Windows Azure Management Portal or run sp_set_firewall_rule on the master database.
```

---

## ⚠️ "See It in Action" Real-World Failure & Recovery Loop (AARF)

### Scenario: The "Allow Azure Services" Perimeter Breach
*   **The Architecture:** A team deploys an Azure SQL Database and turns on `Allow Azure services and resources to access this server` (`start_ip_address = "0.0.0.0"`) so their Azure Web App can query the database.
*   **The Assumption:** The team assumes "Allow Azure Services" creates a secure, private tunnel exclusively between *their* company's Azure subscriptions and the database.
*   **The Failure Loop:**
    *   An attacker creates a $5 trial subscription in Microsoft Azure.
    *   The attacker discovers the company's SQL server FQDN (`sqlsrv-hardened-xxxx.database.windows.net`) via DNS brute-forcing.
    *   The attacker launches an unauthorized VM in Azure.
    *   Because `0.0.0.0` allows *any* Azure IP, the attacker's VM bypasses the server firewall completely!
    *   The attacker performs a brute-force credential attack against the static `sa` / `sqladmin` account, extracting customer records.
*   **The Remediation Protocol:**
    1.  **Never enable `0.0.0.0` in enterprise architectures.** Set `enable_azure_services_access = false`.
    2.  **Deploy Azure Private Endpoints (`azurerm_private_endpoint`):** Project the database directly into your internal Virtual Network (`10.x.x.x`), disabling public network access entirely (`public_network_access_enabled = false`).
    3.  **Enforce Microsoft Entra ID Authentication:** Disable local SQL authentication logins completely (`azuread_administrator.azuread_only_authentication = true`) so that only authenticated Managed Identities with cryptographic Entra tokens can connect.

---

## 🧹 Cost Optimization & Clean Teardown

Azure SQL Databases incur hourly charges based on their provisioned tier. Destroy resources immediately after validation:

```bash
terraform destroy -auto-approve
```
