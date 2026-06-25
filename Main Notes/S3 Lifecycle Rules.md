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
  - aws/lifecycle-rules
  - aws/deep-dive
---

# Amazon S3 - S3 Lifecycle Rules

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Amazon S3]] > **S3 Lifecycle Rules**

---

## 📑 S3 Lifecycle Rules & Analytics
Amazon S3 Lifecycle rules allow users to automate object transitions and deletions to optimize storage costs over time.

### 1. Transition Actions
Transition actions define when objects should be moved to another storage class based on their creation age:
- **Example:** Moving Standard objects to Standard-IA after 30 days.
- **Example:** Moving Standard-IA objects to Glacier Flexible Retrieval after 90 days.

### 2. Expiration Actions
Expiration actions define when objects should be deleted automatically:
- **Object Expiration:** Deletes current object versions (e.g., access log files after 365 days).
- **Non-current Version Expiration:** Automatically deletes or archives old versions of files in version-enabled buckets.
- **Aborting Incomplete Multipart Uploads:** Cleans up incomplete multipart uploads after a specified number of days (e.g., 7 days) so you do not pay for abandoned storage chunks.

### 3. Rule Filters
Lifecycle policies are highly configurable and can be targeted using:
- **Entire Bucket:** Applies to all objects in the bucket.
- **Prefix Filters:** Applies only to objects matching a directory path prefix (e.g., `tmp/` or `backups/`).
- **Object Tag Filters:** Targets objects carrying specific key-value tags (e.g., `Department=Finance`).

### 4. S3 Storage Class Analysis
S3 Analytics scans access patterns of standard objects to provide data-driven recommendations on when to transition objects to Standard-IA.
- **Scope:** Recommendations only apply to S3 Standard and Standard-IA. It does not work with One Zone-IA or Glacier.
- **Output:** Generates a daily CSV report, taking 24 to 48 hours of initial monitoring before generating recommendations.

*Read more in [[Reference Notes/3-6_aws_s3_storage.md#b-lifecycle-policies]]*
