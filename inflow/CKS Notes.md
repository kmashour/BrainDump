  
Report an Issue

KM

## **Understanding Pod Security Policy**

PodSecurityPolicy serves as an admission controller within Kubernetes, enabling cluster administrators to effectively manage security-related aspects of the Pod specification. By creating PodSecurityPolicy resources and defining requirements for Pods, administrators can control which Pods are allowed to run based on security policies. If a Pod complies with the defined PSP requirements, it is admitted to the cluster; otherwise, it is rejected.

## **The Need for Pod Security Policy:**

Kubernetes resources like Deployments, StatefulSets, and Services form the foundation of applications. However, RBAC alone, which controls access to these resources, does not consider the specific settings within the resources. PodSecurityPolicy was introduced to address this gap and provide fine-grained control over security-related fields in Pods. It enabled administrators to prevent privileges and settings that could pose security risks, without relying on external admission controllers.

Over time, it became evident that PodSecurityPolicy had inherent usability challenges that necessitated breaking changes.

PSP faces two major drawbacks: the absence of support for additional resource types and its limited set of controls that overlooks certain container runtime-specific characteristics. Other than that, several complexities are attached to PSPs.

1. Confusing Application of PSPs: Users often found it challenging to correctly apply PodSecurityPolicy to Pods, leading to unintended and broader permissions.
2. Limited Visibility: It was difficult to determine which PodSecurityPolicy applied to a specific Pod, making it hard to track and understand the security policies in place.
3. Limited Support for Changing Pod Defaults: Modifying default values for Pod settings through PodSecurityPolicy had limited scope, causing inconsistencies and unpredictability.
4. Lack of Audit Mode or Dry Run Capability: The absence of an audit mode or dry run capability made it impractical to assess the impact of PSPs before enforcing them or retrofitting them to existing clusters safely.
5. Challenges in Enabling PSP by Default: The complexities and potential risks associated with PodSecurityPolicy made it infeasible to enable it by default across clusters, limiting its widespread adoption.

These usability challenges collectively drove the need for breaking changes and a more user-friendly solution to secure Pod deployments, leading to the deprecation of PodSecurityPolicy in Kubernetes.

For further insights into these and other challenges related to PSP (Pod Security Policies), we recommend watching the SIG Auth’s Maintainer Track session video from KubeCon NA 2019. This video provides valuable information on PSP difficulties.

