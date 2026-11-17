---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: identity
domains:
  - "azure"
related_concepts:
  - "[[Reference Notes/13-104-02_administer_identity.md]]"
  - "[[Reference Notes/13-104-03_administer_governance_and_compliance.md]]"
against: []
reference_guides:
  - "[[Reference Notes/13-104-02_administer_identity.md]]"
tags:
  - azure/identity
  - azure/entra-id
  - azure/workload-identity
  - azure/managed-identity
  - status/completed
---

# Microsoft Entra ID and Cloud Workload Identity

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Azure Identity > **Microsoft Entra ID and Cloud Workload Identity**

---

## 🎯 Purpose (Why it is used)

In legacy on-premises datacenters, application authentication relied upon hardcoded database passwords, plaintext configuration connection strings, and service accounts bound to Kerberos Key Distribution Centers within a physical network perimeter. When migrating to distributed cloud architectures, embedding static credentials inside source code, CI/CD pipelines, and configuration files creates an untenable attack surface—leading directly to credential leakage, key sprawl, and catastrophic data breaches.

**Microsoft Entra ID and Cloud Workload Identity** eliminate static secrets entirely from application infrastructure. By establishing cryptographically validated, automated, and ephemeral service identities directly in the cloud control plane, workloads authenticate seamlessly to target cloud services (such as Azure SQL, Azure Key Vault, Azure Storage, and the Azure Resource Manager REST API) without developers ever touching or rotating passwords.

---

## ⚙️ Functionality (What it is doing)

Microsoft Entra ID Workload Identity operates across three distinct operational patterns:

1. **System-Assigned Managed Identity (SAMI):** A dedicated 1:1 Service Principal generated directly in the tenant and coupled directly to the lifecycle of an individual Azure resource (e.g., Virtual Machine, App Service, Function App). Deleting the Azure resource automatically and immediately purges the identity from Entra ID.
2. **User-Assigned Managed Identity (UAMI):** An independent, ARM-managed first-class Azure resource (`Microsoft.ManagedIdentity/userAssignedIdentities`) provisioned inside a resource group with its own tags, locks, and lifecycle. It can be shared across heterogeneous fleet resources (1:N) and supports cross-cloud Workload Identity Federation (OIDC) without requiring client secrets.
3. **Application Registrations & Service Principals:** Global software blueprints (App Registrations) projected into local directory tenants as concrete security principals (Service Principals) to enable multi-tenant SaaS integration, API daemon authentication, and external non-Azure workload integration.
4. **Link-Local IMDS Token Vending:** Local compute instances retrieve JSON Web Tokens (JWTs) via host-internal REST calls to the Azure Instance Metadata Service (`169.254.169.254`), keeping authentication completely off public wires and isolated at the physical hypervisor layer.

---

## 🏛️ Architectural Context (How it fits in the architecture)

Microsoft Entra ID functions as the central **Identity Plane (AuthN)** for the entire Microsoft cloud ecosystem, strictly separated from the **Azure Resource Manager (ARM) Authorization Plane (AuthZ)**:

```text
+---------------------------------------------------------------------------------------------------+
|                        ENTRA ID CLOUD WORKLOAD IDENTITY ARCHITECTURE                              |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|  [ Azure Workload Compute (VM / App Service / AKS Pod) ]                                          |
|         │                                                                                         |
|         │  1. REST GET Request (Host-Internal Link-Local)                                         |
|         ▼                                                                                         |
|  [ Hypervisor vSwitch IMDS: 169.254.169.254 ]                                                     |
|         │                                                                                         |
|         │  2. Direct Platform Backchannel (Control Plane)                                         |
|         ▼                                                                                         |
|  [ Microsoft Entra ID (Identity Plane - AuthN) ]                                                   |
|         │                                                                                         |
|         ├── Validates Workload Identity (SAMI / UAMI Object ID)                                   |
|         └── Issues Signed OAuth 2.0 / OIDC Bearer Token (JWT)                                     |
|         │                                                                                         |
|         ▼  3. Token Returned to VM Memory                                                         |
|  [ Azure Workload Compute ]                                                                       |
|         │                                                                                         |
|         │  4. Data Plane Request with Bearer Token (VNet / Backbone / Private Link)               |
|         ▼                                                                                         |
|  [ Target Azure Resource (Azure SQL / Key Vault / Storage) ]                                      |
|         │                                                                                         |
|         └── Evaluates RBAC / Access Policy via ARM / Local Engine (Authorization Plane - AuthZ)   |
+---------------------------------------------------------------------------------------------------+
```

