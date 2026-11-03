---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: cloud-governance
domains:
  - azure
  - cloud-architecture
  - governance
related_concepts: []
against: []
reference_guides:
  - "[[Reference Notes/13-104-02_administer_identity.md]]"
  - "[[Reference Notes/13-104-03_administer_governance_and_compliance.md]]"
  - "[[Reference Notes/13-2_azure_core_architecture_hierarchy_and_governance.md]]"
tags:
  - azure/governance
  - azure/rbac
  - azure/locks
  - azure/identity
  - status/completed
---

# Azure Cloud Architecture, Governance and Access Control Mechanics

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Azure Architecture > **Azure Cloud Architecture, Governance and Access Control Mechanics**

---

## 🎯 Purpose (Why it is used)

In enterprise cloud environments, cloud infrastructure operates across multiple organizational tiers—from overarching identity directories down to individual storage accounts and virtual machines. Operating at scale requires strict governance, resource lifecycle protection, and granular access boundaries. Without robust control-plane enforcement, organizational drift, runaway spending, and catastrophic accidental deletions can compromise entire production platforms.

---

## ⚙️ Functionality (What it is doing)

Azure mediates all operations through two distinct operational planes:

1. **The Identity Plane (Microsoft Entra ID):** Governs authentication, directory objects (users, groups, service principals), licenses, and directory roles (such as Global Administrator).
2. **The Resource Plane (Azure Resource Manager - ARM):** Governs physical and logical cloud infrastructure (Management Groups, Subscriptions, Resource Groups, and Resources) using Azure Role-Based Access Control (RBAC), Azure Policy, and Resource Locks.

```text
+---------------------------------------------------------------------------------------------------+
|                                 AZURE DUAL-PLANE ARCHITECTURE                                     |
+---------------------------------------------------------------------------------------------------+
|  ENTRA ID (Identity Plane)                  |  AZURE RESOURCE MANAGER (Resource Plane: ARM)       |
+---------------------------------------------+-----------------------------------------------------+
|  - Root Identity: Tenant Root               |  - Hierarchy: Management Groups -> Subscriptions    |
|  - Top Role: Global Administrator           |  - Top Role: Owner                                  |
|  - Scope: Users, Groups, Enterprise Apps    |  - Scope: Resource Groups, VMs, Networks, Storage   |
|  - Enforcement: OAuth2 / OpenID Connect     |  - Enforcement: ARM REST API Gateways & RBAC        |
+---------------------------------------------------------------------------------------------------+
```

---

## 📚 Deeper Dive Notes in this Domain

* [[Main Notes/Azure/Azure Resource Locks - Control Plane Enforcement, RBAC NotActions Additive Logic, and Privilege Plane Isolation|🔒 Azure Resource Locks: Control Plane Enforcement, RBAC NotActions Additive Logic, and Privilege Plane Isolation]]
* [[Main Notes/Azure/Azure Custom RBAC Roles - Action Grammar, Additive NotActions Logic, and Least-Privilege Engineering|👤 Azure Custom RBAC Roles: Action Grammar, Additive NotActions Logic, and Least-Privilege Engineering]]
* [[Main Notes/Azure/Azure Policy - Pre-Flight Evaluation, Deny Guardrails, and Management Hierarchy Inheritance|📜 Azure Policy: Pre-Flight Evaluation, Deny Guardrails, and Management Hierarchy Inheritance]]

---

## 🔗 Reference Notes Integration
* [[Reference Notes/13-104-01_course_introduction_and_certification|Module 01: Course Introduction & Certification]]
* [[Reference Notes/13-104-02_administer_identity|Module 02: Administer Identity]]
* [[Reference Notes/13-104-03_administer_governance_and_compliance|Module 03: Administer Governance & Compliance]]
* [[Reference Notes/13-2_azure_core_architecture_hierarchy_and_governance|Azure Core Architecture, Hierarchy & Governance]]
