---
obsidianUIMode: preview
class: project-note
tier: project
domains:
  - terraform
  - azure
  - monitoring
concepts_referenced:
  - "[[14-Index - Terraform on Azure]]"
  - "[[13-104-12_administer_monitoring]]"
  - "[[13-7_azure_management_monitoring_and_deployment_tooling]]"
  - "[[13-Index - Azure]]"
difficulty: intermediate
status: completed
---

# Project 10: Full-Stack Monitoring, Log Analytics & Automated Alerts as Code

**Breadcrumbs:** [[--Index--|🏠 Index]] > [[14-Index - Terraform on Azure|☁️ Terraform on Azure MOC]] > [[README|Azure Terraform Projects]] > **Project 10: Full-Stack Monitoring**

---

## 🎯 Executive Overview & Architectural Objectives

Infrastructure as Code is incomplete without Day-2 observability. Deploying compute, databases, and networking without automated metric thresholds and telemetry pipelines creates operational blind spots, allowing resource degradation and memory leaks to silently spiral into customer-facing downtime.

In this project, you will engineer a centralized **Azure Monitor Observability & Alerting Platform** using Terraform. You will provision a centralized Log Analytics Workspace with FinOps cost caps, configure Azure Monitor Action Groups for incident escalation, establish near-real-time metric alert rules, instrument diagnostic log streaming, and execute a live synthetic CPU saturation drill on a Linux VM to validate automated alert triggers.

### Key Architectural Deliverables:
1.  **Central Log Analytics Workspace (`azurerm_log_analytics_workspace`):** Deploy a unified telemetry sink with 30-day retention and a strict FinOps daily ingestion quota (`daily_quota_gb = 1.0`).
2.  **Notification Action Group (`azurerm_monitor_action_group`):** Provision an automated incident dispatch mechanism configuring email notification channels and webhook endpoints.
3.  **Near-Real-Time Metric Alerts (`azurerm_monitor_metric_alert`):** Codify dynamic metric threshold rules monitoring compute health (CPU saturation > 75%, Available Memory < 200MB) evaluated over 5-minute sliding windows.
4.  **Diagnostic Settings Streaming (`azurerm_monitor_diagnostic_setting`):** Declaratively stream platform metrics and audit logs from infrastructure resources into Log Analytics.
5.  **Live Synthetic Stress Drill:** Execute synthetic Linux CPU stress tests (`stress-ng`) to force the Azure Monitor state machine from `Healthy` to `Fired`, verifying alert notification dispatch.

---

## 🏛️ Target Architecture & Component Topology

```mermaid
flowchart TD
    subgraph ComputeWorkload ["Monitored Infrastructure Tier"]
        VM["Linux Virtual Machine\n(Ubuntu 22.04 LTS)\n- Synthetic Load Generated via stress"]
        NIC["Network Interface (Private IP)"]
        VM --- NIC
    end

    subgraph ObservabilityPlatform ["Azure Monitor Platform"]
        direction TB
        
        MetricsEngine["Azure Monitor Metrics Pipeline\n(Near-Real-Time Ingestion: 1-min frequency)"]
        
        LAW["Log Analytics Workspace: law-central-prod\n- SKU: PerGB2018\n- Retention: 30 Days\n- Daily FinOps Cap: 1.0 GB"]
        
        subgraph AlertingEngine ["Metric Alert Rules Engine"]
            AlertCPU["Metric Alert: alert-vm-high-cpu\nCondition: Percentage CPU > 75%\nWindow: 5 min | Frequency: 1 min"]
            AlertMem["Metric Alert: alert-vm-low-memory\nCondition: Available Memory < 200MB"]
        end

        ActionGroup["Azure Monitor Action Group: ag-devops-oncall\n- Short Name: devopsoncall\n- Email: ops-team@example.com\n- Webhook: https://api.pagerduty.com/..."]
    end

    subgraph Operators ["Operations & SRE Escalation"]
        Email["Ops Engineer Inbox"]
        Slack["Incident ChatOps / Webhook"]
    end

    VM -->|Streams Platform Telemetry| MetricsEngine
    VM -->|Diagnostic Logs & Syslog| LAW
    
    MetricsEngine -->|Evaluates Thresholds| AlertCPU
    MetricsEngine -->|Evaluates Thresholds| AlertMem
    
    AlertCPU -->|Fires (Status: Activated)| ActionGroup
    AlertMem -->|Fires (Status: Activated)| ActionGroup
    
    ActionGroup --> Email
    ActionGroup --> Slack
```

