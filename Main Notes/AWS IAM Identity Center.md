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
  - "[[AWS Directory Services]]"
against: []
reference_guides:
  - "[[Reference Notes/3-2_aws_iam.md]]"
tags:
  - aws/iam
  - aws/sso
  - status/completed
---

# AWS IAM Identity Center

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - Identity and Access Management]] > **AWS IAM Identity Center**

---

## 🎯 Purpose (Why it is used)
AWS IAM Identity Center (formerly AWS Single Sign-On) centralizes administrative access control and single sign-on (SSO) to all accounts within an AWS Organization, as well as business cloud applications and Windows EC2 instances. It replaces the need to manage individual IAM users across multiple accounts.

---

## ⚙️ Functionality (What it is doing)
- **Unified Portal Authentication:** Provides users with a single portal login URL to access all authorized AWS consoles, CLI commands, and business apps.
- **Identity Provider Federation:** Connects to external identity providers (IdPs) like Okta, OneLogin, Ping Identity, Active Directory, or utilizes its built-in directory.
- **Permission Sets Management:** Centralizes the definition of IAM policies (Permission Sets) that are automatically deployed as IAM roles in target member accounts.
- **Multi-Account Group Assignment:** Maps directory user groups (e.g., `DatabaseAdmins`) to specific Permission Sets in target member accounts. Identity Center automatically provisions matching IAM roles in those accounts, which users assume dynamically upon login.
- **SAML 2.0 Integration:** Federates access to popular SaaS platforms (e.g., Salesforce, Microsoft 365, Box) or custom internal SAML-enabled applications.
- **Attribute-Based Access Control (ABAC):** Utilizes directory tags (e.g., Cost Center, Title) to evaluate fine-grained permissions dynamically.

---

## 🏛️ Architectural Context (How it fits in the architecture)
IAM Identity Center is deployed in the management account of an AWS Organization. It interfaces directly with the organization directory and user stores. When an authorized user selects an account in the SSO portal, Identity Center requests temporary security credentials via STS, enabling the user to assume a provisioned IAM Role inside that target member account.

---

## 🧩 Problem Solver (What problem it solves)
Managing separate IAM users in multiple accounts leads to credential sprawl, high audit complexity, and severe security risks during user offboarding. IAM Identity Center solves this by enabling single sign-on and centralized user mapping, allowing security teams to revoke a user's access across all accounts instantly from a single directory.

---

## 🟢 Operational Impact (What will happen with it operating)
Users sign in with their corporate credentials once and navigate to multiple AWS consoles without re-authenticating. Security teams manage access policies centrally using Permission Sets. New accounts provisioned under AWS Organizations are automatically registered with SSO profiles.

---

## 🔴 Failure Impact (What will happen without it)
If the Identity Center portal or the connected Identity Provider (e.g., Active Directory) is unavailable, users cannot authenticate and access the AWS management console or CLI. Administrative operations across the multi-account environment are halted unless backup local IAM login credentials are maintained.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **AWS IAM Identity Center**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[AWS IAM Identity Center]]
SORT file.name ASC
```
