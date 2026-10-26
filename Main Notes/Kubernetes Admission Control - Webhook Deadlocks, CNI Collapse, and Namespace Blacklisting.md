---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Kubernetes Pod Security and Policy Engines]]"
sub_type: pitfall
source_type: gemini-chat
author: "Antigravity"
course_title: "CKS Masterclass"
tags:
  - kubernetes/admission-control
  - kubernetes/webhooks
  - kubernetes/troubleshooting
  - status/completed
---

# Kubernetes Admission Control - Webhook Deadlocks, CNI Collapse, and Namespace Blacklisting

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Kubernetes Pod Security and Policy Engines]] > **Webhook Deadlocks & Namespace Blacklisting**

---

## 💀 The Two Great Admission Webhook Disasters

When deploying dynamic admission webhooks (such as OPA Gatekeeper, Kyverno, or custom validation controllers), misconfiguring the webhook scope can trigger two catastrophic failure modes:
1. **The Webhook Deadlock (Circular Dependency Death Spiral):** The cluster cannot boot because the policy engine pod is waiting for itself to approve its own creation.
2. **The CNI and Storage Collapse:** Strict security policies inadvertently reject infrastructure pods (`kube-system`), killing node networking and persistent storage.

---

## 1. Disaster 1: The Circular Dependency Death Spiral

### Why Does It Happen on Cluster Restart?
When a worker node or cluster reboots after a power failure or maintenance:
1. All container processes in the container runtime (`containerd`) are dead.
2. The Deployment controller for OPA Gatekeeper or Kyverno notices the missing pod.
3. The controller submits a fresh **`CREATE Pod`** HTTP request to the `kube-apiserver` (`POST /api/v1/namespaces/gatekeeper-system/pods`).
4. The API Server inspects its registered `ValidatingWebhookConfiguration`.
5. Because the configuration targets `operations: ["CREATE"]` on `resources: ["pods"]`, the API Server pauses the creation and attempts to make an HTTPS call to the webhook endpoint (`https://gatekeeper-service:8443/v1/admit`).
6. **The Trap:** The webhook pod is not running yet—this `CREATE` request is the very process attempting to start it!
7. The connection times out (`connection refused`).
8. If the webhook specifies `failurePolicy: Fail`, the API server interprets the timeout as a security failure and **REJECTS** the pod creation!

```
+-----------------------------------------------------------------------------------+
|                        THE CIRCULAR DEPENDENCY DEATH SPIRAL                       |
+-----------------------------------------------------------------------------------+
| 1. Node reboots. OPA Gatekeeper Pod is stopped.                                   |
|    │                                                                              |
| 2. Deployment controller issues: CREATE Pod (gatekeeper-controller-xyz).          |
|    │                                                                              |
| 3. API Server intercepts CREATE Pod: "Must call Gatekeeper webhook first!"        |
|    │                                                                              |
| 4. API Server dials: https://gatekeeper-service:8443/v1/admit ──► CONNECTION REFUSED|
|    │                                                                              |
| 5. failurePolicy: Fail triggers ──► API Server REJECTS Gatekeeper Pod creation!   |
|    │                                                                              |
| 6. DEADLOCK: Gatekeeper cannot start because it is waiting for itself to approve  |
|    its own creation. NO POD IN THE ENTIRE CLUSTER CAN EVER START AGAIN!           |
+-----------------------------------------------------------------------------------+
```

---

## 2. Disaster 2: The CNI and Storage Driver Rejection

### Why CNI and Storage Pods Need "Superuser" Access
In Kubernetes, network plugins (**Flannel**, **Calico**, **Cilium**) and storage drivers (**AWS EBS CSI**, **Ceph Rook**) do not run as external host binaries. They run as **Pods inside the cluster**, almost always within the **`kube-system`** namespace:

```yaml
# Snippet from a real CNI DaemonSet pod in kube-system:
apiVersion: v1
kind: Pod
metadata:
  name: kube-flannel-ds-xyz
  namespace: kube-system
spec:
  hostNetwork: true       # ⚠️ Required: Must attach to physical host network interface (eth0)
  containers:
  - name: kube-flannel
    securityContext:
      privileged: true    # ⚠️ Required: Must configure kernel routing tables and iptables
    volumeMounts:
    - name: cni-bin
      mountPath: /opt/cni/bin # ⚠️ Required: Writes CNI binary plugins to the host filesystem
  volumes:
  - name: cni-bin
    hostPath:             # ⚠️ Required: Touches physical host directory
      path: /opt/cni/bin
```

