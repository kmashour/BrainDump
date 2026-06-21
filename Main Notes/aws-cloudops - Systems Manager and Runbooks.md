---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Main Notes/aws-cloudops]]"
sub_type: core-concept
source_type: documentation
source_url: "https://docs.aws.amazon.com/systems-manager/"
author: "Andrew Brown"
course_title: "AWS Cloud Ops Engineer Associate"
tags:
  - aws/ssm
  - aws/deep-dive
---

# aws-cloudops - Systems Manager and Runbooks

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Main Notes/aws-cloudops]] > **Systems Manager and Runbooks**

---

## 📑 Systems Manager Core Operations

AWS Systems Manager (SSM) provides operational control over AWS and on-premises hybrid resources. Rather than logging into individual servers manually, SSM aggregates administration tasks into centralized dashboards.

### 1. Port Hardening: Session Manager vs SSH
Traditional server administration relies on SSH (Port 22) or RDP (Port 3389) open to the internet or a bastion host. This architecture introduces security risks (brute-force attacks, key management overhead, network exposure).

AWS Systems Manager Session Manager eliminates these risks:
*   **Port-Free Access:** The SSM Agent running inside the EC2 operating system establishes an outbound connection to the Systems Manager service endpoint via secure WebSocket tunnels. No inbound firewall rules (Port 22/3389) are required in security groups.
*   **Central Authentication:** IAM policies control access permissions rather than static SSH keys.
*   **Auditing:** Every keystroke and console output is logged and streamed directly to CloudWatch Logs or archived in a secure S3 bucket for compliance auditing.

### 2. Fleet Configuration (Run Command & Patch Manager)
*   **Run Command:** Executes scripts or runs pre-defined documents on thousands of EC2 instances simultaneously without needing interactive shell logins. It supports rate-limiting (concurrency control) and error thresholds to abort operations if failures occur.
*   **Patch Manager:** Automates the process of patching managed instances with security updates. It scans instances for missing patches based on predefined patch baselines (e.g., install all critical security updates within 7 days of release) and can execute auto-installation during maintenance windows.

### 3. Event-Driven Remediation (Automation Runbooks)
SSM Automation Runbooks (`AWS::SSM::Automation`) orchestrate multi-step cloud tasks (e.g. stopping instances, detaching volumes, running commands, verifying status).
*   **Trigger Chaining:** When a service failure is logged, an EventBridge rule catches the state change and launches the remediation runbook.
*   **Self-Healing:** If disk storage alarms fire, the runbook runs shell commands to compress logs or delete temp files automatically. If that fails, it can provision an EBS volume resize command, avoiding disk saturation.

*Read more in [[Reference Notes/11-2_incident_response_and_ssm]]*
