---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: security
domains:
  - "azure"
related_concepts:
  - "[[Reference Notes/13-104-02_administer_identity.md]]"
  - "[[Reference Notes/13-104-03_administer_governance_and_compliance.md]]"
  - "[[Reference Notes/13-2_azure_core_architecture_hierarchy_and_governance.md]]"
against: []
reference_guides:
  - "[[Reference Notes/13-104-03_administer_governance_and_compliance.md]]"
tags:
  - azure/governance
  - azure/rbac
  - azure/locks
  - azure/policy
  - status/completed
---

# Azure Resource Governance and Access Control

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Azure Governance > **Azure Resource Governance and Access Control**

---

## 🎯 Purpose (Why it is used)

In enterprise cloud computing, uncontrolled infrastructure deployment leads directly to billing shocks, compliance violations, and catastrophic operational outages. When engineering teams possess broad permissions without guardrails, accidental script executions or unauthorized deployments can destroy production databases or violate data sovereignty laws. 

Azure Resource Governance establishes an automated, multi-tiered framework of control-plane gates, least-privilege role definitions, and non-bypassable deletion safeguards. It ensures that organizational velocity is balanced with deterministic security boundaries across all subscriptions and workloads.

---

## ⚙️ Functionality (What it is doing)

Azure Resource Governance operates through four synchronized control-plane mechanisms:

1. **Management Group Hierarchy:** Enforces top-down organizational structures (`Tenant Root ➔ Enterprise Workloads ➔ Production Workloads`) that cascade policies, compliance rules, and access permissions across multiple subscriptions.
2. **Custom Role-Based Access Control (RBAC):** Tailors granular permission sets (`Actions` minus `NotActions`) that allow operations teams to start, stop, and maintain resources while strictly stripping destructive privileges.
3. **Resource Locks (`CanNotDelete` vs. `ReadOnly`):** Intercepts destructive and modifying operations directly at the Azure Resource Manager (ARM) REST API gateway, blocking all callers—including Subscription Owners and Global Admins.
4. **Azure Policy Enforcement:** Intercepts resource creation requests during pre-flight ARM validation, rejecting non-compliant configurations (e.g., unauthorized geographic regions, missing tags, or unencrypted storage).

---

## 🏛️ Architectural Context (How it fits in the architecture)

Azure separates authority across two distinct architectural planes: the **Identity Plane (Microsoft Entra ID)** and the **Resource Plane (Azure Resource Manager - ARM)**. 

Governance policies, RBAC role definitions, and locks are evaluated natively at the ARM gateway before requests ever touch underlying physical infrastructure:

```text
+---------------------------------------------------------------------------------------------------+
|                        AZURE GOVERNANCE & ACCESS CONTROL PIPELINE                                 |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|  Caller (User / CLI / Pipeline)                                                                   |
|         │                                                                                         |
|         ▼                                                                                         |
|  [ Microsoft Entra ID ] ──────────► Authenticates identity token (OAuth2 / OIDC)                  |
|         │                                                                                         |
|         ▼                                                                                         |
|  [ Azure Resource Manager (ARM) Gateway ]                                                         |
|         │                                                                                         |
|         ├──► 1. RBAC Evaluation: Does identity hold required operation?                           |
|         │       (Grants = Actions - NotActions)                                                   |
|         │                                                                                         |
|         ├──► 2. Resource Lock Check: Is target or parent scope locked?                            |
|         │       (CanNotDelete / ReadOnly blocks ARM DELETE / PUT)                                 |
|         │                                                                                         |
|         ├──► 3. Azure Policy Pre-Flight: Does resource comply with guardrails?                     |
|         │       (Deny / Audit / Modify evaluated before datacenter allocation)                    |
|         │                                                                                         |
|         ▼                                                                                         |
|    [ Physical Datacenter Fabric ] ──► (Provisioned, Mutated, or Stopped)                          |
+---------------------------------------------------------------------------------------------------+
```

---

## 🧩 Problem Solver (What problem it solves)

* **Eliminates Accidental Deletions:** Stops scripts, cleanup jobs, and hurried administrators from deleting production databases and virtual networks via `CanNotDelete` locks.
* **Prevents Privilege Creep:** Replaces broad `Contributor` roles with purpose-built custom roles that eliminate lateral movement and unauthorized resource destruction.
* **Guarantees Data Sovereignty & FinOps Guardrails:** Pre-flight Azure Policy prevents developers from deploying expensive workloads in unapproved geographic regions or spinning up prohibited VM sizes.
* **Decouples Identity from Infrastructure:** Enforces strict boundary isolation between Entra ID directory administration and Azure subscription resource management.

---

## 🟢 Operational Impact (What will happen with it operating)

* Operations teams perform required daily workflows (starting, stopping, rebooting, and monitoring workloads) without possessing permissions to destroy infrastructure.
* Compliant resource deployments through Terraform, ARM, Bicep, or the Azure Portal proceed transparently without delays.
* Destructive actions against critical workloads are physically halted by ARM, requiring an explicit, auditable two-step unlocking procedure by an authorized Owner.
* Compliance dashboards provide continuous, real-time posture reporting across all subscriptions.

---

## 🔴 Failure Impact (What will happen without it)

* **Catastrophic Outages via Script Errors:** An errant `az group delete` command in a CI/CD pipeline or terminal destroys core production resource groups in minutes.
* **The "NotActions is a Deny" Vulnerability:** Teams assume putting an action in `NotActions` protects resources, while overlapping `Contributor` role assignments quietly allow complete resource deletion.
* **Runaway Spend & Compliance Violations:** Developers inadvertently provision unapproved resources in overseas datacenters, violating regulations (GDPR, HIPAA) and exhausting cloud budgets.

---

## 🔍 Deeper Dive Notes
This table automatically indexes all detailed breakdowns, architectural evolutions, and deep dives associated with **Azure Resource Governance and Access Control**:

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
FROM "Main Notes"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

### Core Architecture & Mechanics
- [[Main Notes/Azure Resource Governance - Control Plane Locks, RBAC NotActions Additive Logic, and Privilege Plane Isolation.md|Azure Resource Governance: Control Plane Locks, RBAC NotActions Additive Logic, and Privilege Plane Isolation]]
- [[Main Notes/Azure Resource Governance - Custom RBAC Engineering, Provider Action Grammar, and Least-Privilege Design.md|Azure Resource Governance: Custom RBAC Engineering, Provider Action Grammar, and Least-Privilege Design]]
- [[Main Notes/Azure Resource Governance - Azure Policy Pre-Flight Evaluation, Deny Guardrails, and Management Hierarchy Inheritance.md|Azure Resource Governance: Azure Policy Pre-Flight Evaluation, Deny Guardrails, and Management Hierarchy Inheritance]]

*Related Reference Module:* [[Reference Notes/13-104-03_administer_governance_and_compliance.md|Module 13-104-03: Administer Governance and Compliance]]
