---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[aws]]"
  - "[[S3 Storage Classes]]"
  - "[[S3 Lifecycle Rules]]"
  - "[[S3 Encryption]]"
  - "[[S3 Object Lock]]"
against:
  - "[[aws - EBS and EFS Storage]]"
reference_guides:
  - "[[Reference Notes/3-6_aws_s3_storage.md]]"
tags:
  - aws/s3
  - status/completed
---

# Amazon S3

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **Amazon S3**

---

## 🎯 Purpose (Why it is used)
Amazon S3 (Simple Storage Service) provides industry-leading, highly durable (11 9s), and infinitely scalable object storage in the public cloud. It is designed to store and retrieve any amount of data from anywhere on the web, serving as the storage backbone for cloud backups, static assets, data lakes, and microservices integrations.

---

## ⚙️ Functionality (What it is doing)
- **Object-Based Storage:** Organizes data flatly inside regional buckets using uniquely identifiable key-value structures (Prefix + Object Name).
- **Multipart Uploading:** Parallelizes uploads for large files (mandatory >5 GB, recommended >100 MB) to maximize network bandwidth and improve upload resilience.
- **Access Points & Object Lambda:** Defines dedicated entry points for simplified security controls at scale and dynamically transforms objects (e.g., redacting PII, watermarking images) on the fly via AWS Lambda.
- **Event-Driven Architecture:** Triggers automated workflows (via SQS, SNS, Lambda, or EventBridge) in response to object creation, deletion, or replication.

---

## 🏛️ Architectural Context (How it fits in the architecture)
S3 is a global-namespace, regional-scoped storage fabric residing outside the customer VPC. While it cannot be mounted directly as a filesystem on EC2 (unlike EBS or EFS), instances and services access it via public HTTP/HTTPS API endpoints or VPC Gateway Endpoints to secure internal data flows.

---

## 🧩 Problem Solver (What problem it solves)
S3 eliminates the storage size limits, maintenance overhead, and high costs associated with traditional block-based or on-premises storage arrays. It solves data growth challenges by scaling capacity dynamically without provisioning disks, and guarantees data durability against multi-AZ infrastructure failures.

---

## 🟢 Operational Impact (What will happen with it operating)
Users can store petabytes of data securely, leveraging automatic replication (CRR/SRR) and access logging to meet compliance auditing requirements. Systems experience low-latency read performance (baseline limits of 5,500 GET requests/sec per prefix) and automated optimization via lifecycle rules.

---

## 🔴 Failure Impact (What will happen without it)
If S3 experiences a regional outage, client applications cannot download static assets (CSS, JS, images), backups and log exports will fail, and data lake pipelines will stall. Outages can cause downstream failures in decoupled systems dependent on S3 event notifications.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Amazon S3**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
