---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: security
domains:
  - "aws"
related_concepts:
  - "[[aws]]"
  - "[[AWS Shield]]"
  - "[[aws - KMS and Security Services]]"
against:
  - "[[Network Access Control List]]"
reference_guides:
  - "[[Reference Notes/3-3_aws_kms_security.md]]"
tags:
  - aws/waf
  - status/completed
---

# AWS WAF

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **AWS WAF**

---

## 🎯 Purpose (Why it is used)
AWS WAF (Web Application Firewall) is a Layer 7 firewall service that protects web applications and APIs from common web exploits, malicious bots, and application-layer floods that can affect availability, compromise security, or consume excessive resources.

---

## ⚙️ Functionality (What it is doing)
- **Layer 7 Filtering:** Inspects HTTP and HTTPS request payloads (headers, body, URI strings, query parameters, cookies) at the application layer.
- **Service Deployment Targets:** Integrates natively with Application Load Balancer (ALB), Amazon API Gateway, Amazon CloudFront, AWS AppSync GraphQL APIs, and Amazon Cognito User Pools.
- **Rule Configurations:** Uses Web Access Control Lists (Web ACLs) containing custom or AWS Managed Rules:
  - *IP Sets:* Filters traffic based on IP address blocks (up to 10,000 IPs per set).
  - *HTTP Payload Inspections:* Evaluates SQL injection (SQLi) and Cross-Site Scripting (XSS) patterns.
  - *Size Constraints:* Blocks requests exceeding predefined size limits (e.g., payloads over 2MB).
  - *Geo-Matching:* Restricts or redirects traffic based on country codes.
- **Rate-Based Mitigation:** Counts request volumes from individual IP addresses over sliding windows to block brute-force or application-layer DDoS attacks.
- **Reusability:** Groups multiple rules into Rule Groups that can be attached to multiple Web ACLs.
- **Global vs. Regional Scope:** Web ACLs are regional resources, except when deployed on CloudFront distributions, where they are defined globally in `us-east-1`.

---

## 🏛️ Architectural Context (How it fits in the architecture)
AWS WAF is deployed at the edge or entry point of the web architecture. It intercepts incoming HTTP/HTTPS requests before they reach downstream web servers or serverless backend systems. Because WAF requires Layer 7 protocol parsing, it cannot be deployed on a Network Load Balancer (NLB), which operates at Layer 4 (TCP/UDP).

---

## 🧩 Problem Solver (What problem it solves)
WAF protects applications from OWASP Top 10 vulnerabilities (SQLi, XSS, command injection) and prevents bad bots from crawling websites or performing brute-force logins. It also addresses the limitation of ALBs lacking fixed IPs by allowing a design where an AWS Global Accelerator (providing fixed IPs) fronts the ALB, and WAF is attached to the ALB to inspect the traffic.

---

## 🟢 Operational Impact (What will happen with it operating)
Legitimate HTTP traffic is passed to backend systems with minimal latency overhead. Web exploit attempts and unauthorized bots are dropped at the edge with an HTTP 403 Forbidden response. Security operations teams analyze blocked traffic patterns and refine rule parameters to minimize false positives.

---

## 🔴 Failure Impact (What will happen without it)
Without WAF, web applications are directly exposed to application-layer attacks. Attackers can exploit software vulnerabilities to exfiltrate database contents (SQLi), run unauthorized scripts on user browsers (XSS), or overwhelm application servers using Layer 7 request floods, resulting in database exhaustion and service outages.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **AWS WAF**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
