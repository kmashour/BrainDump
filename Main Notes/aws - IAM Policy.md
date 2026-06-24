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

# aws - IAM Policy

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - Identity and Access Management]] > **IAM Policy**

---

## 📑 IAM Policy JSON Structure & Evaluation Logic

An **IAM Policy** is a JSON document that defines permissions, specifying authorization rules for accessing AWS resources.

### Policy JSON Fields:
*   **Version:** Defines the policy language version (almost always `"2012-10-17"`).
*   **Statement:** The core block containing rules:
    *   **Sid (Statement ID):** An optional identifier for the statement.
    *   **Effect:** Either `"Allow"` or `"Deny"`.
    *   **Principal:** The entity (user, account, role) to which access is granted/denied (only used in resource-based policies).
    *   **Action:** List of API operations allowed or denied (e.g., `s3:GetObject`, `ec2:DescribeInstances`).
    *   **Resource:** The specific AWS resources (ARNs) scope of the statement.
    *   **Condition:** Optional rules governing when the policy is active (e.g., source IP, MFA status).

### Policy Classification:
1.  **AWS-Managed:** Standardized, predefined policies maintained by AWS.
2.  **Customer-Managed:** Custom, reusable policies defined by users in their accounts.
3.  **Inline:** Non-reusable policies attached directly to a single identity.

### Evaluation Decision Engine:
*   **Default Deny:** Requests are denied by default.
*   **Explicit Deny:** An explicit deny statement in *any* policy overrides all allow statements.
*   **Explicit Allow:** If no explicit deny exists, the request must have an explicit allow to succeed.

*Read more in [[Reference Notes/3-2_aws_iam.md#2. IAM Policies & Evaluation Logic]]*
