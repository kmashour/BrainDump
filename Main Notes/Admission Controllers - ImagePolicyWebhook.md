---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Admission Controllers]]"
sub_type: use-case
source_type: documentation
source_url: "https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#imagepolicywebhook"
author: "Kubernetes Documentation"
course_title: "Kubernetes Security Reference"
tags:
  - kubernetes/admission-controllers
  - kubernetes/deep-dive
---

# Admission Controllers - ImagePolicyWebhook

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Admission Controllers]] > **ImagePolicyWebhook**

---

## 📑 ImagePolicyWebhook Setup & Governance

The **`ImagePolicyWebhook`** is a specialized admission controller that intercepts container image deployment requests and queries an external HTTPS webhook backend (such as a container security scanner like Trivy, Aqua, or Anchore) to determine whether the images should be admitted into the cluster.

### 🏛️ Webhook Request Flow
When a Pod is submitted to the API server:
1. The `ImagePolicyWebhook` intercepts the Pod creation request.
2. It POSTs an `imagepolicy.k8s.io/v1alpha1` `ImageReview` payload containing details of all images (including initContainers and ephemeralContainers) to the scanner service.
3. The scanner evaluates the image digest or tags against security policies (e.g. blocking images with critical vulnerabilities, checking if the image comes from a trusted registry).
4. The scanner returns an `ImageReview` response indicating `allowed: true/false`.

### ⚙️ Core Configuration Files
Configuring `ImagePolicyWebhook` requires three config files on the control plane node:

1. **Admission Configuration File (`admission-configuration.yaml`):**
   Registers the plugin and points to the plugin configuration path.
2. **ImagePolicy Configuration File (`imagepolicy-conf.yaml`):**
   Specifies caching times (`allowTTL`/`denyTTL`) and points to the webhook's kubeconfig.
3. **Webhook Kubeconfig File (`kubeconf.yaml`):**
   Defines the TLS certificates and the external scanner's HTTPS endpoint.

---

## 🔍 Hands-on Implementation Pointer

For the complete step-by-step control plane configuration, file paths, kube-apiserver static pod mounting manifests, and failure recovery steps, see the main guide:

*Read more in [0-16_admission_controllers.md](../Reference%20Notes/0-16_admission_controllers.md#4-hands-on-lab-configuring-imagepolicywebhook)*
