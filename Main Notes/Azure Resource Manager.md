---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: control-plane
domains:
  - "azure"
related_concepts:
  - "[[Microsoft Azure]]"
  - "[[Microsoft Entra ID]]"
against:
  - "[[Azure Classic Deployment]]"
reference_guides:
  - "[[Reference Notes/13-2_azure_core_architecture_hierarchy_and_governance.md]]"
  - "[[Reference Notes/13-7_azure_management_monitoring_and_deployment_tooling.md]]"
tags:
  - azure/arm
  - azure/governance
  - status/completed
---

# Azure Resource Manager

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Control Plane > **Azure Resource Manager**

---

## 🎯 Purpose (Why it is used)
**Azure Resource Manager (ARM)** is the centralized deployment, management, and governance service for Microsoft Azure. It acts as the single management gateway that processes all incoming control plane API requests, providing consistent security, role-based access control (RBAC), tag attribution, and policy enforcement across the entire Azure cloud.

---

## ⚙️ Functionality (What it is doing)
1. **Unified API Gateway:** Terminates all requests from Azure Portal, Azure CLI (`az`), Azure PowerShell (`Az`), SDKs, and REST clients at a standardized endpoint.
2. **Declarative Orchestration:** Parses and executes declarative Infrastructure as Code manifests formatted as ARM JSON or **Bicep** templates.
3. **Idempotent Reconciliation:** Evaluates current environment state against desired template declarations, modifying only the deltas without redeploying unchanged resources.
4. **Access & Policy Gating:** Validates the caller's Entra ID identity, verifies Azure RBAC role permissions at the target scope, checks for Resource Locks, and evaluates Azure Policy rules prior to routing requests to the underlying Resource Provider (e.g. `Microsoft.Compute`).

---

## 🏛️ Architectural Context (How it fits in the architecture)
- Sits directly between client management tools and the individual Azure Resource Providers.
- Interacts continuously with Microsoft Entra ID for token validation and Azure Policy for guardrail enforcement.

---

## 🧩 Problem Solver (What problem it solves)
- Prevents configuration drift and inconsistent security enforcement across different operational tools.
- Solves resource lifecycle coupling by organizing interdependent resources into unified **Resource Groups**.

---

## 🟢 Operational Impact (What will happen with it operating)
- Deployments are fully repeatable, auditable, and automated through CI/CD pipelines.
- Accidental deletions of critical resources are blocked by ARM-enforced `CanNotDelete` and `ReadOnly` locks.

---

## 🔴 Failure Impact (What will happen without it)
- The entire Azure control plane becomes inaccessible; users cannot provision, resize, or delete resources (though existing data plane workloads continue executing).

---

## 🔍 Deeper Dive Notes
```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
