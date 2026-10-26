---
obsidianUIMode: preview
class: project-note
tier: project
domains:
  - terraform
  - azure
concepts_referenced:
  - "[[14-Index - Terraform on Azure]]"
  - "[[13-104-09_administer_azure_virtual_machines]]"
  - "[[13-104-07_administer_network_traffic]]"
  - "[[13-3_azure_compute_services_and_workload_paradigms]]"
difficulty: intermediate
status: completed
---

# Project 01: High Availability & Scalable Infrastructure with VMSS & Auto-Scaling

**Breadcrumbs:** [[--Index--|🏠 Index]] > [[14-Index - Terraform on Azure|☁️ Terraform on Azure MOC]] > [[README|Azure Terraform Projects]] > **Project 01: HA & VMSS**

---

## 🎯 Executive Overview & Architectural Objectives

Enterprise web applications require high availability across Availability Zones, automated traffic distribution, and dynamic scaling to handle traffic bursts without operational intervention.

In this project, you will act as a Lead Cloud Platform Engineer deploying a resilient, auto-scaling compute cluster on Microsoft Azure using Terraform. 

### Key Architectural Deliverables:
1.  **Virtual Network & Subnet Topology:** Provision a dedicated VNet (`10.0.0.0/16`) with an isolated compute subnet (`10.0.1.0/24`) and an NSG allowing inbound HTTP (80), HTTPS (443), and SSH (22).
2.  **Layer 4 Standard Load Balancer:** Deploy a public Azure Standard Load Balancer with a multi-zone static Public IP, backend address pool, health probe (`/healthz` or TCP 80), and load balancing rule.
3.  **Outbound Connectivity via NAT Gateway:** Attach an Azure NAT Gateway to prevent outbound SNAT (Source Network Address Translation) port exhaustion when VMSS nodes download OS updates or external dependencies.
4.  **Flexible Virtual Machine Scale Set (`azurerm_orchestrated_virtual_machine_scale_set`):** Provision a multi-zone Linux scale set running Ubuntu 22.04 LTS with automated cloud-init bootstrap (`user-data.sh`) serving an active Nginx web server.
5.  **Dynamic Metric-Based Autoscale Rules:** Configure an `azurerm_monitor_autoscale_setting` that monitors average CPU utilization across the cluster:
    *   **Scale Out:** Adds 1 instance if average CPU > 75% for 5 minutes (Cooldown: 5 minutes).
    *   **Scale In:** Removes 1 instance if average CPU < 25% for 5 minutes (Cooldown: 5 minutes).
    *   **Capacity Boundaries:** Minimum: 2, Default: 3, Maximum: 6 instances.
6.  **State Drift Prevention:** Implement `lifecycle { ignore_changes = [ instances ] }` on the scale set to prevent Terraform from fighting Azure's autoscale engine.

---

## 🏛️ Target Architecture & Component Topology

```mermaid
flowchart TD
    subgraph InternetClients ["Public Internet & End-Users"]
        Clients["Inbound HTTP/HTTPS Traffic"]
    end

    subgraph AzureRegion ["Azure Region: East US (Multi-Zone)"]
        subgraph VNet ["Virtual Network: vnet-compute-prod (10.0.0.0/16)"]
            subgraph WorkloadSubnet ["snet-workload (10.0.1.0/24)"]
                VMSS_Inst1["VMSS Node 01 (Zone 1)\nNginx Webserver"]
                VMSS_Inst2["VMSS Node 02 (Zone 2)\nNginx Webserver"]
                VMSS_Inst3["VMSS Node 03 (Zone 3)\nNginx Webserver"]
            end

            subgraph IngressLayer ["Ingress & Outbound Edge"]
                PubIP["Standard Public IP (Static, Multi-Zone)"]
                LB["Azure Standard Load Balancer\n- Health Probe: TCP 80\n- Load Balancing Rule: Port 80 ➔ Backend Pool"]
                NatGW["Azure NAT Gateway\n(Dedicated Outbound SNAT IP)"]
            end
        end

        subgraph MonitoringControl ["Azure Monitor Autoscale Engine"]
            Autoscale["Autoscale Setting\n- Scale Out: CPU > 75% (Add 1)\n- Scale In: CPU < 25% (Remove 1)\n- Limits: Min 2, Max 6"]
        end
    end

    Clients -->|Port 80 / 443| PubIP
    PubIP --> LB
    LB -->|Distributes Traffic| WorkloadSubnet
    WorkloadSubnet --> NatGW
    NatGW -->|Outbound Updates (Zero SNAT Drops)| InternetClients

    MonitoringControl -.->|Evaluates Metric Rules| WorkloadSubnet
```

