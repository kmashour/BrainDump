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

## 📑 Amazon CloudFront & AWS Global Accelerator

Amazon CloudFront and AWS Global Accelerator are two key network performance optimization services running on AWS's edge network infrastructure.

*   **CloudFront MOC:** See `[[Amazon CloudFront]]` for the CDN architecture (edge caching of HTTP/HTTPS content, OAC origins, and cache invalidation).
*   **Global Accelerator MOC:** See `[[AWS Global Accelerator]]` for Anycast IP routing (caching-less proxy routing of TCP/UDP socket traffic over private global fiber).
*   **Economic Advantage:** Routing static/dynamic assets through CloudFront is significantly cheaper in outbound data transfer (Egress) fees compared to downloading objects directly from S3, serving as a key strategy for S3 cost optimization.

*Read more in [3-12_aws_route53_dns.md](../Reference%20Notes/3-12_aws_route53_dns.md) and [3-13_aws_cloudfront_cdn.md](../Reference%20Notes/3-13_aws_cloudfront_cdn.md)*

