---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[statefulset]]"
sub_type: architecture
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#stable-network-identities"
author: "Kubernetes Authors"
course_title: "CKA Exam Prep"
tags:
  - kubernetes/statefulset
  - networking/dns
---

# statefulset - Headless Service and Stable Identity

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[statefulset]] > **Headless Service and Stable Identity**

---

## 📑 Headless Service and Stable Identity

StatefulSets guarantee unique network identities for each pod ordinal by utilizing companion Headless Services.

### 1. Headless Service Role
A Headless Service is defined with `clusterIP: None`. Instead of routing requests randomly via load-balancing IPs (ClusterIP), the service DNS queries directly return the individual IP addresses of all backing pods.

### 2. Stable DNS Format
Each pod receives a stable hostname containing its ordinal index:
```text
<pod-name>.<service-name>.<namespace>.svc.cluster.local
```

For a StatefulSet `db` and a headless service `postgres` in the namespace `database`:
* **Pod 0 DNS:** `db-0.postgres.database.svc.cluster.local`
* **Pod 1 DNS:** `db-1.postgres.database.svc.cluster.local`

### 3. DNS Diagnostics
Validate resolution inside a network utility container:
```bash
# Verify SRV record discovery
dig SRV postgres.database.svc.cluster.local

# Query specific pod address
nslookup db-0.postgres.database.svc.cluster.local
```

*Read more in [07_kubernetes_workloads_and_controllers.md](../Reference%20Notes/07_kubernetes_workloads_and_controllers.md#10-statefulsets)*
