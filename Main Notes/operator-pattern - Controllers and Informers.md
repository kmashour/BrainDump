---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[operator-pattern]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/extend-kubernetes/operator/"
author: "Kubernetes Authors"
course_title: "Kubernetes Operators"
against: []
tags:
  - kubernetes/extending
  - kubernetes/deep-dive
---

# operator-pattern - Controllers and Informers

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[operator-pattern]] > **Controllers and Informers**

---

## 📑 Custom Controllers & Informer Mechanics

At the heart of the Operator Pattern is the reconciliation loop, which is built on the client-go architecture using Informers and workqueues:

```
+-------------------------------------------------------------------------+
|                          CLIENT-GO CONTROLLER FRAMEWORK                 |
|                                                                         |
|  [ API Server ]                                                         |
|        | (List & Watch)                                                 |
|        v                                                                |
|   [ Informer ]  ---(Refreshes cache)---> [ Local Cache ]                |
|        |                                                                |
|   (Triggers Event Handler)                                              |
|        v                                                                |
|  [ Workqueue ]  <---(Pushes Key/Namespace)                              |
|        |                                                                |
|  (Pops event)                                                           |
|        v                                                                |
|  [ Reconcile() Loop ] <---(Reads details from cache)                   |
|        |                                                                |
|        +----(Performs actual changes: creates pods, updates status)     |
+-------------------------------------------------------------------------+
```

1. **Informer:** Opens a HTTP stream (`Watch` request) to the API server. Rather than polling, it receives real-time events (Add, Update, Delete) and updates a local, in-memory cache.
2. **Lister:** Queries this local cache instead of making network calls to the API server, minimizing control plane overhead.
3. **Resource Event Handler:** Triggered by the informer when changes occur. It extracts the object's namespace and name key (e.g., `default/my-custom-app`) and pushes it onto a workqueue.
4. **Workqueue:** A thread-safe, rate-limiting queue that distributes tasks to workers.
5. **Reconciliation Loop (`Reconcile`):** A custom worker thread pops the key from the workqueue, reads the object from the cache, compares the actual state with the spec, and executes mutations (e.g. creating deployments, mounting disks) to align the states.

*Read more in [0-15_kubernetes_api_extension_and_operators.md](../Reference%20Notes/0-15_kubernetes_api_extension_and_operators.md#2-custom-controllers)*
