---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Azure Cloud Architecture, Governance and Access Control Mechanics]]"
sub_type: mechanics
source_type: gemini-chat
author: "Antigravity Assistant"
course_title: "Azure Architecture & Administration (AZ-104)"
tags:
  - azure/governance
  - azure/rbac
  - azure/custom-roles
  - azure/deep-dive
  - status/completed
---

# Azure Custom RBAC Roles - Action Grammar, Additive NotActions Logic, and Least-Privilege Engineering

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Main Notes/Azure/Azure Cloud Architecture, Governance and Access Control Mechanics|Azure Cloud Architecture, Governance and Access Control Mechanics]] > **Azure Custom RBAC Roles - Action Grammar, Additive NotActions Logic, and Least-Privilege Engineering**

---

## 🎯 1. First Principles: The Danger of Coarse-Grained Roles

In traditional cloud operations, administrators frequently assign built-in broad roles such as **`Contributor`** or **`Virtual Machine Contributor`** to developers and operators. 

While convenient, built-in roles grant immense blast radius:
* A `Virtual Machine Contributor` can provision, reboot, deallocate, **and completely delete** virtual machines, virtual networks, and attached managed disks.
* If a night-shift technician or an automated CI/CD service principal only requires permissions to restart an unresponsive application server, granting deletion rights violates the core security tenet of **Least Privilege**.

When built-in roles are either too permissive or too restrictive, organizations engineer **Custom RBAC Roles** in Azure Resource Manager (ARM).

---

## ⚙️ 2. The Anatomy of ARM Operation Provider Grammar

Every operation in Azure is represented by a standardized REST API string following this namespace structure:

$$\text{\{Company\}}.\text{\{ResourceProvider\}}/\text{\{resourceType\}}/\text{\{action\}}[/subaction]$$

For example:
* `Microsoft.Compute/virtualMachines/read` ➔ Allows reading VM properties and status.
* `Microsoft.Compute/virtualMachines/start/action` ➔ Allows turning on a deallocated VM.
* `Microsoft.Compute/virtualMachines/restart/action` ➔ Allows rebooting the operating system.
* `Microsoft.Compute/virtualMachines/powerOff/action` ➔ Allows stopping the hypervisor.
* `Microsoft.Compute/virtualMachines/delete` ➔ Allows destroying the virtual machine resource.

Notice the suffix `/action`: Operations that execute an active control-plane command rather than simply updating resource metadata properties end with `/action`.

---

## ⚠️ 3. The Additive Evaluation Engine & The "NotActions" Trap

The most critical architectural concept for Azure RBAC—and one of the most heavily tested traps on the AZ-104 exam—is how ARM computes effective rights:

```text
+---------------------------------------------------------------------------------------------------+
|                              AZURE RBAC IS PURELY ADDITIVE                                        |
+---------------------------------------------------------------------------------------------------+
|  Grants = Actions - NotActions                                                                    |
+---------------------------------------------------------------------------------------------------+
|  1. "NotActions" is NOT an explicit Deny!                                                         |
|  2. "NotActions" only subtracts permissions from the "Actions" array of THAT SPECIFIC ROLE.       |
|  3. If another role grants the permission, the user CAN perform the action!                       |
+---------------------------------------------------------------------------------------------------+
```

### The Multi-Role Overlap Scenario (Why Deletions Still Happen)

Consider an enterprise engineer assigned two roles on the same Resource Group:

```text
[ User: Junior DevOps Engineer ]
       │
       ├── Assigned Role A (Custom "VM Operator - No Delete"):
       │   - Actions:    ["Microsoft.Compute/virtualMachines/*"]
       │   - NotActions: ["Microsoft.Compute/virtualMachines/delete"]
       │   (Intent: Prevent the engineer from deleting VMs)
       │
       └── Assigned Role B (Built-in "Contributor"):
           - Actions:    ["*"]
           - NotActions: []
           (Grants full administrative control)
```

**ARM Evaluation:**
1. Does Role A grant delete? No ($Actions - NotActions = \text{No delete}$).
2. Does Role B grant delete? **Yes** ($Actions = \text{All}$).
3. **Outcome:** ARM evaluates all assigned roles additively. The user **CAN delete the virtual machine**!

> [!IMPORTANT]
> To establish an un-bypassable barrier against resource deletion across all identities and roles, you must enforce a **Resource Lock (`CanNotDelete`)**, not rely on `NotActions`.

---

## 🏛️ 4. Concrete JSON Anatomy: The "VM Operator - No Delete" Role

When authoring a custom role in the Azure Portal GUI or via Azure CLI/Bicep, the definition maps to a declarative JSON contract:

```json
{
  "Name": "VM Operator - No Delete",
  "IsCustom": true,
  "Description": "Permits operational control of VMs (start, restart, stop) while strictly stripping deletion rights.",
  "Actions": [
    "Microsoft.Compute/virtualMachines/read",
    "Microsoft.Compute/virtualMachines/start/action",
    "Microsoft.Compute/virtualMachines/restart/action",
    "Microsoft.Compute/virtualMachines/powerOff/action",
    "Microsoft.Network/networkInterfaces/read",
    "Microsoft.Network/virtualNetworks/read"
  ],
  "NotActions": [],
  "DataActions": [],
  "NotDataActions": [],
  "AssignableScopes": [
    "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  ]
}
```

### Decoding the Core Properties:
1. **`Actions`:** The control-plane operations granted by this role. Notice that read permissions for network interfaces and virtual networks are included so operators can view the VM's private IP and topology in the Azure Portal.
2. **`DataActions`:** Grants access to the **data plane** inside the resource (e.g., reading a blob inside a storage account, querying rows inside a SQL database). Virtual machine start/stop commands operate at the control plane, so `DataActions` remains empty.
3. **`AssignableScopes`:** Specifies where this custom role can be assigned. It can be scoped to a **Management Group**, a **Subscription**, or a specific **Resource Group**.
