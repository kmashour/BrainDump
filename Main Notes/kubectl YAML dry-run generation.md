---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kubectl-deeper]]"
sub_type: use-case
source_type: udemy
author: "Mumshad Mannambeth"
course_title: "Certified Kubernetes Administrator (CKA)"
tags:
  - kubernetes/kubectl
  - kubernetes/imperative
---

# kubectl - kubectl YAML dry-run generation

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[kubectl]] > [[kubectl-deeper]] > **YAML dry-run generation**

---

## 📑 1. Speed-run Manifesto
In the CKA exam, writing YAML manifests from scratch is a waste of time. You should use imperative commands with `--dry-run=client -o yaml` to generate baseline templates, then customize them.

---

## ⚙️ 2. CKA Speed Run Cheat Sheet

### A. Pods
```bash
# Generate Nginx pod YAML
kubectl run nginx --image=nginx:alpine --dry-run=client -o yaml > pod.yaml
```

### B. Deployments & Scaling
```bash
# Generate deployment YAML with 3 replicas
kubectl create deployment web-app --image=nginx --replicas=3 --dry-run=client -o yaml > deploy.yaml
```

### C. Services
```bash
# Generate ClusterIP service exposing pod port 80 to service port 8080
kubectl expose pod nginx --name=nginx-service --port=8080 --target-port=80 --dry-run=client -o yaml > svc.yaml

# Generate NodePort service
kubectl create service nodeport web-svc --tcp=80:80 --node-port=30080 --dry-run=client -o yaml
```

### D. Jobs & CronJobs
```bash
# Generate a CronJob running every minute
kubectl create cronjob sleep-job --schedule="*/1 * * * *" --image=busybox -- /bin/sh -c "sleep 30" --dry-run=client -o yaml
```

### E. RBAC Roles & Bindings
```bash
# Create a ClusterRole with rules
kubectl create clusterrole pod-reader --verb=get,list,watch --resource=pods --dry-run=client -o yaml

# Create a RoleBinding matching role to ServiceAccount
kubectl create rolebinding dev-bind --role=pod-reader --serviceaccount=development:default-sa --dry-run=client -o yaml
```

*Read more in [[Reference Notes/0-1_kube_api_and_kubectl.md#8-imperative-commands-vs-declarative-manifests]]*\n