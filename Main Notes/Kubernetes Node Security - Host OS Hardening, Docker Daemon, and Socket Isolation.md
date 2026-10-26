---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Kubernetes Cluster Component Hardening and Communication Security]]"
sub_type: mechanics
source_type: gemini-chat
author: "Antigravity Assistant"
course_title: "CKS Real Exam Blueprint & Host Hardening"
tags:
  - kubernetes/security
  - kubernetes/host-hardening
  - kubernetes/docker-socket
  - kubernetes/systemd
  - kubernetes/cks
  - kubernetes/deep-dive
---

# Kubernetes Node Security - Host OS Hardening, Docker Daemon, and Socket Isolation

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Kubernetes Cluster Component Hardening and Communication Security]] > **Host OS Hardening, Docker Daemon, and Socket Isolation**

---

## 🎯 1. Architectural Role & Threat Surface

In Kubernetes cluster operations, worker and bastion nodes frequently host container engines and debugging tools alongside Kubelet. The Docker daemon (`dockerd`) manages container execution and exposes both local UNIX domain sockets and optional network listeners.

```
[ Non-Root User: 'developer' ] 
               │
               ▼ (Belongs to group 'docker' with rw on /var/run/docker.sock)
[ Talks to Docker UNIX Socket ]
               │
               ▼ (Spins up container mounting host root: -v /:/host)
[ Instant Root Shell on Physical Host OS! ] ❌ Total Cluster Compromise
```

### The Root-Equivalent Vulnerability of `/var/run/docker.sock`
Access to `/var/run/docker.sock` is cryptographically and operationally **equivalent to unrestricted root access on the physical host machine**:
* Any non-root Linux user belonging to the `docker` group can execute:
  ```bash
  docker run -v /:/host -it alpine chroot /host
  ```
  This immediately breaks out of any user permission boundaries, granting an interactive root shell on the host OS.
* From the host root shell, an attacker can extract `/etc/kubernetes/pki/ca.key`, read etcd secrets, or poison static pod manifests.

### The Unauthenticated TCP Listener Threat (Port 2375)
If `dockerd` is configured with `-H tcp://0.0.0.0:2375`:
* Port `2375` transmits unencrypted, unauthenticated HTTP commands.
* Any entity on the local subnet can query the Docker API remotely, launch privileged containers, and seize total control of the node without providing credentials.

---

## 🔬 2. Deep Systems Foundations & Linux Kernel Links

To understand the low-level operating system mechanics behind socket creation, systemd socket activation (`-H fd://`), and container breakouts:

* **Underlying Kernel Architecture:** [[Main Notes/Linux Operating System Architecture and Kernel Mechanics|Linux Operating System Architecture and Kernel Mechanics]]
* **Process Lifecycle & Namespaces:** [[Main Notes/Linux Process Lifecycle - Fork, Clone Syscalls, and PID Namespaces|Process Lifecycle: Fork, Clone Syscalls, and PID Namespaces]]
* **File Descriptors & Socket Activation:** [[Main Notes/Linux File Descriptors - Socket Activation, FD Passing, and Container Breakouts|File Descriptors: Socket Activation, FD Passing, and Container Breakouts]]

---

## 🛡️ 3. The 3 Hardening Actions (CKS Question 13 Blueprint)

To secure a node harboring an exposed Docker daemon, execute the following three remediation actions:

### Action 1: Remove Unprivileged Users from the `docker` Group
Linux uses group permissions on `/var/run/docker.sock` (`rw-rw---- root:docker`). If unauthorized user `developer` belongs to group `docker`, revoke membership immediately:
```bash
sudo gpasswd -d developer docker

# Verify user groups:
id developer
```

---

### Action 2: Restrict Socket Ownership to `root:root`
In modern systemd-managed nodes, the socket is provisioned by `docker.socket`:
1. Inspect `/lib/systemd/system/docker.socket` (or `/usr/lib/systemd/system/docker.socket`).
2. Ensure `SocketGroup` is set to `root` (or remove `SocketGroup=docker`):
   ```ini
   [Socket]
   ListenStream=/var/run/docker.sock
   SocketMode=0660
   SocketUser=root
   SocketGroup=root
   ```

---

### Action 3: Close the Remote TCP Listener (Port 2375)
1. Inspect the main Docker service unit file:
   `/lib/systemd/system/docker.service` (or `/etc/systemd/system/docker.service.d/override.conf`).
2. Locate the `ExecStart=` directive. If it includes `-H tcp://0.0.0.0:2375`, **remove the TCP listener flag**:
   ```ini
   # ❌ INSECURE:
   # ExecStart=/usr/bin/dockerd -H fd:// -H tcp://0.0.0.0:2375

   #  SECURE:
   ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
   ```

---

### Action 4: Reload Systemd & Restart Daemons
Whenever modifying systemd configuration units, reload the system manager configuration and restart **both** the socket and the service:
```bash
sudo systemctl daemon-reload
sudo systemctl restart docker.socket
sudo systemctl restart docker.service
```

---

## 🔍 4. Verification & Testing

```bash
# 1. Verify Port 2375 is completely closed (Returns zero output):
ss -tulpn | grep 2375
# Or:
netstat -tulpn | grep 2375

# 2. Verify /var/run/docker.sock ownership (Must be owned by root:root):
ls -la /var/run/docker.sock
# Expected Output:
# srw-rw---- 1 root root 0 ... /var/run/docker.sock
```
