# 📂 Section: Monitoring Logging and Runtime Security
## 📖 Ensure Immutability of Containers at Runtime
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Monitoring-Logging-and-Runtime-Security/Ensure-Immutability-of-Containers-at-Runtime/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Monitoring-Logging-and-Runtime-Security/Ensure-Immutability-of-Containers-at-Runtime/page)

# Ensure Immutability of Containers at Runtime

> This article explores methods to ensure Kubernetes pods maintain immutability, preventing unauthorized modifications during runtime.

In this article, we explore various methods to ensure that Kubernetes pods adhere to the concept of immutability. Although containers are designed to be immutable by default, it is still possible to perform in-place updates. For instance, one can copy files directly into a pod or obtain a shell within the container to make changes. Here, we discuss how to prevent unauthorized modifications during runtime.

## Enforcing a Read-Only File System

One effective method to maintain container immutability is by ensuring that the pod’s file system remains read-only after startup. This can be implemented through the security context in the pod definition.

Consider the following configuration for an Nginx pod:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  labels:
    run: nginx
  name: nginx
spec:
  containers:
  - image: nginx
    name: nginx
    securityContext:
      readOnlyRootFilesystem: true
```

Using the `readOnlyRootFilesystem: true` field in the security context ensures that the Nginx container starts with a read-only root file system, preventing any unauthorized copying or writing. However, this configuration might disrupt application functionality. For example, deploying the pod as configured above could result in an error because Nginx typically requires write permissions for certain directories.

If you create the pod with this configuration, you may see the following output:

```bash theme={null}
kubectl create -f nginx.yaml
pod/nginx created

kubectl get pods
NAME    READY   STATUS    RESTARTS   AGE
nginx   0/1     Error     0          20s
```

Nginx requires write access to directories such as `/var/run` (to store runtime data) and `/var/cache/nginx` (for caching). The pod logs will indicate failures when it attempts to write to these directories.

!!! note "Important"
Before enforcing a read-only file system, ensure your applications do not depend on writing to the root file system during runtime.

## Using Volumes to Allow Limited Write Access

To resolve these issues, mount volumes on the directories that require write access. In the example below, we use an `emptyDir` volume since the data does not need to persist after the pod terminates. The updated configuration is as follows:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  labels:
    run: nginx
  name: nginx
spec:
  containers:
  - image: nginx
    name: nginx
    securityContext:
      readOnlyRootFilesystem: true
    volumeMounts:
    - name: cache-volume
      mountPath: /var/cache/nginx
    - name: runtime-volume
      mountPath: /var/run
  volumes:
  - name: cache-volume
    emptyDir: {}
  - name: runtime-volume
    emptyDir: {}
```

After applying this configuration, the `/var/cache/nginx` and `/var/run` directories inside the container become writable through the mounted volumes, while the rest of the file system remains read-only. Once recreated, the pod should initialize successfully.

## Testing the Immutable Container with Privileged Mode

In some cases, you might want to observe the behavior of an immutable container even when it's running in privileged mode. Although using the privileged flag is generally discouraged, this example demonstrates that the read-only root file system still prevents modifications, even for a privileged container.

Create a pod with the configuration below:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  labels:
    run: nginx
  name: nginx
spec:
  containers:
  - image: nginx
    name: nginx
    securityContext:
      readOnlyRootFilesystem: true
      privileged: true
    volumeMounts:
    - name: cache-volume
      mountPath: /var/cache/nginx
    - name: runtime-volume
      mountPath: /var/run
  volumes:
  - name: cache-volume
    emptyDir: {}
  - name: runtime-volume
    emptyDir: {}
```

On deployment, you might observe messages similar to:

```bash theme={null}
kubectl create -f nginx.yaml
pod/nginx created

