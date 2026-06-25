---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[AWS Organizations]]"
  - "[[Service Control Policy]]"
  - "[[AWS IAM Identity Center]]"
against: []
reference_guides:
  - "[[Reference Notes/3-2_aws_iam.md]]"
tags:
  - aws/controltower
  - aws/organizations
  - status/completed
---

# AWS Control Tower

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - Identity and Access Management]] > **AWS Control Tower**

---

## 🎯 Purpose (Why it is used)
AWS Control Tower provides the easiest way to set up and govern a secure, multi-account AWS environment based on AWS best practices. It automates the creation of a Landing Zone (a well-architected multi-account baseline) and enforces compliance policies using pre-configured guardrails.

---

## ⚙️ Functionality (What it is doing)
- **Landing Zone Setup:** Automates account structures, federated access (SSO), and centralized logging using CloudTrail and AWS Config.
- **Account Factory Provisioning:** Standardizes the deployment of new, pre-configured AWS accounts with default network templates.
- **Enforce Guardrails:** Employs guardrails to maintain ongoing policy compliance:
  - *Preventive Guardrails:* Block actions using Service Control Policies (SCPs) via AWS Organizations.
  - *Detective Guardrails:* Identify compliance drift using AWS Config rules.
- **Unified Compliance Dashboard:** Offers central monitoring and compliance status of all organization accounts.
- **Automated Remediation:** Triggers alerts (via SNS) or auto-remediation workflows (via Lambda) when non-compliant resources are detected.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Control Tower operates as a high-level orchestration engine that sits on top of AWS Organizations, AWS IAM Identity Center, AWS Service Catalog, and AWS CloudFormation. It manages resources across multiple administrative accounts (e.g., Log Archive, Security/Audit accounts) to isolate logging and monitoring traffic.

---

## 🧩 Problem Solver (What problem it solves)
Manually constructing a secure multi-account environment—establishing centralized log pipelines, directory federation, account provisioning catalogs, and compliance rules—requires extensive engineering hours and is prone to configuration errors. Control Tower solves this by deploying a fully functional, well-architected landing zone in a few clicks.

---

## 🟢 Operational Impact (What will happen with it operating)
Provisioning new accounts is automated and governed by Service Catalog. Compliance baselines are continuously verified, and alerts are dispatched instantly when security configurations are altered in member accounts.

---

## 🔴 Failure Impact (What will happen without it)
Without Control Tower, organizations must manually construct and monitor their multi-account guardrails. This increases the likelihood of security holes, makes it harder to audit compliance, and creates bottleneck delays for developers requesting new accounts.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **AWS Control Tower**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[AWS Control Tower]]
SORT file.name ASC
```
