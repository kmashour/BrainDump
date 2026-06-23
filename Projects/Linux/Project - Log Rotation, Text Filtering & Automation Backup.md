---
obsidianUIMode: preview
class: project-playbook
tier: project-playbook
tags:
  - project
  - linux/diagnostics
  - linux/automation
---

# Project: Log Rotation, Text Filtering & Automation Backup

**Breadcrumbs:** [[8-Index - Linux and OS|🏠 Linux and OS Index]] > **Projects** > **Log Rotation, Text Filtering & Automation Backup**

---

## 🎯 Project Objective
This playbook details configuring custom system log rotations (`logrotate`), text filtering pipelines configuration using `grep`/`awk`/`sed` to scan files, and backup script scheduling using `cron` automation.

---

## 💻 Scenario
A custom web service writes unstructured system logs directly to `/var/log/nginx/app-access.log`.
1.  Configure a weekly log rotation pattern: compress files, keep up to 8 backlogs, and signal the service to reload.
2.  Create an automated nightly backup script (`/srv/scripts/backup.sh`) that pools log archives to `/backup/` directory.
3.  Implement a diagnostic pipeline to parse the log file and extract a report of all HTTP 500 error responses from unique client IPs.

---

## 🛠️ Step-by-Step Implementation

### Step 1: Configure Custom Log Rotation
Add targeted configurations under `/etc/logrotate.d/`.
```bash
# Create custom rotation profile
cat <<EOF > /etc/logrotate.d/nginx-custom-app
/var/log/nginx/app-access.log {
    weekly
    rotate 8
    compress
    delaycompress
    missingok
    notifempty
    create 0640 nginx nginx
    postrotate
        /usr/bin/systemctl reload nginx >/dev/null 2>&1
    endscript
}
EOF

# Dry-run test logrotate configuration to verify syntaxes
logrotate -d /etc/logrotate.d/nginx-custom-app
```

### Step 2: Implement and Schedule Automation Backup Script
Write a bash script that compresses directories and cleans up old backlogs.
```bash
# Create directory structure
mkdir -p /srv/scripts
mkdir -p /backup

# Write backup shell script
cat <<'EOF' > /srv/scripts/backup.sh
#!/bin/bash
# Enterprise Backup Automation Script
BACKUP_DIR="/backup"
SOURCE_DIR="/var/log/nginx"
DATE=$(date +%F_%H-%M-%S)
ARCHIVE="nginx_logs_$DATE.tar.gz"

# Create archive
tar -czf "$BACKUP_DIR/$ARCHIVE" -C "$SOURCE_DIR" .

# Maintain cleanup threshold: Purge files older than 30 days
find "$BACKUP_DIR" -type f -name "nginx_logs_*.tar.gz" -mtime +30 -exec rm -f {} \;
EOF

# Grant execution permissions
chmod +x /srv/scripts/backup.sh

# Register script to cron (schedule at 2:00 AM nightly)
(crontab -l 2>/dev/null; echo "0 2 * * * /srv/scripts/backup.sh") | crontab -
```

### Step 3: Implement Diagnostic Text Processing Pipelines
Extract operational reports from logs using stream operations.
```bash
# Scenario Access Log Structure:
# 192.168.1.15 - - [23/Jun/2026:12:30:45 +0300] "GET /api/v1/resource HTTP/1.1" 500 512

# Execute diagnostic:
# - Filter lines with status '500'
# - Print the first field (client IP)
# - Sort and unique count matches
awk '$9 == 500 {print $1}' /var/log/nginx/app-access.log | sort | uniq -c | sort -nr
```

---

## 🔬 Verification & Diagnostics
```bash
# 1. Force log rotation manually to verify execution
logrotate -f /etc/logrotate.d/nginx-custom-app
ls -la /var/log/nginx/

# 2. Verify registered cron schedules
crontab -l

# 3. Dry-run execute backup script and check archives creation
/srv/scripts/backup.sh
ls -lh /backup/
```
*Expected logrotate Output check:* The `/var/log/nginx/` directory should contain a compressed archive file `app-access.log.1.gz` after force rotation.
