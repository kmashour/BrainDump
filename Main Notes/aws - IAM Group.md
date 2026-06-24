---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[aws - Identity and Access Management]]"
sub_type: core-concept
source_type: udemy
course_title: "AWS Certified Solutions Architect Associate"
tags:
  - aws/iam
  - aws/deep-dive
---

# aws - IAM Group

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - Identity and Access Management]] > **IAM Group**

---

## 📑 IAM Group Governance

An **IAM Group** is a logical collection of IAM users. It allows administrators to define permissions for multiple users at once, simplifying permission management at scale.

### Key Characteristics:
*   **Logical Container:** Groups contain users only. They cannot contain other groups (no support for nested groups).
*   **Dynamic Inheritance:** Users assigned to a group automatically inherit all permissions attached to that group. When a user is removed, they lose those permissions immediately.
*   **Non-Identity Status:** Groups are not security principals. They cannot be referenced as a `Principal` in resource-based policies (e.g., in an S3 Bucket policy); permissions must be applied to the users in the group.
*   **Best Practice:** Assign policies directly to groups and place users into those groups, rather than attaching policies directly to individual users.

*Read more in [[Reference Notes/3-2_aws_iam.md#A. Root User vs. IAM Users & Groups]]*
