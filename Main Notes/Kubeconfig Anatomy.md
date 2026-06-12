---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kubectl-deeper]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/"
author: "Kubernetes Documentation"
against: []
tags:
  - kubernetes/kubectl
  - kubernetes/configuration
---

# kubectl - Kubeconfig Anatomy

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[kubectl]] > [[kubectl-deeper]] > **Kubeconfig Anatomy**

---

## 📑 1. Core Structure of Kubeconfig
A `kubeconfig` file organizes access information for multiple clusters, users, and contexts. The default location is `~/.kube/config`.

```mermaid
classDiagram
    class Kubeconfig {
        clusters: List
        users: List
        contexts: List
        current-context: String
    }
    class Cluster {
        name: String
        server: String (API endpoint)
        certificate-authority-data: String
    }
    class User {
        name: String
        client-certificate-data: String
        client-key-data: String
        token: String
    }
    class Context {
        name: String
        cluster: String
        user: String
        namespace: String
    }
    Kubeconfig --> Cluster
    Kubeconfig --> User
    Kubeconfig --> Context
```

---

## ⚙️ 2. CLI Configuration Reference (CKA Commands)
Use imperative commands to view, merge, and switch contexts in CKA:

### A. View Active Kubeconfig
```bash
# View configuration (with sensitive data hidden)
kubectl config view

# View raw configuration (including certificate data)
kubectl config view --raw
```

### B. Create and Switch Contexts
```bash
# 1. Add cluster definition
kubectl config set-cluster dev-cluster --server=https://10.10.0.10:6443 --certificate-authority=/etc/kubernetes/pki/ca.crt

# 2. Add user credentials
kubectl config set-credentials dev-user --client-certificate=/tmp/client.crt --client-key=/tmp/client.key

# 3. Create context mapping user to cluster
kubectl config set-context dev-context --cluster=dev-cluster --user=dev-user --namespace=development

# 4. Switch current-context
kubectl config use-context dev-context
```

*Read more in [[Reference Notes/0-1_kube_api_and_kubectl.md#3-kubeconfig-anatomy-and-context-management]]*\n