---

## 🧠 Deep-Intuition Azure Administration & Architectural Mechanics

### 1. Why Flexible Orchestration (`azurerm_orchestrated_virtual_machine_scale_set`)?
Historically, Azure provided **Uniform VMSS**, where all instances were identical copies spun up from a single golden VHD image without individual instance identities.
*   **Flexible Orchestration Mode** is the modern cloud standard: it distributes standard individual VMs across Availability Zones and Fault Domains, allows mixed VM sizes (e.g., mixing Spot and On-Demand instances), and enables individual instance patching and maintenance without tearing down the entire scale set.

### 2. Standard Load Balancer & The SNAT Port Exhaustion Trap
*   In Azure, **Standard Load Balancers are closed by default**. Unlike legacy Basic LBs, backend instances behind a Standard LB cannot access the public internet for outbound traffic unless an explicit outbound rule or an **Azure NAT Gateway** is provisioned.
*   When hundreds of scale set instances initiate outbound connections simultaneously (e.g., running `apt-get update`), relying on default Azure outbound IPs causes **SNAT Port Exhaustion**, dropping connections randomly. A dedicated Azure NAT Gateway allocates up to 64,000 concurrent SNAT ports per IP, completely eliminating outbound packet drops.

### 3. The Terraform Autoscale "State War" (The Lifecycle Rule)
When Azure Monitor triggers a scale-out event (scaling instances from 3 to 4), Azure's runtime control plane updates the scale set's `instances` count.
*   If an engineer runs `terraform apply`, Terraform compares the live cloud state (`instances = 4`) with the code (`instances = 3`) and forcefully terminates the newly scaled node!
*   To prevent this conflict, we declare **`lifecycle { ignore_changes = [ instances ] }`**, delegating scaling operations entirely to Azure Monitor.

---

## 💻 Complete Production-Grade Terraform Code

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
      version = "~> 3.6.0"
    }
  }
}

provider "azurerm" {
  features {
    resource_group {
      prevent_deletion_if_contains_resources = false
    }
  }
}
```

### 2. `variables.tf`
```hcl
variable "resource_group_name" {
  type        = string
  description = "Name of the target resource group."
  default     = "rg-ha-vmss-prod"
}

variable "location" {
  type        = string
  description = "Azure region for deployment."
  default     = "eastus"
}

variable "admin_username" {
  type        = string
  description = "Administrator username for Linux VMs."
  default     = "azureuser"
}

variable "vm_sku" {
  type        = string
  description = "Compute SKU tier for scale set instances."
  default     = "Standard_D2s_v5"
}

variable "min_instances" {
  type        = number
  description = "Minimum number of instances for autoscale."
  default     = 2
}

variable "max_instances" {
  type        = number
  description = "Maximum number of instances for autoscale."
  default     = 6
}
```

### 3. `network.tf` (VNet, Subnet, NSG & NAT Gateway)
```hcl
resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
  tags = {
    Environment = "Production"
    Project     = "HA-ScaleSet"
    ManagedBy   = "Terraform"
  }
}

resource "azurerm_virtual_network" "vnet" {
  name                = "vnet-compute-prod"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}

resource "azurerm_subnet" "subnet" {
  name                 = "snet-workload"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = ["10.0.1.0/24"]
}

