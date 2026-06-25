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
  - "[[AWS Secrets Manager]]"
  - "[[aws - KMS and Security Services]]"
against:
  - "[[AWS Secrets Manager]]"
reference_guides:
  - "[[Reference Notes/3-3_aws_kms_security.md]]"
tags:
  - aws/parameterstore
  - status/completed
---

# SSM Parameter Store

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **SSM Parameter Store**

---

## 🎯 Purpose (Why it is used)
AWS Systems Manager (SSM) Parameter Store is a secure, serverless hierarchical database used to store configuration parameters, licensing codes, and secrets. It centralizes configuration management, allowing applications to reference parameters dynamically.

---

## ⚙️ Functionality (What it is doing)
- **Hierarchical Parameter Storage:** Organizes configuration parameters using path structures (e.g. `/finance/payment-app/dev/db-url`).
- **Secret & Non-Secret Support:** Stores configuration in three formats: `String` (plain text), `StringList` (comma-separated list), and `SecureString` (encrypted via integration with AWS KMS).
- **Version Tracking:** Maintains a history of parameter updates, assigning sequential version numbers to enable rolling back configurations.
- **Reference Integration:** Allows referencing parameters directly from AWS CloudFormation stacks, Amazon ECS task definitions, and AWS Systems Manager Run Commands.
- **Secrets Manager Referencing:** Allows querying Secrets Manager secrets via Parameter Store API endpoints using a standardized reference path.
- **Standard vs. Advanced Tiers:**
  - **Standard Tier (Free):** Max size 4KB, max 10,000 parameters. No parameter policies.
  - **Advanced Tier (Paid):** Max size 8KB, max 100,000 parameters. Supports Parameter Policies.
- **Parameter Policies (Advanced Tier):** Enforces lifecycle rules on parameters:
  - *Expiration (TTL):* Automatically deletes the parameter at a specific timestamp.
  - *Expiration Notification:* Triggers EventBridge events prior to expiration.
  - *No-Change Notification:* Triggers EventBridge events if a parameter isn't updated within a set window.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Parameter Store serves as a central config engine. Applications (EC2 instances, Lambda functions) call Parameter Store via SDK during bootstrap or dynamically. IAM policies leverage path prefixes (e.g., `arn:aws:ssm:*:*:parameter/dev/*`) to grant wildcard access to entire application environments.

---

## 🧩 Problem Solver (What problem it solves)
Parameter Store eliminates "configuration sprawl" (where configuration values are scattered across separate application files or environment properties). It provides a free, highly scalable option for storing non-sensitive configuration parameters, reserving paid Secrets Manager secrets for credentials requiring automatic rotation.

---

## 🟢 Operational Impact (What will happen with it operating)
Applications load environment-specific parameters dynamically, eliminating the need to compile separate builds for dev, staging, and production. Parameter changes can trigger EventBridge events to automatically notify operations teams or execute Lambda functions to refresh configurations in real-time.

---

## 🔴 Failure Impact (What will happen without it)
If Parameter Store is unavailable or permission is denied, applications fail to retrieve essential configuration endpoints and credentials during startup. This leads to configuration errors, database connection failures, and system-wide bootstrap failures.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **SSM Parameter Store**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
