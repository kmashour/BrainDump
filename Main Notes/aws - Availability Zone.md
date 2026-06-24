---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[aws]]"
sub_type: core-concept
source_type: udemy
course_title: "AWS Certified Solutions Architect Associate"
tags:
  - aws/infrastructure
  - aws/deep-dive
---

# aws - Availability Zone

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > **Availability Zone**

---

## 📑 Availability Zone (AZ) Design & Resiliency

An Availability Zone (AZ) consists of one or more discrete, physical data centers located within an AWS Region. AZs are engineered to provide high availability and isolation from localized infrastructure failures.

### Key Characteristics:
*   **Redundant Engineering:** Each AZ has independent power feeds, backup generator cooling systems, and redundant network connectivity.
*   **Disaster Isolation:** AZs are physically separated from each other by meaningful physical distances (typically miles/kilometers) to insulate them from localized disasters (e.g., fires, floods, power outages).
*   **High-Speed Interconnection:** All AZs within a region are interconnected using ultra-low latency, high-bandwidth private fiber-optic networks.
*   **Multi-AZ Deployments:** Standard sizing is between 3 and 6 AZs per region (with a minimum of 3). Distributing applications across multiple AZs (Multi-AZ) is the fundamental architecture pattern for implementing high availability and automatic failover.

*Read more in [[Reference Notes/3-1_aws_global_infrastructure.md#3. AWS Physical Footprint & Edge Caching]]*
