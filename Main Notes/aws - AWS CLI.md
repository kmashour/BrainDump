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

# aws - AWS CLI

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - Identity and Access Management]] > **AWS CLI**

---

## 📑 AWS Command Line Interface (CLI) Operation

The **AWS Command Line Interface (CLI)** is a unified, open-source command-line tool that enables operators to control and manage AWS services directly from their terminal using shell commands.

### Core Mechanics:
*   **API Interactivity:** Maps shell commands directly to public AWS service endpoints. The tool prefix is always `aws` (e.g., `aws ec2 describe-instances`).
*   **Underlying Engine:** Built on top of the **AWS SDK for Python (Boto3/Botocore)**.
*   **Authentication & Initialization:**
    *   Initiated by running `aws configure`, which creates configuration files under `~/.aws/credentials` and `~/.aws/config`.
    *   Requires four parameters: Access Key ID, Secret Access Key, Default AWS Region (e.g., `eu-west-1`), and Default Output Format (typically `json`).
*   **Security Best Practice:** Access keys configured on developer workstations should be strictly bound to specific users and rotated periodically. Inside AWS (e.g., on EC2), rely on **IAM Roles (Instance Profiles)** instead of configuring static CLI credentials.

*Read more in [[Reference Notes/3-2_aws_iam.md#4. Programmatic Access: CLI, SDK, and CloudShell]]*
