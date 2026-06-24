---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[aws]]"
sub_type: core-concept
source_type: documentation
source_url: "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html"
author: "AWS Documentation"
course_title: "AWS Elastic Block Store & EFS Storage Guides"
against: []
tags:
  - aws/ebs
  - aws/efs
  - aws/storage
  - aws/deep-dive
---

# aws - EBS and EFS Storage

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > **EBS and EFS Storage**

---

## 📑 EBS and EFS Storage Overview

This core concept covers block storage options on Amazon EC2 including network-attached SAN drives, physically attached temporary host drives, regional network shared filesystems, and volume snapshots.

*   **Network Block Storage:** Scalable, persistent zonal network drives: [[aws - Amazon EBS]]
*   **Point-in-Time Backups:** Incremental S3-backed volume snapshots: [[aws - EBS Snapshot]]
*   **Local Ephemeral Drive:** High-speed physically attached host storage: [[aws - Instance Store]]
*   **Shared Network Filesystem:** Regional POSIX-compliant multi-AZ shared file storage: [[aws - Amazon EFS]]

*Read more in [[Reference Notes/3-5_aws_ebs_efs_storage.md|Module 3-5: AWS EBS & EFS Storage]]*

---

## 🔍 Deeper Dive Notes

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
