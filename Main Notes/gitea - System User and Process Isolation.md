---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[gitea]]"
sub_type: architecture
source_type: documentation
source_url: "https://docs.gitea.com/installation/install-from-binary"
author: "Gitea Authors"
course_title: "Linux Service Administration"
against: []
tags:
  - git/gitea
  - security/isolation
---

# gitea - System User and Process Isolation

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[gitea]] > **System User and Process Isolation**

---

## 📑 System User and Process Isolation

To maintain system security on RHEL 8, Gitea executes under an isolated system account rather than `root`.

### 1. System Account Configuration
* **System User (`git`):** Created with a static UID < 1000 to bypass password expiration schedules.
* **Shell Context (`/bin/bash`):** Required because OpenSSH requires a valid shell to parse and route git-receive-pack operations. 

```bash
sudo useradd -r -m -c "Gitea Version Control" -s /bin/bash git
```

---

## 🔐 SSH Multiplexing & Forced Commands

To prevent users from obtaining a full terminal shell access on the host, OpenSSH is configured to intercept and isolate connection commands.

### The Mechanics
When Gitea saves public keys to `/home/git/.ssh/authorized_keys`, it prepends options:
```text
command="/usr/local/bin/gitea serv key-1",no-port-forwarding,no-X11-forwarding ssh-rsa AAAAB...
```

* **`command="..."`:** Tells the SSH Daemon (`sshd`) to ignore client requests and run Gitea's internal routing agent (`gitea serv`) instead.
* **`no-port-forwarding` / `no-X11-forwarding`:** Closes TCP tunneling vectors on the server.

*Read more in [gitea_installation_and_workflows.md](../Reference%20Notes/gitea_installation_and_workflows.md#2-service-identity--process-isolation)*
