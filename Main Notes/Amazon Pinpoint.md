---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: workload
domains:
  - "aws"
related_concepts:
  - "[[Amazon SES]]"
  - "[[Amazon SNS]]"
against:
  - "[[Amazon SES]]"
reference_guides:
  - "[[Reference Notes/3-20_other_services_whitepapers.md]]"
tags:
  - aws/pinpoint
  - integration/marketing
  - status/completed
---

# Amazon Pinpoint

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **Amazon Pinpoint**

---

## 🎯 Purpose (Why it is used)
Amazon Pinpoint is a managed, two-way marketing communication service. It is designed to engage customers across multiple channels—Email, SMS, Push Notification, and Voice—by managing user segments, building campaign templates, and analyzing user interaction events.

---

## ⚙️ Functionality (What it is doing)
*   **Multichannel Targeted Campaigns:** Executes campaigns across multiple communication channels (SMS, Email, Push notifications, Voice, In-app messaging).
*   **Dynamic User Segmentation:** Groups and segment users dynamically based on demographics, behaviors, attributes, or customer data patterns.
*   **Campaign Scheduling & Triggers:** Schedules marketing campaigns, sets rate limits, and triggers automated follow-ups based on user actions.
*   **Analytics Delivery:** Streams message delivery, bounce, and open metrics to SNS, Firehose, or S3.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Pinpoint sits as the customer engagement coordinator. Unlike SES or SNS which require external applications to schedule messages and track targets, Pinpoint manages the campaign logic, targeting database, and templates natively.

---

## 🧩 Problem Solver (What problem it solves)
Sending targeted campaigns requires complex database schemas to track subscriber lists, template designs, and scheduling states. Pinpoint solves this by offering user segmenting tools, scheduling engines, and templates in a managed service.

---

## 🟢 Operational Impact (What will happen with it operating)
Marketing teams manage campaign layouts and lists without engineering intervention. Deliverability metrics are monitored, and target users are engaged based on real-time behavior.

---

## 🔴 Failure Impact (What will happen without it)
Without Pinpoint, companies must integrate third-party marketing hubs or build complex campaign execution systems using raw databases, SES APIs, and custom chron job schedulers.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Amazon Pinpoint**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
