---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[customresourcedefinition]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/"
author: "Kubernetes Authors"
course_title: "Kubernetes API Extensions"
tags:
  - kubernetes/extending
  - kubernetes/deep-dive
---

# customresourcedefinition - Subresources and Schema

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[customresourcedefinition]] > **Subresources and Schema**

---

## 📑 OpenAPI v3 Validation Schema

The primary api server uses an OpenAPI v3 schema configured within the CRD's `.spec.versions[*].schema.openAPIV3Schema` block to enforce validation constraints.
* **Typing rules:** Every field must specify a type (e.g. `string`, `integer`, `boolean`, `object`, `array`).
* **Validation restrictions:** Supports regex matching (`pattern`), integer boundaries (`minimum`, `maximum`), array limits, and custom lists (`enum`). If a request body violates these rules, the API server rejects it with a `422 Unprocessable Entity` error.

---

## ⚙️ CRD Subresources

CRDs support two optional subresources configured at the version level:

### 1. The `/status` Subresource
* **Purpose:** Decouples user-specified desired state (`spec`) from system-updated observed state (`status`).
* **Mechanics:** Enables the `/status` endpoint path. Writes to `/status` discard changes to `.spec`, and writes to the main path discard changes to `.status`. This avoids race conditions during controller updates.

### 2. The `/scale` Subresource
* **Purpose:** Exposes the custom object to scale-based controller operations (like HorizontalPodAutoscalers).
* **Configuration:** Defines the path to target replica numbers:
  * `specReplicasPath`: Maps the desired replicas field (e.g., `.spec.replicas`).
  * `statusReplicasPath`: Maps the observed replicas field (e.g., `.status.replicas`).
  * `labelSelectorPath`: Maps the pod selector label query to associate target pods.

*Read more in [0-15_kubernetes_api_extension_and_operators.md](../Reference%20Notes/0-15_kubernetes_api_extension_and_operators.md#1-customresourcedefinitions-crds)*
