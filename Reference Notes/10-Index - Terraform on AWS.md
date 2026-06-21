---
obsidianUIMode: preview
class: index-note
tier: reference-note
tags:
  - terraform/reference-index
  - obsidian/moc
---

# ⎈ Terraform on AWS Reference MOC

**Breadcrumbs:** [[--Index--|🏠 Index]] > **Terraform on AWS Reference MOC**

---

## 🏛️ Reference Modules & Frameworks

This index contains our Terraform Infrastructure as Code (IaC) on AWS study modules, starting from basic syntax and state structures to enterprise-grade GitOps, multi-tier HA architecture, and drift remediation.

- ⎈ **[Module 10-1: Terraform Foundations & State Management](10-1_terraform_foundations_and_state.md)**
  * IaC principles, core workflow (init/plan/apply/destroy), provider blocks, S3/DynamoDB remote state backend locking, and repository layouts.
- ⚙️ **[Module 10-2: Variables, Types & Expression Syntax](10-2_variables_types_and_expressions.md)**
  * Input, output, and local variables, type constraints (lists, maps, objects), conditional & splat expressions, dynamic blocks, built-in functions, and data source lookups.
- 🔄 **[Module 10-3: Meta-Arguments, Lifecycle Control & State Ops](10-3_meta_arguments_lifecycle_and_state.md)**
  * Count, depends_on, for_each looping, resource lifecycle rules (create_before_destroy, prevent_destroy), provisioners, terraform import, and HCP Terraform workspaces.
- 🔌 **[Module 10-4: Networking, Static Website Hosting & Security Mini-Projects](10-4_networking_website_and_security.md)**
  * AWS VPC Peering routes, S3 static site hosting with CloudFront CDN/SSL, and IAM user, group, and role permissions management.
- 📦 **[Module 10-5: Production Architecture: Modules, EKS & Serverless](10-5_modules_eks_and_serverless.md)**
  * Reusable custom module design, modular EKS cluster deployments with IRSA role federation, AWS Lambda image processors, and Blue-Green deployments with Beanstalk.
- 🚀 **[Module 10-6: Enterprise CI/CD, Observability, GitOps & Drift Remediation](10-6_cicd_gitops_observability_and_drift.md)**
  * Highly Available 3-tier architectures, GitHub Actions automation pipelines, ArgoCD GitOps reconciliation on Kubernetes EKS, CloudWatch dashboards, and automatic drift detection.

---

## 🛠️ Verification Projects
Hands-on playbooks and milestone projects:
- 🚀 **[Project: HA 3-Tier Architecture on AWS](../Projects/terraform/Project%20-%20HA%203-Tier%20Architecture%20on%20AWS.md)**
- 🚀 **[Project: EKS GitOps and ArgoCD](../Projects/terraform/Project%20-%20EKS%20GitOps%20and%20ArgoCD.md)**
- 🚀 **[Project: Terraform Automation and Drift Remediation](../Projects/terraform/Project%20-%20Terraform%20Automation%20and%20Drift%20Remediation.md)**

