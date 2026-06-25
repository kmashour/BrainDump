---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[aws - Identity and Access Management]]"
  - "[[AWS IAM Identity Center]]"
against: []
reference_guides:
  - "[[Reference Notes/3-2_aws_iam.md]]"
tags:
  - aws/directoryservice
  - aws/active-directory
  - status/completed
---

# AWS Directory Services

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - Identity and Access Management]] > **AWS Directory Services**

---

## 🎯 Purpose (Why it is used)
AWS Directory Services enables AWS resources to run and integrate with Microsoft Active Directory (AD) in the AWS Cloud. It provides managed solutions to connect AWS services to existing on-premises directories or deploy new directory systems, simplifying user and resource management.

---

## ⚙️ Functionality (What it is doing)
- **Managed Active Directory:** Deploys a highly available, Microsoft AD framework on AWS managed infrastructure (Managed Microsoft AD).
- **Directory Proxying:** Connects AWS applications to an on-premises directory without data replication (AD Connector).
- **AD-Compatible Directory:** Deploys a lightweight, Samba-based active directory for cloud-only use cases (Simple AD).
- **Domain Joining:** Enables EC2 instances running Windows or Linux to join the directory domain for centralized credential authentication.
- **Trust Relationships:** Establishes secure forest trust relationships between AWS Managed AD and on-premises Active Directories.
- **Multi-Factor Authentication:** Integrates with RADIUS infrastructures to enable MFA for directory authentication.

---

## 🏛️ Architectural Context (How it fits in the architecture)
AWS Directory Services deployed within a customer's VPC is connected via virtual private gateways (VPN/Direct Connect) to on-premises systems. AWS services (such as WorkSpaces, IAM Identity Center, and RDS for SQL Server) interface with Directory Services to validate credentials and authenticate users.

---

## 🧩 Problem Solver (What problem it solves)
Migrating legacy Windows workloads to AWS is difficult if they rely on Active Directory for authentication, file share access, and group policies. AWS Directory Services solves this by providing managed AD infrastructure in the cloud or acting as a proxy gateway to on-premises domain controllers, avoiding manual replication setup.

---

## 🟢 Operational Impact (What will happen with it operating)
EC2 Windows instances automatically join the domain at startup. Domain users authenticate using their existing corporate passwords to access AWS applications. Directory backups and operating system patches are managed automatically by AWS.

---

## 🔴 Failure Impact (What will happen without it)
If AWS Directory Services becomes unavailable, users cannot authenticate to WorkSpaces, console SSO portals, or domain-joined applications. EC2 instances cannot authenticate domain logins, and directory-based applications fail to query objects, causing service disruption.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **AWS Directory Services**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[AWS Directory Services]]
SORT file.name ASC
```
