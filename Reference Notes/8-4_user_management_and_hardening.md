---
obsidianUIMode: preview
class: reference-note
tier: reference-note
tags:
  - linux/permissions
  - linux/capabilities
  - linux/pam
  - linux/selinux
  - linux/hardening
---

# Module 8-4: User Management, Security & Hardening

**Breadcrumbs:** [[8-Index - Linux and OS|🏠 Linux and OS Index]] > **Security & Hardening**

---

## 🏛️ Account Architectures & POSIX Permissions

### User Account Segmentation
*   **System Users (UID < 1000):** Reserved for system services (e.g. `bin`, `mail`, `nobody`, `systemd-network`). These accounts have no login shells (`/sbin/nologin` or `/usr/sbin/nologin`).
*   **Regular Users (UID >= 1000):** Assigned to human users.
*   **Account Databases:**
    *   `/etc/passwd`: Stores user metadata (username, UID, GID, home directory, default shell).
    *   `/etc/shadow`: Stores salted, hashed user passwords and aging parameters.
    *   `/etc/group`: Stores group metadata and user memberships.

### POSIX Permissions & Special Bits
Files and directories implement access bits for Owner (u), Group (g), and Others (o).

```
   Owner     Group     Others
   r  w  x   r  w  x   r  w  x
   4  2  1   4  2  1   4  2  1
```

*   **Special Bits:**
    1.  **Setuid (4000 / `s` on owner):** When an executable with SUID is run, it executes with the privileges of the file's *owner* (typically root) rather than the executing user. *Example:* `/usr/bin/passwd` needs SUID to modify `/etc/shadow`.
    2.  **Setgid (2000 / `s` on group):**
        *   On files: Executes with the group's privileges.
        *   On directories: Forces any file created inside to inherit the directory's group instead of the user's default group (highly useful for shared folders).
    3.  **Sticky Bit (1000 / `t` on others):** Applies to directories. Restricts file deletion: users can only delete files they own inside the directory, even if they have group write permissions. *Example:* `/tmp` has the sticky bit.

### Umask (User Mask)
A shell variable that defines default permissions removed from newly created files and directories.
*   *Default Base Permissions:* Files are created with `666` (no exec), directories with `777`.
*   *Calculation:* `Base Permissions - Umask = Resulting Permissions`.
    *   If `umask` is `022`: Directories get `755` (`rwxr-xr-x`), files get `644` (`rw-r--r--`).
    *   If `umask` is `027`: Directories get `750`, files get `640`.

---

## 🔒 Advanced Privilege Control: Capabilities & PAM

### Linux Capabilities
To avoid running applications as root (Ring 0 privileges), Linux divides root's power into distinct, fine-grained **Capabilities**. This allows an application to perform a single privileged task without gaining full administrative access.
*   *Common Capabilities:*
    *   `CAP_NET_BIND_SERVICE`: Allows binding to ports below 1024.
    *   `CAP_NET_RAW`: Allows raw socket creation (e.g. `ping`).
    *   `CAP_SYS_TIME`: Allows setting the system clock.
    *   `CAP_SYS_ADMIN`: A broad capability allowing administration tasks (effectively "sub-root").

```bash
# Display capabilities set on a binary
getcap /usr/bin/ping

# Grant a binary the privilege to bind to ports under 1024 without root
setcap 'cap_net_bind_service=+ep' /usr/sbin/nginx
```

### Pluggable Authentication Modules (PAM)
PAM provides a centralized API that decouples application logic from user authentication methods. Applications (like SSH, login, sudo) pass authentication calls to PAM, which evaluates them against rules configured in `/etc/pam.d/`.

*   **PAM Configuration Structure:**
    Each module configuration file follows a standard four-column syntax:
    `Module_Interface  Control_Flag  Module_Path  Module_Arguments`

    1.  **Module Interfaces:**
        *   `auth`: Authenticates the user (passwords, tokens) and establishes credentials.
        *   `account`: Verifies the account status (expiry, time-of-day limits).
        *   `password`: Manages password change requests.
        *   `session`: Handles tasks before/after user session start/termination (mounting home directory, setting ulimits).
    2.  **Control Flags:**
        *   `required`: Module must succeed. If it fails, PAM continues evaluating other modules, but eventually returns a failure.
        *   `requisite`: Module must succeed. If it fails, PAM terminates evaluation immediately and returns a failure (prevents password probing).
        *   `sufficient`: If this module succeeds, and no previous required module has failed, PAM returns success immediately without evaluating remaining modules.
        *   `optional`: Success or failure does not affect the overall login decision.

```bash
# Example SSH PAM configuration (/etc/pam.d/sshd)
# Require standard password authentication AND MFA Google Authenticator
auth       required     pam_unix.so
auth       required     pam_google_authenticator.so
```

---

## 🛡️ Mandatory Access Control: SELinux & AppArmor

POSIX permissions are **Discretionary Access Control (DAC)** (file owners can change permissions at will). **Mandatory Access Control (MAC)** enforces centralized kernel-level security rules that users cannot override.

### SELinux (Security-Enhanced Linux)
SELinux uses a labeling system (Contexts) where every process, file, directory, and port is assigned a security label.
*   **SELinux Context Format:** `user:role:type:sensitivity`
    *   *Type (Targeted Policy):* The most critical field. Governs access via **Type Enforcement**. A process of type `httpd_t` can only access files of type `httpd_sys_content_t` or ports labeled `http_port_t`.
*   **Modes of Operation:**
    *   `Enforcing`: Actively blocks unauthorized actions and logs violations.
    *   `Permissive`: Allows unauthorized actions but logs warning violations (used for debugging/auditing).
    *   `Disabled`: SELinux kernel modules are completely deactivated.
```bash
# Check current SELinux status
sestatus

# Temporarily set SELinux to Permissive mode
setenforce 0

# Restore context of files based on targeted policy directory rules
restorecon -Rv /var/www/html/
```

### AppArmor
A simpler alternative to SELinux. Instead of object labeling, AppArmor uses path-based profiles loaded into `/etc/apparmor.d/` to restrict file, network, and execution access for specific binaries.

---

## 📊 Security Auditing (auditd)

The Linux Audit Daemon (`auditd`) provides kernel-level system monitoring, tracking user actions, system calls, and file modifications based on custom audit rules.

### Audit Rule Configurations
Audit rules are configured in `/etc/audit/rules.d/audit.rules`:
*   *File Watch Rules:* `-w <path> -p <permissions> -k <key_name>`
    *   Permissions: `r` (read), `w` (write), `e` (attribute change), `x` (execute).
*   *Syscall Rules:* `-a always,exit -S <syscall> -k <key_name>`

```bash
# Rule: Watch shadow file for modifications and label as 'identity_theft'
-w /etc/shadow -p wa -k identity_theft

# Rule: Audit all execve system calls (track commands run on system)
-a always,exit -F arch=b64 -S execve -k command_execution

# View audit logs filtering by specific key
ausearch -k identity_theft -i
```

---

## 🔗 RHEL Practical Reference
For practical guides on RHEL user/group administration, special permissions, POSIX Access Control Lists (ACLs), GRUB bootloader password hardening, and basic SELinux type enforcement adjustments, refer to [Module 8-9: Red Hat Enterprise Linux (RHEL) Administration](8-9_redhat_enterprise_linux_administration.md#user-security-and-hardening).

