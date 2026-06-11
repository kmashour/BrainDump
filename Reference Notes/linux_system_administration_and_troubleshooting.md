---
domains:
  - "linux"
  - "security"
  - "troubleshooting"
---

# Linux System Administration & Troubleshooting Reference

This module covers core Linux diagnostic systems, file type validation, exit code mappings, system error translation via `perror`, password cryptography, and remote shell connection libraries.

---

## 1. Querying File Types: The `file` Command

Unlike Windows operating systems, Linux does not rely on filename extensions to identify a file's format. A file named `script.jpg` could actually contain plain-text bash code. The `file` utility solves this ambiguity by reading the file's header bytes (known as "magic numbers") to determine its true MIME type.

*   **Syntax:**
    ```bash
    file target_filename
    ```
*   **Example Output:**
    ```bash
    file archive.tar.gz
    # Output: archive.tar.gz: gzip compressed data, from Unix, original size 10240
    ```

---

## 2. GNU/Linux Exit Codes

Every command executed in a shell returns an exit code (an integer from 0 to 255) to the operating system upon termination. Scripts parse this code to verify if a command succeeded.

*   **Query Last Exit Code:**
    ```bash
    echo $?
    ```

### Common Linux System Exit Codes
Below is the standard reference mapping for GNU/Linux system error numbers (`errno`):

| Exit Code | Description |
| :--- | :--- |
| **0** | **Success** (Command completed without errors) |
| **1** | Operation not permitted |
| **2** | No such file or directory |
| **3** | No such process |
| **4** | Interrupted system call |
| **5** | Input/output error |
| **6** | No such device or address |
| **7** | Argument list too long |
| **8** | Exec format error |
| **9** | Bad file descriptor |
| **10** | No child processes |
| **11** | Resource temporarily unavailable |
| **12** | Cannot allocate memory |
| **13** | Permission denied |
| **14** | Bad address |
| **15** | Block device required |
| **16** | Device or resource busy |
| **17** | File exists |
| **18** | Invalid cross-device link |
| **19** | No such device |
| **20** | Not a directory |
| **21** | Is a directory |
| **22** | Invalid argument |
| **23** | Too many open files in system |
| **24** | Too many open files |
| **25** | Inappropriate ioctl for device |
| **26** | Text file busy |
| **27** | File too large |
| **28** | **No space left on device** |
| **29** | Illegal seek |
| **30** | Read-only file system |
| **31** | Too many links |
| **32** | Broken pipe |
| **33** | Numerical argument out of domain |
| **34** | Numerical result out of range |
| **35** | Resource deadlock avoided |
| **36** | File name too long |
| **38** | Function not implemented |
| **39** | Directory not empty |
| **40** | Too many levels of symbolic links |
| **98** | **Address already in use** (Port bind conflict) |
| **101** | Network is unreachable |
| **110** | Connection timed out |
| **111** | Connection refused |

#### Deep-Intuition (AARF) Breakdown: Exit Code Checks for Automation Scripts
1.  **The Answer (Core Pattern):** Write conditional checks in shell scripts to handle non-zero exit codes:
    ```bash
    cp /source/config.json /etc/app/
    EXIT_STATUS=$?
    
    if [ $EXIT_STATUS -ne 0 ]; then
        echo "Configuration copy failed with exit code $EXIT_STATUS."
        # Take recovery action or exit
        exit $EXIT_STATUS
    fi
    ```
2.  **The Assumptions (Context):** Assumes the script executes in a non-interactive shell and has error trapping configured (`set -e` optionally).
3.  **The Rationale (Why):** When commands fail, they output text to stderr. However, automation engines cannot reliably parse text descriptions. Checking the numeric exit code (`$?`) provides an unambiguous, standardized indicator of process health.
4.  **The Failure Loop (What if not):** Ignoring exit codes in deployment scripts allows errors to cascade silently. If a config file fails to copy due to a "No space left on device" (code 28) or "Permission denied" (code 13), subsequent commands will still run, leading to broken service states.
5.  **Alternative Case (When to use 'if not'):** For commands where non-zero status is expected (e.g. `grep` returning code 1 if no matches are found), disable default exit traps to prevent scripts from terminating prematurely.

---

## 3. Diagnostic Code Translation: The `perror` Command

The `perror` utility translates numeric OS error codes or database-specific error codes (MySQL) into human-readable text descriptions.

*   **Syntax:**
    ```bash
    perror error_number [error_number2 ...]
    ```

### Command Examples
*   **Decode Single Error:**
    ```bash
    perror 2
    # Output: OS error code   2:  No such file or directory
    ```
*   **Decode Multiple Errors:**
    ```bash
    perror 13 28
    # Output:
    # OS error code  13:  Permission denied
    # OS error code  28:  No space left on device
    ```
*   **Decode MySQL Database Errors:**
    ```bash
    perror 1045
    # Output: MySQL error code 1045 (ER_ACCESS_DENIED_ERROR): Access denied for user
    ```

---

## 4. Cryptographic Security & Remote Execution

### Password Hashing & Bcrypt
Storing passwords in plaintext exposes credentials during database leaks. Cryptographic hashing functions transform strings into fixed-length hashes irreversibly.
*   **Bcrypt:** An adaptive cryptographic hash function based on the Blowfish cipher. Bcrypt automatically incorporates a **salt** (a random sequence appended to the password prior to hashing) and implements configurable work factors (iteration rounds). This design mitigates rainbow table attacks and brute-force GPU hardware attacks.

### Remote Execution via Paramiko
`paramiko` is a pure-Python library implementing the SSHv2 protocol to establish secure, encrypted shell connections to remote hosts.
```python
import paramiko

def run_remote_command(hostname, username, password, command):
    # Initialize SSH Client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Establish encrypted connection
        ssh.connect(hostname, username=username, password=password, timeout=10)
        
        # Execute command
        stdin, stdout, stderr = ssh.exec_command(command)
        
        # Retrieve results
        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')
        
        return output, error
    finally:
        ssh.close()
```
