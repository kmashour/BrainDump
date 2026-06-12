---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kubectl]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/overview/kubernetes-api/"
author: "Kubernetes Documentation"
tags:
  - kubernetes/kubectl
  - kubernetes/api-management
---

# kubectl - API Discovery and explanation

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[kubectl]] > **API Discovery & Explanation**

---

## 📑 1. Kubectl API Discovery
To interact with objects, `kubectl` discovers the active API Groups, Versions, and resources supported by the API Server. It queries the `/apis` endpoint and caches metadata locally in `~/.kube/cache`.

---

## ⚙️ 2. Core Exploration Commands

### A. kubectl api-resources
Lists all resources registered in the cluster. This is crucial in the CKA exam to find API groups and namespaced scopes:
```bash
# List all resources
kubectl api-resources

# Filter for resources that support Namespaces
kubectl api-resources --namespaced=true

# Get API Groups for a specific resource (e.g. ingresses)
kubectl api-resources | grep ingresses
```

### B. kubectl api-versions
Lists the supported API groups and versions of the cluster:
```bash
kubectl api-versions
```

### C. kubectl explain
The most useful offline reference during the CKA exam. Describe the schema of any resource fields:
```bash
# Describe Pod spec structure
kubectl explain pod.spec

# Describe service account field inside pod spec recursively
kubectl explain pod.spec.serviceAccountName
```

*Read more in [[Reference Notes/0-12_kubernetes_api_management_and_pod_immutability.md#1-api-machinery-and-object-versioning]]*\n