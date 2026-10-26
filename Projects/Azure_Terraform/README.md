---
obsidianUIMode: preview
class: project-note
tier: project
domains:
  - terraform
  - azure
concepts_referenced:
  - "[[14-Index - Terraform on Azure]]"
  - "[[13-Index - Azure]]"
  - "[[13-Index - AZ-104]]"
difficulty: advanced
status: completed
---

# Azure Terraform: Enterprise Cloud Architecture & Administration Projects

**Breadcrumbs:** [[--Index--|🏠 Index]] > [[14-Index - Terraform on Azure|☁️ Terraform on Azure MOC]] > **Azure Terraform Projects Hub**

---

## 🎯 Curriculum Overview & Engineering Philosophy

Welcome to the **Azure Terraform Enterprise Projects Portfolio**. While theory provides the vocabulary of cloud engineering, production competency requires designing, deploying, and maintaining real-world architectures with code.

This project curriculum is structured as an **in-depth walkthrough to Azure Administration and Solution Architecture**. Each project models a complete, real-world enterprise infrastructure challenge—moving progressively from foundational compute resilience and network segmentation to zero-trust identity, serverless runtimes, enterprise modular Kubernetes, policy-as-code governance, brownfield reverse-engineering, and GitOps automation pipelines.

```
+---------------------------------------------------------------------------------------------------+
|                        Azure Terraform Progressive Learning & Delivery Stages                      |
+---------------------------------------------------------------------------------------------------+
| Stage 1: Core Compute & Networking Resilience                                                     |
|   - Project 01: High Availability & Scalable Infrastructure with VMSS & Auto-scaling              |
|   - Project 02: Enterprise Virtual Network Topology & Global VNet Peering                         |
|   - Project 03: Microsoft Entra ID Authentication, Service Principals & RBAC as Code              |
+---------------------------------------------------------------------------------------------------+
| Stage 2: Cloud-Native PaaS & Serverless Workloads                                                 |
|   - Project 04: Azure App Service with Blue/Green Zero-Downtime Deployment Slots                  |
|   - Project 05: Serverless Event-Driven Azure Functions (QR Code Generator)                       |
|   - Project 06: Terraform Provisioners vs. Native Cloud-Init & Custom Script Extensions           |
+---------------------------------------------------------------------------------------------------+
| Stage 3: Enterprise Platform Engineering & Governance                                             |
|   - Project 07: Enterprise Modular Azure Kubernetes Service (AKS) & Key Vault                     |
|   - Project 08: Azure Policy as Code & Enterprise Compliance Enforcement                          |
|   - Project 09: Hardened Azure SQL Database Server & Firewall Rules as Code                        |
|   - Project 10: Full-Stack Observability with Log Analytics, Metric Alerts & Action Groups        |
+---------------------------------------------------------------------------------------------------+
| Stage 4: Advanced Delivery, Migration & Enterprise GitOps                                         |
|   - Project 11: Terraform Import & Reverse Engineering Live Azure Clouds via aztfy                 |
|   - Project 12: HCP Terraform Cloud Workspaces & Dynamic Workload Identity Federation             |
|   - Project 13: Azure DevOps End-to-End Enterprise CI/CD Pipeline for Terraform                   |
|   - Project 14: Resilient 3-Tier Enterprise Architecture on Azure (Web, App, DB)                  |
|   - Project 15: End-to-End GitOps on Azure Kubernetes Service with ArgoCD                         |
+---------------------------------------------------------------------------------------------------+
```

---

## 🗺️ Master Project Roadmap & Architectural Matrix

