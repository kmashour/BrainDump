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

# aws - IAM User

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - Identity and Access Management]] > **IAM User**

---

## 📑 IAM User Definition & Attributes

An **IAM User** represents a single physical person or system application within your AWS account. It is a resource containing credentials and metadata used to interact directly with AWS APIs.

### Key Characteristics:
*   **1-to-1 Mapping:** Best practices dictate that an IAM user should correspond directly to a single physical individual. Credentials should never be shared.
*   **Authentication Mechanisms:**
    *   **Console Access:** Protected via custom/auto-generated passwords, optionally combined with Multi-Factor Authentication (MFA).
    *   **Programmatic Access:** Accomplished using Access Keys (Access Key ID and Secret Access Key) for CLI/SDK integration.
*   **Default State:** A newly created IAM user has no permissions (Implicit Deny). All access must be explicitly granted using policies.
*   **Group Membership:** IAM users can be assigned to multiple groups to inherit policies dynamically.

*Read more in [[Reference Notes/3-2_aws_iam.md#A. Root User vs. IAM Users & Groups]]*
