---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[Amazon S3]]"
  - "[[Amazon Cognito]]"
  - "[[API Gateway]]"
  - "[[AWS Lambda]]"
against:
  - "[[AWS CloudFormation]]"
reference_guides:
  - "[[Reference Notes/3-20_other_services_whitepapers.md]]"
tags:
  - aws/amplify
  - deployment/application-framework
  - status/completed
---

# AWS Amplify

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **AWS Amplify**

---

## 🎯 Purpose (Why it is used)
AWS Amplify is an application development platform that simplifies building mobile and web applications on AWS. It serves as a declarative, unified framework that manages backend provisioning, hosting, and client integration (often described as "Elastic Beanstalk for mobile and web developers").

---

## ⚙️ Functionality (What it is doing)
*   **Backend Automation (Mobile/Web App Fabric):** Natively provisions and orchestrates backend resources (Cognito, S3, AppSync, API Gateway, DynamoDB, Lambda, Lex, SageMaker) into a single, cohesive application fabric.
*   **CLI Build Integrations:** Integrates CLI-driven workflows to initialize project templates, configuration parameters, and connect frontend client applications directly to AWS.
*   **Frontend Deployment:** Offers managed hosting with built-in CI/CD pipelines, automating frontend builds from repositories and deploying web/mobile host assets to CloudFront.
*   **Frontend Libraries:** Integrates standard platform wrappers (React, Vue, iOS, Android, Flutter) to access backend APIs and data stores using simple SDK calls.
*   **Analytics & Notifications:** Monitors user engagement and coordinates push notifications.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Amplify sits as the developer control layer. Developers use the Amplify CLI to generate cloud resources, and client applications use the Amplify SDK to interact with the backend services.

---

## 🧩 Problem Solver (What problem it solves)
Configuring Cognito authentication, connecting database backends, building REST/GraphQL endpoints, and setting up hosting environments manually is slow and complex. Amplify solves this by providing a single, pre-configured framework for app developers.

---

## 🟢 Operational Impact (What will happen with it operating)
Development velocity is maximized, and backends are provisioned automatically. CI/CD pipelines build and deploy frontend changes automatically upon code commit.

---

## 🔴 Failure Impact (What will happen without it)
Without Amplify, developers must manually build, configure, and maintain individual Cognito, API Gateway, S3, and CloudFront resources using IaC tools like CloudFormation or Terraform.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **AWS Amplify**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
