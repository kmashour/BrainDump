---
obsidianUIMode: preview
class: reference-note
tier: reference-note
tags:
  - linux/automation
  - linux/scripting
  - ansible
  - linux/backups
---

# Module 8-8: Enterprise Automation, Backup & Cloud Integration

**Breadcrumbs:** [[8-Index - Linux and OS|🏠 Linux and OS Index]] > **Automation & Cloud**

---

## 🏛️ Scripting and Systems Automation Best Practices

Automated operations require robust error handling and defensive coding strategies to prevent commands from running in undefined states.

### 1. Defensive Shell Scripting (Bash)
Always include initialization flags to control script execution stability:
*   `set -e`: Terminate execution immediately if any command returns a non-zero exit status.
*   `set -u`: Terminate if the script attempts to evaluate an uninitialized shell variable.
*   `set -o pipefail`: Propagates pipeline errors (non-zero exits in pipe sequences will fail the entire line).

```bash
#!/bin/bash
set -euo pipefail

# Define variables and check parameters
BACKUP_DIR="${1:-/var/backups}"
SOURCE_DIR="/var/www/html"

# Run backup using rsync
if [ -d "$SOURCE_DIR" ]; then
    rsync -aq --delete "$SOURCE_DIR" "$BACKUP_DIR"
    echo "Backup completed successfully."
else
    echo "Error: Source directory does not exist." >&2
    exit 1
fi
```

### 2. Python System Administration
For complex orchestration tasks, Python provides structured libraries:
*   `subprocess`: Spawns OS shell commands safely, avoiding shell injections by avoiding `shell=True` unless arguments are sanitized.
*   `pathlib`: Modern OOP-based file system path manipulation.

```python
#!/usr/bin/env python3
import subprocess
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def get_disk_utilization(partition="/"):
    try:
        # Run df command safely
        result = subprocess.run(['df', '-h', partition], capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split('\n')
        if len(lines) >= 2:
            usage = int(lines[1].split()[4].rstrip('%'))
            return usage
    except Exception as e:
        logging.error(f"Failed to check disk usage: {e}")
    return None

if __name__ == "__main__":
    usage = get_disk_utilization()
    if usage and usage > 90:
        logging.warning(f"Disk partition usage is critical: {usage}%")
```

---

## ⚙️ Configuration Management: Ansible vs. Puppet

Configuration management structures configurations declaratively, ensuring systems converge on a desired state (Idempotency).

### 1. Ansible (Agentless Push Model)
Ansible uses SSH (or WinRM) to push transient python scripts to target nodes, executing them and exiting.
*   *Pros:* No agent daemon running on target nodes; fast initialization.
*   *Key Concepts:* Playbooks (YAML declarative configurations), Inventories, Roles.
```yaml
# Example Ansible Playbook (installing and securing nginx)
- name: Web Server Hardening Playbook
  hosts: webservers
  become: yes
  tasks:
    - name: Ensure nginx is installed
      apt:
        name: nginx
        state: present
        update_cache: yes

    - name: Copy secured configuration template
      template:
        src: templates/nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      notify: Reload Nginx Service

  handlers:
    - name: Reload Nginx Service
      service:
        name: nginx
        state: reloaded
```

### 2. Puppet (Agent-Based Pull Model)
Puppet uses local agent daemons running on target nodes that periodically poll a centralized Puppet Server (Master) to pull compiled catalog manifests and apply them.

---

## 💾 System Backup & Disaster Recovery (DR) Scenarios

Choosing the correct backup tool depends on the required backup speed, granularity, and restoration targets:

### 1. High-Level File Sync: `rsync`
Efficiently syncs files and directories locally or across networks, only copying modified blocks.
```bash
# Sync directories preserving permissions, links, and times recursively (-a)
# Compress data (-z), delete destination files no longer in source (--delete)
rsync -az --delete /var/www/html/ /mnt/backup/web/
```

### 2. File Archive Compilation: `tar`
Compiles multiple directories and files into a single, compressed archive file.
```bash
# Create a compressed Gzip archive (-zcf)
tar -zcf web_backup.tar.gz /var/www/html/
```

### 3. Block-Level Imaging: `dd`
Performs low-level, exact block-by-block copying of disk images or storage devices. Crucial for forensic capture, disk migration, or clone replication.
```bash
# Clone primary disk /dev/sda to secondary backup disk /dev/sdb
# bs=4M speeds up read/write blocks; status=progress prints copy speed
dd if=/dev/sda of=/dev/sdb bs=4M status=progress
```

---

## ☁️ Cloud Provisioning & Hybrid Integration (`cloud-init`)

`cloud-init` is the industry-standard multi-distribution package for automating early-stage initialization of cloud instances during boot (reads metadata from AWS EC2, OpenStack, etc.).

```yaml
# cloud-config metadata snippet
# Configures system users, SSH keys, and installs default packages during first boot
users:
  - name: sysadmin
    groups: sudo, admin
    shell: /bin/bash
    sudo: ['ALL=(ALL) NOPASSWD:ALL']
    ssh_authorized_keys:
      - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC8...

packages:
  - fail2ban
  - jq
  - prometheus-node-exporter

runcmd:
  - [ systemctl, daemon-reload ]
  - [ systemctl, enable, --now, prometheus-node-exporter ]
```
