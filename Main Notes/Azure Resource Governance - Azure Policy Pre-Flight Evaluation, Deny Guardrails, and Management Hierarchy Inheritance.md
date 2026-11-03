---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Azure Resource Governance and Access Control]]"
sub_type: core-concept
source_type: gemini-chat
source_url: ""
author: "Antigravity"
course_title: "AZ-104 Masterclass"
tags:
  - azure/governance
  - azure/policy
  - azure/compliance
  - azure/deep-dive
  - status/completed
---

# Azure Resource Governance - Azure Policy Pre-Flight Evaluation, Deny Guardrails, and Management Hierarchy Inheritance

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Azure Resource Governance and Access Control]] > **Azure Policy Pre-Flight Evaluation & Inheritance**

---

## 🎯 1. First Principles: Why RBAC is Not Enough

A critical realization for enterprise cloud architects is understanding the boundary between **Identity Access (RBAC)** and **Resource Compliance (Azure Policy)**:

| Governance Layer | Question It Answers | Example Scenario |
| :--- | :--- | :--- |
| **Azure RBAC** | *"**WHO** is allowed to perform this operation?"* | *"Can Alice create a Storage Account in this resource group?"* ➔ Yes (Alice is a Contributor). |
| **Azure Policy** | *"**WHAT** resource configurations, parameters, and properties are allowed to exist?"* | *"Is Alice allowed to deploy that storage account in Australia, or with public HTTP access enabled?"* ➔ **NO!** |

Even if an engineer holds `Owner` or `Contributor` rights, RBAC does not enforce business compliance. An authorized engineer could deploy a $10,000/month GPU virtual machine in an unauthorized datacenter, violating both corporate data residency laws (e.g., GDPR, HIPAA) and FinOps budgets. 

**Azure Policy enforces real-time guardrails over resource properties regardless of who requests the deployment.**

---

## ⚡ 2. Pre-Flight ARM Interception Mechanics

When an administrator, a Terraform script, or a CI/CD pipeline deploys a resource to Azure, the request hits the **Azure Resource Manager (ARM)** REST API gateway.

Before any physical storage is allocated, hypervisor scheduled, or billable meter activated, the ARM request enters the **Pre-Flight Validation Pipeline**:

```text
  User / CLI / Terraform Request: Deploy Storage Account in 'West Europe'
                               │
                               ▼
        [ Azure Resource Manager (ARM) Gateway ]
                               │
              1. Authentication & RBAC Check
                 (Is user authorized to deploy? -> YES)
                               │
                               ▼
              2. Azure Policy Evaluation Engine  <── (PRE-FLIGHT GATE)
                 (Does resource match Allowed Locations: 'East US', 'West US'?)
                               │
                ┌──────────────┴──────────────┐
                ▼                             ▼
         [ MATCHES (US) ]             [ VIOLATION (West Europe) ]
                │                             │
                ▼                             ▼
       Proceeds to Physical        HTTP 400 / 403 Validation Failed!
       Datacenter Deployment       Deployment rejected instantly.
                                   Zero resources provisioned.
                                   Zero dollars billed.
```

When a policy with the **`Deny`** effect detects a non-compliant parameter during pre-flight, ARM immediately rejects the request. The deployment aborts with a descriptive violation message:
```text
RequestDisallowedByPolicy: Resource 'stpolicytest8291' was disallowed by policy 'enforce-us-regions-only'.
```

---

## 🎛️ 3. The Azure Policy Effect Spectrum

Azure Policy evaluates resources against conditional rules defined in JSON. Depending on the enterprise objective, a policy definition specifies an **Effect**:

| Policy Effect | Operational Behavior | Enterprise Use Case |
| :--- | :--- | :--- |
| **`Deny`** | Rejects the deployment request immediately during pre-flight validation. | Enforcing allowed geographic regions, banning insecure public IPs on database subnets. |
| **`Audit`** | Allows the resource deployment to succeed, but flags the resource as **Non-Compliant** in the central compliance dashboard. | Monitoring unencrypted storage accounts or VMs missing backup policies without breaking pipelines. |
| **`Modify`** | Automatically adds, updates, or overrides resource properties during creation or via remediation tasks. | Automatically inheriting tags from the parent resource group onto newly provisioned child resources. |
| **`Append`** | Appends required fields to the resource definition during creation. | Forcing HTTPS-only traffic or enforcing TLS 1.2 on storage accounts. |
| **`DeployIfNotExists`** | Deploys a secondary auxiliary resource if a condition is not met after the primary resource is provisioned. | Automatically deploying the Azure Monitor Agent (AMA) whenever a new Linux or Windows VM is spun up. |

---

## 🌳 4. Management Hierarchy Inheritance & Scoping

Azure Policy operates on a strict **Top-Down Cascading Inheritance** model across the enterprise hierarchy:

```text
[ Tenant Root Group ] ◄── Global Policies (e.g., Audit unencrypted disks)
         │
         ├── [ Core Platform Management Group ]
         │
         └── [ Enterprise Workloads Management Group ] ◄── Region Guardrail (Deny non-US)
                     │
                     ├── [ Production Workloads ] ◄── Automatically INHERITS Region Guardrail
                     │         │
                     │         └── [ Subscription: sub-prod-01 ] ◄── INHERITS Region Guardrail
                     │                   │
                     │                   └── [ Resource Group: rg-apps-prod ] ◄── INHERITS!
                     │
                     └── [ Non-Production Workloads ]
                               │
                               └── [ Subscription: sub-dev-01 ]
                                   (Can add explicit "notScopes" / Exclusions for test sandboxes)
```

### Key Scoping Rules for AZ-104:
1. **Inheritance Cannot Be Blocked:** A policy assigned at a parent scope (Management Group or Subscription) **cannot be disabled or overridden** at a child scope. It applies unconditionally to everything beneath it.
2. **Explicit Exclusions (`notScopes`):** If a specific resource group requires an exception (e.g., a development sandbox that needs to test multi-region latency), the administrator must configure an explicit **Exclusion** on the policy assignment at the parent level.
3. **Platform Cost:** Like Resource Locks and Management Groups, **Azure Policy is a built-in platform capability with $0.00 additional cost**.

---

*Read more in [[Reference Notes/13-104-03_administer_governance_and_compliance.md#4-azure-policy-declarative-guardrails--automated-remediation]]*