kubectl get pods
NAME    READY   STATUS    RESTARTS   AGE
nginx   1/1     Running   0          20s
```

Attempting a package update inside the container will still fail due to the read-only root file system:

```bash theme={null}
kubectl exec -ti nginx -- apt update
Reading package lists... Done
E: List directory /var/lib/apt/lists/partial is missing. - Acquire (30: Read-only file system)
command terminated with exit code 100
```

Despite the container being privileged, the read-only setting prevents modifications necessary for updating packages. Moreover, note that changes within the `/proc` pseudo file system, such as modifying the swappiness value, can impact the host machine. This example reinforces the importance of avoiding the privileged flag to maintain container immutability.

!!! warning "Security Warning"
Avoid using the privileged flag unless absolutely necessary. Privileged containers can perform actions that inadvertently affect the host system and compromise security.

## Best Practices for Container Immutability

To ensure that your containers remain immutable, follow these best practices:

| Best Practice              | Description                                                                                           |
| -------------------------- | ----------------------------------------------------------------------------------------------------- |
| Read-Only Root File System | Set containers with a read-only root file system to prevent in-place modifications.                   |
| Limited Write Volumes      | Mount volumes (e.g., `emptyDir` or persistent volumes) only on directories that require write access. |
| Avoid Privileged Mode      | Refrain from using the privileged flag to limit the container’s impact on the host system.            |
| Non-Root Containers        | Run containers as non-root users whenever possible to minimize risks.                                 |
| Enforce Security Policies  | Use Pod Security Policies (PSPs) to enforce immutability and other security best practices.           |

Below is an example of a Pod Security Policy that reinforces these practices:

```yaml theme={null}
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: example
spec:
  privileged: false
  readOnlyRootFilesystem: true
  runAsUser:
    rule: RunAsNonRoot
  seLinux:
    rule: RunAsAny
  supplementalGroups:
    rule: RunAsAny
  fsGroup:
    rule: RunAsAny
```

This policy ensures that containers are non-privileged, have a read-only root file system, run as non-root users, and do not carry unnecessary privileges.

## Conclusion

Ensuring the immutability of containers at runtime is critical for maintaining the integrity and security of your applications in Kubernetes. By enforcing a read-only file system, using limited write-access volumes, and avoiding the privileged flag, you can create a robust and secure environment for your containers. Apply these best practices along with Pod Security Policies to maximize your container’s security.

Now, put these concepts into practice with hands-on exercises to reinforce your understanding and secure your containers effectively.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/c0d849e1-54be-4d78-8936-6ce49434b88d/lesson/e69c4be9-7505-4b77-a0dd-6a8bfccbb79b" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/c0d849e1-54be-4d78-8936-6ce49434b88d/lesson/71a86fa2-0c82-4bd5-a5f1-bba594c39290" />
</CardGroup>

---


# 📂 Section: Monitoring Logging and Runtime Security
## 📖 Falco Configuration Files
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Monitoring-Logging-and-Runtime-Security/Falco-Configuration-Files/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Monitoring-Logging-and-Runtime-Security/Falco-Configuration-Files/page)

# Falco Configuration Files

> This article explores Falco's configuration files, detailing how to update and add custom rules and how Falco processes these configurations at startup.

In this article, we explore the configuration files used by Falco. You will learn how to update existing rules, add custom rules, and gain insight into how Falco processes these configurations at startup.

Previously, we covered writing basic Falco rules. Now, we will focus on where these rules are stored and how Falco loads them during initialization.

## Main Configuration File

Falco’s primary configuration file is a YAML file located at:

/etc/falco/falco.yaml

During the startup process, Falco reads this file and applies its settings. You can verify which configuration file is in use by checking the Falco service unit file (look for the "-c" flag) or by reviewing the logs with the journalctl command.

Below is an excerpt from the Falco logs confirming the configuration file in use:

```console theme={null}
-- Logs begin at Tue 2021-04-13 21:45:35 UTC, end at Tue 2021-04-13 21:51:31 UTC. --
Apr 13 21:45:36 node01 systemd[1]: Starting Falco: Container Native Runtime Security...
Apr 13 21:45:36 node01 systemd[1]: Started Falco: Container Native Runtime Security.
Apr 13 21:45:36 node01 falco[9817]: Falco version 0.28.0 (driver version 5c0b863ddade7a45568c0ac97d037422c9efb750)
Apr 13 21:45:36 node01 falco[9817]: Tue Apr 13 21:45:36 2021: Falco version 0.28.0 (driver version 5c0b863ddade7a45568c0ac97d037422c9efb750)
Apr 13 21:45:36 node01 falco[9817]: Falco initialized with configuration file /etc/falco/falco.yaml
Apr 13 21:45:36 node01 falco[9817]: Tue Apr 13 21:45:36 2021: Falco initialized with configuration file /etc/falco/falco.yaml
```

Within this configuration file, you will find settings that specify:

* The locations of rule files.
* Formatting options for logs and output messages.
* Configurable output channels, among other parameters.

## Loading Rule Files

Falco leverages the "rules\_file" field in the configuration file to load all necessary rules. This field accepts a list of files that contain rule definitions. By default, the built-in rules are stored in `/etc/falco/falco_rules.yaml` and are always the first file in the list.

The order of files is crucial: if a rule appears in more than one file, the definition from the later file in the list will take precedence.

For example:

```yaml theme={null}
rules_file:
  - /etc/falco/falco_rules.yaml
  - /etc/falco/falco_rules.local.yaml
  - /etc/falco/k8s_audit_rules.yaml
  - /etc/falco/rules.d/
