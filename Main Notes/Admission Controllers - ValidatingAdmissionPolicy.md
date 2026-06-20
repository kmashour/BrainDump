---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Admission Controllers]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/"
author: "Kubernetes Authors"
course_title: "Kubernetes Reference Documentation"
tags:
  - kubernetes/admission-controllers
  - kubernetes/cel
  - kubernetes/deep-dive
---

# Admission Controllers - ValidatingAdmissionPolicy

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Admission Controllers]] > **ValidatingAdmissionPolicy**

---

## 📑 Declarative Validation with CEL

In Kubernetes v1.36, **`ValidatingAdmissionPolicy`** provides a declarative, in-process alternative to external validating admission webhooks. Using the **Common Expression Language (CEL)**, administrators can write validation rules directly within Kubernetes API resources.

### ⚙️ How it Works
1. **Low Latency & High Reliability:** CEL expressions are compiled and executed directly inside the `kube-apiserver` process. This eliminates the latency of HTTPS round-trips to external webhooks and avoids network-related failure loops (such as webhook timeouts blocking deployments).
2. **Resource Structure:**
   * **`ValidatingAdmissionPolicy`**: Matches specific API groups, versions, resources, and operations (e.g. `CREATE`, `UPDATE` on Deployments) and specifies the CEL validation `expression`.
   * **`ValidatingAdmissionPolicyBinding`**: Binds the policy to resources (using namespaces or labels) and defines the `validationActions` (such as `Deny`, `Warn`, or `Audit`) when a rule is violated.

### 🧩 Core CEL Variables
CEL expressions evaluate a boolean condition (returning `true` to allow, `false` to deny) using request variables exposed by the API server:
* `self` (or `object`): The incoming resource state (e.g., `self.spec.replicas`).
* `oldObject`: The prior resource state, useful for checking field immutability.
* `request`: Request metadata (e.g., namespace, username, operation type).
* `params`: Configuration parameters passed via a custom resource.

### 🔍 Quick Example
A rule restricting a Deployment's replica count to a maximum of 5:
```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingAdmissionPolicy
metadata:
  name: replica-limit-policy
spec:
  failurePolicy: Fail
  matchConstraints:
    resourceRules:
      - apiGroups: ["apps"]
        apiVersions: ["v1"]
        operations: ["CREATE", "UPDATE"]
        resources: ["deployments"]
  validations:
    - expression: "self.spec.replicas <= 5"
      message: "Deployments are restricted to a maximum of 5 replicas."
```

*Read more in [0-16_admission_controllers.md](../Reference%20Notes/0-16_admission_controllers.md#6-declarative-validation-common-expression-language-cel)*
