---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: network
domains:
  - "aws"
  - "networking"
related_concepts:
  - "[[aws - Route 53 DNS and CloudFront CDN]]"
  - "[[Amazon Route 53]]"
  - "[[AWS Global Accelerator]]"
  - "[[caching]]"
  - "[[cdn]]"
against:
  - "[[AWS Global Accelerator]]"
reference_guides:
  - "[[Reference Notes/3-13_aws_cloudfront_cdn.md]]"
tags:
  - aws/cloudfront
  - status/completed
---

# Amazon CloudFront

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > **Amazon CloudFront**

---

## 🎯 Purpose (Why it is used)
Amazon CloudFront is a globally distributed Content Delivery Network (CDN) service that accelerates the delivery of static and dynamic web content (HTML, CSS, JS, images, media files, and APIs) to users worldwide. By caching content at Edge Locations closer to clients, it minimizes network latency, reduces origin server load, and cuts egress bandwidth costs.

---

## ⚙️ Functionality (What it is doing)
*   **Geographic Content Delivery:** Serves cached assets directly from a global network of hundreds of Edge Locations and Regional Edge Caches.
*   **Cache Management:** Utilizes TTL policies and path-specific cache behaviors to control caching rules, SSL enforcement, and parameter forwarding.
*   **Origin Protection & Acceleration:** Fetches content from backends (Amazon S3 buckets with Origin Access Control (OAC), private endpoints via VPC Origins, or custom HTTP servers) over the optimized private AWS global network.
*   **Edge Security & WAF Integration:** Provides baseline Layer 3/4 DDoS protection via AWS Shield Standard and allows Layer 7 firewalling using AWS WAF.
*   **Dynamic Cache Invalidation:** Supports path-based force-refresh commands (`/images/*`, `/index.html`, `/*`) to purge stale files from edge POPs instantly.

---

## 🏛️ Architectural Context (How it fits in the architecture)
CloudFront is positioned at the outermost perimeter of the application stack, immediately succeeding DNS resolution (Route 53). When a client requests content, DNS points to CloudFront. Static assets are served directly from the Edge, while dynamic requests (e.g., APIs) are proxied back through CloudFront's persistent connection pool to regional load balancers (ALBs) or EC2 origins.

---

## 🧩 Problem Solver (What problem it solves)
*   **High Latency:** Eliminates long distance round-trips over the public internet by caching content at geographically close edge sites.
*   **High Storage Costs (Egress Savings):** Outbound data transfer fees (Egress) from S3 directly to the public internet are expensive. Routing S3 traffic through CloudFront is significantly cheaper, optimizing storage data delivery costs.
*   **Origin Overload (Flash Crowds):** Absorbs high request volumes during traffic spikes, ensuring that the backend origins do not crash from processing redundant static queries.

---

## 🟢 Operational Impact (What will happen with it operating)
Users experience near-instantaneous page loads for images, scripts, and stylesheets, which improves user experience and SEO scores. Web servers only receive dynamic API traffic, reducing CPU usage, memory requirements, and provisioning costs.

---

## 🔴 Failure Impact (What will happen without it)
If CloudFront is disabled or misconfigured, all static and dynamic requests must be processed directly by the origin backend servers. Under high traffic loads, this will exhaust server bandwidth and compute resources, causing slow response times, connection timeouts, and complete application outages.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Amazon CloudFront**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
