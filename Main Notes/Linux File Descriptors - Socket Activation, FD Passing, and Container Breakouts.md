---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Linux Operating System Architecture and Kernel Mechanics]]"
sub_type: mechanics
source_type: gemini-chat
author: "Antigravity Assistant"
course_title: "Linux Kernel Internals & Systems Programming"
tags:
  - linux/kernel
  - linux/file-descriptors
  - linux/systemd
  - linux/socket-activation
  - linux/cve
  - linux/container-escapes
  - linux/deep-dive
---

# Linux File Descriptors - Socket Activation, FD Passing, and Container Breakouts

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Linux Operating System Architecture and Kernel Mechanics]] > **File Descriptors - Socket Activation, FD Passing, and Container Breakouts**

---

## 🎯 1. The UNIX Paradigm: "Everything is a File"

In the Linux operating system, virtually all input and output streams are abstracted as files:
* Regular files on an ext4/xfs filesystem
* Hardware devices (`/dev/sda`, `/dev/null`, `/dev/mem`)
* Inter-Process Communication pipes
* Network sockets (TCP/UDP) and UNIX domain sockets (`/var/run/docker.sock`)

When a process requests the Linux kernel to open an I/O channel (via `open()`, `socket()`, or `pipe()`), the kernel allocates an entry in its internal system-wide file table and returns a non-negative integer to the process. This integer is a **File Descriptor (FD)**.

---

## 📋 2. The Per-Process File Descriptor Table

Every individual process running on Linux possesses its own private **File Descriptor Table** maintained inside the kernel's `task_struct` (`files_struct`):

```
+---------------------------------------------------------------------------------+
|               PER-PROCESS FILE DESCRIPTOR TABLE (e.g. PID 14820)                |
+---------------------------------------------------------------------------------+
| Slot Index  | Hardwired Destination / Target Object                            |
+-------------+-------------------------------------------------------------------+
|   [ 0 ]     | Standard Input  (stdin)  ──► Keyboard / Input pipe                |
|   [ 1 ]     | Standard Output (stdout) ──► Screen / Normal log stream           |
|   [ 2 ]     | Standard Error  (stderr) ──► Screen / Error log stream            |
|   [ 3 ]     | The first available slot for any newly opened file, socket, pipe! |
|   [ 4 ]     | Next open file (e.g. database connection, config file)            |
|   [ 5 ]     | Next open socket...                                               |
+---------------------------------------------------------------------------------+
```

Because slots `0`, `1`, and `2` are globally standardized for process I/O:
* If a program opens `/etc/hosts`, the kernel places that handle into **Slot 3**.
* If it opens a network socket to a database, it goes into **Slot 4**.
* The program interacts with the kernel by referencing these numbers: `read(3, buffer, 1024)` or `write(1, "hello", 5)`.

---

## 🔌 3. Systemd Socket Activation & The `-H fd://` Protocol

Historically, daemons like `dockerd` created their own communication sockets upon startup:
1. `dockerd` booted up as `root`.
2. It called `bind("/var/run/docker.sock")` and `listen()`.
3. If `dockerd` crashed or took 10 seconds to start, any client attempting to connect received `connect: connection refused`.

### The Systemd Revolution: Socket-Based Activation
`systemd` (PID 1) eliminates startup race conditions by separating services into **`.socket`** and **`.service`** unit files:

```
[ System Boot ]
       │
       ▼
[ systemd (PID 1) reads docker.socket ]
       │
       ├── Calls: socket(), bind("/var/run/docker.sock"), listen()
       │   The socket file is now OPEN and listening in kernel memory!
       │   (Even though the dockerd daemon is NOT running yet!)
       │
       ▼
[ A user runs: "docker ps" ] ──► Sends bytes to /var/run/docker.sock
       │
       ▼
[ Linux Kernel holds incoming bytes in the socket buffer ]
       │
       ▼
[ systemd detects activity on the socket and launches docker.service ]
```

---

### How `-H fd://` Works (The `dup2` Handover)
When `systemd` launches `dockerd`, it does not tell Docker to create a socket. Instead, it passes the **already-open file descriptor** directly into the Docker process:

1. Systemd duplicates the open socket to **File Descriptor 3** using the kernel syscall:
   ```c
   dup2(systemd_socket_fd, 3);
   ```
2. Systemd sets an environment variable: `LISTEN_FDS=1`.
3. Systemd launches the binary with the flag: **`-H fd://`** (Host = File Descriptor).

When Docker boots and sees `-H fd://`, it executes the standard library function `sd_listen_fds()`:
> *"I do not need to bind `/var/run/docker.sock`. systemd has already opened it and handed it to me at **File Descriptor 3**!"*