---

## 🧠 Deep-Intuition Azure Administration & Architectural Mechanics

### 1. Metric Alerts vs. Log Query (KQL) Alerts
Azure Monitor provides two distinct alerting paradigms with fundamentally different latency, cost, and diagnostic characteristics:

| Architectural Property | Metric Alerts (`azurerm_monitor_metric_alert`) | Scheduled Query / Log Alerts (`azurerm_monitor_scheduled_query_rules_alert`) |
| :--- | :--- | :--- |
| **Data Source** | Native Azure platform time-series metric store. | Log Analytics Workspace tables (`AzureActivity`, `Syslog`, etc.). |
| **Evaluation Latency** | **Near-real-time (1–2 minutes)**. Evaluated continuously. | **5 to 15 minutes** (governed by log ingestion lag). |
| **State Tracking** | **Stateful**: Automatically tracks `Fired` and `Resolved` states without duplicate alerts. | **Stateless**: Evaluates whether KQL query returns rows in the window. |
| **Use Cases** | Infrastructure health: CPU > 85%, Network In/Out spikes, Disk IOPS saturation. | Complex correlation: HTTP 500 error counts, failed SSH logins, multi-resource logs. |

### 2. The FinOps Daily Ingestion Cap Safeguard
In enterprise cloud environments, runaway logging is one of the most common causes of unexpected Azure bills. An misconfigured application logging in verbose debug mode can ingest hundreds of gigabytes per hour.
*   **The Ingestion Model:** Log Analytics charges per gigabyte ingested (Pay-as-you-go).
*   **The Guardrail:** Setting `daily_quota_gb = 1.0` configures Azure to monitor ingestion volume against a daily ceiling. If application telemetry exceeds 1.0 GB in a single calendar day, Azure automatically suspends log ingestion until the next UTC reset, protecting the enterprise from unexpected multi-thousand dollar overage bills.

---

## 💻 Complete Production-Grade Terraform Code

Organize your project into the following directory:

```
project-10-monitoring/
├── provider.tf
├── variables.tf
├── network.tf
├── compute.tf
├── monitoring.tf
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
  }
}

provider "azurerm" {
  features {}
}
```

### 2. `variables.tf`
```hcl
variable "resource_group_name" {
  type        = string
  default     = "rg-monitoring-prod"
  description = "Resource Group for monitoring resources and test VM."
}

variable "location" {
  type        = string
  default     = "eastus"
  description = "Azure region for deployment."
}

variable "alert_email" {
  type        = string
  default     = "admin@example.com" # Replace with your real notification email
  description = "Target email address for Action Group notifications."
}

variable "admin_username" {
  type        = string
  default     = "azureuser"
  description = "Admin username for the test Linux VM."
}
```

### 3. `network.tf`
```hcl
resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
  tags = {
    Environment = "Observability"
    ManagedBy   = "Terraform"
  }
}

resource "azurerm_virtual_network" "vnet" {
  name                = "vnet-monitoring-demo"
  address_space       = ["10.50.0.0/16"]
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}

resource "azurerm_subnet" "subnet" {
  name                 = "snet-workloads"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = ["10.50.1.0/24"]
}

resource "azurerm_public_ip" "vm_pip" {
  name                = "pip-test-vm"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  allocation_method   = "Static"
  sku                 = "Standard"
}

resource "azurerm_network_security_group" "nsg" {
  name                = "nsg-test-vm"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name

  security_rule {
    name                       = "AllowSSH"
    priority                   = 1000
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "22"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
}

resource "azurerm_network_interface" "vm_nic" {
  name                = "nic-test-vm"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.subnet.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.vm_pip.id
  }
}

resource "azurerm_network_interface_security_group_association" "nic_nsg" {
  network_interface_id      = azurerm_network_interface.vm_nic.id
  network_security_group_id = azurerm_network_security_group.nsg.id
}
```

