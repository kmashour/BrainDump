---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kubelet]]"
sub_type: use-case
source_type: udemy
author: "Mumshad Mannambeth"
course_title: "Certified Kubernetes Administrator (CKA)"
tags:
  - kubernetes/kubelet
  - kubernetes/troubleshooting
---

# kubelet - Inspecting kubelet systemd service logs

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[kubelet]] > **Troubleshooting Logs**

---

## 📑 1. Why Inspect Kubelet Logs?
On a worker node, if `kubectl get nodes` shows the node in a `NotReady` or `Unknown` state, the problem is usually a crashed or misconfigured Kubelet. Since Kubelet runs as a systemd daemon, you must inspect host system logs.

---

## ⚙️ 2. Core Troubleshooting Workflow

### Step 1: Check Service Status
SSH into the failing node and inspect service health:
```bash
systemctl status kubelet
```
If the service is `inactive (dead)` or `failed`, restart it:
```bash
sudo systemctl restart kubelet
```

### Step 2: Extract Systemd Logs
View Kubelet logs using `journalctl`:
```bash
# View last 100 log lines
journalctl -u kubelet -n 100 --no-pager

# Stream logs in real-time
journalctl -u kubelet -f
```

---

## 🔬 3. Common Error Indicators
* **API Server Connection Refused:** `dial tcp 10.10.0.10:6443: connect: connection refused`. (API Server is down or master IP is wrong).
* **Missing Config File:** `unable to load bootstrap-kubeconfig... no such file or directory`.
* **Cgroup Driver Mismatch:** `failed to run Kubelet: misconfigured cgroup driver`. (Alignment failure between kubelet and containerd).

*Read more in [[Reference Notes/0-11_troubleshooting_and_diagnostics.md#2-control-plane-diagnostics-and-static-pod-recovery]]*\n