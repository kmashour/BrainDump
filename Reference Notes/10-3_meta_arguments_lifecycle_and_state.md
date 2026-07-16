# Module 10-3: Meta-Arguments, Lifecycle Control & State Ops

This module details Terraform meta-arguments (`count`, `for_each`, `depends_on`), lifecycle rules (`create_before_destroy`, `prevent_destroy`, `ignore_changes`), provisioner behaviors, state manipulation commands, and declarative import workflows.

---

## 🗺️ Cognitive Map: How to Think About the Flow of Knowledge

To manage resource scaling and safe state transformations, structure your orchestration logic around explicit resource constraints:

```mermaid
graph TD
    subgraph Iteration["1. Loop Control (Meta-Arguments)"]
        Count["count (simple duplicates / conditional toggle)"]
        ForEach["for_each (key-value mapped resources)"]
        DependsOn["depends_on (explicit execution order)"]
    end

    subgraph SafetyGates["2. Lifecycle Policy Rules"]
        CBD["create_before_destroy (zero downtime)"]
        PD["prevent_destroy (stop accidental deletion)"]
        IC["ignore_changes (ignore outside updates)"]
    end

    subgraph StateOps["3. State Transformations & Import"]
        StateMv["terraform state mv (rename boundaries)"]
        ImportBlock["import { ... } (declarative ingestion)"]
    end

    Iteration --> SafetyGates
    SafetyGates --> StateOps
```

1. **Step 1: Loop Control (Section 1):** Iterate collections safely to avoid index shifts.
2. **Step 2: Resource Lifecycle Rules (Section 2):** Safeguard production databases and enable zero-downtime upgrades.
3. **Step 3: State Ingestion (Section 3):** Import running external assets into HCL declarations cleanly.

---

## 1. Loop Control: `count` vs. `for_each` & `depends_on`

Terraform provides meta-arguments to change resource scaling and ordering.

### A. The Index Shifting Problem with `count`
`count` uses integer indexes (0, 1, 2) to provision resources.
```hcl
# If users = ["alice", "bob", "charlie"]
resource "aws_iam_user" "users" {
  count = length(var.users)
  name  = var.users[count.index]
}
```
*   **The Problem:** If you remove `"bob"` (index 1) from the middle of the list, Alice remains at index 0, but Charlie shifts from index 2 to index 1.
*   **The Result:** Terraform sees this as a rename/replacement of index 1 (updating Bob to Charlie) and a deletion of index 2. This triggers unnecessary deletion and recreation of Charlie, causing downtime or policy detachments.

### B. Map-Based Iteration with `for_each`
`for_each` uses map keys or sets, binding resource identities to unique string keys rather than integer indexes:
```hcl
resource "aws_iam_user" "users" {
  for_each = toset(var.users)
  name     = each.value
}
```
*   **The Solution:** Removing `"bob"` only deletes the resource identified by the key `aws_iam_user.users["bob"]`. Charlie's key `aws_iam_user.users["charlie"]` remains completely untouched, preventing index shifts.
*   **Loop Variables:** Inside a `for_each` block, access elements using `each.key` and `each.value`. For sets, key and value are identical. For maps, key is the map key and value is the map value.

### C. Trade-offs: Count vs. For_Each
*   **Use `count` when:**
    1.  Provisioning a conditional resource (toggle switch: `count = var.create_resource ? 1 : 0`).
    2.  Scaling identical, homogeneous resources where index ordering does not matter.
*   **Use `for_each` when:**
    1.  Creating heterogeneous resources based on complex lists, sets, or maps.
    2.  Resources have unique identifiers and must survive list sorting or middle deletions.

### D. Explicit Ordering with `depends_on`
Terraform automatically infers dependencies when a resource references another's attribute (implicit dependency).
*   **Explicit Dependency:** When Terraform cannot detect a dependency implicitly (e.g. an EC2 instance depends on an IAM policy being fully attached to its role to run startup scripts), define `depends_on`:
    ```hcl
    resource "aws_iam_role_policy_attachment" "admin_attach" {
      role       = aws_iam_role.web_role.name
      policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
    }

    resource "aws_instance" "web" {
      ami           = var.ami_id
      instance_type = "t3.micro"
      depends_on    = [aws_iam_role_policy_attachment.admin_attach]
    }
    ```
