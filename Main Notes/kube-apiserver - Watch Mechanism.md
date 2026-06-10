---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kube-apiserver]]"
sub_type: core-concept
sources:
  - "Mumshad CKA Course"
  - "Kubernetes Official Docs"
tags:
  - kubernetes/kube-apiserver
  - kubernetes/deep-dive
---

# kube-apiserver - Watch Mechanism

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[kube-apiserver]] > **Watch Mechanism**

---

## 📡 The Watch Mechanism (`-w`)
Instead of polling the API server periodically (which scales poorly), clients use the HTTP Watch mechanism:
* The client opens a single persistent HTTPS connection.
* The API server streams state events (Added, Modified, Deleted) in chunked JSON messages as they occur in `etcd`.
* Essential for controllers and the scheduler to react instantly to cluster changes.

*Read more in [0-1_kube_api_and_kubectl.md](../Reference%20Notes/0-1_kube_api_and_kubectl.md#4-the-watch-mechanism--w)*.
