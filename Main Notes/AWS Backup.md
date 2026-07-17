---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[AWS Disaster Recovery]]"
  - "[[aws - EBS Snapshot]]"
against: []
reference_guides:
  - "[[Reference Notes/3-15_aws_disaster_recovery.md]]"
tags:
  - aws/backup
  - status/completed
---

# AWS Backup

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[AWS Disaster Recovery]] > **AWS Backup**

---

## 🎯 Purpose (Why it is used)
AWS Backup is a fully managed, centralized backup service designed to automate and consolidate data protection across multiple AWS services. It eliminates the need for custom scripting or manual scheduling to back up cloud resources.

---

## ⚙️ Functionality (What it is doing)
- **Centralized Management:** Provides a single dashboard to configure policies, monitor backup jobs, and prove compliance for audits.
- **Backup Plans:** Custom policy schedules defining frequency (e.g., daily), time windows, retention durations, and cold storage transitions.
- **Cross-Region and Cross-Account Backups:** Automatically replicates backups to other regions or AWS accounts to support robust disaster recovery.
- **Tag-Based Assignment:** Allocates resources to backup plans dynamically using tags (e.g., `Environment: Production`).
- **Vault Lock:** Enforces a WORM (Write Once Read Many) policy on a Backup Vault, preventing anyone (including the root account) from modifying or deleting backups.

---

## 🏛️ Architectural Context (How it fits in the architecture)
AWS Backup acts as an orchestrator across AWS storage and database services, including EBS, S3, RDS, Aurora, DynamoDB, EFS, FSx, and Storage Gateway. Backups are stored in secure Backup Vaults encrypted with KMS Customer Managed Keys.

---

## 🧩 Problem Solver (What problem it solves)
AWS Backup solves the problem of backup fragmentation and scripting risks. Without it, operations teams must maintain separate snapshot scripts for EBS, RDS, and EFS, making it difficult to verify backup completeness and expose resources to deletion during attacks.

---

## 🟢 Operational Impact (What will happen with it operating)
Backups are run systematically, and compliance metrics are tracked automatically. Backup retention policies reduce storage costs by transitioning old snapshots to cold tiers, and ransomware threats are mitigated using Vault Lock.

---

## 🔴 Failure Impact (What will happen without it)
Without AWS Backup, data protection defaults to fragmented, service-specific settings. A developer might spin up a database or volume without backups, leading to total data loss if that resource fails.

---

## 📂 Reference Guides
*   [[3-15_aws_disaster_recovery]] ([3-15_aws_disaster_recovery.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/3-15_aws_disaster_recovery.md))

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **AWS Backup**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
