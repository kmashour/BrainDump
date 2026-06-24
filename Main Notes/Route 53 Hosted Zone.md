---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Amazon Route 53]]"
sub_type: core-concept
source_type: documentation
source_url: "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-working-with.html"
author: "AWS Documentation"
course_title: "AWS Certified Solutions Architect Associate"
tags:
  - aws/route53
  - aws/deep-dive
---

# Route 53 Hosted Zone

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[Amazon Route 53]] > **Route 53 Hosted Zone**

---

## 📑 Public vs. Private Hosted Zones

A **Hosted Zone** is a container that holds DNS records for a domain name and all its subdomains. It dictates how queries are resolved for that specific namespace.

### 🌐 Public Hosted Zones
*   **Definition:** Resolves queries for domains accessible on the public internet.
*   **Resolvability:** Public name servers respond to requests from any client on the internet.
*   **Typical Targets:** Public load balancers, CloudFront distributions, external S3 static web servers, and third-party SaaS entry points.

### 🔒 Private Hosted Zones
*   **Definition:** Resolves queries for domains inside one or more Virtual Private Clouds (VPCs).
*   **Resolvability:** Only resources within the associated VPCs can resolve the domain. The domain name structure and IP targets are completely hidden from the public internet (e.g., `db-cluster.internal`).
*   **Prerequisites:** You must enable `enableDnsHostnames` and `enableDnsSupport` in the target VPC configuration settings.
*   **Overlapping Split-Horizon DNS:** You can create public and private hosted zones with the exact same domain name. Route 53 will resolve requests coming from inside the VPC to the private zone, while queries from the outside resolve to the public zone.

---

## ⚙️ DNS Records and Zone Apex Constraints

A hosted zone contains multiple records matching hostnames to targets.

### 🧩 Record Types
*   **A:** Maps hostname to IPv4 (e.g., `web.example.com` -> `198.51.100.12`).
*   **AAAA:** Maps hostname to IPv6 (e.g., `web.example.com` -> `2001:db8::1`).
*   **CNAME:** Maps hostname to another hostname (e.g., `api.example.com` -> `alb-dns-name.amazonaws.com`).
*   **NS (Name Server):** Defines the four DNS servers that respond to queries for the hosted zone.

###  Apex Zone Resolution: CNAME vs. Alias
*   **The Zone Apex Problem:** Standard DNS protocols (RFCs) dictate that a **CNAME** cannot coexist with other records (like NS or SOA) at the root of a domain (the **Zone Apex**, e.g., `example.com`). Thus, you cannot create a CNAME for the root domain.
*   **The Route 53 Alias Solution:** An **Alias record** is an AWS-specific DNS extension. It allows you to map the root domain/Zone Apex directly to AWS resources (ALBs, CloudFront, S3 website endpoints, etc.) by acting as an A/AAAA record underneath.
    *   *Automatic IP Management:* If the IP addresses of the backend AWS resource change, Route 53 automatically updates the record to resolve to the new IPs.
    *   *Free of Charge:* Alias queries are free.
    *   *No Manual TTL:* TTL is configured and managed dynamically by Route 53.
    *   *EC2 Restriction:* You cannot set an Alias record for a raw EC2 instance DNS name; EC2 instances require A records or CNAMES (for subdomains).

---

## 💰 Hosted Zone Cost Structure
*   **Hosted Zone Fee:** $0.50 per hosted zone per month.
*   **Domain Registration Fee:** Billed annually (e.g., $12 to $13 per year for a `.com` domain). Includes privacy protection to shield admin contact information from the WHOIS database.

*Read more in [[Reference Notes/3-12_aws_route53_dns.md#1. Route 53 DNS Core Concepts & Hosted Zones]]*
