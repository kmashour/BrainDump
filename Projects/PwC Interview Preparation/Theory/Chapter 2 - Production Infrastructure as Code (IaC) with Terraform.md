---
obsidianUIMode: preview
class: project-note
tier: project
domains:
  - "aws"
  - "storage"
concepts_referenced:
  - "[[aws]]"
  - "[[terraform]]"
difficulty: advanced
status: completed
---

# Chapter 2: Production Infrastructure as Code (IaC) with Terraform

**Breadcrumbs:** [[Projects/PwC Interview Preparation/Plan - DevOps Interview Roadmap|DevOps Interview Roadmap]] > Theory > **Chapter 2: IaC with Terraform**

---

## 🔒 1. State File Architecture, KMS Encryption, & DynamoDB Concurrency Locking

In enterprise DevOps setups, Terraform state is treated as a highly sensitive, secure database.

### A. State Security & Envelope Encryption
The state file (`terraform.tfstate`) stores resource details (like DB master passwords or private TLS keys) in plain text.
*   **SSE-KMS Encryption at Rest:** Store state in a dedicated S3 bucket. Enforce S3 Server-Side Encryption using an AWS KMS Customer Managed Key (CMK) (`aws:kms`) rather than standard Amazon-managed keys (`AES256`). This allows you to audit state access audits in CloudTrail logs.
*   **S3 Bucket Policies:** Enforce SSL connection transport via bucket policy `aws:SecureTransport`. Block public read access completely using S3 Public Access Block.

### B. DynamoDB Concurrency Locking Mechanics
*   **The Problem:** Parallel runs (e.g., developers running local applies while a CI pipeline triggers) read the state file, apply mutations, and overwrite each other's changes, leading to corruption.
*   **The Locking Algorithm:**
    1.  The DynamoDB table must have a partition key named exactly `LockID` of type `String`.
    2.  When running any write command (`init`, `plan`, `apply`, `destroy`), Terraform attempts to write an item to this table with the `LockID` matching the state key path.
    3.  The write query utilizes conditional expressions to fail if a record already exists for that `LockID`.
    4.  If the write succeeds, the lock is acquired, and metadata (run ID, operator name, timestamp) is recorded.
    5.  Subsequent executions will fail with a `LockInfo` output.

---

## 🏛️ 2. Multi-Environment State Isolation: Workspaces vs. Directory Structures

When designing multi-environment (Staging, Production) infrastructure pipelines, compare these isolation patterns:

```
WORKSPACE ISOLATION (Single Directory, Shared Code)
  VPC Root/
  ├── main.tf
  ├── variables.tf
  └── tfstate (S3 Bucket)
      ├── env:/staging/terraform.tfstate
      └── env:/production/terraform.tfstate

DIRECTORY-BASED ISOLATION (Separated Code and States)
  VPC Root/
  ├── modules/
  │   └── vpc/
  ├── staging/
  │   ├── main.tf (Calls VPC module, backend pointing to staging state)
  │   └── terraform.tfstate (Staging State)
  └── production/
      ├── main.tf (Calls VPC module, backend pointing to prod state)
      └── terraform.tfstate (Production State)
```

### A. Terraform Workspaces
*   **Mechanism:** Runs in a single folder. Switched via `terraform workspace select <name>`. State files are separated automatically inside the S3 backend prefix path.
*   **Risk:** Highly dangerous for production. A developer can accidentally run `terraform destroy` on production if they fail to check their active workspace. Code logic blocks must use workspace interpolations (`count = terraform.workspace == "prod" ? 3 : 1`), which increases syntax complexity and error rates.

### B. Directory-Based Structure (Recommended for Production)
*   **Mechanism:** Staging and Production have completely separate directories with independent configuration files, backend setups, and variables, calling shared modules.
*   **Security Isolation:** The IAM role credentials used in the staging CI pipeline can be completely restricted from accessing the production directory or production S3 bucket. A mistake in staging code cannot affect production state.

---

## ⚙️ 3. Resource Lifecycle Customizations

Manage how Terraform mutates resources using lifecycle blocks:

*   **`prevent_destroy`:** Prevents accidental deletion of persistent resources:
    ```hcl
    resource "aws_db_instance" "prod_db" {
      # ...
      lifecycle {
        prevent_destroy = true
      }
    }
    ```
*   **`create_before_destroy`:** Modifies Terraform's update sequence. By default, Terraform destroys the old resource *before* launching the replacement. Setting this true forces Terraform to create the replacement first. This is critical for zero-downtime replacements (e.g. provisioning a new EC2 Launch Template instance before terminating the old one).
*   **`ignore_changes`:** Blocks state reconciliation loops when resources are modified externally (e.g. AWS Auto Scaling group modifying `desired_capacity`, or container security platforms modifying tags).
    ```hcl
    lifecycle {
      ignore_changes = [tags, desired_capacity]
    }
    ```

---

## 🔄 4. Infrastructure Drift Detection & GitOps Remediation

*   **What is Drift?** Configuration drift occurs when the actual state of cloud resources deviates from the declared configuration (e.g. an operator manually opens port 22 in a security group via the AWS Console).
*   **Automated Detection:** Run a scheduled CI job (e.g. daily cron) executing:
    `terraform plan -detailed-exitcode`
    *   *Exit Code 0:* Succeeded, no changes.
    *   *Exit Code 1:* Succeeded, but changes/drift detected.
    *   *Exit Code 2:* Command failed with an error.
*   **Remediation Pathways:**
    1.  **Overwriting manual changes:** Run `terraform apply` in the CI pipeline to reconcile the cloud infrastructure back to the code definition.
    2.  **Importing valid manual changes:** If the manual change was approved, add the resource block to the configuration and run `terraform import` (or use the declarative `import` block in Terraform 1.5+) to sync the state.

*See details on state and backends in [[Reference Notes/10-1_terraform_foundations_and_state]] and variables in [[Reference Notes/10-2_variables_types_and_expressions]].*
