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
*   **Cognito User Pools (CUP - Authentication Directory):** A serverless directory database of users. Manages signup, signin, email/phone verifications, password resets, and MFA. Emits JSON Web Tokens (JWTs) (ID, Access, and Refresh tokens). Integrates natively with API Gateway and Application Load Balancer (ALB) to validate user tokens before routing traffic to backend compute.
*   **Cognito Identity Pools (Federated Identity - Authorization):** Exchanges authentication tokens (from CUP, social sign-ins, or OIDC/SAML) for temporary AWS credentials (via AWS Security Token Service / STS). This allows mobile/web clients to make direct API calls to AWS resources (such as writing to a private S3 folder or querying a database table) without routing through a custom backend API.
*   **Fine-Grained Row-Level Security:** Secures DynamoDB tables for multi-tenant applications by applying IAM policies with conditions that compare the `dynamodb:LeadingKeys` partition key against the user's validated Cognito Identity ID (`cognito-identity.amazonaws.com:sub`). This guarantees that users can only read or write their own rows of data.

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