### The Failure Chain: What Happens When Policies Evaluate `kube-system`
Suppose a security team deploys a policy:
> *"No pod in the cluster may specify `privileged: true` or `hostNetwork: true`."*

If the webhook evaluates `kube-system`:
1. The node reboots or the CNI DaemonSet rolls out an update.
2. The Flannel or Calico DaemonSet requests the creation of a new CNI pod.
3. The API Server forwards the CNI pod manifest to the webhook.
4. The policy engine evaluates the rule: *"Flannel has `privileged: true`! **VIOLATION!**"*
5. The webhook returns `{ "allowed": false, "reason": "Privileged pods are banned!" }`.
6. The API Server **REJECTS** the CNI pod!

```
+-----------------------------------------------------------------------------------+
|                        THE CNI REJECTION DISASTER                                 |
+-----------------------------------------------------------------------------------+
| 1. Policy engine blocks Flannel because Flannel is privileged.                    |
|    │                                                                              |
| 2. Flannel Pod is NEVER created.                                                  |
|    │                                                                              |
| 3. Without Flannel, the node has NO overlay network!                              |
|    │                                                                              |
| 4. Worker Node switches to: NotReady                                              |
|    │                                                                              |
| 5. CoreDNS dies. Workload pods cannot acquire IP addresses.                       |
|    │                                                                              |
| 6. TOTAL CLUSTER COLLAPSE!                                                        |
+-----------------------------------------------------------------------------------+
```

---

## 3. The Solution: Namespace Blacklisting via `namespaceSelector`

To guarantee that a cluster cannot commit suicide, Kubernetes provides the **`namespaceSelector`** on `ValidatingWebhookConfiguration` and `MutatingWebhookConfiguration`.

### Blacklisting (`NotIn`) vs. Whitelisting (`In`)

```
+-----------------------------------------------------------------------------------+
|                        BLACKLIST vs. WHITELIST IN ADMISSION                       |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  STRATEGY 1: BLACKLIST (NotIn) ◄── (Mandatory for Cluster Security Policies)      |
|  "Protect EVERYTHING by default, EXEMPT only system infrastructure"              |
|                                                                                   |
|  namespaceSelector:                                                               |
|    matchExpressions:                                                              |
|      - key: kubernetes.io/metadata.name                                           |
|        operator: NotIn                                                            |
|        values: ["kube-system", "kube-public", "gatekeeper-system"]                |
|                                                                                   |
|  - Result: Every newly created developer namespace is protected automatically.    |
|    Developers cannot accidentally bypass security by forgetting a label.          |
|                                                                                   |
|  ───────────────────────────────────────────────────────────────────────────────  |
|                                                                                   |
|  STRATEGY 2: WHITELIST (In / matchLabels) ◄── (Best for Optional Add-Ons)        |
|  "Do nothing by default, APPLY only to namespaces with a specific label"         |
|                                                                                   |
|  namespaceSelector:                                                               |
|    matchLabels:                                                                   |
|      istio-injection: enabled                                                     |
|                                                                                   |
|  - Result: Only namespaces explicitly tagged by an engineer receive the feature.  |
+-----------------------------------------------------------------------------------+
```

### Why Security Standards Mandate Blacklists (`NotIn`)
In cloud-native security, the core axiom is **Secure-by-Default (Zero Trust)**:
* If you used a whitelist (`In`) for security, any developer who forgot to label their namespace would leave their entire application unprotected.
* By using **`NotIn` (blacklisting `kube-system` and the webhook namespace itself)**:
  1. Every new project is protected from day one.
  2. The webhook pod can boot up without waiting for its own approval.
  3. CNI, CoreDNS, and CSI storage drivers remain fully functional.

*Related Reference Module:* [[Reference Notes/0-16_admission_controllers.md|Module 0-16: Kubernetes Admission Controllers & Webhooks]]
