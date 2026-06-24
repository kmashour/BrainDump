---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[aws]]"
sub_type: core-concept
source_type: documentation
source_url: "https://docs.aws.amazon.com/route53/"
author: "AWS Documentation"
course_title: "Route 53 & CloudFront Integration Guides"
against: []
tags:
  - aws/route53
  - aws/cloudfront
  - aws/deep-dive
---

# aws - Route 53 DNS and CloudFront CDN

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[aws]] > **Route 53 DNS and CloudFront CDN**

---

## 📑 Amazon Route 53 DNS

Amazon Route 53 is a highly available and scalable Domain Name System (DNS) service. It maps human-readable domain names (e.g. `example.com`) to numeric IP addresses.

*   **Concept MOC:** See `[[Amazon Route 53]]` for the service architecture overview.
*   **Hosted Zones:** See `[[Route 53 Hosted Zone]]` (Public vs. Private hosted zones, Zone Apex constraints, CNAME vs. Alias).
*   **Routing Policies:** See `[[Route 53 Routing Policies]]` (Simple, Weighted, Latency, Failover, Geolocation, Geoproximity, IP-based, and Multi-value routing).
*   **Resolver Endpoints:** See `[[Route 53 Resolver]]` (Inbound vs. Outbound resolver endpoints for hybrid cloud networking).

---

## 📑 Amazon CloudFront CDN

Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency and high transfer speeds.

*   **Edge Locations:** A global network of data centers that cache copies of your static and dynamic files (images, CSS, JS, etc.) closer to your users.
*   **Origin Servers:** The source of truth for the files (e.g. S3 buckets, EC2 instances, or Application Load Balancers).
*   **Economic Advantage:** Fetching data through CloudFront edge caches is significantly cheaper in outbound data transfer (Egress) fees compared to downloading objects directly from S3 buckets, making it a primary strategy for S3 cost optimization.

*Read more in [3-12_aws_route53_dns.md](../Reference%20Notes/3-12_aws_route53_dns.md) and [3-13_aws_cloudfront_cdn.md](../Reference%20Notes/3-13_aws_cloudfront_cdn.md)*
