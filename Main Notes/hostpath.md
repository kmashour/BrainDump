---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[persistentvolume]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/storage/volumes/#hostpath"
author: "Kubernetes Documentation"
tags:
  - kubernetes/storage
  - kubernetes/volumes
---

# persistentvolume - hostpath

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[persistentvolume]] > **hostPath**

---

## 📑 1. What is a hostPath Volume?
A `hostPath` volume mounts a file or directory from the host node's filesystem directly into your Pod.

```text
[ Container Mount: /usr/share/nginx/html ]
                  ||
                  \/ (Direct link)
[ Host Directory:  /data/website-content ]
```

---

## ⚙️ 2. Configuration Spec Example
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: hostpath-pod
spec:
  containers:
  - name: web-server
    image: nginx:alpine
    volumeMounts:
    - name: site-data
      mountPath: /usr/share/nginx/html
  volumes:
  - name: site-data
    hostPath:
      path: /data/website-content # <-- Path on the host node
      type: DirectoryOrCreate     # <-- Creates directory if missing
```

---

## ⚠️ 3. CKA Security and Portability Risks
* **No Node Portability:** If the Pod is rescheduled to a different node, it will mount the path on *that* host, which might have completely different files or lack the path entirely.
* **Security Risk:** Pods running with root permissions can access sensitive host directories (like `/var/log`, `/etc/kubernetes/pki` or Docker socket), leading to host privilege escalation.

*Read more in [[Reference Notes/0-8_storage_mechanics_and_csi.md#1-volume-plugins-and-in-tree-types]]*\n