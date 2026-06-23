---
obsidianUIMode: preview
class: reference-note
tier: reference-note
tags:
  - linux/init
  - linux/systemd
  - container/init
---

# Module 8-5: System Services, Initialization & Daemonization

**Breadcrumbs:** [[8-Index - Linux and OS|🏠 Linux and OS Index]] > **Initialization & Services**

---

## 🏛️ Evolution of Initialization Systems

The system initialization process (init) is the first user-space process spawned by the Linux kernel (PID 1) upon boot. Over time, init has evolved to handle modern hardware and parallel processing constraints.

### 1. Traditional SysV Init
*   **Architecture:** Sequential, script-driven initialization.
*   **Runlevels:** Defines system modes (e.g. `0` Halt, `1` Single-user, `3` Multi-user CLI, `5` Multi-user Graphical, `6` Reboot).
*   **Startup Procedure:** Governed by `/etc/inittab`. Init runs shell scripts sequentially from `/etc/rc.d/rcX.d/` (where `X` is the target runlevel). Filenames starting with `S` are started; those starting with `K` are stopped.
*   **Limitation:** Very slow boot times. If a network configuration script blocks waiting for DHCP, all subsequent services (like web or database engines) are blocked.

### 2. Upstart
*   **Architecture:** Event-driven initialization.
*   **Startup Procedure:** Services start or stop in response to system events (e.g. "network-up", "disk-mounted", "hardware-inserted").
*   **Advantages:** Enabled parallel service execution and automatic service respawning.

### 3. systemd
*   **Architecture:** Object-based dependency graphs.
*   **Advantages:**
    *   **Parallel Execution:** Starts services concurrently.
    *   **Socket Activation:** Creates network/IPC sockets *before* the service starts, buffering client requests while the service loads, starting the target daemon on demand.
    *   **Cgroups Tracking:** Places services in cgroups to track child processes, preventing orphaned processes.
    *   **Targets:** Replaced runlevels with target units (e.g. `multi-user.target`, `graphical.target`).

---

## ⚙️ systemd Architecture & Configuration

Everything managed by systemd is classified as a **Unit** (configured using declarative `.ini` file configurations).

### Unit Types
*   `*.service`: Configures system services/daemons.
*   `*.socket`: Configures network ports or IPC sockets.
*   `*.target`: Groups units together to establish boots states.
*   `*.timer`: Configures calendar or relative time-triggered execution (replaces cron).
*   `*.mount`: Automates file system mount configurations.

### Anatomy of a Service Unit File
```ini
[Unit]
Description=Custom Web Engine Daemon
After=network.target                  # Ordering: start after network is active
Requires=postgresql.service           # Hard Dependency: stop this if postgresql fails

[Service]
Type=simple                           # Service lifecycle tracking model
User=webadmin
Group=webadmin
ExecStart=/usr/local/bin/web_app --port 8080
Restart=always                        # Auto-respawn behavior
RestartSec=5                          # Delay before respawn attempt

# systemd Sandboxing & Security Enforcement
PrivateTmp=yes                        # Creates isolated mount namespace for /tmp
ProtectSystem=strict                  # Mounts system binaries (/usr, /etc) as read-only
ProtectHome=yes                       # Hides /home and /root directories
NoNewPrivileges=yes                   # Prevents privilege escalation (SUID bypass)

[Install]
WantedBy=multi-user.target            # Target link created when 'systemctl enable' is run
```

### Dependency Ordering vs. Requirements
*   **`Requires=`:** Hard dependency. If unit `A` requires unit `B`, starting `A` will start `B`. If `B` fails or stops, `A` stops.
*   **`Wants=`:** Soft dependency. Starting `A` starts `B`. If `B` fails, `A` remains running.
*   **`After=` / `Before=`:** Simple execution ordering. Does not imply dependency. If `A` is ordered `After` `B`, starting both simultaneously ensures systemd waits for `B` to finish loading before initializing `A`.
*   **`Conflicts=`:** Negative dependency. If `A` conflicts with `B`, starting `A` immediately stops `B`.

---

## 🔄 Daemonization & The PID 1 Container Problem

### Standard Daemonization Mechanics (Double-Fork)
In classic Linux systems, a process daemonizes (runs in the background) by executing a double-fork sequence:
1.  **First Fork:** Clones the process. The parent exits, placing the child in the background.
2.  **`setsid()`:** The child calls `setsid()` to detach from the terminal and become a session leader.
3.  **Second Fork:** Clones the process again. The parent exits. The grandchild cannot acquire a controlling terminal.
4.  **Redirection:** Closes standard inputs, outputs, and errors (`stdin`, `stdout`, `stderr`), redirecting them to `/dev/null` or logs, and changes directory to `/`.

### The PID 1 Container Problem (Zombie Reaping)
In operating systems, the first process (PID 1) must perform two critical OS operations:
1.  **Reaping Orphaned Processes (Zombies):** When a child process terminates, it becomes a zombie until its parent calls `wait()`. If the parent dies before the child, the child is adopted by PID 1. PID 1 must call `wait()` to clear the zombie from the system PID table.
2.  **Signal Forwarding:** Signals sent to the container (`SIGTERM`, `SIGINT`) are delivered to PID 1. If PID 1 is not configured to forward these signals, the application processes running inside will never receive termination signals, causing containers to hang on stops (terminated via `SIGKILL` after a timeout).

#### Container Implications
When running standard applications (Node, Python, Java) directly as the container entrypoint, they run as PID 1. They are not built to act as init systems, so they:
*   Do not reap zombie processes, causing the PID table to exhaust over time.
*   Do not handle or forward standard system signals.

```
+-------------------------------------------------------+
|  Normal Host: Init (systemd) [PID 1]                  |
|     L__ Orphans adopted & reaped automatically        |
+-------------------------------------------------------+
|  Poor Container: Python App [PID 1]                   |
|     L__ Python ignores zombie children -> Zombie Leak |
+-------------------------------------------------------+
|  Good Container: tini / dumb-init [PID 1]             |
|     L__ Reaps zombies & forwards SIGTERM to Python    |
+-------------------------------------------------------+
```

*   **Solution:** Use lightweight init scripts (like `tini` or `dumb-init`) as the container entrypoint to act as PID 1, spawning the application process as a child.
```dockerfile
# Dockerfile Example
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["python3", "app.py"]
```

---

## 🔗 RHEL Practical Reference
For practical guides on RHEL system boot process tracking, modifying systemd targets, recovering from boot failures with `rd.break` root redirection, and custom unit creations, refer to [Module 8-9: Red Hat Enterprise Linux (RHEL) Administration](8-9_redhat_enterprise_linux_administration.md#boot-initialization-and-systemd).

