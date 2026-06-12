---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[label]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/"
author: "Kubernetes Documentation"
against: []
tags:
  - kubernetes/metadata
---

# label - annotation

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[label]] > **Annotations**

---

## 📑 1. Purpose of Annotations
Unlike labels which are used to select and group objects, **annotations** are used to attach arbitrary non-identifying metadata to objects. Tools, libraries, and operators retrieve this metadata to determine configuration parameters.

---

## ⚙️ 2. Formatting and Rules
* **Key-Value structure:** Both key and value must be strings.
* **Character limits:** Key can have prefixes, values can contain structured data (like JSON or escaped YAML) up to 256KB in size.
```yaml
metadata:
  annotations:
    builder: "jenkins-ci"
    git/commit: "a1b2c3d4e5"
    nginx.ingress.kubernetes.io/rewrite-target: /
```

---

## 🔬 3. CKA Command Operations
You can add or update annotations using `kubectl annotate`:
```bash
# Add annotation to pod
kubectl annotate pod nginx description="production web server"

# Update annotation (overwrite)
kubectl annotate pod nginx description="testing web server" --overwrite

# Remove annotation (by appending a minus sign to the key)
kubectl annotate pod nginx description-
```

*Read more in [[Reference Notes/0-2_cluster_architecture_and_components.md#6-the-kubernetes-object-model]]*\n