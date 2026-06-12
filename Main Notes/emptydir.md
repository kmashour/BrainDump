---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[persistentvolume]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/storage/volumes/#emptydir"
author: "Kubernetes Documentation"
tags:
  - kubernetes/storage
  - kubernetes/volumes
---

# persistentvolume - emptydir

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[persistentvolume]] > **emptyDir**

---

## 📑 1. What is an emptyDir Volume?
An `emptyDir` volume is created when a Pod is assigned to a Node, and it exists as long as that Pod is running on that node. It is initially empty, and all containers in the Pod can read and write to it.

```text
[ Pod Sandbox ]
  |-- Container A (writes to mount) <-\ 
  |                                   |-- [ Shared emptyDir Directory on Host ]
  |-- Container B (reads from mount) <-/
```

---

## ⚙️ 2. YAML Spec Example
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: shared-volume-pod
spec:
  containers:
  - name: writer
    image: busybox
    command: ["sh", "-c", "echo 'hello' > /data/file.txt; sleep 3600"]
    volumeMounts:
    - name: shared-storage
      mountPath: /data
  - name: reader
    image: busybox
    command: ["sh", "-c", "sleep 5; cat /data/file.txt; sleep 3600"]
    volumeMounts:
    - name: shared-storage
      mountPath: /data
  volumes:
  - name: shared-storage
    emptyDir: {} # <-- Shared volume
```

---

## 🔬 3. emptyDir in Memory (tmpfs)
You can configure the emptyDir to be backed by RAM (tmpfs) rather than node storage. This is fast but counts against container memory limits:
```yaml
  volumes:
  - name: shared-storage
    emptyDir:
      medium: Memory
```

*Read more in [[Reference Notes/0-8_storage_mechanics_and_csi.md#1-volume-plugins-and-in-tree-types]]*\n