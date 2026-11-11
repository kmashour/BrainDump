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

This index contains our canonical Terraform Infrastructure as Code (IaC) on Microsoft Azure curriculum, synthesized directly from the 29-day production course inflow materials, HashiCorp architecture standards, and Microsoft Azure platform best practices. It bridges foundational HCL engine mechanics, atomic syntax rules, and state memory models directly into enterprise Azure solution architecture.

- ⎈ **[[14-1_terraform_azure_foundations_and_state|Module 14-1: Terraform Core Engine, AzureRM Provider & State Locking]]**
  * HCL block anatomy, arguments vs computed attributes, resource addressing & DAG dependency graphing, 5-phase CLI lifecycle (`init`, `validate`, `plan`, `apply`, `destroy`), execution plan symbols (`+`, `~`, `-`, `-/+`), `azurerm` provider anatomy, mandatory `features {}` block, version pinning operators (`~>`, `>=`, `=`), provider aliasing (`alias`), 5 Azure authentication models (Azure CLI, Service Principal with secret/cert, MSI, OIDC), state JSON schema (`serial`, `lineage`, `resources`), and native Azure Blob Lease concurrency locking (`x-ms-lease-action: acquire`, HTTP 412, `force-unlock`).
- ⚙️ **[[14-2_terraform_azure_variables_types_and_expressions|Module 14-2: Variables, Type Constraints, Dynamic Blocks & Expressions]]**
  * The Variable Trinity: Input Variables (with `regex`/`can` custom validation rules), Output Variables (with `sensitive = true`), and Local Values (`locals`). String templates & interpolation rules (the Golden Rule of Bare References vs. `${...}` interpolation, HCL1 vs. HCL2 history, escaping with `$${}`). 7-level variable precedence hierarchy. 4-tier type constraints: Primitives (`string`, `number`, `bool`), Collections (`list`, `set` [why sets cannot be indexed], `map`), Structural (`tuple`, `object`), and `optional(type, default)`. Expressions: inline ternary conditionals, `for` list/map comprehensions, splat `[*]` operators. Dynamic Blocks: the "Block Stamper" mental model, why `for_each` fails on nested blocks, automatic iterator naming (`<block_name>.value.<attribute>`), and custom iterators.
- 🔄 **[[14-3_terraform_azure_meta_arguments_lifecycle_and_functions|Module 14-3: Meta-Arguments, Lifecycle Control, Functions & Data Sources]]**
  * `count` vs. `for_each`: Complete mathematical breakdown of the Catastrophic Array-Shift Trap and why maps/sets (`toset()`) prevent unintended destruction. Explicit DAG forcing via `depends_on` (handling Azure RBAC propagation delays). Lifecycle meta-arguments: `prevent_destroy`, `create_before_destroy` (and the Azure Global Naming Clash Trap), `ignore_changes` (autoscale drift, Key Vault IP injections, ACR image tags), and `replace_triggered_by`. Built-in function suite: String, Collection, Filesystem, Encoding (`jsonencode`, `base64encode`), and Crypto. Data sources (`data "..."`): `azurerm_client_config` and querying platform Hub VNets/Subnets.
- 📦 **[[14-4_terraform_azure_modules_and_code_organization|Module 14-4: Modular Architecture, Code Organization & Reusable Modules]]**
  * Reusable child module engineering: standard triad (`main.tf`, `variables.tf`, `outputs.tf`, `versions.tf`), directory-per-environment (`dev/`, `staging/`, `prod/`) vs. Workspaces comparison. The **Provider Inversion Rule** (child modules must never declare `provider "azurerm" {}`). Output-to-Input passthrough chaining. Dynamic module looping with `for_each` (static key constraint). Passing custom providers via `providers = { azurerm = azurerm.alias }`. Module sourcing and semantic git version pinning (`?ref=vX.Y.Z`). Zero-downtime refactoring: declarative `moved {}` blocks vs. imperative `terraform state mv`.
- 🏛️ **[[14-5_terraform_azure_enterprise_infrastructure_patterns|Module 14-5: Enterprise Azure Infrastructure Patterns as Code]]**
  * Enterprise networking: Hub-and-Spoke topology, subnet delegation (`Microsoft.Web/serverFarms`), high-scale outbound egress via Azure NAT Gateway (64k SNAT ports), and asymmetric bidirectional VNet peering (`hub_to_spoke` and `spoke_to_hub` with `depends_on`). App Service Blue/Green deployment slots with sticky configuration. Provisioners anti-pattern vs. native Custom Script Extensions and Cloud-Init. Zero-Trust machine identity: User-Assigned Managed Identity and scoped RBAC. Azure Policy as Code (`azurerm_policy_definition` with `effect = "Deny"`). Hardened Azure SQL Server (public access disabled, AAD-only auth, Private Endpoints, Private DNS Zone links). Full-stack observability: Log Analytics workspaces, diagnostic settings, metric alerts, and action groups.
- 💾 **[[14-6_terraform_azure_state_operations_import_and_migration|Module 14-6: State Operations, Migration, import Blocks, aztfy & HCP Terraform]]**
  * The three planes of reality: Physical Reality vs. Desired Code vs. State Database. State CLI surgery suite (`state list`, `state show`, `state mv`, `state rm`, `state pull`, `state push`, `force-unlock`). The 3 ingestion methodologies: Method 1 (Native imperative `terraform import` & Modern declarative `import {}` blocks in v1.5+ with `-generate-config-out=generated.tf` and top-down Azure ingestion hierarchy); Method 2 (Microsoft `aztfy` / `aztfexport` interactive TUI and its 4 enterprise caveats); Method 3 (Google `terraformer`). HashiCorp Cloud Platform (HCP) Terraform multi-tenant architecture (Org -> Projects -> Workspaces), the 3 execution workflows (VCS-driven, CLI-driven via `cloud {}`, API-driven), environment vs. terraform variables, and seamless remote backend state migration (`terraform init -migrate-state`).
- 🐙 **[[14-7_terraform_azure_github_actions_cicd_automation|Module 14-7: Enterprise CI/CD, GitOps Automation, Azure DevOps & Argo CD]]**
  * The GitOps paradigm: Single source of truth, declarative state, and automated continuous reconciliation. Infrastructure branching strategies: short-lived feature branches (`feature/*`) vs. trunk-based deployment. Secretless cloud authentication using OpenID Connect (OIDC) & Workload Identity Federation: 5-step cryptographic handshake, Entra ID federated credentials, Subject claims (`sub: repo:org/repo:pull_request` vs. `ref:refs/heads/main`). Multi-stage delivery pipelines: Azure DevOps declarative YAML (`validate`, `DevDeploy`, `StagingDeploy`, and parameter-driven `destroy` pipelines) and GitHub Actions 2-stage workflow (speculative PR plan comments via `actions/github-script`, protected production apply on merge). Nightly automated drift detection cron pipelines (`terraform plan -detailed-exitcode`). Cloud-native GitOps on Azure Kubernetes Service (AKS) with Argo CD: AKS cluster provisioning, External Secrets Operator (ESO) integration with Key Vault, Argo CD Application CRD (`kind: Application`), self-healing drift reconciliation, and automated zero-downtime rolling upgrades.

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
