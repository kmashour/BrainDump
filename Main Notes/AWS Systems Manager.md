---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[aws - EC2 Instance]]"
  - "[[SSM Parameter Store]]"
against:
  - "[[ansible]]"
reference_guides:
  - "[[Reference Notes/3-20_other_services_whitepapers.md]]"
tags:
  - aws/ssm
  - management/fleet
  - status/completed
---

# AWS Systems Manager

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **AWS Systems Manager**

---

## 🎯 Purpose (Why it is used)
AWS Systems Manager (SSM) is a secure management hub that provides visibility and control of your AWS infrastructure. By running the lightweight **SSM Agent** on managed nodes, it enables centralized configuration, patching, remote commands, and secure terminal shells on EC2 instances and on-premises servers.

---

## ⚙️ Functionality (What it is doing)
*   **SSM Agent Prerequisites:** Managed instances (EC2 or on-premises) must run the SSM Agent, have outbound endpoint connectivity, and use an IAM instance profile with the `AmazonSSMManagedInstanceCore` policy attached.
*   **SSM Session Manager:** Starts secure, keyless CLI shell sessions with port 22/3389 completely closed. Keystroke audits and session outputs are streamed directly to Amazon S3 or CloudWatch Logs.
*   **Run Command:** Remotely executes shell commands or SSM Documents (predefined script templates) across server resource groups without requiring SSH.
*   **Patch Manager:** Scans for and installs OS/security updates according to patch baselines, scheduled via Maintenance Windows.
*   **Automation Runbooks:** Executes multi-step workflows (remotely or automatically triggered by EventBridge alerts or AWS Config compliance remediations).

---

## 🏛️ Architectural Context (How it fits in the architecture)
SSM sits as the secure operation control layer over virtual machines. The SSM Agent connects outbound to Systems Manager APIs. Operators interact with SSM via the AWS API to manage servers without requiring direct network routing.

---

## 🧩 Problem Solver (What problem it solves)
Managing large server fleets requires managing SSH/RDP ports, distributing key pairs, maintaining bastion hosts, and tracking patch updates. Systems Manager solves this by routing all shell traffic and patch baselines securely over AWS APIs.

---

## 🟢 Operational Impact (What will happen with it operating)
SSH key management is eliminated, and ingress port 22 is securely closed on servers. Logging of terminal inputs/outputs is centralized in S3/CloudWatch, and patching compliance is monitored dynamically.

---

## 🔴 Failure Impact (What will happen without it)
Without Systems Manager, operations teams must open network paths (port 22/3389) on firewalls, manage SSH keys, host public bastion nodes, and use manual methods to deploy security patches.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **AWS Systems Manager**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
