---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Amazon S3]]"
sub_type: core-concept
source_type: udemy
source_url: "https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/"
author: "Stephane Maarek"
course_title: "Ultimate AWS Certified Solutions Architect Associate"
tags:
  - aws/s3
  - aws/encryption
  - aws/deep-dive
---

# Amazon S3 - S3 Encryption

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Amazon S3]] > **S3 Encryption**

---

## 📑 S3 Encryption At Rest & In Transit
Amazon S3 provides multiple encryption methods to protect data at rest and during transmission.

### 1. Server-Side Encryption (SSE)
AWS performs the encryption and decryption operations using one of three backend mechanisms:
- **SSE-S3 (S3-Managed Keys):** S3 manages, rotates, and owns the keys. Enabled by default for all new objects. Uses AES-256 (`"x-amz-server-side-encryption": "AES256"`).
- **SSE-KMS (AWS KMS Keys):** Leverages AWS Key Management Service (KMS). Allows key rotation, audit trails with CloudTrail, and custom key usage policies. High request volumes can cause throttling against KMS API quotas; S3 Bucket Keys can be enabled to cache KMS keys and reduce KMS API requests and cost by up to 99%.
- **SSE-C (Customer-Provided Keys):** The customer manages the keys outside AWS. The client passes the key in HTTP headers on every request. S3 uses the key for the operation and discards it immediately (never stores it). HTTPS is mandatory.
- **DSSE-KMS (Double Engine KMS):** Applies two layers of server-side encryption to objects, meeting strict regulatory compliance standards.

### 2. Client-Side Encryption
The client encrypts the data locally before sending it to S3. Decryption also happens locally after downloading. S3 only sees and stores pre-encrypted binary blobs. The client is 100% responsible for managing the encryption lifecycle and keys.

### 3. Encryption in Transit (Enforcing SSL/TLS)
S3 supports both unencrypted HTTP and encrypted HTTPS. Best practice dictates forcing encryption in transit. This is done via a bucket policy that explicitly denies any S3 operations when the condition `"aws:SecureTransport": "false"` is met.

*Read more in [[Reference Notes/3-6_aws_s3_storage.md#6-s3-encryption]]*
