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

---

## 7. Advanced Volume & Ephemeral Storage Checklists

#### 1. Projected Volumes Spec Check
If you need to project multiple sources into a single directory:
*   Ensure all sources are read-only (`readOnly: true`).
*   Verify the projected list structure under `projected.sources`:
    ```yaml
    volumes:
    - name: unified-volume
      projected:
        sources:
        - secret:
            name: user-pass
        - configMap:
            name: db-host
    ```

#### 2. Ephemeral Storage Limit Eviction Diagnostics
If a Pod keeps crashing or is terminated with the message `Evicted` and reason `DiskPressure`:
1.  **Check Pod events**:
    ```bash
    kubectl describe pod <pod-name>
    ```
    *Look for*: `Evicted: Pod ephemeral local storage usage exceeds the total limit of containers`.
2.  **Verify local limits**:
    Check the container `resources.limits` configuration:
    ```yaml
    resources:
      limits:
        ephemeral-storage: "1Gi"
    ```
    If the container writes large temporary files or outputs massive logs, increase the limit or configure a PersistentVolume.

#### 3. Generic Ephemeral Volume Usage
If you need temporary scratch space that requires dynamic provisioning (e.g. SSD disk speed or dedicated PV limits):
*   Define the `ephemeral.volumeClaimTemplate` inline inside `spec.volumes`:
    ```yaml
    volumes:
    - name: temp-ssd-volume
      ephemeral:
        volumeClaimTemplate:
          spec:
            accessModes: [ "ReadWriteOnce" ]
            storageClassName: "ssd-storage"
            resources:
              requests:
                storage: 5Gi
    ```
    *Note:* The lifecycle of this volume and claim is bound directly to the Pod. When the Pod is deleted, the dynamic claim and volume are unmounted and deleted.

---

## 8. Pod Security Admission & Secrets Hardening Checklist

### A. Pod Security Admission Namespace Labeling
Verify and apply Pod Security Standards (PSS) to namespaces:
```bash
# Label namespace to ENFORCE the restricted profile
kubectl label namespace secure-ns pod-security.kubernetes.io/enforce=restricted

# Label namespace to WARN on baseline violations
kubectl label namespace secure-ns pod-security.kubernetes.io/warn=baseline

# Audit namespace labeling status
kubectl get ns secure-ns --show-labels
```

### B. Secrets Encryption at Rest Verification
Verify that encryption-at-rest is enabled and functioning:
```bash
# Verify api-server process arguments for encryption provider configuration
ps -aux | grep kube-apiserver | grep encryption-provider-config

# Query etcd registry directly to verify cipher text encryption (returns encrypted format, not plaintext values)
kubectl exec -n kube-system etcd-control-plane -- etcdctl \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  get /registry/secrets/default/my-secret
```

### C. Restricting Namespace Metadata Access
* **Escalation Vector:** Restrict developer RoleBindings from granting `patch` or `update` access on `namespaces`. Since PSA and NetworkPolicies rely on namespace labels, users could downgrade namespace security parameters by altering labels.


## 9. ImagePolicyWebhook Configuration Checklist

*Reference Guide:* [[Reference Notes/0-16_admission_controllers.md|0-16_admission_controllers.md]]
*Hands-on Project:* [[Projects/kubernetes/Project - Admission Webhooks.md|Project - Admission Webhooks.md]]

Use this checklist to configure external container image scanning at API admission time.

### A. Directory & File Setup
Create a dedicated config directory on the control plane node and populate the configuration files:
```bash
# 1. Create configuration directory
mkdir -p /etc/kubernetes/imgvalidation

# 2. Write Admission Configuration file
cat <<EOF > /etc/kubernetes/imgvalidation/admission-configuration.yaml
apiVersion: apiserver.config.k8s.io/v1
kind: AdmissionConfiguration
plugins:
  - name: ImagePolicyWebhook
    path: /etc/kubernetes/imgvalidation/imagepolicy-conf.yaml
EOF

# 3. Write ImagePolicy configuration file
cat <<EOF > /etc/kubernetes/imgvalidation/imagepolicy-conf.yaml
imagePolicy:
  kubeConfigFile: /etc/kubernetes/imgvalidation/kubeconf.yaml
  allowTTL: 50
  denyTTL: 50
  retryBackoff: 500
  defaultAllow: false
EOF

# 4. Write Webhook Kubeconfig file
cat <<EOF > /etc/kubernetes/imgvalidation/kubeconf.yaml
apiVersion: v1
kind: Config
clusters:
- cluster:
    certificate-authority: /etc/kubernetes/imgvalidation/webhook.crt
    server: https://image-checker-webhook.default.svc:1323/image_policy
  name: checker_webhook
contexts:
- context:
    cluster: checker_webhook
    user: api-server
  name: checker_validator
current-context: checker_validator
preferences: {}
users:
- name: api-server
  user:
    client-certificate: /etc/kubernetes/pki/front-proxy-client.crt
    client-key: /etc/kubernetes/pki/front-proxy-client.key
EOF
```