### 4. `compute.tf` (Monitored Workload VM)
```hcl
resource "azurerm_linux_virtual_machine" "test_vm" {
  name                  = "vm-monitored-workload"
  resource_group_name   = azurerm_resource_group.rg.name
  location              = azurerm_resource_group.rg.location
  size                  = "Standard_B2s"
  admin_username        = var.admin_username
  network_interface_ids = [azurerm_network_interface.vm_nic.id]

  admin_ssh_key {
    username   = var.admin_username
    public_key = file("~/.ssh/id_rsa.pub")
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts-gen2"
    version   = "latest"
  }

  # Cloud-init to preinstall stress-ng utility for the live alert test
  custom_data = base64encode(<<-EOF
    #!/bin/bash
    apt-get update -y
    apt-get install -y stress-ng htop
  EOF
  )

  tags = {
    Role = "MetricTestWorkload"
  }
}
```

### 5. `monitoring.tf` (Workspace, Action Group & Metric Alerts)
```hcl
# 1. Central Log Analytics Workspace with FinOps Daily Cap
resource "azurerm_log_analytics_workspace" "law" {
  name                = "law-central-observability"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "PerGB2018"
  retention_in_days   = 30

  # FinOps Safeguard: Strict 1.0 GB daily volume ceiling
  daily_quota_gb = 1.0

  tags = {
    Purpose = "CentralizedObservability"
  }
}

# 2. Azure Monitor Action Group for Alert Escalation
resource "azurerm_monitor_action_group" "devops_alert" {
  name                = "ag-devops-oncall"
  resource_group_name = azurerm_resource_group.rg.name
  short_name          = "devopsoncall"

  email_receiver {
    name                    = "PrimaryIncidentEmail"
    email_address           = var.alert_email
    use_common_alert_schema = true
  }
}

# 3. High CPU Metric Alert (Stateful, 5-minute rolling window)
resource "azurerm_monitor_metric_alert" "vm_cpu_alert" {
  name                = "alert-vm-high-cpu-utilization"
  resource_group_name = azurerm_resource_group.rg.name
  scopes              = [azurerm_linux_virtual_machine.test_vm.id]
  description         = "Triggered when VM CPU saturation exceeds 75% for 5 consecutive minutes."
  severity            = 2 # Severity: Warning
  frequency           = "PT1M" # Evaluated every 1 minute
  window_size         = "PT5M" # 5-minute aggregation window

  criteria {
    metric_namespace = "Microsoft.Compute/virtualMachines"
    metric_name      = "Percentage CPU"
    aggregation      = "Average"
    operator         = "GreaterThan"
    threshold        = 75.0
  }

  action {
    action_group_id = azurerm_monitor_action_group.devops_alert.id
  }
}

# 4. Low Available Memory Metric Alert
resource "azurerm_monitor_metric_alert" "vm_memory_alert" {
  name                = "alert-vm-low-available-memory"
  resource_group_name = azurerm_resource_group.rg.name
  scopes              = [azurerm_linux_virtual_machine.test_vm.id]
  description         = "Triggered when Available Memory drops below 200MB."
  severity            = 1 # Severity: Error
  frequency           = "PT1M"
  window_size         = "PT5M"

  criteria {
    metric_namespace = "Microsoft.Compute/virtualMachines"
    metric_name      = "Available Memory Bytes"
    aggregation      = "Average"
    operator         = "LessThan"
    threshold        = 209715200 # 200 Megabytes in bytes
  }

  action {
    action_group_id = azurerm_monitor_action_group.devops_alert.id
  }
}
```

### 6. `outputs.tf`
```hcl
output "vm_public_ip" {
  value       = azurerm_public_ip.vm_pip.ip_address
  description = "Public IP address to SSH into the test workload VM."
}

output "log_analytics_workspace_id" {
  value       = azurerm_log_analytics_workspace.law.id
  description = "Resource ID of the central Log Analytics Workspace."
}

output "action_group_id" {
  value       = azurerm_monitor_action_group.devops_alert.id
  description = "Resource ID of the incident Action Group."
}
```

