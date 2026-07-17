---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[AWS Disaster Recovery]]"
sub_type: core-concept
source_type: documentation
source_url: "https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-of-workloads-on-aws/disaster-recovery-of-workloads-on-aws.html"
author: "AWS Whitepaper"
course_title: "Disaster Recovery of Workloads on AWS"
against: []
tags:
  - aws/disaster-recovery
  - aws/dr
  - aws/deep-dive
---

# aws - Disaster Recovery Strategies

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[AWS Disaster Recovery]] > **Disaster Recovery Strategies**

---

## 📑 Disaster Recovery Metrics: RPO and RTO

*   **RPO (Recovery Point Objective):** The maximum acceptable amount of data loss measured in time (e.g. how many hours of transaction history can be lost since the last backup).
*   **RTO (Recovery Time Objective):** The maximum acceptable downtime duration allowed to restore the application back to service.

---

## 📑 Disaster Recovery Approaches

AWS offers four primary strategies for disaster recovery, balancing cost against speed of recovery:

1.  **Backup & Restore (High RTO/RPO, Lowest Cost):** Periodically backing up data and copying AMIs to a remote region. No infrastructure runs in the DR region until a disaster occurs.
2.  **Pilot Light (Moderate RTO/RPO, Low Cost):** Critical core data systems (like databases) are actively running and replicating in the DR region, while other resources (web servers) are shutdown or pre-configured as templates (AMIs), ready to spin up during failover.
3.  **Warm Standby (Low RTO/RPO, Moderate Cost):** A scaled-down but fully functional copy of the production environment is always running in the DR region. Scales up to full capacity during a failover.
4.  **Multi-Site Active-Active (Near-Zero RTO/RPO, Highest Cost):** Full, identical environments run concurrently in multiple regions. Traffic is dynamically routed to both regions (e.g. using Route 53 latency routing).

---

## 📑 High Availability vs. Fault Tolerance

*   **High Availability (HA):** Ensures the application remains accessible (e.g. by routing traffic around failed nodes using a Load Balancer). Performance may degrade.
*   **Fault Tolerance:** Guarantees zero downtime and zero performance degradation during hardware/component failure (requires fully redundant configurations).

*Read more in [[3-15_aws_disaster_recovery]] ([3-15_aws_disaster_recovery.md](file:///home/karim/Desktop/BrainDump/Reference%20Notes/3-15_aws_disaster_recovery.md))*
