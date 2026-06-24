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
  - "[[Route 53 Hosted Zone]]"
  - "[[Route 53 Routing Policies]]"
  - "[[Route 53 Resolver]]"
against: []
reference_guides:
  - "[[Reference Notes/3-12_aws_route53_dns.md]]"
tags:
  - aws/route53
  - status/completed
---

# Amazon Route 53

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > **Amazon Route 53**

---

## 🎯 Purpose (Why it is used)
Amazon Route 53 is a highly available and scalable Domain Name System (DNS) service. It serves as the authoritative DNS service for registered domains, translating human-friendly domain names (such as `example.com`) into computer-understandable numeric IP addresses (such as `192.0.2.1` or `2001:db8::1`), and acts as a domain registrar to manage domain names under a single interface.

---

## ⚙️ Functionality (What it is doing)
*   **Domain Registration:** Purchases and registers new domains, configures auto-renewal, and protects registrant contact privacy.
*   **DNS Resolution:** Manages zone files containing records (A, AAAA, CNAME, NS, MX, TXT) and responds to client queries with high speed and reliability.
*   **Health Checking:** Actively monitors the availability and latency of endpoints using a global network of health checkers, enabling automatic DNS failover when endpoints fail.
*   **Traffic Routing:** Controls global network routing using complex policies (Simple, Weighted, Latency, Failover, Geolocation, Geoproximity, IP-based, and Multi-value).
*   **Hybrid Resolver:** Provides DNS resolver endpoints (Inbound/Outbound) to connect AWS Cloud DNS with on-premises corporate name servers.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Route 53 sits at the outermost perimeter of an AWS infrastructure deployment. When client applications attempt to access services (e.g., Application Load Balancers, CloudFront distributions, S3 static websites, or API Gateways), they first resolve the DNS domain via Route 53. Inside a VPC, Route 53 acts as the internal core DNS resolver (VPC IP address `.2` resolver) mapping internal private domain zones.

---

## 🧩 Problem Solver (What problem it solves)
*   **Eliminates DNS Outages:** As the only AWS service offering a 100% availability SLA, it ensures global name resolution remains online even during major regional infrastructure failures.
*   **Mitigates Regional Downtime:** Automated health checking and DNS failover automatically redirect traffic away from unhealthy servers/regions to standby resources.
*   **Reduces Egress Cost & Stale Routing:** Integrates custom Alias records to automatically handle load balancer IP updates without client-side query costs or stale DNS resolution failures.

---

## 🟢 Operational Impact (What will happen with it operating)
When operating normally, Route 53 dynamically routes user requests to healthy and lowest-latency endpoints. Applications load faster for users globally because of geolocation/latency policies, and network costs are optimized by keeping internal corporate traffic strictly inside private VPC networks via private hosted zones.

---

## 🔴 Failure Impact (What will happen without it)
If Route 53 were to fail or misconfigured, all application endpoints using its domain names become completely unreachable (DNS name resolution failure). Inside a VPC, internal resource communication (such as EC2 instances querying databases via internal DNS hostnames) would break immediately, causing complete service degradation.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Amazon Route 53**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
