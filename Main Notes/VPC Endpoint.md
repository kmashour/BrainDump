---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: network
domains:
  - "aws"
related_concepts:
  - "[[Amazon VPC]]"
against:
  - "[[AWS NAT Gateway]]"
reference_guides:
  - "[[Reference Notes/3-9_aws_vpc_networking.md]]"
tags:
  - aws/networking
  - status/completed
---

# VPC Endpoint

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Reference Notes/3-Index - AWS|AWS]] > [[Amazon VPC]] > **VPC Endpoint**

---

## 🎯 Purpose (Why it is used)
A **VPC Endpoint** is a virtual device that enables private connection between an AWS VPC and supported AWS services (e.g., S3, DynamoDB, Systems Manager, KMS) or custom SaaS services. It ensures that traffic between the VPC and the designated service does not leave the AWS private network backbone, eliminating the need for an Internet Gateway, NAT Gateway, or VPN connection.

---

## ⚙️ Functionality (What it is doing)
- **AWS backbone Routing:** Encapsulates traffic destinating to public services and routes it internally within the AWS cloud fabric.
- **Gateway Endpoints:** Serves as a target in subnet route tables to route traffic to S3 and DynamoDB (free to configure).
- **Interface Endpoints (PrivateLink):** Provisions an Elastic Network Interface (ENI) with a private IP from the subnet pool, using local DNS mapping to resolve service endpoints to this ENI (hourly + per-GB charge).
- **Endpoint Policies:** Applies JSON authorization policies to restrict access to specific target resources or users.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Gateway Endpoints are configured at the Route Table level. Interface Endpoints attach directly to subnets as ENIs, requiring associated Security Groups. Both endpoint types bypass standard NAT gateways and IGWs. On-premises networks can access Interface Endpoints over VPN/Direct Connect, while accessing Gateway Endpoints from on-premises requires forward proxies.

---

## 🧩 Problem Solver (What problem it solves)
Accessing AWS services typically requires workloads to go over the public internet via NAT Gateways and Internet Gateways, which exposes outbound traffic, increases latency, and incurs heavy data transfer processing fees ($0.045/GB NAT Gateway fees). VPC Endpoints solve this by routing traffic privately, enhancing security compliance, and dramatically reducing costs (Gateway endpoints are free).

---

## 🟢 Operational Impact (What will happen with it operating)
Workloads communicate with AWS services privately and securely. Private DNS allows standard SDK commands (e.g., `aws s3 cp`) to function seamlessly without changing code, as queries resolve to the private endpoint. Endpoint policies block unauthorized data exfiltration.

---

## 🔴 Failure Impact (What will happen without it)
If a VPC Endpoint is deleted or its policy is misconfigured (e.g., blocking access to S3 or KMS), private EC2 instances will lose access to these services. Automated database backups, SSM agent check-ins, and key decryption requests will fail immediately.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **VPC Endpoint**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[VPC Endpoint]]
SORT file.name ASC
```
