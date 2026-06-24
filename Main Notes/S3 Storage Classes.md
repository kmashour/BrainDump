---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Amazon S3]]"
sub_type: core-concept
source_type: udemy
source_url: "https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/"
author: "Stephane Maarek"
course_title: "Ultimate AWS Certified Solutions Architect Associate"
tags:
  - aws/s3
  - aws/storage-classes
  - aws/deep-dive
---

# Amazon S3 - S3 Storage Classes

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Amazon S3]] > **S3 Storage Classes**

---

## 📑 S3 Storage Classes Overview
Amazon S3 offers a variety of storage classes tailored to different data access patterns, performance requirements, and cost budgets. All S3 storage classes (except One Zone-IA) replicate data across at least three Availability Zones (AZs) for high durability.

### 1. S3 Standard (General Purpose)
- **Use Case:** Active, frequently accessed data.
- **Details:** High-throughput, low-latency, and redundant across at least 3 AZs. No minimum storage duration or retrieval fees.

### 2. S3 Intelligent-Tiering
- **Use Case:** Data with unknown, unpredictable, or changing access patterns.
- **Details:** Automatically moves data between two access tiers (Frequent and Infrequent) based on usage. Incurs a small monthly monitoring and auto-tiering fee, but has **no retrieval charges**.

### 3. S3 Standard-Infrequent Access (Standard-IA)
- **Use Case:** Data accessed less frequently but requiring immediate access when needed (e.g., backups, disaster recovery).
- **Details:** Lower storage cost but charges a retrieval fee per GB. Has a **30-day minimum storage duration** and a 128 KB minimum billable object size.

### 4. S3 One Zone-Infrequent Access (One Zone-IA)
- **Use Case:** Non-critical backups or secondary copies of data that can be easily recreated.
- **Details:** Stores data in a **single Availability Zone** instead of three. Offers the same durability as Standard-IA but with 20% lower cost. If the AZ is destroyed, the data is lost. Has a **30-day minimum storage duration** and a 128 KB minimum billable object size.

### 5. S3 Glacier Tiers (Archive)
- **Glacier Instant Retrieval:** Milliseconds retrieval. Best for archives accessed once a quarter. Minimum storage of 90 days.
- **Glacier Flexible Retrieval:** Retrievable via three tiers: Expedited (1-5 mins), Standard (3-5 hrs), or Bulk (5-12 hrs, free). Minimum storage of 90 days.
- **Glacier Deep Archive:** The lowest cost storage option in AWS, designed for long-term compliance archiving. Retrieve standard in 12 hours, bulk in 48 hours. Minimum storage of 180 days.

### 6. S3 Express One Zone (Directory Buckets)
- **Use Case:** Extremely low-latency and high-performance applications (AI/ML training, financial simulations).
- **Details:** Stores data in a single AZ within custom **Directory Buckets**. Handles hundreds of thousands of requests per second with single-digit millisecond latency (10x faster than Standard).

*Read more in [[Reference Notes/3-6_aws_s3_storage.md#2-s3-storage-classes-lifecycle-transitions]]*
