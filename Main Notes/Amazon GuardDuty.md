---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: security
domains:
  - "aws"
related_concepts:
  - "[[aws]]"
  - "[[aws - KMS and Security Services]]"
against: []
reference_guides:
  - "[[Reference Notes/3-3_aws_kms_security.md]]"
tags:
  - aws/guardduty
  - status/completed
---

# Amazon GuardDuty

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **Amazon GuardDuty**

---

## 🎯 Purpose (Why it is used)
Amazon GuardDuty is a continuous security monitoring and threat detection service that analyzes log and event streams in an AWS account to identify malicious or unauthorized activity, compromised hosts, and security threats.

---

## ⚙️ Functionality (What it is doing)
- **Continuous Threat Discovery:** Leverages machine learning, anomaly detection, threat intelligence, and behavioral analytics to identify threats.
- **Log Stream Analysis:** Continuously ingests and processes metadata from three core data sources (without requiring agent installation or affecting performance):
  - *CloudTrail Management Logs:* Monitors for unauthorized API calls, console logins, and infrastructure changes.
  - *CloudTrail Data Logs:* Audits access patterns and object-level operations on S3 buckets.
  - *VPC Flow Logs:* Detects network anomalies, port scans, and unusual connection behavior.
  - *DNS Query Logs:* Identifies compromised instances communicating with Command & Control (C2) servers.
- **Optional Security Coverage:** Dynamically enables specialized threat detection for:
  - *EKS Audit Logs & Runtime Monitoring:* Audits Kubernetes control plane events and container activity.
  - *RDS Login Events:* Monitors for database brute-force attempts and anomalous logins.
  - *Lambda Network Activity:* Detects suspicious outbound traffic from serverless functions.
  - *EBS Volume Scanning:* Continuously monitors volume writes for malware signatures.
- **Cryptocurrency Finding Focus:** Includes dedicated detection patterns for cryptocurrency mining activity, which is a common indicator of compute instance compromise.
- **Alert Orchestration:** Automatically sends findings to AWS Security Hub and Amazon EventBridge. EventBridge rules can trigger automated remediations (via AWS Lambda) or send immediate operational alerts (via SNS).

---

## 🏛️ Architectural Context (How it fits in the architecture)
GuardDuty operates entirely out-of-band at the AWS control plane layer. It consumes log metadata directly from AWS backend services, meaning it has zero impact on network performance, compute resources, or application latency, and does not require agent installation.

---

## 🧩 Problem Solver (What problem it solves)
It detects sophisticated threats that traditional firewalls and IAM policies miss. For example, it identifies instances exfiltrating data via DNS queries (DNS tunneling), credentials compromised and accessed from an unusual geolocation, or rogue compute workloads running hidden cryptocurrency miners.

---

## 🟢 Operational Impact (What will happen with it operating)
Security teams receive real-time, categorized threat alerts (Low, Medium, High severity) with detailed contextual data (compromised resource, source IP, API call). Automated responses can instantly quarantine compromised EC2 instances by modifying their security groups.

---

## 🔴 Failure Impact (What will happen without it)
Without GuardDuty, stealthy account compromises, data exfiltration, or cryptojacking operations can remain undetected for months. This can result in massive financial data breaches, resource abuse bills, and prolonged exposure of sensitive infrastructure.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Amazon GuardDuty**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
