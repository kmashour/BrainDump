# 📂 Section: System Hardening
## 📖 AppArmor in Kubernetes
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/AppArmor-in-Kubernetes/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/AppArmor-in-Kubernetes/page)

# AppArmor in Kubernetes

> This article explains how to secure Kubernetes container deployments using AppArmor profiles to enforce security policies at the kernel level.

In this lesson, we explain how to secure your container deployments in Kubernetes using AppArmor profiles. AppArmor enforces security policies at the kernel level by limiting file system writes and other potentially risky operations within containers.

AppArmor support was introduced in Kubernetes v1.4 and, although it remained in beta until version 1.20, it has proven to be an effective tool for hardening container security. To enable AppArmor on Kubernetes pods, ensure that each node in your cluster meets the following requirements:

– The AppArmor kernel module must be enabled.\
– The desired AppArmor profile must be loaded on each node.\
– The container runtime (e.g., Docker, CRI-O, Containerd) must support AppArmor.

<Callout icon="lightbulb" color="#1CB2FE">
  Before proceeding, verify that all nodes have the AppArmor kernel module enabled and the required profile loaded.
</Callout>

<Frame>
  ![The image outlines requirements for using AppArmor in Kubernetes: version above 1.4, enabled kernel module, loaded profile, and supported container runtime.](https://kodekloud.com/kk-media/image/upload/v1752871728/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-AppArmor-in-Kubernetes/frame_50.jpg)
</Frame>

## Example: Ubuntu Sleeper Pod with AppArmor Profile

Below is an example where an Ubuntu container is configured as a Sleeper pod. The container prints a message and sleeps for one hour. Because the container's command does not require file system write access, the pod is secured with an AppArmor profile that denies write operations.

### Verify the AppArmor Profile

Before deploying your pod, ensure the AppArmor profile is loaded on all nodes. Run the following command on each worker node:

```plaintext theme={null}
aa-status
apparmor module is loaded.
13 profiles are loaded.
13 profiles are in enforce mode.
    apparmor-deny-write
    /sbin/dhclient
    /usr/bin/man
    /usr/lib/NetworkManager/mn-dhcp-client.action
    /usr/lib/NetworkManager/mn-dhcp-helper
    ...
    /usr/sbin/tcpdump
    docker-default
    man_filter
    man_groff
0 profiles are in complain mode.
11 processes have profiles defined.
11 processes are in enforce mode.
    /sbin/dhclient (621)
    docker-default (3970)
    docker-default (4025)
    docker-default (9853)
    docker-default (9964)
0 processes are in complain mode.
2 processes are unconfined but have a profile defined.
```

### Basic Pod Definition

Here is the basic YAML specification for creating the Ubuntu Sleeper pod:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu-sleeper
spec:
  containers:
    - name: hello
      image: ubuntu
      command: [ "sh", "-c", "echo 'Sleeping for an hour!' && sleep 1h" ]
```

### AppArmor Deny Write Profile

The following is an example of an AppArmor profile (`apparmor-deny-write`) designed to deny all file write operations:

```plaintext theme={null}
profile apparmor-deny-write flags=(attach_disconnected) {
    file,
    # Deny all file writes.
    deny /** w,
}
```

<Callout icon="lightbulb" color="#1CB2FE">
  Make sure the above profile is loaded on every worker node where your pod might run.
</Callout>

### Applying the AppArmor Profile to the Pod

Previously, when AppArmor was in beta, it was necessary to annotate the pod's metadata to specify the AppArmor profile. The annotation used was `container.apparmor.security.beta.kubernetes.io` with the container name as the key and a value formatted as `localhost/<profile-name>`.

Legacy configuration example:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu-sleeper
  annotations:
    container.apparmor.security.beta.kubernetes.io/ubuntu-sleeper: localhost/apparmor-deny-write
spec:
  containers:
    - name: ubuntu-sleeper
      image: ubuntu
      command: [ "sh", "-c", "echo 'Sleeping for an hour!' && sleep 1h" ]
```

Starting from newer Kubernetes versions, you can specify an AppArmor profile using the `securityContext` within the pod specification. The updated configuration is shown below:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu-sleeper
spec:
  securityContext:
    appArmorProfile:
      type: Localhost
      localhostProfile: apparmor-deny-write
  containers:
    - name: ubuntu-sleeper
      image: ubuntu
      command: [ "sh", "-c", "echo 'Sleeping for an hour!' && sleep 1h" ]
```

### Creating and Testing the Pod

1. **Create the Pod:** Save the YAML configuration (e.g., as `ubuntu-sleeper.yaml`) and run:

   ```plaintext theme={null}
   kubectl create -f ubuntu-sleeper.yaml
   pod/ubuntu-sleeper created
   ```

2. **Verify Pod Logs:** Check the container's logs to ensure that the message has been printed:

   ```plaintext theme={null}
   kubectl logs ubuntu-sleeper
   Sleeping for an hour!
   ```

3. **Test the AppArmor Profile:** Attempt to create a file inside the container to test the deny write rule. Run:

   ```plaintext theme={null}
   kubectl exec -ti ubuntu-sleeper -- touch /tmp/test
   ```

   The operation should fail with a permission denied error:

   ```plaintext theme={null}
   touch: cannot touch '/tmp/test': Permission denied
   command terminated with exit code 1
   ```

<Callout icon="triangle-alert" color="#FF6B6B">
  If the file creation attempt fails as shown above, it confirms that the AppArmor profile is enforcing the security restrictions correctly.
</Callout>

This concludes the lesson on using AppArmor profiles in Kubernetes. For further practice and deeper understanding, explore additional hands-on labs and documentation on Kubernetes security.

For more information, refer to:

* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Kubernetes Security Best Practices](https://kubernetes.io/docs/concepts/security/overview/)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/d67be5ee-871d-4435-a187-382610cb6a1f/lesson/b469e2e2-7a6b-468d-ab12-ddd4eac35057" />
</CardGroup>

---


# 📂 Section: System Hardening
## 📖 AppArmor
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/AppArmor/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/AppArmor/page)

# AppArmor

> This article explores AppArmor, a Linux security module that limits application access to system resources, enhancing container security beyond Seccomp profiles.

In this lesson, we explore AppArmor, a robust Linux security module designed to limit an application's access to system resources. By enforcing strict restrictions, AppArmor helps reduce the attack surface and enhances container security beyond what Seccomp profiles provide.

Previously, we examined Seccomp profiles in Kubernetes. Although Seccomp is effective at limiting the available syscalls for container operations, it does not manage access to specific resources such as files or directories. For example, a custom Seccomp profile can block the MKDIR syscall to prevent the creation of new directories.

Consider the following custom Seccomp profile that allows only a selected set of syscalls while denying all others (including MKDIR by default):

```json theme={null}
{
  "defaultAction": "SCMP_ACT_ERRNO",
  "architectures": [
    "SCMP_ARCH_X86_64",
    "SCMP_ARCH_X86",
    "SCMP_ARCH_X32"
  ],
  "syscalls": [
    {
      "names": [
        "execve",
        "close",
        "brk"
      ],
      "action": "SCMP_ACT_ALLOW"
    }
  ]
}
```

You can run a container with this Seccomp profile as shown below:

```bash theme={null}
docker run -it --security-opt seccomp=/root/custom.json docker/whalesay /bin/sh
```

Inside the container, if you try to create a directory:

```bash theme={null}
# mkdir test
```

You will encounter an error similar to:

```bash theme={null}
mkdir: can't create directory 'test': Operation not permitted
```

<Callout icon="lightbulb" color="#1CB2FE">
  While Seccomp restricts which system calls a container can execute, it does not control access to the filesystem. For enhanced resource-level security, AppArmor is used.
</Callout>

## Introducing AppArmor

AppArmor confines applications to a limited set of resources, including specific file and directory permissions, network settings, and Linux capabilities. It is installed and enabled by default on most Linux distributions.

### Verifying AppArmor

To ensure that AppArmor is active, run the following command:

```bash theme={null}
systemctl status apparmor
```

Additionally, make sure that the AppArmor kernel module is loaded on every node hosting your container. You can verify this by checking the enabled parameter:

```bash theme={null}
cat /sys/module/apparmor/parameters/enabled
```

The expected output should be:

```text theme={null}
Y
```

To view all loaded AppArmor profiles, inspect the profiles file:

```bash theme={null}
cat /sys/kernel/security/apparmor/profiles
```

This command might produce output similar to:

```text theme={null}
docker-default (enforce)
/usr/sbin/tcpdump (enforce)
/usr/sbin/ntpd (enforce)
/usr/lib/snapd/snap-confine (enforce)
/usr/lib/snapd/snap-confine/mount-namespace-capture-helper (enforce)
/usr/lib/connman/scripts/dhclient-script (enforce)
/usr/lib/NetworkManager/nm-dhcp-helper (enforce)
/usr/lib/NetworkManager/nm-dhcp-client.action (enforce)
/sbin/dhclient (enforce)
/usr/bin/man (enforce)
/usr/bin/man_filter (enforce)
```

## Creating and Using AppArmor Profiles

An AppArmor profile is a plain text file that defines the resources accessible to an application, such as Linux capabilities, network access, and file permissions. For instance, the profile below restricts write access across the entire filesystem:

```plain theme={null}
profile apparmor-deny-write flags=(attach_disconnected) {
    file,
    # Deny all file writes.
    deny /** w,
}
```

This profile initially permits filesystem access with the "file" shorthand, then explicitly denies write operations on any file under the root directory and its subdirectories.

Similarly, to prevent remounting the root filesystem as read-only, you can create the following profile:

```plain theme={null}
profile apparmor-deny-remount-root flags=(attach_disconnected) {
  # Deny remounting the root filesystem as read-only.
  deny mount options=(ro, remount) -> /,
}
```

<Callout icon="triangle-alert" color="#FF6B6B">
  Ensure that your AppArmor profiles are correctly configured. Incorrect settings may lead to unexpected behavior or reduced security. Always test profiles in a controlled environment before deploying them in production.
</Callout>

### Checking AppArmor Profile Status

The `aa-status` tool provides a comprehensive view of AppArmor’s current state. Running this command displays details such as loaded profiles, their modes (enforce, complain, or unconfined), and the processes constrained by these profiles.

Example output of `aa-status`:

```bash theme={null}
aa-status
apparmor module is loaded.
12 profiles are loaded.
12 profiles are in enforce mode.
    /sbin/dhclient
    /usr/bin/man
    /usr/lib/NetworkManager/nm-dhcp-client.action
    /usr/lib/NetworkManager/nm-dhcp-helper
    ...
    /usr/sbin/tcpdump
    docker-default
    man_filter
    man_groff
0 profiles are in complain mode.
11 processes have profiles defined.
11 processes are in enforce mode:
    /sbin/dhclient (621)
    docker-default (3970)
    docker-default (4025)
    docker-default (9853)
    docker-default (9964)
0 processes are in complain mode.
0 processes are 'unconfined' but have a profile defined.
```

## AppArmor Profile Modes

AppArmor profiles operate in three distinct modes:

* **Enforce mode:** The profile rules are strictly enforced on the application.
* **Complain mode:** The application is allowed to perform actions outside the defined profile rules while logging such actions as warnings.
* **Unconfined mode:** No restrictions are applied, and actions are not logged.

Moving forward, we will discuss how to create and manage AppArmor profiles using dedicated AppArmor utilities.

For more details on securing containerized environments, you may refer to the following resources:

* [Linux Security Modules (LSM) Overview](https://en.wikipedia.org/wiki/Linux_Security_Modules)
* [Kubernetes Security Best Practices](https://kubernetes.io/docs/concepts/security/overview/)

Thank you.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/d67be5ee-871d-4435-a187-382610cb6a1f/lesson/06f55a49-58d3-4d83-815f-0350ebc9c803" />
</CardGroup>

---


# 📂 Section: System Hardening
## 📖 AquaSec Tracee
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/AquaSec-Tracee/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/AquaSec-Tracee/page)

# AquaSec Tracee

> This article explores Tracee, an open-source tool for tracing system calls in containers using eBPF technology.

In this article, we explore Tracee—an open-source tool from Aqua Security that leverages eBPF (Extended Berkeley Packet Filter) to trace system calls on containers at runtime. By running programs directly in kernel space without modifying the kernel or loading additional modules, eBPF empowers Tracee to monitor operating system behavior and detect suspicious activity with minimal overhead.

## Running Tracee as a Docker Container

Running Tracee as a Docker container simplifies dependency management and environment setup. When Tracee runs as a container, it compiles the eBPF program and, by default, stores the output in the `/tmp/tracee` directory. To persist the compiled program between runs, bind mount the `/tmp/tracee` directory from the host to the container.

Additionally, Tracee requires access to kernel headers to compile the eBPF program. On Ubuntu systems, these headers are typically located in `/lib/modules` (with dependencies in `/usr/src`). Ensure these directories are also bind mounted into the container in read-only mode. Since Tracee needs extended privileges for syscall tracing, run the container using Docker’s `--privileged` flag.

<Frame>
  ![The image shows a presentation slide about tracing syscalls with "tracee," detailing bind mounts and their purposes, and mentioning additional capabilities as "Privileged."](https://kodekloud.com/kk-media/image/upload/v1752871730/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-AquaSec-Tracee/frame_110.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Remember to bind mount the `/tmp/tracee`, `/lib/modules`, and `/usr/src` directories properly to ensure that the eBPF program compiles and persists across runs.
</Callout>

## Tracing Syscalls for a Single Command

To capture system calls generated by a single command (for example, `ls`), run the Tracee container with the `--trace` option specifying the command to trace. Execute the following command:

```bash theme={null}
docker run --name tracee --rm --privileged --pid=host \
  -v /lib/modules/:/lib/modules:ro \
  -v /usr/src:/usr/src:ro \
  -v /tmp/tracee:/tmp/tracee \
  aquasec/tracee:0.4.0 --trace comm=ls
```

This command outputs a list of syscalls invoked by the `ls` command. A sample output might include:

```text theme={null}
TIME(s)      UID    COMM    PID    TID    RET
1263.457188  0      ls      27461  27461  -2
1263.457218  0      ls      27461  27461  -2
1263.457238  0      ls      27461  27461  0
...
[output truncated]
```

## Tracing Syscalls for All New Processes

If you wish to monitor the system calls for all new processes on the host, configure Tracee with the `--trace` flag to track new process IDs. Use the command below:

```bash theme={null}
sudo docker run --name tracee --rm --privileged --pid=host \
  -v /lib/modules/:/lib/modules:ro \
  -v /usr/src:/usr/src:ro \
  -v /tmp/tracee:/tmp/tracee \
  aquasec/tracee:0.4.0 --trace pid=new
```

This setup produces extensive output as Tracee collects syscall data for every new process initiated on the host. An excerpt from the output may resemble:

```text theme={null}
1613.769845 0  wc      1619 1619  -2   openat
1613.846148 0  kubectl 1617 1621  -2   openat
...
```

<Callout icon="lightbulb" color="#1CB2FE">
  For environments where heavy logging might overwhelm the output, consider filtering or redirecting logs to manage the volume of data.
</Callout>

## Tracing Syscalls for New Containers

Tracee also supports capturing system calls from new containers. To enable this functionality, launch Tracee with the option `--trace container=new`. Follow these steps:

1. Open a terminal and run Tracee with container tracing enabled:

   ```bash theme={null}
   sudo docker run --name tracee --rm --privileged --pid=host \
     -v /lib/modules/:/lib/modules:ro \
     -v /usr/src:/usr/src:ro \
     -v /tmp/tracee:/tmp/tracee \
     aquasec/tracee:0.4.0 --trace container=new
   ```

2. In another terminal window, launch an Ubuntu container that prints a message and exits:

   ```bash theme={null}
   docker run ubuntu echo hi
   ```

Upon executing the Ubuntu container, you should see "hi" printed in the container's output and Tracee’s terminal will display all syscalls generated by this container.

## Conclusion

Tracee is a powerful eBPF-based tool that enables real-time monitoring of system calls in various environments—whether for a single command, all new processes, or new containers. By running Tracee as a Docker container, you streamline dependency management while ensuring effective tracking of system activities. In our next article, we will cover strategies to restrict system calls made by applications to further enhance security.

For more detailed documentation and related resources, refer to the [Aqua Security Tracee GitHub repository](https://github.com/aquasecurity/tracee) and explore additional guides on eBPF tracing and container security practices.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/d67be5ee-871d-4435-a187-382610cb6a1f/lesson/f1281fe2-f470-4565-a898-836d990047ec" />
</CardGroup>

---


# 📂 Section: System Hardening
## 📖 Creating AppArmor Profiles
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Creating-AppArmor-Profiles/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Creating-AppArmor-Profiles/page)

# Creating AppArmor Profiles

> This guide explains how to create custom AppArmor profiles for applications, including generating profiles from scripts and verifying their enforcement.

In this guide, we will walk through the process of creating custom AppArmor profiles. After reviewing several example profiles in previous lessons, it’s time to build an application-specific profile from scratch.

## Example Bash Script

Below is a sample Bash script named "add\_data.sh" that creates directories under the /opt filesystem and writes a log file within the new directory:

```bash theme={null}
#!/bin/bash
data_directory=/opt/app/data
mkdir -p "${data_directory}"
echo "=> File created at $(date)" | tee "${data_directory}/create.log"
```

To run the script, execute the following command in your terminal:

```bash theme={null}
./add_data.sh
```

Expected terminal output:

```plaintext theme={null}
=> File created at Mon Mar 12 03:29:22 UTC 2021
```

You can verify the content of the log file with:

```bash theme={null}
cat /opt/app/data/create.log
```

This should display:

```plaintext theme={null}
=> File created at Mon Mar 12 03:29:22 UTC 2021
```

## Generating an AppArmor Profile for the Script

Instead of creating a profile manually, you can use AppArmor’s built-in tools. First, install the AppArmor-utils package. On Ubuntu, run:

```bash theme={null}
apt-get install -y apparmor-utils
```

The installation output will resemble:

```plaintext theme={null}
Reading package lists... Done
Building dependency tree        
Reading state information... Done
The following packages were automatically installed and are no longer required:
  libc-ares2 libhttp-parser2.7.1 libnetplan0 libuv1 nodejs-doc python3-netifaces
Use 'apt autoremove' to remove them.
The following additional packages will be installed:
  python3-apparmor python3-libapparmor
Suggested packages:
  vim-addon-manager
The following NEW packages will be installed:
  apparmor-utils python3-apparmor python3-libapparmor
...
Unpacking apparmor-utils (2.12-4ubuntu5.1) ...
Setting up python3-libapparmor (2.12-4ubuntu5.1) ...
Setting up python3-apparmor (2.12-4ubuntu5.1) ...
Setting up apparmor-utils (2.12-4ubuntu5.1) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
```

Once installed, generate a profile for the Bash script using the following command:

```bash theme={null}
aa-genprof /root/add_data.sh
```

The output will be similar to:

```plaintext theme={null}
Writing updated profile for /root/add_data.sh.
Setting /root/add_data.sh to complain mode!

Before you begin, you may wish to check if a profile already exists for the application you wish to confine. See the following wiki page for more information:
https://gitlab.com/apparmor/apparmor/wikis/Profiles
Profiling: /root/add_data.sh

Please start the application to be profiled in another window and exercise its functionality now.

Once completed, select the "Scan" option below in order to scan the system logs for AppArmor events.

For each AppArmor event, you will be given the opportunity to choose whether the access should be allowed or denied.

[(S)can system log for AppArmor events] / (F)inish
```

## Profiling the Script

1. Open a separate terminal window and run the Bash script to generate AppArmor events:

   ```bash theme={null}
   ./add_data.sh
   ```

2. Return to the `aa-genprof` prompt and press `s` to scan the system logs. The tool will then display multiple prompts for each event encountered, such as:

   ```plaintext theme={null}
   Profile: /root/add_data.sh
   Execute: /usr/bin/mkdir
   Severity: unknown
   ```

   To allow the execution of the `mkdir` command, choose the inherit option by entering `i`.

3. Further prompts might appear. For example:

   ```plaintext theme={null}
   Profile: /root/add_data.sh
   Execute: /usr/bin/tee
   Severity: 3
   (I)nherit / (C)hild / (P)rofile / (N)amed / (U)nconfined / (X) ix On / (D)eny / Abo(r)t / (F)inish
   ```

   Again, select the appropriate option—typically `i` for inherit if needed.

4. Another prompt may request permission to access the tty interface. If a prompt with severity 9 appears when printing to the console, enter `a` (allow).

5. You might encounter a prompt asking for read access to a system file. For instance:

   ```plaintext theme={null}
   Profile: /root/add_data.sh
   Path: /proc/filesystems
   New Mode: owner r
   Severity: 6
   [1] 'owner /proc/filesystems r,'
   (A)llow / [D]eny / [I]gnore / [G]lob / Glob with [E]xtension / [N]ew /
   Audi(t) / [O]wner permissions off / Abo(t) / [F]inish
   ```

   Since the script does not need access to this file, choose `d` to deny access.

<Callout icon="lightbulb" color="#1CB2FE">
  Ensure that you only allow permissions essential for your application to operate. Deny any unnecessary access to maintain a secure profile.
</Callout>

After processing all events, press `S` to save and `F` to finish. You should see output similar to:

```plaintext theme={null}
= Changed Local Profiles =

The following local profiles were changed. Would you like to save them?

[1 - /root/add_data.sh]
(s)ave Changes / Save Sele(c)t(ed Profile / [(V)iew Changes] / View Changes
b/w -(C)lean profiles ./ Abo(r)t
Writing updated profile for /root/add_data.sh.

Profiling: /root/add_data.sh
.

For each AppArmor event, you will be given the opportunity to choose whether the access should be allowed or denied.

[(S)can system log for AppArmor events] / (F)inish Setting /root/add_data.sh to enforce mode.
Finished generating profile for /root/add_data.sh
```

Your new AppArmor profile is now running in enforce mode.

## Verifying the Profile

To confirm that the profile is in enforce mode, use the following command:

```bash theme={null}
aa-status
```

Expected output:

```plaintext theme={null}
apparmor module is loaded.
13 profiles are loaded.
13 profiles are in enforce mode.
/root/add_data.sh
/sbin/dhclient
/usr/bin/man
/usr/lib/NetworkManager/nm-dhcp-client.action
/usr/lib/NetworkManager/nm-dhcp-helper
...
usr/sbin/tcpdump
docker-default
man_filter
man_groff
0 profiles are in complain mode.
11 processes have profiles defined.
11 processes are in enforce mode.
/root/add_data.sh
/sbin/dhclient (621)
docker-default (3970)
docker-default (4025)
docker-default (9853)
docker-default (9964)
0 processes are in complain mode.
0 processes are unconfined but have a profile defined.
```

The new profile, along with other existing profiles, is stored in the /etc/apparmor.d directory. An example profile for "add\_data.sh" might look like this:

```bash theme={null}
# Last Modified: Mon Mar 22 11:21:42 2021
#include <tunables/global>

/root/add_data.sh {
    #include <abstractions/base>
    #include <abstractions/bash>
    #include <abstractions/consoles>

    deny owner /proc/filesystems r,
    /root/add_data.sh r,
    /usr/bin/bash ix,
    /usr/bin/date mrix,
    /usr/bin/mkdir mrix,
    /usr/bin/tee mrix,
    owner /opt/app/ rw,
    owner /opt/app/data/ w,
    owner /opt/app/data/create.log w,
}
```

## Testing the Enforced Profile

To verify that the enforced profile restricts unauthorized access, modify the script to change the log file path from `/opt/app/data` to `/opt`. Update the script as follows:

```bash theme={null}
#!/bin/bash
data_directory=/opt
mkdir -p "${data_directory}"
echo "=> File created at $(date)" | tee "${data_directory}/create.log"
```

When you run the modified script:

```bash theme={null}
./add_data.sh
```

You should see an output similar to:

```plaintext theme={null}
tee: /opt/create.log: Permission denied
=> File created at Mon 22 Mar 2021 04:04:47 PM EDT
```

This confirms that while the script can output to the terminal, the AppArmor profile restricts write access only to the `/opt/app` directory, yielding a permission denied error when attempting to write directly to `/opt`.

## Working with Existing AppArmor Profiles

To load an existing profile, use the AppArmor parser command. If no output is returned, the profile has been successfully loaded.\
To disable a profile, use the same command with the `-r` flag and create a symlink to the profile in the `/etc/apparmor.d/disable` directory.

<Callout icon="lightbulb" color="#1CB2FE">
  Now that you've learned how to create and enforce AppArmor profiles for a custom application, you can explore securing applications running within Kubernetes pods using AppArmor for enhanced security.
</Callout>

This concludes the lesson on creating AppArmor profiles. Next, we will explore securing an application running inside a Kubernetes pod with AppArmor profiles.

Happy securing!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/d67be5ee-871d-4435-a187-382610cb6a1f/lesson/093e196c-059d-4eac-8816-af343c5e0695" />
</CardGroup>

---


# 📂 Section: System Hardening
## 📖 Identify and Disable Open Ports
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Identify-and-Disable-Open-Ports/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Identify-and-Disable-Open-Ports/page)

# Identify and Disable Open Ports

> This guide explores techniques to inspect a Linux system for open ports and methods to disable unnecessary ones for enhanced security and performance.

In this guide, we explore techniques to inspect a Linux system for open ports and methods to disable those that are unnecessary. By managing open ports, you can enhance your system's security and streamline network performance.

## Understanding Open Ports

When a process starts, it often binds to a port—an addressable location in the operating system that directs network traffic between applications. For example, TCP port 22 is typically dedicated to an SSH server process. Disabling unused ports minimizes potential security vulnerabilities.

## Using netstat to Check Active Ports

To determine which ports are actively listening for connections, you can use the `netstat` command. The following example shows active ports including port 22 for SSH, port 2379 for an etcd instance, and port 6443 for the Kubernetes API server, which are common on a Kubernetes control plane node:

```bash theme={null}
netstat -an | grep -w LISTEN
tcp        0      0 127.0.0.1:10248         0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:10249         0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:2379          0.0.0.0:*               LISTEN
tcp        0      0 10.53.64.6:2379         0.0.0.0:*               LISTEN
tcp        0      0 10.53.64.6:2380         0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:42893         0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:2381          0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.11:46607        0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:8080            0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:10257         0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:10259         0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN
tcp6       0      0 :::10250                :::*                    LISTEN
tcp6       0      0 :::6443                 :::*                    LISTEN
tcp6       0      0 :::10256                :::*                    LISTEN
tcp6       0      0 :::22                   :::*                    LISTEN
tcp6       0      0 :::8888                 :::*                    LISTEN
```

The output above identifies various services bound to different ports. For instance, port 53 is conventionally reserved for the Domain Name Server (DNS) and is used for both TCP and UDP traffic.

## Determining Port Usage

A straightforward way to verify the purpose of each port is by consulting the `/etc/services` file on Ubuntu-based systems. This file catalogs service names, protocols, and associated port numbers. For example, inspecting this file will confirm that port 53 is indeed allocated for DNS services.

<Callout icon="lightbulb" color="#1CB2FE">
  Before installing new software, it's critical to review which ports should remain open. Always consult the official documentation of the software—such as the kubeadm documentation for Kubernetes clusters—to understand the required ports.
</Callout>

## Disabling Unnecessary Ports

After identifying the open ports your system requires, you can proceed to disable or block the unused ones. This step is essential for bolstering your system's security and ensuring only necessary network interfaces are accessible.

## Additional References

For more detailed information, consider the following resources:

* [Kubernetes Basics](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Docker Hub](https://hub.docker.com/)
* [Terraform Registry](https://registry.terraform.io/)

By following these guidelines, you can ensure that your Linux system is not only secure but also optimized for performance through effective port management.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/d67be5ee-871d-4435-a187-382610cb6a1f/lesson/266b4f76-b359-4005-8586-05c96690941c" />
</CardGroup>

---


# 📂 Section: System Hardening
## 📖 Implement Seccomp in Kubernetes
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Implement-Seccomp-in-Kubernetes/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Implement-Seccomp-in-Kubernetes/page)

# Implement Seccomp in Kubernetes

> This article explores implementing Seccomp profiles in Kubernetes to enhance container security by filtering system calls.

In this article, we explore how to implement Seccomp profiles in Kubernetes to bolster container security by filtering system calls (syscalls). We start by reviewing how Docker and Kubernetes apply Seccomp by default and then demonstrate how to enable and customize Seccomp profiles within Kubernetes pods.

<Callout icon="lightbulb" color="#1CB2FE">
  By restricting syscalls, Seccomp helps reduce the attack surface in containerized environments. This guide outlines both default behaviors and custom configurations for running secure Kubernetes workloads.
</Callout>

***

## Default Seccomp Profile in Docker

Docker uses a built-in Seccomp profile to block approximately 60 syscalls by default. To inspect Docker’s default Seccomp configuration, we can use the open-source container introspection tool called amicontained.

Run the following command to launch amicontained as a Docker container:

```bash theme={null}
docker run r.j3ss.co/amicontained amicontained
```

The command output indicates that 64 syscalls are blocked due to Docker's default Seccomp profile. Notice that the Seccomp mode is set to filtering (mode 2):

```bash theme={null}
Container Runtime: docker
Has Namespaces:
    pid: true
    user: false
AppArmor Profile: docker-default (enforce)
Capabilities:
    BOUNDING -> chown dac_override fowner fsetid kill setgid setuid setpcap net_bind_service net_raw sys_chroot mknod audit_write setcap
Seccomp: filtering
Blocked Syscalls (64):
    MSGRCV SYSCFG SETPGID SETSID USELIB USTAT SYSFS VHAVGUP PIVOT_ROOT _SYSCTL ACCT SETTIMEOFDAY MOUNT UMOUNT2 SWAPON SWAPOFF REBOOT SETHOSTNAME SETDOMAINNAME IOPL IOPEM CREATE_MODULE INIT_MODULE DELETE_MODULE GET_KERNEL_SYMS QUERY_MODULE QUOTACLI NESSERVCTL GETPMSG PUTMSG AFS_SYSCALL TUXCALL SECURITY LOOKUP_DCOOKIE CLOCK_SETTIME VSERVER MBIND SET_MEMPOLICY GET_MEMPOLICY KEXEC_LOAD ADD_KEY REQUEST_KEY KEYCTL MIGRATE_PAGES UNSHARE MOVE_PAGES PERF_EVENT_OPEN FANOTIFY_INIT NAME_TO_HANDLE_AT OPEN_BY_HANDLE_AT CLOCK_ADJTIME SETNS PROCESS_VM_READV PROCESS_VM_WRITEV KCMP FINIT_MODULE KEXEC_FILE_LOAD
Looking for Docker.sock
```

***

## Running the Container as a Kubernetes Pod

Deploying the same image as a Kubernetes pod yields a different outcome. In Kubernetes (version 1.20 during this recording), Seccomp is not enabled by default.

Create a pod with the following command:

```bash theme={null}
kubectl run amicontained --image=r.j3ss.co/amicontained amicontained -- amicontained
```

You should see:

```bash theme={null}
pod/test created
```

Next, inspect the pod logs:

```bash theme={null}
kubectl logs amicontained
```

The log output will display Seccomp as disabled along with only 21 syscalls being blocked:

```bash theme={null}
Container Runtime: docker
Has Namespaces:
  pid: true
  user: false
AppArmor Profile: docker-default (enforce)
Capabilities:
  BOUNDING -> chown dac_override fowner fsetid kill setgid setuid setpcap
  net_bind_service net_raw sys_chroot mknod audit_write setcap
Seccomp: disabled

Blocked Syscalls (21):
  SYSCLOG SETGID SETSID VHANGUP PIVOT_ROOT ACCT SETTIMEOFDAY UMOUNT2 SWAPON
  SWAPOFF REBOOT SETHOSTNAME SETDOMAINNAME INIT_MODULE DELETE_MODULE LOOKUP_DCOOKIE
  KEXEC_LOAD FANOTIFY_INIT OPEN_BY_HANDLE_AT FINIT_MODULE KEXEC_FILE_LOAD

Looking for Docker.sock
```

<Callout icon="lightbulb" color="#1CB2FE">
  By default, Kubernetes pods do not enforce Seccomp filtering; hence, fewer syscalls are blocked.
</Callout>

***

## Enabling Seccomp in a Kubernetes Pod

To enable Seccomp filtering in a pod, specify a Seccomp profile in the pod (or container) manifest. The example below demonstrates using the default Docker profile via the `seccompProfile` field under the pod-level security context:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  labels:
    run: amicontained
  name: amicontained
spec:
  securityContext:
    seccompProfile:
      type: RuntimeDefault
  containers:
    - args:
        - amicontained
      image: r.j3ss.co/amicontained
      name: amicontained
      securityContext:
        allowPrivilegeEscalation: false
```

Setting `allowPrivilegeEscalation: false` restricts the container process from gaining additional privileges beyond what is needed.

Apply the pod definition:

```bash theme={null}
kubectl apply -f pod-definition.yaml
```

Then verify the pod logs:

```bash theme={null}
kubectl logs amicontained
```

The logs should now show that Seccomp filtering is active with additional syscalls being blocked:

```bash theme={null}
Container Runtime: docker
Has Namespaces:
  pid: true
  user: false
AppArmor Profile: docker-default (enforce)
Capabilities:
  BOUNDING -> chown dac_override fowner fsetid kill setgid setuid setpcap net_bind_service net_raw
Seccomp: filtering

Blocked Syscalls (64):
  SYSCLOG SETPGID SETSID USELIB USTAT SYSFS Vhangup PIVOT_ROOT _SYSCtl ACCT SETTIMEOFDAY MOUNT
  UMOUNT2 SWAPON SWAPOFF REBOOT SETHOSTNAME SETDOMAINNAME IOPL CREATE_MODULE INIT_MODULE DELETE_MODULE
  GET_KERNEL_SYMS QUERY_MODULE QUOTACTL NFS_SERVERCTL GETMSG PUTMSG AFS_SYSCALL TUXCALL SECURITY
  LOOKUP_DCOOKIE CLOCK_SETTIME VSERVER MBIND SET_MPOLICY GET_MEMPOLICY KEXEC_LOAD ADD_KEY REQUEST_KEY
  KEYCTL MIGRATE_PAGES UNSHARE MOVE_PAGES PERF_EVENT_OPEN FANotify_INIT NAME_TO_HANDLE_AT OPEN_BY_HANDLE_AT
  CLOCK_ADJTIME SETNS PROCESS_VM_READV PROCESS_VM_WRITEV KCMP FINIT_MODULE KEXEC_FILE_LOAD BPF USERFAULTFD
Looking for Docker.soc
```

***

## Using the Unconfined Seccomp Profile

If you prefer to run a pod without any Seccomp restrictions (which is the default behavior), explicitly set the Seccomp profile to Unconfined in your pod manifest:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  labels:
    run: amicontained
  name: amicontained
spec:
  securityContext:
    seccompProfile:
      type: Unconfined
  containers:
    - args:
        - amicontained
      image: r.j3ss.co/amicontained
      name: amicontained
      securityContext:
        allowPrivilegeEscalation: false
```

***

## Using Custom Seccomp Profiles

Custom Seccomp profiles offer granular security control based on your application's syscall needs. The following sections detail how to create a pod with a custom Seccomp profile, enforce strict policies, and tailor profiles for your specific requirements.

### Creating a Pod with a Custom Profile

In this example, we create a pod using the Ubuntu image. The container prints a message and then sleeps for 100 seconds. The pod manifest below applies a custom Seccomp profile from a file on the node.

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: test-audit
spec:
  securityContext:
    seccompProfile:
      type: Localhost
      localhostProfile: <path to the custom JSON file>
  containers:
    - command: ["bash", "-c", "echo 'I just made some syscalls' && sleep 100"]
      image: ubuntu
      name: ubuntu
      securityContext:
        allowPrivilegeEscalation: false
```

<Callout icon="lightbulb" color="#1CB2FE">
  The `localhostProfile` path is relative to the default Seccomp profile directory (typically `/var/lib/kubelet/seccomp`). For example, if you place your custom profile in `/var/lib/kubelet/seccomp/profiles/`, the path might be `profiles/audit.json`.
</Callout>

Inside your custom profile (e.g., `audit.json`), you could set the default action to log syscalls:

```json theme={null}
{
  "defaultAction": "SCMP_ACT_LOG"
}
```

Once the pod is running, all container syscalls are logged to the node’s syslog (commonly `/var/log/syslog`). You can check the logs with:

```bash theme={null}
grep syscall /var/log/syslog
```

A sample audit log might look like:

```bash theme={null}
grep syscall /var/log/syslog
Mar 19 23:53:45 node01 kernel: [ 264.340952] audit: type=1326 audit(1616198025.076:14):  auid=4294967295 uid=0 gid=0 ses=4294967295 pid=8816 comm="runc:[2:INIT]" exe="/" sig=0 arch=c000003e syscall=257 compat=0 ip=0x5642801010aa code=0x7ffc0000
Mar 19 23:53:45 node01 kernel: [ 264.340954] audit: type=1326 audit(1616198025.076:15):  auid=4294967295 uid=0 gid=0 ses=4294967295 pid=8816 comm="runc:[2:INIT]" exe="/" sig=0 arch=c000003e syscall=35 compat=0 ip=0x564280fcc662d code=0x7ffc0000
...
```

Additionally, tools like [Tracee](https://github.com/aquasecurity/tracee) can be useful for analyzing syscalls. For instance, run the Tracee container to monitor new container syscalls:

```bash theme={null}
sudo docker run --name tracee --rm --privileged --pid=host \
  -v /lib/modules/:/lib/modules:ro -v /usr/src:/usr/src:ro \
  -v /tmp/tracee:/tmp/tracee aquasec/tracee:0.4.0 --trace container=new
```

### Creating a Profile That Rejects All Syscalls

To enforce a stricter security posture, you can create a profile that denies any syscall by default. Create a JSON file (e.g., `violation.json`) with the following content:

```json theme={null}
{
  "defaultAction": "SCMP_ACT_ERRNO"
}
```

Apply this profile in your pod's security context. When created, the pod status will be "ContainerCannotRun" because even essential syscalls are blocked. For example:

Apply the pod definition:

```bash theme={null}
kubectl apply -f test-violation.yaml
```

Then check the pod status:

```bash theme={null}
kubectl get pods
```

Expected output:

```bash theme={null}
NAME             READY   STATUS                RESTARTS   AGE
test-violation   0/1     ContainerCannotRun    0          2m2s
```

<Callout icon="triangle-alert" color="#FF6B6B">
  While a strict Seccomp profile can improve security, it may render the pod non-functional if critical syscalls are blocked.
</Callout>

### Customizing and Using a Tailored Seccomp Profile

After analyzing your application’s syscall requirements—by inspecting audit logs or using tools like Tracee—you can craft a custom Seccomp profile that allows only the required syscalls.

Create a custom profile JSON file (for example, `custom.json`) with specific rules and place it in the node’s Seccomp profile directory (typically in a `profiles` folder under `/var/lib/kubelet/seccomp`).

Then reference your custom profile in a pod definition:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: test-custom
spec:
  securityContext:
    seccompProfile:
      type: Localhost
      localhostProfile: profiles/custom.json
  containers:
    - command: ["bash", "-c", "echo 'I just made some syscalls' && sleep 100"]
      image: ubuntu
      name: ubuntu
  restartPolicy: Never
```

Verify that the pod starts successfully:

```bash theme={null}
kubectl get pods
```

Expected output:

```bash theme={null}
NAME         READY   STATUS    RESTARTS   AGE
test-custom  1/1     Running   0          2m2s
```

Once your custom profile is applied, only the required syscalls will be allowed, enhancing container isolation and security.

***

## Conclusion

Implementing and customizing Seccomp profiles in Kubernetes enhances container security by limiting unnecessary syscalls. Although creating a custom profile can be time-consuming, mastering existing profiles and tailoring them to your application's needs is essential for a secure container environment.

For further details, refer to the official [Kubernetes Seccomp Documentation](https://kubernetes.io/docs/concepts/containers/seccomp-profiles/).

Now is the time to experiment with Seccomp profiles in your environment. By leveraging these security measures, you can achieve a more robust and secure Kubernetes deployment.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/d67be5ee-871d-4435-a187-382610cb6a1f/lesson/4bc6526e-316d-44f8-90f4-3ff132fa1b11" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/d67be5ee-871d-4435-a187-382610cb6a1f/lesson/c6466fea-8065-407e-8971-b3e857d2227c" />
</CardGroup>

---


# 📂 Section: System Hardening
## 📖 Least Privilege Principle
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Least-Privilege-Principle/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Least-Privilege-Principle/page)

# Least Privilege Principle

> This article explores the Least Privilege Principle, a security concept that minimizes risk by granting roles only necessary access for their tasks.

In this article, we explore the Least Privilege Principle—a critical security concept that minimizes risk and enhances operational efficiency by granting roles only the access necessary for their tasks.

<Frame>
  ![The image features the text "Least Privilege Principle" on a blue background with a geometric network design on the right.](https://kodekloud.com/kk-media/image/upload/v1752871731/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Least-Privilege-Principle/frame_0.jpg)
</Frame>

Imagine a busy international airport with flights departing every hour. The procedures a traveler follows before boarding illustrate the principle of least privilege perfectly.

1. **Baggage Drop-off:**\
   At the check-in counter, you can only check in if your flight departs within a few hours. Luggage is dropped off at the specific airline’s counter, where an attendant verifies your valid ticket before you proceed further.

2. **Immigration Check:**\
   An immigration officer checks your travel documents, and any lapse in valid documentation results in denied access.

3. **Security Screening:**\
   During security, any prohibited or hazardous items in your carry-on must be discarded.

4. **Navigating the Departure Hall:**\
   You then move through the departure hall to your boarding gate. Public areas and duty-free shops are accessible, but boarding is allowed only at the designated gate. Sensitive areas such as cargo bays and runways remain strictly off-limits.

This analogy not only highlights the traveler’s journey but also underscores the need for different access levels among the airport’s various personnel. Consider the following roles and their specific privileges:

* **Traveler:** Accesses public spaces after check-in and boards only at the designated gate.
* **Baggage Counter Employees:** Handle traveler and airline-specific information for check-in processes.
* **Security Officers:** Inspect belongings in the security area while also accessing some public spaces.
* **Store Employees:** Operate within public areas and may have extended access to backroom operations.
* **Boarding Gate Staff:** Assist travelers in boarding, similar to baggage counter staff.
* **Cleaning Staff:** Access designated areas, with some having permission for restricted zones such as terminals or cargo drop-off areas.
* **Cargo Loaders and Maintenance Workers:** Have access similar to cleaning staff and also unrestricted areas like the loading bay.
* **Pilots, Stewards, and Flight Attendants:** Possess specialized access to restricted zones, such as cockpits and specific aircraft-related areas, limited to their airline’s operations.

<Callout icon="lightbulb" color="#1CB2FE">
  Applying the principle of least privilege means granting every role only the access they need, reducing potential risks and improving overall security.
</Callout>

<Frame>
  ![The image illustrates various airport roles, including baggage counter staff, security check personnel, store employees, travelers, pilots, stewards, cargo loaders, maintenance workers, and cleaners.](https://kodekloud.com/kk-media/image/upload/v1752871732/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Least-Privilege-Principle/frame_250.jpg)
</Frame>

The same principle applies to computer systems, such as Linux operating systems and Kubernetes clusters. When securing Kubernetes infrastructure, it is paramount to restrict access by implementing measures such as:

| Security Measure                 | Description                                                                          |
| -------------------------------- | ------------------------------------------------------------------------------------ |
| Limit Node Access                | Ensure nodes have restricted user permissions to prevent unauthorized modifications. |
| Role-Based Access Control (RBAC) | Define precise access rights for users and services within the cluster.              |
| Remove Obsolete Packages         | Keep systems updated by removing software that is no longer required.                |
| Restrict Network Access          | Limit network communication between components to reduce attack surfaces.            |
| Restrict Kernel Modules          | Load only essential kernel modules and block unnecessary ones.                       |
| Fix Open Ports                   | Identify and secure any open ports to prevent unauthorized entry points.             |

<Frame>
  ![The image lists security measures: limit node access, RBAC access, remove obsolete packages, restrict network access, restrict kernel modules, and fix open ports, alongside a phone icon.](https://kodekloud.com/kk-media/image/upload/v1752871733/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Least-Privilege-Principle/frame_280.jpg)
</Frame>

Beyond user permissions, this principle extends to system components. Ensure that:

* Only the required software is installed on the host.
* Unnecessary services do not expose the nodes.
* Unused kernel modules are not loaded after boot.
* Any open ports are identified and promptly secured.

<Callout icon="lightbulb" color="#1CB2FE">
  In upcoming articles, we will delve deeper into securing Kubernetes environments, exploring how to fortify nodes, enforce RBAC, and apply additional security best practices.
</Callout>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/d67be5ee-871d-4435-a187-382610cb6a1f/lesson/26fe1d7b-c7c9-49df-9a25-a919ff3f084e" />
</CardGroup>

---


# 📂 Section: System Hardening
## 📖 Linux Capabilities
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Linux-Capabilities/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Linux-Capabilities/page)

# Linux Capabilities

> This article explores adding or removing Linux capabilities on Kubernetes pods and explains restrictions on certain operations even when running as root.

In this lesson, we explore how to add or remove Linux capabilities on Kubernetes pods and understand why certain operations, like changing the system date, can be restricted even when running as root.

Earlier, in our Seccomp lecture, we observed that even when a container runs with Seccomp set to unconfined, modifying the system date is prohibited. This behavior extends to Kubernetes pods as well. By default, Kubernetes pods do not utilize Seccomp, and a container—even running as root (UID 0)—may still be restricted from performing certain operations.

<Callout icon="lightbulb" color="#1CB2FE">
  When running containers with Docker, the default security settings include restrictions that prevent operations such as modifying the system clock, unless explicitly permitted by adjusting capabilities.
</Callout>

## Demonstration Using Docker

The example below demonstrates the restricted behavior using Docker:

```bash theme={null}
docker run -it --rm --security-opt seccomp=unconfined docker/whalesay /bin/sh
# date -s '19 APR 2012 22:00:00'
date: cannot set date: Operation not permitted
Thu Apr 19 22:00:00 UTC 2012

kubectl run --rm -it ubuntu-sleeper --image=ubuntu -- bash
```

Even though the container runs as the root user (UID 0), the attempt to change the date fails. This behavior helps us understand how Linux processes operate under different privilege levels.

## Understanding Linux Process Privileges

Before Linux kernel 2.2, processes were classified into:

* **Privileged processes:** Run by the root user (UID 0) and bypass many kernel permission checks.
* **Unprivileged processes:** Run by non-root users and are subject to various kernel restrictions.

Starting with Linux kernel 2.2, the traditional superuser privileges were broken down into individual units called capabilities. This allows administrators to grant only specific privileges to processes, even if they run as the root user.

Some examples of these capabilities include:

* **CAP\_CHOWN:** Allows changing file ownership.
* **CAP\_NET\_ADMIN:** Permits operations like modifying network interface configurations, managing routing tables, and binding processes to specific addresses.
* **CAP\_SYS\_BOOT:** Enables a process to reboot the system.
* **CAP\_SYS\_TIME:** Permits setting or adjusting the system clock.

For a comprehensive list of capabilities, consult the official Linux documentation.

## Checking Capabilities

You can determine the capabilities required by a command using the `getcap` command. For example, the `ping` command requires the `CAP_NET_RAW` capability:

```bash theme={null}
getcap /usr/bin/ping
```

The expected output is:

```bash theme={null}
/usr/bin/ping = cap_net_raw+ep
```

To inspect the capabilities of a running process, use the `getpcaps` command. For instance, to check the capabilities of the SSH daemon process:

1. Locate the PID of the SSH daemon:
   ```bash theme={null}
   ps -ef | grep /usr/sbin/sshd | grep -v grep
   ```
   Output:
   ```bash theme={null}
   root     779     1  0 03:55 ?        00:00:00 /usr/sbin/sshd -D
   ```
2. Use `getpcaps` with the PID:
   ```bash theme={null}
   getpcaps 779
   ```

## Visual Overview

The image below compares Linux capabilities before and after Kernel 2.2, highlighting examples like CAP\_CHOWN and CAP\_SYS\_TIME:

<Frame>
  ![The image illustrates Linux capabilities, comparing privileged processes before and after Kernel 2.2, highlighting specific capabilities like CAP\_CHOWN and CAP\_SYS\_TIME.](https://kodekloud.com/kk-media/image/upload/v1752871738/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Linux-Capabilities/frame_100.jpg)
</Frame>

## Linux Capabilities in Kubernetes Containers

Returning to our Ubuntu sleeper pod example, attempting to change the date from within the container resulted in:

```bash theme={null}
kubectl run --rm -it ubuntu-sleeper --image=ubuntu -- bash
root@ubuntu-sleeper:# date -s '19 APR 2012 22:00:00'
date: cannot set date: Operation not permitted
Thu Apr 19 22:00:00 UTC 2012
root@ubuntu-sleeper:#
```

This failure occurs because containers, even when running as root, are started with a limited set of capabilities. Docker, the container runtime, initiates containers with only 14 capabilities by default. Without the specific capability `CAP_SYS_TIME` required to modify the system clock, the operation is prohibited.

## Default Capabilities in Linux

The following Go code snippet demonstrates how default capabilities are defined in a Linux environment:

```go theme={null}
// DefaultCapabilities returns a Linux kernel default capabilities
func DefaultCapabilities() []string {
    return []string{
        "CAP_CHOWN",
        "CAP_DAC_OVERRIDE",
        "CAP_FOWNER",
        "CAP_MKNOD",
        "CAP_NET_RAW",
        "CAP_SETGID",
        "CAP_SETUID",
        "CAP_SETFCAP",
        "CAP_SETPCAP",
        "CAP_NET_BIND_SERVICE",
        "CAP_SYS_CHROOT",
        "CAP_KILL",
        "CAP_AUDIT_WRITE",
    }
}
```

## Modifying Container Capabilities

To adjust the capabilities for a container:

* **Add a Capability:** Update the container manifest under the security context by including the required capability (e.g., `CAP_SYS_TIME`) in the capabilities array. With this configuration, the container will be permitted to adjust the system clock.

* **Remove a Capability:** Use the drop field with an array of capabilities to be removed. For example, if you remove `CAP_CHOWN`, the `chown` command will no longer function within the container.

<Callout icon="triangle-alert" color="#FF6B6B">
  Modifying container capabilities can expose the host system to security risks. Always ensure that only the necessary capabilities are granted and follow the principle of least privilege.
</Callout>

## Conclusion

Understanding how Linux capabilities function is crucial for effectively managing security in Kubernetes pods. Experiment with modifying capabilities to gain hands-on experience, and refer to the official documentation for more detailed information.

For more insights and detailed documentation on Kubernetes and container security, consider exploring these resources:

* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Linux Capabilities Documentation](https://man7.org/linux/man-pages/man7/capabilities.7.html)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/d67be5ee-871d-4435-a187-382610cb6a1f/lesson/aa37d503-85f0-47ba-9360-31514b3c5030" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/d67be5ee-871d-4435-a187-382610cb6a1f/lesson/058cc5f9-4239-44ec-8021-e9201d4edc2b" />
</CardGroup>

---


# 📂 Section: System Hardening
## 📖 Linux Syscalls
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Linux-Syscalls/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Linux-Syscalls/page)

# Linux Syscalls

> This article explores Linux syscalls, detailing their role in process execution and interactions between user applications and the kernel.

In this article, we'll explore Linux syscalls (system calls) and examine what happens under the hood when an application or process runs. We will review how a process executes on Linux by examining some fundamental concepts of the Linux operating system.

The Linux kernel is the central component that acts as an interface between the hardware and running processes. It efficiently manages system resources by operating in a dedicated memory area called kernel space, while user applications (written in languages such as C, Java, or Python) run in user space. The kernel space contains the kernel code, device drivers, and its extensions—all essential for proper communication between hardware and applications.

## How Programs Use System Calls

System calls enable applications running in user space to request services from the kernel. For instance, when an application needs to open a file stored on disk, it cannot access the hardware directly; instead, it must instruct the kernel to perform the necessary operations. Consider the task of creating an empty file named `error.log` in the `/tmp` directory. This process involves a series of system calls, beginning with the `execve` call to execute the binary (such as the `touch` command).

The Linux kernel architecture involves many layers: user space, kernel space, system calls, and the interactions with memory, CPU, and devices. The image below reinforces this conceptual framework:

<Frame>
  ![The image illustrates the Linux Kernel architecture, showing user space, kernel space, system calls, and interactions with memory, CPU, and devices.](https://kodekloud.com/kk-media/image/upload/v1752871739/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Linux-Syscalls/frame_80.jpg)
</Frame>

Common system calls include `open`, `close`, `read`, and several others. The `execve` system call, for example, is used to execute a program by passing an array of arguments. In our example, it executes the `touch` command with `/tmp/error.log` as an argument. The output provided indicates that 23 environment variables were inherited during this call.

## Tracing Syscalls with strace

One effective method for tracing the system calls made by a process is by using the `strace` command.

> **Tip**
>
> To verify if `strace` is installed and locate its executable path, run:

```bash theme={null}
which strace
/usr/bin/strace
```

`strace` is available by default on most Linux distributions. It traces system calls invoked by an application as well as the signals delivered to it. For example, to observe the system calls made when creating a file in `/tmp`, prefix the operation with the `strace` command:

```bash theme={null}
strace touch /tmp/error.log
```

The output will begin with a line similar to the following:

```bash theme={null}
execve("/usr/bin/touch", ["touch", "/tmp/error.log"], 0x7ffce8f874f8 /* 23 vars */) = 0
...
[Output Truncated]
```

In this example:

* `execve` is the system call used to execute the program.
* The first argument is the absolute path to the executable (`/usr/bin/touch`).
* The second argument is an array containing `"touch"` and the file path `/tmp/error.log`.
* The comment `/* 23 vars */` indicates that the call inherited 23 environment variables.

To verify the number of inherited environment variables, execute:

```bash theme={null}
env | wc -l
```

The output should display `23`.

## Tracing a Running Process

To trace system calls of a process that is already running, first determine its PID. For example, to find the PID of the `etcd` process, run:

```bash theme={null}
pidof etcd
```

Assuming the PID is `3596`, attach `strace` to the process as follows:

```bash theme={null}
strace -p 3596
```

You might see output similar to this while `etcd` continues to run:

```bash theme={null}
strace: Process 3596 attached
futex(0x1ac6be8, FUTEX_WAIT_PRIVATE, 0, NULL) = 0
futex(0xc000540bc8, FUTEX_WAKE_PRIVATE, 1) = 1
```

Press Control+C to detach once you have gathered the necessary information.

## Displaying a Summary of Syscalls

To generate a summary report of system call usage, add the `-c` flag to `strace`:

```bash theme={null}
strace -c touch /tmp/error.log
```

This command produces an output summary like the one below:

```plaintext theme={null}
% time     seconds  usecs/call  calls  errors syscall
------ ----------- ----------- ------ ------ -----------
  0.00      0.000000        0      1      0  read
  0.00      0.000000        0      6      0  close
  0.00      0.000000        0      2      0  fstat
  0.00      0.000000        0      5      0  mmap
  0.00      0.000000        0      4      0  mprotect
  0.00      0.000000        0      1      0  munmap
  0.00      0.000000        0      3      0  brk
  0.00      0.000000        0      3      3  access
  0.00      0.000000        0      1      0  dup2
  0.00      0.000000        0      1      0  execve
  0.00      0.000000        0      1      0  arch_prctl
  0.00      0.000000        0      1      0  openat
  0.00      0.000000        0      1      0  utimensat
------ ----------- ----------- ------ ------ -----------
100.00      0.000000       32      3 total
```

Even simple commands like `touch` invoke multiple system calls; complex applications can generate hundreds or even thousands of system calls per second.

> **Summary**
>
> This exploration of Linux syscalls illustrates the fundamental interactions between user applications and the kernel. Understanding these interactions is essential for troubleshooting, performance tuning, and system analysis.

This concludes our in-depth look at Linux syscalls. For more advanced topics, consider exploring related resources such as the [Linux Kernel Documentation](https://www.kernel.org/doc/html/latest/) and online tutorials on system performance analysis.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/d67be5ee-871d-4435-a187-382610cb6a1f/lesson/57f1aafe-3307-4bd0-bde4-84f472b588af" />
</CardGroup>

---


# 📂 Section: System Hardening
## 📖 Minimize IAM roles
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Minimize-IAM-roles/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Minimize-IAM-roles/page)

# Minimize IAM roles

> This article explains implementing the principle of least privilege using IAM on public cloud platforms to enhance security and minimize unauthorized access.

In this lesson, we explore how to implement the principle of least privilege using Identity and Access Management (IAM) on public cloud platforms like AWS. The "least privilege" strategy ensures that each user or service has only the necessary permissions to perform its tasks, thereby reducing the risk of unauthorized access.

## Understanding Root and IAM User Roles

Earlier, we discussed the different types of accounts in Linux and why using a root user for daily operations is not advisable. Similarly, in public cloud platforms like AWS, the root account created during signup holds full administrative privileges. Although you initially access the AWS Management Console using the email associated with the root account, it's best practice to use this account only to create new IAM users and assign them the appropriate permissions. Once new IAM user accounts are set up, the root credentials should be securely stored and used only when absolutely necessary.

<Callout icon="lightbulb" color="#1CB2FE">
  Avoid using the root account for everyday tasks. Instead, delegate responsibilities using IAM users and groups to enforce the principle of least privilege.
</Callout>

### Example: AWS Account Setup

Consider a scenario where a user named Mark ([mark@example.com](mailto:mark@example.com)) creates a new AWS account. Initially, Mark signs in using his root credentials, which grants him full administrative privileges. To secure his environment, Mark should create individual IAM users for team members rather than relying on the root account for daily operations.

## Creating IAM Users and Groups

Let's create several new IAM users: Lucy, Shiva, Abdul, and Anita.

<Frame>
  ![The image shows an AWS root account hierarchy diagram with four users: Lucy, Shiva, Abdul, and Anita.](https://kodekloud.com/kk-media/image/upload/v1752871741/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Minimize-IAM-roles/frame_120.jpg)
</Frame>

Cloud providers, by default, assign minimal permissions to new users. In AWS, a user's capabilities are determined by the permissions defined in their IAM roles. For example, if Shiva, Abdul, and Anita are developers needing to create EC2 instances and access S3 buckets, you would attach policies granting only these essential permissions.

<Frame>
  ![The image shows a diagram of user permissions for AmazonEC2Create and AmazonS3BucketAccess, with checkmarks and crosses indicating access levels for Shiva, Abdul, and Anita.](https://kodekloud.com/kk-media/image/upload/v1752871742/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Minimize-IAM-roles/frame_160.jpg)
</Frame>

### Simplifying Permissions with IAM Groups

For easier management, group users with similar roles into an IAM group. An IAM group allows you to grant the same set of permissions to multiple users by attaching policies directly to the group. For instance, create a "Developer Group" that includes Shiva, Abdul, and Anita, and attach the necessary policies for EC2 and S3 access.

<Frame>
  ![The image shows an IAM group named "Developer Group" with members Shiva, Abdul, and Anita, linked to permissions for AmazonEC2Create and AmazonS3BucketAccess.](https://kodekloud.com/kk-media/image/upload/v1752871744/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Minimize-IAM-roles/frame_180.jpg)
</Frame>

## Managing Permissions for AWS Resources

Permissions management isn’t limited to human users; AWS resources also require explicit access controls. For example, an EC2 instance that needs to access S3 buckets does not have inherent permissions. To enable access, create an IAM role—such as "S3 Access Role"—and attach the same policies used for the developer group. This role should then be assigned to the EC2 instance.

It’s important to note that unlike user accounts, you cannot attach an IAM policy directly to an AWS resource. Always use IAM roles to ensure that AWS services operate with only the minimum required permissions.

<Callout icon="triangle-alert" color="#FF6B6B">
  Avoid alternative methods of granting access (like providing programmatic keys directly) as they are generally less secure. Use IAM roles to minimize risk and adhere to the principle of least privilege.
</Callout>

<Frame>
  ![The image illustrates an AWS architecture involving S3BucketAccessRole, AmazonS3BucketAccess, and an S3 bucket, showing access permissions and role assignments.](https://kodekloud.com/kk-media/image/upload/v1752871745/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Minimize-IAM-roles/frame_300.jpg)
</Frame>

## Continual Review and Auditing

Regular audits of your IAM policies and permissions are crucial to maintaining a secure environment. Periodically review and remove any unused permissions. AWS provides built-in tools like [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/trustedadvisor) for real-time security checks and recommendations. Equivalent tools include [Security Command Center](https://cloud.google.com/security-command-center) in Google Cloud and [Azure Advisor](https://azure.microsoft.com/en-us/services/advisor/) in Microsoft Azure.

## Conclusion

It is essential to understand and apply least privilege principles using IAM roles to safeguard your cloud infrastructure. While IAM details might not be the primary focus of certification exams, having a solid grasp of these concepts is beneficial.

<Frame>
  ![The image shows logos for AWS Trusted Advisor, Google Cloud's Security Command Center, and Azure Advisor, representing cloud security and advisory services from Amazon, Google, and Microsoft.](https://kodekloud.com/kk-media/image/upload/v1752871748/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Minimize-IAM-roles/frame_340.jpg)
</Frame>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/d67be5ee-871d-4435-a187-382610cb6a1f/lesson/e61a4d59-3c31-4374-880f-87a0386691f4" />
</CardGroup>

---


# 📂 Section: System Hardening
## 📖 Minimize external access to the network
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Minimize-external-access-to-the-network/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Minimize-external-access-to-the-network/page)

# Minimize external access to the network

> This article discusses tools and techniques to restrict network access to servers and enhance security through proper port management and firewall configurations.

In this lesson, we explore tools and techniques that restrict network access to your servers. Understanding how services bind to ports is critical for establishing a secure environment. For instance, an SSH server typically listens on port 22, meaning that any device on the network could potentially access it unless proper restrictions are in place.

## Verifying Port Bindings

You can verify if a port is actively listening for incoming connections with the following commands. Notice that when port 22 is bound to IP address 0.0.0.0, it indicates that the service is accessible from any network interface:

```bash theme={null}
systemctl status ssh
```

```bash theme={null}
cat /etc/services | grep ssh
```

```plaintext theme={null}
ssh             22/tcp                     # SSH Remote Login Protocol
```

Without any additional configuration, any device on the network can establish a connection to the server on the open ports. To see a broader picture of the active ports, the `netstat` command can be used to list all listening ports:

```bash theme={null}
netstat -an | grep -w LISTEN
```

```plaintext theme={null}
tcp        0      0 127.0.0.1:10248         0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:10249         0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:2379          0.0.0.0:*               LISTEN
tcp        0      0 10.53.64.6:2379         0.0.0.0:*               LISTEN
tcp        0      0 10.53.64.6:2380         0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:42893         0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:2381          0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.11:46607        0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:8080            0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:10257         0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:10259         0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:53              0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN
tcp6       0      0 :::10250                :::*                    LISTEN
tcp6       0      0 :::6443                 :::*                    LISTEN
tcp6       0      0 :::10256                :::*                    LISTEN
tcp6       0      0 :::22                   :::*                    LISTEN
tcp6       0      0 :::8888                 :::*                    LISTEN
```

<Callout icon="lightbulb" color="#1CB2FE">
  Applying the principle of least privilege is essential—limit access only to necessary ports and services to reduce your system’s attack surface.
</Callout>

## Approaches to Network Security

In real-world environments with interconnected clients and servers across multiple routers and switches, adopting layered security measures is critical. There are two primary approaches to enforcing network security:

1. **Network-wide Security:**\
   Utilize external firewalls or dedicated security appliances such as Cisco ASA, Juniper NextGen Firewall, Barracuda NextGen Firewall, or Fortinet devices. These solutions allow you to define complex rules that control the flow of traffic across the entire network.

2. **Server-level Security:**\
   Implement host-based firewalls using tools like iptables, firewalld, or UFW on Linux systems, and leverage built-in firewall capabilities on Windows servers. This approach restricts network access on a per-server basis.

## Next Steps: Configuring UFW

In the next section, we will demonstrate how to use UFW (Uncomplicated Firewall) from the command line to configure a Linux firewall effectively. UFW simplifies the process of setting firewall rules for both incoming and outgoing connections.

For additional insights on firewall configuration and network security best practices, consider consulting the following resources:

* [UFW Documentation](https://help.ubuntu.com/community/UFW)
* [iptables Man Page](https://linux.die.net/man/8/iptables)

This guide equips you with the foundational knowledge to minimize external network access and enhance your overall security posture.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/d67be5ee-871d-4435-a187-382610cb6a1f/lesson/aa5b922c-75d8-4df0-8ad8-dc272920caa9" />
</CardGroup>

---


# 📂 Section: System Hardening
## 📖 Privilege Escalation in Linux
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Privilege-Escalation-in-Linux/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Privilege-Escalation-in-Linux/page)

# Privilege Escalation in Linux

> This article explores privilege escalation in Linux, focusing on the use of sudo for executing commands with elevated privileges securely.

In this lesson, we explore how privilege escalation works in Linux and why it is critical from a security perspective. Previously, we disabled root user login via SSH because using the root account for routine tasks poses significant security risks. However, performing administrative tasks—such as installing software or conducting system maintenance—still requires elevated privileges.

One of the most effective methods to execute commands with root privileges is through the sudo command. Using sudo enables trusted users to run administrative commands by providing their own password, which not only strengthens security but also creates an audit trail of actions performed.

<Callout icon="lightbulb" color="#1CB2FE">
  For enhanced security, always use sudo rather than logging in directly as root.
</Callout>

## Using Sudo Versus Direct Commands

If you attempt to install a package without sudo privileges, you will encounter a permission error:

```bash theme={null}
apt install nginx
E: Could not open lock file /var/lib/dpkg/lock-frontend - open (13: Permission denied)
E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?
```

When you prepend the command with sudo, the system will prompt you for your password, allowing you to proceed with administrative tasks:

```bash theme={null}
sudo apt install nginx
[sudo] password for michael:
```

## Understanding the /etc/sudoers File

The default configuration for sudo is maintained in the `/etc/sudoers` file. This file governs policies for executing commands with elevated privileges and can only be modified by users who have been explicitly granted access. Only users listed in the `/etc/sudoers` file can use sudo, thereby preventing unauthorized root logins.

Below is an excerpt from the `/etc/sudoers` file that demonstrates a granular assignment of privileges:

```bash theme={null}
cat /etc/sudoers
User privilege specification
root    ALL=(ALL:ALL) ALL
# Members of the admin group may gain root privileges
%admin ALL=(ALL) ALL
# Allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) ALL
# Allow mark to run any command
mark    ALL=(ALL:ALL) ALL
# Allow Sarah to reboot the system
sarah localhost=/usr/bin/shutdown -r now
# See sudoers(5) for more information on "#include" directives
#include /etc/sudoers.d
```

Each line in the sudoers file is structured as follows:

1. **User or Group:** The first field specifies the user or group (groups are prefixed with `%`) that receives the privileges.
2. **Host Specification:** The second field, typically set to `ALL`, indicates that the privileges apply to all hosts (commonly confined to the localhost).
3. **Run-as Specification:** The third field, enclosed in parentheses, indicates the user(s) as whom the commands will be executed. “ALL” means that commands can be run as any user.
4. **Command Specification:** The fourth field specifies the allowed commands. Using “ALL” permits any command, though you can restrict users to specific commands, as demonstrated in the entry for Sarah.

Using sudo in this way executes the command in the user's shell environment, rather than switching entirely to a root shell. For further security, you can assign a no-login shell to the root account.

<Callout icon="triangle-alert" color="#FF6B6B">
  Avoid modifying the `/etc/sudoers` file improperly—always use the `visudo` command to safely edit this file.
</Callout>

That concludes this lesson. Please continue with the practice exercises to work with SSH and sudo.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/d67be5ee-871d-4435-a187-382610cb6a1f/lesson/5c0e085f-5fd0-41a5-b248-c53afa22bb32" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/d67be5ee-871d-4435-a187-382610cb6a1f/lesson/a4f40d83-225d-40b2-a6e2-90f3f70a72a0" />
</CardGroup>

---


# 📂 Section: System Hardening
## 📖 Remove Obsolete Packages and Services
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Remove-Obsolete-Packages-and-Services/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Remove-Obsolete-Packages-and-Services/page)

# Remove Obsolete Packages and Services

> This guide explores best practices for removing unnecessary packages and services to keep systems lean and secure.

In this guide, we'll explore best practices for keeping your system lean and secure by eliminating unnecessary packages and services. Over time, systems can accumulate software installed by default from snapshots or image templates, which increases complexity and enlarges your security attack surface.

<Callout icon="lightbulb" color="#1CB2FE">
  Regularly auditing installed software and services is vital. This process helps ensure that only essential components are maintained and updated with the latest security patches. For example, verify whether Apache is genuinely needed on Kubernetes cluster nodes or if it was installed inadvertently.
</Callout>

<Frame>
  ![The image advises installing only necessary packages, listing "kubelet," "kubeadm," "Container runtime," and "kubectl" in green, and "apache2" in red.](https://kodekloud.com/kk-media/image/upload/v1752871749/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Remove-Obsolete-Packages-and-Services/frame_50.jpg)
</Frame>

## Managing Services with systemd

Modern Linux distributions commonly use systemd to manage services. The `systemctl` utility provides comprehensive control to view service status, start, and stop essential services.

For instance, to check the status of the Apache service, run:

```plaintext theme={null}
systemctl status apache2
Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset: enabled)
Drop-In: /lib/systemd/system/apache2.service.d
 └─apache2-system.conf
