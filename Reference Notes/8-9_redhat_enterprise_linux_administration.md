---
obsidianUIMode: preview
class: reference-note
tier: reference-note
tags:
  - linux/rhel
  - linux/administration
  - rhcsa
---

# Module 8-9: Red Hat Enterprise Linux (RHEL) Administration

**Breadcrumbs:** [[8-Index - Linux and OS|🏠 Linux and OS Index]] > **RHEL Administration**

---

> [!NOTE]
> **Source Citation & Translation Notice**
> This reference module integrates, translates, and synthesizes 59 transcripts of the Red Hat Enterprise Linux (RHEL 7) Administration course by engineer **Mostafa Hamouda** (Arab Linux Community). Arabic system explanations, CLI interactions, and concept briefs are translated here into high-quality technical English.
> *   **Source Playlist:** [YouTube - Red Hat Enterprise Linux Course](https://www.youtube.com/playlist?list=PL3a3w9-o-9_qfMmVVwZLKk)

---

## Shell Environment and Command History

### CLI Shell Navigation
*   **Prompt Elements:** The prompt typically displays `[username@hostname current_dir]$` for unprivileged users, and `[username@hostname current_dir]#` for root.
*   **Shell Expansion & Globbing:**
    *   `*` matches zero or more characters.
    *   `?` matches exactly one character.
    *   `[a-z]` matches a range of characters.
    *   `{app,web}` braces expand to multiple arguments (e.g. `mkdir -p /srv/{app,web}`).

### History Execution & Configuration
The shell history tracks executed commands for reuse.
*   **Variables:**
    *   `HISTSIZE`: Maximum number of commands stored in memory during active shell session.
    *   `HISTFILESIZE`: Maximum number of commands written to the persistent file (`~/.bash_history`).
    *   `HISTTIMEFORMAT`: Configures timestamp auditing for each command.
*   **Execution Commands:**
    *   `history`: Lists recorded commands with index numbers.
    *   `!!`: Re-executes the immediately preceding command.
    *   `!n`: Re-executes command number `n` in history.
    *   `!grep`: Re-executes the most recent command starting with "grep".
    *   `history -c`: Clears the current shell memory history.
    *   `history -w`: Writes the active session memory history to `~/.bash_history`.

---

## Storage and File Systems

### Partitioning Layouts (MBR vs. GPT)
*   **MBR (Master Boot Record):**
    *   Legacy standard stored in the first 512 bytes of a disk.
    *   Limits disk space to 2 TB.
    *   Supports a maximum of 4 primary partitions (or 3 primary and 1 extended partition containing logical partitions).
*   **GPT (GUID Partition Table):**
    *   Modern standard using globally unique identifiers.
    *   Supports disks larger than 2 TB.
    *   Provides redundancy by writing partition tables at the beginning and end of disk.
    *   Supports up to 128 primary partitions by default on Linux.

### Software RAID Management (mdadm)
*   **Init Arrays:** Use `mdadm` to combine multiple physical drives or partitions into a single logical array.
*   **Command Set:**
    ```bash
    # Create a RAID 5 array with 3 active disks and 1 hot spare
    mdadm --create /dev/md0 --level=5 --raid-devices=3 /dev/sdb1 /dev/sdc1 /dev/sdd1 --spare-devices=1 /dev/sde1

    # Monitor status of the array
    cat /proc/mdstat
    mdadm --detail /dev/md0

    # Stop and assemble arrays
    mdadm --stop /dev/md0
    mdadm --assemble --scan
    ```

### Logical Volume Manager (LVM) Architecture
LVM provides an evolutionary abstraction layer over raw physical disk blocks, enabling virtual block allocation.

```
+-------------------------------------------------------------+
|                     Logical Volume (LV)                     |
|           /dev/vg_system/lv_data (Formatted: XFS/ext4)      |
+-------------------------------------------------------------+
                                |
+-------------------------------------------------------------+
|                      Volume Group (VG)                      |
|                  vg_system (Storage Pool)                    |
+-------------------------------------------------------------+
                                |
+-------------------------------------------------------------+
|                    Physical Volumes (PV)                    |
|          /dev/sdb1                     /dev/sdc1            |
+-------------------------------------------------------------+
```

*   **Abstractions:**
    1.  **Physical Volume (PV):** Maps raw partitions or RAID arrays into LVM blocks.
    2.  **Volume Group (VG):** Pools multiple PVs into a unified storage allocation pool.
    3.  **Logical Volume (LV):** Sub-divides a VG into functional virtual partitions for formatting and mounting.
*   **LVM CLI Command Sequences:**
    ```bash
    # 1. Initialize physical volumes
    pvcreate /dev/sdb1 /dev/sdc1

    # 2. Pool physical volumes into a volume group
    vgcreate vg_data /dev/sdb1 /dev/sdc1

    # 3. Create logical volume from volume group
    lvcreate -L 20G -n lv_files vg_data

    # 4. Expand Volume Group (Add new disk space)
    pvcreate /dev/sdd1
    vgextend vg_data /dev/sdd1

    # 5. Online Expand Logical Volume and Filesystem (XFS/ext4)
    lvextend -L +10G /dev/vg_data/lv_files
    
    # Check filesystem type and resize
    # For ext4:
    resize2fs /dev/vg_data/lv_files
    # For XFS:
    xfs_growfs /mnt/files
    ```

### Persistent Mounting (`/etc/fstab`)
For filesystems to survive reboots, they must be registered in `/etc/fstab`.
*   **Format:** `<device/UUID> <mount_point> <filesystem_type> <options> <dump> <fsck_pass>`
*   **Example Entry:**
    `UUID=a1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5d6 /data xfs defaults,noatime,nodev 0 2`
*   **Validation Command:**
    `mount -a` (Mounts all entry items from `/etc/fstab`. MUST be run after any edit to verify no syntax errors prevent booting).

### SWAP & Quotas
*   **SWAP Space Creation:**
    ```bash
    # Initialize partition/file as SWAP
    mkswap /dev/sdb2
    # Activate SWAP volume
    swapon /dev/sdb2
    # Verify active SWAP memory pools
    swapon -s
    ```
*   **User/Group Quotas:** Limit storage block allocations per user or group on specific mounts.
    *   Configure fstab option flags: `usrquota,grpquota`
    *   Enable quotas: `quotacheck -cugm /mountpoint`, `quotaon /mountpoint`
    *   Edit limits: `edquota username`

---

## Networking and Services

### Interface Configuration Profiles (nmcli)
NetworkManager CLI (`nmcli`) manages interface states and persistent configurations.
*   **Commands:**
    ```bash
    # Show status of all connections
    nmcli connection show

    # Add a persistent static IPv4 profile
    nmcli connection add type ethernet con-name eth-static ifname ens33 ip4 192.168.1.100/24 gw4 192.168.1.1

    # Set DNS parameters on profile
    nmcli connection modify eth-static ipv4.dns "8.8.8.8 8.8.4.4" ipv4.method manual

    # Activate interface configuration profile
    nmcli connection up eth-static
    ```

### NIC Teaming & Bridging
*   **Teaming:** Combines two or more physical network interfaces (slaves) into one virtual interface (team) for high-availability or throughput. Managed via `teamd`.
    ```bash
    # Add team interface
    nmcli connection add type team con-name team0 ifname team0 config '{"runner": {"name": "activebackup"}}'

    # Add slave interfaces to team0
    nmcli connection add type team-slave con-name team0-slave1 ifname ens37 master team0
    nmcli connection add type team-slave con-name team0-slave2 ifname ens38 master team0

    # Bring up the team
    nmcli connection up team0
    ```
*   **Bridging:** Connects separate network segments, enabling virtual machines to bind directly to host networks.
    ```bash
    # Create the bridge interface
    nmcli connection add type bridge con-name br0 ifname br0
    # Bind physical interface to bridge
    nmcli connection add type bridge-slave con-name br0-slave ifname ens33 master br0
    ```

### Network File Sharing (NFS & FTP)
*   **NFS Server Setup:**
    *   Package: `nfs-utils`
    *   Configuration file: `/etc/exports`
    *   Configuration format: `<path> <client_ip/subnet>(options)`
    *   *Example export:* `/srv/nfs 192.168.1.0/24(rw,sync,no_root_squash)`
    *   Run commands: `systemctl enable --now nfs-server`, `exportfs -arv`
*   **FTP (vsftpd) Setup:**
    *   Package: `vsftpd`
    *   Configuration file: `/etc/vsftpd/vsftpd.conf`
    *   Parameters: `anonymous_enable=NO`, `local_enable=YES`, `write_enable=YES`, `chroot_local_user=YES`

### Apache HTTPD Web Hosting
*   **Package:** `httpd`
*   **Configuration Files:** `/etc/httpd/conf/httpd.conf` and additional configurations in `/etc/httpd/conf.d/` (e.g. `ssl.conf`, `vhosts.conf`).
*   **Virtual Hosts:** Set up multiple domain namespaces on a single host.
    ```apache
    # Name-based VirtualHost configuration
    <VirtualHost *:80>
        ServerName www.example.com
        DocumentRoot /var/www/example
        ErrorLog logs/example_error_log
    </VirtualHost>
    ```
*   **SSL/TLS Security:** Requires module `mod_ssl` to handle certificates.
    *   `SSLEngine on`
    *   `SSLCertificateFile /etc/pki/tls/certs/httpd.crt`
    *   `SSLCertificateKeyFile /etc/pki/tls/private/httpd.key`

### BIND DNS Configuration
*   **Package:** `bind`, `bind-utils`
*   **Configuration File:** `/etc/named.conf`
    *   Set listening interfaces: `listen-on port 53 { any; };`
    *   Set query permissions: `allow-query { any; };`
*   **Zone Configurations:** Configure forwarding and reverse lookups in `/var/named/`:
    ```
    $TTL 86400
    @   IN  SOA  ns1.example.com. root.example.com. (
                  2026062301 ; Serial
                  3600       ; Refresh
                  1800       ; Retry
                  604800     ; Expire
                  86400 )    ; Minimum
        IN  NS   ns1.example.com.
    ns1 IN  A    192.168.1.10
    www IN  A    192.168.1.20
    ```

---

## User Security and Hardening

### User/Group Management CLI
*   **Commands:**
    *   `useradd -m -g users -G wheel developer` (Creates user, default group, and supplementary group memberships).
    *   `passwd -e developer` (Forces user password change on next system login session).
    *   `usermod -L developer` / `usermod -U developer` (Locks/Unlocks user login sessions).
    *   `groupadd sysadmins`

### POSIX Permissions, SUID/SGID & Sticky Bits
*   **SUID (Set Owner User ID - Value 4):** Executes binary files with permissions of the file owner (e.g. `passwd` command has SUID set to run as root).
    `chmod u+s /path/to/binary`
*   **SGID (Set Group ID - Value 2):** Runs binaries as the file group owner. Applied to directories: any new sub-file or folder inherits the parent directory's group instead of the creating user's primary group.
    `chmod g+s /path/to/directory`
*   **Sticky Bit (Value 1):** Applied to directories. Only the file owner, directory owner, or root user can delete files inside it, preventing users from purging other users' data (e.g. `/tmp`).
    `chmod +t /path/to/directory`

### POSIX Access Control Lists (ACLs)
Standard permissions only support one user and group. ACLs allow fine-grained access mapping for multiple users.
*   **Command Sequences:**
    ```bash
    # Check current ACL rules on a file
    getfacl /data/reports.txt

    # Grant user 'developer' write permission to file
    setfacl -m u:developer:rw /data/reports.txt

    # Grant group 'sysadmins' read permission to directory
    setfacl -m g:sysadmins:rx /data/reports/

    # Set default ACL on directory for all newly created files
    setfacl -d -m u:developer:rw /data/reports/

    # Purge all custom ACL permissions from file
    setfacl -b /data/reports.txt
    ```

### Boot Security & SELinux Core Tuning
*   **GRUB Menu Lock:** Secure bootloaders from unauthorized parameters manipulation.
    Create a password using `grub2-mkpasswd-pbkdf2` and configure `/etc/grub.d/40_custom` with user credentials. Recompile configuration via `grub2-mkconfig -o /boot/grub2/grub.cfg`.
*   **SELinux Adjustments:**
    *   *Port Configuration:* `semanage port -a -t http_port_t -p tcp 8080` (Allows apache to bind to custom non-standard port 8080).
    *   *Directory Context Rules:* `semanage fcontext -a -t httpd_sys_content_t "/srv/web(/.*)?"` (Registers targeted context). Use `restorecon -R -v /srv/web/` to commit directory changes.

---

## Boot Initialization and Systemd

### SysV Init vs. Systemd Targets
*   **SysV Init Runlevels:** Executed boot scripts sequentially.
    *   `0`: Halt, `1`: Single-User, `3`: Multi-User CLI, `5`: Multi-User GUI, `6`: Reboot.
*   **systemd parallelization:** Launches services concurrently using sockets, reducing boot times.
*   **Target Mappings:**
    *   `poweroff.target` maps to Runlevel 0.
    *   `rescue.target` maps to Runlevel 1.
    *   `multi-user.target` maps to Runlevel 3.
    *   `graphical.target` maps to Runlevel 5.
    *   `reboot.target` maps to Runlevel 6.
*   **Target Management:**
    ```bash
    # Show active target
    systemctl get-default

    # Change active default target persistently
    systemctl set-default multi-user.target

    # Switch target immediately
    systemctl isolate graphical.target
    ```

### Boot Failure Troubleshooting (`rd.break`)
If filesystems fail to load, or root password recovery is needed, interrupt the boot loader sequence:
1.  Reboot system. On the GRUB menu screen, highlight boot entry and press `e` to edit.
2.  Scroll down to kernel arguments line (starts with `linux16` or `linux`). Append parameter: `rd.break`
3.  Press `Ctrl + x` to boot. The system breaks execution before handing over control to systemd and presents an unauthenticated root RAM shell.
4.  Run command sequences:
    ```sh
    # Re-mount root directory read-write
    mount -o remount,rw /sysroot

    # Redirect root filesystem to system directory
    chroot /sysroot

    # Modify root credentials
    passwd root

    # Re-create SELinux auto-relabel flag
    touch /.autorelabel

    # Exit chroot environment and resume boot
    exit
    exit
    ```

---

## Diagnostics and Text Processing

### VIM Navigation
VIM modes of operation:
1.  **Command Mode (Default):** Navigation (`h`, `j`, `k`, `l`), line manipulation (`dd` delete, `yy` copy, `p` paste).
2.  **Insert Mode (`i` / `a`):** Interactive editing.
3.  **Last-line Mode (`:`):** Execution operations (`:wq` save and quit, `:q!` quit ignoring changes).
    *   Find and replace: `:%s/old_text/new_text/g`
    *   Line numbers toggle: `:set nu`, `:set nonu`

### Text Processing & Filtering
Command pipelines scan, filter, and extract file parameters.
*   **`find` Search:** Search files by name, type, size, or permissions.
    `find /var/log/ -name "*.log" -mtime -7 -exec ls -lh {} \;`
*   **`grep` Regular Expressions:**
    `grep -E "^[0-9]{1,3}\." /etc/hosts` (Extracts lines beginning with numbers).
*   **`awk` / `sed` Stream Processing:**
    `awk -F: '$3 >= 1000 {print $1, $6}' /etc/passwd` (Lists user accounts with UID >= 1000).

### Custom Log Rotation
Custom files are integrated into the logrotate configuration daemon `/etc/logrotate.d/`.
```
/var/log/custom-app.log {
    weekly
    rotate 4
    compress
    delaycompress
    missingok
    notifempty
    create 0640 app-user app-group
    postrotate
        /usr/bin/systemctl kill -s HUP custom-app.service >/dev/null 2>&1
    endscript
}
```
*   Parameters:
    *   `weekly`: Rotate log files once per week.
    *   `rotate 4`: Maintain up to 4 historical compressed archives.
    *   `compress`: Apply gzip compression.
    *   `postrotate`: Execute commands after rotation sequence (e.g. reload app).
```