# Network Security Group
resource "azurerm_network_security_group" "nsg" {
  name                = "nsg-workload-web"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name

  security_rule {
    name                       = "AllowHTTPInbound"
    priority                   = 100
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "80"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }

  security_rule {
    name                       = "AllowHTTPSInbound"
    priority                   = 110
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "443"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
}

resource "azurerm_subnet_network_security_group_association" "nsg_assoc" {
  subnet_id                 = azurerm_subnet.subnet.id
  network_security_group_id = azurerm_network_security_group.nsg.id
}

# Azure NAT Gateway (Dedicated Outbound SNAT)
resource "azurerm_public_ip" "nat_pip" {
  name                = "pip-natgw-outbound"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  allocation_method   = "Static"
  sku                 = "Standard"
  zones               = ["1", "2", "3"]
}

resource "azurerm_nat_gateway" "nat_gw" {
  name                    = "natgw-compute-prod"
  location                = azurerm_resource_group.rg.location
  resource_group_name     = azurerm_resource_group.rg.name
  sku_name                = "Standard"
  idle_timeout_in_minutes = 10
}

resource "azurerm_nat_gateway_public_ip_association" "nat_pip_assoc" {
  nat_gateway_id       = azurerm_nat_gateway.nat_gw.id
  public_ip_address_id = azurerm_public_ip.nat_pip.id
}

resource "azurerm_subnet_nat_gateway_association" "subnet_nat_assoc" {
  subnet_id      = azurerm_subnet.subnet.id
  nat_gateway_id = azurerm_nat_gateway.nat_gw.id
}
```

### 4. `loadbalancer.tf`
```hcl
resource "random_string" "dns_suffix" {
  length  = 6
  special = false
  upper   = false
}

resource "azurerm_public_ip" "lb_pip" {
  name                = "pip-lb-web"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  allocation_method   = "Static"
  sku                 = "Standard"
  zones               = ["1", "2", "3"]
  domain_name_label   = "web-ha-${random_string.dns_suffix.result}"
}

resource "azurerm_lb" "lb" {
  name                = "lb-web-external"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "Standard"

  frontend_ip_configuration {
    name                 = "LoadBalancerFrontend"
    public_ip_address_id = azurerm_public_ip.lb_pip.id
  }
}

resource "azurerm_lb_backend_address_pool" "bepool" {
  name            = "bepool-web-servers"
  loadbalancer_id = azurerm_lb.lb.id
}

resource "azurerm_lb_probe" "http_probe" {
  name            = "probe-http-port80"
  loadbalancer_id = azurerm_lb.lb.id
  protocol        = "Tcp"
  port            = 80
  interval_in_seconds = 5
  number_of_probes    = 2
}

resource "azurerm_lb_rule" "http_rule" {
  name                           = "LBRule-HTTP-80"
  loadbalancer_id                = azurerm_lb.lb.id
  protocol                       = "Tcp"
  frontend_port                  = 80
  backend_port                   = 80
  frontend_ip_configuration_name = "LoadBalancerFrontend"
  backend_address_pool_ids       = [azurerm_lb_backend_address_pool.bepool.id]
  probe_id                       = azurerm_lb_probe.http_probe.id
  disable_outbound_snat          = true # Delegates outbound SNAT to NAT Gateway
}
```

### 5. `vmss.tf` & `user-data.sh`
Create the cloud-init bootstrap script `user-data.sh`:
```bash
#!/bin/bash
apt-get update -y
apt-get install -y nginx curl jq
HOSTNAME=$(hostname)
INSTANCE_IP=$(hostname -I | cut -d' ' -f1)
cat <<EOF > /var/www/html/index.html
<!DOCTYPE html>
<html>
<head><title>HA Azure VMSS Cluster</title></head>
<body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
  <h1 style="color: #0078D4;">Production Azure VMSS with Terraform</h1>
  <p>Served by Worker Node: <strong>${HOSTNAME}</strong></p>
  <p>Internal Private IP: <strong>${INSTANCE_IP}</strong></p>
  <p>Status: <span style="color: green; font-weight: bold;">Healthy</span></p>
</body>
</html>
EOF
systemctl enable nginx
systemctl restart nginx
```

Now define `vmss.tf`:
```hcl
# Generate SSH key pair for secure administrative access
resource "tls_private_key" "ssh" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "azurerm_orchestrated_virtual_machine_scale_set" "vmss" {
  name                        = "vmss-web-prod"
  location                    = azurerm_resource_group.rg.location
  resource_group_name         = azurerm_resource_group.rg.name
  sku_name                    = var.vm_sku
  instances                   = 3
  platform_fault_domain_count = 1
  zones                       = ["1", "2", "3"]

  user_data_base64 = base64encode(file("${path.module}/user-data.sh"))

  os_profile {
    linux_configuration {
      disable_password_authentication = true
      admin_username                  = var.admin_username
      admin_ssh_key {
        username   = var.admin_username
        public_key = tls_private_key.ssh.public_key_openssh
      }
    }
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-LTS-gen2"
    version   = "latest"
  }

  os_disk {
    storage_account_type = "Premium_LRS"
    caching              = "ReadWrite"
  }

  network_interface {
    name                          = "nic-vmss-web"
    primary                       = true
    enable_accelerated_networking = false

    ip_configuration {
      name                                   = "ipconfig-primary"
      primary                                = true
      subnet_id                              = azurerm_subnet.subnet.id
      load_balancer_backend_address_pool_ids = [azurerm_lb_backend_address_pool.bepool.id]
    }
  }

  lifecycle {
    # Crucial: Protects autoscale runtime updates from Terraform reset
    ignore_changes = [
      instances
    ]
  }
}
```

### 6. `autoscale.tf`
```hcl
resource "azurerm_monitor_autoscale_setting" "autoscale" {
  name                = "autoscale-vmss-cpu"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  target_resource_id  = azurerm_orchestrated_virtual_machine_scale_set.vmss.id

  profile {
    name = "DefaultAutoscaleProfile"

    capacity {
      default = 3
      minimum = var.min_instances
      maximum = var.max_instances
    }

    # Scale Out Rule (CPU > 75%)
    rule {
      metric_trigger {
        metric_name        = "Percentage CPU"
        metric_resource_id = azurerm_orchestrated_virtual_machine_scale_set.vmss.id
        time_grain         = "PT1M"
        statistic          = "Average"
        time_window        = "PT5M"
        time_aggregation   = "Average"
        operator           = "GreaterThan"
        threshold          = 75
      }

      scale_action {
        direction = "Increase"
        type      = "ChangeCount"
        value     = "1"
        cooldown  = "PT5M"
      }
    }

    # Scale In Rule (CPU < 25%)
    rule {
      metric_trigger {
        metric_name        = "Percentage CPU"
        metric_resource_id = azurerm_orchestrated_virtual_machine_scale_set.vmss.id
        time_grain         = "PT1M"
        statistic          = "Average"
        time_window        = "PT5M"
        time_aggregation   = "Average"
        operator           = "LessThan"
        threshold          = 25
      }

      scale_action {
        direction = "Decrease"
        type      = "ChangeCount"
        value     = "1"
        cooldown  = "PT5M"
      }
    }
  }
}
```

### 7. `outputs.tf`
```hcl
output "load_balancer_public_ip" {
  value       = azurerm_public_ip.lb_pip.ip_address
  description = "Public IP address of the Standard Load Balancer."
}

output "load_balancer_fqdn" {
  value       = "http://${azurerm_public_ip.lb_pip.fqdn}"
  description = "Fully qualified domain name for the load balancer."
}
```

---

## 🛠️ Step-by-Step Implementation Walkthrough

1.  **Initialize the Terraform Workspace:**
    ```bash
    terraform init
    ```
2.  **Validate & Plan Infrastructure:**
    ```bash
    terraform validate
    terraform plan -out=tfplan
    ```
3.  **Deploy Resources to Azure:**
    ```bash
    terraform apply tfplan
    ```
4.  👁️ **Visual Checkpoint in Azure Portal:**
    *   Open **Virtual machine scale sets** ➔ Click `vmss-web-prod`.
    *   Under **Settings**, click **Instances**. Verify 3 running instances distributed across Zone 1, Zone 2, and Zone 3.
    *   Under **Monitoring**, click **Scaling**. Confirm the custom metric rules (CPU > 75% scale out, CPU < 25% scale in).
    *   Navigate to **Load balancers** ➔ `lb-web-external` ➔ Verify backend pool displays 3 healthy targets.

---

## 🔬 Verification & Live Probe Testing

Execute these tests in your terminal:

```bash
# 1. Retrieve the Load Balancer FQDN
LB_URL=$(terraform output -raw load_balancer_fqdn)
echo "Testing Load Balancer Endpoint: ${LB_URL}"

# 2. Issue multiple requests to observe round-robin distribution across instances
for i in {1..6}; do
  curl -s "${LB_URL}" | grep "Served by Worker Node"
  sleep 1
done
```
**Expected Output:** Notice different worker hostnames responding, proving that the Layer 4 Standard Load Balancer is actively distributing connections across availability zones!

---

## ⚠️ "See It in Action" Real-World Failure & Recovery Loop (AARF)

### Scenario: The Autoscale Fighting Loop (The Missing Ignore Changes)
*   **The Assumption:** An engineer assumes that Terraform code should always explicitly dictate the current instance count: `instances = 3`.
*   **The Failure Loop:**
    *   During Black Friday, incoming web traffic surges. Azure Monitor autoscale rules detect CPU > 75% and scale the VMSS from 3 to 6 instances.
    *   A DevOps engineer deploys an unrelated DNS tag change using `terraform apply`.
    *   Terraform evaluates `instances = 3` in code vs. `instances = 6` in Azure. Terraform forcefully terminates 3 healthy production instances under peak load, crashing the website!
*   **The Root Cause:**
    *   Terraform assumes state drift must always be reconciled back to HCL.
*   **The Remediation:**
    *   Always add `lifecycle { ignore_changes = [ instances ] }` on resources where an external Azure auto-scaling engine is delegated runtime authority.

---

## 🧹 Cost Optimization & Clean Teardown

Run this command to destroy all compute instances, NAT gateways, and load balancers:

```bash
terraform destroy -auto-approve
```