---

## 🛠️ Step-by-Step Implementation Walkthrough

### 1. Apply Monitoring Platform & Workload
```bash
terraform init
terraform plan -var="alert_email=your.email@example.com" -out=tfplan
terraform apply tfplan
```

### 2. 👁️ Visual Checkpoint in Azure Portal
1.  Navigate to **Log Analytics workspaces** in the Azure Portal:
    *   Click `law-central-observability`.
    *   Under **Settings**, click **Usage and estimated costs** ➔ **Daily cap**:
        *   Confirm Daily cap is **ON** and set to `1.0 GB/day`.
2.  Navigate to **Monitor** ➔ Click **Alerts** in the sidebar:
    *   Click **Alert rules** in the top navigation bar.
    *   Verify both rules exist: `alert-vm-high-cpu-utilization` and `alert-vm-low-available-memory`.
    *   Confirm Target resource: `vm-monitored-workload` and Status: **Enabled**.
3.  Click **Action groups** in Monitor: Confirm `ag-devops-oncall` with your configured email receiver.

---

## 🔬 Verification & Live Probe Testing

To prove that the observability loop triggers and notifies engineers under actual workload duress, execute a synthetic CPU saturation drill on the VM.

### 1. Connect to VM & Trigger Synthetic Load
```bash
VM_IP=$(terraform output -raw vm_public_ip)
ssh azureuser@$VM_IP

# Verify stress-ng is installed
stress-ng --version

# Squelch both virtual CPU cores at 100% load for 6 minutes (360 seconds)
stress-ng --cpu 2 --cpu-load 100 --timeout 360s
```

### 2. Observe Real-Time Metric Spikes in Azure CLI
In another terminal tab, query Azure Monitor metrics directly:

```bash
az monitor metrics list \
  --resource $(az vm show -g rg-monitoring-prod -n vm-monitored-workload --query id -o tsv) \
  --metric "Percentage CPU" \
  --interval PT1M
```
You will observe `Percentage CPU` jump from ~2% to 99.8%!

### 3. Verify Alert State Transition
After the 5-minute aggregation window completes:
1.  Open **Azure Monitor** ➔ **Alerts**.
2.  The `alert-vm-high-cpu-utilization` rule transitions from `Resolved` to `Fired` (Severity 2).
3.  Check your email inbox: You will receive an official notification from Microsoft Azure Alert with subject:
    `[Alert Activated] Warning: alert-vm-high-cpu-utilization on vm-monitored-workload`.
4.  Once the 6-minute `stress-ng` run completes and CPU falls below 75%, Azure Monitor's stateful engine automatically fires a `[Alert Resolved]` email!

---

## ⚠️ "See It in Action" Real-World Failure & Recovery Loop (AARF)

### Scenario: The $10,000 "Runaway Log Ingestion" Disaster
*   **The Architecture:** An engineering team connects 100 microservices running on Azure to a single central Log Analytics workspace without configuring ingestion controls.
*   **The Assumption:** The team assumes logs only generate trivial text charges.
*   **The Failure Loop:**
    *   A minor bug in a backend microservice causes an infinite loop that logs complete request and response payloads with stack traces 50 times per second per pod.
    *   Over a long holiday weekend, the microservices flood Log Analytics with over **3.5 Terabytes of log data per day**.
    *   By Monday morning, the workspace has accrued over $12,000 in unexpected ingestion and data retention fees!
*   **The Remediation Protocol:**
    1.  **Always enforce `daily_quota_gb`:** Codify `daily_quota_gb = 5.0` (or team-approved limit) in your HCL. When the cap is reached, ingestion stops automatically.
    2.  **Enable Ingestion Cap Alerts:** Azure Monitor automatically triggers an alert when 100% of the daily cap is reached.
    3.  **Data Collection Rules (DCR):** Use Azure Monitor DCRs to filter out `DEBUG` and `INFO` log levels at the agent collector before data is transmitted over the wire to Azure.

---

## 🧹 Cost Optimization & Clean Teardown

```bash
terraform destroy -auto-approve
```
