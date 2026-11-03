---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Azure Resource Governance and Access Control]]"
sub_type: architecture
source_type: gemini-chat
source_url: ""
author: "Antigravity"
course_title: "AZ-104 Masterclass"
tags:
  - azure/governance
  - azure/locks
  - azure/rbac
  - azure/deep-dive
  - status/completed
---

# Azure Resource Governance - Control Plane Locks, RBAC NotActions Additive Logic, and Privilege Plane Isolation

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Azure Resource Governance and Access Control]] > **Control Plane Locks & Privilege Isolation**

---

## 🎯 1. First Principles: The Need for Absolute Safety Latches

In enterprise cloud operations, operations teams frequently run cleanup scripts, automated CI/CD pipelines, and bulk resource teardowns. When engineers possess broad permissions (such as `Contributor` or `Owner`), a single typing error (e.g., executing `az group delete` against a production resource group instead of a test sandbox) can instantly destroy mission-critical databases, virtual networks, and storage accounts.

To safeguard infrastructure, Microsoft Azure implements three distinct layers of access and lifecycle governance:
1. **Identity Boundaries:** Microsoft Entra ID vs. Azure Resource Manager (ARM).
2. **Permission Grants:** Role-Based Access Control (RBAC) with additive action evaluation.
3. **Control-Plane Interception:** Resource Locks (`CanNotDelete` and `ReadOnly`).

---

## 🏛️ 2. The Two Separate Universes: Entra ID vs. Azure RBAC

A fundamental architectural principle of Azure is the complete separation between the **Identity Plane** and the **Resource Plane (ARM)**:

```text
+---------------------------------------------------------------------------------------------------+
| ENTRA ID (Identity Plane)                   | AZURE RBAC (Resource Plane: ARM)                     |
+---------------------------------------------+-----------------------------------------------------+
| Top Role: Global Administrator              | Top Role: Owner                                     |
| Scope: Users, Groups, Passwords, Domains    | Scope: Management Groups, Subscriptions, RGs, VM/DB |
| Authority: Directory Object Management      | Authority: Cloud Infrastructure Deployment & Config |
+---------------------------------------------------------------------------------------------------+
```

### Can a Global Administrator Touch Azure Resources by Default?
* **No.** By design, a **Global Administrator** has absolute authority over identity objects in Entra ID, but has **zero access** to Azure Subscriptions, Resource Groups, or Virtual Machines.
* If a Global Administrator logs into a subscription where they have not been explicitly assigned an Azure RBAC role, they cannot read, create, or delete resources.

### The Emergency Elevation Mechanism
A Global Administrator can only access Azure subscriptions by deliberately toggling an administrative switch:
1. In Entra ID properties, they enable **"Access management for Azure resources"**.
2. This temporarily elevates their account to the **User Access Administrator** role at the **Tenant Root Management Group** level.
3. Only after this explicit elevation can they assign RBAC roles or manage locks across the underlying subscriptions.

---

## ⚠️ 3. The "NotActions is a Deny" Trap (Additive RBAC Evaluation)

A common misconception among systems administrators is believing that specifying an action under `NotActions` creates a security Deny.

### The Mathematical Reality of RBAC
Azure RBAC is **strictly additive**. A role definition calculates permissions using basic set subtraction:

$$\text{Role Grants} = \text{Actions} - \text{NotActions}$$

* `Actions` specifies what permissions the role makes available.
* `NotActions` merely **subtracts** permissions from the `Actions` array of that specific role definition.
* **`NotActions` is NOT a Deny rule.** It simply means: *"This specific role does not grant this operation."*

```text
SCENARIO: Contractor assigned two roles on the same Resource Group:
-----------------------------------------------------------------------------------------
Role 1 (Custom Role): Actions: ["Microsoft.Compute/*"], NotActions: ["Microsoft.Compute/*/delete"]
Role 2 (Built-in Contributor): Grants full create/read/update/delete across all resources.
-----------------------------------------------------------------------------------------
EVALUATION:
- Role 1 does not grant delete.
- Role 2 explicitly grants delete.
- RESULT: The contractor CAN successfully delete the production virtual machine!
```

Because RBAC is purely additive, assigning a custom role with `NotActions` cannot prevent deletion if any other assigned role grants that permission.

---

## 🔒 4. Resource Locks: The Ultimate Control-Plane Enforcer

To enforce an absolute, non-bypassable barrier against deletion or modification, Azure provides **Resource Locks**.

### Does a Lock Apply to Global Admins and Subscription Owners?
* **YES, 100%.**
* Resource Locks operate directly at the Azure Resource Manager (ARM) REST API gateway.
* When a delete call reaches ARM, the lock engine intercepts the request **before checking user RBAC privileges**.
* If a `CanNotDelete` lock exists on the resource or any of its parent scopes (Resource Group or Subscription), ARM rejects the request immediately:
  ```text
  Status 409 Conflict: ScopeLocked
  The resource 'rg-production-core' cannot be deleted because it is locked by 'lock-prevent-deletion'.
  ```
* Even a **Subscription Owner** or an elevated **Global Administrator** is blocked from deleting a locked resource.

---

## 🔑 5. Who Can Remove (Turn Off) a Resource Lock?

A Resource Lock is not an irreversible cryptographic lock; it is an administrative safety latch. To remove or delete a lock, an identity must hold the explicit permission:

$$\text{Microsoft.Authorization/locks/*}$$

### Built-In Role Capability Matrix:

| Azure Role | Can Delete Resources? | Can Create/Modify Resources? | Can Remove a Resource Lock? |
| :--- | :---: | :---: | :---: |
| **Owner** | Yes | Yes | **YES** |
| **User Access Administrator** | No | No | **YES** |
| **Contributor** | Yes | Yes | ❌ **NO** *(Blocked)* |
| **Reader** | No | No | ❌ **NO** *(Blocked)* |

* **Notice the Contributor Restriction:** A `Contributor` can spin up 100 VMs, change configurations, and delete unlocked databases, but **cannot delete or alter a Resource Lock**.
* This makes Resource Locks the ideal mechanism for Lead Architects to protect infrastructure against accidental deletion by day-to-day developers and contributors.

---

## 🛡️ 6. The "Speed-Bump" Philosophy vs. Multi-User Authorization (MUA)

### The Two-Step Speed Bump
Why can an `Owner` delete a lock?
* A Resource Lock acts like the **protective flip-cover over a missile launch button**.
* It stops scripts, automated pipelines, and hurried operators from destroying assets by accident.
* To destroy a locked production database, an Owner must consciously navigate to the **Locks** blade, delete the lock, confirm the action, and then proceed with deletion.

### Defense Against Rogue Owners: Multi-User Authorization (Resource Guard)
If an enterprise needs to stop even a rogue, disgruntled, or compromised Owner from deleting mission-critical backups or locked data vaults, Azure provides **Multi-User Authorization (MUA)** via **Azure Resource Guard**:
* Critical operations (such as deleting a lock or purging a recovery vault) require authorization from a **secondary administrator** residing in an independent Entra ID directory.
* No single user, regardless of their Owner privileges, can unilaterally bypass the protection.

---

*Read more in [[Reference Notes/13-104-03_administer_governance_and_compliance.md#3-resource-locks-preventing-accidental-deletion--tampering]]*
