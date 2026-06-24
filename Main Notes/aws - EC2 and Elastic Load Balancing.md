---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[aws]]"
sub_type: core-concept
source_type: udemy
course_title: "AWS Certified Solutions Architect Associate"
against: []
tags:
  - aws/compute
  - aws/deep-dive
---

# aws - EC2 and Elastic Load Balancing

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > **EC2 and Elastic Load Balancing**

---

## 📑 EC2 and Elastic Load Balancing (ELB) Overview

This core concept covers Amazon EC2 compute instances, configuration images (AMIs), routing topologies (Placement Groups), secure metadata services (IMDS), dynamic load balancing across target groups (ELB), and elastic resource scaling (ASG).

*   **Virtual Compute:** Renting scalable servers with administrative control: [[aws - EC2 Instance]]
*   **Virtual Machine Blueprints:** Creating pre-configured templates for deployment: [[aws - AMI]]
*   **Placement Topologies:** Influencing location on hardware racks: [[aws - Placement Group]]
*   **Instance Metadata:** Querying configuration details securely: [[aws - IMDS]]

*Read more in [[Reference Notes/3-4_aws_ec2_compute.md|Module 3-4: AWS EC2 Compute]] and [[Reference Notes/3-10_aws_elb_load_balancing.md|Module 3-10: AWS Elastic Load Balancing]]*

---

## 🔍 Deeper Dive Notes

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
