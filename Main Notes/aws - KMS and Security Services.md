---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[aws]]"
sub_type: core-concept
source_type: documentation
source_url: "https://docs.aws.amazon.com/kms/"
author: "AWS Documentation"
course_title: "AWS KMS Developer Guide"
tags:
  - aws/security
  - aws/kms
  - aws/deep-dive
---

# aws - KMS and Security Services

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[aws]] > **KMS and Security Services**

---

## 📑 AWS KMS & Envelope Encryption

AWS Key Management Service (KMS) manages Customer Master Keys (CMKs) to secure your data keys. To avoid sending large files over the network to KMS, AWS enforces **Envelope Encryption**:

1.  **Generate Data Key:** The application requests a data key from KMS using a CMK.
2.  **Key Delivery:** KMS returns a plaintext data key and an encrypted data key.
3.  **Local Encryption:** The application encrypts its data locally using the plaintext key, then discards it from memory.
4.  **Storage:** The application stores the encrypted data alongside the encrypted data key.
5.  **Decryption:** To decrypt, the application sends the encrypted data key to KMS, receives the plaintext key, decrypts the data, and discards the plaintext key.

*Note:* CMKs never leave KMS. AWS-managed keys automatically rotate every 3 years; customer-managed keys rotate optionally every year.

---

## 📑 Secrets Manager vs. Parameter Store

*   **AWS Systems Manager Parameter Store:** A secure, hierarchical database for storing configuration parameters and secrets (passwords, database strings). Free for standard parameters; lacks automatic rotation.
*   **AWS Secrets Manager:** Specifically designed for secrets management. Supports automatic credential rotation (e.g. database passwords) via Lambda integrations, cross-account access, and secrets generation. Paid per secret.

---

## 📑 Edge Security: WAF and Shield

*   **AWS WAF (Web Application Firewall):** Filters HTTP/HTTPS traffic at Layer 7. Protects applications from SQL injection, Cross-Site Scripting (XSS), and bad bots. Can be associated with CloudFront, ALB, and API Gateway.
*   **AWS Shield:** Managed DDoS protection service. Shield Standard protects all customers automatically at Layers 3/4. Shield Advanced provides active mitigation, DDoS response team (DRT) support, and financial protection.

*Read more in [3-3_aws_kms_security.md](../Reference%20Notes/3-3_aws_kms_security.md#1-aws-key-management-service-kms--envelope-encryption)*