*   **Trade-off:** Use `depends_on` sparingly. Overusing it forces serial execution, slows down plan/apply runs, and masks cyclical dependency bugs.

---

## 2. Deep-Intuition (AARF) Breakdowns: Lifecycle Rules & Imports

### A. Zero-Downtime Swaps via `create_before_destroy`
#### Deep-Intuition (AARF) Breakdown:
1. **The Answer (Core Pattern):** Declare a `lifecycle` block setting `create_before_destroy = true` within resources that must be swapped without traffic loss (like Auto Scaling Groups or Launch Templates):
    ```hcl
    resource "aws_launch_template" "asg_template" {
      name_prefix   = "web-template-"
      image_id      = var.ami_id
      instance_type = "t3.micro"

      lifecycle {
        create_before_destroy = true
      }
    }
    ```
2. **The Assumptions (Context):** The resource name must use `name_prefix` instead of a static `name`. If the name is static, creating the new instance before destroying the old one will trigger a name collision error at the cloud API side.
3. **The Rationale (Why):** By default, Terraform's replacement pattern is **destroy-then-create**. If you modify a resource that requires replacement (like an AMI change), Terraform deletes the existing resource, causing downtime while the new instance is provisioned and bootstrapped. `create_before_destroy` forces Terraform to provision the new resource first, verify it is healthy, and only then terminate the old instance.
4. **The Failure Loop (What if not):** If lifecycle swaps are left to default, updating Launch Templates or AMIs terminates running servers immediately. The application is completely offline until the new instances spin up, download dependencies, and pass health probes, causing production outages.
5. **Alternative Case (When to use 'if not'):** For stateful resources that cannot co-exist concurrently (like mounting a specific single-attachment EBS volume to an EC2 instance), destroy-then-create is mandatory.

### B. Critical Protections: `prevent_destroy` & `ignore_changes`
*   **`prevent_destroy`**: Protect critical resources (like databases or storage buckets) from accidental deletions.
    ```hcl
    resource "aws_db_instance" "prod_db" {
      allocated_storage = 20
      engine            = "postgres"
      instance_class    = "db.t3.medium"
      
      lifecycle {
        prevent_destroy = true
      }
    }
    ```
    If a developer runs `terraform destroy` or modifies an attribute requiring replacement, Terraform immediately halts compilation with an error, protecting the database.
*   **`ignore_changes`**: Ignore attributes modified outside of Terraform (e.g. by auto-scaling policies, AWS console quick-fixes, or external agents).
    ```hcl
    resource "aws_instance" "web" {
      ami           = var.ami_id
      instance_type = "t3.micro"
      tags = {
        Name = "Web-Server"
      }

      lifecycle {
        ignore_changes = [
          tags, # Ignores tag edits made via AWS Console or external automation
          instance_type # Ignores instance size changes from external schedulers
        ]
      }
    }
    ```

---

## 3. Declarative Import Blocks (Terraform v1.5+)

#### Deep-Intuition (AARF) Breakdown:
1. **The Answer (Core Pattern):** Declare `import` blocks in code to ingest running resources, and use `-generate-config-out` during plan execution to auto-write the HCL declarations.
    ```hcl
    # import.tf
    import {
      to = aws_s3_bucket.imported_bucket
      id = "my-pre-existing-s3-bucket-name"
    }
    ```
    Execution command:
    ```bash
    terraform plan -generate-config-out=generated_resources.tf
    ```
2. **The Assumptions (Context):** The target ID matches the cloud resource key identifier (e.g. S3 bucket name, VPC ID, or instance ID).
3. **The Rationale (Why):** Legacy imports (`terraform import` CLI command) were imperative and required developers to manually write matching HCL resource blocks first, then execute a CLI command that modified the state file directly. If the written HCL did not match the cloud configuration, subsequent plans would show massive updates. Declarative `import` blocks compile import instructions directly into the code. The `-generate-config-out` flag tells Terraform to inspect the cloud resource, generate correct HCL code, and write it to a file, preventing human mapping errors and ensuring the import is reviewable in pull requests.
4. **The Failure Loop (What if not):** If legacy command-line imports are used, developers bypass code reviews. If multiple imports are executed, the state file is mutated directly without trackable commits, increasing the risk of state corruption.
5. **Alternative Case (When to use 'if not'):** For massive scale-out import automation pipelines where configuration is generated programmatically from CMDB systems, CLI-based imports inside scripts remain a viable pattern.
