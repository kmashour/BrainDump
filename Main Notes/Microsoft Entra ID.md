---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: security
domains:
  - "azure"
  - "identity"
related_concepts:
  - "[[Microsoft Azure]]"
  - "[[Azure Resource Manager]]"
against:
  - "[[Active Directory Domain Services]]"
reference_guides:
  - "[[Reference Notes/13-6_azure_identity_access_and_security_architecture.md]]"
tags:
  - azure/identity
  - azure/security
  - status/completed
---

# Microsoft Entra ID

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Identity & Security > **Microsoft Entra ID**

---

## 🎯 Purpose (Why it is used)
**Microsoft Entra ID** (formerly **Azure Active Directory / Azure AD**) is Microsoft's cloud-based Identity and Access Management (IAM) service. It serves as the enterprise identity boundary for authenticating users, services, and devices across Microsoft Azure subscriptions, Microsoft 365, third-party SaaS platforms, and on-premises hybrid environments.

---

## ⚙️ Functionality (What it is doing)
1. **Modern Authentication:** Issues and validates identity tokens using open web protocols (OAuth 2.0, OpenID Connect, SAML 2.0).
2. **Flat Object Directory:** Manages Users, Security Groups, Service Principals, and Managed Identities without traditional Active Directory complexities (no Organizational Units or Group Policies).
3. **Adaptive Conditional Access:** Analyzes real-time risk signals (user identity, IP location, device health, sign-in risk) to dynamically enforce MFA, restrict sessions, or block access.
4. **Hybrid Identity Sync:** Integrates with on-premises Active Directory Domain Services (AD DS) via Microsoft Entra Connect.

---

## 🏛️ Architectural Context (How it fits in the architecture)
- The Entra ID **Tenant** sits at the absolute apex of the Azure management tree.
- Subscriptions trust an Entra ID tenant to authenticate identities, while Azure RBAC governs what authenticated identities can perform inside subscriptions.

---

## 🧩 Problem Solver (What problem it solves)
- Eliminates fragmented, siloed user accounts across disparate cloud and SaaS applications.
- Enforces Zero Trust access controls before traffic reaches cloud workloads.

---

## 🟢 Operational Impact (What will happen with it operating)
- Users enjoy frictionless Single Sign-On (SSO) with Multi-Factor Authentication protection.
- Service-to-service communication is secured passwordlessly via Managed Identities.

---

## 🔴 Failure Impact (What will happen without it)
- Identity verification collapses; users and services cannot authenticate to Azure Portal, APIs, or SaaS applications.

---

## 🔍 Deeper Dive Notes
```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
