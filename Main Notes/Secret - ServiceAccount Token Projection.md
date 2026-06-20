---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[secret]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#launch-a-pod-using-service-account-token-projection"
author: "Kubernetes Authors"
course_title: "Kubernetes Tasks Guide"
tags:
  - kubernetes/secret
  - kubernetes/serviceaccount
  - kubernetes/deep-dive
---

# Secret - ServiceAccount Token Projection

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[secret]] > **ServiceAccount Token Projection**

---

## 📑 Legacy Secrets vs. Modern Projected Tokens

Workload authentication to the API server historically relied on long-lived Secrets. Modern Kubernetes (v1.22+) replaces this with dynamic, ephemeral token projection.

| Characteristic | Legacy ServiceAccount Token Secrets | Modern Projected ServiceAccount Tokens |
| :--- | :--- | :--- |
| **Storage** | Persistent API `Secret` object stored in `etcd`. | Dynamic JWT generated on-demand; never stored in `etcd`. |
| **TTL** | None (valid indefinitely until deleted). | Short-lived (typically 1 hour, custom expiration). |
| **Rotation** | Manual rotation if compromised. | Automatic rotation handled by Kubelet background loops. |
| **Audience** | No restriction (can authenticate anywhere). | Bound cryptographically to specific audience (e.g. `api`). |
| **Binding** | Independent of Pod lifecycle. | Bound to specific Pod UID; invalidated on Pod deletion. |

---

## ⚙️ ServiceAccount Token Projection Manifest

To use token projection, specify a `projected` volume source in the Pod manifest:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: projected-token-pod
spec:
  containers:
  - name: app-container
    image: alpine
    volumeMounts:
    - name: sa-token-vol
      mountPath: /var/run/secrets/projected/serviceaccount
      readOnly: true
  serviceAccountName: my-serviceaccount
  volumes:
  - name: sa-token-vol
    projected:
      sources:
      - serviceAccountToken:
          audience: api
          expirationSeconds: 3600
          path: token
```

---

## 🔄 Automatic Rotation Mechanics

1. **Generation:** The Kubelet calls the API server's `TokenRequest` endpoint to request a short-lived token bound to the Pod's lifecycle.
2. **Mounting:** Kubelet writes this token to a volatile memory-backed `tmpfs` volume mounted inside the container.
3. **Auto-Refresh Loop:** Kubelet periodically checks the token's lifetime and requests a fresh token when:
   * The token reaches **80% of its total TTL** (48 minutes for a 1-hour token).
   * The token has been active for **24 hours**.
4. **Atomic Write Swap:** Kubelet writes the new token to a temporary file (`.token.tmp`) and executes an atomic Linux `rename()` system call to replace the active token. This avoids partial read corruption and allows the container to dynamically consume the rotated token without needing a Pod restart.

*Read more in [0-7_security_and_network_policies.md](../Reference%20Notes/0-7_security_and_network_policies.md#115-modern-tokenrequest-api--serviceaccount-token-projection)*

