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

# aws - IAM Role

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - Identity and Access Management]] > **IAM Role**

---

## 📑 IAM Role Architecture

An **IAM Role** is an IAM identity that you can create in your account that has specific permissions. It is similar to an IAM user, but it is not associated with a specific person. Instead of having permanent credentials, a role is designed to be assumed by anyone or anything that needs it (AWS services, federated users, etc.).

### Key Architecture Components:
*   **Trust Policy:** A resource-based policy that defines *which* principals are allowed to assume the role. This defines the trust boundary (e.g., allowing the EC2 service `ec2.amazonaws.com` or another AWS account to assume it).
*   **Permission Policy:** An identity-based policy attached to the role that defines *what* actions the assuming entity can take on which resources.
*   **Dynamic Credential Generation:** When an entity assumes a role, AWS Security Token Service (STS) dynamically generates temporary security credentials.
*   **Instance Profiles:** A container for an IAM role that you use to pass the role permissions to an EC2 instance. The EC2 instance retrieves credentials automatically from the Instance Metadata Service (IMDS).

### 🔄 Cross-Account Access: IAM Role vs. Resource-Based Policy
When delegating access across AWS accounts, operators can either use IAM Roles or Resource-Based Policies:
*   **IAM Roles (Trust Delegation):** The caller assumes a role in the target account via `sts:AssumeRole`. They temporarily **relinquish** their original account permissions and inherit the target role's permissions. (Ideal for administrative delegation).
*   **Resource-Based Policies (Direct Access):** The caller accesses the resource directly without assuming a role. They **keep** all their original permissions. (Ideal for data pipeline operations, e.g., scanning a DynamoDB table in Account A and writing the output directly to S3 in Account B).

*Read more in [[Reference Notes/3-2_aws_iam.md#5. IAM Roles & AWS STS]] and [[Reference Notes/3-2_aws_iam.md#9. Advanced IAM Security Mechanics]]*