```

<Callout icon="lightbulb" color="#1CB2FE">
  Custom rules or modifications should be added to `/etc/falco/falco_rules.local.yaml` to avoid being overwritten by package updates.
</Callout>

## Additional Configuration Options

Other significant options in the Falco configuration include the JSON output setting and logging configurations. By enabling JSON output, events are logged in JSON format rather than plain text. Additional settings control where logs are sent (e.g., standard error, syslog) and the log level for Falco's own messages.

Below is an example of a configuration file with additional options:

```yaml theme={null}
rules_file:
  - /etc/falco/falco_rules.yaml
  - /etc/falco/falco_rules.local.yaml
  - /etc/falco/k8s_audit_rules.yaml
  - /etc/falco/rules.d
json_output: false
log_stderr: true
log_syslog: true
log_level: info
```

## Defining Output Channels

By default, Falco logs its events to standard output, but you can configure various output channels to suit your needs. For instance, you can enable file logging, program output to external tools (such as sending alerts via a Slack webhook), or even HTTP output to a specified endpoint.

The following example demonstrates how to configure different output channels:

```yaml theme={null}
stdout_output:
  enabled: true

file_output:
  enabled: true
  filename: /opt/falco/events.txt

program_output:
  enabled: true
  program: "jq '{text: .output}' | curl -d @- -X POST https://hooks.slack.com/services/XXXX"

http_output:
  enabled: true
  url: http://some.url/some/path/
```

After making changes to the configuration file, ensure you reload Falco’s configuration and restart the engine for the updates to take effect.

## Falco Rules Files

The file `/etc/falco/falco_rules.yaml` houses Falco's built-in rules, lists, and macros. An example of a built-in rule that detects when a terminal shell is started within a container is shown below:

```yaml theme={null}
- rule: Terminal shell in container
  desc: A shell was used as the entrypoint/exec point into a container with an attached terminal.
  condition: >
    spawned_process and container
    and shell_procs and proc.tty != 0
    and container_entrypoint
    and not user_expected_terminal_shell_in_container_conditions
  output: >
    A shell was spawned in a container with an attached terminal (user=%user.name user_loginuid=%user.loginuid %container.info
    shell=%proc.name parent=%proc.pname cmdline=%proc.cmdline terminal=%proc.tty container_id=%container.id image=%container.image.repository)
  priority: NOTICE
```

<Callout icon="triangle-alert" color="#FF6B6B">
  Direct modifications to `/etc/falco/falco_rules.yaml` may be lost during package updates. Always add custom changes to `/etc/falco/falco_rules.local.yaml`.
</Callout>

For example, to adjust the rule's priority from NOTICE to WARNING and to introduce a custom rule that triggers a critical alert for abnormal file reads, you can define the rules as follows:

```yaml theme={null}
- rule: Terminal shell in container
  desc: A shell was used as the entrypoint/exec point into a container with an attached terminal.
  condition: >
    spawned_process and container
    and shell_procs and proc.tty != 0
    and container_entrypoint
    and not user_expected_terminal_shell_in_container_conditions
  output: >
    A shell was spawned in a container with an attached terminal (user=%user.name user_loginuid=%user.loginuid %container.info
    shell=%proc.name parent=%proc.pname cmdline=%proc.cmdline terminal=%proc.tty container_id=%container.id image=%container.image.repository)
  priority: WARNING

- rule: Anomalous read in kodekloud/webapp pod
  desc: Detect suspicious file reads in a custom webapp container.
  condition: >
    open_read and container
    and container.image.repository == "kodekloud/simple-webapp"
    and fd.directory != "/opt/app"
  output: >
    A file was opened and read outside the /opt/app directory (user=%user.name user_loginuid=%user.loginuid
    container_id=%container.id image=%container.image.repository)
  priority: CRITICAL