Active: active (running) since Mon 2021-03-29 18:01:14 UTC; 1s ago
Process: 19026 ExecStart=/usr/sbin/apachectl start (code=exited, status=0/SUCCESS)
Main PID: 19037 (apache2)
Tasks: 55 (limit: 7372)
CGroup: /system.slice/apache2.service
 ├─19037 /usr/sbin/apache2 -k start
 ├─19038 /usr/sbin/apache2 -k start
 └─19039 /usr/sbin/apache2 -k start
```

This output confirms that Apache is active and running, with its main configuration file located at `/lib/systemd/system/apache2.service`. While many packages install their service files automatically, some services might be manually added to launch additional processes. It is crucial to identify and manage only the services required for your environment.

### Listing All Installed Services

To view all services installed on your system, use:

```bash theme={null}
systemctl list-units --type service
```

A sample output includes:

```plaintext theme={null}
apache2.service         loaded active running   The Apache HTTP Server
apparmor.service        loaded active exited    AppArmor initialization
containerd.service      loaded active running   containerd container runtime
dbus.service            loaded active running   D-Bus System Message Bus
docker.service          loaded active running   Docker Application Container Engine
ebtables.service        loaded active exited    ebtables ruleset management
kmod-static-nodes.service loaded active exited   Create list of required static device nodes
kubelet.service         loaded active running   kubelet: The Kubernetes Node Agent
proxy.service           loaded active running   kubectl proxy 8888
systemd-journal-flush.service loaded active exited Flush Journal to Persistent Storage
```

## Disabling Unnecessary Services

If you determine that a service file is not needed, you can disable and stop it. For example, to disable Apache:

```bash theme={null}
systemctl stop apache2
systemctl disable apache2
```

You might see output similar to:

```plaintext theme={null}
Synchronizing state of apache2.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install disable apache2
```

After stopping the service, remove the corresponding package. For example, to remove Apache using `apt`:

```bash theme={null}
apt remove apache2
```

A sample removal process output would be:

```plaintext theme={null}
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages were automatically installed and are no longer required:
  apache2-bin apache2-data apache2-utils libapr1 libaprutil1 libaprutil1-dbd-sqlite3
  libapru1-ldap liblua5.2-0 ssl-cert
