---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[AWS Disaster Recovery]]"
against: []
reference_guides:
  - "[[Reference Notes/3-15_aws_disaster_recovery.md]]"
tags:
  - aws/drs
  - status/completed
---

# AWS Elastic Disaster Recovery

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[AWS Disaster Recovery]] > **AWS Elastic Disaster Recovery**

---

## 🎯 Purpose (Why it is used)
AWS Elastic Disaster Recovery (DRS) is the recommended service for disaster recovery to AWS. It minimizes downtime and data loss by enabling fast, reliable recovery of physical, virtual, and cloud-based servers into AWS.

---

## ⚙️ Functionality (What it is doing)
- **Continuous Block-Level Replication:** Copies source disks continuously over secure channels, capturing active writes without degrading OS performance.
- **Low-Cost Staging Area:** Replicates data into a staging environment consisting of small EC2 instances and low-cost EBS volumes.
- **Automated Recovery Provisioning:** Spins up production-grade EC2 instances and high-performance EBS volumes matching source configurations during failover within minutes.
- **Failback Orchestration:** Synchronizes changes back to the source server once the primary data center recovers.

---

## 🏛️ Architectural Context (How it fits in the architecture)
AWS DRS uses a lightweight Replication Agent installed on source servers (on-premises VMs or EC2 instances in a different region). The agents send block-level writes to a staging VPC in AWS. During failover, instances are launched in the production target subnets of the target VPC.

---

## 🧩 Problem Solver (What problem it solves)
DRS solves the problem of high infrastructure costs and complex restore times associated with traditional active-passive standby environments. By using a staging area, it avoids paying for fully provisioned compute instances until an actual failover is declared.

---

## 🟢 Operational Impact (What will happen with it operating)
Critical servers are protected with sub-minute RPOs and low RTOs. DRS simplifies operational readiness through non-disruptive recovery drills and automated failback configurations.

---

## 🔴 Failure Impact (What will happen without it)
Without DRS, administrators must manage custom replication scripts, build identical secondary active environments at full cost, or accept high RTOs associated with restoring from cold database backups.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **AWS Elastic Disaster Recovery**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