| Project | Target Architecture & Azure Services | Key Terraform Resources & Concepts | Azure Administration & Architecture Skill |
| :--- | :--- | :--- | :--- |
| **[[Project-01_HA_Scalable_Infrastructure_VMSS\|Project 01: HA & VMSS]]** | Virtual Network, Subnet, NSG, Standard Public IP, Standard Load Balancer, NAT Gateway, Flexible VMSS, Autoscale. | `azurerm_orchestrated_virtual_machine_scale_set`, `azurerm_lb`, `azurerm_monitor_autoscale_setting`. | Multi-zone compute resiliency, L4 load balancing, outbound SNAT via NAT Gateway, and metric-based scaling. |
| **[[Project-02_VNet_Architecture_and_Global_Peering\|Project 02: VNet Peering]]** | Multi-region VNets (East US & West US), Subnets, Dual Test VMs, Bidirectional VNet Peering links. | `azurerm_virtual_network_peering`, `allow_forwarded_traffic`, `allow_gateway_transit`, Provider aliasing. | High-speed global peering over Microsoft optical WAN, non-transitive routing, and latency testing. |
| **[[Project-03_Entra_ID_Identity_Governance_and_SPN\|Project 03: Entra ID & SPN]]** | Microsoft Entra ID App Registrations, Enterprise Service Principals, Client Secrets, Azure RBAC scopes. | `azuread_application`, `azuread_service_principal`, `azuread_service_principal_password`, `azurerm_role_assignment`. | Zero-trust machine identity management, scoped least-privilege RBAC, and secure CI/CD service connections. |
| **[[Project-04_App_Service_Blue_Green_Deployment_Slots\|Project 04: App Service Slots]]** | Linux App Service Plan P1v3, Web App, `staging` Deployment Slot, Sticky settings, Canary traffic routing (10%). | `azurerm_service_plan`, `azurerm_linux_web_app`, `azurerm_linux_web_app_slot`, `app_settings`. | PaaS compute scaling, zero-downtime blue/green deployments, warm-up validation, and sticky slot persistence. |
| **[[Project-05_Serverless_Azure_Functions_Event_Driven\|Project 05: Serverless Functions]]** | Consumption Function App (Python), Storage Account Blob Containers, Application Insights telemetry. | `azurerm_linux_function_app`, `azurerm_storage_account`, `azurerm_application_insights`. | Serverless event-driven architecture, scale-to-zero FinOps optimization, and storage input/output bindings. |
| **[[Project-06_Terraform_Provisioners_and_Cloud_Init\|Project 06: Provisioners & Cloud-Init]]** | Ubuntu Linux VM, SSH Key Pairs, `file`, `local-exec`, and `remote-exec` provisioners vs. native `custom_data`. | `provisioner "remote-exec"`, `null_resource`, `custom_data`, `base64encode(file("cloud-init.yaml"))`. | Imperative vs. declarative bootstrapping, why provisioners are a last resort, and cloud-init immutability. |
| **[[Project-07_Enterprise_Modular_AKS_Cluster\|Project 07: Modular AKS & Key Vault]]** | Custom HCL Module Architecture (`modules/network`, `modules/keyvault`, `modules/aks`), System-Assigned MSI. | `module "aks"`, `azurerm_kubernetes_cluster`, `azurerm_key_vault`, `default_node_pool`, Azure CNI. | Enterprise platform engineering, Day-2 Kubernetes operations as code, Secrets Store CSI driver integration. |
| **[[Project-08_Azure_Policy_and_Governance_as_Code\|Project 08: Azure Policy as Code]]** | Custom Policy Definitions (Allowed Locations), Policy Assignments scoped to Resource Groups, Non-Compliance msgs. | `azurerm_policy_definition`, `azurerm_resource_group_policy_assignment`, JSON ARM policy rules. | Preventative cloud guardrails, regulatory compliance automation, and audit vs. deny enforcement effects. |
| **[[Project-09_Secure_Azure_SQL_Database_and_Firewall\|Project 09: Azure SQL & Firewall]]** | Azure SQL Logical Server, General Purpose DB, Server Firewall Rules, Entra ID Admin integration. | `azurerm_mssql_server`, `azurerm_mssql_database`, `azurerm_mssql_firewall_rule`, `azuread_administrator`. | PaaS database security baselines, firewall whitelisting, avoiding plaintext passwords, and TDE encryption. |
| **[[Project-10_Full_Stack_Monitoring_Log_Analytics_and_Alerts\|Project 10: Full-Stack Monitoring]]** | Central Log Analytics Workspace, 1.0 GB Daily Volume Cap, Metric Alert rules, Action Groups (Email/Webhook). | `azurerm_log_analytics_workspace`, `azurerm_monitor_metric_alert`, `azurerm_monitor_action_group`. | FinOps ingestion capping, low-latency metric alerts vs. scheduled KQL alerts, automated operational escalations. |
| **[[Project-11_Terraform_Import_and_AzOps_Terrafy\|Project 11: Import & Azure Terrafy]]** | Reverse-engineering existing Azure Portal resources into declarative HCL code and synchronized state. | `terraform import`, Terraform 1.5+ `import {}` blocks, Azure Terrafy (`aztfy`), state reconciliation. | Brownfield cloud adoption, managing unmanaged portal drift, and safe infrastructure onboarding. |
| **[[Project-12_HCP_Terraform_Cloud_Workspaces\|Project 12: HCP Terraform Cloud]]** | HCP Terraform Organization, Remote Execution Workspaces, VCS-driven triggers, Azure OIDC dynamic credentials. | `cloud {}` block, Workload Identity Federation (OIDC), speculative execution plans, remote state locking. | Enterprise team collaboration at scale, secretless cloud authentication, and centralized governance. |
| **[[Project-13_Azure_DevOps_Enterprise_CICD_Pipeline\|Project 13: Azure DevOps CI/CD]]** | Multi-Stage Azure Pipelines YAML (`azure-pipelines.yml`), Service Connections, Manual Approval Gates. | Azure DevOps Pipeline Tasks, `terraform fmt -check`, `terraform plan`, Environment Gates, `terraform apply`. | Enterprise GitOps CI/CD delivery, security linting, multi-environment promotion, and automated state locks. |
| **[[Project-14_Production_3_Tier_Architecture_on_Azure\|Project 14: Resilient 3-Tier Architecture]]** | Web Tier (App Gateway + VMSS), App Tier (Internal LB + VMSS), DB Tier (Azure SQL + Private Endpoint). | Segmented subnets, strict stateful NSGs, Private DNS Zones, multi-tier dependency mapping. | Zero-trust enterprise network segmentation, end-to-end high availability across 3 Availability Zones. |
| **[[Project-15_Enterprise_AKS_GitOps_with_ArgoCD\|Project 15: AKS GitOps with ArgoCD]]** | Production AKS Cluster, Helm Provider bootstrapping ArgoCD, Kubernetes provider, GitOps reconciliation. | `provider "helm"`, `helm_release "argocd"`, `provider "kubernetes"`, Application CRDs. | Unified infrastructure and application delivery, Git as single source of truth, automated drift self-healing. |

