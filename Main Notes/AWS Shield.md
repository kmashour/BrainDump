---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: security
domains:
  - "aws"
related_concepts:
  - "[[aws]]"
  - "[[AWS WAF]]"
  - "[[aws - KMS and Security Services]]"
against:
  - "[[AWS WAF]]"
reference_guides:
  - "[[Reference Notes/3-3_aws_kms_security.md]]"
tags:
  - aws/shield
  - status/completed
---

# AWS Shield

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **AWS Shield**

---

## 🎯 Purpose (Why it is used)
AWS Shield is a managed Distributed Denial of Service (DDoS) protection service that safeguards applications running on AWS. It provides continuous detection and automatic inline mitigations to prevent network and application-layer downtime.

---

## ⚙️ Functionality (What it is doing)
- **Shield Standard (Free/Automatic):** Defends all AWS customers automatically at no additional cost against common Layer 3 and Layer 4 infrastructure attacks (such as SYN floods, UDP floods, and reflection attacks).
- **Shield Advanced (Subscription-Based):** Paid subscription ($3,000/month per organization) providing advanced DDoS detection and mitigation for:
  - Amazon Elastic Compute Cloud (EC2)
  - Elastic Load Balancing (ELB)
  - Amazon CloudFront
  - AWS Global Accelerator
  - Amazon Route 53
- **24/7 Response Team Access:** Provides 24/7 access to the AWS DDoS Response Team (DRT) / Shield Response Team (SRT) for manual mitigation support during active attacks.
- **Financial Charge Protection:** Reimburses customers for scaling and usage charges (e.g. EC2 scaling, ELB bandwidth) incurred due to DDoS traffic spikes.
- **Automated Layer 7 Mitigation:** Automatically generates, tests, and deploys AWS WAF rules in the customer's Web ACL to block Layer 7 application DDoS attacks (like HTTP floods) on-the-fly.

---

## 🏛️ Architectural Context (How it fits in the architecture)
AWS Shield is embedded directly in the AWS global network edge. It inspects incoming packets at the border routers before they reach VPC resources. Shield Advanced is configured at the resource level, mapping specific CloudFront distributions, Application Load Balancers, or Elastic IPs to active protection profiles.

---

## 🧩 Problem Solver (What problem it solves)
It prevents malicious actors from rendering applications unavailable by flooding network interfaces or web application servers with synthetic traffic. It eliminates the financial liability of cloud auto-scaling during a DDoS attack (which would otherwise cost thousands of dollars as backend EC2 instances scale out to handle the attack traffic).

---

## 🟢 Operational Impact (What will happen with it operating)
Layer 3/4 infrastructure floods are automatically absorbed and scrubbed at the AWS border network with zero impact on application latency. During a Layer 7 flood, Shield Advanced automatically implements WAF rules to drop malicious request shapes, keeping the backend application responsive for legitimate users.

---

## 🔴 Failure Impact (What will happen without it)
Without Shield, massive Layer 3/4 volume floods (exceeding hundreds of gigabits per second) will saturate the target's network interfaces, rendering all application endpoints completely unreachable. Sophisticated application-layer floods will bypass default network defenses, exhausting database connection pools and web server CPU, causing severe downtime.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **AWS Shield**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
