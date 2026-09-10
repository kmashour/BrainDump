---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: storage
domains:
  - "azure"
  - "storage"
related_concepts:
  - "[[Microsoft Azure]]"
  - "[[Azure Resource Manager]]"
against:
  - "[[Classic Storage Account]]"
reference_guides:
  - "[[Reference Notes/13-5_azure_storage_services_redundancy_and_migration.md]]"
tags:
  - azure/storage
  - status/completed
---

# Azure Storage Account

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Storage > **Azure Storage Account**

---

## 🎯 Purpose (Why it is used)
An **Azure Storage Account** is a top-level administrative namespace in Azure that unifies four distinct cloud storage services—**Blob Storage (Objects), Azure Files (SMB/NFS), Azure Queues (Messaging), and Azure Tables (NoSQL)**—under a single management, billing, firewall, and encryption boundary.

---

## ⚙️ Functionality (What it is doing)
1. **Multi-Service Hosting:** Exposes specialized DNS endpoints for Blobs (`blob.core.windows.net`), Files (`file.core.windows.net`), Queues, and Tables.
2. **Access Tiering:** Optimizes object lifecycle costs across Hot, Cool, Cold, and Archive tiers.
3. **Configurable Redundancy:** Replicates data across local datacenters (LRS), Availability Zones (ZRS), or secondary paired regions (GRS/GZRS) providing up to 16 nines of durability.
4. **Data Protection:** Enforces encryption at rest with Microsoft-managed keys or customer-managed keys (CMK) in Azure Key Vault.

---

## 🏛️ Architectural Context (How it fits in the architecture)
- Deployed inside a Resource Group under an Azure Subscription.
- Can be accessed publicly via HTTPS, or restricted to private VNet subnets via Private Endpoints.

---

## 🧩 Problem Solver (What problem it solves)
- Solves the complexity of managing separate object, file, and queue storage platforms by consolidating them under one unified namespace.
- Prevents data loss during localized datacenter fires or regional catastrophes through automated zone and geo-redundancy.

---

## 🟢 Operational Impact (What will happen with it operating)
- Applications store petabytes of unstructured files, application logs, and shared file shares cost-effectively.

---

## 🔴 Failure Impact (What will happen without it)
- Cloud workloads lose access to persistent object storage, VM boot diagnostics, and shared SMB network drives.

---

## 🔍 Deeper Dive Notes
```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
