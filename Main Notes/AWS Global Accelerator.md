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
  - "[[Amazon CloudFront]]"
  - "[[load-balancing]]"
against:
  - "[[Amazon CloudFront]]"
reference_guides:
  - "[[Reference Notes/3-13_aws_cloudfront_cdn.md]]"
tags:
  - aws/global-accelerator
  - status/completed
---

# AWS Global Accelerator

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > **AWS Global Accelerator**

---

## 🎯 Purpose (Why it is used)
AWS Global Accelerator is a network acceleration service that optimizes the path from global clients to your applications using the AWS private global network. It bypasses the public internet transit path, resolving issues with latency, packet loss, and connection instability, while providing static Anycast IP addresses for simplified whitelisting and rapid regional failover.

---

## ⚙️ Functionality (What it is doing)
*   **Anycast Routing:** Provides **two static Anycast IP addresses** announced globally. Client requests automatically route to the nearest edge location.
*   **AWS Private Network Transit:** Proxies incoming TCP/UDP traffic from the edge location directly to backend application endpoints over the private AWS global fiber network.
*   **Endpoint Health Checks & Failover:** Continuously monitors the health of configured endpoints across multiple AWS Regions and automatically redirects traffic to a healthy endpoint in less than 30 seconds upon failure.
*   **Session Stickiness:** Supports Client Affinity (sticky sessions) mapping subsequent requests from a specific client IP to the same endpoint.
*   **Resource Compatibility:** Integrates with endpoints such as Application Load Balancers (ALBs), Network Load Balancers (NLBs), EC2 instances, and Elastic IPs.

---

## 🏛️ Architectural Context (How it fits in the architecture)
AWS Global Accelerator sits at the outermost entry point of the infrastructure. Instead of clients resolving dynamic DNS mappings to regional load balancers (which can cache stale IPs), clients connect to the accelerator's two fixed Anycast IPs. The accelerator acts as a high-speed Layer 4 proxy directing traffic to regional ALBs or EC2 groups.

---

## 🧩 Problem Solver (What problem it solves)
*   **Public Internet Jitter:** Bypasses congested routers and multiple network hops on the public internet, routing packets through AWS's private network instead.
*   **DNS Propagation Delays:** Eliminates regional failover downtime caused by DNS cache propagation delays. The accelerator's Anycast IPs remain unchanged, and failover happens internally within 30 seconds.
*   **Dynamic IP Whitelisting Overhead:** Provides exactly two static IPs, removing the operational overhead for enterprise clients who must whitelist server endpoints in corporate firewalls.

---

## 🟢 Operational Impact (What will happen with it operating)
Global users experience stable connection speeds, low latency, and zero packet drops, which is critical for gaming, real-time IoT feeds, VoIP, and financial transactions. Multi-region architectures achieve deterministic, fast failovers during regional cloud outages.

---

## 🔴 Failure Impact (What will happen without it)
Without Global Accelerator, clients must connect to application endpoints over the public internet, introducing latency, jitter, and packet loss. Regional failovers will rely on DNS routing updates (e.g., Route 53 latency/failover policies), which can cause up to several minutes of downtime due to client-side DNS caching of expired TTL records.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **AWS Global Accelerator**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
