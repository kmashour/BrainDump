---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[label]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/"
author: "Kubernetes Documentation"
course_title: "Kubernetes Concepts Overview"
against: []
tags:
  - kubernetes/label
  - kubernetes/deep-dive
---

# label - Selectors and Character Syntax

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[label]] > **Selectors and Character Syntax**

---

## 📑 Label Key and Value Syntax Rules

Valid label keys have two segments: an optional prefix and a name, separated by a slash (`/`).
* **Name Segment (Required):**
  * Must be 63 characters or less.
  * Must begin and end with an alphanumeric character (`[a-z0-9A-Z]`).
  * Can contain dashes (`-`), underscores (`_`), dots (`.`), and alphanumeric characters in between.
* **Prefix Segment (Optional):**
  * If specified, it must be a valid DNS subdomain (max 253 characters).
  * System prefixes `kubernetes.io/` and `k8s.io/` are strictly reserved for core Kubernetes components.
  * If the prefix is omitted, the label key is assumed to be private to the user.
* **Label Values:**
  * Must be 63 characters or less.
  * Must begin and end with an alphanumeric character.
  * Can contain dashes (`-`), underscores (`_`), dots (`.`), and alphanumeric characters.

---

## 🔍 Label Selector Expressions

Kubernetes supports two types of selectors for filtering labeled resources:

### 1. Equality-Based Selectors
Allows filtering by label keys and values using equality or inequality:
* `=`: Equals (e.g., `environment = production`).
* `==`: Equals (synonym for `=`).
* `!=`: Not Equals (e.g., `tier != frontend`).

### 2. Set-Based Selectors
Allows filtering based on a set of values:
* `in`: Matches values in the specified set (e.g., `environment in (production, qa)`).
* `notin`: Matches values not in the specified set (e.g., `tier notin (frontend, admin)`).
* `exists`: Matches resources containing the key, regardless of value (e.g., `partition`).
* `!exists`: Matches resources not containing the key (e.g., `!partition`).

*Read more in [0-2_cluster_architecture_and_components.md](../Reference%20Notes/0-2_cluster_architecture_and_components.md#6-core-kubernetes-object-model-and-metadata)*
