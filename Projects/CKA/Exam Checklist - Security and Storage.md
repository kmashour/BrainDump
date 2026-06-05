---
class: exam-checklist
tier: project-note
project: 'CKA Exam'
status: 'Ready for Review'
---

# CKA Exam Checklist - Security and Storage

This guide covers Role-Based Access Control (RBAC), Kubeconfig configuration, ServiceAccounts, SecurityContexts, NetworkPolicies, and Persistent Storage mechanics.

---

## 1. Role-Based Access Control (RBAC)

RBAC controls authorization by matching API permissions to users, groups, or ServiceAccounts.

### 1.1 RBAC Primitives
*   **Role**: Defines permission rules within a **single namespace**.
*   **RoleBinding**: Grants Role permissions to subjects in that namespace.
*   **ClusterRole**: Defines permissions **cluster-wide** (and for non-namespaced resources like Nodes, PVs).
*   **ClusterRoleBinding**: Grants ClusterRole permissions cluster-wide.

> [!TIP]
> **Exam Trick:** You can bind a `ClusterRole` using a `RoleBinding` in a specific namespace. This grants the permissions of the ClusterRole *only within that namespace*, which prevents duplicating common Roles (like `view`).

### 1.2 Complete RBAC YAML Templates

#### Role (Namespaced)
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-manager
  namespace: development
rules:
- apiGroups: [""] # "" indicates the core API group
  resources: ["pods", "pods/log"]
  verbs: ["get", "list", "watch", "create", "update", "delete"]
- apiGroups: ["apps"]
  resources: ["deployments"]
  verbs: ["get", "list", "update", "patch"]
```

#### RoleBinding (Namespaced)
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: pod-manager-binding
  namespace: development
subjects:
- kind: User
  name: dev-user
  apiGroup: rbac.authorization.k8s.io
- kind: ServiceAccount
  name: CI-sa
  namespace: development
roleRef:
  kind: Role
  name: pod-manager
  apiGroup: rbac.authorization.k8s.io
```

### 1.3 Authorization Testing (`kubectl auth can-i`)
Validate permissions from the command line using impersonation:
```bash
# Check if you can perform a specific action
kubectl auth can-i create deployments

# Test permissions as a specific user in a namespace
kubectl auth can-i list secrets --as dev-user -n development

# Test permissions as a ServiceAccount
kubectl auth can-i get pods --as system:serviceaccount:development:CI-sa -n development

# Test cluster-scoped permissions as a master group user
kubectl auth can-i delete nodes --as-group system:masters
```

---

## 2. Kubeconfig Context Configuration

Kubeconfig files manage credentials, cluster endpoints, and contexts. The default path is `~/.kube/config`.

### 2.1 Kubeconfig Structure
A Kubeconfig is divided into:
*   `clusters`: API server endpoints and CA certificates.
*   `users`: Client certificate and key paths, or tokens.
*   `contexts`: Binds a user to a cluster and sets a default namespace.

### 2.2 CLI Management Commands
```bash
# 1. View merged active configuration
kubectl config view

# 2. Add a new cluster configuration
kubectl config set-cluster staging-cluster \
  --server=https://192.168.1.50:6443 \
  --certificate-authority=/etc/kubernetes/pki/ca.crt \
  --embed-certs=true

# 3. Add credentials for a user
kubectl config set-credentials stage-developer \
  --client-certificate=/etc/kubernetes/pki/users/stage-dev.crt \
  --client-key=/etc/kubernetes/pki/users/stage-dev.key \
  --embed-certs=true

# 4. Create a context binding the user and cluster
kubectl config set-context staging-context \
  --cluster=staging-cluster \
  --user=stage-developer \
  --namespace=staging

# 5. Switch active context
kubectl config use-context staging-context

# 6. Change default namespace for active context
kubectl config set-context --current --namespace=finance
```

---

## 3. ServiceAccounts & Token Mount Rules

ServiceAccounts provide identities for workloads inside Pods.

### 3.1 Automounting Token Rules
By default, Kubernetes mounts the default ServiceAccount token at `/var/run/secrets/kubernetes.io/serviceaccount/token`. If the pod does not interact with the API, disable this for security:

#### Option A: Disable on ServiceAccount
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: secured-sa
automountServiceAccountToken: false
```

#### Option B: Disable on Pod Spec
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secure-app
spec:
  automountServiceAccountToken: false
  containers:
  - name: nginx
    image: nginx:alpine
```

