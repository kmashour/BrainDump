---
obsidianUIMode: preview
class: project-playbook
tier: project-playbook
tags:
  - project
  - linux/services
  - linux/apache
---

# Project: Apache Web Server Deployment, Virtual Hosts, and Directory Security

**Breadcrumbs:** [[8-Index - Linux and OS|🏠 Linux and OS Index]] > **Projects** > **Apache Web Server Deployment, Virtual Hosts, and Directory Security**

---

## 🎯 Project Objective
This playbook details installing Apache HTTPD, configuring port/name-based Virtual Hosts, securing sub-directories using basic HTTP password authentication, and configuring SSL/TLS encryption.

---

## 💻 Scenario
Set up an Apache server hosting two separate domains on a single host:
1.  **Site A:** `www.engineering.local` hosting engineers files.
2.  **Site B:** `www.finance.local` hosting financial reports. This site must run exclusively on port 443 with self-signed SSL certificates, and its sub-directory `/var/www/finance/reports` must require HTTP password authentication for user `admin`.

---

## 🛠️ Step-by-Step Implementation

### Step 1: Install httpd and Secure SSL Modules
```bash
# Install packages
yum install -y httpd mod_ssl openssl

# Enable service
systemctl enable --now httpd
```

### Step 2: Generate Self-Signed SSL Certificates
Generate encryption keys for `www.finance.local`.
```bash
# Create directory
mkdir -p /etc/httpd/ssl/

# Generate SSL Private Key and Certificate Signing Request (CSR)
openssl req -new -nodes -x509 \
  -subj "/C=US/ST=State/L=City/O=Finance/CN=www.finance.local" \
  -days 365 \
  -keyout /etc/httpd/ssl/finance.key \
  -out /etc/httpd/ssl/finance.crt

# Apply strict permissions
chmod 600 /etc/httpd/ssl/finance.key
```

### Step 3: Configure Virtual Hosts and Directory Protections
Create custom configurations under `/etc/httpd/conf.d/vhosts.conf`.
```bash
# Create Site document roots
mkdir -p /var/www/engineering
mkdir -p /var/www/finance/reports

# Create basic HTML index pages
echo "<h1>Welcome to Engineering Portal</h1>" > /var/www/engineering/index.html
echo "<h1>Secure Finance Reports</h1>" > /var/www/finance/reports/index.html

# Set directory permissions and SELinux contexts
chown -R apache:apache /var/www/
semanage fcontext -a -t httpd_sys_content_t "/var/www(/.*)?"
restorecon -Rv /var/www/

# Write Virtual Host configuration definitions
cat <<EOF > /etc/httpd/conf.d/vhosts.conf
# Site A: Engineering HTTP configuration
<VirtualHost *:80>
    ServerName www.engineering.local
    DocumentRoot /var/www/engineering
    ErrorLog logs/engineering_error_log
    CustomLog logs/engineering_access_log combined
</VirtualHost>

# Site B: Finance HTTPS configuration
<VirtualHost *:443>
    ServerName www.finance.local
    DocumentRoot /var/www/finance
    
    SSLEngine on
    SSLCertificateFile /etc/httpd/ssl/finance.crt
    SSLCertificateKeyFile /etc/httpd/ssl/finance.key

    ErrorLog logs/finance_error_log
    CustomLog logs/finance_access_log combined

    # Enforce basic directory auth protection on reports sub-folder
    <Directory "/var/www/finance/reports">
        AuthType Basic
        AuthName "Restricted Finance Access"
        AuthUserFile /etc/httpd/.htpasswd
        Require valid-user
    </Directory>
</VirtualHost>
EOF
```

### Step 4: Configure HTTP Password Credentials
```bash
# Generate htpasswd credentials database
htpasswd -cb /etc/httpd/.htpasswd admin FinanceSecurePass123!

# Secure the htpasswd file permissions
chown root:apache /etc/httpd/.htpasswd
chmod 640 /etc/httpd/.htpasswd
```

### Step 5: Configure Firewalls and Restart httpd
```bash
# Allow HTTP, HTTPS service access in firewalld
firewall-cmd --permanent --add-service=http
firewall-cmd --permanent --add-service=https
firewall-cmd --reload

# Restart Apache to parse configuration changes
systemctl restart httpd
```

---

## 🔬 Verification & Diagnostics
Configure the host testing client DNS maps (`/etc/hosts`):
`127.0.0.1 www.engineering.local www.finance.local`

```bash
# 1. Verify Site A (Unencrypted)
curl -I http://www.engineering.local/
# (Should return HTTP 200)

# 2. Verify Site B Directory Auth protection
curl -k -I https://www.finance.local/reports/
# (Should return HTTP 401 Unauthorized)

# 3. Authenticate to Site B
curl -k -u admin:FinanceSecurePass123! https://www.finance.local/reports/
# (Should return HTTP 200 with reports HTML content)
```
---
> [!WARNING]
> If curl fails with SELinux warnings, verify context settings using:
> `ls -lZ /var/www/`
