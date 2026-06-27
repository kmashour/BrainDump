---
obsidianUIMode: preview
class: reference-note
tier: reference-note
tags:
  - cncf/secrets-store-csi
  - kubernetes/secrets
  - aws/secrets-manager
  - status/completed
---

# Module 12-2: Secrets Store CSI Driver Integration (KodeKloud Talk)

**Breadcrumbs:** [[12-Index - CNCF References|🏠 CNCF References Index]] > **Secrets Store CSI Driver Integration (KodeKloud Talk)**

---

> [!NOTE]
> **Source Citation**
> This reference module summarizes and analyzes the tutorial presentation: *"Secret Store CSI Driver Tutorial | Kubernetes Secrets | AWS Secrets Manager"* by **KodeKloud**. It covers the operational security issues of Base64 encoded Kubernetes secrets, the architecture and lifecycle of the Secrets Store CSI Driver, external provider comparison (ESO and Sealed Secrets), and AWS/EKS integration (IRSA, ServiceAccount annotations, and auto-rotation).
> *   **Source Presentation:** [YouTube - Secrets Store CSI Driver Tutorial](https://www.youtube.com/watch?v=MTnQW9MxnRI)

---

## 🎯 The Security Problem: Native Kubernetes Secrets

Traditional Kubernetes secrets are not secure by default:
* **Base64 Encoding vs. Encryption:** Kubernetes secrets are stored as Base64 encoded strings in `etcd`. Base64 is an encoding scheme, not an encryption method. Anyone with read access to the secret or control plane can easily decode it (`echo "encoded-string" | base64 -d`).
* **GitOps & Version Control Risks:** YAML manifests containing Base64 encoded secrets cannot be safely committed to public or private version control repositories (e.g., GitHub), creating credentials leakage risks.
* **Centralization Requirement:** Organizations utilize external secrets management platforms (such as AWS Secrets Manager, HashiCorp Vault, Google Secret Manager, Azure Key Vault) to store and audit credentials in a single central repository, requiring clusters to dynamically pull and sync these values.

---

## 🏛️ Architectural Comparison: CSI Driver vs. ESO vs. Sealed Secrets

| Secrets Management Tool | Storage Pattern in Cluster | Key Advantages | Key Disadvantages |
| :--- | :--- | :--- | :--- |
| **Sealed Secrets** (Bitnami) | Commits encrypted secrets to Git. Decrypted inside cluster into native `Secret` objects. | GitOps friendly; no external runtime dependencies. | Still persists credentials as native `Secret` API objects in `etcd`. |
| **External Secrets Operator** (ESO) | Synchronizes external store APIs directly to native Kubernetes `Secret` objects. | Seamless integration with external providers; standard environment variables injection. | Persists secrets in `etcd`, which increases the cluster's attack surface and audit scope. |
| **Secrets Store CSI Driver** | Mounts external secrets as files inside a RAM-backed `tmpfs` volume. | **Minimizes attack surface** (no native `Secret` objects stored in `etcd`/cluster memory). Compliant & auditable. | Pod volume lifecycle bound; applications must read credentials from files instead of environment variables. |

---

## ⚙️ How the Secrets Store CSI Driver Works

The lifecycle of dynamic secret mounting follows a structured request-response sequence between the node agent and the external provider:

```
[ Kubelet ] ---> (Mount Request) ---> [ CSI Driver DaemonSet ]
                                            |
                                            v (Read Object Config)
                                    [ SecretProviderClass CRD ]
                                            |
                                            v (Assume IAM Role / Fetch Token)
                                    [ ServiceAccount (IRSA) ]
                                            |
                                            v (API Request)
                                    [ External provider Plugin (e.g. AWS) ]
                                            |
                                            v (Retrieve Plaintext)
                                    [ AWS Secrets Manager ]
                                            |
                                            v (Mount tmpfs Volume)
[ App Container ] <--- (File: /var/secrets/MySQL_Creds)
```

1. **Volume Mounting:** Kubelet schedules a Pod and detects a CSI volume referencing the `secrets-store.csi.k8s.io` driver.
2. **Configuration Resolution:** The CSI Driver reads the corresponding `SecretProviderClass` Custom Resource to locate the target keys and external secrets manager name.
3. **IAM Token Exchange:** The driver accesses the Pod's projected ServiceAccount token (via EKS OIDC/IRSA) and exchanges it via STS for temporary IAM permissions.
4. **Secret Retrieval:** The AWS Provider Plugin uses the temporary STS credentials to fetch the secret payload via `GetSecretValue` from AWS Secrets Manager.
5. **Decryption & Mounting:** The provider decrypts the payload and passes the keys to the CSI Driver, which mounts them as files into a RAM-backed `tmpfs` volume in the container path.

---

## 🛠️ Step-by-Step Implementation Playbook

### 1. Central Secret Configuration (AWS Secrets Manager)
Create the secret keys in AWS:
```bash
aws secretsmanager create-secret --name MySQL_Creds \
  --secret-string '{"username":"user123","password":"password123"}' \
  --region us-east-1
```

### 2. Install CSI Driver and AWS Provider Plugin
Deploy the Secrets Store CSI Driver via Helm and apply the AWS provider installer manifest:
```bash
# Add secrets-store helm repo
helm repo add secrets-store-csi-driver https://kubernetes-sigs.github.io/secrets-store-csi-driver/charts
helm repo update

# Install Helm Chart in kube-system namespace
helm install csi-secrets-store secrets-store-csi-driver/secrets-store-csi-driver \
  --namespace kube-system

# Verify installation of Custom Resource Definitions (CRDs)
kubectl get crd -n kube-system
# Expected:
# secretproviderclasses.secrets-store.csi.x-k8s.io
# secretproviderclasspodstatuses.secrets-store.csi.x-k8s.io

# Deploy AWS Provider Plugin DaemonSet
kubectl apply -f https://raw.githubusercontent.com/aws/secrets-store-csi-driver-provider-aws/main/deployment/aws-provider-installer.yaml
```

### 3. AWS IAM Policy & EKS ServiceAccount (IRSA)
Create the IAM policy to read AWS secrets, and generate an annotated ServiceAccount `API_DSA` bound to the IAM Role using `eksctl`:
```bash
# A. Create IAM Policy
aws iam create-policy --policy-name CSI_EKS_SecretsManager_Policy \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "secretsmanager:GetSecretValue",
          "secretsmanager:DescribeSecret"
        ],
        "Resource": "*"
      }
    ]
  }'

# B. Create annotated ServiceAccount using eksctl
eksctl create iamserviceaccount \
  --name API_DSA \
  --namespace default \
  --cluster eks-demo-1 \
  --region us-east-1 \
  --attach-policy-arn arn:aws:iam::<YOUR_AWS_ACCOUNT_ID>:policy/CSI_EKS_SecretsManager_Policy \
  --approve \
  --override-existing-serviceaccounts
```

### 4. Create the SecretProviderClass Resource
Define the `SecretProviderClass` YAML mapping the target secrets name and provider:
```yaml
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: database-aws-secrets
  namespace: default
spec:
  provider: aws
  parameters:
    objects: |
      - objectName: "MySQL_Creds"
        objectType: "secretsmanager"
```
Apply the configuration:
```bash
kubectl apply -f secretproviderclass.yaml
```

### 5. Configure Pod Workload Specs
Configure the deployment to reference the ServiceAccount and declare the CSI volume:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: secure-api-app
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      app: secure-api
  template:
    metadata:
      labels:
        app: secure-api
    spec:
      serviceAccountName: API_DSA
      containers:
      - name: api-web-server
        image: nginx:alpine
        volumeMounts:
        - name: secret-volume
          mountPath: /tmp
          readOnly: true
      volumes:
      - name: secret-volume
        csi:
          driver: secrets-store.csi.k8s.io
          readOnly: true
          volumeAttributes:
            secretProviderClass: "database-aws-secrets"
```
Apply the deployment:
```bash
kubectl apply -f deployment.yaml
```

---

## 🔍 Diagnostics, Troubleshooting & Auto-Rotation

### 1. Diagnostic CLI Commands
Verify mounted files inside the container:
```bash
# Exec into pod and list mounted files
kubectl exec -it <pod-name> -- ls /tmp
# Expected: MySQL_Creds

# Cat the JSON payload from the mounted path
kubectl exec -it <pod-name> -- cat /tmp/MySQL_Creds
# Expected: {"username":"user123","password":"password123"}
```

### 2. Common Failure Loops
* **MountVolume.SetUp failed:** If OIDC configurations or ServiceAccount annotations are incorrect, Pod creation halts with:
  `WebIdentityErr: failed to retrieve credentials`
* **Object type must be specified:** A formatting error in `SecretProviderClass` parameters (e.g. nesting errors or typos) will cause mount failures:
  `must use object type when a full ARN is not specified`

### 3. Secret Auto-Rotation Configuration
By default, secrets rotation is disabled. To enable auto-rotation, update the Helm release parameters:
```bash
# Update Helm release with rotation enabled (polling interval: 120s)
helm upgrade csi-secrets-store secrets-store-csi-driver/secrets-store-csi-driver \
  --namespace kube-system \
  --set enableSecretRotation=true \
  --set rotationPollInterval=120s
```
* **Application Reload Rationale:** Although the files in `/tmp` are overwritten automatically when rotated in AWS, applications that load credentials into memory *only at startup* will run on stale configs. Workloads must execute filesystem watcher processes or fetch keys from the mount path per request to avoid service degradation.

---

## 🔗 Related Reference Notes
* **Cluster Security & Policies:** [[0-7_security_and_network_policies|Module 0-7: Cluster Security & Network Policies]]
* **CNCF Disaster Recovery:** [[12-1_cncf_kubernetes_disaster_recovery|Module 12-1: CNCF Kubernetes Disaster Recovery]]
