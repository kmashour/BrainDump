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
  - azure/identity
  - azure/entra-id
  - azure/rbac
  - azure/deep-dive
  - status/completed
---

# Azure Resource Governance - Entra Directory Roles vs Azure Role Assignments and Role-Assignable Group Invariants

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Azure Resource Governance and Access Control]] > **Entra Roles vs. Azure RBAC & Role-Assignable Groups**

---

## 🎯 1. First Principles: The Dual Role Taxonomy on User Profiles

When inspecting any identity in Microsoft Entra ID, administrators are presented with two distinct permission blades in the user navigation menu: **`Assigned roles`** and **`Azure role assignments`**.

These two blades represent completely separate operational planes with distinct scopes, APIs, and licensing requirements:

```text
USER PROFILE NAVIGATION (e.g., Sarah Jenkins)
          │
          ├──► [ Assigned roles ] ──────────────► MICROSOFT ENTRA ID DIRECTORY ROLES
          │                                       - Plane: Identity Plane
          │                                       - Examples: Global Administrator, User Administrator, Billing Admin
          │                                       - Target: Directory Objects (Users, Groups, Domains, Licenses)
          │                                       - Managed via: Microsoft Graph API
          │
          └──► [ Azure role assignments ] ──────► AZURE RBAC ROLE ASSIGNMENTS
                                                  - Plane: Resource Plane (Azure Resource Manager - ARM)
                                                  - Examples: Owner, Contributor, Reader, Custom Roles
                                                  - Target: Cloud Infrastructure (Management Groups, Subscriptions, RGs, VMs)
                                                  - Managed via: ARM REST APIs
```

---

## ⚖️ 2. Architectural Comparison Matrix

| Dimension | Microsoft Entra ID Roles (`Assigned roles`) | Azure RBAC Roles (`Azure role assignments`) |
| :--- | :--- | :--- |
| **Operational Plane** | **Identity Plane** (Tenant-wide) | **Resource Plane** (ARM hierarchy) |
| **Governed Entities** | Users, Groups, Enterprise Apps, Domains, Licenses, SSPR. | Management Groups, Subscriptions, Resource Groups, VMs, Storage, VNets. |
| **Top-Level Role** | **Global Administrator** | **Owner** |
| **Default Access** | Has **zero access** to Azure infrastructure resources by default. | Has full administrative control over assigned Azure subscriptions and resources. |
| **Elevation Path** | Can elevate to *User Access Administrator* at Root Management Group via the *"Access management for Azure resources"* toggle. | Cannot elevate to Entra ID directory administration. |
| **Group Assignment** | **Restricted:** Requires Entra ID P1/P2 and Role-Assignable Groups. | **Unrestricted:** Can be assigned to standard Security Groups for **free** on all subscription tiers. |

---

## 👥 3. Role-Assignable Groups Mechanics & Invariants

A critical distinction on the AZ-104 exam is how groups are granted permissions across both planes:

### 1. Azure RBAC to Groups: 100% Free and Native
* An administrator can assign any Azure RBAC role (e.g., `Reader`, `Contributor`, or custom roles) to standard security groups across subscriptions and resource groups at **$0.00 cost** on any subscription tier.

### 2. Entra ID Directory Roles to Groups: The "Role-Assignable" Requirement
* By default, Microsoft Entra ID **strictly forbids** assigning directory roles (like *User Administrator* or *Helpdesk Administrator*) to arbitrary security groups.
* In the **Entra ID Free tier**, directory roles can **ONLY be assigned directly to individual human user accounts**.

To assign a directory role to a group, the group must be explicitly created as a **Role-Assignable Group**:

```text
+---------------------------------------------------------------------------------------------------+
|                        THE ROLE-ASSIGNABLE GROUP INVARIANTS                                       |
+---------------------------------------------------------------------------------------------------+
| 1. Licensing Gate:                                                                                |
|    Requires a Microsoft Entra ID P1 or P2 license.                                                |
|                                                                                                   |
| 2. Creation-Time Immutability ("At Birth Only"):                                                  |
|    The setting "Microsoft Entra roles can be assigned to the group" (isAssignableToRole: true)   |
|    MUST be enabled during initial group creation.                                                 |
|    - A regular group CANNOT be converted into a role-assignable group later!                      |
|    - A role-assignable group CANNOT have this setting turned off later!                           |
|                                                                                                   |
| 3. Security Boundary Protection:                                                                  |
|    Only Global Administrators and Privileged Role Administrators can manage the membership        |
|    of role-assignable groups, preventing delegated admins from performing privilege escalation.   |
+---------------------------------------------------------------------------------------------------+
```

---

## 🔬 4. High-Yield AZ-104 Exam Scenarios

### Scenario A: Group Assignment Licensing Failure
* **The Question:** *"You have an Entra ID Free tenant. You create a security group named `grp-helpdesk` and attempt to assign the User Administrator directory role to it, but the role assignment is unavailable. Why?"*
* **The Answer:** Assigning Entra ID directory roles to groups requires **Role-Assignable Groups**, which is a premium feature requiring **Microsoft Entra ID P1 or P2**. On the Free tier, directory roles must be assigned directly to individual users.

### Scenario B: The Retroactive Toggle Trap
* **The Question:** *"You have an existing security group named `grp-cloud-ops` with 50 members. You now want to assign the Helpdesk Administrator role to this group. How should you proceed?"*
* **The Answer:** You **cannot** enable role assignment on an existing group. You must create a **new** security group with the toggle *"Microsoft Entra roles can be assigned to the group"* enabled at creation time, migrate the members, and assign the role.

---

*Read more in [[Reference Notes/13-104-02_administer_identity.md#3-microsoft-entra-id-roles-vs-azure-rbac-roles]]*
