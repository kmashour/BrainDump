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
  - azure/management-groups
  - azure/hierarchy
  - azure/deep-dive
  - status/completed
---

# Azure Resource Governance - Resource Hierarchy Topography, Management Group Nesting, and Scope Boundaries

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Azure Resource Governance and Access Control]] > **Resource Hierarchy Topography & Scope Boundaries**

---

## 🎯 1. First Principles: The "Folder vs. Account" Mental Model

A common architectural trap for cloud engineers is confusing the relationship between **Management Groups** and **Subscriptions**.

To eliminate ambiguity, Azure infrastructure adheres to a strict physical analog:
* **Management Groups are FOLDERS:** They possess no compute power, generate no direct bills, and store no data disks. They are purely logical administrative containers designed to organize subscriptions.
* **Subscriptions are BILLING ACCOUNTS / FILES:** They represent the contractual and financial agreement with Microsoft. All quotas, payment methods, and metered charges are anchored to the subscription.
* **The Rule of Direction:** You put subscriptions **INSIDE** management groups. A subscription can **NEVER** contain a management group.

```text
                     LEVEL 1: ROOT FOLDER
                    [ Tenant Root Group ]
                             │
                             ▼
                     LEVEL 2: ORGANIZATIONAL FOLDER
                  [ Enterprise Workloads ]
                             │
                             ▼
                     LEVEL 3: ENVIRONMENT FOLDER
                   [ Production Workloads ]
                             │
                             ▼
                     LEVEL 4: BILLING BOUNDARY (File)
                   [ Azure Subscription ]  <── Sits INSIDE a Management Group!
                             │
                             ▼
                     LEVEL 5: APPLICATION BOUNDARY
                    [ Resource Groups ]
                             │
                             ▼
                     LEVEL 6: WORKLOAD
                   [ Resources (VMs, DBs) ]
```

---

## 🏛️ 2. The Single-Parent Invariant & Multi-Subscription Scaling

Azure enforces strict structural laws across the Management Group hierarchy:

1. **The Single-Parent Rule:** Every Management Group and Subscription has exactly **one parent**. A subscription cannot belong to two management groups simultaneously.
2. **Hierarchy Depth Limits:** Management group trees support a maximum depth of **6 levels** beneath the Tenant Root Group.
3. **Capacity Limits:** A single Microsoft Entra ID tenant supports up to **10,000 Management Groups**.

### Free Accounts vs. Enterprise Multitenancy
* **On a Free / Single-Subscription Account:** An administrator can still construct an elaborate multi-tiered tree of management groups (e.g., `Platform`, `Workloads`, `Decommissioned`) at $0 cost. However, because only one subscription exists, that single subscription can only reside in **one** node of the tree at any given moment.
* **In Large Enterprises (50+ Subscriptions):** Rather than manually configuring 50 subscriptions, platform architects place 20 production subscriptions into `mg-workloads-prod`. A single Azure Policy or RBAC assignment applied at `mg-workloads-prod` automatically and instantaneously cascades to all 20 subscriptions.

---

## 🚫 3. The "No Upward Escalation" Rule in Assignable Scopes

When authoring **Custom RBAC Roles**, administrators frequently discover that the Tenant Root Group is greyed out or missing from the **Assignable scopes** picker:

```text
[ Tenant Root Group ]              ▲  ❌ CANNOT REACH UPWARDS!
         │                         │
[ Management Group ]               │
         │                         │
[ Subscription Scope ] ◄── YOU ARE HERE (Started role creation inside Subscription)
         │
[ Resource Group Scope ]           ▼  ✅ CAN REACH DOWNWARDS!
```

### Why ARM Blocks Upward Scope Selection:
1. **Context Scoping:** When the role creation wizard is launched from the **Subscription Access Control (IAM)** blade, the session execution context is bound to that subscription. ARM strictly forbids defining assignable scopes *above* the current authoring context.
2. **Permission Boundary (`roleDefinitions/write`):** Adding the Tenant Root Group requires that the identity holds `Microsoft.Authorization/roleDefinitions/write` at the **Tenant Root Group itself**. An `Owner` on a Subscription only has authorization *at that subscription and below*.

### The Resolution for Shared Enterprise Roles:
To make a custom role assignable across an entire management group hierarchy:
1. Navigate directly to **Management groups** in the Azure Portal.
2. Select the target Management Group (e.g., `Enterprise Workloads` or `Tenant Root Group`).
3. Open **Access control (IAM)** at that specific management group level and click **+ Add custom role**.

---

## 🔄 4. Moving Subscriptions Across the Topography

Subscriptions can be dynamically re-parented across management groups without disrupting running workloads:
* Moving a subscription from `mg-workloads-dev` to `mg-workloads-prod` is purely a control-plane re-binding.
* Virtual machines, databases, and networks experience **zero packet drops and zero downtime**.
* However, the subscription **immediately loses** policies inherited from the old parent and **immediately inherits** the policies, locks, and RBAC assignments enforced by the new parent.

---

*Read more in [[Reference Notes/13-104-03_administer_governance_and_compliance.md#1-management-groups-enterprise-governance-tree]]*