[SIG Auth Update and Deep Dive – Mo Khan, Red Hat; Mike Danese, Google; & Tim Allclair, Google](https://youtu.be/SFtHRmPuhEw)

As you all know, In Kubernetes 1.21, PodSecurityPolicy (PSP) is being deprecated and removed from Kubernetes 1.25, paving the way for a replacement that offers improved functionality and sustainability.

## **Transitioning to a New Pod Security Solution**

With the phasing out and discontinuation of actively developed Pod Security Policies (PSPs), it becomes crucial for cluster administrators and operators to find alternative security measures. Fortunately, there are two promising options available to meet this need:

1. Policy-as-code (PAC) solutions within the Kubernetes ecosystem.
2. The Kubernetes Pod Security Standards (PSS) with Pod Security Admission (PSA)

In the Kubernetes community, several open source PAC solutions have emerged, providing a reliable alternative to PSPs. These solutions, although not officially part of the Kubernetes project, can be obtained from the Kubernetes ecosystem. Some notable examples of PAC solutions include:

- Kyverno
- OPA/Gatekeeper
- Open Policy Agent (OPA)
- jsPolicy

Here comes the lesson topic,

**Pod Security Admission (PSA) and Kubernetes Pod Security Standards (PSS).**

The Pod Security Standards (PSS) and Pod Security Admission (PSA) were introduced by the Kubernetes Auth Special Interest Group (SIG) in response to the deprecation of the Pod Security Policy (PSP) and the ongoing requirement of managing pod security in Kubernetes. PSA is an integrated solution within Kubernetes that offers built-in capabilities for governing pod security. The solution incorporates a webhook project designed for admission controllers, which ensures enforcement of the controls outlined in the Pod Security Standards (PSS). This admission controller approach bears similarity to the functioning of PAC (Policy as Code) systems.

**Bit about Pod Security Standards(PSS)**

PSS defines three different security policies that cover a wide range of security needs. These policies are cumulative and vary in their level of restrictiveness:

1. Privileged: This policy grants the highest level of access without any restrictions. It is useful for system-wide programs like logging agents, CNIs, and storage drivers that require privileged access.
2. Baseline: This policy aims to be highly restrictive to prevent known privilege escalation while still allowing the use of the default Pod configuration with minimal alterations. The baseline policy imposes restrictions on specific capabilities, including hostNetwork, hostPID, hostIPC, hostPath, hostPort, and the addition of Linux capabilities.
3. Restricted: This strict policy follows current best practices for hardening Pods. It builds upon the baseline policy and adds additional constraints, such as prohibiting the Pod from running as the root user or in the root group. Restricted policies may affect the functionality of applications and are designed for running security-critical applications.

Read more about PSS in the official Kubernetes documentation: [https://kubernetes.io/docs/concepts/security/pod-security-standards/](https://kubernetes.io/docs/concepts/security/pod-security-standards/)

These policies define different execution profiles for Pods, categorized into privileged and limited access tiers.

**Pod Security Admission(PSA) operates in three modes to enforce the controls defined by PSS:**

**Enforce**: When this mode is enabled, the PSA evaluates the Pod against the policy. If the Pod fails to meet the policy requirements, it is rejected.

**Audit**: In this mode, the Pod is allowed to run even if it violates the policy. However, the violation is recorded in the Kubernetes audit log.

**Warn**: This mode generates a warning for any policy violation but does not prevent the Pod from running.

### **Let’s Understand Namespace Labels in PSA**

Namespace labels play a crucial role in implementing PSA. They determine the policy level that applies to all Pods within a specific namespace. Here’s how they work:

First, Label Key: The key used for labeling namespaces is pod-security.kubernetes.io/enforce, pod-security.kubernetes.io/audit, and pod-security.kubernetes.io/warn.

Then, Label Value: The value of these labels indicates the policy level to be enforced, audited, or warned. These levels are typically privileged, baseline, or restricted, aligning with the Pod Security Standards.

### **Let’s take a look at an example scenario**

_In Enforce Mode:_

The Namespace Label looks like this.. pod-security.kubernetes.io/**enforce: restricted**

The Effect will be that any Pod that doesn’t meet the ‘restricted’ PSS in this namespace will be rejected.

_In the Audit Mode,_

The Namespace Label looks like this.

pod-security.kubernetes.io/**audit: baseline**

The Effect of this label will be that violations and violations of the ‘baseline’ PSS are logged in the audit log, but Pods are allowed to run.

Finally, the Warn Mode.

The Namespace Label is like this.

pod-security.kubernetes.io/**warn: privileged**

The Effect is that warnings and warnings are generated for any Pod that doesn’t meet the ‘privileged’ standard, but no enforcement occurs.

### **Let’s get an idea about the practical considerations of these.**

If no labels are present on a namespace, a default policy (usually the least restrictive) is applied.

Also, A namespace can have labels for all three modes, each specifying a different policy level.

Finally, Be cautious with changing labels, as escalating policy levels can lead to existing Pods being out of compliance.

More about configuring the built-in admission controller can be found here.

[https://kubernetes.io/docs/tasks/configure-pod-container/enforce-standards-admission-controller/#configure-the-admission-controller](https://kubernetes.io/docs/tasks/configure-pod-container/enforce-standards-admission-controller/#configure-the-admission-controller)

Imagine you’re setting up security in a Kubernetes cluster, using Pod Security Admission (PSA) to enforce certain rules. But, like in any good security system, you realize there are some special cases, some exceptions to the rule. That’s where PSA exemptions come in.

Think of PSA as a strict security guard, but one who knows that sometimes, specific people or situations need a bit of flexibility. Here are the key types of exemptions:

First, Usernames: It’s like having a VIP list. If a request comes from certain users – think of them as trusted individuals in your Kubernetes world – PSA steps aside and lets them through without the usual checks. These could be system administrators or automated processes that you know are safe.

Second, RuntimeClassNames: This is for those special types of Pods that need to run in a unique way, maybe for performance or compatibility reasons. When they have a particular runtime class name, they’re like guests with a special pass, exempt from the usual security checks.

Finally, the Namespaces: Sometimes, you have entire sections of your Kubernetes cluster where the standard rules don’t apply. In these ‘exempt namespaces,’ Pods can operate with more freedom, outside the usual security boundaries.

Now, how do you set these exemptions up? When configuring your Kubernetes API server, you can directly program these special passes into the PSA admission controller. It’s like giving the security guard a list of exceptions right from the start.

But there’s another way too. In the world of Kubernetes, you also have something called a Validating Webhook. Here, you can define exemptions in a more flexible way, using a Kubernetes ConfigMap resource. Think of this like a digital file that contains all the special rules and exemptions. This file is then placed right inside the ‘pod-security-webhook’ container, like handing over a constantly updating list of exceptions to your security guard.

In both cases, whether it’s directly through the API server or via the Validating Webhook, you’re ensuring that your Kubernetes cluster remains secure while also being flexible enough to accommodate special cases and needs.

And that, in a nutshell, is how PSA uses exemptions to maintain a balance between strict security and necessary flexibility in a Kubernetes environment.

## **Migration Strategies: From PSP to PSA**

let’s talk about moving from PodSecurityPolicy to Pod Security Admission in Kubernetes. It’s a bit like updating your software – you want to make sure everything runs smoothly without disrupting your work.

First things first, understand what you currently have. It’s like taking inventory. Look over your existing PSPs and note down what security policies you’ve got in place. This is your starting point.

Next up, get to know PSA. It’s important to understand how it works. PSA has three levels – Privileged, Baseline, and Restricted. Think about which level fits best with your current PSPs. It’s like choosing the right tool for the job.

Time for a test run with PSA in Audit Mode. Here, you’re just observing, not making any changes. Turn on PSA and see how your policies would work in real-time. It’s a bit like a dress rehearsal.

Now, translate your old PSPs into PSA policies. You’re basically updating your security measures. Find the closest match in PSA for each PSP, or write a new policy if you need to.

Before you go all in, use PSA in Warn Mode. This way, you’ll get alerts for any issues, but it won’t stop anything from running. It’s like having a friendly reminder before you make a big change.

Keep an eye on things. Monitor your audit and warning logs. This helps you see if there are any issues you need to fix. Think of it as fine-tuning your setup.

Ready to enforce your new policies? Switch from audit to enforce mode in PSA. Now, your policies are not just for show; they’re actually in effect.

Take it slow. Don’t rush into enforcing everything at once. Start with one area at a time, like focusing on a specific part of your project. This way, you can manage the changes better.

Keep everyone in the loop. Make sure your team knows about the new policies and how they work. Good communication is key to a smooth transition.

And lastly, don’t forget your resources. The Kubernetes documentation, blog posts, and GitHub repository are great places to look for more detailed information. They’re like your go-to guides.

By following these steps, you can switch from PSP to PSA with as little disruption as possible, keeping your Kubernetes environment secure and up-to-date.

## **Let’s see Pod Security Standards in Action.**

Here are practical examples of how different Pod Security Standards can be applied to a hypothetical pod spec:

First, the Privileged Level is appropriate for workloads that require all capabilities and access to the host.

```
apiVersion: v1
kind: Pod
metadata:
  name: privileged-pod
spec:
  containers:
  – name: privileged-container
    image: nginx
    securityContext:
      privileged: true
```

Second, the Baseline Level, which is the default for most clusters, disallows privilege escalation.

```
apiVersion: v1
kind: Pod
metadata:
  name: baseline-pod
spec:
  containers:
  – name: baseline-container
    image: nginx
    securityContext:
      allowPrivilegeEscalation: false
```

Finally, Restricted Level for workloads that require the highest level of security.

```
apiVersion: v1
kind: Pod
metadata:
  name: restricted-pod
spec:
  securityContext:
    seccompProfile:
      type: RuntimeDefault
  containers:
  – name: restricted-container
    image: nginx
    securityContext:
      allowPrivilegeEscalation: false
      runAsNonRoot: true
      readOnlyRootFilesystem: true
```

In a real-world world scenario,

A container that needs to manage the host’s network stack might require privileged access.

An API server that needs limited security permissions without escalation privileges would fit into baseline policies.

A payment processing app that handles sensitive data would benefit from the restricted level to minimize the attack surface.

Always refer to the latest Kubernetes documentation when implementing these examples, as details may have changed since my last update.

---

## 🌐 Scraped Reference Content

> [!NOTE]
> The content below has been automatically scraped from official documentation and related sub-links for deeper context.

### 📄 Source: [https://kubernetes.io/docs/concepts/security/pod-security-standards/](https://kubernetes.io/docs/concepts/security/pod-security-standards/)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - 日本語 (Japanese)   - 한국어 (Korean)   - বাংলা (Bengali)   - Français (French)   - Deutsch (German)   - हिन्दी (Hindi)   - Bahasa Indonesia (Indonesian)   - Italiano (Italian)   - فارسی (Persian)   - Polski (Polish)   - Português (Portuguese)   - Русский (Russian)   - Español (Spanish)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
#### 

# Pod Security Standards 
- - - - - - - - - - - - - - - - 
- 
  - 
    -   - 
    -     - 
      -       - 
        - 
          -           -           -           -           -           -           -           -           -       -     - 
      -       -       -       -       -   - 
    - 
      -       - 
        -         -         -         -         -         -         -         -         -         -       -       -     - 
      -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -     - 
      - 
        -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -         -         -         -       - 
        -         -         -         -         -         -         -         -       - 
        -       - 
        -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       - 
        -         -         -         -         -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -     - 
      - 
        -         -       - 
        -         -       -   - 
    - 
      -       -       -     - 
      - 
        -         -         -         -         -         -         -         -       -       - 
        -         -         -         -         -       -       - 
        -         -         -         -         -         -       - 
        -         -         -         -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       - 
        -         -         -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       - 
        -         -         -         -         -         -         -       - 
        -         -         -         -         -         -         -         -         -         -     - 
      -       -       -       -       -       -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -     - 
      -       - 
        -         -       -       -       -       -       -     - 
      -       -       -       -     - 
      -       -       -       -     - 
      -       -       -       -     -     -     -   - 
    -     - 
      - 
        -       - 
        -       - 
        -       - 
        -       - 
        -       - 
        -     - 
      -       -       -       -     - 
      -       -       -       -     - 
      -       -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     -     - 
      -     - 
      -       - 
        -         -         -         -         -         -       - 
        -       - 
        -       - 
        -       - 
        -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -       - 
        -         -       - 
        -       - 
        -       - 
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -         -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -     - 
      -       -       -       -       -       -       -     - 
      -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -     - 
      - 
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -     - 
      -       -       - 
        -         -         -         -         - 
          -           -           -         -         - 
          -           -           -         -         - 
          -           -         - 
          -         -         - 
          -           -           -           -           -           -           -           -           -           -           -           -           -           -           -         -         -         - 
          -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -         -         -         -         -         -         -         -         -         -         -         -         - 
          -           -         -         -         -         -         -         - 
          -         -         -         -         - 
          -           -           -           -           -           -         -         -         - 
          -           -           -           -           -           -         -         - 
          -           -         -         -         -       -       -       -       -       -       -     - 
      -     - 
      -       -       -       -       -       -       -     - 
      -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -     - 
      -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -     -     -   - 
- 
  -   -   - - 
  - - 
  - - - 
  -   -   - 
- - - - 
# Pod Security Standards A detailed look at the different policy levels defined in the Pod Security Standards. 
The Pod Security Standards define three different policies to broadly cover the security spectrum. These policies are cumulative and range from highly-permissive to highly-restrictive. This guide outlines the requirements of each policy. 
|  Profile  | Description  |
|  Privileged  | Unrestricted policy, providing the widest possible level of permissions. This policy allows for known privilege escalations.  |
|  Baseline  | Minimally restrictive policy which prevents known privilege escalations. Allows the default (minimally specified) Pod configuration.  |
|  Restricted  | Heavily restricted policy, following current Pod hardening best practices.  |
## Profile Details 
### Privileged 
The Privileged policy is purposely-open, and entirely unrestricted. This type of policy is typically aimed at system- and infrastructure-level workloads managed by privileged, trusted users. 
The Privileged policy is defined by an absence of restrictions. If you define a Pod where the Privileged security policy applies, the Pod you define is able to bypass typical container isolation mechanisms. For example, you can define a Pod that has access to the node's host network. 
### Baseline 
The Baseline policy is aimed at ease of adoption for common containerized workloads while preventing known privilege escalations. This policy is targeted at application operators and developers of non-critical applications. The following listed controls should be enforced/disallowed: 
#### Note: In this table, wildcards ( *) indicate all elements in a list. For example, spec.containers[*].securityContextrefers to the Security Context object for all defined containers . If any of the listed containers fails to meet the requirements, the entire pod will fail validation. Baseline policy specification 
|  Control  | Policy  |
|  HostProcess  | 
Windows Pods offer the ability to run HostProcess containers which enables privileged access to the Windows host machine. Privileged access to the host is disallowed in the Baseline policy. Feature state: Stable since Kubernetes v1.26 
Restricted Fields 
- spec.securityContext.windowsOptions.hostProcess- spec.containers[*].securityContext.windowsOptions.hostProcess- spec.initContainers[*].securityContext.windowsOptions.hostProcess- spec.ephemeralContainers[*].securityContext.windowsOptions.hostProcess
Allowed Values 
- Undefined/nil - false |
|  Host Namespaces  | 
Sharing the host namespaces must be disallowed. 
Restricted Fields 
- spec.hostNetwork- spec.hostPID- spec.hostIPC
Allowed Values 
- Undefined/nil - false |
|  Privileged Containers  | 
Privileged Pods disable most security mechanisms and must be disallowed. 
Restricted Fields 
- spec.containers[*].securityContext.privileged- spec.initContainers[*].securityContext.privileged- spec.ephemeralContainers[*].securityContext.privileged
Allowed Values 
- Undefined/nil - false |
|  Capabilities  | 
Adding additional capabilities beyond those listed below must be disallowed. 
Restricted Fields 
- spec.containers[*].securityContext.capabilities.add- spec.initContainers[*].securityContext.capabilities.add- spec.ephemeralContainers[*].securityContext.capabilities.add
Allowed Values 
- Undefined/nil - AUDIT_WRITE- CHOWN- DAC_OVERRIDE- FOWNER- FSETID- KILL- MKNOD- NET_BIND_SERVICE- SETFCAP- SETGID- SETPCAP- SETUID- SYS_CHROOT |
|  HostPath Volumes  | 
HostPath volumes must be forbidden. 
Restricted Fields 
- spec.volumes[*].hostPath
Allowed Values 
- Undefined/nil  |
|  Host Ports  | 
HostPorts should be disallowed entirely (recommended) or restricted to a known list 
Restricted Fields 
- spec.containers[*].ports[*].hostPort- spec.initContainers[*].ports[*].hostPort- spec.ephemeralContainers[*].ports[*].hostPort
Allowed Values 
- Undefined/nil - Known list (not supported by the built-in Pod Security Admission controller ) - 0 |
|  Host Probes / Lifecycle Hooks (v1.34+)  | 
The Host field in probes and lifecycle hooks must be disallowed. 
Restricted Fields 
- spec.containers[*].livenessProbe.httpGet.host- spec.containers[*].readinessProbe.httpGet.host- spec.containers[*].startupProbe.httpGet.host- spec.containers[*].livenessProbe.tcpSocket.host- spec.containers[*].readinessProbe.tcpSocket.host- spec.containers[*].startupProbe.tcpSocket.host- spec.containers[*].lifecycle.postStart.tcpSocket.host- spec.containers[*].lifecycle.preStop.tcpSocket.host- spec.containers[*].lifecycle.postStart.httpGet.host- spec.containers[*].lifecycle.preStop.httpGet.host- spec.initContainers[*].livenessProbe.httpGet.host- spec.initContainers[*].readinessProbe.httpGet.host- spec.initContainers[*].startupProbe.httpGet.host- spec.initContainers[*].livenessProbe.tcpSocket.host- spec.initContainers[*].readinessProbe.tcpSocket.host- spec.initContainers[*].startupProbe.tcpSocket.host- spec.initContainers[*].lifecycle.postStart.tcpSocket.host- spec.initContainers[*].lifecycle.preStop.tcpSocket.host- spec.initContainers[*].lifecycle.postStart.httpGet.host- spec.initContainers[*].lifecycle.preStop.httpGet.host
Allowed Values 
- Undefined/nil - ""  |
|  AppArmor  | 
On supported hosts, the RuntimeDefaultAppArmor profile is applied by default. The baseline policy should prevent overriding or disabling the default AppArmor profile, or restrict overrides to an allowed set of profiles. 
Restricted Fields 
- spec.securityContext.appArmorProfile.type- spec.containers[*].securityContext.appArmorProfile.type- spec.initContainers[*].securityContext.appArmorProfile.type- spec.ephemeralContainers[*].securityContext.appArmorProfile.type
Allowed Values 
- Undefined/nil - RuntimeDefault- Localhost
- metadata.annotations["container.apparmor.security.beta.kubernetes.io/*"]
Allowed Values 
- Undefined/nil - runtime/default- localhost/* |
|  SELinux  | 
Setting the SELinux type is restricted, and setting a custom SELinux user or role option is forbidden. 
Restricted Fields 
- spec.securityContext.seLinuxOptions.type- spec.containers[*].securityContext.seLinuxOptions.type- spec.initContainers[*].securityContext.seLinuxOptions.type- spec.ephemeralContainers[*].securityContext.seLinuxOptions.type
Allowed Values 
- Undefined/"" - container_t- container_init_t- container_kvm_t- container_engine_t(since Kubernetes 1.31) 
Restricted Fields 
- spec.securityContext.seLinuxOptions.user- spec.containers[*].securityContext.seLinuxOptions.user- spec.initContainers[*].securityContext.seLinuxOptions.user- spec.ephemeralContainers[*].securityContext.seLinuxOptions.user- spec.securityContext.seLinuxOptions.role- spec.containers[*].securityContext.seLinuxOptions.role- spec.initContainers[*].securityContext.seLinuxOptions.role- spec.ephemeralContainers[*].securityContext.seLinuxOptions.role
Allowed Values 
- Undefined/""  |
|  /procMount Type  | 
The default /procmasks are set up to reduce attack surface, and should be required. 
Restricted Fields 
- spec.containers[*].securityContext.procMount- spec.initContainers[*].securityContext.procMount- spec.ephemeralContainers[*].securityContext.procMount
Allowed Values 
- Undefined/nil - Default |
|  Seccomp  | 
Seccomp profile must not be explicitly set to Unconfined. 
Restricted Fields 
- spec.securityContext.seccompProfile.type- spec.containers[*].securityContext.seccompProfile.type- spec.initContainers[*].securityContext.seccompProfile.type- spec.ephemeralContainers[*].securityContext.seccompProfile.type
Allowed Values 
- Undefined/nil - RuntimeDefault- Localhost |
|  Sysctls  | 
Sysctls can disable security mechanisms or affect all containers on a host, and should be disallowed except for an allowed "safe" subset. A sysctl is considered safe if it is namespaced in the container or the Pod, and it is isolated from other Pods or processes on the same Node. 
Restricted Fields 
- spec.securityContext.sysctls[*].name
Allowed Values 
- Undefined/nil - kernel.shm_rmid_forced- net.ipv4.ip_local_port_range- net.ipv4.ip_unprivileged_port_start- net.ipv4.tcp_syncookies- net.ipv4.ping_group_range- net.ipv4.ip_local_reserved_ports(since Kubernetes 1.27) - net.ipv4.tcp_keepalive_time(since Kubernetes 1.29) - net.ipv4.tcp_fin_timeout(since Kubernetes 1.29) - net.ipv4.tcp_keepalive_intvl(since Kubernetes 1.29) - net.ipv4.tcp_keepalive_probes(since Kubernetes 1.29)  |
### Restricted 
The Restricted policy is aimed at enforcing current Pod hardening best practices, at the expense of some compatibility. It is targeted at operators and developers of security-critical applications, as well as lower-trust users. The following listed controls should be enforced/disallowed: 
#### Note: In this table, wildcards ( *) indicate all elements in a list. For example, spec.containers[*].securityContextrefers to the Security Context object for all defined containers . If any of the listed containers fails to meet the requirements, the entire pod will fail validation. Restricted policy specification 
|  Control  | Policy  |
|  Everything from the Baseline policy  |
|  Volume Types  | 
The Restricted policy only permits the following volume types. 
Restricted Fields 
- spec.volumes[*]
Allowed Values Every item in the spec.volumes[*]list must set one of the following fields to a non-null value: 
- spec.volumes[*].configMap- spec.volumes[*].csi- spec.volumes[*].downwardAPI- spec.volumes[*].emptyDir- spec.volumes[*].ephemeral- spec.volumes[*].persistentVolumeClaim- spec.volumes[*].projected- spec.volumes[*].secret |
|  Privilege Escalation (v1.8+)  | 
Privilege escalation (such as via set-user-ID or set-group-ID file mode) should not be allowed. This is Linux only policy in v1.25+ (spec.os.name != windows)
Restricted Fields 
- spec.containers[*].securityContext.allowPrivilegeEscalation- spec.initContainers[*].securityContext.allowPrivilegeEscalation- spec.ephemeralContainers[*].securityContext.allowPrivilegeEscalation
Allowed Values 
- false |
|  Running as Non-root  | 
Containers must be required to run as non-root users. 
Restricted Fields 
- spec.securityContext.runAsNonRoot- spec.containers[*].securityContext.runAsNonRoot- spec.initContainers[*].securityContext.runAsNonRoot- spec.ephemeralContainers[*].securityContext.runAsNonRoot
Allowed Values 
- trueThe container fields may be undefined/ nilif the pod-level spec.securityContext.runAsNonRootis set to true.  |
|  Running as Non-root user (v1.23+)  | 
Containers must not set runAsUser to 0 
Restricted Fields 
- spec.securityContext.runAsUser- spec.containers[*].securityContext.runAsUser- spec.initContainers[*].securityContext.runAsUser- spec.ephemeralContainers[*].securityContext.runAsUser
Allowed Values 
- any non-zero value - undefined/null |
|  Seccomp (v1.19+)  | 
Seccomp profile must be explicitly set to one of the allowed values. Both the Unconfinedprofile and the absence of a profile are prohibited. This is Linux only policy in v1.25+ (spec.os.name != windows)
Restricted Fields 
- spec.securityContext.seccompProfile.type- spec.containers[*].securityContext.seccompProfile.type- spec.initContainers[*].securityContext.seccompProfile.type- spec.ephemeralContainers[*].securityContext.seccompProfile.type
Allowed Values 
- RuntimeDefault- LocalhostThe container fields may be undefined/ nilif the pod-level spec.securityContext.seccompProfile.typefield is set appropriately. Conversely, the pod-level field may be undefined/ nilif _all_ container- level fields are set.  |
|  Capabilities (v1.22+)  | 
Containers must drop ALLcapabilities, and are only permitted to add back the NET_BIND_SERVICEcapability. This is Linux only policy in v1.25+ (.spec.os.name != "windows")
Restricted Fields 
- spec.containers[*].securityContext.capabilities.drop- spec.initContainers[*].securityContext.capabilities.drop- spec.ephemeralContainers[*].securityContext.capabilities.drop
Allowed Values 
- Any list of capabilities that includes ALL
Restricted Fields 
- spec.containers[*].securityContext.capabilities.add- spec.initContainers[*].securityContext.capabilities.add- spec.ephemeralContainers[*].securityContext.capabilities.add
Allowed Values 
- Undefined/nil - NET_BIND_SERVICE |
## Policy Instantiation 
Decoupling policy definition from policy instantiation allows for a common understanding and consistent language of policies across clusters, independent of the underlying enforcement mechanism. 
As mechanisms mature, they will be defined below on a per-policy basis. The methods of enforcement of individual policies are not defined here. 
Pod Security Admission Controller 
- Privileged namespace - Baseline namespace - Restricted namespace 
### Alternatives Note: This section links to third party projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for these projects, which are listed alphabetically. To add a project to this list, read the content guide before submitting a change. More information. 
Other alternatives for enforcing policies are being developed in the Kubernetes ecosystem, such as: 
- Kubewarden - Kyverno - OPA Gatekeeper 
## Pod OS field 
Kubernetes lets you use nodes that run either Linux or Windows. You can mix both kinds of node in one cluster. Windows in Kubernetes has some limitations and differentiators from Linux-based workloads. Specifically, many of the Pod securityContextfields have no effect on Windows . 
#### Note: Kubelets prior to v1.24 don't enforce the pod OS field, and if a cluster has nodes on versions earlier than v1.24 the Restricted policies should be pinned to a version prior to v1.25. 
### Restricted Pod Security Standard changes 
Another important change, made in Kubernetes v1.25 is that the Restricted policy has been updated to use the pod.spec.os.namefield. Based on the OS name, certain policies that are specific to a particular OS can be relaxed for the other OS. 
#### OS-specific policy controls 
Restrictions on the following controls are only required if .spec.os.nameis not windows: 
- Privilege Escalation - Seccomp - Linux Capabilities 
## User namespaces 
User Namespaces are a Linux-only feature to run workloads with increased isolation. How they work together with Pod Security Standards is described in the documentation for Pods that use user namespaces. 
## FAQ 
### Why isn't there a profile between Privileged and Baseline? 
The three profiles defined here have a clear linear progression from most secure (Restricted) to least secure (Privileged), and cover a broad set of workloads. Privileges required above the Baseline policy are typically very application specific, so we do not offer a standard profile in this niche. This is not to say that the privileged profile should always be used in this case, but that policies in this space need to be defined on a case-by-case basis. 
SIG Auth may reconsider this position in the future, should a clear need for other profiles arise. 
### What's the difference between a security profile and a security context? 
Security Contexts configure Pods and Containers at runtime. Security contexts are defined as part of the Pod and container specifications in the Pod manifest, and represent parameters to the container runtime. 
Security profiles are control plane mechanisms to enforce specific settings in the Security Context, as well as other related parameters outside the Security Context. As of July 2021, Pod Security Policies are deprecated in favor of the built-in Pod Security Admission Controller . 
### What about sandboxed Pods? 
There is currently no API standard that controls whether a Pod is considered sandboxed or not. Sandbox Pods may be identified by the use of a sandboxed runtime (such as gVisor or Kata Containers), but there is no standard definition of what a sandboxed runtime is. 
The protections necessary for sandboxed workloads can differ from others. For example, the need to restrict privileged permissions is lessened when the workload is isolated from the underlying kernel. This allows for workloads requiring heightened permissions to still be isolated. 
Additionally, the protection of sandboxed workloads is highly dependent on the method of sandboxing. As such, no single recommended profile is recommended for all sandboxed workloads. 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified August 02, 2026 at 11:18 PM PST: docs: fix broken Kyverno link in Pod Security Standards (2c1aa11ce2) 
Items on this page refer to third party products or projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for those third-party products or projects. See the CNCF website guidelines for more details. 
You should read the content guide before proposing a change that adds an extra third-party link. 
- - - - - - 

- - - - 

### 📄 Source: [https://kubernetes.io/docs/tasks/configure-pod-container/enforce-standards-admission-controller/#configure-the-admission-controller](https://kubernetes.io/docs/tasks/configure-pod-container/enforce-standards-admission-controller/#configure-the-admission-controller)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - Português (Portuguese)   - বাংলা (Bengali)   - Français (French)   - Deutsch (German)   - हिन्दी (Hindi)   - Bahasa Indonesia (Indonesian)   - Italiano (Italian)   - 日本語 (Japanese)   - 한국어 (Korean)   - فارسی (Persian)   - Polski (Polish)   - Русский (Russian)   - Español (Spanish)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
#### 

# Enforce Pod Security Standards by Configuring the Built-in Admission Controller 
- - - - - - - - - - - - - - - - 
- 
  - 
    -   - 
    -     - 
      -       - 
        - 
          -           -           -           -           -           -           -           -           -       -     - 
      -       -       -       -       -   - 
    - 
      -       - 
        -         -         -         -         -         -         -         -         -         -       -       -     - 
      -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -     - 
      - 
        -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -         -         -         -       - 
        -         -         -         -         -         -         -         -       - 
        -       - 
        -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       - 
        -         -         -         -         -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -     - 
      - 
        -         -       - 
        -         -       -   - 
    - 
      -       -       -     - 
      - 
        -         -         -         -         -         -         -         -       -       - 
        -         -         -         -         -       -       - 
        -         -         -         -         -         -       - 
        -         -         -         -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       - 
        -         -         -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       - 
        -         -         -         -         -         -         -       - 
        -         -         -         -         -         -         -         -         -         -     - 
      -       -       -       -       -       -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -     - 
      -       - 
        -         -       -       -       -       -       -     - 
      -       -       -       -     - 
      -       -       -       -     - 
      -       -       -       -     -     -     -   - 
    -     - 
      - 
        -       - 
        -       - 
        -       - 
        -       - 
        -       - 
        -     - 
      -       -       -       -     - 
      -       -       -       -     - 
      -       -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     -     - 
      -     - 
      -       - 
        -         -         -         -         -         -       - 
        -       - 
        -       - 
        -       - 
        -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -       - 
        -         -       - 
        -       - 
        -       - 
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -         -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -     - 
      -       -       -       -       -       -       -     - 
      -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -     - 
      - 
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -     - 
      -       -       - 
        -         -         -         -         - 
          -           -           -         -         - 
          -           -           -         -         - 
          -           -         - 
          -         -         - 
          -           -           -           -           -           -           -           -           -           -           -           -           -           -           -         -         -         - 
          -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -         -         -         -         -         -         -         -         -         -         -         -         - 
          -           -         -         -         -         -         -         - 
          -         -         -         -         - 
          -           -           -           -           -           -         -         -         - 
          -           -           -           -           -           -         -         - 
          -           -         -         -         -       -       -       -       -       -       -     - 
      -     - 
      -       -       -       -       -       -       -     - 
      -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -     - 
      -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -     -     -   - 
- - 
- - - - 
# Enforce Pod Security Standards by Configuring the Built-in Admission Controller 
Kubernetes provides a built-in admission controller to enforce the Pod Security Standards . You can configure this admission controller to set cluster-wide defaults and exemptions . 
## Before you begin 
Following an alpha release in Kubernetes v1.22, Pod Security Admission became available by default in Kubernetes v1.23, as a beta. From version 1.25 onwards, Pod Security Admission is generally available. 
To check the version, enter kubectl version. 
If you are not running Kubernetes 1.37, you can switch to viewing this page in the documentation for the Kubernetes version that you are running. 
## Configure the Admission Controller 
#### Note: pod-security.admission.config.k8s.io/v1configuration requires v1.25+. For v1.23 and v1.24, use v1beta1 . For v1.22, use v1alpha1 . 
```
apiVersion:apiserver.config.k8s.io/v1kind:AdmissionConfigurationplugins:- name:PodSecurityconfiguration:apiVersion:pod-security.admission.config.k8s.io/v1# see compatibility notekind:PodSecurityConfiguration# Defaults applied when a mode label is not set.## Level label values must be one of:# - "privileged" (default)# - "baseline"# - "restricted"## Version label values must be one of:# - "latest" (default) # - specific version like "v1.37"defaults:enforce:"privileged"enforce-version:"latest"audit:"privileged"audit-version:"latest"warn:"privileged"warn-version:"latest"exemptions:# Array of authenticated usernames to exempt.usernames:[]# Array of runtime class names to exempt.runtimeClasses:[]# Array of namespaces to exempt.namespaces:[]
```

#### Note: The above manifest needs to be specified via the --admission-control-config-fileto kube-apiserver. 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified October 17, 2023 at 2:00 PM PST: Update enforce-standards-admission-controller.md (2d8edf7829) 
- - - - - - 

- - - - 
