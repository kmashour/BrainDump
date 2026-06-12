---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[virtual-machine]]"
against:
  - "[[infra/openstack]]"
reference_guides:
  - "[[Reference Notes/3-Index - AWS.md]]"
tags:
  - aws/component
  - status/completed
---

# aws

**Breadcrumbs:** [[0-Index|🏠 Index]] > Infrastructure > **aws**

---

## 🎯 Purpose (Why it is used)
Amazon Web Services (AWS) is a public cloud computing platform providing global, on-demand infrastructure resources (compute, database, storage, networking) over the internet with pay-as-you-go pricing.

---

## ⚙️ Functionality (What it is doing)
*   **Compute Provisioning:** Allocates virtual machines (EC2) dynamically.
*   **Global Storage Scaling:** Manages scalable object storage (S3), network volumes (EBS), and file systems (EFS).
*   **Isolated Networking:** Provisions virtual isolated private networks (VPCs) with subnets, route tables, and gateways.
*   **Database Management:** Operates relational (RDS) and NoSQL (DynamoDB) managed database solutions.

---

## 🏛️ Architectural Context (How it fits in the architecture)
AWS serves as the underlying physical and virtual hosting fabric for modern microservices and container orchestrators. E.g., Kubernetes clusters (EKS) consume AWS virtual hardware, VPC networks, and EBS CSI volume provisioners to back container workloads.

---

## 🔍 Deeper Dive Notes
```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
FROM "Main Notes"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), "aws")
SORT file.name ASC
```
