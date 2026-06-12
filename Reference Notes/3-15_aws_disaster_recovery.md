---
domains:
  - "aws"
  - "dr"
---

# Module 3-15: AWS Disaster Recovery

**Breadcrumbs:** [[3-Index - AWS|📐 AWS Index]] > **Module 3-15: AWS Disaster Recovery**

This module details disaster recovery architectures, Recovery Point Objectives (RPO), Recovery Time Objectives (RTO), and cross-region failover.

---

## ⏱️ RPO vs. RTO Metrics

Disaster recovery strategies are defined by two business metrics:
* **Recovery Point Objective (RPO):** The acceptable amount of data loss measured in time (e.g., losing 4 hours of transactions). Determines backup frequency.
* **Recovery Time Objective (RTO):** The acceptable downtime to restore services after a disaster. Determines system design.

```
Low Cost / High RTO & RPO                               High Cost / Low RTO & RPO
--------------------------------------------------------------------------------->
Backup & Restore (Hours) -> Pilot Light (Mins) -> Warm Standby (Secs) -> Multi-Site (Real-time)
```

---

## 🏛️ Disaster Recovery Strategies

### A. Backup & Restore (Lowest Cost / Slowest)
* **Mechanics:** Back up database snapshots and VM AMIs to S3. In a disaster, rebuild the infrastructure in a different region using CloudFormation and restore backups.

### B. Pilot Light
* **Mechanics:** Databases are running and replicated in real-time in the DR region. All application compute servers (EC2) are turned off. In a disaster, the EC2 instances are spun up (e.g., via Auto Scaling) and DNS routes traffic to the new region.

### C. Warm Standby
* **Mechanics:** A scaled-down version of the production environment is kept running in the DR region (e.g., 1 EC2 instance instead of 10). In a disaster, the environment is scaled up to handle the full load.

### D. Multi-Site Active-Active (Highest Cost / Fastest)
* **Mechanics:** Full, duplicate production environments run concurrently in two regions. User traffic is load-balanced globally (e.g., via Route 53 Latency or Geolocation policies). If one region fails, traffic routes to the healthy region.

---

## 🧠 Deep-Intuition (AARF) Breakdown: Pilot Light vs. Warm Standby Selection

1. **The Answer (Core Pattern):** Deploy a **Pilot Light** DR strategy for enterprise database workloads with an RPO of minutes and an RTO of under 30 minutes.
2. **The Assumptions (Context):** The primary and DR database replication must be active, and EC2 launch templates must be configured in the DR region.
3. **The Rationale (Why):** Pilot Light keeps compute costs minimal because EC2 instances are not running. The database replication ensures no data is lost (low RPO). Since launch templates exist, scaling up compute takes under 15 minutes, meeting RTO goals.
4. **The Failure Loop (What if not):** Operating a Warm Standby DR site for small workloads idle 99% of the time wastes budget on running unused EC2 instances.
5. **Alternative Case (When to use 'if not'):** For critical web APIs where even 5 minutes of downtime is unacceptable, deploy Active-Active Multi-Site.

![[../Attachments/Pasted image 20250516105714.png]]
![[../Attachments/Pasted image 20250516110610.png]]
![[../Attachments/Pasted image 20250516110618.png]]
![[../Attachments/Pasted image 20250516111402.png]]
