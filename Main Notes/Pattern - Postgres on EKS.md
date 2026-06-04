---
obsidianUIMode: preview
class: pattern-note
tier: main-note
domains:
  - "aws"
  - "kubernetes"
  - "database"
  - "linux"
components:
  - "[[pod]]"
  - "[[node]]"
  - "[[container-runtime]]"
sources:
  - "AWS RDS & EKS Storage Whitepaper"
tags:
  - architecture/pattern
  - aws/eks
  - kubernetes/storage
---

# Pattern: Postgres on EKS

**Breadcrumbs:** [[Index|🏠 Index]] > Patterns > **Postgres on EKS**

---

## 🏛️ Architectural Context
This pattern describes hosting a stateful PostgreSQL database inside a Kubernetes cluster (EKS) utilizing AWS EBS (Elastic Block Store) volumes formatted with Linux file systems (ext4/XFS), comparing it against a fully managed database approach (AWS RDS).

### Interactive Component Map
```
[ Client / App Pod ] ---> [ PostgreSQL StatefulSet Pod (EKS) ]
                                    |
                           [ PersistentVolumeClaim ]
                                    |
                            [ EBS CSI Driver ]
                                    |
                        [ AWS EBS Volume (gp3) ]
```

---

## ⚖️ Trade-offs & Alternatives
When designing database persistence on AWS, engineers choose between self-hosted Kubernetes stateful sets and fully managed services:

### Approach A: Self-hosted PostgreSQL on EKS (Using EBS)
* **Pros:** Complete control over DB configuration, extension loading, and replication strategies; no cloud vendor lock-in.
* **Cons:** High administrative overhead. You must manage database failover, backups, and Linux disk volume resizing manually.

### Approach B: Fully Managed AWS RDS PostgreSQL (Alternative)
* **Pros:** Automatic multi-AZ replication, point-in-time recovery, automated patching, and instant disk scaling managed by AWS.
* **Cons:** Vendor lock-in, higher cost per resource unit, and limited access to the underlying OS configuration.

---

## 🛠️ Verification & Practical Implementation
To verify the performance of the Linux disk storage driver on AWS EKS:
1. Deploy the EBS CSI Driver in the EKS cluster.
2. Define a StorageClass mapping to AWS gp3 volumes:
   ```yaml
   apiVersion: storage.k8s.io/v1
   kind: StorageClass
   metadata:
     name: ebs-sc
   provisioner: ebs.csi.aws.com
   volumeBindingMode: WaitForFirstConsumer
   parameters:
     type: gp3
   ```
3. Deploy the PostgreSQL StatefulSet with a volumeClaimTemplate referencing `ebs-sc`.