Use 'apt autoremove' to remove them.
The following packages will be REMOVED:
  apache2
0 upgraded, 0 newly installed, 1 to remove and 23 not upgraded.
After this operation, 536 kB disk space will be freed.
Do you want to continue? [Y/n] Y
(Reading database ... 15908 files and directories currently installed.)
Removing apache2 (2.4.29-1ubuntu4.14) ...
invoke-rc.d: policy-rc.d denied execution of stop.
invoke-rc.d: policy-rc.d denied execution of stop.
```

<Callout icon="triangle-alert" color="#FF6B6B">
  Before purging any package, ensure that it is not required by other services or dependencies. Removing essential software may disrupt system functionality.
</Callout>

## Further Reading

For additional best practices in configuring and managing services, refer to section 2 of the [CIS Benchmarks for Distribution Independent Linux](https://www.cisecurity.org/cis-benchmarks/).

By following these guidelines, you can streamline your system by maintaining only the essential packages and services, thereby reducing complexity and enhancing overall security.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/d67be5ee-871d-4435-a187-382610cb6a1f/lesson/3238a3aa-4ff7-4ab7-a8cf-6a3101b2078c" />
</CardGroup>

---


# 📂 Section: System Hardening
## 📖 Restrict Kernel Modules
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Restrict-Kernel-Modules/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Restrict-Kernel-Modules/page)

# Restrict Kernel Modules

> This guide explains how to restrict specific Linux kernel modules to enhance system security.

In this guide, you'll learn how to restrict the use of specific Linux kernel modules to improve the security of your system. The Linux kernel follows a modular design, making it easy to extend its capabilities dynamically. For example, when new hardware is connected, the kernel automatically or manually loads the necessary module—using tools such as modprobe or insmod—to enable device support (e.g., video card drivers).

## Loading and Listing Kernel Modules

Kernel modules are loaded as required, either manually by a system administrator or automatically by the kernel. For instance, to load the PC Speaker module manually, execute the following command as the root user:

```bash theme={null}
modprobe pcspkr
```

After loading modules, you can list all active modules using:

```bash theme={null}
lsmod
```

A typical output from the `lsmod` command might resemble:

```bash theme={null}
# lsmod
Module                  Size  Used by
floppy                 69417  0
xt_conntrack           16384  1
ipt_MASQUERADE         16384  1
nf_nat_masquerade_ipv4 16384  1 ipt_MASQUERADE
nf_conntrack_netlink   40960  0
nfnetlink              16384  2 nf_conntrack_netlink
xfrm_user              32768  1
xfrm_algo              16384  1 xfrm_user
xt_addrtype            16384  2
iptable_filter         16384  1
iptable_nat            16384  1
nf_conntrack_ipv4      16384  3
nf_defrag_ipv4         16384  1 nf_conntrack_ipv4
nf_nat_ipv4            16384  1 iptable_nat
```

<Callout icon="lightbulb" color="#1CB2FE">
  Be aware that an unprivileged process running inside a pod may cause some network protocol-related modules to load automatically—for example, by creating a network socket.
</Callout>

Due to this behavior, attackers might exploit the automatic module loading. Restricting these modules proactively enhances your system's security posture.

## Blacklisting Kernel Modules

To prevent potential security risks, you can blacklist kernel modules so that they are not loaded by the system—even if triggered by certain operations like network socket creation.

### Example: Blacklisting the SCTP Module

The SCTP module is seldom used in Kubernetes clusters and is a common example to blacklist. Follow these steps to disable its loading:

1. Create or edit a configuration file under `/etc/modprobe.d/` (e.g., `/etc/modprobe.d/blacklist.conf`).
2. Add the following entry to the file:

   ```bash theme={null}
   cat /etc/modprobe.d/blacklist.conf
   blacklist sctp
   ```

You can use any file name ending with a `.conf` extension as long as it is located in the `/etc/modprobe.d/` directory.

### Blacklisting Multiple Modules

To also prevent the loading of the dccp module (Datagram Congestion Control Protocol), append its entry into the same file. Once done, reboot your system and confirm that the module is no longer active:

```bash theme={null}
cat /etc/modprobe.d/blacklist.conf
blacklist sctp
blacklist dccp
shutdown -r now
lsmod | grep dccp
```

<Callout icon="triangle-alert" color="#FF6B6B">
  After updating the configuration file, reboot your system to ensure changes take effect. Failure to do so might leave the module active, potentially exposing your system to security risks.
</Callout>

For further details on kernel module security and additional best practices, refer to section 3.4 in the [CIS Benchmarks for Kubernetes](https://www.cisecurity.org/benchmark/kubernetes/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/d67be5ee-871d-4435-a187-382610cb6a1f/lesson/2af4c922-95be-4292-a78d-eccce18e5359" />
</CardGroup>

---


# 📂 Section: System Hardening
## 📖 Restrict Syscalls Using Seccomp
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Restrict-Syscalls-Using-Seccomp/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Restrict-Syscalls-Using-Seccomp/page)

# Restrict syscalls using seccomp

> This article explores restricting system calls in applications using Seccomp to enhance security and minimize the attack surface.

In this article, we’ll explore how to restrict the system calls (syscalls) that applications can invoke, limiting them to only those essential for their operation. This approach minimizes the attack surface, boosting security by preventing access to all 435+ available Linux syscalls.

Even seemingly simple commands, such as using the touch command, trigger multiple syscalls. For example, running:

```bash theme={null}
strace -c touch /tmp/error.log
% time     seconds  usecs/call     calls    errors  syscall
-------  -----------  -----------  --------  -------  ----------------
  0.00    0.000000        0     1              1    read
  0.00    0.000000        0     6              0    close
  0.00    0.000000        0     2              0    fstat
  0.00    0.000000        0     5              0    mmap
  0.00    0.000000        0     4              0    mprotect
  0.00    0.000000        0     1              0    munmap
  0.00    0.000000        0     3              0    brk
  0.00    0.000000        0     3              3    access
  0.00    0.000000        0     1              0    dup2
  0.00    0.000000        0     1              0    execve
  0.00    0.000000        0     1              0    arch_prctl
  0.00    0.000000        0     3              0    openat
  0.00    0.000000        0     1              0    utimensat