```

After updating your rules, remember to reload the Falco configuration and restart the engine for the changes to be applied.

## Hot Reloading the Falco Configuration

To apply configuration changes without restarting the entire Falco service, you can use hot reloading. When running via systemd, Falco’s process ID (PID) is stored in `/var/run/falco.pid`. You can reload the configuration by sending a SIGHUP (signal hangup) to the Falco process. For example:

```bash theme={null}
cat /var/run/falco.pid
7183
kill -1 $(cat /var/run/falco.pid)
```

This command instructs Falco to reload its configuration and restart the engine without a full service restart, ensuring your custom rules and settings are immediately active.

***

That concludes our in-depth guide on Falco configuration files. Now, put your newfound knowledge into practice by applying these concepts in your environment.

For more information on Falco and container security, be sure to check out the [Falco Documentation](https://falco.org/docs/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/c0d849e1-54be-4d78-8936-6ce49434b88d/lesson/5e5fd05e-4725-4988-817c-6f8036b2f7e5" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/c0d849e1-54be-4d78-8936-6ce49434b88d/lesson/a17a72ac-3fa6-420f-b58d-3740a1ffe114" />
</CardGroup>

---


# 📂 Section: Monitoring Logging and Runtime Security
## 📖 Falco Overview and Installation
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Monitoring-Logging-and-Runtime-Security/Falco-Overview-and-Installation/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Monitoring-Logging-and-Runtime-Security/Falco-Overview-and-Installation/page)

# Falco Overview and Installation

> This guide covers installing Falco on Kubernetes to detect and analyze potential threats through system call monitoring.

In this guide, we will walk through installing Falco on a Kubernetes cluster and show you how to use it to detect and analyze potential threats.

Falco works by monitoring system calls from user-space applications into the Linux kernel. It captures these calls and processes them with its policy engine, which uses predefined rules to identify suspicious activities. When an anomaly is detected, Falco can alert administrators via syslog, standard output, Slack, email notifications, and other channels.

## How Falco Operates

Falco has two methods to interact with the Linux kernel:

1. **Kernel Module Method**\
   Falco can insert a kernel module, adding extra code to the Linux kernel. Although this approach is effective, it is considered intrusive. Some managed Kubernetes service providers restrict the use of kernel modules due to security policies.

2. **eBPF (Extended Berkeley Packet Filter) Method**\
   Alternatively, Falco leverages eBPF to interact with the kernel in a less invasive way. This method is generally preferred by many providers for its lower impact on system integrity.

Once system calls are captured by either method, they are passed through user-space syscall libraries and then filtered by Falco's policy engine. This engine evaluates the data using Falco rules and generates alerts if any suspicious events occur.

<Frame>
  ![The image illustrates Falco's architecture, showing components like applications, syscalls, kernel modules, eBPF, policy engine, libraries, and Falco rules, leading to output generation.](https://kodekloud.com/kk-media/image/upload/v1752871681/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Falco-Overview-and-Installation/frame_90.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Installing Falco directly on a node as a service ensures that even in the event of a compromise, Falco remains isolated from the Kubernetes environment and continues to effectively detect suspicious behavior.
</Callout>

## Installing Falco on a Node

Since Falco interacts directly with the kernel, installing it as a standard software package involves also installing the corresponding kernel module. Follow these steps to install Falco on a node:

1. Import the Falco public key and add the repository:

   ```bash theme={null}
   curl -s https://falco.org/repo/falcosecurity-3672BA8F.asc | apt-key add -
   echo "deb https://download.falco.org/packages/deb stable main" | tee -a /etc/apt/sources.list.d/falcosecurity.list
   ```
2. Update the package list, install the appropriate kernel headers and Falco, then start the service:

   ```bash theme={null}
   apt update -y
   apt-get install -y linux-headers-$(uname -r)
   apt install -y falco
   systemctl start falco
   ```

## Deploying Falco as a DaemonSet

If installing Falco directly on the node is not feasible, you can deploy it as a DaemonSet across all cluster nodes. The easiest way to achieve this is by using Helm charts. For detailed deployment instructions, please refer to the detailed steps provided in the [reference section](#links-and-references) below.

## Verifying the Installation

After installing Falco, verify that the Falco pods are running on all nodes by executing:

```bash theme={null}
kubectl get pods

