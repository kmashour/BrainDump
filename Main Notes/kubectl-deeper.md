---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kubectl]]"
sub_concepts:
  - "[[Kubeconfig Anatomy]]"
  - "[[API Discovery and explanation]]"
  - "[[kubectl - Plugins|kubectl Plugins]]"
use_cases:
  - "[[kubectl YAML dry-run generation]]"
  - "[[Force Deletion bypass]]"
  - "[[JSONPath and custom-columns filters]]"
external_links:
  - "[Mumshad CKA Course](https://kodekloud.com)"
  - "[kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)"
sub_type: core-concept
source_type: udemy
tags:
  - kubernetes/deep-dive
---
# kubectl deeper

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[kubectl]] > **deeper dive**

---

This note covers the structural layout of Kubeconfig files, high-speed CKA syntax tricks, and advanced output parsing techniques for the **kubectl** CLI.

---

## 🗂️ 1. Kubeconfig Anatomy
The configuration file at `~/.kube/config` determines which cluster `kubectl` targets and how it authenticates. It is split into three main blocks:
1. **`clusters`:** A list of target clusters, including their API Server endpoints (e.g., `https://10.244.0.1:6443`) and Certificate Authority (CA) data to verify the server's identity.
2. **`users`:** A list of credentials. This contains client certificates (`client-certificate-data`, `client-key-data`), authentication tokens, or OIDC login configurations.
3. **`contexts`:** Associations mapping a `user` to a `cluster` and specifying a default `namespace` (e.g., "connect to `prod-cluster` as `admin-user` inside the `apps` namespace").

Commands to manage kubeconfigs:
* View current context: `kubectl config current-context`
* Switch context: `kubectl config use-context <context-name>`
* Set default namespace: `kubectl config set-context --current --namespace=<ns-name>`

---

## 🏎️ 2. High-Speed Syntax Formulas (CKA Exam Essentials)
In the CKA exam, speed is critical. Never write YAML manifests from scratch.

### A. The Dry-Run Template Generator
Generate resource manifests instantly without committing them to the API Server:
```bash
# Generate a Pod manifest
kubectl run nginx --image=nginx --dry-run=client -o yaml > pod.yaml

# Generate a Deployment manifest
kubectl create deployment web-app --image=nginx --replicas=3 --dry-run=client -o yaml > deploy.yaml

# Generate a Service manifest
kubectl expose pod nginx --port=80 --target-port=80 --type=NodePort --dry-run=client -o yaml > svc.yaml
```

### B. Force Deletion (Instant Cleanup)
By default, deleting a resource waits for containers to shutdown cleanly (30-second grace period). Bypass this for immediate results:
```bash
kubectl delete pod my-pod --force --grace-period=0
```

---

## 🔎 3. Advanced Output Formatting
You can parse complex API payloads directly in the CLI using filters:

### A. Custom Columns
Extract specific nested fields in a clean table format:
```bash
# Get Pod name and node assignment
kubectl get pods -o custom-columns=POD_NAME:.metadata.name,NODE_ASSIGNED:.spec.nodeName
```

### B. JSONPath Formatting
Extract lists, arrays, or single values from JSON structures:
```bash
# Extract the IP address of all running pods
kubectl get pods -o jsonpath='{.items[*].status.podIP}'

# Extract the container image of a deployment
kubectl get deploy web-app -o jsonpath='{.spec.template.spec.containers[0].image}'
```

---

## 🗺️ 4. API Discovery Commands
Query the API schema directly from the CLI:
* **`kubectl api-resources`:** Lists all API resource types, their shortnames (e.g., `po`, `deploy`, `svc`), API groups, and whether they are namespaced.
* **`kubectl api-versions`:** Lists the enabled API version paths.
* **`kubectl explain <resource>`:** Renders inline documentation for fields (e.g., `kubectl explain pod.spec.containers.securityContext`).

*Read more in [0-1_kube_api_and_kubectl.md](../Reference%20Notes/0-1_kube_api_and_kubectl.md#5-kubectl-cli-formula--speed-tricks).*


## 🔍 Sub-Concepts & Use Cases
This table automatically displays all deeper notes, use cases, and configurations associated with **kubectl-deeper**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[kubectl-deeper]]
SORT file.name ASC
```