-------  -----------  -----------  --------  -------  ----------------
100.00    0.000000      32     3    total
```

Running the command again shows similar syscall statistics, illustrating that even everyday applications use numerous syscalls:

```bash theme={null}
strace -c touch /tmp/error.log
% time     seconds  usecs/call  calls  errors syscall
------ ----------- ----------- ------ --------- ----------------
 0.00      0.000000         0.0      1       0  read
 0.00      0.000000         0.0      6       0  close
 0.00      0.000000         0.0      2       0  fstat
 0.00      0.000000         0.0      5       0  mmap
 0.00      0.000000         0.0      4       0  mprotect
 0.00      0.000000         0.0      1       0  munmap
 0.00      0.000000         0.0      3       0  brk
 0.00      0.000000         0.0      3       3  access
 0.00      0.000000         0.0      2       0  dup2
 0.00      0.000000         0.0      1       0  execve
 0.00      0.000000         0.0      1       0  arch_prctl
 0.00      0.000000         0.0      3       0  openat
 0.00      0.000000         0.0      1       0  utimensat
------ ----------- ----------- ------ --------- ----------------
100.00     0.000000        32.0     32       3  total
```

Allowing unrestricted syscall access increases the risk of exploitation. For instance, the [Dirty COW vulnerability](https://en.wikipedia.org/wiki/Dirty_COW) in 2016 exploited the ptrace syscall to write to a read-only file, leading to privilege escalation and container escape.

<Frame>
  ![The image describes CVE-2016-5195, a Linux kernel vulnerability known as "Dirty COW," allowing privilege escalation via a race condition in memory handling.](https://kodekloud.com/kk-media/image/upload/v1752871750/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Restrict-syscalls-using-seccomp/frame_60.jpg)
</Frame>

## The Role of Seccomp

By default, the Linux kernel permits all user-space programs to invoke any syscall. Seccomp (Secure Computing) is a kernel-level feature, introduced in 2005 and available since Linux version 2.6.12, that allows you to sandbox applications by filtering their allowed syscalls.

To verify if your kernel supports Seccomp, run:

```bash theme={null}
grep -i seccomp /boot/config-$(uname -r)
CONFIG_HAVE_ARCH_SECCOMP_FILTER=y
CONFIG_SECCOMP_FILTER=y
CONFIG_SECCOMP=y
```

If these options are set to "y", then Seccomp is supported on your system.

### Demonstrating Seccomp in Action

First, run a container using the popular Docker whalesay image. This container prints Docker’s signature whale ASCII art alongside a provided argument (here, "hello!"):

```bash theme={null}
docker run docker/whalesay cowsay hello!
< hello! >
       ------
        \
         \
          ##     :
       ## ## ##  ==
       ## ## ##  ===
        '""""""'   /
         ~~~  ~~~~~~~~~~~~~~~~~~~ ~  ---
