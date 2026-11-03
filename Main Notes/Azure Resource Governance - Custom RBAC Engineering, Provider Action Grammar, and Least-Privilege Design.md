---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Azure Resource Governance and Access Control]]"
sub_type: mechanics
source_type: gemini-chat
source_url: ""
author: "Antigravity"
course_title: "AZ-104 Masterclass"
tags:
  - azure/governance
  - azure/rbac
  - azure/custom-roles
  - azure/deep-dive
  - status/completed
---

# Azure Resource Governance - Custom RBAC Engineering, Provider Action Grammar, and Least-Privilege Design

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Azure Resource Governance and Access Control]] > **Custom RBAC Engineering & Action Grammar**

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

## ⚖️ 3. Actions vs. DataActions (Management Plane vs. Data Plane)

Azure RBAC strictly decouples managing the container from managing the payload inside:

```text
+---------------------------------------------------------------------------------------------------+
| MANAGEMENT PLANE (Actions)                  | DATA PLANE (DataActions)                            |
+---------------------------------------------+-----------------------------------------------------+
| Controls the ARM Azure Resource             | Interacts with data residing INSIDE the resource    |
| - Microsoft.Storage/storageAccounts/read    | - Microsoft.Storage/storageAccounts/blobServices/   |
| - Microsoft.Compute/virtualMachines/start   |   containers/blobs/read (Read actual blob contents) |
| - Microsoft.KeyVault/vaults/write           | - Microsoft.KeyVault/vaults/secrets/getSecret/action|
+---------------------------------------------------------------------------------------------------+
```

When building compute-focused roles (like VM operators), permissions operate exclusively at the management plane (`Actions`), leaving `DataActions` empty.

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
2. **`NotActions`:** Explicitly empty. Rather than relying on the unreliable `NotActions` subtraction trap, least-privilege engineering builds the role by explicitly whitelisting only the necessary actions.
3. **`AssignableScopes`:** Specifies where this custom role can be assigned. It can be scoped to a **Management Group**, a **Subscription**, or a specific **Resource Group**.

---

*Read more in [[Reference Notes/13-104-03_administer_governance_and_compliance.md#2-role-based-access-control-rbac-internals--custom-roles]]*
