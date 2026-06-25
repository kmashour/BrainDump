---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[aws - Identity and Access Management]]"
  - "[[Service Control Policy]]"
  - "[[AWS IAM Identity Center]]"
  - "[[AWS Control Tower]]"
against: []
reference_guides:
  - "[[Reference Notes/3-2_aws_iam.md]]"
tags:
  - aws/organizations
  - status/completed
---

# AWS Organizations

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - Identity and Access Management]] > **AWS Organizations**

---

## 🎯 Purpose (Why it is used)
AWS Organizations is an account management service that enables cloud administrators to consolidate multiple AWS accounts into an organization that they create and centrally manage. It provides administrative scaling, unified billing, and compliance controls across all member accounts.

---

## ⚙️ Functionality (What it is doing)
- **Hierarchical Governance:** Groups accounts into Organizational Units (OUs) to apply policies at root, OU, or account levels.
- **Consolidated Billing:** Consolidates payments across all accounts under a single management account.
- **Aggregate Volume Pricing:** Combines resource usage across all member accounts to qualify for higher discount tiers on services (e.g., EC2, S3).
- **Automated Account Creation:** Provides APIs to automate the creation of new AWS accounts programmatically.
- **Resource Sharing:** Automatically shares Reserved Instances (RIs) and Savings Plans discounts across all member accounts.
- **Service Integration:** Integrates with other AWS services (e.g., CloudTrail, GuardDuty, IAM Identity Center) to enable organization-wide monitoring and access.
- **Stronger Security Boundaries:** Isolates workloads in separate accounts to restrict security breaches and API/credential exposure, rather than relying solely on VPC separation.
- **Centralized Security Logging:** Provisions organization-wide CloudTrail logging to collect audit trails in a dedicated, secure Central Logging S3 account.
- **Automatic Cross-Account Administration:** Automatically establishes administrative roles in member accounts for management and security monitoring.

---

## 🏛️ Architectural Context (How it fits in the architecture)
AWS Organizations sits at the top level of the multi-account cloud hierarchy. The Organization is created within the Management Account, which manages the root OU. Member accounts are organized into sub-OUs representing business units or environments. Service Control Policies (SCPs) are attached to these OUs and flow down to restrict member accounts' API spaces.

---

## 🧩 Problem Solver (What problem it solves)
As organizations grow, managing hundreds of AWS accounts independently leads to security drift, billing complexity, and administrative overhead. AWS Organizations solves this by providing a single control plane for account provisioning, security governance, and billing aggregation, replacing manual cross-account roles and separate invoices.

---

## 🟢 Operational Impact (What will happen with it operating)
Billing is simplified into a single monthly invoice. Administrators gain the ability to deploy security baseline settings (like organization-wide CloudTrail logging) in a single operation. Developers can request new, isolated sandboxes in seconds via API, which are automatically subject to organizational boundaries.

---

## 🔴 Failure Impact (What will happen without it)
Without AWS Organizations, each account operates as a separate billing and administrative silo. Global compliance enforcement is impossible, requiring security teams to configure policies in every account individually. Lost opportunities for aggregated billing discounts can lead to significantly higher cloud spend.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **AWS Organizations**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[AWS Organizations]]
SORT file.name ASC
```