### 3.2 Kubernetes Token API changes
*   **v1.22+**: Tokens are mounted as projected volumes with a 1-hour expiration and are auto-rotated.
*   **v1.24+**: Secrets are no longer auto-generated when creating a ServiceAccount.
    *   To get a token, use the TokenRequest API: `kubectl create token <sa-name>`
    *   For a long-lived, static token, manually define a Secret:
    ```yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: my-sa-token-secret
      annotations:
        kubernetes.io/service-account.name: secured-sa # Must match SA name
    type: kubernetes.io/service-account-token
    ```

---

## 4. SecurityContext Parameters

SecurityContexts define privilege and access control settings for Pods and Containers.

### 4.1 Scope of Parameters
*   **Pod-level only**: `fsGroup` (volume group ID ownership), `sysctls`.
*   **Container-level only**: `capabilities`, `privileged`, `allowPrivilegeEscalation`, `readOnlyRootFilesystem`.
*   **Shared**: `runAsUser`, `runAsGroup`, `runAsNonRoot`, `seLinuxOptions`.

### 4.2 Comprehensive Spec Template
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
spec:
  securityContext:
    runAsUser: 1000        # Pod-level defaults
    runAsGroup: 3000
    runAsNonRoot: true     # Container MUST run with non-root UID
    fsGroup: 4000          # Mounted volumes are owned by GID 4000
  containers:
  - name: secure-app
    image: nginx:alpine
    securityContext:
      runAsUser: 1001      # Override pod level
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true # Root filesystem is read-only
      capabilities:
        add: ["NET_BIND_SERVICE"]   # Bind to privileged ports (<1024)
        drop: ["ALL"]               # Drop all other default capabilities
```

---

## 5. NetworkPolicy YAML Syntax

NetworkPolicies isolate traffic. By default, pod communication is unrestricted (default-allow). Enforced only if using a CNI that supports them (e.g. Calico, Cilium).

### 5.1 AND vs OR Selector Rules
*   **OR Logic** (Separate array items `-`): Allow if it matches namespaceSelector **OR** podSelector.
    ```yaml
      from:
      - namespaceSelector:
          matchLabels: { env: prod }
      - podSelector:
          matchLabels: { app: web }
    ```
*   **AND Logic** (Same array item): Allow only if it matches both namespaceSelector **AND** podSelector.
    ```yaml
      from:
      - namespaceSelector:
          matchLabels: { env: prod }
        podSelector:
          matchLabels: { app: web }
    ```

### 5.2 Default Deny-All Ingress and Egress
Apply to lockdown a namespace completely:
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: secure-ns
spec:
  podSelector: {} # Matches all pods in namespace
  policyTypes:
  - Ingress
  - Egress
```

### 5.3 Database Ingress Policy Template
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: db-ingress-policy
  namespace: secure-ns
spec:
  podSelector:
    matchLabels:
      role: database
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: frontend
    ports:
    - protocol: TCP
      port: 5432
```

---

## 6. PV, PVC, and StorageClass Mechanics

Kubernetes separates physical storage (PV) from application storage requests (PVC).

### 6.1 PV-to-PVC Binding Criteria
A PVC binds to a PV automatically based on:
1.  **StorageClass Match**: Both must have identical `storageClassName`. (Use `""` for static PVs with no class).
2.  **Access Mode**: The PV must support *all* access modes requested by the PVC (`ReadWriteOnce` (RWO), `ReadOnlyMany` (ROX), `ReadWriteMany` (RWX), or `ReadWriteOncePod` (RWOP)).
3.  **Capacity**: The PV's capacity must be $\ge$ the PVC requested size.

### 6.2 Reclaim Policies
Configured under `persistentVolumeReclaimPolicy` on the PV:
*   **Retain**: Default. Deleting the PVC leaves the PV in a `Released` state. Storage data is kept and must be manually deleted.
*   **Delete**: Deleting the PVC automatically triggers the CSI driver to delete the physical volume and the PV object.
*   **Recycle**: Deprecated. Scrubs storage files (`rm -rf`) and returns the PV to `Available`.

### 6.3 Dynamic StorageClass Settings
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: dynamic-sc
provisioner: ebs.csi.aws.com
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
```
*   `volumeBindingMode: WaitForFirstConsumer`: Mandatory for local storage and highly recommended for cloud storage. Delays volume provisioning until the Pod using the PVC is scheduled. This prevents Availability Zone mismatch errors.
*   `allowVolumeExpansion: true`: Allows resizing a volume online by editing the PVC storage request.

### 6.4 PVC Protection Finalizers
If a PVC is stuck in `Terminating` because the referencing pod is deleted, you can bypass safety checks by removing finalizers (Warning: Use with caution!):
```bash
# Clear PVC Protection finalizer
kubectl patch pvc <pvc-name> -p '{"metadata":{"finalizers":null}}'

# Clear PV Protection finalizer
kubectl patch pv <pv-name> -p '{"metadata":{"finalizers":null}}'
```