* **Separation of Identity from Access:** Entra ID proves *who the workload is* (Authentication) and issues a signed cryptographically unforgeable JWT. The receiving service independently verifies the JWT signature and enforces Azure RBAC or local access control to determine *what the workload can do* (Authorization).
* **Multi-Tenant SaaS Isolation:** Software applications maintain a single global Application ID across all customer tenants, while each customer tenant instantiates its own isolated Service Principal Object ID to anchor local RBAC role assignments.

---

## 🧩 Problem Solver (What problem it solves)

* **Eliminates Hardcoded Secrets & Credential Leakage:** Developers never embed client secrets, API tokens, or certificates in configuration files, environmental variables, or Git repositories.
* **Solves the "Secret Zero" Conundrum:** Traditional secret vaults (like HashiCorp Vault or Azure Key Vault) require an initial secret to authenticate. Managed Identity provides hardware-attested, host-level authentication, bootstrapping secure communication with zero initial secrets.
* **Automates Credential Rotation:** Entra ID manages, rotates, and refreshes backing platform certificates every 46 days automatically behind the scenes with zero downtime and zero maintenance overhead.
* **Prevents Multi-Tenant Tenant Bleed:** Strict separation of Application ID (Client ID) from Principal ID (Object ID) guarantees that permissions granted to an external SaaS application in one enterprise tenant never bleed into or affect another tenant.
* **Eliminates CI/CD Runner Secrets:** Workload Identity Federation enables external CI/CD pipelines (GitHub Actions, GitLab CI) to exchange short-lived OIDC tokens for Azure access tokens, eliminating permanent, long-lived client secrets.

---

## 🟢 Operational Impact (What will happen with it operating)

* Applications running on virtual machines, container apps, and Kubernetes pods acquire short-lived OAuth 2.0 bearer tokens dynamically through the local Azure Instance Metadata Service (IMDS).
* All authentication transactions are fully auditable within Entra ID Sign-in Logs and Azure Activity Logs, attributing every database query or key retrieval directly to an unambiguous Service Principal Object ID.
* Fleet-wide infrastructure automation scripts leverage User-Assigned Managed Identities with deterministic Azure Resource Manager (ARM) lifecycle management, tags, and locks.
* Security engineers define least-privilege RBAC role assignments at precise subscription, resource group, or resource scopes without creating long-lived secret management overhead.

---

## 🔴 Failure Impact (What will happen without it)

* **Credential Sprawl & Source Code Leaks:** Development teams fall back on API keys, connection strings, and client secrets, which inevitably leak into public GitHub repositories, container image layers, or build logs.
* **Catastrophic Secret Expiration Outages:** Expired client secrets in production services trigger widespread cascade outages when certificates or passwords lapse unmonitored at 2:00 AM.
* **Privilege Creep and Blast Radius Amplification:** Teams share broad, monolithic Service Principals across multiple applications to avoid credential management friction, granting excessive permissions that allow an attacker compromising one microservice to pivot across the entire cloud footprint.
* **Tenant Confusion Vulnerabilities:** Assigning Azure RBAC permissions to Application IDs instead of Object IDs breaks multi-tenant boundaries, potentially granting unauthorized foreign SaaS tenants administrative access over enterprise infrastructure.

---

## 🔍 Deeper Dive Notes
This table automatically indexes all detailed breakdowns, architectural evolutions, and deep dives associated with **Microsoft Entra ID and Cloud Workload Identity**:

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
FROM "Main Notes"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

### Core Architecture & Mechanics
- [[Main Notes/Azure Workload Identity - IMDS Host Interception vs Target Service Network Traversal.md|Azure Workload Identity: IMDS Host Interception vs Target Service Network Traversal]]
- [[Main Notes/Azure Workload Identity - RBAC Principal ID Invariants, Multi-Tenant SaaS Isolation, and UAMI OIDC Federation.md|Azure Workload Identity: RBAC Principal ID Invariants, Multi-Tenant SaaS Isolation, and UAMI OIDC Federation]]

*Related Reference Module:* [[Reference Notes/13-104-02_administer_identity.md|Module 13-104-02: Administer Identity]]