```

Next, start another container with an interactive shell. Inside the container, try changing the system time. Note that the shell runs as PID 1:

```bash theme={null}
docker run -it --rm docker/whalesay /bin/sh
#
# date -s '19 APR 2012 22:00:00'
date: cannot set date: Operation not permitted
```

You can inspect the container’s process status by reading `/proc/1/status`. The Seccomp field should indicate a value of 2, meaning a filtered Seccomp profile is in use.

### Seccomp Modes

Seccomp operates in three distinct modes:

* **Mode 0:** Seccomp is disabled.
* **Mode 1:** Strict mode, permitting only four syscalls: read, write, exit, and sigreturn.
* **Mode 2:** Filter mode, allowing a defined subset of syscalls based on a filtering profile. Our container example uses Mode 2.

The diagram below summarizes these modes:

<Frame>
  ![The image outlines three syscall restriction modes: Mode 0 (DISABLED), Mode 1 (STRICT), and Mode 2 (FILTERED).](https://kodekloud.com/kk-media/image/upload/v1752871751/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Restrict-syscalls-using-seccomp/frame_220.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Docker automatically applies a default Seccomp filter if your host supports Seccomp. This default filter is defined via a JSON document that whitelists approximately 60 syscalls.
</Callout>

## Default Docker Seccomp Profile

The default Docker profile is designed to block dangerous syscalls such as ptrace, which was exploited in the Dirty COW vulnerability. Here is an example snippet of a default Seccomp JSON profile used by Docker:

```json theme={null}
{
  "defaultAction": "SCMP_ACT_ERRNO",
  "architectures": [
    "SCMP_ARCH_X86_64",
    "SCMP_ARCH_X86",
    "SCMP_ARCH_X32"
  ],
  "syscalls": [
    {
      "names": [
        "arch_prctl",
        "brk",
        "capget",
        "capset",
        "mkdir",
        "close",
        "execve",
        "...",
        "clone"
      ],
      "action": "SCMP_ACT_ALLOW"
    }
  ]
}
```

The key elements of any Seccomp JSON profile are:

1. **Architectures** – Defines the supported CPU architectures (e.g., x86\_64, x86, x32).
2. **Syscalls** – An array listing syscall names and their permitted actions.
3. **Default Action** – Determines how to handle syscalls not explicitly listed. Whitelist profiles typically deny undeclared syscalls.

A **whitelist profile** explicitly allows certain syscalls while denying all others:

```json theme={null}
{
  "defaultAction": "SCMP_ACT_ERRNO",
  "architectures": [
    "SCMP_ARCH_X86_64",
    "SCMP_ARCH_X86",
    "SCMP_ARCH_X32"
  ],
  "syscalls": [
    {
      "names": [
        "<syscall-1>",
        "<syscall-2>",
        "<syscall-3>"
      ],
      "action": "SCMP_ACT_ALLOW"
    }
  ]
}
```

In contrast, a **blacklist profile** allows all syscalls by default and only denies those specifically listed:

```json theme={null}
{
  "defaultAction": "SCMP_ACT_ALLOW",
  "architectures": [
    "SCMP_ARCH_X86_64",
    "SCMP_ARCH_X86",
    "SCMP_ARCH_X32"
  ],
  "syscalls": [
    {
      "names": [
        "<syscall-1>",
        "<syscall-2>",
        "<syscall-3>"
      ],
      "action": "SCMP_ACT_ERRNO"
    }
  ]
}
```

<Callout icon="triangle-alert" color="#FF6B6B">
  While blacklist profiles are easier to implement, they are inherently less secure compared to whitelist profiles due to the possibility of overlooking dangerous syscalls.
</Callout>

The default Docker Seccomp profile on x86 blocks around 60 syscalls related to functions such as system time adjustments, file system mounts, and kernel module loading. This is why changing the system time in our earlier container failed:

```bash theme={null}
docker run -it --rm docker/whalesay /bin/sh
#
# date -s '19 APR 2012 22:00:00'
date: cannot set date: Operation not permitted
```

For a complete list of blocked syscalls, refer to the [Docker documentation](https://docs.docker.com/engine/security/seccomp/).

## Custom Seccomp Profiles

Although Docker’s default profile enhances security by restricting many dangerous syscalls, you can further harden your container by using a custom Seccomp profile. For example, to block the mkdir syscall, you might modify the default filter and save it as custom.json:

```json theme={null}
{
  "defaultAction": "SCMP_ACT_ERRNO",
  "architectures": [
    "SCMP_ARCH_X86_64",
    "SCMP_ARCH_X86",
    "SCMP_ARCH_X32"
  ],
  "syscalls": [
    {
      "names": [
        "arch_prctl",
        "brk",
        "capget",
        "capset",
        "close",
        "execve",
        "clone"
      ],
      "action": "SCMP_ACT_ALLOW"
    }
  ]
}
```

Start a container using your custom profile with the --security-opt flag:

```bash theme={null}
docker run -it --rm --security-opt seccomp=/root/custom.json docker/whalesay /bin/sh
```

Within this container, attempting to create a directory using mkdir will result in an error:

```bash theme={null}
/ #
/ # mkdir test
mkdir: can't create directory 'test': Operation not permitted
```

It is also possible to disable Seccomp entirely using the "unconfined" flag, though this is strongly discouraged:

```bash theme={null}
docker run -it --rm --security-opt seccomp=unconfined docker/whalesay /bin/sh
#
```

Even without a Seccomp profile, certain syscalls (like those used to change the system time) may remain blocked by additional Docker security measures:

```bash theme={null}
docker run -it --rm --security-opt seccomp=unconfined docker/whalesay /bin/sh
# date -s '19 APR 2012 22:00:00'
date: cannot set date: Operation not permitted
```

Additional security layers are discussed in further lessons.

***

For more guidance on Docker security and related topics, please refer to the [Docker Documentation](https://docs.docker.com/engine/security/seccomp/) and other linked resources.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/d67be5ee-871d-4435-a187-382610cb6a1f/lesson/5e9b6232-59d3-44b3-8716-a5dfe51a2411" />
</CardGroup>

---


# 📂 Section: System Hardening
## 📖 SSH Hardening
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/SSH-Hardening/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/SSH-Hardening/page)

# SSH Hardening

> Learn to enhance the security of SSH on Linux servers through key-based authentication and configuration modifications.

SSH is a critical service used to log into remote Linux servers and execute commands securely. In this lesson, you'll learn how to harden SSH to enhance the security of your nodes.

## Overview

Connecting to a remote server typically involves using the ssh command with the server’s IP address or hostname. You can specify the remote user by either prepending the username followed by an @ symbol (e.g., user\@hostname) or by using the -l flag. Remember, the remote server must have the SSH service running and allow connections through port 22.

Also, valid authentication credentials are required to access the server. These credentials can be either a username and password combination or an SSH key pair for a passwordless login. In the following sections, we first explore basic SSH usage and then move on to setting up SSH key pairs.

## Basic SSH Connection

To connect from your laptop to a Linux host named node01, simply run:

```bash theme={null}
ssh node01
```

If no username is specified, SSH will use your local username (for example, mark). When connected, you will be prompted to enter the password for that user on the remote system. In this scenario, your laptop acts as the client while node01 functions as the server running the SSH service.

<Callout icon="lightbulb" color="#1CB2FE">
  If you encounter connection issues, ensure that the SSH service is active on the remote server and that port 22 is open.
</Callout>

## Using SSH Key Pairs for Authentication

A more secure authentication method involves using a cryptographic key pair—composed of a private key on the client and a public key installed on the remote server. With this setup, you can log in without repeatedly entering a password.

### Generating an SSH Key Pair

Generate the key pair on your client (e.g., your laptop) using the ssh-keygen command:

```bash theme={null}
ssh-keygen -t rsa
```

During generation, you will be prompted to enter a passphrase. Although optional, adding a passphrase increases security in case your private key is compromised. Note that using a passphrase will require you to enter it each time the key is used. The keys are stored in a hidden directory within your home folder (.ssh), with the public key typically named id\_rsa.pub and the private key as id\_rsa.

Example output:

```bash theme={null}
ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/home/mark/.ssh/id_rsa): 
/home/mark/.ssh/id_rsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/mark/.ssh/id_rsa.
Your public key has been saved in /home/mark/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:PCRTdbxxzffzmi8uunjn5V/1LZCG0BvhVJYXBr9gYsE mark@localhost
The key's randomart image is:
+---[RSA 2048]----+
|      .o=oo+    |
|       +E=++    |
|      o * o=. o |
|       = o*.o.   |
|      S o + .    |
|       . . oo+   |
|          .. o+..|
|         .o=..oo+|
|          ..o.o+.|
+----[SHA256]-----+
```

The public key (id\_rsa.pub) is shared with remote systems, while the private key (id\_rsa) stays secure on your client system.

### Copying the Public Key to the Remote Server

To enable passwordless login, copy the public key to the remote server using the ssh-copy-id command. For example, if your username is mark and the remote server is node01, run:

```bash theme={null}
ssh-copy-id mark@node01
```

After providing your password for the remote system, the public key is appended to the `authorized_keys` file inside the `.ssh` directory of your remote home folder. You can verify its content with:

```bash theme={null}
cat /home/mark/.ssh/authorized_keys
```

This confirms that the public key has been successfully installed. Going forward, you should be able to connect without entering your password each time.

## Hardening the SSH Configuration

Once key-based authentication is set up, you can further secure your server by modifying the SSH configuration.

### Disabling Root Login

Disabling remote logins for the root account is a best security practice. This prevents unauthorized direct root access. Instead, use standard user accounts with privilege escalation tools like sudo for administrative tasks.

Edit the SSH configuration file as the root user:

```bash theme={null}
vi /etc/ssh/sshd_config
```

Locate the line for PermitRootLogin and change it to:

```bash theme={null}
PermitRootLogin no
```

### Disabling Password-Based Authentication

Since key-based authentication is now in place, you can disable password-based authentication to further protect your server. In the same configuration file (`/etc/ssh/sshd_config`), find the PasswordAuthentication directive and update it as follows:

```bash theme={null}
PasswordAuthentication no
```

After making these changes, save the file and restart the SSH service:

```bash theme={null}
systemctl restart sshd
```

<Callout icon="lightbulb" color="#1CB2FE">
  After restarting the SSH service, ensure you can log in with your SSH key. It is advised to keep an active session until you confirm that key-based authentication works properly, to avoid locking yourself out.
</Callout>

## Summary

In this lesson, you learned how to secure your Linux nodes by hardening the SSH service. We covered:

* Basic SSH connection commands
* Generating and using SSH key pairs for enhanced security
* Copying your public key to the remote server
* Securing the SSH configuration by disabling root login and password-based authentication

For more detailed security guidance, consider exploring established best practices for SSH hardening.

Happy securing!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/d67be5ee-871d-4435-a187-382610cb6a1f/lesson/ca52732f-2d65-4d47-8eca-1f42459c01f2" />
</CardGroup>

---


# 📂 Section: System Hardening
## 📖 Section Introduction
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Section-Introduction/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/Section-Introduction/page)

# Section Introduction

> This lesson explores techniques for system hardening to secure operating systems and limit access through practical labs and configuration changes.

Hello and welcome to this comprehensive lesson on system hardening.

My name is Vijin Palazhi, and I'll be your guide as we explore various techniques for securing your systems. This lesson is designed for anyone looking to reduce the host operating system footprint and limit node access, ensuring your deployment remains as secure as possible.

<Callout icon="lightbulb" color="#1CB2FE">
  In this lesson, we will cover practical hardening techniques that include not only configuration changes but also hands-on labs to reinforce learning.
</Callout>

## Topics Covered

* **SSH Hardening:** Learn how to disable root user access and configure passwordless SSH to bolster your system's security.
* **Privilege Escalation:** Understand how privilege escalation works in Linux and discover effective mitigation strategies.
* **Removal of Obsolete Packages:** Identify and remove outdated packages and services to minimize potential vulnerabilities.
* **Kernel Module Restrictions:** Learn methods to restrict kernel modules, thereby reducing the attack surface.
* **Network Port Management:** Identify and disable unused open ports in Linux to prevent unauthorized access.
* **Cloud Role Minimization:** Understand the importance of minimizing roles and access in cloud environments to maintain secure operations.
* **Firewall Configuration:** Gain insights into effective firewall setup and management.
* **Seccomp for System Calls:** Explore how to restrict system calls using Seccomp.
* **Security Tools:** Get acquainted with security tools like AppArmor that can enhance your system protection.

<Callout icon="lightbulb" color="#1CB2FE">
  Whether you're a beginner or an experienced professional in software development, operations, or IT, this section will equip you with essential security fundamentals and practical skills.
</Callout>

## Prerequisites

Before diving into the hands-on labs, we'll cover the prerequisite concepts to ensure that you have a solid understanding of basic security practices. These fundamentals are vital not only for certification and Kubernetes environments but also for securing any IT infrastructure.

This lesson is packed with numerous practical labs designed to reinforce your learning through direct application of the concepts covered. Prepare to engage with interactive exercises that will help you master each technique effectively.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/d67be5ee-871d-4435-a187-382610cb6a1f/lesson/1a1a9f9b-4811-4169-9fd9-75fb4f9659e7" />
</CardGroup>

---


# 📂 Section: System Hardening
## 📖 UFW Firewall Basics
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/UFW-Firewall-Basics/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/System-Hardening/UFW-Firewall-Basics/page)

# UFW Firewall Basics

> This article introduces UFW, a user-friendly firewall interface for managing Linux firewall rules on an Ubuntu server.

In this lesson, we introduce UFW (Uncomplicated Firewall), a user-friendly interface designed to simplify managing Linux firewall rules. We'll walk through configuring UFW on an Ubuntu server (app01) to restrict network access and secure your environment.

Imagine a setup where access to app01 must be limited. In this scenario, only the jump server with IP address 172.16.238.5 is allowed to establish SSH connections. This jump server is the primary access point for system administrators. Additionally, app01 hosts a web server on port 80, which needs to be accessible not only from the jump server but also from internal clients within the IP range 172.16.100.0/28.

<Frame>
  ![The image illustrates a network setup with an Admin Jump Server and Internal Users accessing an application server (app01) via SSH, HTTP, and TCP protocols.](https://kodekloud.com/kk-media/image/upload/v1752871753/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-UFW-Firewall-Basics/frame_40.jpg)
</Frame>

All other ports on app01 must remain closed to inbound traffic. To achieve this, we leverage Netfilter, the Linux kernel's internal packet filtering system. Although IPTables is a common command-line tool for managing firewall rules, its complexity often demands a simpler solution. UFW serves as an intuitive front-end for configuring IPTables.

<Frame>
  ![The image shows a comparison between "iptables" and "ufw (Uncomplicated Firewall)" under the title "Install UFW."](https://kodekloud.com/kk-media/image/upload/v1752871754/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-UFW-Firewall-Basics/frame_80.jpg)
</Frame>

## Inspecting Active Ports

Before configuring UFW, log in via SSH to app01 and inspect the active listening ports using the netstat utility. Run the following command to confirm that SSH (port 22) and HTTP (port 80) are active, along with port 8080 which should be blocked from inbound connections:

```bash theme={null}
netstat -an | grep -w LISTEN
```

Expected output:

```plaintext theme={null}
tcp        0      0 0.0.0.0:22          0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:80           0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:8080         0.0.0.0:*               LISTEN
```

## Installing UFW

To install UFW on app01, start by updating your package list and then installing UFW:

```bash theme={null}
apt-get update
# ... additional update output ...
apt-get install ufw
```

After installation, check the current status of UFW:

```bash theme={null}
ufw status
```

The expected output should state:

```plaintext theme={null}
Status: inactive
```

## Configuring Default Firewall Rules

Since no firewall rules are active yet, begin by setting default policies. We want to permit all outbound traffic while denying inbound connections. Execute these commands as the root user:

```bash theme={null}
ufw default allow outgoing
```

The system will confirm:

```plaintext theme={null}
Default outgoing policy changed to 'allow'
(be sure to update your rules accordingly)
```

Next, set the default rule to deny all inbound connections:

```bash theme={null}
ufw default deny incoming
```

## Defining Specific Allow Rules

Now that the default policies are in place, add rules to allow specific traffic:

1. Allow SSH connections on port 22 only from the jump server with IP address 172.16.238.5:

   ```bash theme={null}
   ufw allow from 172.16.238.5 to any port 22 proto tcp
   ```

2. Allow HTTP connections on port 80 from the jump server:

   ```bash theme={null}
   ufw allow from 172.16.238.5 to any port 80 proto tcp
   ```

3. Allow HTTP access on port 80 from the internal network (IP range 172.16.100.0/28):

   ```bash theme={null}
   ufw allow from 172.16.100.0/28 to any port 80 proto tcp
   ```

Since port 8080 is actively listening but must be blocked, add an explicit deny rule:

```bash theme={null}
ufw deny 8080
```

<Callout icon="lightbulb" color="#1CB2FE">
  Although the default policy already denies incoming connections, explicitly denying port 8080 clarifies its intended blocked status.
</Callout>

## Enabling UFW

Before enabling UFW, verify that all necessary rules are correctly set to avoid unintended disconnections. Once reviewed, enable UFW with:

```bash theme={null}
ufw enable
```

The system warns that enabling UFW may disrupt existing SSH connections. Confirm by entering “y” when prompted:

```plaintext theme={null}
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
```

After UFW is enabled, check its status:

```bash theme={null}
ufw status
```

Expected output:

```plaintext theme={null}
Status: active
To                         Action      From
--                         -----       ----
22/tcp                     ALLOW       172.16.238.5
80/tcp                     ALLOW       172.16.238.5
80/tcp                     ALLOW       172.16.100.0/28
8080                       DENY        Anywhere
8080 (v6)                  DENY        Anywhere (v6)
```

## Deleting Firewall Rules

To remove a specific rule, such as the deny rule for port 8080, use the following command:

```bash theme={null}
ufw delete deny 8080
```

The system confirms the deletion:

```plaintext theme={null}
Rule deleted
Rule deleted (v6)
```

Alternatively, you can delete rules based on their line numbers listed in the firewall status. For example, if the deny rule for port 8080 is listed as rule number 5 and then as rule number 4, delete them one by one:

```bash theme={null}
ufw delete 5
# Confirm deletion when prompted, then:
ufw delete 4
```

After removing rules, recheck the status:

```bash theme={null}
ufw status
```

The updated rules should appear as follows:

```plaintext theme={null}
Status: active
To                         Action      From
--                         -----       ----
22/tcp                     ALLOW       172.16.238.5
80/tcp                     ALLOW       172.16.238.5
80/tcp                     ALLOW       172.16.100.0/28
8080                       DENY        Anywhere
```

## Summary

This lesson provided a comprehensive guide to configuring UFW on an Ubuntu server to secure SSH and HTTP traffic while blocking unauthorized connections. By setting default policies and specifying clear allow/deny rules, you can effectively manage your server's firewall and maintain a secure environment.

Practice these UFW commands to solidify your understanding and ensure your server remains protected against unwanted network traffic.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/d67be5ee-871d-4435-a187-382610cb6a1f/lesson/330f6887-f23b-41f4-8a6d-3db2f2fee5fd" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/d67be5ee-871d-4435-a187-382610cb6a1f/lesson/22eb9c61-27bc-4c84-a5fd-5672cac031de" />
</CardGroup>

---


