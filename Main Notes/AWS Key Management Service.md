---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: security
domains:
  - "aws"
related_concepts:
  - "[[aws]]"
  - "[[AWS Secrets Manager]]"
  - "[[SSM Parameter Store]]"
  - "[[aws - KMS and Security Services]]"
against:
  - "[[AWS CloudHSM]]"
reference_guides:
  - "[[Reference Notes/3-3_aws_kms_security.md]]"
tags:
  - aws/kms
  - status/completed
---

# AWS Key Management Service

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **AWS Key Management Service**

---

## 🎯 Purpose (Why it is used)
AWS Key Management Service (KMS) is a fully managed, highly available service that enables customers to create, manage, and control cryptographic keys used to encrypt data at rest. It integrates with other AWS services and client-side applications, enforcing strict authorization boundaries for key usage.

---

## ⚙️ Functionality (What it is doing)
- **Key Lifecycle Management:** Handles creation, deletion, description, and rotation (automatic or on-demand) of Customer Managed Keys (CMKs).
- **Access Control Policies:** Enforces fine-grained key usage using JSON-based Key Policies (default or custom) that define who can administer or use the key (independent of IAM policies).
- **Service Integration:** Seamlessly handles encryption and decryption across AWS services (such as EBS, S3, RDS, SSM).
- **Compliance and Auditability:** Integrates with AWS CloudTrail to log every API call (e.g. key usage, administration, rotation) for compliance audits.
- **Symmetric vs Asymmetric Support:** Supports symmetric keys (256-bit AES, where the key never leaves KMS) and asymmetric keys (RSA/ECC public/private key pairs used for signing/verification or encryption/decryption).
- **Multi-Region Replicas:** Provisions Multi-Region keys (sharing the same key ID and key material) to facilitate low-latency local decryption for global applications without cross-region API calls or re-encryption.

---

## 🏛️ Architectural Context (How it fits in the architecture)
KMS acts as the centralized cryptographic provider for an AWS account. Applications (e.g., EC2 instances, Lambda functions) and AWS services call the KMS API out-of-band to request data key generation or data decryption. Key access requests are validated against both the target IAM policy and the KMS Key Policy.

---

## 🧩 Problem Solver (What problem it solves)
KMS eliminates the operational overhead of procuring, configuring, and managing physical Hardware Security Modules (HSMs) and secure key distribution software. It prevents data leakage in the event of physical drive theft (since EBS/S3 data is encrypted with keys stored in HSMs) and implements strict separation of duties (e.g., database admins can access database records but cannot decrypt fields without KMS permission).

---

## 🟢 Operational Impact (What will happen with it operating)
AWS services perform envelope encryption transparently. For example, when S3 downloads an encrypted object, it calls KMS in the background to decrypt the data key, decrypts the object locally in memory, and returns it to the client. Users and compliance officers gain a detailed audit log in CloudTrail of who accessed what data and when.

---

## 🔴 Failure Impact (What will happen without it)
If KMS is unavailable or permissions are misconfigured, applications cannot decrypt data keys, triggering complete service outages. EC2 hosts will fail to attach encrypted EBS volumes, S3 will return `AccessDeniedException` on object retrievals, and stateful application components will crash on startup.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **AWS Key Management Service**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
