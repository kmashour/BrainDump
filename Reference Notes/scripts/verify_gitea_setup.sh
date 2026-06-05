#!/bin/bash
# ==============================================================================
# Gitea Installation and Security Audit Verification Script
# Target OS: RHEL 8
# Path: Reference Notes/scripts/verify_gitea_setup.sh
# ==============================================================================

# Color definitions
RED='\e[31m'
GREEN='\e[32m'
YELLOW='\e[33m'
BLUE='\e[34m'
CYAN='\e[36m'
BOLD='\e[1m'
NC='\e[0m' # No Color

# Counters for summary
TOTAL_CHECKS=0
PASSED_CHECKS=0
FAILED_CHECKS=0
WARNING_CHECKS=0

# Helper function to print header
print_header() {
    echo -e "\n${BOLD}${BLUE}======================================================================${NC}"
    echo -e "${BOLD}${BLUE}  $1${NC}"
    echo -e "${BOLD}${BLUE}======================================================================${NC}"
}

# Helper function to log results
log_result() {
    local status=$1
    local message=$2
    TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
    
    case "$status" in
        "OK")
            echo -e "[ ${GREEN}${BOLD}OK${NC} ] $message"
            PASSED_CHECKS=$((PASSED_CHECKS + 1))
            ;;
        "FAIL")
            echo -e "[ ${RED}${BOLD}FAIL${NC} ] $message"
            FAILED_CHECKS=$((FAILED_CHECKS + 1))
            ;;
        "WARN")
            echo -e "[ ${YELLOW}${BOLD}WARN${NC} ] $message"
            WARNING_CHECKS=$((WARNING_CHECKS + 1))
            ;;
        "INFO")
            echo -e "[ ${CYAN}${BOLD}INFO${NC} ] $message"
            ;;
    esac
}

# ==============================================================================
# 1. USER VERIFICATION
# ==============================================================================
print_header "1. User Verification"
if id -u git >/dev/null 2>&1; then
    uid=$(id -u git)
    shell=$(getent passwd git | cut -d: -f7)
    
    # Check UID range (< 1000 for system users)
    if [ "$uid" -lt 1000 ]; then
        log_result "OK" "User 'git' exists as a system user (UID: $uid)"
    else
        log_result "FAIL" "User 'git' exists but is NOT a system user (UID: $uid, expected < 1000)"
    fi
    
    # Check default shell (must be /bin/bash for Git-over-SSH forced commands)
    if [ "$shell" = "/bin/bash" ]; then
        log_result "OK" "User 'git' default shell is /bin/bash"
    else
        log_result "FAIL" "User 'git' default shell is '$shell' (expected /bin/bash)"
    fi
else
    log_result "FAIL" "User 'git' does not exist on this host"
fi

# ==============================================================================
# 2. STORAGE VERIFICATION
# ==============================================================================
print_header "2. Storage Verification"
if [ -L "/var/lib/gitea" ]; then
    target=$(readlink "/var/lib/gitea")
    if [ "$target" = "/app/gitea" ] || [ "$target" = "/app/gitea/" ]; then
        log_result "OK" "/var/lib/gitea is a symbolic link pointing to /app/gitea"
    else
        log_result "FAIL" "/var/lib/gitea is a symbolic link but points to '$target' (expected /app/gitea)"
    fi
else
    if [ -e "/var/lib/gitea" ]; then
        log_result "FAIL" "/var/lib/gitea exists but is NOT a symbolic link"
    else
        log_result "FAIL" "/var/lib/gitea does not exist"
    fi
fi

if [ -d "/app/gitea" ]; then
    log_result "OK" "Target storage directory /app/gitea exists"
else
    log_result "FAIL" "Target storage directory /app/gitea does not exist"
fi

# Verify /app is on a larger partition than root/var
if df -P /app /var/lib >/dev/null 2>&1; then
    app_size_kb=$(df -P /app | awk 'NR==2 {print $2}')
    var_size_kb=$(df -P /var/lib | awk 'NR==2 {print $2}')
    app_readable=$(df -h /app | awk 'NR==2 {print $2}')
    var_readable=$(df -h /var/lib | awk 'NR==2 {print $2}')
    
    if [ "$app_size_kb" -gt "$var_size_kb" ]; then
        log_result "OK" "/app partition size ($app_readable) is larger than /var/lib ($var_readable)"
    else
        log_result "WARN" "/app partition size ($app_readable) is not larger than /var/lib ($var_readable)"
    fi
else
    log_result "WARN" "Could not verify partition sizes for /app and /var/lib"
fi

# ==============================================================================
# 3. PERMISSIONS VERIFICATION
# ==============================================================================
print_header "3. Permissions Verification"
# Directory /etc/gitea
if [ -d "/etc/gitea" ]; then
    dir_perms=$(stat -c "%a" /etc/gitea)
    dir_owner=$(stat -c "%U:%G" /etc/gitea)
    
    if [ "$dir_perms" = "750" ]; then
        log_result "OK" "Directory /etc/gitea has correct permissions (750)"
    else
        log_result "FAIL" "Directory /etc/gitea has permissions $dir_perms (expected 750)"
    fi
    
    if [ "$dir_owner" = "root:git" ]; then
        log_result "OK" "Directory /etc/gitea is owned by root:git"
    else
        log_result "FAIL" "Directory /etc/gitea is owned by $dir_owner (expected root:git)"
    fi
