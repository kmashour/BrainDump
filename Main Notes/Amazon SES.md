---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: workload
domains:
  - "aws"
related_concepts:
  - "[[Amazon SNS]]"
  - "[[Amazon Pinpoint]]"
against:
  - "[[Amazon Pinpoint]]"
reference_guides:
  - "[[Reference Notes/3-20_other_services_whitepapers.md]]"
tags:
  - aws/ses
  - integration/email
  - status/completed
---

# Amazon SES

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **Amazon SES**

---

## 🎯 Purpose (Why it is used)
Amazon Simple Email Service (SES) is a highly scalable, managed email sending and receiving service designed for developers and businesses. It serves as a cost-effective utility to send transactional alerts, notifications, bulk newsletter updates, and marketing materials securely.

---

## ⚙️ Functionality (What it is doing)
*   **Outbound Delivery:** Sends emails via standard SMTP protocols or native AWS API calls.
*   **Inbound Receiving:** Accepts incoming emails, saving raw data in S3 or triggering Lambda functions to process message bodies.
*   **Sender Verification:** Implements DKIM (DomainKeys Identified Mail) and SPF (Sender Policy Framework) to authenticate domains.
*   **Deliverability Auditing:** Tracks deliveries, bounces, complaint rates, and spam feedback loop results.

---

## 🏛️ Architectural Context (How it fits in the architecture)
SES serves as the integration endpoint for email communications. Application backend handlers (e.g. Lambdas or ECS microservices) query the SES endpoint to generate emails dynamically.

---

## 🧩 Problem Solver (What problem it solves)
Running self-managed SMTP servers involves managing IP warm-up protocols, configuring DNS spam preventions, and resolving blacklists. SES solves this by offering vetted IP pools and reputation metrics.

---

## 🟢 Operational Impact (What will happen with it operating)
Email delivery is handled asynchronously, and domain deliverability ratings are tracked. Automated bounce and complaint notifications routes to SQS or Lambda to purge bad addresses.

---

## 🔴 Failure Impact (What will happen without it)
Without SES, applications must connect to external third-party mail APIs or self-manage complex mail servers, exposing them to scaling bottlenecks and domain spam blocking risks.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Amazon SES**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