---

## ⚙️ Standard Project Walkthrough Lifecycle

Every project document in this series adheres to a standardized, production-grade 7-section structure:

1. **🎯 Executive Overview & Architectural Objectives:** Business context, production motivations, and target deliverables.
2. **🏛️ Target Architecture & Component Topology:** Visual diagrams and component interaction flows.
3. **🧠 Deep-Intuition Azure Administration & Architectural Mechanics:** Clear explanations of the underlying Azure platform internals (e.g., how NAT Gateways handle SNAT port exhaustion, how Blob Leases prevent state corruption, how App Service deployment slots execute warmup pings).
4. **💻 Complete Production-Grade Terraform Code:** Full, working HCL files (`provider.tf`, `variables.tf`, `main.tf`, `outputs.tf`, `terraform.tfvars`) ready to execute.
5. **🛠️ Step-by-Step Implementation Walkthrough:** Exact terminal execution commands paired with **Azure Portal Visual Checkpoints** (`👁️ Visual Checkpoint`) so you can visually verify resources in the GUI.
6. **🔬 Verification & Live Probe Testing:** CLI queries, curl tests, and network verification commands proving operational success.
7. **⚠️ "See It in Action" Real-World Failure & Recovery Loop (AARF):** Practical Assumption-Architecture-Root-Cause-Failure scenarios analyzing common production pitfalls and their live fixes.
8. **🧹 Cost Optimization & Clean Teardown:** Explicit teardown commands to prevent unnecessary cloud expenditure.

---

## 📚 Curriculum Relationship to Certification Tracks

This hands-on portfolio aligns with and deepens the following Microsoft Azure certifications:

*   **Microsoft Certified: Azure Administrator Associate (AZ-104):** Compute (VMSS), Networking (VNets, Peering, Load Balancer, App Gateway), Storage, Entra ID Identity, Governance (Policies, RBAC), and Observability (Monitor, Alerts).
*   **Microsoft Certified: Azure Solutions Architect Expert (AZ-305):** Multi-region disaster recovery, High Availability 3-tier topologies, Zero Trust network isolation, Private Link, and automated GitOps application delivery.
