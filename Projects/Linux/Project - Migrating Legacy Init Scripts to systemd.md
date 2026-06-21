---
obsidianUIMode: preview
class: project-note
tier: project
domains: ["linux"]
concepts_referenced: ["[[init]]"]
difficulty: "beginner"
status: "completed"
---

# Project: Migrating Legacy Init Scripts to systemd

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Projects > **Migrating Legacy Init Scripts to systemd**

---

## 🎯 Project Overview
This project provides a step-by-step migration playbook to convert a legacy **SysV init shell script** (originally running sequentially on older distributions like RHEL 6 or SysV systems) into a modern **systemd Service Unit configuration** (running on modern RHEL 7/8/9+, Debian, or Ubuntu).

By completing this migration:
1. Shell script parsing latency is removed.
2. The service gains declarative dependency resolution.
3. Systemd takes over process auto-respawning and logging integration.
4. Kernel-level sandboxing (e.g. read-only system paths, isolated `/tmp`) is applied.
5. Child processes are tracked using cgroups, preventing zombie/orphan escapes.

---

## 🛠️ Step-by-Step Ingestion & Migration

### 1. Analyzing the Legacy SysV Init Script
Below is a legacy `/etc/init.d/custom-daemon` script written in bash. It manages a custom web service manually using PID files.

```bash
#!/bin/bash
# chkconfig: 345 99 10
# description: Custom Legacy SysV Daemon
# processname: custom-daemon

PIDFILE=/var/run/custom-daemon.pid
EXEC=/usr/local/bin/custom-daemon

start() {
    if [ -f $PIDFILE ]; then
        echo "Service is already running."
    else
        echo "Starting custom-daemon..."
        $EXEC > /var/log/custom-daemon.log 2>&1 &
        echo $! > $PIDFILE
    fi
}

stop() {
    if [ -f $PIDFILE ]; then
        PID=$(cat $PIDFILE)
        echo "Stopping custom-daemon (PID: $PID)..."
        kill -15 $PID
        rm -f $PIDFILE
    else
        echo "Service is not running."
    fi
}

case "$1" in
    start)  start ;;
    stop)   stop ;;
    restart) stop; sleep 2; start ;;
    *) echo "Usage: $0 {start|stop|restart}"; exit 1 ;;
esac
```

#### The Rationale (Why):
This legacy script is error-prone. If the service crashes, the PID file `/var/run/custom-daemon.pid` remains. Subsequent calls to `start` will think it is running, blocking restoration.

---

### 2. Creating the Modern systemd Unit Configuration
Write a declarative systemd unit configuration file to replace the legacy logic.

#### The Answer:
Create and edit `/etc/systemd/system/custom-daemon.service`:
```ini
[Unit]
Description=Custom Web Daemon (Migrated from SysV)
After=network.target

[Service]
Type=simple
User=nobody
Group=nogroup
ExecStart=/usr/local/bin/custom-daemon
StandardOutput=journal
StandardError=journal
Restart=on-failure
RestartSec=5

# Hardening / Sandboxing
PrivateTmp=yes
ProtectSystem=strict
ProtectHome=yes
NoNewPrivileges=yes

[Install]
WantedBy=multi-user.target
```

#### The Assumptions:
* `/usr/local/bin/custom-daemon` runs in the foreground by default (which fits `Type=simple`).
* You are deploying on systemd-compliant systems.

#### The Rationale (Why):
* **`Type=simple`:** Systemd assumes the daemon starts immediately and handles execution. No double-fork daemonization scripts are needed.
* **`Restart=on-failure`:** Automatically monitors and restarts the service if it exits with a non-zero status.
* **`StandardOutput=journal`:** Standard output logs are automatically redirected to `journald`, removing the need for manual redirect scripts (`> /var/log/...`).
* **Hardening:** `ProtectSystem=strict` mounts system bin directories `/usr` and `/etc` as read-only for this process, preventing malicious shell inject exploits.

---

### 3. Transitioning the Service Commands
Deregister the legacy init script and load the new systemd unit.

#### The Answer:
```bash
# 1. Stop and remove the old script from SysV control
sudo service custom-daemon stop
sudo rm /etc/init.d/custom-daemon

# 2. Force systemd to reload its configuration and parse the new unit
sudo systemctl daemon-reload

# 3. Enable the unit to start at boot, and start it now
sudo systemctl enable --now custom-daemon.service
```

---

## 🔍 Verification & Diagnostics

### 1. Auditing the Process Tree & Control Group
Verify that systemd is managing and tracking the daemon inside a cgroup structure:
```bash
systemd-cgls --unit custom-daemon.service
```
*Expected Output:*
```
Directory /sys/fs/cgroup/system.slice/custom-daemon.service:
└─14820 /usr/local/bin/custom-daemon
```

---

### 2. Analyzing Logs with journalctl
Query the service's log buffer using `journalctl`:
```bash
journalctl -u custom-daemon.service -e
```
*Expected Output:*
```
Jun 22 00:54:12 server systemd[1]: Started Custom Web Daemon (Migrated from SysV).
Jun 22 00:54:13 server custom-daemon[14820]: Initializing web listener on port 8080...
Jun 22 00:54:13 server custom-daemon[14820]: Server is ready.
```
