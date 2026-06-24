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

# aws - AWS Region

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > **AWS Region**

---

## 📑 AWS Region Architecture & Selection

An AWS Region is a physical, geographically isolated location in the world where AWS clusters multiple, redundant data centers (grouped into Availability Zones). 

### Key Characteristics:
*   **Logical Isolation:** Regions are completely independent of one another. Failure in one region is structurally designed not to cascade to any other region.
*   **Dedicated Backbone Routing:** All inter-region communications run over AWS's private, high-capacity fiber-optic network infrastructure rather than the public internet.
*   **Resource Scope:** Most AWS resources (e.g., EC2 instances, EBS volumes, VPC subnets) are constrained to the selected region and are not visible in other regions.

### Region Selection Criteria:
1. **Compliance and Data Sovereignty:** Ensuring compliance with regional/national regulations governing data residency (e.g., EU GDPR or French data sovereignty requiring the use of Europe (Paris) `eu-west-3`).
2. **User Latency:** Deploying workloads in the geographic region closest to end-users to minimize network round-trip time.
3. **Service Availability:** Confirming via the AWS Region Table that the target region supports all required services and feature sets (as some regions do not launch with all services).
4. **Cost and Pricing:** Auditing pricing pages since service costs vary by region due to localized operational expenses, taxation, and power utility rates.

*Read more in [[Reference Notes/3-1_aws_global_infrastructure.md#3. AWS Physical Footprint & Edge Caching]]*
