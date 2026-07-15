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
difficulty: intermediate
status: completed
---

# Chapter 2: Production Infrastructure as Code (IaC) with Terraform

**Breadcrumbs:** [[Projects/PwC Interview Preparation/Plan - DevOps Interview Roadmap|DevOps Interview Roadmap]] > Theory > **Chapter 2: IaC with Terraform**

---

## 🔒 1. State File Security & State Concurrency Locking

In an enterprise environment, the Terraform state file is a highly sensitive asset and a single point of failure.

### A. State File Security (Encryption at Rest & Transit)
The state file (`terraform.tfstate`) contains resource attributes in plain text, including sensitive values like database passwords, private keys, and API tokens.
*   **Encrypted S3 Backend:** Store the state file in an Amazon S3 bucket with **Default Encryption** (using AWS KMS customer-managed keys `aws/s3`) and a bucket policy enforcing **HTTPS-only** access (`aws:SecureTransport`).
*   **Restricted Access:** Apply least-privilege IAM policies, limiting state file read/write permissions strictly to the CI/CD deployment roles.

### B. Concurrency Locking via DynamoDB
*   **The Problem:** If two developers or two parallel CI/CD runners execute `terraform apply` concurrently, they will read the same state, attempt conflicting writes, and corrupt the state file.
*   **The Solution:** Use a DynamoDB Table for distributed locking:
    1.  Create a DynamoDB table with a primary key attribute named exactly `LockID` of type `String`.
    2.  When a run begins, Terraform acquires a lock by writing an entry containing the run metadata to the DynamoDB table.
    3.  If another run attempts to start, it reads the DynamoDB record, sees the active lock, outputs a `ResourceLocked` error, and terminates.
    4.  Upon successful completion (or clean failure), the lock record is deleted.

```hcl
# backend-config.tf
terraform {
  backend "s3" {
    bucket         = "pwc-production-tfstate"
    key            = "vpc-infrastructure/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "pwc-terraform-locks" # Enforces locking
    encrypt        = true                  # Enforces Server-Side Encryption (SSE)
  }
}
```

---

## 🏛️ 2. Terraform Code Modularity: Custom Modules vs. Flat Code

### A. The Monolithic Trap
Writing all resources in a single flat directory (`main.tf`, `variables.tf`) makes the code unmaintainable and highly risky. A tiny error in one resource can cause Terraform to rebuild unrelated critical resources.

### B. Module Segmentation Best Practices
*   **Decoupled State files:** Break infrastructure down into separate states with independent lifecycles:
    *   *Network Layer:* VPC, subnets, NAT gateways, route tables (changes rarely).
    *   *Database Layer:* Aurora, RDS clusters, Security Groups (changes occasionally).
    *   *Application Layer:* ECS services, EKS configurations, Route 53 records (changes frequently).
*   **Reusable Custom Modules:** Standardize infrastructure patterns. For example, a custom VPC module can be written once and referenced across staging and production environments, enforcing standard tags and subnet division:
    ```hcl
    module "vpc" {
      source = "git::git@github.com:pwc/tf-modules.git//vpc?ref=v1.2.0" # Version-pinned module
      vpc_cidr = "10.0.0.0/16"
      environment = "production"
    }
    ```

---

## ⚙️ 3. Advanced Lifecycle Hooks & Security as Code (SaC)

PwC projects require strict operational compliance. Use lifecycle configurations to automate safeguards:

1.  **`prevent_destroy = true`:**
    Place this inside database instances, primary DNS hosted zones, or EFS volume resources. If a developer runs `terraform destroy` or makes a code change that triggers resource replacement, Terraform aborts the run:
    ```hcl
    lifecycle {
      prevent_destroy = true
    }
    ```
2.  **`create_before_destroy = true`:**
    Useful when updating Launch Templates, Auto Scaling groups, or Security Groups. By default, Terraform destroys the old resource before building the new one, causing application downtime. This flag forces Terraform to instantiate the replacement resource *first*, update load balancer targets, and then delete the old instance.
3.  **`ignore_changes`:**
    Used when resources are altered dynamically outside Terraform (e.g. AWS Auto Scaling adjusting the `desired_capacity` of a group, or security tools applying temporary audit tags). Prevents Terraform from reverting these live changes during subsequent applies:
    ```hcl
    lifecycle {
      ignore_changes = [tags, desired_capacity]
    }
    ```
4.  **Enforcing Resource Tagging Compliance:**
    Standardize cost allocation and audit compliance by enforcing default tags at the provider level:
    ```hcl
    provider "aws" {
      region = "us-east-1"
      default_tags {
        tags = {
          Environment = var.environment
          Owner       = "PwC-DevOps-Team"
          ManagedBy   = "Terraform"
          ProjectID   = "PWC-ETIC-045"
        }
      }
    }
    ```

*See similar modular variables and S3 state templates in [[Reference Notes/10-1_terraform_foundations_and_state]] and [[Reference Notes/10-2_variables_types_and_expressions]].*
