---
obsidianUIMode: preview
class: project-playbook
tier: project-playbook
tags:
  - project
  - linux/users
  - linux/permissions
---

# Project: User Administration & POSIX-ACL Hardening

**Breadcrumbs:** [[8-Index - Linux and OS|🏠 Linux and OS Index]] > **Projects** > **User Administration & POSIX-ACL Hardening**

---

## 🎯 Project Objective
This project demonstrates enterprise user/group administration, system access policies configuration, special permission bits (SUID, SGID, Sticky Bit), and fine-grained access controls using POSIX Access Control Lists (ACLs).

---

## 💻 Scenario
A development agency requires a shared directory `/srv/projects/` where:
1.  All users in the `developers` group can read/write files.
2.  Newly created files in the directory automatically inherit the `developers` group ownership.
3.  Users cannot delete files created by other users (Sticky Bit protection).
4.  A specific external auditor `audit-user` needs read-only access to a specific sub-folder without being added to the `developers` group.
5.  A senior lead `lead-dev` needs full read-write permissions to all files, including future files, via default ACL rules.

---

## 🛠️ Step-by-Step Implementation

### Step 1: Create Users and Groups
We initialize groups and users with appropriate primary and supplementary memberships.
```bash
# Create groups
groupadd developers
groupadd auditing

# Create users
useradd -m -g developers -G wheel lead-dev
useradd -m -g developers developer1
useradd -m -g developers developer2
useradd -m -g auditing audit-user

# Set passwords (for testing)
echo "Password123" | passwd --stdin lead-dev
echo "Password123" | passwd --stdin developer1
echo "Password123" | passwd --stdin developer2
echo "Password123" | passwd --stdin audit-user
```

### Step 2: Establish the Shared Directory and Special Permissions
Create the directory structure and apply standard group overrides.
```bash
# Create project directories
mkdir -p /srv/projects/finance
mkdir -p /srv/projects/engineering

# Set primary owner to root, and group owner to developers
chown -R root:developers /srv/projects

# Configure permissions:
# - Owner: Read, Write, Execute (7)
# - Group: Read, Write, Execute (7)
# - Others: Read, Execute (5)
chmod 775 /srv/projects

# Apply SGID: Newly created files inherit the 'developers' group owner
chmod g+s /srv/projects

# Apply Sticky Bit: Users can only delete their own files
chmod +t /srv/projects
```

### Step 3: Implement POSIX Access Control Lists (ACL)
Configure fine-grained security policies on the `finance` directory.
```bash
# Grant audit-user read-only access to finance folder
setfacl -m u:audit-user:rx /srv/projects/finance

# Grant lead-dev full write access to all files inside engineering
setfacl -m u:lead-dev:rwx /srv/projects/engineering

# Configure Default ACLs on engineering so that future files inherit lead-dev rwx permissions
setfacl -d -m u:lead-dev:rwx /srv/projects/engineering
setfacl -d -m g:developers:rwx /srv/projects/engineering
```

---

## 🔬 Verification & Diagnostics

### Verify Directory Permissions and ACLs
```bash
# Inspect permissions
ls -ld /srv/projects

# Inspect active ACL policies
getfacl /srv/projects/finance
getfacl /srv/projects/engineering
```

*Expected getfacl Output:*
```
# file: srv/projects/finance
# owner: root
# group: developers
user::rwx
user:audit-user:r-x
group::rwx
mask::rwx
other::r-x
```

### Functional Validation Testing
```bash
# 1. Test SGID and Sticky Bit as developer1
su - developer1 -c "touch /srv/projects/dev1_file.txt"
ls -l /srv/projects/dev1_file.txt
# (Should show group ownership as 'developers' instead of 'developer1')

# 2. Test deletion protection as developer2
su - developer2 -c "rm -f /srv/projects/dev1_file.txt"
# (Should fail with "Permission denied" due to the Sticky Bit (+t))

# 3. Test Auditor read access
su - audit-user -c "cat /srv/projects/finance/some_report.txt"
# (Should succeed)
su - audit-user -c "touch /srv/projects/finance/audit_log.txt"
# (Should fail with "Permission denied")
```
