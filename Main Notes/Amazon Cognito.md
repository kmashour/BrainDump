---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[API Gateway]]"
  - "[[AWS Lambda]]"
  - "[[aws - IAM Role]]"
  - "[[Amazon DynamoDB]]"
against: []
reference_guides:
  - "[[Reference Notes/3-18_serverless.md]]"
tags:
  - aws/cognito
  - status/completed
---

# Amazon Cognito

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Category > **Amazon Cognito**

---

## 🎯 Purpose (Why it is used)
Amazon Cognito is a serverless identity management service that provides user signup, signin, and access control for web and mobile applications. It secures application interfaces by managing identities outside AWS accounts.

---

## ⚙️ Functionality (What it is doing)
*   **User Directory (User Pools):** Stores application user credentials, managing signup, email/phone verifications, password resets, and MFA.
*   **Federated Identity (Identity Pools):** Exchanges external authentication tokens (Google, Facebook, CUP) for temporary AWS credentials.
*   **ALB & API Gateway Integration:** Intercepts client connections to validate tokens before traffic is forwarded to backends.
*   **Fine-Grained Authorization:** Attaches dynamic IAM policies to users to restrict AWS API access down to specific resource folders or rows.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Cognito sits at the auth boundary of serverless mobile and web frontends. Clients fetch tokens from Cognito User Pools, which are verified by API Gateway, or exchanged through Identity Pools to securely write to S3 buckets or DynamoDB directly.

---

## 🧩 Problem Solver (What problem it solves)
Without Cognito, development teams must build and maintain user database tables, implement cryptographic password salting and hashes, write session management tokens, manage OAuth integrations, and build custom AWS STS federation layers. Cognito manages this identity flow securely at scale.

---

## 🟢 Operational Impact (What will happen with it operating)
Users authenticate securely against OAuth-compliant endpoints. Tokens are verified automatically by traffic load balancers or gateways, offloading authentication validation logic from application compute instances entirely.

---

## 🔴 Failure Impact (What will happen without it)
If the Amazon Cognito identity service experiences outages:
*   Users cannot sign up, sign in, or refresh session tokens, causing lockouts.
*   API Gateway and ALBs fail token validations, returning authentication error messages.
*   Mobile clients cannot fetch temporary credentials, blocking direct S3 or DynamoDB file transfers.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Amazon Cognito**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