NAME          READY   STATUS    RESTARTS   AGE
falco-7grdt   1/1     Running   0          2m21s
falco-tmq28   1/1     Running   0          2m21s
```

If the pods are running, your Falco installation is successfully monitoring your Kubernetes environment for any anomalous behavior.

<Callout icon="lightbulb" color="#1CB2FE">
  With Falco up and running, you are well-equipped to utilize its robust rules engine to detect potential threats and secure your Kubernetes cluster.
</Callout>

## Links and References

* [Falco Official Documentation](https://falco.org/docs/)
* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Helm Charts Repository](https://artifacthub.io/)

By following these steps, you will ensure a secure and efficient Falco deployment that continuously monitors your Kubernetes environment for any suspicious activity. Happy monitoring!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/c0d849e1-54be-4d78-8936-6ce49434b88d/lesson/33a62604-1e7b-4e9a-950e-5e7a0302b141" />
</CardGroup>

---


# 📂 Section: Monitoring Logging and Runtime Security
## 📖 Mutable vs Immutable Infrastructure
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Monitoring-Logging-and-Runtime-Security/Mutable-vs-Immutable-Infrastructure/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Monitoring-Logging-and-Runtime-Security/Mutable-vs-Immutable-Infrastructure/page)

# Mutable vs Immutable Infrastructure

> This article explores the differences between mutable and immutable infrastructure, highlighting their implications for system design, updates, and security.

In this lesson, we explore the fundamental differences between mutable and immutable infrastructure through a clear, real-world example. Understanding these concepts is essential for designing robust, scalable, and secure systems.

## Mutable Infrastructure

Mutable infrastructure involves updating existing servers or resources directly when changes occur. Consider a simple scenario where a web server is running Nginx version 1.17 on a host. When a new version of Nginx is released, the server software gets upgraded—first from 1.17 to 1.18 and then to 1.19. This process can be executed manually by downloading the required version or automatically using ad-hoc scripts and configuration management tools such as the [Ansible Advanced Course](https://learn.kodekloud.com/user/courses/ansible-advanced-course).

In a larger environment with a pool of three web servers running identical software, the same upgrade process must be applied to every server:

<Frame>
  ![The image shows a server icon with "v1.19" above it, and "Scripts" and "Ansible" logos on the right side.](https://kodekloud.com/kk-media/image/upload/v1752871682/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Mutable-vs-Immutable-Infrastructure/frame_50.jpg)
</Frame>

This method of updating software on servers without replacing the infrastructure is known as in-place updating, and it is a classic example of mutable infrastructure.

<Callout icon="lightbulb" color="#1CB2FE">
  Keep in mind that in mutable environments, even though the underlying hardware remains the same, the software and configurations are subject to change.
</Callout>

### Risks of Mutable Infrastructure

In real-world scenarios, updating servers can introduce challenges. For example, if web servers 1 and 2 have the necessary dependencies to upgrade from Nginx 1.17 to 1.19, the upgrade will complete successfully. However, if web server 3 is missing some required dependencies—whether due to network issues, insufficient disk space, or operating system discrepancies—the upgrade might fail, leaving it at version 1.18. This results in a pool of servers running different software versions, a phenomenon known as configuration drift.

<Frame>
  ![The image illustrates "Configuration Drift" with three servers, two running version 1.19 and one running version 1.18, highlighting version inconsistencies.](https://kodekloud.com/kk-media/image/upload/v1752871683/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Mutable-vs-Immutable-Infrastructure/frame_170.jpg)
</Frame>

Configuration drift complicates planning for future updates and troubleshooting because each server might behave differently.

## Immutable Infrastructure

Immutable infrastructure offers a contrasting approach. Instead of altering the software on existing servers, new servers are provisioned with the updated version—say, Nginx 1.19 replacing Nginx 1.17—while the old servers are decommissioned. In this model, once a server is deployed, it is never modified during its lifetime; any change requires provisioning a new server with the updated software.

<Frame>
  ![The image illustrates "Immutable Infrastructure" with three identical server icons labeled "v1.18."](https://kodekloud.com/kk-media/image/upload/v1752871684/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Mutable-vs-Immutable-Infrastructure/frame_220.jpg)
</Frame>

This approach minimizes configuration drift because every new server starts from a standardized, unchanged configuration. Immutable infrastructure is particularly effective in environments where consistency, security, and scalability are critical.

### Containers and Immutability

The immutable model applies seamlessly to containerized applications. Since containers are generated from images, any update—such as moving from Nginx 1.18 to 1.19—must be performed on the image first. The updated image is then deployed through a rolling update process, ensuring that no downtime occurs during the transition.

For example, to update Nginx in a Dockerfile from version 1.18 to 1.19, modify the base image as follows:

```dockerfile theme={null}
FROM nginx:1.19
COPY nginx.conf /etc/nginx
ENTRYPOINT ["sh", "entrypoint.sh"]
```

<Callout icon="triangle-alert" color="#FF6B6B">
  While it is technically feasible to modify a running container (for example, by copying files directly to the filesystem or by manually accessing the container with a shell), doing so increases the risk of security vulnerabilities. Prevent runtime modifications to minimize the likelihood of unauthorized access or malicious changes.
</Callout>

In summary, embracing immutable infrastructure—whether in traditional server environments or containerized platforms—streamlines updates, reduces configuration drift, and enhances overall system security. In the upcoming lesson, we will further explore strategies to prevent runtime modifications and secure your deployments effectively.

For additional reading, consider exploring:

* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Docker Hub](https://hub.docker.com/)
* [Terraform Registry](https://registry.terraform.io/)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/c0d849e1-54be-4d78-8936-6ce49434b88d/lesson/2028480e-7020-410f-bdef-c203b61a00ef" />
</CardGroup>

---


# 📂 Section: Monitoring Logging and Runtime Security
## 📖 Perform Behavioral Analytics of Syscall Process
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Monitoring-Logging-and-Runtime-Security/Perform-Behavioral-Analytics-of-Syscall-Process/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Monitoring-Logging-and-Runtime-Security/Perform-Behavioral-Analytics-of-Syscall-Process/page)

# Perform behavioral analytics of syscall process

> This article discusses monitoring Kubernetes clusters for abnormal behavior using behavioral analytics on syscalls to enhance security and mitigate potential cyber threats.

In this article, we dive into monitoring Kubernetes clusters for abnormal behavior, potential cyberattacks, and security breaches. By leveraging advanced behavioral analytics on syscalls, you can significantly improve your cluster’s security posture and minimize damage in the event of an intrusion.

Various strategies exist to secure Kubernetes infrastructures—including hardening control plane components, implementing sandboxing techniques to limit container permissions, using mTLS for secure communications, and restricting network access to nodes. However, even with all these security measures in place,

<Frame>
  ![The image lists security measures: Securing Cluster, Sandboxing Techniques, Restricting Network Access, Minimizing Microservices Vulnerability, and MTLS Encryption.](https://kodekloud.com/kk-media/image/upload/v1752871685/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Perform-behavioral-analytics-of-syscall-process/frame_30.jpg)
</Frame>

there is no absolute guarantee against emerging threats. An attacker might always discover a new vulnerability, making it critical to prepare for potential container compromises.

<Callout icon="lightbulb" color="#1CB2FE">
  Early detection of suspicious activity can significantly mitigate the impact of a breach. By rapidly identifying irregularities, you can quickly contain any threat and prevent further damage.
</Callout>

<Frame>
  ![The image depicts a network diagram with three "controlplane" nodes and two "worker" nodes, connected in sequence, with an arrow pointing to a worker node from a figure.](https://kodekloud.com/kk-media/image/upload/v1752871688/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Perform-behavioral-analytics-of-syscall-process/frame_60.jpg)
</Frame>

To understand this concept better, consider an analogy with credit and debit card security. Modern smart chips and ATM authentication mechanisms have drastically improved card security, yet a card can still be physically stolen. If an unauthorized user learns your PIN, they can withdraw funds—even using contactless methods.

Before the advent of smartphones, fraudulent transactions might have gone unnoticed for days or weeks until you reviewed your bank statement. Today, instant smartphone notifications alert you immediately, allowing you to quickly report and reverse the transactions. Additionally, setting transaction limits can further restrict potential losses.

<Frame>
  ![The image shows a credit card icon with three features: Instant Notifications, Revert Transactions, and Transaction Limits.](https://kodekloud.com/kk-media/image/upload/v1752871689/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Perform-behavioral-analytics-of-syscall-process/frame_150.jpg)
</Frame>

This analogy holds true for compromised computer systems as well. Swift detection in the event of a breach is critical to containing damage and reducing the overall blast radius. Quickly identifying abnormal activities allows for rapid replacement of compromised nodes or pods

<Frame>
  ![The image depicts a network diagram with control plane and worker nodes, highlighting a security breach on a worker node with a warning symbol and an intruder icon.](https://kodekloud.com/kk-media/image/upload/v1752871690/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Perform-behavioral-analytics-of-syscall-process/frame_170.jpg)
</Frame>

and patching any exploited vulnerabilities to prevent future attacks.

## How to Identify Breaches in a Kubernetes Cluster

One effective tool for securing your Kubernetes environment is [Falco](https://falco.org) from Sysdig. Previously, deep dives into syscalls were performed using tools such as [strace](https://strace.io) and [AquaSec Tracee](https://github.com/aquasecurity/tracee) to analyze application behaviors within pods.

When hundreds of applications run across numerous pods, they generate thousands of syscalls—making simple monitoring insufficient:

<Frame>
  ![The image illustrates Falco monitoring system calls from containers interacting with the Linux kernel and hardware, listing specific syscalls like close and nanosleep.](https://kodekloud.com/kk-media/image/upload/v1752871692/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Perform-behavioral-analytics-of-syscall-process/frame_210.jpg)
</Frame>

We need robust methods to analyze these syscalls and filter out suspicious events. For example, if an event involves accessing a container's bash shell or a program attempting to read the /etc/shadow file (which contains sensitive password data), it should be flagged for further investigation.

Consider this scenario: attackers often attempt to erase their trail from the system logs.

```bash theme={null}
kubectl exec -ti nginx-master -- bash
# cat /etc/shadow > /opt/logs/audit.log
```

<Callout icon="triangle-alert" color="#FF6B6B">
  Deleting parts of audit logs—an action that is not typical for a legitimate administrator—can be flagged as anomalous behavior. Monitoring these events provides an early warning sign of a potential intrusion.
</Callout>

Even when access seems legitimate, Falco can monitor and send alerts through multiple notification channels, ensuring you remain informed of any suspicious activity.

In upcoming sections, we will explore the process of installing Falco on your Kubernetes cluster and leveraging its capabilities to detect and analyze security threats in real-time.

For additional insights on Kubernetes security, consider exploring:

* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Docker Hub](https://hub.docker.com/)
* [Terraform Registry](https://registry.terraform.io/)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/c0d849e1-54be-4d78-8936-6ce49434b88d/lesson/13be41c6-4b0a-45b3-a9e5-0e7d96767ecc" />
</CardGroup>

---


# 📂 Section: Monitoring Logging and Runtime Security
## 📖 Section Introduction
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Monitoring-Logging-and-Runtime-Security/Section-Introduction/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Monitoring-Logging-and-Runtime-Security/Section-Introduction/page)

# Section Introduction

> This article explores monitoring, logging, and runtime security with a focus on behavior analytics for system calls and file activities to detect malicious activities.

In this article, we delve into the critical aspects of monitoring, logging, and runtime security, with a special focus on behavior analytics for system calls and file activities at both the host and container levels. Our approach is designed to detect malicious activities early and effectively, reinforcing your overall security posture.

We begin by exploring how tools such as Falco can help implement robust defense-in-depth strategies. These techniques ensure comprehensive threat detection by covering multiple components, including:

* Physical infrastructure
* Applications
* Networks
* Data
* Users
* Workloads

This expansive coverage guarantees that potential attacks are identified regardless of where they occur.

<Frame>
  ![The image lists course objectives for Kubernetes security, including attack surface understanding, cluster hardening, vulnerability minimization, supply chain security, monitoring, threat detection, and mock exams.](https://kodekloud.com/kk-media/image/upload/v1752871693/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Section-Introduction/frame_20.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  The integration of multiple security layers—ranging from host-level system call monitoring to container runtime security—enhances your ability to quickly identify and neutralize threats.
</Callout>

Furthermore, we investigate advanced techniques for in-depth analytical investigations to identify malicious actors within dynamic environments. We also present methods to ensure the immutability of containers during runtime, thereby reducing the risk of unauthorized modifications.

Finally, the article discusses the implementation of Kubernetes audit logs. These logs are vital for monitoring access and improving security oversight by providing a clear view of system events.

By the end of this article, you will understand how to effectively leverage these tools and strategies to secure your infrastructure against evolving threats.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/c0d849e1-54be-4d78-8936-6ce49434b88d/lesson/bf4c8718-d889-4787-85ff-b8593251209d" />
</CardGroup>

---


# 📂 Section: Monitoring Logging and Runtime Security
## 📖 Use Falco to Detect Threats
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Monitoring-Logging-and-Runtime-Security/Use-Falco-to-Detect-Threats/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Monitoring-Logging-and-Runtime-Security/Use-Falco-to-Detect-Threats/page)

# Use Falco to Detect Threats

> This article demonstrates using Falco to detect and alert on suspicious activity within a Kubernetes cluster.

In this lesson, we demonstrate how to use Falco—a powerful cloud-native runtime security tool—to detect and alert on suspicious activity within your Kubernetes cluster. We start by verifying that Falco is actively monitoring your nodes, then deploy an NGINX pod to generate events, and finally, customize Falco rules to enhance detection capabilities.

## Verifying Falco is Running

First, ensure that Falco has been installed on your host system as a package. You can verify its status by running:

```bash theme={null}
systemctl status falco
```

<Callout icon="lightbulb" color="#1CB2FE">
  Ensure that Falco is installed and properly configured on your nodes before proceeding.
</Callout>

## Creating an NGINX Pod

To generate events for Falco to monitor, deploy an NGINX pod with the following command:

```bash theme={null}
kubectl run nginx --image=nginx
```

Next, confirm that the pod is scheduled on a specific node (e.g., node 01) by listing all pods with detailed information:

```bash theme={null}
kubectl get pods -o wide
```

## Monitoring Falco Logs

Open a new terminal session and SSH into node 01. Begin streaming Falco logs in real time to monitor security events:

```bash theme={null}
journalctl -fu falco
```

You may notice numerous log entries; focus on the new events as they occur since older log messages can be ignored.

## Interacting with the NGINX Container

In your initial terminal session, access the NGINX container's shell by executing:

```bash theme={null}
kubectl exec -ti nginx -- bash
```

Shortly after opening the shell, you will receive an alert in the Falco logs indicating that a shell has been spawned inside the container. This log entry will include important details such as the container ID, image name, and namespace.

To illustrate Falco's capability in detecting sensitive file accesses, execute the following command inside the container to view the contents of the /etc/shadow file:

```bash theme={null}
cat /etc/shadow
```

As soon as you run this command, Falco generates another alert noting that a sensitive file was accessed.

## Understanding Falco Rules

Falco uses a set of rules defined in a YAML configuration file to determine which events should trigger alerts. Each rule comprises five mandatory keys:

* **rule:** A unique name for the rule.
* **desc:** A detailed description explaining the purpose of the rule.
* **condition:** A filtering expression applied to incoming events.
* **output:** The log message generated when the rule is triggered.
* **priority:** The severity level associated with the event.

Below is an example of a custom Falco rule designed to detect the opening of a shell within a container:

```yaml theme={null}
- rule: Detect Shell inside a container
  desc: Alert if a shell such as bash is open inside a container
  condition: container and proc.name in (linux_shells)
  output: Bash Opened (user=%user.name container=%container.id)
  priority: WARNING

