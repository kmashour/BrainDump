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

# aws - AWS STS

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - Identity and Access Management]] > **AWS STS**

---

## 📑 AWS Security Token Service (STS) Mechanics

**AWS Security Token Service (STS)** is a global web service that enables you to request temporary, limited-privilege credentials for AWS Identity and Access Management (IAM) users or for users that you authenticate (federated users).

### Key Features & Execution Flow:
*   **API Calling:** Triggered by calling APIs such as `AssumeRole`, `AssumeRoleWithSAML`, or `GetSessionToken`.
*   **Returned Credentials:** Dynamically issues a set of temporary credentials consisting of:
    1.  **Access Key ID**
    2.  **Secret Access Key**
    3.  **Security/Session Token**
*   **Configurable Expiration:** Credentials are valid for a configured duration, ranging from **15 minutes up to 12 hours**. Once expired, the credentials cannot be used, and a new session must be initiated.
*   **Security Advantages:** Eliminates the need to distribute or embed long-term access keys. Ideal for cross-account access, federated access, and machine-to-machine integrations (e.g., EC2 Instance Profiles).

*Read more in [[Reference Notes/3-2_aws_iam.md#5. IAM Roles & AWS STS]]*