Docker immediately calls `accept(3, ...)` and begins servicing the client requests that were already waiting in the kernel buffer.

```
[ systemd (PID 1) ]
       │
       │ Spawns dockerd with open socket sitting in Slot 3
       ▼
[ dockerd Process ]
   ├── FD 0: stdin
   ├── FD 1: stdout
   ├── FD 2: stderr
   └── FD 3: /var/run/docker.sock  <── Inherited directly from systemd!
```

#### Why This is an Operational & Security Masterpiece:
* **Zero-Downtime Restarts:** If `docker.service` is restarted during maintenance, the socket `/var/run/docker.sock` **never closes** because it belongs to `systemd` (PID 1). Incoming client commands are buffered by the kernel rather than failing with `connection refused`.
* **Privilege Separation:** `docker.socket` defines permissions (`SocketUser=root`, `SocketGroup=root`, `SocketMode=0660`). Systemd locks down the socket before the daemon process even executes.

---

## 💀 4. Container Escapes via Leaked File Descriptors (CVE-2024-21626 & CVE-2019-5736)

Why must Kubernetes security engineers understand File Descriptors? Because **container escapes occur when open file descriptors leak across namespace boundaries**.

### The Inheritance Vulnerability (`O_CLOEXEC`)
In Linux, when a parent process spawns a child process (`fork()` + `execve()`), **the child inherits all open file descriptors from the parent's table by default**—unless the parent explicitly sets the `O_CLOEXEC` (Close-on-Exec) flag on the descriptor.

---

### Anatomy of CVE-2024-21626 ("Leaky Vessels" in `runc`)

In January 2024, a critical vulnerability was disclosed in `runc` (the underlying OCI runtime for Docker and Kubernetes `containerd`):

1. **The Setup on the Host:** When `runc` prepared a new container, it ran as `root` on the physical worker node.
2. During initialization, `runc` opened internal directories on the **host operating system** (such as `/sys/fs/cgroup`).
3. The Linux kernel assigned that host directory handle to **Slot 7** in `runc`'s file descriptor table.
4. **The Flaw:** `runc` entered the container's Mount Namespace and executed the user's container process (`nginx`), but **forgot to close File Descriptor 7**!

```
[ Host System (Worker Node) ]
  runc opens /sys/fs/cgroup ──► Assigned to FD 7 in host memory
         │
         ▼ runc launches container without closing FD 7
[ Container Process (nginx) ]
  Mount Namespace restricted: can only see /app, /bin, /lib
  BUT in its Process FD Table:
  ├── FD 0: stdin
  ├── FD 1: stdout
  ├── FD 2: stderr
  └── FD 7: [OPEN HOST DIRECTORY HANDLE!] ═════════════════════╗
                                                               ║ (Bypasses chroot!)
                                                               ▼
                                                  [ Physical Host Hard Drive ]
```

#### The Exploit (Container Breakout):
The attacker inside the container did not need to crack kernel encryption or break Linux namespaces. 
They simply instructed the kernel to change directories to the open descriptor:
```c
fchdir(7); // Jump current directory to open File Descriptor 7!
```
From there, the attacker navigated up the directory tree (`../../../../etc/shadow`) and overwrote files on the **host operating system as root**, achieving instant container breakout!

---

### Anatomy of CVE-2019-5736 (`/proc/self/exe` Overwrite)
In this earlier escape, an attacker inside a container accessed `/proc/<runc-pid>/exe`—which is a file descriptor pointing to the **`runc` binary residing on the host node**. By opening this file descriptor for writing, the attacker overwrote the host's `/usr/bin/runc` executable, gaining root execution on the host the next time any container started!

---

## 🛠️ 5. Practical Terminal Inspection & Verification

### Inspecting a Process's Open File Descriptors
Every process exposes its file descriptor table in the `/proc` virtual filesystem under `/proc/<PID>/fd/`:

```bash
# 1. Inspect the open file descriptors of dockerd or containerd:
PID=$(pidof dockerd)
sudo ls -l /proc/$PID/fd/

# Example Output:
# lrwx------ 1 root root ... 0 -> /dev/null
# lrwx------ 1 root root ... 1 -> /dev/null
# lrwx------ 1 root root ... 2 -> /dev/null
# lrwx------ 1 root root ... 3 -> socket:[28914]  <── (The systemd socket!)
# lr-x------ 1 root root ... 4 -> /run/containerd/containerd.sock

# 2. Trace open sockets for a running pod:
POD_PID=$(ps aux | grep nginx | head -n1 | awk '{print $2}')
sudo ls -l /proc/$POD_PID/fd/
```
