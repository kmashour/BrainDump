---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kube-apiserver]]"
sub_type: pitfall
sources:
  - "CKA Practice Exam Troubleshooting Section"
  - "K8s Troubleshooting Newsletter"
tags:
  - kubernetes/kube-apiserver
  - kubernetes/pitfall
  - kubernetes/troubleshooting
---

# kube-apiserver - Port Conflicts and Systemd Failure

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[kube-apiserver]] > **Port Conflicts and Systemd Failure**

---

## ⚠️ The Port Conflict Pitfall
A common CKA scenario or production issue is the `kube-apiserver` failing to boot or crashing in a systemd service loop:

### Root Causes
1. **Port `6443` Bind Failure:** Another process is running and binding to port `6443`, or there are leftover zombie apiserver processes binding to it.
2. **Incorrect Certificate Paths:** Modifying `/etc/kubernetes/manifests/kube-apiserver.yaml` with a typo in the client certificate CA paths causes the apiserver to crash loop continuously because it cannot read TLS assets on startup.

### Diagnostics
When the apiserver is down, check:
* **For static pods (kubeadm):**
  Check docker/containerd logs directly on the node since `kubectl` will be completely unresponsive:
  ```bash
  # Check containerd container list
  crictl ps -a | grep apiserver
  # Check logs
  crictl logs <container-id>
  ```
* **For manual systemd setups:**
  ```bash
  systemctl status kube-apiserver
  journalctl -u kube-apiserver -f --no-pager
  ```

### Resolving Port Conflicts
Use `netstat` or `ss` to identify processes blocking the port:
```bash
ss -lntp | grep 6443
# Kill the blocking process
kill -9 <PID>
```
