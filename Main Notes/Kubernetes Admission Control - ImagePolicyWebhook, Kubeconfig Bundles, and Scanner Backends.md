---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Kubernetes Pod Security and Policy Engines]]"
sub_type: architecture
source_type: gemini-chat
author: "Antigravity"
course_title: "CKS Masterclass"
tags:
  - kubernetes/admission-control
  - kubernetes/image-policy-webhook
  - kubernetes/supply-chain
  - status/completed
---

# Kubernetes Admission Control - ImagePolicyWebhook, Kubeconfig Bundles, and Scanner Backends

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Kubernetes Pod Security and Policy Engines]] > **ImagePolicyWebhook & Scanner Architecture**

---

## 🔍 The Supply Chain Gatekeeper: `ImagePolicyWebhook`

`ImagePolicyWebhook` is an in-tree admission plugin inside `kube-apiserver` dedicated specifically to container supply-chain security. It intercepts pod creation requests, inspects container image references (tags and SHA-256 digests), and evaluates them against an external vulnerability scanner (such as **Trivy**, **Anchore**, **Clair**, or **Snyk**).

```
[ Developer runs: kubectl apply -f pod.yaml (image: app:v1) ]
                               │
                               ▼
                      [ kube-apiserver ]
                               │
            (Built-in plugin: ImagePolicyWebhook intercepts)
                               │
                               ▼  (HTTPS POST with image name & digest)
═════════════════════════════════════════════════════════════════════════════════
          THE IMAGE REVIEW CONTRACT (imagepolicy.k8s.io/v1alpha1)
═════════════════════════════════════════════════════════════════════════════════
                               │
                               ▼
                [ SCANNER BACKEND (e.g. Trivy) ]
                ├── Checks image digest in its vulnerability database
                ├── Evaluates CVE policy:
                │   - Does app:v1 have Critical CVEs?
                │   - Was app:v1 signed with Cosign?
                │   - Does it use the 'latest' tag without a digest?
                └── Returns JSON verdict:
                    { "allowed": false, "reason": "Image has 2 CRITICAL CVEs!" }
                               │
                               ▼
                      [ kube-apiserver ]
                               │
                               ├── If allowed: Pod proceeds to scheduler.
                               └── If denied:  Admission fails! Pod rejected!
```

---

## 1. Why Does `ImagePolicyWebhook` Require a Kubeconfig File?

In Kubernetes internal architecture, a **Kubeconfig (`kind: Config`)** is not just for developers running `kubectl` from their laptops. It is the standardized configuration format used whenever *any* Kubernetes component needs to establish an HTTPS/mTLS connection to an external endpoint.

Instead of writing a custom HTTP client from scratch, the `kube-apiserver` reuses its standard Go client library (`client-go`).

### The 3 Mandatory Networking Questions Answered by Kubeconfig

```yaml
apiVersion: v1
kind: Config

# QUESTION 1: Where am I connecting, and how do I trust its TLS certificate?
clusters:
- cluster:
    certificate-authority: /etc/kubernetes/admission/ca.crt # ⚠️ Avoids "unknown authority" TLS panics
    server: https://127.0.0.1:1234/image_policy             # URL of the scanner backend
  name: image-checker

# QUESTION 2: Who am I authenticating as? (mTLS client identity)
users:
- name: api-server
  user:
    client-certificate: /etc/kubernetes/admission/client.crt
    client-key: /etc/kubernetes/admission/client.key

# QUESTION 3: How do I glue the target (cluster) and my identity (user) together?
contexts:
- context:
    cluster: image-checker
    user: api-server
  name: image-checker-ctx

# THE SWITCH: Which context should the API server activate?
current-context: image-checker-ctx
```

#### Why `certificate-authority` is Mandatory:
Because scanner endpoints typically run on internal ports using private TLS certificates, omitting `certificate-authority` causes the API server to reject the connection immediately with:
`x509: certificate signed by unknown authority`.

#### Why `current-context` is Mandatory:
A Kubeconfig file can store definitions for dozens of clusters and users. `current-context` tells the client library which connection profile to instantiate upon boot.

---

## 2. The Admission Configuration File (`AdmissionConfiguration`)

The behavior of the `ImagePolicyWebhook` plugin is governed by an `AdmissionConfiguration` YAML file:

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: AdmissionConfiguration
plugins:
- name: ImagePolicyWebhook
  configuration:
    imagePolicy:
      kubeConfigFile: /etc/kubernetes/admission/kubeconfig.yaml
      allowTTL: 50        # Seconds to cache approved decisions
      denyTTL: 50         # Seconds to cache rejected decisions
      retryBackoff: 500   # Milliseconds to wait before retry
      defaultAllow: false # ⚠️ THE ZERO-TRUST RULE (Must be false!)
```

### The Critical Exam Trap: `defaultAllow: false`
* If `defaultAllow: true`: If the scanner backend crashes or the network blips, the API Server **allows all images through without scanning** (fail-open).
* If `defaultAllow: false`: If the scanner is unreachable, the API Server **denies all images** (fail-closed / zero-trust). In the CKS exam and production environments, `defaultAllow` must always be `false`.

---

## 3. Configuring the Kube-APIServer Static Pod

To activate the webhook, edit `/etc/kubernetes/manifests/kube-apiserver.yaml`:

```yaml
spec:
  containers:
  - command:
    - kube-apiserver
    - --enable-admission-plugins=NodeRestriction,ImagePolicyWebhook # 1. Enable plugin
    - --admission-control-config-file=/etc/kubernetes/admission/admission-config.yaml # 2. Set config path
    volumeMounts:
    - mountPath: /etc/kubernetes/admission
      name: admission-config
      readOnly: true
  volumes:
  - hostPath:
      path: /etc/kubernetes/admission
    name: admission-config
```

> [!CAUTION]
> **Static Pod Volume Mount Requirement:**
> Because `kube-apiserver` runs inside a container, it cannot access files stored on the host node at `/etc/kubernetes/admission` unless that directory is explicitly mapped via both `volumes.hostPath` and `containers[*].volumeMounts`. Failing to mount the directory causes the API server to crash on startup with `no such file or directory`.

*Related Reference Module:* [[Reference Notes/0-7-5_supply_chain_security_and_imagepolicywebhook.md|Module 0-7-5: Supply Chain Security & ImagePolicyWebhook]]
