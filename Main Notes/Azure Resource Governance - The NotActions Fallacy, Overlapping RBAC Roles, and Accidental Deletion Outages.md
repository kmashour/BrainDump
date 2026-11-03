---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Azure Resource Governance and Access Control]]"
sub_type: pitfall
source_type: gemini-chat
source_url: ""
author: "Antigravity"
course_title: "AZ-104 Masterclass"
tags:
  - azure/governance
  - azure/rbac
  - azure/troubleshooting
  - azure/resource-locks
  - status/completed
---

# Azure Resource Governance - The NotActions Fallacy, Overlapping RBAC Roles, and Accidental Deletion Outages

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Azure Resource Governance and Access Control]] > **The NotActions Fallacy & Deletion Outages**

---

## 💥 Incident Forensics: The "NotActions is a Deny" Production Outage

In enterprise cloud security, one of the most dangerous and widespread operational pitfalls is treating Azure RBAC's `NotActions` as an explicit "Deny" rule. This architectural misunderstanding routinely results in accidental production deletions during automated maintenance or multi-role assignments.

---

## 🏛️ 1. The Architectural Setup & Engineering Assumptions

A financial enterprise contracts a third-party DevOps engineering team to manage and maintain its virtual machine infrastructure. 

To prevent accidental data loss:
1. The lead security architect creates a **Custom RBAC Role** named `VM Operations Specialist`:
   ```json
   {
     "Name": "VM Operations Specialist",
     "Actions": [
       "Microsoft.Compute/virtualMachines/*"
     ],
     "NotActions": [
       "Microsoft.Compute/virtualMachines/delete"
     ]
   }
   ```
2. **The Flawed Engineering Assumption:**
   The security team assumes that placing `Microsoft.Compute/virtualMachines/delete` inside `NotActions` establishes an explicit security block, guaranteeing that contractors can **never** delete a virtual machine under any circumstances.

---

## 💀 2. The Failure Loop Manifestation (Multi-Role Collision)

Two months later, a network performance degradation occurs in production resource group `rg-core-banking`:

```text
                                [ User: External Contractor ]
                                               │
               ┌───────────────────────────────┴───────────────────────────────┐
               ▼                                                               ▼
  Role 1: VM Operations Specialist                              Role 2: Virtual Machine Contributor
  (Assigned at Subscription Scope)                              (Assigned at Resource Group Scope)
  - Actions:    Microsoft.Compute/virtualMachines/*             - Actions:    Microsoft.Compute/*
  - NotActions: Microsoft.Compute/virtualMachines/delete        - NotActions: None
               │                                                               │
               └───────────────────────────────┬───────────────────────────────┘
                                               │
                                               ▼
                         Contractor executes cleanup script:
                           "az vm delete --name vm-banking-prod-01 --yes"
                                               │
                                               ▼
                              💥 DELETION PERMITTED BY ARM! 💥
                              Production VM and OS Disk destroyed!
```

### The Outage:
1. To troubleshoot the network degradation, a local branch admin temporarily grants the contractor the built-in **`Virtual Machine Contributor`** role on `rg-core-banking`.
2. The contractor runs an automated bash cleanup script to terminate idle staging machines.
3. Due to an environment variable misconfiguration, the script targets three production database nodes (`vm-banking-prod-01`, `vm-banking-prod-02`, `vm-banking-prod-03`).
4. **The Disaster:** Azure Resource Manager (ARM) immediately executes the deletion request. Three mission-critical production virtual machines are destroyed.
5. The incident response team is stunned: *"Why did Azure permit the deletion when the contractor's custom role explicitly contained NotActions for delete?"*

---

## 🔬 3. Root Cause Analysis (RCA): Additive Set Evaluation

The catastrophic failure occurred because of a fundamental misunderstanding of Azure RBAC mathematics:

### 1. `NotActions` is Subtraction, NOT a Deny
In Azure RBAC, `NotActions` does **NOT** mean "Deny this operation." It merely subtracts operations from the `Actions` array of that **specific role definition**:

$$\text{Effective Role Grants} = \text{Actions} - \text{NotActions}$$

`NotActions` simply prevents that specific role from granting the permission. It provides zero protection against permissions granted by other roles.

### 2. Multi-Role Authorization Evaluation
When a caller makes a REST API request to ARM, Azure evaluates all role assignments additively:

$$\text{Total Permissions} = \text{Grants}_{\text{Role 1}} \cup \text{Grants}_{\text{Role 2}} \cup \dots \cup \text{Grants}_{\text{Role } n}$$

* Role 1 (`VM Operations Specialist`) granted: Everything *except* delete.
* Role 2 (`Virtual Machine Contributor`) granted: Everything *including* delete.
* **The Union:** The caller possesses `Microsoft.Compute/virtualMachines/delete` via Role 2. ARM approves the deletion request.

---

## 🛡️ 4. Remediation & The Control-Plane Solution: Resource Locks

The only mechanism in Azure that creates an absolute, non-bypassable barrier against resource deletion across all identities and overlapping roles is an **Azure Resource Lock**.

```text
                              Incoming HTTP DELETE Request
                                           │
                                           ▼
                    [ Azure Resource Manager (ARM) Gateway ]
                                           │
                 ┌─────────────────────────┴─────────────────────────┐
                 │                                                   │
                 ▼                                                   ▼
       [ RBAC Authorization ]                             [ Resource Lock Engine ]
       - Checks Roles 1 & 2                               - Checks for "CanNotDelete" lock
       - Evaluates: Additive Grant                        - Found on: "rg-core-banking"
       - Result: ALLOW (Permitted)                        - Result: HARD BLOCK (HTTP 409)
                 │                                                   │
                 └─────────────────────────┬─────────────────────────┘
                                           │
                                           ▼
                             HTTP 409 Conflict: ScopeLocked
                             ARM drops packet immediately!
                             Zero infrastructure deleted!
```

### Portal GUI Remediation Procedure:
1. In the Azure Portal, navigate to the target Resource Group: **`rg-core-banking`**.
2. In the left navigation menu under **Settings**, select **Locks**.
3. Click **+ Add**:
   * **Lock name:** `lock-production-critical`
   * **Lock type:** Select **`Delete`** *(Maps to ARM `CanNotDelete`)*
   * **Notes:** `Blocks all destructive deletion requests across all assigned roles.`
4. Click **OK**.

### Architectural Guarantee:
With the `CanNotDelete` lock active, no identity—whether a Contractor, a Contributor, or even a **Subscription Owner**—can delete the resource. To delete, a privileged Owner must explicitly navigate to the Locks blade, remove the lock, and then perform the deletion.

---

*Read more in [[Reference Notes/13-104-03_administer_governance_and_compliance.md#3-resource-locks-preventing-accidental-deletion--tampering]]*
