---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: security
domains:
  - "aws"
related_concepts:
  - "[[aws]]"
  - "[[AWS Key Management Service]]"
  - "[[SSM Parameter Store]]"
  - "[[aws - KMS and Security Services]]"
against:
  - "[[SSM Parameter Store]]"
reference_guides:
  - "[[Reference Notes/3-3_aws_kms_security.md]]"
tags:
  - aws/secretsmanager
  - status/completed
---

# AWS Secrets Manager

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **AWS Secrets Manager**

---

## 🎯 Purpose (Why it is used)
AWS Secrets Manager is a managed service designed to store, retrieve, rotate, and audit database credentials, API keys, OAuth tokens, and other secrets. It replaces hardcoded credentials in application code with dynamic API calls, minimizing the risk of credential exposure.

---

## ⚙️ Functionality (What it is doing)
- **Automatic Secrets Rotation:** Automatically rotates secrets on a scheduled interval (e.g., every 30 days) or on-demand without redeploying applications.
- **Lambda Rotation Integration:** Interfaces with AWS Lambda to orchestrate rotations (e.g. changing the credentials on the target database, verifying accessibility, and then updating Secrets Manager).
- **Out-of-the-Box Integrations:** Directly rotates credentials for RDS (MySQL, PostgreSQL, Oracle, SQL Server), Amazon Aurora, Redshift, and DocumentDB databases.
- **Cross-Region Replication:** Replicates secrets automatically across multiple AWS regions to support disaster recovery, local low-latency access, and multi-region active-active architectures.
- **Resource-Based Key Policies:** Supports attaching resource policies to control access, enabling secure cross-account secret sharing without assuming IAM roles.
- **Encryption at Rest:** Enforces encryption of all secrets at rest using default AWS-managed KMS keys or custom Customer Managed Keys (CMKs).

---

## 🏛️ Architectural Context (How it fits in the architecture)
Secrets Manager sits alongside application hosting platforms (EC2, ECS, EKS, Lambda). At runtime, applications call the Secrets Manager API using the AWS SDK to retrieve the latest credentials. To minimize latency and API costs, client applications typically cache secret values locally for a short time.

---

## 🧩 Problem Solver (What problem it solves)
It solves the issue of hardcoded secrets in Git repositories, container images, and plaintext environment variables. It automates database password rotation—which is historically difficult because it requires synchronizing password updates on both the database and all dependent application servers.

---

## 🟢 Operational Impact (What will happen with it operating)
Applications dynamically retrieve credentials, making them immune to database password changes. Security teams can enforce 30-day password rotation policies globally. If the primary region suffers an outage, replica secrets can be promoted to standalone secrets to maintain application availability.

---

## 🔴 Failure Impact (What will happen without it)
If Secrets Manager is unavailable or permissions are revoked, applications cannot fetch credentials during startup or execution. This results in immediate connection failures to databases, third-party APIs, and external microservices, causing complete application downtime.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **AWS Secrets Manager**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
