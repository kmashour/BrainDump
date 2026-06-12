---
domains:
  - "aws"
  - "security"
class: reference-note
tier: reference-note
tags:
  - aws/kms
  - aws/encryption
  - aws/security
---

# Module 3-3: AWS KMS & Security

This module details cryptographic key management using **AWS Key Management Service (KMS)**, envelope encryption, secrets protection, user identity syncing via **AWS Cognito**, and edge-security layers utilizing **AWS WAF** and **AWS Shield**.

---

## 🗺️ Cognitive Map: KMS Envelope Encryption

```
+---------------------+
|  Your Application   |
+---------------------+
          |
          | 1. Request Data Key from KMS
          v
+---------------------+
|        AWS KMS      |
|  (with your CMK)    |
+---------------------+
          |
          | 2. Returns:
          |    - Plaintext Data Key
          |    - Encrypted Data Key (encrypted with CMK)
          v
+---------------------+
|  Your Application   |
+---------------------+
          |
          | 3. Uses Plaintext Data Key to Encrypt Data
          v
+---------------------+
| Encrypted Data File |
| + Encrypted Data Key|
+---------------------+
```

---

## 1. AWS Key Management Service (KMS) & Envelope Encryption
AWS KMS handles creation and management of customer master keys (CMKs) to encrypt data at rest.

### A. Envelope Encryption Mechanics
Envelope encryption uses a master key (CMK) to protect a data key, which encrypts the actual data:
1.  **Request:** The application requests a Data Key from KMS using a CMK.
2.  **Response:** KMS generates the Data Key and returns two copies: a **Plaintext Data Key** and an **Encrypted Data Key** (encrypted by the CMK).
3.  **Encryption:** The application encrypts the payload using the Plaintext Data Key, then immediately discards the Plaintext Data Key from memory.
4.  **Storage:** The application stores the encrypted payload alongside the Encrypted Data Key.
5.  **Decryption:** The application sends the Encrypted Data Key to KMS, which decrypts it using the CMK and returns the Plaintext Data Key. The application then decrypts the data.



---

## 2. Key Types & Management
*   **Symmetric Keys:** A single 256-bit AES key used for encryption/decryption. The CMK never leaves the secure boundaries of KMS.
*   **Asymmetric Keys:** Public/Private key pairs used for signing/verification or encryption/decryption.
*   **AWS-Managed Keys:** Free, automatically created on your behalf by AWS (e.g., `aws/s3`). Rotated every 3 years. Cannot be shared across accounts.
*   **Customer-Managed Keys:** Managed by you. Cost $1/month. Allow granular key policies, optional 1-year rotation, and cross-account sharing.

---

## 3. Secrets Manager & Parameter Store
AWS provides two options for managing configurations and secrets:
*   **AWS Systems Manager Parameter Store:** A secure, serverless store for hierarchical configuration data. Free for standard parameters. Does not support automatic rotation natively.
*   **AWS Secrets Manager:** A paid service ($0.40/secret/month) specifically designed for sensitive credentials. Supports auto-rotation (e.g., RDS passwords via Lambda integration) and cross-account access.

---

## 4. Encryption on EC2 and EBS (Eissa Notes)


---

## 5. Audit & Monitoring Services


---

## 6. Deep-Intuition (AARF) Breakdowns

### AARF Breakdown: KMS Customer Managed Keys (CMK)
1.  **The Answer (Core Pattern):** Utilize KMS Customer Managed Keys (CMKs) with explicit IAM Key Policies restricting access to authorized execution roles:
    ```json
    {
      "Sid": "AllowUseOfTheKey",
      "Effect": "Allow",
      "Principal": {"AWS": "arn:aws:iam::123456789012:role/AppExecutionRole"},
      "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey*"
      ],
      "Resource": "*"
    }
    ```
2.  **The Assumptions (Context):** The calling application role must have permission to access both the target storage resource (e.g., S3 bucket, EBS volume) *and* the KMS key used for envelope encryption.
3.  **The Rationale (Why):** Implements separation of duties. Restricting key permissions ensures that even if a user bypasses S3 bucket policies, they cannot read data without decrypting it, providing a double-barrier security topology and complete CloudTrail auditing.
4.  **The Failure Loop (What if not):** If IAM roles have S3 access but lack KMS Decrypt permissions on the custom CMK, application read API requests fail with `Access Denied` or `KMS.AccessDeniedException`, causing application crashes during startup or retrieval.
5.  **Alternative Case (When to use 'if not'):** For non-sensitive, high-volume workloads where API call costs are a major concern, use S3 Managed Keys (SSE-S3) to completely bypass KMS transaction charges.

