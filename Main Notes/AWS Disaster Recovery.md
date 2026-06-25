---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[aws]]"
  - "[[aws - Disaster Recovery Strategies]]"
  - "[[AWS Elastic Disaster Recovery]]"
  - "[[AWS Database Migration Service]]"
  - "[[AWS Backup]]"
against: []
reference_guides:
  - "[[Reference Notes/3-15_aws_disaster_recovery.md]]"
tags:
  - aws/disaster-recovery
  - status/completed
---

# AWS Disaster Recovery

**Breadcrumbs:** [[0-Index|🏠 Index]] > Infrastructure > **AWS Disaster Recovery**

---

## 🎯 Purpose (Why it is used)
AWS Disaster Recovery is a suite of design patterns, best practices, and managed cloud services implemented to protect workloads from localized outages, physical disasters, security breaches, and hardware failures. It provides mechanisms to replicate infrastructure and data across geographic regions to ensure business continuity.

---

## ⚙️ Functionality (What it is doing)
- **RPO and RTO Orchestration:** Helps align technical infrastructure with business metrics like Recovery Point Objective (data age limit) and Recovery Time Objective (downtime duration limit).
- **Multi-Region Failovers:** Reroutes traffic dynamically via Route 53 during outages.
- **Spectrum of DR Strategies:** Offers strategies ranging from low-cost offline data recovery (Backup and Restore) to real-time multi-region deployments (Multi-Site Active-Active).

---

## 🏛️ Architectural Context (How it fits in the architecture)
Disaster recovery sits as a wrapper layer around all compute, storage, network, and database services. A typical multi-region DR design mirrors production databases, stores backup images in separate S3 buckets with cross-region replication, and uses global traffic managers (Route 53 or Global Accelerator) at the edge.

---

## 🧩 Problem Solver (What problem it solves)
It prevents catastrophic outages and irreversible data loss. Without disaster recovery planning, a regional network failure, cloud provider outage, or cyberattack can permanently delete enterprise datasets and keep services offline for days, resulting in massive financial and reputational damage.

---

## 🟢 Operational Impact (What will happen with it operating)
Workloads operate with high availability and resilience. Systems recover from failures automatically or with minimal manual intervention. Compliance standards are met via auditable recovery drills and secure data locks.

---

## 🔴 Failure Impact (What will happen without it)
Without disaster recovery, failures will lead to immediate downtime, data loss up to the last manually copied backup, and high recovery times (MTTR) as engineers manually reconstruct environments.

---

## 📂 Reference Guides
*   [[3-15_aws_disaster_recovery]] ([3-15_aws_disaster_recovery.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/3-15_aws_disaster_recovery.md))

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **AWS Disaster Recovery**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