else
    log_result "FAIL" "Directory /etc/gitea does not exist"
fi

# File /etc/gitea/app.ini
if [ -f "/etc/gitea/app.ini" ]; then
    file_perms=$(stat -c "%a" /etc/gitea/app.ini)
    file_owner=$(stat -c "%U:%G" /etc/gitea/app.ini)
    
    if [ "$file_perms" = "640" ]; then
        log_result "OK" "Configuration file /etc/gitea/app.ini has correct permissions (640)"
    else
        log_result "FAIL" "Configuration file /etc/gitea/app.ini has permissions $file_perms (expected 640)"
    fi
    
    if [ "$file_owner" = "root:git" ]; then
        log_result "OK" "Configuration file /etc/gitea/app.ini is owned by root:git"
    else
        log_result "FAIL" "Configuration file /etc/gitea/app.ini is owned by $file_owner (expected root:git)"
    fi
else
    log_result "FAIL" "Configuration file /etc/gitea/app.ini does not exist"
fi

# ==============================================================================
# 4. ACCESS CONTROL (FACL) VERIFICATION
# ==============================================================================
print_header "4. Access Control (FACL) Verification"
if [ -d "/app" ]; then
    if command -v getfacl >/dev/null 2>&1; then
        facl_out=$(getfacl -p /app 2>/dev/null)
        # Search specifically for user:git:x
        git_facl_line=$(echo "$facl_out" | grep -E '^user:git:[r-][w-][x-]')
        
        if [ -n "$git_facl_line" ]; then
            facl_perms=$(echo "$git_facl_line" | cut -d: -f3)
            if [[ "$facl_perms" == *x* ]]; then
                log_result "OK" "User 'git' has traversal permissions (execute) via FACL on /app: $git_facl_line"
            else
                log_result "FAIL" "User 'git' has FACL on /app but lacks traversal (execute) permissions: $git_facl_line"
            fi
        else
            # Fallback to check if /app is world-executable
            other_perms=$(stat -c "%A" /app 2>/dev/null | cut -c10)
            if [ "$other_perms" = "x" ]; then
                log_result "WARN" "No specific FACL entry for 'git' on /app, but it is traversable by others (world-executable: $other_perms)"
            else
                log_result "FAIL" "No FACL entry found for 'git' on /app and directory is not traversable (execute bit missing)"
            fi
        fi
    else
        log_result "WARN" "getfacl command not found. Performing standard traversal test using sudo -u git"
        if sudo -u git test -x /app >/dev/null 2>&1; then
            log_result "OK" "User 'git' can traverse /app (system check passed)"
        else
            log_result "FAIL" "User 'git' cannot traverse /app (permission denied)"
        fi
    fi
else
    log_result "FAIL" "Parent directory /app does not exist"
fi

# ==============================================================================
# 5. SYSTEMD CONFIGURATION
# ==============================================================================
print_header "5. Systemd Configuration"
service_file="/etc/systemd/system/gitea.service"
if [ -f "$service_file" ]; then
    log_result "OK" "Systemd service file exists: $service_file"
    
    # Check User
    svc_user=$(grep -E '^\s*User\s*=' "$service_file" | cut -d= -f2 | xargs)
    if [ "$svc_user" = "git" ]; then
        log_result "OK" "Service parameter 'User' is set to 'git'"
    else
        log_result "FAIL" "Service parameter 'User' is set to '$svc_user' (expected 'git')"
    fi
    
    # Check Group
    svc_group=$(grep -E '^\s*Group\s*=' "$service_file" | cut -d= -f2 | xargs)
    if [ "$svc_group" = "git" ]; then
        log_result "OK" "Service parameter 'Group' is set to 'git'"
    else
        log_result "FAIL" "Service parameter 'Group' is set to '$svc_group' (expected 'git')"
    fi
    
    # Check Environment variables
    env_content=$(grep -E '^\s*Environment\s*=' "$service_file")
    if [ -n "$env_content" ]; then
        # Check USER=git
        if echo "$env_content" | grep -qE 'USER=git(\s+|$)'; then
            log_result "OK" "Service environment variable 'USER=git' is configured"
        else
            log_result "FAIL" "Service environment variable 'USER=git' is missing or incorrect"
        fi
        
        # Check HOME=/home/git
        if echo "$env_content" | grep -qE 'HOME=/home/git(\s+|$)'; then
            log_result "OK" "Service environment variable 'HOME=/home/git' is configured"
        else
            log_result "FAIL" "Service environment variable 'HOME=/home/git' is missing or incorrect"
        fi
        
        # Check GITEA_WORK_DIR=/var/lib/gitea or /app/gitea
        if echo "$env_content" | grep -qE 'GITEA_WORK_DIR=(/var/lib/gitea|/app/gitea)(\s+|$)'; then
            work_dir_val=$(echo "$env_content" | sed -n 's/.*GITEA_WORK_DIR=\([^ ]*\).*/\1/p' | xargs)
            log_result "OK" "Service environment variable 'GITEA_WORK_DIR=$work_dir_val' is configured"
        else
            log_result "FAIL" "Service environment variable 'GITEA_WORK_DIR=/var/lib/gitea' is missing or incorrect"
        fi
    else
        log_result "FAIL" "No Environment directive found in $service_file"
    fi
