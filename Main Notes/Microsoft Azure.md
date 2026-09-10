---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "azure"
  - "cloud"
related_concepts:
  - "[[Azure Resource Manager]]"
  - "[[Microsoft Entra ID]]"
  - "[[Azure Virtual Network]]"
  - "[[Azure Storage Account]]"
against:
  - "[[Amazon Web Services]]"
reference_guides:
  - "[[Reference Notes/13-Index - Azure.md]]"
  - "[[Reference Notes/13-1_azure_fundamentals_cloud_concepts_and_economics.md]]"
tags:
  - azure/cloud
  - status/completed
---

# Microsoft Azure

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Cloud Platforms > **Microsoft Azure**

---

## 🎯 Purpose (Why it is used)
**Microsoft Azure** is a global public cloud computing platform providing over 200 cloud services across Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS). It allows organizations to build, deploy, manage, and scale enterprise applications globally using an agile consumption-based operational model (OpEx) while maintaining compliance with international sovereignty regulations.

---

## ⚙️ Functionality (What it is doing)
1. **Global Physical Infrastructure:** Operates across 60+ geographical regions interconnected by Microsoft's private, low-latency global fiber network.
2. **Declarative Resource Management:** Provides a single, unified control plane (**Azure Resource Manager - ARM**) that guarantees identical authentication, RBAC authorization, and policy enforcement across all client tools (Portal, CLI, PowerShell, SDKs).
3. **Enterprise Identity Integration:** Natively couples with **Microsoft Entra ID** to deliver Zero Trust identity governance, Conditional Access, Single Sign-On (SSO), and hybrid Active Directory synchronization.

---

## 🏛️ Architectural Context (How it fits in the architecture)
- **Hierarchy:** Organizes resources through `Entra ID Tenant ➔ Root Management Group ➔ Management Groups ➔ Subscriptions ➔ Resource Groups ➔ Resources`.
- **Hybrid Reach:** Extends cloud governance and data services to on-premises datacenters, AWS, and GCP via **Azure Arc**.

---

## 🧩 Problem Solver (What problem it solves)
- Eliminates multi-million-dollar upfront hardware and datacenter capital expenditure (CapEx).
- Solves hardware procurement latency by provisioning compute, storage, and networking in seconds.
- Guarantees 99.99% high availability uptime SLAs through multi-zone redundancy.

---

## 🟢 Operational Impact (What will happen with it operating)
- Workloads scale horizontally and vertically on demand in response to real-time traffic metrics.
- Enterprise governance is automated across hundreds of subscriptions via Azure Policy initiatives.

---

## 🔴 Failure Impact (What will happen without it)
- Organizations remain burdened by physical server lifecycles, manual patching, cooling failures, and unscalable on-premises capacity limits.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Microsoft Azure**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
