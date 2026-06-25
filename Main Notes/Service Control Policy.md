---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: security
domains:
  - "aws"
related_concepts:
  - "[[aws - Identity and Access Management]]"
  - "[[AWS Organizations]]"
  - "[[aws - IAM Policy]]"
against: []
reference_guides:
  - "[[Reference Notes/3-2_aws_iam.md]]"
tags:
  - aws/organizations
  - aws/scp
  - status/completed
---

# Service Control Policy

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - Identity and Access Management]] > **Service Control Policy**

---

## 🎯 Purpose (Why it is used)
Service Control Policies (SCPs) are organizational policy types used to manage permissions in an AWS Organization. SCPs offer central control over the maximum available permissions for all accounts in your organization, ensuring member accounts stay within corporate compliance guidelines.

---

## ⚙️ Functionality (What it is doing)
- **Establish Permission Guardrails:** Limits the actions that identity-based and resource-based policies can perform on users and roles in member accounts.
- **Hierarchical Inheritance:** Applies to accounts at Root, OU, or individual levels, cascading permissions down the organizational tree.
- **Explicit Allow Filtering:** Filters permissions rather than granting them. Accounts must have an explicit allow at every level of the hierarchy (`FullAWSAccess` SCP is attached by default).
- **Deny Precedence:** An explicit deny statement in an SCP overrides any allows granted in identity-based or resource-based policies in member accounts.
- **Safety Bypass:** Management accounts are immune to SCPs to prevent accidental lockout of root management functions.

---

## 🏛️ Architectural Context (How it fits in the architecture)
SCPs act as a filter positioned between organizational administration and member account execution. When an IAM user or role in a member account attempts an action, the IAM evaluation engine checks if the action is allowed by applicable SCPs before checking account-level identity or resource-based policies.

---

## 🧩 Problem Solver (What problem it solves)
Even with strict IAM configuration, individual account administrators in member sandboxes could modify log settings, delete backups, or run unauthorized high-cost services. SCPs solve this by locking down the maximum API space at the organizational level, preventing administrators in member accounts from bypassing security baselines.

---

## 🟢 Operational Impact (What will happen with it operating)
Security baselines are enforced globally. Administrators in member accounts cannot disable security features like CloudTrail or leave the organization. The effective permission space of all users/roles (including root users of member accounts) is constrained by the SCP boundaries.

---

## 🔴 Failure Impact (What will happen without it)
Without SCPs, there is no centralized filter to restrict API actions inside member accounts. A compromised administrator account in a member sandbox can delete audit logs, change compliance configurations, or incur significant costs, exposing the organization to security breaches and financial loss.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Service Control Policy**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[Service Control Policy]]
SORT file.name ASC
```
