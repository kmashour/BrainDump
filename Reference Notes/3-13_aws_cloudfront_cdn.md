---
domains:
  - "aws"
  - "network"
---

# Module 3-13: AWS CloudFront CDN

**Breadcrumbs:** [[3-Index - AWS|📐 AWS Index]] > **Module 3-13: AWS CloudFront CDN**

This module details Edge location caching, Origin configurations, cache invalidations, and secure private delivery mechanisms.

---

## 🚀 CloudFront Edge Caching Mechanics

Amazon CloudFront is a Content Delivery Network (CDN) that caches data globally:

```
User ----(HTTPS request)----> Edge Location (Cache Hit? Yes -> Return Data)
                                   |
                             (Cache Miss?)
                                   v
                             Origin (S3 / ALB) ---> Cache & Return to User
```

* **Cache TTL:** Controlled by cache control headers (`Cache-Control: max-age`) sent by the origin server.
* **Cache Invalidation:** Forcefully purges cached files from Edge Locations before the TTL expires, ensuring users receive updated versions of files. Billed per path invalidated.

---

## 🔒 Securing Origins: OAI vs. OAC

When S3 is the origin for a CloudFront distribution, it must be secured so users cannot bypass the CDN:
* **Origin Access Identity (OAI):** Legacy method. Creates a virtual IAM identity for the distribution to allow S3 access. Does not support SSE-KMS encryption.
* **Origin Access Control (OAC):** Modern, recommended method. Supports all S3 encryption types (SSE-KMS), provides granular policy signing, and has improved security.

---

## 🧠 Deep-Intuition (AARF) Breakdown: CloudFront OAC for Secure S3 Delivery

1. **The Answer (Core Pattern):** Restrict S3 bucket access to a CloudFront distribution using Origin Access Control (OAC) and configure the S3 Bucket Policy to explicitly allow the distribution principal:
    ```json
    {
      "Version": "2012-10-17",
      "Statement": {
        "Sid": "AllowCloudFrontServicePrincipal",
        "Effect": "Allow",
        "Principal": {"Service": "cloudfront.amazonaws.com"},
        "Action": "s3:GetObject",
        "Resource": "arn:aws:s3:::my-bucket/*",
        "Condition": {
          "StringEquals": {
            "AWS:SourceArn": "arn:aws:cloudfront::123456789012:distribution/EDIST12345"
          }
        }
      }
    }
    ```
2. **The Assumptions (Context):** The S3 bucket public access must be blocked, and the CloudFront origin settings must be set to use OAC.
3. **The Rationale (Why):** Bypassing the CDN exposes the S3 bucket to data extraction attacks and high transfer costs. Using OAC ensures S3 objects are only served via CloudFront, enabling Edge security controls (WAF) and caching benefits.
4. **The Failure Loop (What if not):** If OAC is misconfigured or the S3 policy is not updated, S3 returns `403 Forbidden` errors to the CDN, causing a complete website outage.
5. **Alternative Case (When to use 'if not'):** For public S3 buckets hosting assets that do not require regional latency controls or WAF filtering, leave public access open.

---

## 🔐 Signed URLs vs. Signed Cookies

* **Signed URLs:** Provides temporary access to a single file. (Use for single downloads, streaming media, or individual files).
* **Signed Cookies:** Provides temporary access to multiple files. (Use for premium subscriber content or restricted website sections with many files).

![[../Attachments/Pasted image 20250719154304.png]]
![[../Attachments/Pasted image 20250719154322.png]]
![[../Attachments/Pasted image 20250719154504.png]]
![[../Attachments/Pasted image 20250719154825.png]]
![[../Attachments/Pasted image 20250719154834.png]]
![[../Attachments/Pasted image 20250721181838.png]]
![[../Attachments/Pasted image 20250721181850.png]]
![[../Attachments/Pasted image 20250721181910.png]]
![[../Attachments/Pasted image 20250721181922.png]]
![[../Attachments/Pasted image 20250721182013.png]]
![[../Attachments/Pasted image 20250721182023.png]]
