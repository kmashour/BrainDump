---
obsidianUIMode: preview
class: pattern-note
tier: main-note
domains:
  - "aws"
  - "kubernetes"
  - "database"
  - "linux"
  - "networking"
components:
  - "[[statefulset]]"
  - "[[pod]]"
  - "[[node]]"
  - "[[persistentvolume]]"
  - "[[persistentvolumeclaim]]"
  - "[[storageclass]]"
  - "[[ingress]]"
sources:
  - "[[Reference Notes/08_security_and_network_policies.md]]"
  - "[[Reference Notes/09_storage_mechanics_and_csi.md]]"
  - "[[Reference Notes/10_networking_dns_and_ingress.md]]"
  - "[[Reference Notes/14_scheduling_logging_and_lifecycle.md]]"
tags:
  - architecture/pattern
  - aws/eks
  - kubernetes/storage
  - security/tls
  - networking/ingress
---

# Pattern: Postgres on EKS

**Breadcrumbs:** [[Index|🏠 Index]] > Patterns > **Postgres on EKS**

---

## 🏛️ Architectural Context

Hosting a stateful, production-grade PostgreSQL database inside a Kubernetes cluster (EKS) requires coordinating high-performance storage, container security, and network routing. This pattern integrates three core design patterns:

1. **Topology-Aware Volume Binding (`WaitForFirstConsumer`)**:
   AWS EBS volumes are zonal resources (locked to a specific availability zone like `us-east-1a`). By default, `volumeBindingMode: Immediate` provisions the volume instantly when the PVC is created. If the scheduler later schedules the Pod to a node in `us-east-1b` (due to CPU/memory limits or node taints), the Pod will stay stuck in a `Pending` state with a scheduling conflict.
   Setting `volumeBindingMode: WaitForFirstConsumer` delays dynamic provisioning. The scheduler first chooses a valid node based on resources and affinity, identifies its zone (e.g., `us-east-1a`), and then instructs the AWS EBS CSI driver to provision the volume in that exact zone.

2. **Pod-Level TLS Encryption & Certificates API**:
   To secure database traffic in transit, PostgreSQL is configured to enforce TLS. Rather than manually injecting keys into worker nodes, the pattern utilizes the Kubernetes **Certificates API**. 
   We submit a `CertificateSigningRequest` (CSR) to the cluster control plane to sign the PostgreSQL server certificates. The signed certificate and private key are stored in a Kubernetes `Secret` and mounted directly into the database container's isolated filesystem namespace, where PostgreSQL reads them at startup.

3. **L7 Ingress Path-Based Routing & Edge SSL Termination**:
   External administrative access (e.g., via pgAdmin) is exposed using the Nginx Ingress Controller. 
   * **SSL Termination**: The Ingress controller terminates external HTTPS traffic using a wildcard or domain TLS certificate stored in a dedicated Kubernetes Secret.
   * **Path-Based Routing & Rewriting**: The controller routes requests based on paths (e.g., `/pgadmin` routes to pgAdmin, while `/api` routes to application services). Because pgAdmin expects request payloads relative to the root (`/`), the Ingress controller uses the `rewrite-target` annotation to strip the prefix before forwarding traffic to the backend service.

4. **AWS KMS Secrets Envelope Encryption**:
   To secure sensitive database credentials (e.g., `POSTGRES_PASSWORD`), the database password is stored in a Kubernetes `Secret`. Rather than relying on default base64 encoding (which is readable by anyone with access to etcd or backups), the cluster is configured with **AWS KMS Envelope Encryption**.
   The API server uses a KMS provider key to encrypt the data encryption keys (DEKs) that encrypt the Secret payload in etcd. The secret is dynamically injected as an environment variable into the PostgreSQL container at runtime, never writing plaintext credentials to disk.

### Interactive Component Map
```mermaid
graph TD
    Client([User Browser]) -- HTTPS: /pgadmin --> Ingress[Nginx Ingress Controller]
    Client -- HTTPS: /api/v1 --> Ingress
    
    subgraph EKS Cluster [EKS Cluster - VPC]
        Ingress -- Decrypts SSL / Forwards to pgadmin-service:80 --> PGAdmin[pgAdmin Pod]
        Ingress -- Decrypts SSL / Forwards to app-service:8080 --> AppPod[App Pod]
        
        AppPod -- Establishes SSL Connection --> Postgres[PostgreSQL StatefulSet Pod]
        PGAdmin -- Establishes SSL Connection --> Postgres
        
        subgraph Worker Node [Worker Node - us-east-1a]
            Postgres
            DiskMount[/var/lib/postgresql/data]
        end
        
        subgraph AWS Cloud [AWS Infrastructure]
            EBS[AWS EBS gp3 Volume]
        end
        
        Postgres -- Write Operations --> DiskMount
        DiskMount -- Bound via EBS CSI --> EBS
    end
    
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:2px,color:#fff;
    classDef aws fill:#ff9900,stroke:#fff,stroke-width:2px,color:#fff;
    class Ingress,PGAdmin,AppPod,Postgres k8s;
    class EBS aws;
```

---

## ⚖️ Trade-offs & Alternatives

When designing database persistence on AWS, engineers choose between self-hosted Kubernetes stateful sets and fully managed services:

### Approach A: Self-hosted PostgreSQL on EKS (Using EBS, CSR, and Ingress)
* **Pros**: 
  * Complete control over DB configuration, extension loading (e.g., TimescaleDB, PostGIS), and replication strategies.
  * No cloud vendor lock-in; the manifests can be ported to other clouds (Azure AKS, Google GKE) with minimal changes.
  * Reduced cloud expenditures for high-compute workloads compared to RDS DB instance pricing.
* **Cons**:
  * High administrative overhead. The ops team must manage replication failure recovery, database backups, and manual minor/major engine upgrades.
  * Complex disk sizing. Though EBS dynamic expansion is supported, it requires monitoring and automating expansion thresholds.

### Approach B: Fully Managed AWS RDS PostgreSQL (Alternative)
* **Pros**:
  * Automatic multi-AZ replication, automated point-in-time recovery (PITR), auto-patching, and automated disk scaling managed by AWS.
  * Offloads the administrative burden from Kubernetes operations.
* **Cons**:
  * Vendor lock-in (AWS RDS APIs and IAM integrations).
  * High cost per resource unit.
  * Limited access to the underlying OS configuration, making kernel-level optimizations or custom extension loading impossible.

---

## 🛠️ Verification & Practical Implementation

### Step 1: StorageClass with Topology-Aware Dynamic Provisioning
Define a StorageClass utilizing the AWS EBS CSI driver. Note the `WaitForFirstConsumer` binding mode and the expansion flag:

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: ebs-gp3-sc
provisioner: ebs.csi.aws.com
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
parameters:
  type: gp3
  iops: "3000"
  throughput: "125"
```

### Step 2: Request TLS Certificates via the Kubernetes Certificates API
Generate a private key and CSR for the database server, submit it as a Kubernetes resource, approve it, and store it in a Secret:

1. **Generate Key and CSR**:
   ```bash
   openssl genrsa -out postgres.key 2048
   openssl req -new -key postgres.key -subj "/CN=postgres.default.svc.cluster.local" -out postgres.csr
   ```

2. **Submit `CertificateSigningRequest`**:
   Create a manifest `postgres-csr.yaml` embedding the base64-encoded CSR (without newlines):
   ```yaml
   apiVersion: certificates.k8s.io/v1
   kind: CertificateSigningRequest
   metadata:
     name: postgres-csr
   spec:
     request: <BASE64_ENCODED_CSR_STRING>
     signerName: kubernetes.io/kube-apiserver-client
     usages:
     - digital signature
     - key encipherment
     - server auth
     - client auth
   ```
   Apply it:
   ```bash
   kubectl apply -f postgres-csr.yaml
   ```

3. **Approve and Retrieve Certificate**:
   ```bash
   # Approve the request
   kubectl certificate approve postgres-csr
   
   # Download the signed certificate
   kubectl get csr postgres-csr -o jsonpath='{.status.certificate}' | base64 --decode > postgres.crt
   ```

4. **Create TLS Secret**:
   ```bash
   kubectl create secret tls postgres-tls-secret \
     --cert=postgres.crt \
     --key=postgres.key \
     --namespace=default
   ```

5. **Create Database Credentials Secret**:
   ```bash
   kubectl create secret generic postgres-db-secret \
     --from-literal=password="SuperSecurePassword123" \
     --namespace=default
   ```

### Step 3: Deploy PostgreSQL StatefulSet with SSL Configuration
Configure the StatefulSet to mount the TLS Secret and configure PostgreSQL for SSL:

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres
  namespace: default
spec:
  serviceName: postgres-headless
  replicas: 1
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
      - name: postgres
        image: postgres:15-alpine
        env:
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: postgres-db-secret
              key: password
        # Enable SSL flags in PostgreSQL startup command
        command:
        - "postgres"
        - "-c"
        - "ssl=on"
        - "-c"
        - "ssl_cert_file=/etc/postgresql/certs/tls.crt"
        - "-c"
        - "ssl_key_file=/etc/postgresql/certs/tls.key"
        ports:
        - containerPort: 5432
          name: db
        volumeMounts:
        - name: postgres-data
          mountPath: /var/lib/postgresql/data
        - name: postgres-certs
          mountPath: /etc/postgresql/certs
          readOnly: true
      volumes:
      - name: postgres-certs
        secret:
          secretName: postgres-tls-secret
          defaultMode: 0600 # PostgreSQL requires strict permissions on private keys
  volumeClaimTemplates:
  - metadata:
      name: postgres-data
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: "ebs-gp3-sc"
      resources:
        requests:
          storage: 10Gi
```

### Step 4: Expose pgAdmin Interface with Path-Based Routing & Ingress TLS
Deploy pgAdmin and create an Ingress resource terminating TLS at the edge and rewriting paths:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: pgadmin-ingress
  namespace: default
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /$2
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - db-admin.myorg.com
    secretName: wildcard-domain-tls-secret
  rules:
  - host: db-admin.myorg.com
    http:
      paths:
      - path: /pgadmin(/|$)(.*)
        pathType: Prefix
        backend:
          service:
            name: pgadmin-service
            port:
              number: 80
```

*Request translation:* 
* Client accesses `https://db-admin.myorg.com/pgadmin/login`
* Ingress controller terminates SSL using `wildcard-domain-tls-secret`.
* Ingress controller rewrites path to `/login` (via matching captured regex group 2) and forwards to `pgadmin-service:80/login`.
