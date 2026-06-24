---
obsidianUIMode: preview
class: project-playbook
tier: project-playbook
tags:
  - project
  - linux/services
  - linux/databases
  - linux/mariadb
---

# Project: MariaDB Database Installation and User Security

**Breadcrumbs:** [[8-Index - Linux and OS|🏠 Linux and OS Index]] > **Projects** > **MariaDB Database Installation and User Security**

---

## 🎯 Project Objective
This playbook covers installing and initializing a MariaDB relational database engine, executing security hardening configurations, provisioning databases and tables, and configuring specific user privileges mapping.

---

## 💻 Scenario
1.  **Database Host:** `192.168.12.10` running MariaDB server.
2.  **Database Name:** `corp_db`.
3.  **Database User:** `dbuser` with access restricted to host `localhost` and granted full rights to `corp_db`.

---

## 🛠️ Step-by-Step Implementation

### Step 1: Install MariaDB Server Packages
```bash
dnf install -y mariadb-server mariadb
```

### Step 2: Start Service and Secure Installation
```bash
# Start and enable daemon
systemctl enable --now mariadb

# Execute standard security script to lock defaults
mysql_secure_installation
# (Interactive prompts: Set Root Pass: Yes, Remove Anon Users: Yes, Disable Remote Root Login: Yes, Remove Test DB: Yes, Reload Privileges: Yes)
```

### Step 3: Configure Database Schemas, Users, and Privileges
Connect to the database server using root credentials:
```bash
mysql -u root -p
```
Run the following SQL administration sequences:
```sql
-- 1. Create target database schema
CREATE DATABASE corp_db;

-- 2. Inspect created databases
SHOW DATABASES;

-- 3. Provision database user with secure credentials
CREATE USER 'dbuser'@'localhost' IDENTIFIED BY 'DbSecurePass123!';

-- 4. Grant privileges on database tables
GRANT ALL PRIVILEGES ON corp_db.* TO 'dbuser'@'localhost';

-- 5. Commit changes to user privilege caches
FLUSH PRIVILEGES;

-- 6. Verify privileges mapping
SHOW GRANTS FOR 'dbuser'@'localhost';

-- 7. Exit mysql session shell
EXIT;
```

### Step 4: Configure Firewall Ports (Optional for Remote Access)
If remote clients need to query the database server:
```bash
firewall-cmd --permanent --add-service=mysql
firewall-cmd --reload
```

---

## 🔬 Verification & Diagnostics

### Validate Database Login
Test authentication as the newly created user `dbuser`:
```bash
mysql -u dbuser -p -e "SHOW DATABASES;"
```
*Expected Output snippet:*
```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| corp_db            |
+--------------------+
```

### Check Database Health
To review system statistics:
```bash
mysqladmin -u dbuser -p status
```
*Expected Output snippet:*
```
Uptime: 452  Threads: 1  Questions: 4  Slow queries: 0  Opens: 3  Flush tables: 1  Open tables: 26  Queries per second avg: 0.008
```
---
> [!TIP]
> Database connection errors can be diagnosed by checking MariaDB logging outputs in `/var/log/mariadb/mariadb.log`.