- list: linux_shells
  items: [bash, zsh, ksh, sh, csh]

- macro: container
  condition: container.id != host
```

### Rule Breakdown

1. **Rule & Description:**\
   The rule "Detect Shell inside a container" is designed to trigger an alert when a shell (such as bash) is initiated within a container environment.

2. **Condition:**\
   The condition uses a macro named "container" to ensure the event originates from within a container and checks if the process name belongs to one of the pre-defined Linux shells (bash, zsh, ksh, sh, or csh).

3. **Output:**\
   The output message incorporates dynamic filters to include the username (`user=%user.name`) and container ID (`container=%container.id`) in the alert.

4. **Priority:**\
   The severity level for this alert is set to WARNING. Falco supports multiple priority levels ranging from debug (lowest) to emergency (highest).

5. **Lists and Macros:**
   * The "linux\_shells" list consolidates common shell names to simplify the condition.
   * The "container" macro verifies that the event originates from a container (i.e., `container.id != host`), improving the readability and maintainability of the rule.

For further details on syscall filters and additional macros, please visit the [Falco reference documentation](https://falco.org/docs/).

<Callout icon="triangle-alert" color="#FF6B6B">
  Always ensure that your security rules are tested in a non-production environment before applying them to production systems.
</Callout>

## Conclusion

This lesson covered the key steps to verify Falco's operation, interact with a running container, and implement a custom rule to detect when a shell is spawned inside a container. In the next installment, we will dive into configuring Falco’s settings and explore how to fine-tune custom rules for broader threat detection.

For more insights and in-depth tutorials on container security, continue exploring our documentation and related resources.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/c0d849e1-54be-4d78-8936-6ce49434b88d/lesson/b14718bb-dd48-495a-be04-05ed8d110ac7" />
</CardGroup>

---


