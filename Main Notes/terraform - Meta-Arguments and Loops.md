---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[terraform]]"
sub_type: core-concept
source_type: documentation
source_url: "https://developer.hashicorp.com/terraform/language/meta-arguments/for_each"
author: "HashiCorp Docs"
course_title: "Terraform Language: Meta-Arguments"
tags:
  - terraform/loops
  - terraform/deep-dive
---

# terraform - Meta-Arguments and Loops

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[terraform]] > **Meta-Arguments and Loops**

---

## 📑 HCL Looping Mechanisms: count vs. for_each

Loop control allows provisioning multiple resources from a single block definition.

### 1. The Index Shifting Risk of `count`
`count` provisions resources based on an integer list length, assigning numeric index IDs (`resource.name[0]`, `resource.name[1]`). 
*   **The Bug:** If you delete a resource from the middle of the source list, the list length changes and all subsequent resource indexes shift down. Terraform treats this as a rename/replacement of all shifted resources, causing unnecessary downtime and resource recreation.

### 2. Key-Based Loop Isolation via `for_each`
`for_each` takes a map or set, binding resource identity to string-based map keys (`resource.name["bob"]`, `resource.name["charlie"]`). Removing an element deletes *only* the specific keyed resource, leaving all other resources completely untouched.

### 3. Inline Attribute Loops: Dynamic Blocks
Dynamic blocks generate repeating inline blocks (like Security Group rules or AWS load balancer listeners) by iterating over a list of objects at compile time.

*Read more in [[Reference Notes/10-3_meta_arguments_lifecycle_and_state.md#1-loop-control-count-vs-for_each]]*
