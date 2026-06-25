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
  - aws/object-lock
  - aws/deep-dive
---

# Amazon S3 - S3 Object Lock

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Amazon S3]] > **S3 Object Lock**

---

## 📑 S3 Object Lock & Glacier Vault Lock
Both options implement the **WORM (Write Once, Read Many)** data model to prevent files from being deleted or overwritten.

### 1. S3 Glacier Vault Lock
- Applied at the Glacier Vault level using a Vault Lock Policy.
- Once configured and locked, the policy **cannot be edited or deleted by anyone**, including the administrator or AWS support. Useful for strict compliance storage.

### 2. S3 Object Lock
- Configured at the S3 bucket level (requires versioning enabled).
- Allows locking specific object versions.
- **Retention Modes:**
  - **Compliance Mode:** Strict. The locked version cannot be deleted or overwritten by any user, including the root account. The retention period cannot be shortened.
  - **Governance Mode:** Lighter. Most users cannot delete the object version or alter settings, but users with the `s3:BypassGovernanceRetention` permission (and passing the header `x-amz-bypass-governance-retention: true`) can delete the object or shorten the lock period.
- **Legal Holds:**
  - Protects an object indefinitely.
  - Applied and removed using the `s3:PutObjectLegalHold` permission. Does not require a retention period; it stays active until explicitly removed.

*Read more in [[Reference Notes/3-6_aws_s3_storage.md#7-data-protection--worm-object-lock--vault-lock]]*