### B. Kube-APIServer Configuration
Mount the directory and enable the plugin inside the kube-apiserver static pod manifest (`/etc/kubernetes/manifests/kube-apiserver.yaml`):

```yaml
# Add command flags:
- --enable-admission-plugins=NodeRestriction,ImagePolicyWebhook
- --admission-control-config-file=/etc/kubernetes/imgvalidation/admission-configuration.yaml

# Add VolumeMount inside container:
volumeMounts:
- mountPath: /etc/kubernetes/imgvalidation
  name: imgvalidation
  readOnly: true

# Add HostPath Volume inside spec:
volumes:
- hostPath:
    path: /etc/kubernetes/imgvalidation
    type: DirectoryOrCreate
  name: imgvalidation
```

### C. Troubleshooting & Verification
* **API Server restart:** Check if the API server starts up successfully:
  ```bash
  watch crictl ps
  ```
* **Read api-server logs if it crash loops:**
  ```bash
  tail -f /var/log/pods/kube-system_kube-apiserver-*/kube-apiserver/*.log
  ```
* **Verify webhook enforcement:** Test creating a pod. If the webhook works, pods using unauthorized images will be blocked with a clear message:
  ```text
  Error from server (Forbidden): Pod "unauthorized-pod" is forbidden: image policy webhook denied the request
  ```


## 10. Custom Mutating Admission Webhook Configuration Checklist

*Reference Guide:* [[Reference Notes/0-16_admission_controllers.md|0-16_admission_controllers.md]]
*Hands-on Project:* [[Projects/kubernetes/Project - Admission Webhooks.md|Project - Admission Webhooks.md]]

Use this checklist to deploy and verify an external Mutating Admission Webhook inside the cluster.

### A. Secret & TLS Setup
The webhook server requires certificates to serve traffic over HTTPS:
```bash
# 1. Create the target namespace
kubectl create namespace webhook-demo

# 2. Create the TLS secret containing the signed webhook certificate/key
kubectl -n webhook-demo create secret tls webhook-server-tls \
  --cert=/etc/webhook/certs/tls.crt \
  --key=/etc/webhook/certs/tls.key
```

### B. Deployment & Service Configuration
Deploy the webhook server app and expose it using an internal Service on port 443:
```yaml
# webhook-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webhook-server
  namespace: webhook-demo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: webhook-server
  template:
    metadata:
      labels:
        app: webhook-server
    spec:
      containers:
      - name: webhook-server
        image: security-webhook:latest
        ports:
        - containerPort: 8443
        volumeMounts:
        - name: certs
          mountPath: /etc/webhook/certs
          readOnly: true
      volumes:
      - name: certs
        secret:
          secretName: webhook-server-tls
---
# webhook-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: webhook-service
  namespace: webhook-demo
spec:
  ports:
  - port: 443
    targetPort: 8443
  selector:
    app: webhook-server
```
Deploy the configurations:
```bash
kubectl apply -f webhook-deployment.yaml
kubectl apply -f webhook-service.yaml
```

### C. Webhook Registration Configuration
Register the mutating webhook with the API server, ensuring the `caBundle` matches the CA certificate signing the webhook cert:
```yaml
# webhook-configuration.yaml
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingWebhookConfiguration
metadata:
  name: mutating-security-webhook
webhooks:
  - name: webhook-server.webhook-demo.svc
    clientConfig:
      service:
        name: webhook-service
        namespace: webhook-demo
        path: "/mutate"
      caBundle: "<BASE64_CA_PEM_HERE>"
    rules:
      - operations: ["CREATE"]
        apiGroups: [""]
        apiVersions: ["v1"]
        resources: ["pods"]
    admissionReviewVersions: ["v1"]
    sideEffects: None
    timeoutSeconds: 5
```
Apply the configuration:
```bash
kubectl apply -f webhook-configuration.yaml
```

### D. Operational Testing
* **Test Case 1 (Defaults Injection):** Deploy a pod with no security context. Check if the webhook automatically injected the default values:
  ```bash
  kubectl get pod pod-with-defaults -o yaml | grep -A 2 securityContext
  # Expected output:
  # securityContext:
  #   runAsNonRoot: true
  #   runAsUser: 1234
  ```
* **Test Case 2 (Overrides):** Deploy a pod with `runAsNonRoot: false`. The webhook should allow it to run as root.
* **Test Case 3 (Conflict):** Deploy a pod with `runAsNonRoot: true` and `runAsUser: 0`. The webhook should reject the creation:
  ```text
  Error from server (InternalError): error when creating "pod-with-conflict.yaml": Internal error occurred: admission webhook "webhook-server.webhook-demo.svc" denied the request: runAsNonRoot specified, but runAsUser set to 0 (the root user)
  ```



