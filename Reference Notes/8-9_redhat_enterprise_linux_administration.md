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
> This reference module integrates, translates, and synthesizes 65 transcripts of the Red Hat Enterprise Linux (RHEL 7) Administration course by engineer **Mostafa Hamouda** (Arab Linux Community). Arabic system explanations, CLI interactions, and concept briefs are translated here into high-quality technical English.
> *   **Source Playlist:** [YouTube - Red Hat Enterprise Linux Course (PLy1Fx2HfcmWBpD_PI4AQpjeDK5-5q6TG7)](https://www.youtube.com/playlist?list=PLy1Fx2HfcmWBpD_PI4AQpjeDK5-5q6TG7)

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
    # Wipe partition signatures before building
    dd if=/dev/zero of=/dev/sdb bs=1M count=10

    # Create a RAID 5 array with 3 active disks and 1 hot spare
    mdadm --create /dev/md0 --level=5 --raid-devices=3 /dev/sdb1 /dev/sdc1 /dev/sdd1 --spare-devices=1 /dev/sde1

    # Monitor status of the array
    cat /proc/mdstat
    mdadm --detail /dev/md0

    # Stop and clean up arrays
    mdadm --stop /dev/md0
    mdadm --zero-superblock /dev/sdb1 /dev/sdc1 /dev/sdd1 /dev/sde1  # Wipe RAID metadata
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

    # 6. Decommissioning LVM Cleanly
    lvremove /dev/vg_data/lv_files   # Remove Logical Volume
    vgremove vg_data                 # Remove Volume Group
    pvremove /dev/sdb1 /dev/sdc1     # Remove Physical Volumes
    ```

### Persistent Mounting (`/etc/fstab`)
For filesystems to survive reboots, they must be registered in `/etc/fstab`.
*   **Format:** `<device/UUID> <mount_point> <filesystem_type> <options> <dump> <fsck_pass>`
*   **Example Entry:**
    `UUID=a1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5d6 /data xfs defaults,noatime,nodev 0 2`
*   **Validation Command:**
    `mount -a` (Mounts all entry items from `/etc/fstab`. MUST be run after any edit to verify no syntax errors prevent booting).
*   **Mount Cache Troubleshooting:**
    If you manually modify `/etc/fstab` and subsequent manual mount commands fail due to resource conflicts or systemd maintaining cache, flush systemd's cache:
    `systemctl daemon-reload`


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

## Package Management (YUM and DNF)

Package managers automate software distribution and local dependency resolution (resolving "dependency hell") by querying remote or local repository database metadata (`repodata` XML files).

### YUM Command Set
*   **Core Commands:**
    ```bash
    yum search vim                    # Query packages matching string
    yum info httpd                    # Display metadata, description, and source repo
    yum install httpd                 # Install package and resolve dependencies
    yum remove httpd                  # Uninstall package (does not strip shared deps)
    yum update                        # Perform system-wide package upgrades
    yum update tzdata                 # Update a single package
    yum provides /etc/mime.types      # Identify which package provides a specific file
    ```
*   **Group Package Management:**
    ```bash
    yum groups list                   # List available group packages
    yum groups install "Web Server"   # Install an entire group stack in one command
    ```

### Cache Configuration & Cleaning
By default, YUM deletes downloaded RPM binaries after installation. To change this behavior, edit `/etc/yum.conf`:
```ini
[main]
keepcache=1                           # Retain RPM cache in /var/cache/yum/
```
*   **Cache Commands:**
    ```bash
    yum clean all                     # Clear all cached package databases and files
    yum clean packages                # Delete cached RPM files
    yum clean metadata                # Clear cached XML repository index files
    ```

### Auditing and Rollback (YUM History)
YUM tracks all package transactions in a database, allowing administrators to audit modifications and revert installation states.
*   **Command Set:**
    ```bash
    yum history                       # List transaction IDs, dates, and actions
    yum history info 11               # View details of transaction ID 11
    yum history undo 11               # Roll back transaction ID 11 (purges all installed files)
    yum history redo 11               # Re-apply transaction ID 11
    ```

### DNF (Dandified YUM)
DNF is the modern successor to YUM (the default package manager starting in RHEL 8). DNF implements a cleaner codebase, faster dependency resolution, and remains fully backward-compatible with YUM command syntax.

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

#### DNS Replication (Master/Slave Zone Transfers)
Deploying a secondary nameserver distributes traffic load and provides failover redundancy.
*   **Triggers & SOA Parameters:**
    Replication updates are determined by the Start of Authority (SOA) parameters:
    ```
    $TTL 86400
    @   IN  SOA  ns1.example.com. root.example.com. (
                  2026062401 ; Serial (Format: YYYYMMDDNN. Must increment on Master updates)
                  3600       ; Refresh (Time in seconds Slave waits before polling Master)
                  1800       ; Retry (Time Slave waits after a failed refresh poll)
                  604800     ; Expire (Max time Slave keeps cached zone without Master connection)
                  86400 )    ; Minimum / Negative TTL (Caching time for failed lookups)
    ```

*   **Master Server Zone Block (`/etc/named.conf`):**
    ```named
    zone "example.com" IN {
        type master;
        file "example.com.db";
        allow-transfer { 192.168.200.130; };   # Secondary DNS Server IP
        also-notify { 192.168.200.130; };      # Push updates automatically
    };
    ```

*   **Slave Server Zone Block (`/etc/named.conf`):**
    *   *Note:* The zone database file must reside in the `slaves/` subdirectory (`/var/named/slaves/`) because the `named` system account only has write permissions to this directory.
    ```named
    zone "example.com" IN {
        type slave;
        file "slaves/example.com.db";
        masters { 192.168.200.128; };          # Primary DNS Server IP
    };
    ```

*   **Verification:**
    Check the system logs on the Slave server to verify that the zone transfer succeeded:
    `tail -n 50 /var/log/messages` (Verify completion: `transfer of 'example.com/IN' from 192.168.200.128#53: Transfer completed`).


---

## Centralized Authentication and Identity Management

### FreeIPA Client & Server Enrollment
FreeIPA (Identity, Policy, Audit) is an integrated centralized directory service that combines LDAP (directory), Kerberos (authentication), NTP (time synchronization), and DNS.

*   **Sizing Prerequisite:** FreeIPA servers run Java/Tomcat and require at least **2GB RAM** to prevent service crashes.
*   **Host Prep & DNS Configuration:**
    Ensure both servers have persistent static IPs and resolve each other locally.
    ```bash
    # On Server
    hostnamectl set-hostname server.example.com
    nmcli connection modify eth0 ipv4.addresses 192.168.153.150/24 ipv4.gateway 192.168.153.2 ipv4.dns 8.8.8.8 ipv4.method manual
    nmcli connection up eth0

    # On Client
    hostnamectl set-hostname client1.example.com
    nmcli connection modify eth0 ipv4.addresses 192.168.153.151/24 ipv4.gateway 192.168.153.2 ipv4.dns 8.8.8.8 ipv4.method manual
    nmcli connection up eth0
    ```
    Add host entries to `/etc/hosts`:
    ```
    192.168.153.150 server.example.com server
    192.168.153.151 client1.example.com client1
    ```
*   **Server Installation:**
    ```bash
    yum install ipa-server
    ipa-server-install  # Choose integrated DNS: no | realm: EXAMPLE.COM
    ```
*   **Kerberos Auditing & User Provisioning:**
    ```bash
    kinit admin                    # Authenticate as administrator
    klist                          # View active ticket expiration
    ipactl status                  # Check state of IPA daemons
    ipa user-add                   # Provision new user (e.g. login: developer)
    ipa passwd developer           # Assign initial password
    ```
*   **Client Enrollment:**
    ```bash
    yum install ipa-client
    ipa-client-install             # Server: server.example.com | Domain: example.com
    authconfig --enablemkhomedir --update   # Enable automatic home dir creation on login
    ```

### Microsoft Active Directory Integration (realmd)
The `realmd` daemon simplifies joining Linux clients to an existing Active Directory domain, coordinating SSSD, Samba, Kerberos, and PAM configurations under a single tool.

*   **Setup Prerequisites:** Set the DNS server of the Linux client to point directly to the AD Domain Controller (e.g. `192.168.153.148`):
    ```bash
    nmcli connection modify eth0 ipv4.dns 192.168.153.148
    nmcli connection up eth0
    hostnamectl set-hostname client1.example.com
    ```
*   **Discovery and Enrollment:**
    ```bash
    # Discover AD domain
    realm discover example.com

    # Install required integration packages
    yum install sssd adcli samba-common-tools oddjob oddjob-mkhomedir openldap-clients

    # Join the AD Domain
    realm join example.com -U Administrator  # Prompts for Domain Admin credentials

    # Confirm domain registration
    realm list
    ```
*   **Authentication Check:**
    ```bash
    su - developer@example.com   # Log in on Linux with AD credentials
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
Standard Linux UGO (User-Group-Others) permissions only support assigning one owner and one group. Granting write access to non-owners via "Others" compromises the principle of least privilege. ACLs allow fine-grained access mapping for multiple users and groups.

#### Compatibility & Mounting
*   **Kernel Check:** Verify that the running kernel supports ACLs:
    `grep -i acl /boot/config-$(uname -r)` (Ensure `CONFIG_EXT4_FS_POSIX_ACL=y` and `CONFIG_XFS_FS_POSIX_ACL=y` are present).
*   **Superblock defaults:** Modern filesystems (like XFS and ext4 on RHEL 7) compile ACL support by default. Verify using:
    `dumpe2fs /dev/sdb1 | grep "Default mount options"` (Look for `acl`).
*   **Manual Mount Flags:** For older filesystems lacking superblock defaults, enable ACL support at mount:
    ```bash
    mount -o acl /dev/sdb1 /srv
    mount -o remount,acl /srv
    # Persistent mount (/etc/fstab):
    /dev/sdb1 /srv ext4 defaults,acl 0 0
    ```

#### ACL Management CLI
*   **Command Sequences:**
    ```bash
    # Check current ACL rules on a file
    getfacl /data/reports.txt

    # Grant user 'developer' write permission to file
    setfacl -m u:developer:rw /data/reports.txt

    # Grant group 'sysadmins' read permission to directory
    setfacl -m g:sysadmins:rx /data/reports/

    # Set default ACL on directory for all newly created files (Inheritance)
    setfacl -d -m u:developer:rw /data/reports/

    # Recursively apply ACLs to existing files and directories
    setfacl -R -m u:developer:rw /data/reports/

    # Combine recursive and default rules for inheritance
    setfacl -R -d -m u:developer:rw /data/reports/

    # Remove specific ACL entry for user 'developer'
    setfacl -x u:developer /data/reports.txt

    # Purge all custom ACL permissions from file (restores UGO permissions)
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

    # Prevent a service from starting (manually or automatically)
    systemctl mask httpd          # Symlinks unit file to /dev/null

    # Restore service enablement control
    systemctl unmask httpd
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
