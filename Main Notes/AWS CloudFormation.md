---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
related_concepts:
  - "[[aws]]"
  - "[[aws - EC2 Instance]]"
  - "[[Amazon VPC]]"
against:
  - "[[terraform]]"
reference_guides:
  - "[[Reference Notes/3-20_other_services_whitepapers.md]]"
tags:
  - aws/cloudformation
  - deployment/iac
  - status/completed
---

# AWS CloudFormation

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **AWS CloudFormation**

---

## 🎯 Purpose (Why it is used)
AWS CloudFormation is a managed service designed for Infrastructure as Code (IaC). It enables developers and systems administrators to declare and provision an entire suite of AWS infrastructure resources in a safe, repeatable, and automated manner using declarative JSON or YAML templates.

---

## ⚙️ Functionality (What it is doing)
*   **Declarative Infrastructure:** Outlines resource configurations, dependencies, and parameters in a JSON or YAML template file, which CloudFormation builds automatically.
*   **Dependency Management:** Resolves the correct order of resource creation and destruction based on logical references.
*   **Change Sets:** Previews changes to stacks to identify additions, modifications, and resource replacements before execution.
    *   *Replacement Warning:* Certain property modifications trigger resource recreation (`Replacement: True`), which deletes the old physical resource, resulting in downtime and ephemeral data loss.
*   **Tag Propagation:** Stack-level tags automatically propagate to all supported resources provisioned within the stack, simplifying cost allocation.
*   **Service Role Delegation:** Uses dedicated IAM service roles (via `iam:PassRole`) to delegate permissions to CloudFormation to create, update, or delete stack resources on behalf of the invoking user.

---

## 🏛️ Architectural Context (How it fits in the architecture)
CloudFormation acts as the deployment control plane for AWS workloads. Templates are stored in S3, and CloudFormation interprets them to spin up EC2 hosts, VPC subnets, security rules, and databases.

---

## 🧩 Problem Solver (What problem it solves)
Configuring cloud infrastructure manually via the Web Console is error-prone, hard to track, and difficult to repeat across environments (e.g. dev, staging, prod). CloudFormation solves this by defining infrastructure as version-controlled code.

---

## 🟢 Operational Impact (What will happen with it operating)
Deployments are consistent, repeatable, and fast. Changes to infrastructure are audit-logged and peer-reviewed through code commits. Stacks can be destroyed and recreated on-demand to save costs.

---

## 🔴 Failure Impact (What will happen without it)
Without CloudFormation (or a similar tool like Terraform), operations teams must write custom scripting API wrappers or manually click through console portals to provision and scale environments.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **AWS CloudFormation**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