else
    log_result "FAIL" "Systemd service file $service_file does not exist"
fi

# ==============================================================================
# 6. PORT AND SOCKET CHECKS
# ==============================================================================
print_header "6. Port and Socket Checks"
port_listener=$(ss -tlnp 2>/dev/null | grep -E '(:3000\s+|:3000$)')

if [ -n "$port_listener" ]; then
    log_result "OK" "Port 3000 is active and listening"
    if echo "$port_listener" | grep -qi "gitea"; then
        log_result "OK" "Port 3000 is bound by Gitea process"
    else
        log_result "WARN" "Port 3000 is bound, but process name does not contain 'gitea': $port_listener"
    fi
else
    # Check if systemctl says service is active
    if systemctl is-active gitea >/dev/null 2>&1; then
        log_result "FAIL" "Gitea service is active, but port 3000 is NOT listening"
    else
        log_result "FAIL" "Port 3000 is not active, and Gitea service is not running"
    fi
fi

# ==============================================================================
# 7. SELINUX CHECK
# ==============================================================================
print_header "7. SELinux Check"
if command -v getenforce >/dev/null 2>&1; then
    selinux_mode=$(getenforce)
    log_result "INFO" "SELinux mode is: $selinux_mode"
    
    if [ "$selinux_mode" = "Enforcing" ]; then
        log_result "OK" "SELinux is in Enforcing mode"
    elif [ "$selinux_mode" = "Permissive" ]; then
        log_result "WARN" "SELinux is in Permissive mode (logging but not enforcing)"
    else
        log_result "WARN" "SELinux is Disabled"
    fi
    
    # Binary context check (/usr/local/bin/gitea)
    binary_path="/usr/local/bin/gitea"
    if [ -f "$binary_path" ]; then
        binary_context=$(ls -Z "$binary_path" 2>/dev/null | awk '{print $1}')
        if [ "$binary_context" = "?" ] || [ -z "$binary_context" ] || [[ "$binary_context" == *"/"* ]]; then
            log_result "WARN" "SELinux attributes not supported on filesystem or disabled for binary $binary_path"
        else
            binary_type=$(echo "$binary_context" | cut -d: -f3)
            if [ "$binary_type" = "bin_t" ] || [ "$binary_type" = "usr_t" ]; then
                log_result "OK" "Binary $binary_path SELinux context type is correct: $binary_type"
            else
                log_result "FAIL" "Binary $binary_path SELinux context type is '$binary_type' (expected bin_t or usr_t)"
            fi
        fi
    else
        log_result "FAIL" "Gitea binary not found at $binary_path"
    fi
    
    # Data directory context check (/app/gitea)
    data_path="/app/gitea"
    if [ -d "$data_path" ]; then
        data_context=$(ls -Zd "$data_path" 2>/dev/null | awk '{print $1}')
        if [ "$data_context" = "?" ] || [ -z "$data_context" ] || [[ "$data_context" == *"/"* ]]; then
            log_result "WARN" "SELinux attributes not supported on filesystem or disabled for directory $data_path"
        else
            data_type=$(echo "$data_context" | cut -d: -f3)
            if [ "$data_type" = "var_lib_t" ]; then
                log_result "OK" "Data directory $data_path SELinux context type is correct: var_lib_t"
            else
                log_result "FAIL" "Data directory $data_path SELinux context type is '$data_type' (expected var_lib_t)"
            fi
        fi
    else
        log_result "FAIL" "Data directory not found at $data_path"
    fi
else
    log_result "WARN" "SELinux command utilities (getenforce) not found on this system"
fi

# ==============================================================================
# AUDIT SUMMARY
# ==============================================================================
echo -e "\n${BOLD}${BLUE}======================================================================${NC}"
echo -e "${BOLD}${BLUE}  Verification Summary${NC}"
echo -e "${BOLD}${BLUE}======================================================================${NC}"
echo -e "Total Checks Performed: $TOTAL_CHECKS"
echo -e "Passed:                 ${GREEN}${BOLD}$PASSED_CHECKS${NC}"
echo -e "Failed:                 ${RED}${BOLD}$FAILED_CHECKS${NC}"
echo -e "Warnings:               ${YELLOW}${BOLD}$WARNING_CHECKS${NC}"
echo -e "${BOLD}${BLUE}======================================================================${NC}"

if [ "$FAILED_CHECKS" -gt 0 ]; then
    echo -e "\n${RED}${BOLD}Audit Status: FAIL${NC} - One or more checks failed. Please review the failures above."
    exit 1
else
    echo -e "\n${GREEN}${BOLD}Audit Status: PASS${NC} - All checks passed successfully (with $WARNING_CHECKS warning(s))."
    exit 0
fi
