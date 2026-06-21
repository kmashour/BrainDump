---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[terraform]]"
sub_type: core-concept
source_type: documentation
source_url: "https://developer.hashicorp.com/terraform/language/state"
author: "HashiCorp Docs"
course_title: "Terraform Language: State"
tags:
  - terraform/state
  - terraform/deep-dive
---

# terraform - State and Backend Locking

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[terraform]] > **State and Backend Locking**

---

## 📑 State Architecture & Concurrency Rules

The state database is central to Terraform's execution lifecycle.

### 1. State Database File (`.tfstate`)
Terraform maps HCL resource declarations to real-world cloud objects inside the JSON-formatted state file. It acts as a cache, tracking resource attributes and dependencies.
*   **Secret Exposure:** The state file stores database passwords, private keys, and configuration secrets in plaintext. Commit rules must exclude state files from version control (`.gitignore`), storing them securely in encrypted remote buckets instead.

### 2. S3 Remote Backend & DynamoDB Locks
In team environments, local state files cause write conflicts and configuration drift. The industry standard is to configure a remote S3 backend with DynamoDB locking:
*   **S3 Backend:** Stores the state file remotely. Enables versioning to support rollbacks and encryption at rest.
*   **DynamoDB Locking:** When a developer runs a plan or apply, Terraform creates a locking record in DynamoDB. Concurrent runs detect this lock and exit immediately, preventing write conflicts and corruption.

*Read more in [[Reference Notes/10-1_terraform_foundations_and_state.md#3-remote-state-management-dynamodb-concurrency-locking]]*
