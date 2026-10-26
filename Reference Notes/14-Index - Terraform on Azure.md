---
obsidianUIMode: preview
class: index-note
tier: reference-note
tags:
  - terraform/azure
  - azure/iac
  - obsidian/moc
---

# ☁️ Terraform on Azure Reference MOC

**Breadcrumbs:** [[--Index--|🏠 Index]] > [[13-Index - Azure|☁️ Azure MOC]] > **Terraform on Azure Reference MOC**

---

## 🏛️ Theoretical Foundations & Core Frameworks

This index contains our canonical Terraform Infrastructure as Code (IaC) on Microsoft Azure curriculum, synthesized from industry-standard architectures, HashiCorp production recommendations, and comprehensive technical video series. It bridges fundamental IaC engine concepts directly into Azure administration and solution architecture.

- ⎈ **[[14-1_terraform_azure_foundations_and_state|Module 14-1: Terraform Core Engine, AzureRM Provider & State Locking]]**
  * Declarative IaC principles, mutable vs immutable infrastructure, the `azurerm` provider configuration (`features {}` block), authentication models (Azure CLI, Service Principal, Managed Identity, OIDC federation), remote state on Azure Storage Account blob containers, and native Blob Lease concurrency locking.
- ⚙️ **[[14-2_terraform_azure_variables_types_and_expressions|Module 14-2: Variables, Type Constraints, Dynamic Blocks & Expressions]]**
  * Input, output, and local variables, variable precedence hierarchy, primitive and structural type constraints (`object`, `tuple`, `map`, `list`), conditional expressions, splat expressions, and repeating nested Azure resource configurations via `dynamic` blocks.
- 🔄 **[[14-3_terraform_azure_meta_arguments_lifecycle_and_functions|Module 14-3: Meta-Arguments, Lifecycle Control, Functions & Data Sources]]**
  * Resource looping (`count` vs `for_each`), explicit dependency graphing (`depends_on`), lifecycle meta-arguments (`create_before_destroy`, `prevent_destroy`, `ignore_changes`), preconditions/postconditions, built-in function suite (string, collection, encoding, filesystem), and querying existing Azure infrastructure using `data` sources.

---

## 🛠️ Enterprise Hands-On Projects Portfolio

Hands-on enterprise projects and solution architecture walkthroughs implemented under `Projects/Azure_Terraform/`:

- 🚀 **[[../Projects/Azure_Terraform/Project-01_HA_Scalable_Infrastructure_VMSS|Project 01: High Availability & Scalable Infrastructure with VMSS & Auto-Scaling]]**
- 🚀 **[[../Projects/Azure_Terraform/Project-02_VNet_Architecture_and_Global_Peering|Project 02: Enterprise Virtual Network Topology & Global VNet Peering]]**
- 🚀 **[[../Projects/Azure_Terraform/Project-03_Entra_ID_Identity_Governance_and_SPN|Project 03: Microsoft Entra ID Authentication, Service Principals & RBAC as Code]]**
- 🚀 **[[../Projects/Azure_Terraform/Project-04_App_Service_Blue_Green_Deployment_Slots|Project 04: Azure App Service with Blue/Green Zero-Downtime Deployment Slots]]**
- 🚀 **[[../Projects/Azure_Terraform/Project-05_Serverless_Azure_Functions_Event_Driven|Project 05: Serverless Event-Driven Azure Functions (QR Code Generator)]]**
- 🚀 **[[../Projects/Azure_Terraform/Project-06_Terraform_Provisioners_and_Cloud_Init|Project 06: Terraform Provisioners vs. Native Cloud-Init & Custom Script Extensions]]**
- 🚀 **[[../Projects/Azure_Terraform/Project-07_Enterprise_Modular_AKS_Cluster|Project 07: Enterprise Modular Azure Kubernetes Service (AKS) & Key Vault]]**
- 🚀 **[[../Projects/Azure_Terraform/Project-08_Azure_Policy_and_Governance_as_Code|Project 08: Azure Policy as Code & Enterprise Compliance Enforcement]]**
- 🚀 **[[../Projects/Azure_Terraform/Project-09_Secure_Azure_SQL_Database_and_Firewall|Project 09: Hardened Azure SQL Database Server & Firewall Rules as Code]]**
- 🚀 **[[../Projects/Azure_Terraform/Project-10_Full_Stack_Monitoring_Log_Analytics_and_Alerts|Project 10: Full-Stack Observability with Log Analytics, Metric Alerts & Action Groups]]**
- 🚀 **[[../Projects/Azure_Terraform/Project-11_Terraform_Import_and_AzOps_Terrafy|Project 11: Terraform Import & Reverse Engineering Live Azure Clouds via aztfy]]**
- 🚀 **[[../Projects/Azure_Terraform/Project-12_HCP_Terraform_Cloud_Workspaces|Project 12: HCP Terraform Cloud Workspaces & Dynamic Workload Identity Federation]]**
- 🚀 **[[../Projects/Azure_Terraform/Project-13_Azure_DevOps_Enterprise_CICD_Pipeline|Project 13: Azure DevOps End-to-End Enterprise CI/CD Pipeline for Terraform]]**
- 🚀 **[[../Projects/Azure_Terraform/Project-14_Production_3_Tier_Architecture_on_Azure|Project 14: Resilient 3-Tier Enterprise Architecture on Azure (Web, App, DB)]]**
- 🚀 **[[../Projects/Azure_Terraform/Project-15_Enterprise_AKS_GitOps_with_ArgoCD|Project 15: End-to-End GitOps on Azure Kubernetes Service with ArgoCD]]**

---

## 🔗 Multi-Cloud Cross-References
* **AWS Terraform Track:** [[10-Index - Terraform on AWS|Terraform on AWS Reference MOC]]
* **Azure Core Architecture Track:** [[13-Index - Azure|Microsoft Azure Reference MOC]]
* **Kubernetes Infrastructure Track:** [[0-Index - Kubernetes|Kubernetes Reference MOC]]
