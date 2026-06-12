---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kubectl-deeper]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/reference/kubectl/jsonpath/"
author: "Kubernetes Documentation"
against: []
tags:
  - kubernetes/kubectl
  - kubernetes/telemetry
---

# kubectl - JSONPath and custom-columns filters

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[kubectl]] > [[kubectl-deeper]] > **JSONPath Filters**

---

## 📑 1. JSONPath Query Syntax
In the CKA exam, you are often asked to extract specific fields (e.g. node IPs, pod images) and save them to a file. **JSONPath** allows you to navigate the JSON output returned by the API server.

```text
JSONPath Elements:
$          Root object
.          Child operator
[*]        Wildcard array matcher
[?()]      Filter expression
@          Current object reference
```

---

## ⚙️ 2. Core CKA JSONPath Commands Cheat Sheet

### A. Extract Node IPs
```bash
# Get InternalIPs of all nodes
kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type=="InternalIP")].address}'
```

### B. Extract Pod Images
```bash
# List all container images running in all namespace pods
kubectl get pods -A -o jsonpath='{.items[*].spec.containers[*].image}'
```

### C. Sort by Field
```bash
# Sort events by creation timestamp
kubectl get events -A --sort-by='.metadata.creationTimestamp'
```

### D. Custom Columns Format
Use `-o custom-columns` to format fields into clean tables:
```bash
kubectl get nodes -o custom-columns=NODE:.metadata.name,IP:.status.addresses[0].address,CPU:.status.capacity.cpu
```

*Read more in [[Reference Notes/0-11_troubleshooting_and_diagnostics.md#5-advanced-telemetry-jsonpath-and-custom-columns]]*\n