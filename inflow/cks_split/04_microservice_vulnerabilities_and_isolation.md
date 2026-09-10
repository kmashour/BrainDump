# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Additional Considerations API Priority Fairness
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Additional-Considerations-API-Priority-Fairness/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Additional-Considerations-API-Priority-Fairness/page)

# Additional Considerations API Priority Fairness

> This guide explores API priority and fairness, pod priority and preemption, and strategies for configuring DNS in multi-tenant Kubernetes environments.

In multi-tenant Kubernetes environments, managing workload priorities is critical for ensuring that both the control plane and node resources are allocated efficiently. In this guide, we explore key concepts such as API priority and fairness, pod priority and preemption, and strategies for configuring DNS in a multi-tenant setup.

## API Priority and Fairness

Kubernetes processes all resource management operations through its singular API endpoint. This makes the API a focal point for managing requests like creating namespaces, scaling applications, and updating deployments. In clusters supporting multiple tenants—with varying levels of application criticality—it is crucial to ensure that essential API requests receive higher priority.

Consider a scenario with two tenants sharing a cluster. Tenant A (in namespace A) runs critical services that require rapid scaling, while Tenant B (in namespace B) handles less critical workloads. To avoid delays in request handling for Tenant A due to Tenant B’s traffic, Kubernetes allows configuring API priority and fairness settings.

### Configuring API Priority

You first define priority level configurations using the beta API from `flowcontrol.apiserver.k8s.io/v1beta3`. In the configuration below, the "high-priority" level is allocated a higher assured concurrency than the "low-priority" level:

```yaml theme={null}
apiVersion: flowcontrol.apiserver.k8s.io/v1beta3
kind: PriorityLevelConfiguration
metadata:
  name: high-priority
spec:
  type: Limited
  limited:
    assuredConcurrencyShares: 10  # High priority gets more concurrency
    limitResponse:
      type: Queue
---
apiVersion: flowcontrol.apiserver.k8s.io/v1beta3
kind: PriorityLevelConfiguration
metadata:
  name: low-priority
spec:
  type: Limited
  limited:
    assuredConcurrencyShares: 1  # Low priority gets less concurrency
    limitResponse:
      type: Queue
```

Next, create FlowSchema objects that map these priority levels to specific tenant requests. The following example assigns higher precedence to namespace A (critical tenant) over namespace B:

```yaml theme={null}
apiVersion: flowcontrol.apiserver.k8s.io/v1beta3
kind: FlowSchema
metadata:
  name: high-priority-namespace-a
spec:
  priorityLevelConfiguration:
    name: high-priority  # Link to high priority
    matchingPrecedence: 1000
  rules:
    - subjects:
        - kind: ServiceAccount
          name: "system-account"  # Alternatively, match on user or service account
          namespace: "namespace-a"  # Target Namespace A
      resourceRules:
        - verbs: ["*"]
          apiGroups: ["*"]
          resources: ["*"]

---
apiVersion: flowcontrol.apiserver.k8s.io/v1beta3
kind: FlowSchema
metadata:
  name: low-priority-namespace-b
spec:
  priorityLevelConfiguration:
    name: low-priority  # Link to low priority
    matchingPrecedence: 2000
  rules:
    - subjects:
        - kind: Group
          name: "regular-users"
        - kind: ServiceAccount
          name: "default"
          namespace: "namespace-b"  # Target Namespace B
      resourceRules:
        - verbs: ["*"]
          apiGroups: ["*"]
          resources: ["*"]
```

<Callout icon="lightbulb" color="#1CB2FE">
  This configuration ensures that API requests from critical namespaces are prioritized, preserving the responsiveness of essential operations.
</Callout>

## Pod Priority and Preemption

Beyond API request handling, Kubernetes also supports pod priority and preemption to manage node resource allocation (including CPU, memory, etc.). This mechanism guarantees that critical pods gain necessary resources, even under resource pressure, by preempting or evicting less critical pods when needed.

<Frame>
  ![Diagram of a Kubernetes cluster with nodes A and B, showing namespaces for critical, regular, and development environments, illustrating pod priority and preemption.](https://kodekloud.com/kk-media/image/upload/v1752871628/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Additional-Considerations-API-Priority-Fairness/frame_200.jpg)
</Frame>

For example, if Tenant A (running critical workloads in namespace A) needs to ensure constant operation of production databases or core services, pod priority and preemption help maintain resource allocation, even if lower-priority Tenant B jobs are affected.

### Configuring Pod Priority

Begin by defining priority classes that distinguish between critical and non-critical workloads. In the configuration below, the "high-priority" class is assigned a higher value, ensuring its pods are scheduled preferentially:

```yaml theme={null}
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: high-priority
value: 1000  # High priority for critical workloads
globalDefault: false
description: "This priority class is for critical production workloads."
---
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: low-priority
value: 100  # Low priority for non-critical tasks
globalDefault: false
description: "This priority class is for non-critical development workloads."
```

Then, assign the appropriate priority class to your pod specifications. The following example shows how to define a critical application pod in namespace A:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: critical-app
  namespace: namespace-a
spec:
  priorityClassName: high-priority
  containers:
  - name: app-container
    image: nginx
    resources:
      requests:
        memory: "500Mi"
        cpu: "500m"
      limits:
        memory: "500Mi"
        cpu: "500m"
```

This assignment ensures that pods associated with critical workloads receive the necessary scheduling preference during peak load scenarios.

## Comparing API Priority and Pod Priority

Both API priority and pod priority serve crucial yet distinct roles within a Kubernetes cluster:

* **API Priority and Fairness:**\
  These settings control the flow and processing of Kubernetes API requests. They manage operations such as creating, updating, or fetching cluster resources and ensure that critical API interactions are not stalled by heavy traffic from lower priority sources.

* **Pod Priority and Preemption:**\
  These mechanisms focus on resource allocation at the node level. They prioritize scheduling for critical pods and allow the system to evict lower priority pods when essential resources are required.

Below is a comparative illustration clarifying the roles of API priority versus pod priority:

<Frame>
  ![The image compares API Priority and Fairness with Pod Priority and Preemption, detailing their scope, purpose, controls, and handling, concluding they cannot replace each other.](https://kodekloud.com/kk-media/image/upload/v1752871629/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Additional-Considerations-API-Priority-Fairness/frame_380.jpg)
</Frame>

<Callout icon="triangle-alert" color="#FF6B6B">
  Both mechanisms are integral for the stability and performance of multi-tenant clusters. It is important to carefully plan and test your configurations to ensure critical workloads receive the intended level of service.
</Callout>

By understanding and appropriately implementing API priority and pod priority configurations, you can effectively manage resource contention and maintain service quality across multi-tenant Kubernetes environments.

For more insights on Kubernetes configuration and best practices, refer to the [Kubernetes Documentation](https://kubernetes.io/docs/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/68165e01-d5f6-406f-adc5-681c83aeddc2" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Admission Controllers
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Admission-Controllers/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Admission-Controllers/page)

# Admission Controllers

> This article explores admission controllers in Kubernetes, which validate, mutate, or reject API requests before they are persisted.

In this article, we explore admission controllers in Kubernetes—powerful components that validate, mutate, or reject API requests before they are persisted. Typically, users interact with the Kubernetes cluster using the kubectl utility. When a command such as creating a pod is issued, the request reaches the API server and is ultimately saved in the etcd database.

## Request Lifecycle in Kubernetes

When a request is sent to the API server, it undergoes several critical steps:

1. **Authentication:**\
   The API server authenticates the request. For instance, when using kubectl, the KubeConfig file supplies the necessary certificates. You can view a snippet from the KubeConfig file using:

   ```bash theme={null}
   cat ~/.kube/config
   ```

   ```yaml theme={null}
   apiVersion: v1
   clusters:
   - cluster:
       certificate-authority-data: LS0tLS1CRUdJTiBDRVUx...
   ```

<Callout icon="lightbulb" color="#1CB2FE">
  Only a portion of the base64-encoded certificate data is shown for brevity.
</Callout>

2. **Authorization:**\
   After authentication, the request is authorized. Kubernetes uses role-based access control (RBAC) to determine if the user has permission to perform the requested operation. For example, a role allowing the manipulation of pods might be defined as:

   ```yaml theme={null}
   apiVersion: rbac.authorization.k8s.io/v1
   kind: Role
   metadata:
     name: developer
   rules:
   - apiGroups: [""]
     resources: ["pods"]
     verbs: ["list", "get", "create", "update", "delete"]
   ```

   More granular permissions can also be established. For instance, the following role permits a developer to create only specific pods:

   ```yaml theme={null}
   apiVersion: rbac.authorization.k8s.io/v1
   kind: Role
   metadata:
     name: developer
   rules:
   - apiGroups: [""]
     resources: ["pods"]
     verbs: ["create"]
     resourceNames: ["blue", "orange"]
   ```

   In this case, the developer is restricted to creating pods named either "blue" or "orange."

## The Role of Admission Controllers

Beyond basic authentication and authorization, there are scenarios that require additional validations or modifications to incoming requests. Consider a pod creation request, where you might want to:

* Ensure that images are only pulled from an approved internal registry.
* Enforce that the image tag is not set to "latest."
* Reject requests if the container runs as the root user.
* Modify the container’s security context or enforce specific metadata labels.

Take this pod manifest as an example:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: web-pod
spec:
  containers:
    - name: ubuntu
      image: ubuntu:latest
      command: ["sleep", "3600"]
      securityContext:
        runAsUser: 0
        capabilities:
          add: ["MAC_ADMIN"]
```

RBAC does not cover these complex validations or modifications. That is where admission controllers come into play; they provide an additional security layer by examining, modifying, or rejecting API requests before they reach etcd.

<Frame>
  ![The image illustrates the Kubernetes process flow: Kubectl command, authentication, authorization, admission controllers, and finally, pod creation.](https://kodekloud.com/kk-media/image/upload/v1752871631/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Admission-Controllers/frame_210.jpg)
</Frame>

### Built-In Admission Controllers

Kubernetes includes several pre-built admission controllers, such as:

* **Always Pull Images:** Ensures that images are pulled on each pod creation.
* **Default Storage Class:** Automatically assigns a default storage class to persistent volume claims if none is specified.
* **Event Rate Limit:** Restricts the number of requests processed by the API server concurrently.
* **Namespace Exists:** Verifies that the specified namespace exists, rejecting requests for non-existent namespaces.

## Namespace-Related Admission Controllers

### Namespace Exists Admission Controller

If you attempt to create a pod in a non-existent namespace, the namespace exists admission controller will reject the request. For example:

```bash theme={null}
kubectl run nginx --image nginx --namespace blue
```

The flow is as follows:

1. The API server authenticates and authorizes the request.
2. The namespace exists admission controller verifies if the "blue" namespace is available.
3. Since the namespace does not exist, the request is rejected.

### Namespace Auto-Provision Admission Controller

An alternate admission controller, the namespace auto-provision admission controller, can automatically create a namespace if it does not exist. Note that this controller is not enabled by default. Without auto-provisioning, running the command:

```bash theme={null}
kubectl run nginx --image nginx --namespace blue
```

results in:

```bash theme={null}
Error from server (NotFound): namespaces "blue" not found
```

To see which admission controllers are enabled by default, run:

```bash theme={null}
kube-apiserver -h | grep enable-admission-plugins
```

If your cluster uses a kubeadm-based setup, execute this command within the kube-apiserver control plane pod:

```bash theme={null}
kubectl exec kube-apiserver-controlplane -n kube-system -- kube-apiserver -h | grep enable-admission-plugins
```

<Callout icon="lightbulb" color="#1CB2FE">
  Using these commands helps ensure that you're aware of all the active admission controllers in your cluster.
</Callout>

## Configuring Admission Controllers

### Enabling Admission Controllers

To enable additional admission controllers, update the `--enable-admission-plugins` flag on the kube-apiserver. In a kubeadm-based setup, this update is performed in the kube-apiserver manifest file. For example, you might configure the API server service as follows:

```bash theme={null}
ExecStart=/usr/local/bin/kube-apiserver \\
  --advertise-address=${INTERNAL_IP} \\
  --allow-privileged=true \\
  --apiserver-count=3 \\
  --authorization-mode=Node,RBAC \\
  --bind-address=0.0.0.0 \\
  --enable-swagger-ui=true \\
  --etcd-servers=https://127.0.0.1:2379 \\
  --event-ttl=1h \\
  --runtime-config=api/all \\
  --service-cluster-ip-range=10.32.0.0/24 \\
  --service-node-port-range=30000-32767 \\
  --v=2 \\
  --enable-admission-plugins=NodeRestriction,NamespaceAutoProvision
```

When the API server runs as a pod in a kubeadm-based setup, the manifest might look like this:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  name: kube-apiserver
  namespace: kube-system
spec:
  containers:
    - name: kube-apiserver
      image: k8s.gcr.io/kube-apiserver-amd64:v1.11.3
      command:
        - kube-apiserver
        - --authorization-mode=Node,RBAC
        - --advertise-address=172.17.0.107
        - --allow-privileged=true
        - --enable-bootstrap-token-auth=true
        - --enable-admission-plugins=NodeRestriction,NamespaceAutoProvision
```

To disable specific admission controller plugins, leverage the `--disable-admission-plugins` flag in a similar way.

### Testing Auto-Provisioning

After enabling the desired admission controllers, a pod creation request in a non-existent namespace behaves differently. With the namespace auto-provision controller enabled, executing:

```bash theme={null}
kubectl run nginx --image nginx --namespace blue
```

will successfully create the pod. Upon listing namespaces with:

```bash theme={null}
kubectl get namespaces
```

you should observe that the "blue" namespace has been automatically created:

```plaintext theme={null}
NAME         STATUS   AGE
blue         Active   3m
default      Active   23m
kube-public  Active   24m
kube-system  Active   24m
```

## Deprecation Notice

Note that the namespace auto-provision and namespace existence admission controllers have been deprecated and replaced by the namespace lifecycle admission controller. The namespace lifecycle admission controller now ensures that requests targeting non-existent namespaces are rejected, while also safeguarding critical namespaces (such as default, kube-system, and kube-public) from deletion.

## Conclusion

Admission controllers represent an advanced layer of security within Kubernetes by allowing for complex validations and modifications to API requests. They operate seamlessly in the background, ensuring that your cluster adheres to stringent security and operational policies. Practice deploying and configuring these controllers to strengthen your understanding and enhance your Kubernetes security posture.

For further details, consider reviewing additional Kubernetes documentation on [Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) and [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/357adf04-1e02-4e8e-ac27-d1706d01e46d" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/07a89281-4a2c-4cf1-a6ce-db287457cf05" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Container Sandboxing
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Container-Sandboxing/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Container-Sandboxing/page)

# Container Sandboxing

> Hardening containers by applying sandboxing techniques such as namespaces, seccomp, AppArmor, capability drops, and microVM alternatives to reduce kernel attack surface and improve isolation.

In this lesson we examine how to harden containers by applying sandboxing techniques that reduce the kernel attack surface and limit what containerized processes can do. We contrast container isolation with virtual machines, show practical examples (including PID namespaces), and present common sandboxing controls and advanced alternatives that provide stronger isolation.

## Quick refresher: virtual machines vs containers

Virtual machines provide strong isolation because each VM runs a full guest operating system and its own kernel on top of a hypervisor. Containers, by contrast, share the host kernel and isolate processes using kernel mechanisms such as namespaces and cgroups. That architecture difference is critical when evaluating attack surfaces and escape risks.

<Frame>
  <img src="https://mintcdn.com/kodekloud-c4ac6d9a/1UnYm26nZTOghZP0/images/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Container-Sandboxing/container-sandboxing-vm-vs-containers.jpg?fit=max&auto=format&n=1UnYm26nZTOghZP0&q=85&s=e2d68d65cce0e09bc770570a2a77d65f" alt="A diagram titled &#x22;Container Sandboxing&#x22; comparing virtual machines and containers. It shows layered stacks (application, libs, deps, guest OS) with VMs using a hypervisor and separate guest OSes, while containers share Docker and the host OS over the hardware." width="1920" height="1080" data-path="images/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Container-Sandboxing/container-sandboxing-vm-vs-containers.jpg" />
</Frame>

| Isolation Aspect                  | Virtual Machines                | Containers                                |
| --------------------------------- | ------------------------------- | ----------------------------------------- |
| Kernel per workload               | Yes — dedicated guest kernel    | No — shared host kernel                   |
| Isolation mechanism               | Hypervisor-based                | Namespaces, cgroups, LSMs                 |
| Typical use case                  | Strong multi-tenant isolation   | Lightweight microservices, higher density |
| Escape risk if kernel compromised | Lower (guest kernel separation) | Higher (shared kernel)                    |

## PID namespaces: a simple example

Containers map process IDs into a PID namespace. Inside the container, a process can appear as PID 1, while on the host it has a different PID. This demonstrates logical process isolation but also shows that the host can still observe and terminate the underlying host PID.

Example (run a BusyBox container that sleeps for 1000 seconds):

```bash theme={null}
# Run a container that sleeps
$ docker run -d --name sleeping-container busybox sleep 1000
e2fd5090c9a51eb7cc91a466cf2e18c5468871f84adbb55c2e6c1cf4ea0028a8

# Inside the container: PID 1 is the sleep process
$ docker exec -ti sleeping-container ps -ef
PID   USER     TIME  COMMAND
1     root     0:00  sleep 1000
11    root     0:00  ps -ef

# On the host you can also see the sleep process with a different PID
$ ps -ef | grep sleep | grep -vi grep
root     7902  7871  0 21:39 ?        00:00:00 sleep 1000
```

Because the host-level process exists, killing that host PID terminates the container process. This shows that namespaces provide isolation at the user-space level, but the shared kernel remains the ultimate control plane.

<Callout icon="warning" color="#FF6B6B">
  Containers share the host kernel. If the kernel has a vulnerability (for example, a local privilege escalation like Dirty COW), a compromised container process can potentially exploit the kernel and affect the host and other containers.
</Callout>

## How containerized processes interact with the kernel

Applications (in containers or on bare OS) run in user space and make system calls to access hardware and privileged services. Since containers use the host kernel, restricting system call access and other kernel-visible actions is a key hardening strategy. Two widely used kernel-level sandboxing controls are seccomp and AppArmor (or SELinux).

* Seccomp: restricts the set of system calls a process may invoke.
* AppArmor: enforces path- and capability-based access controls for files and other resources.

Both tools reduce the risk of a kernel exploit being used from within a container by reducing what code inside the container can ask the kernel to do.

## Example sandboxing configurations

Example seccomp profile (whitelist-style — deny by default, allow a small syscall set):

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
        "brk",
        "access",
        "capset",
        "clone"
      ],
      "action": "SCMP_ACT_ALLOW"
    }
  ]
}
```

Example AppArmor profile snippet (blacklist-style rule denying writes to /proc):

```text theme={null}
profile apparmor-deny-write flags=(attach_disconnected) {
    #include <abstractions/base>

    # Allow typical reads and library access (adjust paths for your program)
    /usr/bin/your-binary ixr,
    /lib/** r,
    /usr/lib/** r,
    /etc/** r,

    # Deny all write access to /proc
    deny /proc/** w,
}
```

### Whitelist vs blacklist approaches

| Pattern                      | Description                                      | Strengths                               | Trade-offs                               |
| ---------------------------- | ------------------------------------------------ | --------------------------------------- | ---------------------------------------- |
| Whitelist (seccomp)          | Default deny; explicitly allow required syscalls | Minimal kernel surface, strong security | Requires profiling/application knowledge |
| Blacklist (AppArmor snippet) | Default allow; block specific actions or paths   | Easier to implement for diverse apps    | May miss attack vectors; less strict     |

<Callout icon="lightbulb" color="#1CB2FE">
  When feasible, prefer whitelist-based restrictions (e.g., seccomp profiles) to minimize the kernel functionality exposed to containerized applications. Use blacklists when you need broader compatibility and then complement them with other controls.
</Callout>

## Practical guidance for production workloads

* Small, homogeneous fleets: Create strict, minimal seccomp and AppArmor/SELinux profiles for each service (for example, many Nginx or MySQL instances). This gives strong protection with manageable maintenance.
* Large, heterogeneous fleets: Use a layered approach — namespaces + cgroups + capability drops + seccomp + LSMs (AppArmor/SELinux) — and focus on automation to generate and roll out profiles.
* Follow the principle of least privilege: drop Linux capabilities your process does not need and restrict filesystem and network access.
* Monitor and iterate: use runtime observability and profiling to generate accurate whitelists and to find false positives/negatives before enforcing strict policies.

## Advanced sandboxing / microVM alternatives

If the shared-kernel model is unacceptable for your threat model, consider technologies that provide stronger kernel isolation by running containers inside lightweight VMs or alternative kernels:

| Technology      | Description                                                             | Use case                                          |
| --------------- | ----------------------------------------------------------------------- | ------------------------------------------------- |
| gVisor          | User-space kernel that intercepts syscalls and emulates kernel behavior | Improve isolation without heavy VMs               |
| Kata Containers | Runs container workloads inside lightweight VMs managed by a runtime    | Stronger isolation with VM-level boundaries       |
| Firecracker     | MicroVMs designed for minimal overhead and fast startup                 | Serverless and multi-tenant isolation at VM level |

These projects trade some density and complexity for stronger separations between workloads and the host kernel.

## Further reading and references

* Seccomp man page: [https://man7.org/linux/man-pages/man2/seccomp.2.html](https://man7.org/linux/man-pages/man2/seccomp.2.html)
* AppArmor project: [https://apparmor.net/](https://apparmor.net/)
* Dirty COW vulnerability: [https://en.wikipedia.org/wiki/Dirty\_COW](https://en.wikipedia.org/wiki/Dirty_COW)
* gVisor: [https://gvisor.dev/](https://gvisor.dev/)
* Kata Containers: [https://katacontainers.io/](https://katacontainers.io/)
* Firecracker: [https://firecracker-microvm.github.io/](https://firecracker-microvm.github.io/)

Choose the combination of sandboxing techniques that best fits your operational constraints and threat model. No single control is sufficient on its own — layering defenses increases resilience while balancing manageability.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/cb62e103-2544-447d-98cd-d669d79bd382" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Control Plane Isolation
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Control-Plane-Isolation/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Control-Plane-Isolation/page)

# Control Plane Isolation

> This article explores control plane isolation in Kubernetes to ensure secure, multi-tenant environments through namespaces, access control mechanisms, and resource quotas.

In this article, we will explore control plane isolation in Kubernetes—a critical mechanism for ensuring secure, multi-tenant environments. By isolating the control plane, different teams can operate without interfering with each other’s operations. This isolation is achieved through namespaces, access control mechanisms, and resource quotas.

## Namespaces Overview

Namespaces offer a way to partition cluster resources among multiple users, ensuring that resources in one namespace remain isolated from those in another. This strategy yields two primary benefits:

* Resource names within one namespace can overlap with those in another, allowing teams to use familiar names without conflicts.
* Many Kubernetes security policies, including role-based access control (RBAC), roles, and network policies, are scoped to individual namespaces.

The diagram below illustrates Kubernetes cluster control plane isolation using namespaces across three nodes. Each node manages different namespaces for effective resource management.

<Frame>
  ![The image illustrates Kubernetes cluster control plane isolation using namespaces across three nodes, each containing different namespaces for resource management.](https://kodekloud.com/kk-media/image/upload/v1752871635/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Control-Plane-Isolation/frame_30.jpg)
</Frame>

You can create namespaces easily with the following commands:

```bash theme={null}
kubectl create namespace namespaceA
kubectl create namespace namespaceB
```

Within each namespace, you can deploy pods or services—allowing the same name to be used across namespaces without conflict.

## Authorization and Access Control

Proper authorization is the cornerstone of control plane isolation. Without adequate restrictions, teams or workloads might improperly access or modify API resources, undermining security policies. Implementing the principle of least privilege is essential: each team should only access the namespaces and resources they require.

The next diagram emphasizes Kubernetes control plane isolation through access controls. It showcases how namespaces, pods, services, persistent volumes, and RBAC policies work together to enforce the principle of least privilege.

<Frame>
  ![The image illustrates Kubernetes control plane isolation using access controls, featuring namespaces with pods, services, persistent volumes, and RBAC policies, emphasizing the principle of least privilege.](https://kodekloud.com/kk-media/image/upload/v1752871636/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Control-Plane-Isolation/frame_110.jpg)
</Frame>

RBAC configurations within each namespace dictate which users or service accounts can perform specific actions, ensuring that permissions are strictly confined to their appropriate scope even when teams share the same cluster.

### Example: Role and RoleBinding in the Development Namespace

The following example demonstrates how to create a Role and a corresponding RoleBinding in the "development" namespace. The Role, "developer-role," grants permissions (get, list, watch, create, update, delete) on pods and services. The RoleBinding, "developer-rolebinding," then ties this role to the user "pranjal."

```yaml theme={null}
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: development
  name: developer-role
rules:
  - apiGroups: [""]
    resources: ["pods", "services"]
    verbs: ["get", "list", "watch", "create", "update", "delete"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: developer-rolebinding
  namespace: development
subjects:
  - kind: User
    name: pranjal
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: developer-role
  apiGroup: rbac.authorization.k8s.io
```

<Callout icon="lightbulb" color="#1CB2FE">
  This configuration enforces strict access control, ensuring that user "pranjal" can only perform the defined actions on pods and services within the "development" namespace.
</Callout>

## Summary

Control plane isolation in Kubernetes is essential for maintaining a secure and efficient multi-tenant cluster environment. By effectively using namespaces along with tightly scoped RBAC policies and access controls, organizations can ensure that each team operates within its designated boundaries without affecting others.

For more information, explore our additional resources on [Kubernetes Basics](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/) and [Kubernetes Documentation](https://kubernetes.io/docs/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/4b127100-e6b3-42a9-af50-4bcf5966ef76" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 DNS in Multi Tenant Environments
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/DNS-in-Multi-Tenant-Environments/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/DNS-in-Multi-Tenant-Environments/page)

# DNS in Multi Tenant Environments

> This guide explores configuring DNS in multi-tenant Kubernetes environments to ensure security and isolation between tenants sharing the same cluster.

In this guide, we explore how to configure DNS in a multi-tenant Kubernetes environment. DNS plays a crucial role in Kubernetes by translating service and pod names to IP addresses, ensuring seamless communication within the cluster. However, when multiple tenants share the same cluster—each represented by different namespaces—special considerations are necessary to enforce security and isolation between these tenants.

By default, Kubernetes deploys a DNS service (typically CoreDNS) to manage name resolution throughout the cluster. This default configuration allows any service or pod to be accessed across namespaces using fully qualified domain names (FQDNs). For example, a service named "backend" in namespace A can be resolved from namespace B using the following FQDN:

```text theme={null}
backend.namespace-a.svc.cluster.local
```

This behavior simplifies in-cluster communication but lacks robust isolation between tenants. In multi-tenant setups, restricting cross-namespace DNS resolution is essential to prevent accidental or malicious discovery of resources across namespaces.

<Callout icon="lightbulb" color="#1CB2FE">
  Restricting DNS queries to the same namespace enhances tenant security and prevents unwanted cross-namespace communication.
</Callout>

## Configuring CoreDNS for Tenant Isolation

To enhance security, you can modify the CoreDNS configuration so that DNS queries are limited to the namespace in which they originate. The following steps demonstrate how to achieve this.

### Step 1: Edit the CoreDNS ConfigMap

Use the following command to edit the CoreDNS configuration stored in the ConfigMap:

```bash theme={null}
kubectl edit configmap coredns -n kube-system
```

### Step 2: Update the CoreDNS Corefile

Within the ConfigMap, adjust the Corefile by adding the `fallthrough in-namespace` directive under the Kubernetes block. Below is an example of the updated Corefile:

```yaml theme={null}
apiVersion: v1
kind: ConfigMap
metadata:
  name: coredns
  namespace: kube-system
data:
  Corefile: |
    .:53 {
        errors
        health {
            lameduck 5s
        }
        ready
        kubernetes cluster.local in-addr.arpa ip6.arpa {
            pods verified
            fallthrough in-namespace
        }
        prometheus :9153
        forward . /etc/resolv.conf
        cache 30
        loop
        reload
        loadbalance
    }
```

After updating the ConfigMap, CoreDNS automatically reloads the configuration in its running pods.

<Callout icon="triangle-alert" color="#FF6B6B">
  Be aware that misconfiguring DNS settings can interrupt service discovery within your cluster. Always validate changes in a test environment before applying them to production.
</Callout>

### Step 3: Test the DNS Restrictions

Deploy pods in different namespaces and perform DNS queries to verify that cross-namespace resolution is restricted. For instance, use the command below to launch a test pod in "namespace-a" and attempt to resolve a service in "namespace-b":

```bash theme={null}
kubectl run test-pod --rm -i --tty --image=busybox --restart=Never --namespace=namespace-a -- nslookup backend.namespace-b.svc.cluster.local
```

If configured correctly, the DNS lookup from a pod in namespace A will not resolve a service in namespace B, thereby ensuring improved tenant isolation and enhanced security.

## Summary Table

| Configuration Step     | Action                                   | Command/Code Example                                                                                                                           |
| ---------------------- | ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Edit CoreDNS ConfigMap | Modify the CoreDNS settings              | `kubectl edit configmap coredns -n kube-system`                                                                                                |
| Update Corefile        | Add `fallthrough in-namespace` directive | See the YAML snippet above for the updated Corefile configuration                                                                              |
| Test DNS Isolation     | Verify isolation by performing nslookup  | `kubectl run test-pod --rm -i --tty --image=busybox --restart=Never --namespace=namespace-a -- nslookup backend.namespace-b.svc.cluster.local` |

Implementing these steps guarantees that pods in one namespace cannot resolve services in another, reinforcing security in your multi-tenant Kubernetes environment. For additional best practices, see the [Kubernetes Documentation](https://kubernetes.io/docs/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/0717d4eb-9fb4-4f54-80a7-3e04f18a1971" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Data Plane Isolation Network
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Data-Plane-Isolation-Network/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Data-Plane-Isolation-Network/page)

# Data Plane Isolation Network

> This lesson explores enforcing multi-tenancy in Kubernetes through network policies to enhance security by isolating network traffic between different tenants and their applications.

In this lesson, we explore how to enforce multi-tenancy in Kubernetes by applying network policies. These policies enhance security in multi-tenant clusters by isolating network traffic between different tenants and their applications. This tutorial builds on concepts discussed in the [Kubernetes Troubleshooting for Application Developers](https://learn.kodekloud.com/user/courses/kubernetes-troubleshooting-for-application-developers) course and sets the stage for more advanced topics in the [Kubernetes Challenges](https://learn.kodekloud.com/user/courses/kubernetes-challenges) course.

## Overview of Network Policies

Network policies enable administrators to define rules that control the flow of network traffic between pods in Kubernetes. Key elements of these policies include:

• Pod Selectors: Identify target pods based on their labels.\
• Namespace Selectors: Specify the namespaces to which the policy applies.\
• Ports: Define allowed or restricted port numbers or ranges.\
• Protocols: Indicate the applicable protocols, such as TCP or UDP.

<Callout icon="lightbulb" color="#1CB2FE">
  Network policies are fundamental to securing multi-tenant environments by ensuring that only authorized communications occur between specified pods and namespaces.
</Callout>

## Multi-Tenant Use Case

Imagine a Kubernetes cluster with two namespaces: tenant A and tenant B. In this scenario, you may want to restrict traffic between these namespaces. For instance, a policy could allow pods in tenant A (identified by a particular label) to accept TCP traffic on port 8080 only from pods in tenant B.

## Example: Allowing Inter-Tenant Traffic

Below is an example YAML manifest for a network policy that permits pods labeled with `app: backend` in the `tenant_a` namespace to receive TCP traffic on port 8080 from any pod in a namespace labeled as `tenant_b`:

```yaml theme={null}
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-tenant-a-to-tenant-b
  namespace: tenant_a
spec:
  podSelector:
    matchLabels:
      app: backend
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          tenant: tenant_b
  ports:
  - protocol: TCP
    port: 8080
```

This configuration illustrates how network policies can control and secure inter-tenant communications in a Kubernetes cluster. By setting precise rules for pod and namespace selectors, ports, and protocols, administrators can ensure that only allowed interactions occur.

## Conclusion

Effective traffic management is critical for the security of multi-tenant Kubernetes clusters. Utilizing network policies enables administrators to maintain granular control over network communications and isolate traffic between tenants. Further exploration of Kubernetes security best practices will enhance your ability to secure your cluster effectively.

<Callout icon="lightbulb" color="#1CB2FE">
  For more details on Kubernetes security, visit the [Kubernetes Documentation](https://kubernetes.io/docs/) and explore other related resources.
</Callout>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/be9b113a-7cf0-45be-a673-2cf5cf333656" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Data Plane Isolation Storage
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Data-Plane-Isolation-Storage/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Data-Plane-Isolation-Storage/page)

# Data Plane Isolation Storage

> This article explores implementing data-plane isolation for storage using distinct storage classes for different tenant types to manage persistent volumes and claims.

In this lesson, we explore how to implement data-plane isolation for storage through the use of storage classes. By defining distinct storage classes for different tenant types, you can manage persistent volumes (PVs) and persistent volume claims (PVCs) according to the specific performance requirements of each group.

Consider the following scenario with two namespaces:

* **Namespace A**: Dedicated to a critical tenant requiring high-performance storage.
* **Namespace B**: Allocated to a regular tenant with standard resource demands.

By setting up separate storage classes, you can effectively isolate the data plane and ensure that each tenant's storage is provisioned and managed optimally.

<Callout icon="lightbulb" color="#1CB2FE">
  Creating separate storage classes allows you to customize PVs and PVCs for varying workloads, leading to improved resource utilization and better performance isolation.
</Callout>

## High-Performance Storage Class Example

For the critical tenant in Namespace A, a high-performance storage class can be configured to provide PVs with enhanced IOPS. The YAML configuration below demonstrates how to set up such a storage class:

```yaml theme={null}
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: high-performance
provisioner: kubernetes.io/aws-ebs
parameters:
  type: io1                          # AWS io1 disks support high IOPS
  iopsPerGB: "50"                    # Specify high IOPS per GB
  fsType: ext4
reclaimPolicy: Delete
allowVolumeExpansion: true
volumeBindingMode: Immediate
```

PVCs targeting high IOPS workloads can bind directly to this storage class, ensuring that critical applications receive the necessary performance. Conversely, a standard-performance storage class can be configured for regular tenants with less intensive storage requirements.

<Callout icon="lightbulb" color="#1CB2FE">
  For additional insights into Kubernetes storage and persistent volume configurations, check out the [Kubernetes Documentation](https://kubernetes.io/docs/concepts/storage/).
</Callout>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/e2b565cf-bcf5-460f-8f07-c75f2cae1f9c" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/9748ac82-ecd9-47e8-a112-06b81f64bbc6" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Data Plane Isolation
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Data-Plane-Isolation/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Data-Plane-Isolation/page)

# Data Plane Isolation

> This article explores data-plane isolation in Kubernetes to enhance performance, security, and reliability in multi-tenant environments.

In this article, we will explore the concept of data-plane isolation in Kubernetes, an essential strategy for maintaining performance, enhancing security, and ensuring reliability in multi-tenant environments.

The data plane is responsible for the execution of workloads, managing key functions such as network operations, storage handling, and compute resource management. Effective data-plane isolation helps prevent resource contention and reduces security risks by ensuring that workloads remain segregated even when sharing the same infrastructure.

## Key Mechanisms for Data-Plane Isolation

Data-plane isolation is implemented through several critical mechanisms, including:

* **Network Policies:** These policies control the flow of traffic between pods, ensuring that only authorized communications occur.
* **Storage Isolation:** Storage resources are segmented to prevent unauthorized access and to guarantee that storage operations of one tenant do not interfere with others.
* **Taints and Tolerations:** This mechanism prevents pods from being scheduled on inappropriate nodes by allowing only those pods with the matching tolerations to run on tainted nodes.

<Callout icon="lightbulb" color="#1CB2FE">
  Understanding these mechanisms is vital for designing secure and efficient Kubernetes environments. In the upcoming lessons, we will examine each of these techniques in greater detail.
</Callout>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/bef9038a-bed3-4645-bd80-68a7337eca37" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Demo Encrypting Secret Data at Rest
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Demo-Encrypting-Secret-Data-at-Rest/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Demo-Encrypting-Secret-Data-at-Rest/page)

# Demo Encrypting Secret Data at Rest

> This guide explains how to secure secret data at rest in Kubernetes by encrypting it within the etcd datastore.

In this guide, you'll learn how to secure secret data at rest in Kubernetes by encrypting it inside the etcd datastore. We cover creating secret objects, inspecting their base64-encoded storage, and finally enabling encryption at rest through an encryption configuration. This step-by-step process helps ensure that confidential information remains protected even if someone gains access to your etcd datastore.

***

## 1. Creating a Secret in Kubernetes

Begin by launching your single-node Kubernetes playground built with Kubernetes and ContainerD. Open your terminal to create a secret object using various methods. Here are several examples:

```bash theme={null}
# Create a new secret named my-secret by loading files from a directory
kubectl create secret generic my-secret --from-file=path/to/bar

# Create a secret with specified keys taken from disk files
kubectl create secret generic my-secret --from-file=ssh-privatekey=path/to/id_rsa --from-file=ssh-publickey=path/to/id_rsa.pub

# Create a secret with literal values for keys
kubectl create secret generic my-secret --from-literal=key1=supersecret --from-literal=key2=topsecret

# Create a secret using a combination of a file and a literal value
kubectl create secret generic my-secret --from-file=ssh-privatekey=path/to/id_rsa --from-literal=passphrase=topsecret

# Create a secret from environment files
kubectl create secret generic my-secret --from-env-file=path/to/foo.env --from-env-file=path/to/bar.env
```

Additional customization options include:

* `--allow-missing-template-keys=true`
* `--append-hash=false`
* `--dry-run='none'`

After creating the secret, verify its existence with:

```bash theme={null}
controlplane ~ ➜ kubectl create secret generic my-secret --from-literal=key1=supersecret
secret/my-secret created

controlplane ~ ➜ kubectl get secret
NAME        TYPE    DATA   AGE
my-secret   Opaque  1      5s
```

To inspect the secret details:

```bash theme={null}
controlplane ~ ➜ kubectl describe secret my-secret
Name:         my-secret
Namespace:    default
Labels:       <none>
Annotations:  <none>

Type: Opaque

Data
====
key1:  11 bytes
```

And view its YAML representation:

```bash theme={null}
controlplane ~ ➜ kubectl get secret my-secret -o yaml
apiVersion: v1
data:
  key1: C3VwZXJzZWNyZQ==
kind: Secret
metadata:
  creationTimestamp: "2022-10-24T05:34:13Z"
  name: my-secret
  namespace: default
  resourceVersion: "2111"
  uid: dfe97062-5aa1-46a8-b71c-ffa0cd4c08ec
type: Opaque
```

Notice that the secret data is stored using Base64 encoding. For example:

```bash theme={null}
controlplane ~ → kubectl get secret my-secret -o yaml
apiVersion: v1
data:
  key1: c3VwZXJzZW5yZXQ=
kind: Secret
metadata:
  creationTimestamp: "2022-10-24T05:34:13Z"
  name: my-secret
  namespace: default
  resourceVersion: "2111"
  uid: dfe97c62-5aa1-46a8-b71c-ffa0cd4c08ec
type: Opaque

controlplane ~ → echo "c3VwZXJzZW5yZXQ=" | base64 --decode
supersecret
controlplane ~ →
```

This demonstrates that anyone with access to the secret manifest can decode the data.

<Callout icon="triangle-alert" color="#FF6B6B">
  Storing secrets in base64 does not provide true security. Without encryption at rest, confidential data can be exposed by anyone with direct access to the etcd datastore.
</Callout>

***

## 2. Inspecting Secrets in etcd

Now, explore how Kubernetes stores secret data in etcd. The secret data is persisted under paths such as `/registry/secrets/default/secret1`.

### Viewing Unencrypted Data via etcdctl

You can use the `etcdctl` client (with API version 3) to view raw data stored in etcd. For example, run the following command:

```bash theme={null}
ETCDCTL_API=3 etcdctl \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  get /registry/secrets/default/secret1 | hexdump -C
```

A sample output might be:

```text theme={null}
2f 72 65 67 69 73 74 72 79 2f 73 65 63 72 65 74  |/registry/secret|
31 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  |1..............|
31 2e 6b 38 73 73 73 73 73 73 73 73 73 73 73 73  |1.k8sssssssssss...|
06 2f 76 31                                     |./v1|
```

Running the command with the secret key from our object yields similar unencrypted output, which clearly demonstrates that secret data (i.e., the password "supersecret") is stored without encryption. Anybody with etcd access and the appropriate certificates can retrieve and decode this information.

***

## 3. Installing and Running etcdctl

If you encounter a missing `etcdctl` command, install it using your package manager. For Ubuntu users:

```bash theme={null}
controlplane ~ ➜ etcdctl
-bash: etcdctl: command not found

controlplane ~ ✗ apt-get install etcd-client
Reading package lists... Done
Building dependency tree
...
Setting up etcd-client (3.2.26+dfsg-6) ...
```

After installation, running `etcdctl` displays usage information along with a relevant warning regarding the API version:

```bash theme={null}
controlplane ~ ➜ etcdctl
NAME:
       etcdctl - A simple command line client for etcd.

WARNING:
       Environment variable ETCDCTL_API is not set; defaults to etcdctl v2.
       Set environment variable ETCDCTL_API=3 to use v3 API or ETCDCTL_API=2 to use v2 API.
```

***

## 4. Verifying etcd Data for Your Secrets

Ensure your Kubernetes cluster contains the necessary certificate files, such as `/etc/kubernetes/pki/etcd/ca.crt`. Then inspect the raw secrets stored in etcd using:

```bash theme={null}
ETCDCTL_API=3 etcdctl \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  get /registry/secrets/default/my-secret | hexdump -C
```

This unencrypted output verifies the vulnerability—anyone with etcd access can read the confidential data.

***

## 5. Determining if Encryption at Rest Is Enabled

Before proceeding further, confirm that the Kube API server is configured with an encryption provider. Check for the `--encryption-provider-config` flag in the process arguments or in the API server manifest file. If the flag is absent, you must enable encryption at rest for your secrets.

<Frame>
  ![The image shows a Kubernetes documentation page about configuring and determining encryption at rest, including a caution for high-availability configurations.](https://kodekloud.com/kk-media/image/upload/v1752871637/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Demo-Encrypting-Secret-Data-at-Rest/frame_420.jpg)
</Frame>

***

## 6. Configuring Encryption at Rest

To secure your secret data at rest, create an encryption configuration file that specifies which resources to encrypt and which encryption providers to use. Create a file named "enc.yaml" with the following content:

```yaml theme={null}
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
  - resources:
      - secrets
  providers:
    - aescbc:
        keys:
          - name: key1
            secret: y0xTt+U6xgRdNxe4nDYYsij0GgRDoUYc+wAwOKeNfPs=
    - identity: {}
```

Key points in this configuration:

* The resource targeted for encryption is `secrets`.
* The first provider uses the AES-CBC algorithm. Its key must be a base64-encoded 32-byte value (generate one with the command below if needed).
* The `identity` provider acts as a fallback and will not encrypt data. Its placement after the AES-CBC provider ensures new secrets are encrypted.

Generate a key if needed:

```bash theme={null}
head -c 32 /dev/urandom | base64
```

Save the generated content into the file `enc.yaml`.

***

## 7. Updating the Kube API Server Manifest

To apply the encryption configuration, update the Kube API server manifest with the new encryption file reference. Follow these steps:

1. Create a local directory to store the encryption file (e.g., `/etc/kubernetes/enc`).

2. Move `enc.yaml` into this directory:

   ```bash theme={null}
   mkdir /etc/kubernetes/enc
   mv enc.yaml /etc/kubernetes/enc/
   ```

3. Modify the Kube API server manifest (typically found at `/etc/kubernetes/manifests/kube-apiserver.yaml`) to include a new volume mount and add the `--encryption-provider-config` flag. An example snippet is as follows:

   ```yaml theme={null}
   spec:
     containers:
     - command:
       - kube-apiserver
       ...
       - --encryption-provider-config=/etc/kubernetes/enc/enc.yaml
     volumeMounts:
       ...
       - name: enc
         mountPath: /etc/kubernetes/enc
         readOnly: true
     volumes:
       ...
       - name: enc
         hostPath:
           path: /etc/kubernetes/enc
           type: DirectoryOrCreate
   ```

4. Save your changes. The API server will restart and load the new configuration. Verify the running process with:

   ```bash theme={null}
   ps aux | grep kube-api
   ```

Ensure that the `--encryption-provider-config` flag is present and references the correct path.

***

## 8. Verifying Encryption of New Secrets

Once encryption is enabled, Kubernetes will encrypt all new secret objects in etcd. To test this, create a new secret:

```bash theme={null}
kubectl create secret generic my-secret-2 --from-literal=key2=topsecret
```

Verify its creation:

```bash theme={null}
controlplane ~ ➜ kubectl get secret
NAME          TYPE     DATA   AGE
my-secret     Opaque   1      16m
my-secret-2   Opaque   1      3s
```

Then inspect the secret data in etcd:

```bash theme={null}
ETCDCTL_API=3 etcdctl \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  get /registry/secrets/default/my-secret-2 | hexdump -C
```

You should no longer see the plain text value "topsecret" in the output, confirming that the data is now encrypted.

To update and re-encrypt pre-existing secrets, run:

```bash theme={null}
kubectl get secrets --all-namespaces -o json | kubectl replace -f -
```

This command re-writes each secret so that they are encrypted using the new configuration.

***

## 9. Conclusion

In this guide, we demonstrated how Kubernetes stores secret data as base64‑encoded strings in etcd, highlighting the vulnerabilities of unencrypted data. We then enabled encryption at rest by creating an encryption configuration file, updating the Kube API server manifest, and subsequently verifying that both new and updated secrets are securely encrypted. Following these steps is essential to protect critical data from unauthorized access.

Thank you for reading this guide on encrypting secret data at rest in Kubernetes. For further details, refer to the [Kubernetes Documentation](https://kubernetes.io/docs/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/cbace715-77f8-4f42-8141-dab7052585c6" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Different types of Multi Tenancy in Kubernetes
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Different-types-of-Multi-Tenancy-in-Kubernetes/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Different-types-of-Multi-Tenancy-in-Kubernetes/page)

# Different types of Multi Tenancy in Kubernetes

> This article explores multi-team and multi-customer tenancy models in Kubernetes for effective resource management and security.

In this article, we explore the two primary types of multi-tenancy models in Kubernetes: multi-team tenancy and multi-customer tenancy. Understanding these approaches is crucial for designing clusters that meet diverse organizational needs while ensuring secure and efficient resource management.

## Multi-Team Tenancy

Multi-team tenancy refers to managing and isolating resources for various teams or projects within a single Kubernetes cluster. This model enables different internal groups to share a common infrastructure while maintaining logical separation. Think of it like a multi-story office building where each floor (or namespace) is allocated to a different team.

<Frame>
  ![The image illustrates a Kubernetes cluster with multi-team tenancy, showing nodes A, B, and C, each hosting different teams, supported by compute, storage, and network resources.](https://kodekloud.com/kk-media/image/upload/v1752871638/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Different-types-of-Multi-Tenancy-in-Kubernetes/frame_20.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  In multi-team tenancy, role-based access control (RBAC) and namespace quotas are critical to ensure fair resource allocation and security among internal teams.
</Callout>

## Multi-Customer Tenancy

Multi-customer tenancy involves hosting and segregating applications for multiple external customers or clients from a single Kubernetes cluster. This approach is common among SaaS providers who must isolate data and applications to meet strict security standards. In this model, each customer’s workload is securely separated even though they share the same underlying infrastructure.

<Frame>
  ![The image illustrates a Kubernetes cluster with multi-customer tenancy, showing nodes A, B, and C, each hosting different customers, supported by compute, storage, and network resources.](https://kodekloud.com/kk-media/image/upload/v1752871640/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Different-types-of-Multi-Tenancy-in-Kubernetes/frame_50.jpg)
</Frame>

<Callout icon="triangle-alert" color="#FF6B6B">
  For multi-customer environments, enforcing stringent security protocols (such as compliance with GDPR, HIPAA, or other regulatory standards) is essential, as customers do not have direct access to the cluster.
</Callout>

## Key Differences

When comparing multi-team and multi-customer tenancy, consider the following differences:

* **Focus:**
  * **Multi-Team:** Primarily designed for managing internal organizational teams.
  * **Multi-Customer:** Tailored for managing applications and data for external clients.

* **Isolation and Security:**
  * Both models rely on Kubernetes namespaces for resource isolation. However, multi-customer tenancy typically demands higher security measures and separation due to stricter regulatory requirements.

* **Access Control:**
  * **Multi-Team:** Internal teams usually have direct access to the cluster through tools like kubectl or GitOps controllers.
  * **Multi-Customer:** External customers do not have direct access; instead, cluster operations remain behind the scenes.

<Frame>
  ![The image compares multi-team and multi-customer tenancy, highlighting differences in focus, isolation, resource management, governance, compliance, and access restrictions using Kubernetes.](https://kodekloud.com/kk-media/image/upload/v1752871641/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Different-types-of-Multi-Tenancy-in-Kubernetes/frame_150.jpg)
</Frame>

In multi-customer setups, Kubernetes operates largely behind the scenes, ensuring that end-users experience a secure and seamlessly managed service environment.

For additional details on Kubernetes design patterns and security practices, consider exploring the following resources:

* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Kubernetes Basics](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/7a505db4-e9ba-4e77-8ec8-623a95ab8d81" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Implement pod to pod encryption by use of mTLS
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Implement-pod-to-pod-encryption-by-use-of-mTLS/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Implement-pod-to-pod-encryption-by-use-of-mTLS/page)

# Implement pod to pod encryption by use of mTLS

> This guide explores securing pod-to-pod communication in Kubernetes using mutual TLS encryption to ensure data confidentiality and integrity.

In this guide, we explore how to secure pod-to-pod communication within a Kubernetes cluster by leveraging mutual TLS (mTLS) encryption. By implementing mTLS, you ensure that data exchanged between pods remains confidential and tamper-proof.

<Frame>
  ![The image is an orange slide with the text "Using mTLS to secure Pod-Pod communication" and a small circular design in the corner.](https://kodekloud.com/kk-media/image/upload/v1752871642/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Implement-pod-to-pod-encryption-by-use-of-mTLS/frame_0.jpg)
</Frame>

## The Need for Encryption in Kubernetes

Kubernetes clusters often span multiple nodes with numerous pods communicating with each other. By default, these inter-pod communications are unencrypted, which poses a risk if sensitive data—such as customer phone numbers or addresses—is transmitted in plain text. mTLS provides a robust solution by authenticating and encrypting communications between pods, thereby reducing the risks of data breaches and unauthorized access.

<Callout icon="lightbulb" color="#1CB2FE">
  Using mTLS in a Kubernetes environment ensures that every pod verifies its communication counterpart, leading to significantly enhanced security across your cluster.
</Callout>

## How mTLS Works Between Pods

The process of establishing a secure connection between two pods involves several steps:

1. **Certificate Request:**\
   Pod A initiates communication by requesting Pod B’s certificate.
2. **Certificate Exchange:**\
   Pod B responds with its certificate and simultaneously requests Pod A’s certificate.
3. **Certificate Validation and Key Exchange:**\
   After validating Pod B's certificate, Pod A sends its public certificate along with a symmetric encryption key.
4. **Secure Communication:**\
   Once Pod B validates Pod A’s certificate, both pods switch to using the symmetric key to encrypt all further communications.

<Frame>
  ![The image illustrates a secure communication process with keys, locks, and a message, involving a user named John at 123 Sesame Street.](https://kodekloud.com/kk-media/image/upload/v1752871643/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Implement-pod-to-pod-encryption-by-use-of-mTLS/frame_100.jpg)
</Frame>

This mutual authentication and encryption ensure that each pod's identity is verified, preventing attackers from introducing fake data or commands.

## Managing Encryption Across a Cluster

One might wonder how to manage secure communication when hundreds of pods across several nodes must interact. While some applications, like MySQL, offer built-in encryption, relying solely on individual applications can lead to inconsistencies. Different encryption algorithms may be used, adding complexity and potential security gaps.

A more efficient strategy is to implement mTLS using dedicated service mesh tools. This approach abstracts encryption responsibilities from the application layer to the network layer.

### Service Mesh Tools for mTLS

Popular tools such as [Istio](https://istio.io) and [Linkerd](https://linkerd.io) enable mTLS at the network level, ensuring seamless and consistent encryption for service-to-service communication. These tools:

* Offload encryption tasks from application code.
* Provide centralized management of encryption policies.
* Ensure consistent security across heterogeneous applications.

Among these, [Istio](https://istio.io) is widely adopted for its ability to automatically deploy sidecar containers alongside application pods.

## Istio and Its Modes of Operation

Istio enhances cluster security by automatically intercepting pod communications. When a web application pod communicates with a MySQL pod, the Istio sidecar attached to each pod encrypts and decrypts messages seamlessly.

Istio supports two primary encryption modes:

* **Permissive (Opportunistic) Mode:**\
  Traffic is encrypted when possible, but unencrypted communication is allowed for interactions with external services or non-mTLS-compatible applications.
* **Strict (Enforced) Mode:**\
  All traffic must be encrypted using mTLS. Although this maximizes security, it requires all communicating services to support mTLS.

<Frame>
  ![The image depicts a network diagram with Istio-managed services, including webapp1, webapp2, and MySQL, connected by dotted lines, indicating service mesh architecture.](https://kodekloud.com/kk-media/image/upload/v1752871644/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Implement-pod-to-pod-encryption-by-use-of-mTLS/frame_200.jpg)
</Frame>

<Callout icon="triangle-alert" color="#FF6B6B">
  Before enabling strict mTLS mode, ensure all your services are mTLS-compatible to avoid connectivity issues.
</Callout>

## How Istio Implements mTLS

When communication is initiated, Istio’s sidecar intercepts and encrypts outbound messages. On the receiving end, the corresponding sidecar decrypts the message before passing it on to the application. This approach not only secures the traffic but also simplifies the process for developers, as encryption is handled externally.

<Frame>
  ![The image illustrates a network architecture with a web app and MySQL using sidecars, and an external app communicating in plain text.](https://kodekloud.com/kk-media/image/upload/v1752871645/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Implement-pod-to-pod-encryption-by-use-of-mTLS/frame_380.jpg)
</Frame>

## Conclusion

By integrating mTLS with service mesh technologies like Istio, you can achieve a high level of security within your Kubernetes clusters. This setup ensures that:

* Each pod is mutually authenticated.
* All data in transit is encrypted.
* The encryption overhead is managed independently of the application, contributing to a streamlined and secure infrastructure.

Implementing pod-to-pod encryption using mTLS is a critical step in safeguarding your Kubernetes environment from potential security breaches. For more detailed information on Kubernetes security practices, visit the [Kubernetes Documentation](https://kubernetes.io/docs/).

That concludes our guide on implementing pod-to-pod encryption using mTLS.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/e3bb6e70-2188-4bfb-9711-162152b85d2d" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Introduction to Cilium
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Introduction-to-Cilium/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Introduction-to-Cilium/page)

# Introduction to Cilium

> This article explores leveraging Cilium for robust Pod-to-Pod encryption in containerized applications using eBPF for advanced network security policies.

In this lesson, we explore how to leverage Cilium for robust Pod-to-Pod encryption. Cilium is an open-source solution that secures network connectivity between containerized applications. Built for modern microservices architectures, it utilizes extended eBPF (Extended Berkeley Packet Filter) to enforce advanced network security policies. Among its many features, pod-to-pod encryption stands out as a key benefit.

<Frame>
  ![The image provides an overview of Cilium, an open-source software for securing network connectivity between container applications, featuring eBPF and pod-to-pod encryption.](https://kodekloud.com/kk-media/image/upload/v1752871646/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Introduction-to-Cilium/frame_20.jpg)
</Frame>

## Cilium's Approach to Pod-to-Pod Encryption

Cilium leverages eBPF for highly efficient data processing, enabling encryption with minimal performance overhead. Encryption is applied transparently, meaning your application code remains unchanged and unaware of the security processes in the background.

Key features include:

* **Flexible Encryption Options:** Multiple encryption algorithms to suit different use cases.
* **End-to-End Security:** Continuous encryption ensures data remains secure throughout its network journey.
* **Policy-Driven Control:** Customizable encryption policies allow precise management of security across the cluster.

<Frame>
  ![The image outlines Cilium's approach to P2P encryption, highlighting eBPF utilization, transparent encryption, flexible options, end-to-end security, and policy-driven encryption.](https://kodekloud.com/kk-media/image/upload/v1752871647/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Introduction-to-Cilium/frame_70.jpg)
</Frame>

## Setting Up Cilium

Setting up Cilium for encryption involves several high-level steps:

1. **Installation:**\
   Deploy Cilium on your Kubernetes cluster via Helm or standard manifests, depending on your preferred method.

2. **Configuration:**\
   Enable the encryption features explicitly after installation to secure pod-to-pod communications.

3. **Key Management:**\
   Utilize Cilium’s native key management system, or integrate it with your existing infrastructure for managing encryption keys.

4. **Policy Definition:**\
   Create specific encryption policies based on namespaces or labels to control exactly where and when encryption is applied.

<Frame>
  ![The image outlines steps for setting up Cilium for encryption: Installation, Configuration, Key Management, and Policy Definition.](https://kodekloud.com/kk-media/image/upload/v1752871648/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Introduction-to-Cilium/frame_110.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  For detailed installation and configuration instructions, refer to the official [Cilium documentation](https://docs.cilium.io/en/stable/).
</Callout>

## Monitoring and Performance Benefits

Continuous monitoring is vital to verify that encryption is consistently active and that all inter-pod traffic remains secure. Thanks to its efficient eBPF implementation, Cilium introduces minimal performance overhead while executing encryption and other security tasks. Its robust features include:

* **Encryption:** Secure data transmission between pods.
* **Identity Management:** Effective tracking and control of application identities.
* **Policy Enforcement:** Streamlined application of security policies across your cluster.

These features collectively contribute to making your Kubernetes cluster both secure and easily manageable.

<Frame>
  ![The image lists the benefits of Cilium: Performance, Security, Flexibility, and Simplicity, each represented by an icon.](https://kodekloud.com/kk-media/image/upload/v1752871649/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Introduction-to-Cilium/frame_150.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Cilium is backed by a vibrant community, including contributions from open-source enthusiasts and enterprise-level organizations, ensuring continuous improvement and support.
</Callout>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/9394b49e-69bf-45d7-bef6-c9f47cc0ded0" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/4dead9aa-6347-4d88-99f5-3ca11820d0be" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Kata Containers
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Kata-Containers/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Kata-Containers/page)

# kata Containers

> This article introduces Kata Containers and its approach to container sandboxing for enhanced security and isolation.

In this article, we introduce Kata Containers and explore its innovative approach to container sandboxing, designed to enhance security and isolation.

Kata Containers distinguishes itself from alternatives like [gVisor](https://gvisor.dev) by using a lightweight virtual machine (VM) for each container. Unlike traditional containerization, where multiple applications share the same operating system kernel, Kata Containers assigns a dedicated kernel to every container. This isolation strategy prevents system-wide failures since any malfunction within a container only affects that individual container.

<Callout icon="lightbulb" color="#1CB2FE">
  Each container in Kata Containers runs inside its own lightweight VM, ensuring
  that issues in one container do not compromise the stability of other
  containers or the host system.
</Callout>

While the idea of deploying a separate VM for every container might suggest a significant performance overhead, Kata Containers is optimized to minimize this impact. Although there is a slight performance trade-off—mainly due to the additional memory and compute resources required—this compromise is balanced by the enhanced security and isolation benefits provided.

## Hardware Virtualization Requirements

One important factor to consider is that Kata Containers depends on hardware virtualization support. This means that running Kata Containers in common cloud environments can be challenging. Typically, cloud compute instances already operate as virtual machines, so deploying Kata Containers would involve nested virtualization, where a VM runs inside another VM.

<Callout icon="triangle-alert" color="#FF6B6B">
  Many cloud providers do not support nested virtualization. However, some
  exceptions exist. For instance, [Google
  Cloud](https://cloud.google.com/compute/docs/instances/nested-virtualization)
  allows nested virtualization, though it often requires manual configuration
  and may not yield optimal performance.
</Callout>

If you have access to dedicated physical or bare metal servers—especially in a cloud setting—you can leverage Kata Containers without the performance limitations associated with nested virtualization.

For more detailed insights into container security and virtualization technologies, consider exploring additional resources and documentation from [Kubernetes Documentation](https://kubernetes.io/docs/) and [Docker Hub](https://hub.docker.com/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/0edfec7a-c84e-498e-a1f7-03ea99038d3b" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Levels of Isolation in Kubernetes Namespace Pod Node
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Levels-of-Isolation-in-Kubernetes-Namespace-Pod-Node/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Levels-of-Isolation-in-Kubernetes-Namespace-Pod-Node/page)

# Levels of Isolation in Kubernetes Namespace Pod Node

> This article explores layers of isolation in Kubernetes to ensure secure operation of workloads, teams, or customers sharing the same cluster without interference.

In this lesson, we explore the multiple layers of isolation in Kubernetes. We focus on how workloads, teams, or customers sharing the same cluster can operate securely without interfering with one another. Kubernetes offers isolation at different levels, each with varying trade-offs in implementation effort, operational complexity, and cost.

Imagine a Kubernetes cluster where different teams—say, Team A and Team B—deploy their own pods. Without proper isolation, a pod from one team might inadvertently or maliciously access or interfere with the pods of another team, such as gaining access to a team’s database.

<Frame>
  ![The image illustrates Kubernetes cluster isolation, showing separate Team-a and Team-b pods with a security shield indicating restricted interaction between them.](https://kodekloud.com/kk-media/image/upload/v1752871650/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Levels-of-Isolation-in-Kubernetes-Namespace-Pod-Node/frame_30.jpg)
</Frame>

Kubernetes achieves tenant isolation across both the control plane and the data plane:

* **Control Plane Isolation**: Implemented using namespaces and access control mechanisms such as Role-Based Access Control (RBAC).
* **Data Plane Isolation**: Managed via network policies, storage isolation, and node isolation.

<Callout icon="lightbulb" color="#1CB2FE">
  Namespaces divide a Kubernetes cluster into logical sections, ensuring that each team or project can manage its resources independently.
</Callout>

## Namespace Isolation

Think of namespaces as different office spaces within a large building. Each team, department, or customer is allocated its own office with dedicated resources, but they still share common infrastructure like electricity and water. In Kubernetes, namespaces allow each team to have isolated resources without affecting other teams.

<Frame>
  ![The image illustrates "Namespace Isolation" using a building analogy, with each floor representing a team namespace and shared facilities depicted on the side.](https://kodekloud.com/kk-media/image/upload/v1752871651/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Levels-of-Isolation-in-Kubernetes-Namespace-Pod-Node/frame_100.jpg)
</Frame>

Within these namespaces, RBAC acts like key cards in an office building—granting employees different levels of access based on their roles. Managers might have broad access, while regular team members have limited access to only their designated areas.

## Pod Isolation

Within each namespace, pods serve as individual workspaces. A pod is a set of one or more containers that closely share resources, similar to employees sharing a desk workspace. Although containers within a pod collaborate, different pods remain isolated to securely allocate resources and limit interference.

<Frame>
  ![The image illustrates pod/container isolation, showing two people at desks with shared facilities like a printer and meeting room, emphasizing isolated yet collaborative workspaces.](https://kodekloud.com/kk-media/image/upload/v1752871652/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Levels-of-Isolation-in-Kubernetes-Namespace-Pod-Node/frame_150.jpg)
</Frame>

## Network Isolation

Just as an office building might have exclusive meeting rooms or secure network segments, Kubernetes employs network policies to restrict communication between pods. These rules ensure that only allowed pods interact, maintaining security within the internal network.

<Frame>
  ![The image illustrates network isolation, showing Team A allowed and Team B denied access to internal communications, highlighting network policy control.](https://kodekloud.com/kk-media/image/upload/v1752871653/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Levels-of-Isolation-in-Kubernetes-Namespace-Pod-Node/frame_170.jpg)
</Frame>

## Node Isolation

Nodes in a Kubernetes cluster can be compared to floors in a building. Each floor (node) can host multiple teams under strict access policies or, in some cases, be dedicated entirely to a single team. This approach further enforces isolation at the infrastructure level.

<Frame>
  ![The image illustrates node level isolation in Kubernetes, comparing nodes to building floors, with restricted access for different companies on specific floors.](https://kodekloud.com/kk-media/image/upload/v1752871653/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Levels-of-Isolation-in-Kubernetes-Namespace-Pod-Node/frame_190.jpg)
</Frame>

## Hard Isolation vs. Soft Isolation

Kubernetes supports two primary models of tenant isolation:

### Hard Isolation

Hard isolation involves dedicating physical or virtual infrastructure to each tenant so that compute, storage, and networking resources are not shared. This model guarantees complete segregation of workloads.

<Frame>
  ![The image illustrates a Kubernetes cluster with hard isolation, showing Node A and Node B, each with separate namespaces, pods, services, PVs, and PVCs.](https://kodekloud.com/kk-media/image/upload/v1752871654/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Levels-of-Isolation-in-Kubernetes-Namespace-Pod-Node/frame_220.jpg)
</Frame>

### Soft Isolation

Soft isolation, on the other hand, allows tenants to share the underlying infrastructure while enforcing logical separations using namespaces. Resource quotas and limits prevent any single tenant from consuming too much of the cluster’s resources, and network policies continue to define clear communication boundaries.

<Frame>
  ![The image illustrates a Kubernetes cluster with soft isolation, showing Node A containing Tenant A and B namespaces, each with pods, services, PVs, and PVCs.](https://kodekloud.com/kk-media/image/upload/v1752871655/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Levels-of-Isolation-in-Kubernetes-Namespace-Pod-Node/frame_240.jpg)
</Frame>

## Conclusion

Kubernetes provides a robust framework for isolating workloads through namespaces, RBAC, network policies, and node-level controls. Whether employing hard isolation with dedicated infrastructure or soft isolation through shared resources with logical segmentation, Kubernetes ensures that multiple tenants can coexist securely and efficiently within the same environment.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/54864781-db49-4d5f-ba87-b510b9e632fa" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Manage Kubernetes secrets
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Manage-Kubernetes-secrets/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Manage-Kubernetes-secrets/page)

# Manage Kubernetes secrets

> This article provides a guide on securing applications with Kubernetes Secrets, detailing creation, injection, and best practices for managing sensitive data.

Welcome to this comprehensive guide on securing your applications with Kubernetes Secrets. In this lesson, you'll learn how to replace hardcoded sensitive data in your applications with a more secure approach using Kubernetes Secrets. We will walk through a Python web application example, demonstrate both imperative and declarative methods for creating Secrets, and explain how to inject these Secrets into your Pods securely.

## Example Application Overview

In our example, a simple Python web application connects to a MySQL database. On a successful connection, the application displays a success message. However, the code currently hardcodes the database hostname, username, and password. Although non-sensitive data such as hostnames or usernames can be stored in a ConfigMap, using the same approach for sensitive information like passwords is not recommended.

Below is an excerpt of the Python application code:

```python theme={null}
import os
from flask import Flask, render_template  # Added render_template import

app = Flask(__name__)

@app.route("/")
def main():
    # Warning: Hardcoding credentials (host, user, password) is not secure.
    mysql.connector.connect(host="mysql", database="mysql",
                            user="root", password="paswrd")
    return render_template('hello.html', color=fetchcolor())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
```

<Callout icon="triangle-alert" color="#FF6B6B">
  Hardcoding credentials in your application code is insecure. Use Kubernetes Secrets to manage sensitive configuration data securely.
</Callout>

A sample ConfigMap for non-sensitive configurations might look like this:

```yaml theme={null}
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  # Non-sensitive configuration data can be placed here.
```

While a ConfigMap can hold non-sensitive values safely, passwords require an extra layer of security. This is where Kubernetes Secrets become essential—they store sensitive information in an encoded format rather than plain text.

## Steps to Work with Kubernetes Secrets

Creating and using Secrets generally involves two main steps:

1. **Create the Secret.**
2. **Inject the Secret into a Pod.**

### Mapping Plain Text to Base64 Encoded Values

Consider the following mapping between plain text values and their corresponding base64-encoded values:

Plain text:

```text theme={null}
DB Host:      mysql
DB User:      root
DB Password:  paswrd
```

Encoded format:

```text theme={null}
DB_Host:      bXlzcWw=
DB_User:      cm9vdA==
DB_Password:  cGFzd3Jk
```

<Callout icon="lightbulb" color="#1CB2FE">
  Always encode your sensitive data using base64 when creating a declarative Secret. Avoid using plain text values.
</Callout>

## Creating a Secret

There are two primary methods to create a Kubernetes Secret: the imperative and declarative approaches.

### Imperative Approach

With the imperative approach, you can directly add key-value pairs from the command line. For example, to create a secret named "app-secret" with values for DB\_Host, DB\_User, and DB\_Password, use:

```bash theme={null}
kubectl create secret generic app-secret --from-literal=DB_Host=mysql --from-literal=DB_User=root --from-literal=DB_Password=paswrd
```

Alternatively, if you have your data stored in a file, you can create the secret with:

```bash theme={null}
kubectl create secret generic app-secret --from-file=app_secret.properties
```

### Declarative Approach

For a more controlled process, create a YAML definition for the Secret. Note that all values must be base64 encoded. Here is an example:

```yaml theme={null}
apiVersion: v1
kind: Secret
metadata:
  name: app-secret
data:
  DB_Host: bXlzcWw=
  DB_User: cm9vdA==
  DB_Password: cGFzd3Jk
```

Create the Secret by applying the YAML file:

```bash theme={null}
kubectl create -f secret-data.yaml
```

> Note: When specifying data values in plain text, the information is not secure. Ensure that the secret values are base64 encoded using one of the available encoding methods.

### Encoding Secret Data

On a Linux system, you can generate the base64-encoded version of your secret by running:

```bash theme={null}
echo -n 'mysql' | base64
echo -n 'root' | base64
echo -n 'paswrd' | base64
# Output: cGFzd3Jk
```

## Viewing and Decoding Secrets

To list all Secrets, execute:

```bash theme={null}
kubectl get secrets
```

Sample output:

```plaintext theme={null}
NAME          TYPE     DATA   AGE
app-secret    Opaque   3      10m
```

To view detailed information about a specific Secret without revealing its actual values, use:

```bash theme={null}
kubectl describe secrets app-secret
```

For example:

```plaintext theme={null}
Name:         app-secret
Namespace:    default
Labels:       <none>
Annotations:  <none>
Type:         Opaque

Data
====
DB_Host:      10 bytes
DB_User:      4 bytes
DB_Password:  6 bytes
```

To display the Secret in YAML format (this shows the encoded values), run:

```bash theme={null}
kubectl get secret app-secret -o yaml
```

To decode an encoded value, execute:

```bash theme={null}
echo -n 'bXlzcWw=' | base64 --decode
echo -n 'cm9vdA==' | base64 --decode
# Output: root
```

## Injecting Secrets into a Pod

After creating a Secret, you can inject it into a Pod in two ways: as environment variables or as files via a mounted volume.

### Injecting as Environment Variables

Use the `envFrom` property in your container specification to inject the Secret data as environment variables. For example:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: simple-webapp-color
  labels:
    name: simple-webapp-color
spec:
  containers:
    - name: simple-webapp-color
      image: simple-webapp-color
      ports:
        - containerPort: 8080
      envFrom:
        - secretRef:
            name: app-secret
```

All key-value pairs in the "app-secret" will be available as environment variables in your container.

### Injecting as Files in a Volume

Alternatively, mount the Secret as a volume so that each key is written into a separate file. Example configuration:

```yaml theme={null}
volumes:
  - name: app-secret-volume
    secret:
      secretName: app-secret
```

Mount the volume into your container (for instance, at `/opt/app-secret-volumes`) and inspect the files:

```bash theme={null}
ls /opt/app-secret-volumes
cat /opt/app-secret-volumes/DB_Password
# Output: paswrd
```

## Security Considerations

When managing Secrets in Kubernetes, keep the following security best practices in mind:

* Kubernetes Secrets are encoded but not encrypted, meaning anyone with access can decode them using base64.
* Avoid checking in secret definition files to version control systems, such as GitHub.
* By default, Secrets stored in etcd are not encrypted. Consider enabling encryption at rest for enhanced security.

### Enabling Encryption at Rest

To enhance security, enable encryption at rest by configuring an encryption file similar to the snippet below:

```yaml theme={null}
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
  - resources:
      - secrets
providers:
  - identity: {}
  - aesgcm:
      keys:
        - name: key1
          secret: c2VjcmV0IGlzIHN1bXdlcnZlZQ==
        - name: key2
          secret: dGhpcPyBcyBwYXNzd29yZA==
  - aescbc:
      keys:
        - name: key1
          secret: c2VjcmV0IGlzIHN1bXdlcnZlZQ==
        - name: key2
          secret: dGhpcPyBcyBwYXNzd29yZA==
  - secretbox:
      keys:
        - name: key1
          secret: YWjZGVmZ2hpamtsbW5vcHyc3R1nd4eXokMjY=
```

Then, pass the configuration to the kube-apiserver. Modify your API server Pod specification as follows:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  annotations:
    kubeadm.kubernetes.io/kube-apiserver.advertise-address.endpoint: 10.10.30.4:6443
  labels:
    component: kube-apiserver
    tier: control-plane
  name: kube-apiserver
  namespace: kube-system
spec:
  containers:
    - command:
        - kube-apiserver
        # ... other command arguments ...
        - --encryption-provider-config=/etc/kubernetes/enc/enc.yaml  # Add this line
      volumeMounts:
        # ... other mounts ...
        - name: enc
          mountPath: /etc/kubernetes/enc
          readOnly: true  # Add this line
  volumes:
    # ... other volumes ...
    - name: enc
      hostPath:
        path: /etc/kubernetes/enc
        type: DirectoryOrCreate  # Add this line
```

Keep in mind that anyone who can create Pods or Deployments in the same namespace could potentially access these Secrets. Use role-based access control (RBAC) to limit access effectively.

For additional protection, consider integrating third-party secret providers such as the AWS Provider, Azure Provider, GCP Provider, or Vault Provider. These external solutions store Secrets outside etcd and provide advanced security controls.

<Frame>
  ![The image provides guidelines on handling secrets, emphasizing encryption, access control, and considering third-party providers for secure storage.](https://kodekloud.com/kk-media/image/upload/v1752871656/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Manage-Kubernetes-secrets/frame_470.jpg)
</Frame>

## Conclusion

In this lesson, we covered the importance of managing sensitive data in Kubernetes using Secrets. We discussed both imperative and declarative methods to create Secrets, learned how to inject them into your Pods as environment variables or as files in a volume, and reviewed critical best practices along with encryption strategies. Practice these techniques to improve the security of your Kubernetes deployments and safeguard your sensitive data.

For more detailed information, explore the official [Kubernetes Documentation](https://kubernetes.io/docs/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/2cc1de3d-e070-4999-a083-0eb4ff7f8084" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/0f29d43a-a993-41fb-b58d-5c99f56c356a" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 OPA in Kubernetes
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/OPA-in-Kubernetes/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/OPA-in-Kubernetes/page)

# OPA in Kubernetes

> This article explores integrating OPA with Kubernetes using the Gatekeeper approach for enhanced policy enforcement and governance.

In this article, we explore the integration of OPA (Open Policy Agent) with Kubernetes using the Gatekeeper approach. This method leverages the OPA Constraint Framework alongside Kubernetes admission controllers for enhanced policy enforcement and governance.

<Frame>
  ![The image illustrates the OPA Constraint Framework, showing interactions between Kubernetes components, OPA, and Gatekeeper for policy enforcement and governance.](https://kodekloud.com/kk-media/image/upload/v1752871657/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-OPA-in-Kubernetes/frame_10.jpg)
</Frame>

With the Gatekeeper approach, the admission controller collaborates with the OPA Constraint Framework by using CRD-based (Custom Resource Definition) policies. This facilitates easier policy sharing and builds trust across your Kubernetes environment.

Before diving into the details of the OPA Constraint Framework, let’s review how to deploy OPA Gatekeeper in Kubernetes.

## Installing OPA Gatekeeper

Deploying OPA Gatekeeper is simple. Execute the following command to apply the Gatekeeper specification files:

```bash theme={null}
kubectl apply -f https://raw.githubusercontent.com/open-policy-agent/gatekeeper/v3.14.0/deploy/gatekeeper
```

After deployment, verify that all Gatekeeper components are installed and running in the `gatekeeper-system` namespace:

```bash theme={null}
kubectl get all -n gatekeeper-system
```

Expected output:

```bash theme={null}
NAME                                           READY   STATUS      RESTARTS   AGE
pod/gatekeeper-audit-6699999786d-6n8xt           1/1     Running     1          (12s ago)   31s
pod/gatekeeper-controller-manager-854f95df4f-dbhp7   1/1  Running     0          31s
pod/gatekeeper-controller-manager-854f95df4f-k96kj   1/1  Running     0          31s
pod/gatekeeper-controller-manager-854f95df4f-zfnbw   1/1  Running     0          31s

NAME                                          TYPE            CLUSTER-IP       EXTERNAL-IP    PORT(S)        AGE
service/gatekeeper-webhook-service            ClusterIP       172.20.60.127   <none>         443/TCP        31s

NAME                                          READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/gatekeeper-audit             1/1     1            1           31s
deployment.apps/gatekeeper-controller-manager  3/3     3            3           31s

NAME                                          DESIRED   CURRENT   READY   AGE
replicaset.apps/gatekeeper-audit-6699999786   1         1         1       31s
replicaset.apps/gatekeeper-controller-manager-854f95df4f   3         3         3       31s
```

<Callout icon="lightbulb" color="#1CB2FE">
  Ensure that you have adequate RBAC permissions before deploying Gatekeeper in your cluster.
</Callout>

## Understanding the OPA Constraint Framework

The OPA Constraint Framework allows you to declare policies that specify required conditions, enforce those conditions at the appropriate locations, and define the checks to be performed. For example, if you want all objects in a specific namespace (e.g., "example") to include a "billing" label, the framework will enforce this rule via the Kubernetes admission controller.

When a pod creation request is submitted, the admission controller follows these steps:

1. Retrieve the labels from the pod.
2. Verify if the required label (e.g., "billing") is present.
3. Return an error if the label is missing.

<Frame>
  ![The image outlines the OPA Constraint Framework, detailing requirements, enforcement location, and specification actions for Kubernetes admission control with namespace and label examples.](https://kodekloud.com/kk-media/image/upload/v1752871659/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-OPA-in-Kubernetes/frame_160.jpg)
</Frame>

## Implementing Label Validation with Rego

Below is an example of Rego code that validates the presence of a required label (e.g., "billing") on a pod. The code compares the provided labels with a hard-coded required label.

### Example 1

```rego theme={null}
package systemrequiredlabels

import data.lib.helpers

violation["msg": msg, "details": {"missing_labels": missing}} {
    provided := {label | input.request.object.metadata.labels[label]}
    required := {label | label == ["billing"]}
    missing = required - provided
    count(missing) > 0
    msg = sprintf("you must provide labels: %v", [missing])
}
```

### Example 2

A similar rule with a slightly different format:

```rego theme={null}
package systemrequiredlabels

import data.lib.helpers

violation["msg"] = msg {
    details := {"missing_labels": missing}
    provided := {label | input.request.object.metadata.labels[label]}
    required := {label | label := ["billing"]}
    missing = required - provided
    count(missing) > 0
    msg = sprintf("you must provide labels: %v", [missing])
}
```

### Example 3

An alternative format with syntactical differences:

```rego theme={null}
package systemrequiredlabels

import data.lib.helpers

violation["msg": msg, "details": {"missing_labels": missing}} {
    provided := {label | input.request.object.metadata.labels[label]}
    required := {label | label = ["billing"]}
    missing := required - provided
    count(missing) > 0
    msg = sprintf("you must provide labels: %v", [missing])
}
```

In these examples:

* The `provided` variable extracts labels from the incoming pod object.
* The `required` set is fixed to include "billing".
* The `missing` variable determines any labels from the `required` set that are absent.
* If any required labels are missing (`count(missing) > 0`), an error message is generated.

## Extending the Use Case with Parameterization

To support more dynamic scenarios—such as enforcing different labels based on the namespace—you can create a Constraint Template. This enables you to pass the required label as a parameter instead of hardcoding it.

Below is an example Constraint Template that encapsulates the Rego code while exposing a parameter for the required label:

```yaml theme={null}
apiVersion: templates.gatekeeper.sh/v1
kind: ConstraintTemplate
metadata:
  name: systemrequiredlabels
spec:
  crd:
    spec:
      names:
        kind: SystemRequiredLabel
      validation:
        # Schema for the 'parameters' field goes here
  targets:
    - target: admission.k8s.gatekeeper.sh
      rego: |
        package systemrequiredlabels

        import data.lib.helpers

        violation[{"msg": msg, "details": {"missing_labels": missing}}] {
          provided := {label | input.request.object.metadata.labels[label]}
          # Use the parameter passed in the constraint instead of hardcoding
          required := {label | label == input.parameters.labels[_]}
          missing = required - provided
          count(missing) > 0
          msg = sprintf("you must provide labels: %v", [missing])
        }
```

Once your Constraint Template is ready, define specific constraints to enforce policies for different namespaces. For instance:

### Constraint for Billing Label

```yaml theme={null}
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: SystemRequiredLabel
metadata:
  name: require-billing-label
spec:
  match:
    namespaces: ["expensive"]
  parameters:
    labels: ["billing"]
```

### Constraint for Tech Label

```yaml theme={null}
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: SystemRequiredLabel
metadata:
  name: require-tech-label
spec:
  match:
    namespaces: ["engineering"]
  parameters:
    labels: ["tech"]
```

These constraints dynamically pass the required labels via the `input.parameters` object in Rego based on the namespace.

## Summary

Below is a quick reference table summarizing the key steps for integrating OPA with Kubernetes using Gatekeeper:

| Step                        | Description                                              | Example Command/Definition                                         |
| --------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------ |
| Install OPA Gatekeeper      | Deploy Gatekeeper components using Kubernetes manifests. | `kubectl apply -f [Gatekeeper URL]`                                |
| Verify Deployment           | Check that all Gatekeeper components are running.        | `kubectl get all -n gatekeeper-system`                             |
| Validate Labels with Rego   | Use Rego code to compare provided and required labels.   | See provided Rego examples                                         |
| Create Constraint Template  | Define a CRD that accepts dynamic parameters for labels. | Provided YAML for Constraint Template                              |
| Define Constraint Resources | Enforce policies on specific namespaces with parameters. | Provided YAML for `require-billing-label` and `require-tech-label` |

<Callout icon="lightbulb" color="#1CB2FE">
  Any object creation that violates the defined policies will trigger an error during the admission phase, preventing non-compliant objects from being admitted into the cluster.
</Callout>

### Example Files

#### requiredlabels-template.yaml

```yaml theme={null}
apiVersion: templates.gatekeeper.sh/v1
kind: ConstraintTemplate
metadata:
  name: systemrequiredlabels
spec:
  crd:
    spec:
      names:
        kind: SystemRequiredLabel
      validation:
        # Schema for the 'parameters' field goes here
  targets:
    - target: admission.k8s.gatekeeper.sh
      rego: |
        package systemrequiredlabels

        import data.lib.helpers

        violation[{"msg": msg, "details": {"missing_labels": missing}}] {
          provided := {label | input.request.object.metadata.labels[label]}
          required := {label | label == input.parameters.labels[_]}
          missing = required - provided
          count(missing) > 0
          msg = sprintf("you must provide labels: %v", [missing])
        }
```

#### require-label-billing.yaml

```yaml theme={null}
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: SystemRequiredLabel
metadata:
  name: require-billing-label
spec:
  match:
    namespaces: ["expensive"]
  parameters:
    labels: ["billing"]
```

Apply these configurations with the following commands:

```bash theme={null}
kubectl apply -f requiredlabels-template.yaml
kubectl apply -f require-label-billing.yaml
# Output: Constraint require-billing-label created
```

With these steps in place, any new Kubernetes object that fails to meet the policy requirements will be rejected at admission time, ensuring continued compliance within your cluster.

That concludes our exploration of integrating OPA with Kubernetes using Gatekeeper. Experiment with these policies in your environment to tailor enforcement to your specific needs.

For further details on OPA and Kubernetes, consider visiting:

* [OPA Documentation](https://www.openpolicyagent.org/docs/)
* [Kubernetes Documentation](https://kubernetes.io/docs/)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/2e072033-de08-4375-84d4-cf8e8462169d" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/13a2b63a-24ac-4430-bc1f-42e03006412a" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 One way SSL vs Mutual SSL
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/One-way-SSL-vs-Mutual-SSL/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/One-way-SSL-vs-Mutual-SSL/page)

# One way SSL vs Mutual SSL

> This article explores the differences between one-way SSL and mutual TLS, focusing on their processes, security levels, and typical use cases.

In this article, we explore the basics of mTLS (mutual TLS) and compare it with one-way SSL. We dive into how TLS encrypts traffic between systems, explains the process of creating and using SSL certificates, and highlights their importance in securing web servers and SSH, among other applications. For example, when a customer accesses online banking without encryption, an attacker could intercept network traffic to obtain sensitive credentials. However, by leveraging TLS certificates, a secure HTTPS connection is established, protecting user data.

## One-way SSL

When a client connects to a bank’s website using one-way SSL:

1. The client receives the bank’s public certificate.
2. The web browser verifies the certificate by ensuring the certificate authority (CA) that signed it is trusted. Browsers maintain a trust store with trusted CA public keys.
3. The browser then uses the bank’s public certificate to encrypt a symmetric key, which is sent securely to the bank.
4. The bank decrypts the symmetric key using its private key.

This process uses asymmetric encryption initially to securely share a symmetric key. Once the symmetric key is established, both the client and the bank use it to encrypt and decrypt the data exchanged in their communication. In one-way SSL, only the client verifies the server’s certificate. The bank does not authenticate the client certificate; it instead relies on additional credentials (such as username, password, or client number) to confirm the user's identity.

<Callout icon="lightbulb" color="#1CB2FE">
  One-way SSL is widely used for internet-based services like email accounts, social media, and online banking where verifying the server's authenticity is the primary concern.
</Callout>

## Mutual TLS (mTLS)

Consider a scenario where no human user is entering credentials—imagine two organizations exchanging confidential information. For instance, suppose mybank.com (acting as a client) needs to retrieve data from the server abc-financials. In this case, it is essential for the server to verify that the request comes from the legitimate mybank.com. This is where mutual TLS comes into play.

When using mTLS, both parties authenticate each other. Here is how the process works when mybank.com (client) requests data from abc-financials (server):

1. The client requests the server’s public certificate.
2. The server responds with its public certificate and simultaneously requests the client’s certificate.
3. The client verifies the server’s certificate using the CA’s public keys from its trust store.
4. After successful verification, the client sends its certificate to the server along with a symmetric key encrypted with the server’s public key.
5. The server validates the client’s certificate using the CA to ensure it belongs to mybank.com.

Once both parties have mutually authenticated, they use the shared symmetric key to encrypt all subsequent communications, ensuring that data exchange remains secure.

<Callout icon="lightbulb" color="#1CB2FE">
  Mutual TLS is especially beneficial in scenarios where automated systems or organizations need to exchange data securely, as it provides strong authentication on both ends.
</Callout>

## Summary

The following table summarizes the key differences between one-way SSL and mutual TLS:

| Feature                  | One-way SSL                                                     | Mutual TLS                                                  |
| ------------------------ | --------------------------------------------------------------- | ----------------------------------------------------------- |
| Certificate verification | Only the server's certificate is verified by the client         | Both client and server certificates are verified            |
| Typical use cases        | Web services (online banking, email, social media)              | Automated system-to-system communication (B2B data sharing) |
| Security level           | Secure communication; user authentication is handled separately | Enhanced security with mutual authentication                |

This concludes our exploration of one-way SSL and mutual TLS. For further reading on securing pod-to-pod communications in Kubernetes clusters and implementing mTLS, consider the following resources:

* [Kubernetes Basics](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Docker Hub](https://hub.docker.com/)
* [Terraform Registry](https://registry.terraform.io/)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/e186af38-c267-427e-a3ae-cd849fb451aa" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Open Policy Agent OPA
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Open-Policy-Agent-OPA/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Open-Policy-Agent-OPA/page)

# Open Policy Agent OPA

> This lesson introduces Open Policy Agent (OPA) for managing authorization in a web service scenario using a simple Flask application.

In this lesson, we dive into Open Policy Agent (OPA) by examining a straightforward web service scenario and demonstrating how OPA can manage authorization. We focus on plain OPA without using Docker or Kubernetes, making it easy to understand the core concepts.

Imagine a web service where users place orders for products. The service must be secure: communications between the user and the web portal are both authenticated and authorized. Authentication confirms the user’s identity (e.g., via usernames/passwords or certificates), while authorization controls what an authenticated user is permitted to do—such as viewing past orders or placing new ones.

<Frame>
  ![The image illustrates a flowchart with "OPA" text, showing a user accessing a web service through authentication and authorization processes.](https://kodekloud.com/kk-media/image/upload/v1752871659/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Open-Policy-Agent-OPA/frame_70.jpg)
</Frame>

Below, we first demonstrate a basic Python-based Flask application without any authorization. Next, we incorporate basic authorization within Flask. Finally, we integrate OPA to provide a robust and flexible authorization solution.

***

## A Simple Flask Application Without Authorization

Consider this basic Flask application which serves the "/home" endpoint and returns a welcome message:

```python theme={null}
@app.route('/home')
def hello_world():
    return 'Welcome Home!', 200
```

In this initial version, there is no authorization in place, meaning the endpoint is accessible to anyone.

***

## Adding Basic Authorization in Flask

To add a simple layer of authorization, we check if the user is "john". In this example, the username is provided as a URL parameter:

```python theme={null}
@app.route('/home')
def hello_world():
    user = request.args.get("user")
    if user != "john":
        return 'Unauthorized!', 401
    return 'Welcome Home!', 200
```

While this manual check works for a single case, it quickly becomes unmanageable as the number of users, groups, and roles grows—especially in environments where multiple programming languages are used.

***

## Introducing OPA for Scalable Authorization

To overcome the complexities of distributed authorization, OPA can be deployed as a centralized policy decision point. With OPA, you define policies in a single location that all services can query via an API to determine access permissions.

### Deploying the OPA Server

Begin by downloading the OPA binary, making it executable, and starting the OPA server using the `-s` flag. By default, OPA listens on port 8181 and has an open API without built-in authentication or authorization:

```bash theme={null}
curl -L -o opa https://github.com/open-policy-agent/opa/releases/download/v0.11.0/opa_linux_amd64
chmod 755 ./opa
./opa run -s
{"addrs":["8181"],"insecure_addr":"","level":"info","msg":"First line of log stream.","time":"2021-03-18T20:25:38+08:00"}
```

<Callout icon="lightbulb" color="#1CB2FE">
  By default, OPA’s API is open, so it is advisable to implement proper network security measures in production environments.
</Callout>

***

### Defining an Authorization Policy with Rego

OPA policies are authored in Rego and stored in files with the `.rego` extension. Below is an example policy that permits access to the `/home` endpoint only if the user is "john":

```rego theme={null}
package httpapi.authz

# HTTP API request
import input

default allow = false

allow {
    input.path == "home"
    input.user == "john"
}
```

To load this policy into OPA, use a PUT request:

```bash theme={null}
curl -X PUT --data-binary @example.rego http://localhost:8181/v1/policies/example1
```

To list all existing policies, run:

```bash theme={null}
curl http://localhost:8181/v1/policies
```

***

### Integrating OPA with the Python Application

Instead of embedding the authorization check within your application code, you can now delegate it to the OPA server. The updated Flask application builds an input dictionary and sends it as JSON to the OPA API. The appropriate query endpoint for our policy package, `httpapi.authz`, is `/v1/data/httpapi/authz`.

```python theme={null}
@app.route('/home')
def hello_world():
    user = request.args.get("user")
    input_dict = {
        "input": {
            "user": user,
            "path": "home"
        }
    }
    rsp = requests.post("http://127.0.0.1:8181/v1/data/httpapi/authz", json=input_dict)
    if not rsp.json()["result"]["allow"]:
        return 'Unauthorized!', 401
    return 'Welcome Home!', 200
```

With this implementation, the Flask application offloads the authorization decision to OPA, which evaluates the input against its policies and responds with a decision.

***

### Experimenting with Rego in the Playground

OPA offers an interactive Rego playground at [play.openpolicyagent.org](https://play.openpolicyagent.org), where you can experiment with writing and testing policies. The playground allows you to work with structured input data and refine your policies on the fly.

For instance, given the input:

```json theme={null}
{
    "user": "john",
    "path": "home"
}
```

The policy will return:

```json theme={null}
{
    "allow": true
}
```

Check out the playground to experiment with more complex policies and inputs.

***

### Testing Your OPA Policies

OPA includes a built-in testing framework that allows you to run tests using Rego test files. Below is an example test file for an authorization policy:

```rego theme={null}
package authz

test_post_allowed {
    allow with input as {"path": ["users"], "method": "POST"}
}

test_get_anonymous_denied {
    not allow with input as {"path": ["users"], "method": "GET"}
}

test_get_user_allowed {
    allow with input as {"path": ["users", "bob"], "method": "GET", "user_id": "bob"}
}

test_get_another_user_denied {
    not allow with input as {"path": ["users", "bob"], "method": "GET", "user_id": "alice"}
}
```

Execute the tests with the following command:

```bash theme={null}
$ opa test -v
data.authz.test_post_allowed: PASS (1.417µs)
data.authz.test_get_anonymous_denied: PASS (426ns)
data.authz.test_get_user_allowed: PASS (367ns)
data.authz.test_get_another_user_denied: PASS (320ns)
-----------------------------------------------------------
PASS: 4/4
```

<Callout icon="lightbulb" color="#1CB2FE">
  Using OPA's testing framework ensures that your policies perform as expected before deploying them into production.
</Callout>

***

<Frame>
  ![The image describes Rego, a policy language used in OPA for querying structured documents, inspired by Datalog, and emphasizes its readability and declarative nature.](https://kodekloud.com/kk-media/image/upload/v1752871660/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Open-Policy-Agent-OPA/frame_480.jpg)
</Frame>

***

## Conclusion

This lesson provided an introduction to OPA by starting with a simple Flask application, adding basic in-code authorization, and finally migrating to a centralized authorization model using OPA. We explored how to author policies in Rego, load them into OPA, integrate policy queries into your application, and test your policies using OPA’s testing framework.

In future lessons, we will explore how OPA integrates with Kubernetes and delve into more advanced use cases. Practice with OPA to gain a deeper understanding of centralized authorization—happy coding!

For additional resources and further reading, explore:

* [Open Policy Agent Documentation](https://www.openpolicyagent.org/docs/)
* [Rego Language Guide](https://www.openpolicyagent.org/docs/latest/policy-language/)
* [Flask Documentation](https://flask.palletsprojects.com/)
* [Python Requests Library](https://docs.python-requests.org/)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/ec830ff8-68a1-48de-b113-7f588bacdf7c" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/eecb8373-8a36-4008-871e-afd5dbf59b23" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Overview of Multi Tenancy in Kubernetes
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Overview-of-Multi-Tenancy-in-Kubernetes/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Overview-of-Multi-Tenancy-in-Kubernetes/page)

# Overview of Multi Tenancy in Kubernetes

> This article explores multi-tenancy in Kubernetes, focusing on user isolation, security, and resource management within a shared cluster environment.

In this article, we explore multi-tenancy in Kubernetes and demonstrate how the platform enables multiple users, tenants, or customers to share a single cluster while ensuring strong isolation, security, and efficient resource management. You will learn about various approaches such as namespace isolation, resource quotas, network policies, and storage isolation, which help maintain fairness and security among tenants sharing the same infrastructure. This concept is especially relevant in SaaS environments where multiple customers use a single cluster.

<Frame>
  ![The image shows an agenda listing topics: Multi-Tenancy, Namespace Isolation, Resource Quotas, Network Policies, and Storage Isolation.](https://kodekloud.com/kk-media/image/upload/v1752871661/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Overview-of-Multi-Tenancy-in-Kubernetes/frame_10.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Think of a large office building representing your Kubernetes cluster. Each floor, analogous to a namespace, provides a distinct environment for different teams, companies, or customers. Shared common areas such as elevators and parking lots are like cluster-wide resources (networking, storage, and nodes) that require careful management to ensure balanced use.
</Callout>

One common anti-pattern in Kubernetes is provisioning a separate cluster for each tenant or application. Although this might seem like an effective way to isolate teams or applications, it quickly becomes unsustainable as the number of tenants increases. Managing multiple clusters—each with its individual resources, security policies, and configurations—introduces significant complexity and operational overhead.

To illustrate, imagine that each floor of a multi-story building (Kubernetes namespace) is used by a different tenant. Even though the building (cluster) is shared, strict controls such as access badges (Kubernetes RBAC) and designated facilities (network policies, storage limitations) ensure that no single tenant monopolizes resources or compromises security.

<Frame>
  ![The image explains "What is Tenant?" in Kubernetes, highlighting access control, security, and shared facilities like cluster resources, using icons and a building metaphor.](https://kodekloud.com/kk-media/image/upload/v1752871663/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Overview-of-Multi-Tenancy-in-Kubernetes/frame_120.jpg)
</Frame>

Kubernetes multi-tenancy is all about providing isolated environments within a common infrastructure. This is particularly important for cloud-native applications, where compute, storage, and networking resources need to be shared efficiently and securely among various users and teams.

<Frame>
  ![The image illustrates a Kubernetes cluster with multi-tenancy, showing isolated environments for different teams across nodes, utilizing shared compute, storage, and network resources.](https://kodekloud.com/kk-media/image/upload/v1752871664/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Overview-of-Multi-Tenancy-in-Kubernetes/frame_140.jpg)
</Frame>

<Callout icon="triangle-alert" color="#FF6B6B">
  Without robust isolation mechanisms, unauthorized data access or resource contention might occur. Overconsumption of resources by one tenant can impact the performance and stability of the overall system. Always enforce strict isolation and monitoring to avoid these pitfalls.
</Callout>

Implementing multi-tenancy comes with its challenges. It is essential to set up strong isolation mechanisms to prevent data leakage between tenants and ensure that one tenant’s workload does not adversely affect others. As the number of tenants increases, managing security policies, access controls, and resource allocations becomes more complex, all while adhering to regulatory requirements and safeguarding data privacy and sovereignty.

The advantages of a multi-tenant architecture in Kubernetes are substantial. By sharing a single cluster, organizations can maximize resource utilization and reduce both hardware and operational costs. Here’s a quick look at the benefits:

| Benefit                 | Description                                                                                              |
| ----------------------- | -------------------------------------------------------------------------------------------------------- |
| Cost Efficiency         | Reduced hardware and operational expenses by eliminating the need for separate clusters.                 |
| Enhanced Resource Usage | Better utilization of compute, storage, and network resources across multiple tenants.                   |
| Simplified Management   | Centralized control simplifies operational management, monitoring, and troubleshooting.                  |
| Robust Security         | Isolation mechanisms like namespaces, RBAC, and network policies prevent interference and data breaches. |

<Frame>
  ![The image illustrates the advantages of multi-tenancy in Kubernetes, highlighting isolated environments, cost savings, and features like namespaces, RBAC, and network policies, while addressing complexity and compliance.](https://kodekloud.com/kk-media/image/upload/v1752871665/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Overview-of-Multi-Tenancy-in-Kubernetes/frame_220.jpg)
</Frame>

In summary, multi-tenancy in Kubernetes allows multiple teams or users to safely share the same underlying infrastructure while maintaining strong isolation and efficient resource management. In the upcoming lessons, we will dive deeper into the specifics of namespaces, RBAC, network policies, and other techniques that form the backbone of multi-tenant environments in Kubernetes.

For additional insights on Kubernetes usage and best practices, consider exploring the following resources:

* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Kubernetes Basics](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
* [Docker Hub](https://hub.docker.com/)
* [Terraform Registry](https://registry.terraform.io/)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/d0e9f6b4-246e-4d88-bd04-afdc00afad40" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Pod Security Admission and Pod Security Standards
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Pod-Security-Admission-and-Pod-Security-Standards/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Pod-Security-Admission-and-Pod-Security-Standards/page)

# Pod Security Admission and Pod Security Standards

> This article explores Pod Security Admission and Pod Security Standards in Kubernetes, detailing their implementation, profiles, and configuration for enhanced security.

In this article, we explore Pod Security Admission (PSA) and Pod Security Standards as defined in Kubernetes Enhancement Proposal KEP-2579. PSA is designed to replace Pod Security Policies (PSP) with a solution that is safe to enable on new clusters, easy to use, and highly extensible. This approach meets several key requirements outlined in the proposal.

<Frame>
  ![The image lists pod security requirements, including validation, safety, built-in controller, Windows support, API responsiveness, ease of use, and extensibility, related to KEP 2579 PSP Replacement.](https://kodekloud.com/kk-media/image/upload/v1752871666/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Pod-Security-Admission-and-Pod-Security-Standards/frame_20.jpg)
</Frame>

The new implementation prioritizes simplicity and safety. Advanced or custom configurations can still be managed by third-party solutions such as KRAIL, Kyverno, or OPA Gatekeeper.

PSA operates as an Admission Controller and is enabled by default in Kubernetes clusters. To verify its activation, run the following command to display the enabled admission plugins in the kube-apiserver:

```bash theme={null}
kubectl exec -n kube-system kube-apiserver-controlplane -it -- kube-apiserver -h | grep enable-admission-plugins
```

Since PSA is active by default, no extra steps are required to enroll it. Simply run the above command within the kube-apiserver pod and search for entries related to pod security to confirm its configuration.

PSA is applied at the namespace level by using specific labels. For example, to enforce Pod Security Standards on a namespace named "payroll", add the appropriate pod security settings to that namespace by specifying a mode and a security policy.

<Callout icon="lightbulb" color="#1CB2FE">
  There are three built-in profiles provided by the Pod Security Standards:

  * **Privileged**: Offers nearly no restrictions, allowing extensive permissions and potential privilege escalation.
  * **Baseline**: Balances security and functionality by preventing unauthorized privilege escalation while supporting most containerized applications.
  * **Restricted**: Implements strict security measures based on pod hardening best practices, ensuring high security at the cost of potential compatibility challenges.
</Callout>

A mode determines the action taken when a policy violation occurs. The available modes are:

* **enforce**: Rejects pod creation requests that do not comply with the specified policy.
* **audit**: Allows pod creation but logs the policy violation in the audit logs.
* **warn**: Permits pod creation and issues a warning to the user regarding the policy violation.

<Frame>
  ![The image explains configuring PSA with modes (enforce, audit, warn) and profiles (Privileged, Baseline, Restricted), detailing actions on violations and policy descriptions.](https://kodekloud.com/kk-media/image/upload/v1752871667/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Pod-Security-Admission-and-Pod-Security-Standards/frame_160.jpg)
</Frame>

For instance, if you label a namespace to "enforce" the restricted policy, any pod that fails to meet the strict criteria will be refused. Conversely, setting the mode to "warn" under the restricted profile will allow pod deployment but alert the user with a warning.

The baseline profile is optimized for most containerized applications by preventing unauthorized elevated access. For further details on the restrictions applied by this profile, refer to the [Kubernetes Pod Security Standards documentation](https://kubernetes.io/docs/concepts/security/pod-security-standards/).

<Frame>
  ![The image shows a "Baseline Profile" for Kubernetes security, detailing policies and restrictions for host processes, namespaces, privileged containers, and more.](https://kodekloud.com/kk-media/image/upload/v1752871669/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Pod-Security-Admission-and-Pod-Security-Standards/frame_230.jpg)
</Frame>

In contrast, the restricted profile applies the latest security best practices. Although this may lead to compatibility challenges, it ensures a robust security posture.

<Frame>
  ![The image outlines Kubernetes pod security standards for a "Restricted Profile," detailing policies on volume types, privilege escalation, non-root user requirements, and capabilities.](https://kodekloud.com/kk-media/image/upload/v1752871670/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Pod-Security-Admission-and-Pod-Security-Standards/frame_250.jpg)
</Frame>

In our example setup, we demonstrate different security configurations across namespaces:

| Namespace | Mode    | Profile    | Description                                                             |
| --------- | ------- | ---------- | ----------------------------------------------------------------------- |
| payroll   | enforce | restricted | Pods must strictly adhere to the restricted policy.                     |
| hr        | enforce | baseline   | Pods are expected to follow baseline security practices.                |
| dev       | warn    | restricted | Pods receive warnings if they do not comply with the restricted policy. |

The commands to label the respective namespaces are as follows:

```bash theme={null}
kubectl label ns payroll pod-security.kubernetes.io/enforce=restricted
kubectl label ns hr pod-security.kubernetes.io/enforce=baseline
kubectl label ns dev pod-security.kubernetes.io/warn=restricted
```

This configuration ensures that pods within the "payroll" namespace are strictly enforced under the restricted policy, pods in the "hr" namespace adhere to baseline security practices, and pods in the "dev" namespace trigger warnings for violations under the restricted policy.

<Callout icon="lightbulb" color="#1CB2FE">
  We encourage you to experiment with Pod Security Admission and Pod Security Standards to better understand how they enhance security in Kubernetes clusters. For additional information, visit the [Kubernetes Documentation](https://kubernetes.io/docs/).
</Callout>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/f83417e1-f0a2-4aa2-a2a0-348f72a0271d" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Pod Security Policies
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Pod-Security-Policies/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Pod-Security-Policies/page)

# Pod Security Policies

> This article explores pod security in Kubernetes, focusing on Pod Security Policies and their role in restricting insecure configurations.

In this lesson, we explore pod security in Kubernetes by examining a sample pod definition and discussing how Pod Security Policies (PSPs) were used to restrict insecure configurations. Although PSPs have been deprecated in favor of Pod Security Admission and Pod Security Standards (available since Kubernetes 1.25), understanding PSPs is still useful—especially when working with legacy clusters.

***

## Sample Pod Definition

Below is a sample pod definition that creates a pod running an Ubuntu container. The configuration includes permissive settings often unsuitable for production environments:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: sample-pod
spec:
  containers:
    - name: ubuntu
      image: ubuntu
      command: ["sleep", "3600"]
      securityContext:
        privileged: True
        runAsUser: 0
        capabilities:
          add: ["CAP_SYS_BOOT"]
  volumes:
    - name: data-volume
      hostPath:
        path: /data
        type: Directory
```

In this pod:

* The `privileged` flag is set to `True`, granting container processes elevated privileges.
* The container runs as root (`runAsUser: 0`).
* It adds specific capabilities like `CAP_SYS_BOOT`.
* A HostPath volume is used, exposing part of the host’s filesystem.

These settings can introduce security vulnerabilities. To safeguard your cluster, it is important to enforce policies that restrict such configurations.

***

## The Role of Pod Security Policies

Pod Security Policies were designed to validate pod creation requests against a set of pre-configured security rules. When the PSP admission controller is enabled, it intercepts pod creation requests and rejects those that do not comply with the defined policies. For example, a pod configured with the `privileged` flag set to `True` can be denied by an appropriately configured PSP.

<Callout icon="lightbulb" color="#1CB2FE">
  When a violation is detected, the system rejects the pod creation request and returns an error message, preventing insecure pods from running.
</Callout>

***

## Enabling PSP on the API Server

PSP functions as an Admission Controller. To enable it, add the `PodSecurityPolicy` plugin to the API server’s list of admission plugins. An example snippet from the API server’s startup command is shown below:

```text theme={null}
ExecStart=/usr/local/bin/kube-apiserver \
  --advertise-address=${INTERNAL_IP} \
  --allow-privileged=true \
  --apiserver-count=3 \
  --authorization-mode=Node,RBAC \
  --bind-address=0.0.0.0 \
  --enable-swagger-ui=true \
  --etcd-servers=https://127.0.0.1:2379 \
  --event-ttl=1h \
  --runtime-config=api/all \
  --service-cluster-ip-range=10.32.0.0/24 \
  --service-node-port-range=30000-32767 \
  --v=2 \
  --enable-admission-plugins=PodSecurityPolicy
```

Similarly, here’s an excerpt from the API server pod definition that confirms the admission plugin is enabled:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  name: kube-apiserver
  namespace: kube-system
spec:
  containers:
    - command:
        - kube-apiserver
        - --authorization-mode=Node,RBAC
        - --advertise-address=172.17.0.107
        - --allow-privileged=true
        - --enable-bootstrap-token-auth=true
        - --enable-admission-plugins=PodSecurityPolicy
      image: k8s.gcr.io/kube-apiserver-amd64:v1.11.3
      name: kube-apiserver
```

Once the admission controller is activated, every pod creation request is validated against the PSP rules.

***

## Defining a Pod Security Policy

To enforce security, you can create a PSP that, for instance, disallows pods with the privileged flag enabled. Start by reviewing the original pod definition for context:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: sample-pod
spec:
  containers:
    - name: ubuntu
      image: ubuntu
      command: ["sleep", "3600"]
      securityContext:
        privileged: True
        runAsUser: 0
        capabilities:
          add: ["CAP_SYS_BOOT"]
  volumes:
    - name: data-volume
      hostPath:
        path: /data
        type: Directory
```

Now, define a Pod Security Policy that disallows privileged containers:

```yaml theme={null}
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: example-psp
spec:
  privileged: false
```

This basic PSP will reject any pod creation request that tries to run a container with the `privileged` flag.

You can further customize the policy to enforce stricter measures. For instance, the following definition disallows running as root, mandates dropping the `CAP_SYS_BOOT` capability, adds a default capability, and only permits specific volume types:

```yaml theme={null}
# pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: sample-pod
spec:
  containers:
    - name: ubuntu
      image: ubuntu
      command: ["sleep", "3600"]
      securityContext:
        privileged: True
        runAsUser: 0
        capabilities:
          add: ["CAP_SYS_BOOT"]
  volumes:
    - name: data-volume
      hostPath:
        path: /data
        type: Directory
---
# psp.yaml
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: example-psp
spec:
  privileged: false
  seLinux:
    rule: RunAsAny
  supplementalGroups:
    rule: RunAsAny
  runAsUser:
    rule: MustRunAsNonRoot
  requiredDropCapabilities:
    - CAP_SYS_BOOT
  defaultAddCapabilities:
    - CAP_SYS_TIME
  volumes:
    - persistentVolumeClaim
```

<Callout icon="lightbulb" color="#1CB2FE">
  It is important to understand that while PSPs can add default values to pod definitions, the new Pod Security Admission and Pod Security Standards do not support this mutating behavior.
</Callout>

***

## How the Admission Controller Works

When a pod creation request is submitted, the PSP admission controller:

* Queries all available Pod Security Policy objects.
* Validates the pod against the defined rules.
* Denies requests that conflict with the established policies (e.g., a pod using a disallowed `privileged` flag).

If the PSP admission controller is enabled without the proper PSP objects and roles, all pod creation requests may be blocked. This scenario emphasizes the need for correctly defined policies and associated Role and RoleBinding configurations.

For pods to access a PSP, they must be associated with a Service Account. By default, the `default` Service Account is used if none is specified. Then, you need to create a Role and RoleBinding to grant the Service Account permission to use the specific PSP. For example:

```yaml theme={null}
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: psp-example-role
rules:
  - apiGroups: ["policy"]
    resources: ["podsecuritypolicies"]
    resourceNames: ["example-psp"]
    verbs: ["use"]
```

```yaml theme={null}
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: psp-example-rolebinding
subjects:
  - kind: ServiceAccount
    name: default
    namespace: default
roleRef:
  kind: Role
  name: psp-example-role
  apiGroup: rbac.authorization.k8s.io
```

With these permissions in place, any pod creation request that fails to meet the PSP criteria is denied by the admission controller.

***

## Summary and Challenges

To summarize:

* Pod Security Policies validate and potentially modify pod definitions based on strict security rules.
* Enabling PSPs requires changes both at the API server level (by enabling the admission controller) and at the cluster level (by creating the necessary PSP objects and RBAC permissions).
* An incomplete setup can result in the unintentional denial of all pod creation requests.
* Binding PSP access to specific Service Accounts might interfere with the functionality of controllers (like Deployments) if not correctly configured.

<Callout icon="triangle-alert" color="#FF6B6B">
  Due to the complexities and effort required to manage PSP configurations, they were deprecated in Kubernetes 1.21 and removed entirely in 1.25. The newer Pod Security Admission and Pod Security Standards provide a more streamlined approach to securing your cluster.
</Callout>

<Frame>
  ![The image outlines Kubernetes pod security, mentioning Pod Security Policy (deprecated), Pod Security Admission, and Pod Security Standards.](https://kodekloud.com/kk-media/image/upload/v1752871671/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Pod-Security-Policies/frame_530.jpg)
</Frame>

We will further explore the Pod Security Admission mechanism and explain how it simplifies securing your Kubernetes environment.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/a2615821-9959-462d-8869-080fb902705b" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Pod to Pod Encryption
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Pod-to-Pod-Encryption/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Pod-to-Pod-Encryption/page)

# Pod to Pod Encryption

> Pod-to-pod encryption in Kubernetes secures communication between pods, ensuring data confidentiality and integrity, especially in multi-tenant environments.

Pod-to-pod encryption is a critical security measure in Kubernetes clusters. It ensures that communication between pods—whether within the same namespace or across different namespaces—is encrypted, maintaining the confidentiality and integrity of transmitted data. This security mechanism is especially vital in multi-tenant environments where sensitive data flows between services.

Imagine an e-commerce application deployed on Kubernetes with two main components: a front-end pod that manages customer orders and a back-end pod that processes payment information. When a customer places an order, the front-end pod sends sensitive payment details, including credit card information, to the back-end pod. Without encryption, an attacker could intercept this communication during a man-in-the-middle attack, leading to a potential data breach.

<Callout icon="lightbulb" color="#1CB2FE">
  Enabling pod-to-pod encryption ensures that even if data is intercepted, it remains unreadable and tamper-proof because it is securely encrypted.
</Callout>

<Frame>
  ![The image illustrates pod-to-pod encryption within a Kubernetes cluster, showing secure communication between frontend and backend components.](https://kodekloud.com/kk-media/image/upload/v1752871671/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Pod-to-Pod-Encryption/frame_70.jpg)
</Frame>

Encrypting data in transit not only protects against eavesdropping and interception but also helps organizations meet compliance standards such as GDPR and HIPAA. This encryption mitigates insider threats by securing internal communications and supports the zero-trust security model—where every connection is considered untrusted until verified. In this way, pod-to-pod encryption reinforces the overall security posture of your Kubernetes cluster without introducing significant operational complexity.

Automated key management provided by Kubernetes-native tools further simplifies the encryption process. This ease of management is crucial in multi-tenant environments where numerous tenants may share the same network infrastructure. In cloud-native scenarios, where traditional network boundaries are blurred, pod-to-pod encryption becomes indispensable for securing communications.

<Frame>
  ![The image lists reasons for pod-to-pod encryption, including data security, compliance, insider threat mitigation, zero-trust, MITM prevention, confidentiality, enhanced security, key management, communication security, and cloud adaptability.](https://kodekloud.com/kk-media/image/upload/v1752871673/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Pod-to-Pod-Encryption/frame_150.jpg)
</Frame>

There are several methods to implement pod-to-pod encryption:

* **Mutual TLS (mTLS):** Commonly implemented via service meshes like Istio or Linkerd.
* **Cilium Encryption:** Utilizes IPsec or WireGuard protocols.
* **Calico Encryption:** Leverages IPsec for secure communication.

Each method offers its own advantages depending on the specific requirements of your environment. Detailed discussions, especially regarding Cilium encryption, highlight the flexibility and robustness of these solutions.

<Frame>
  ![The image lists methods for implementing pod-to-pod encryption: Mutual TLS (mTLS), Cilium, and Calico.](https://kodekloud.com/kk-media/image/upload/v1752871674/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Pod-to-Pod-Encryption/frame_180.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Implementing pod-to-pod encryption is a key best practice for securing Kubernetes deployments. It not only safeguards sensitive data against external attacks but also reinforces trust in internal communications.
</Callout>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/e01226b6-c183-4049-85a5-866f0015f4fa" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Quality of Service
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Quality-of-Service/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Quality-of-Service/page)

# Quality of Service

> This article explores how Kubernetes implements Quality-of-Service to manage resource allocation and ensure fair distribution among tenants in multi-tenant environments.

In this article, we explore how Kubernetes implements Quality-of-Service (QoS) to manage resource allocation and ensure fair distribution of resources among tenants in multi-tenant environments. Kubernetes organizes pods into distinct QoS classes based on their resource requests and limits, which guarantees predictable resource availability while preventing any single tenant from monopolizing cluster resources.

Below, we detail several scenarios that illustrate the different QoS classes in Kubernetes.

***

## Guaranteed QoS

Pods receive the Guaranteed QoS classification when both CPU and memory requests and limits are set to identical values. With this configuration, Kubernetes guarantees that the pod always has the specified resources. The pod will not be evicted unless the host node experiences instability.

For example, consider a pod in namespace A running mission-critical production workloads:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: critical-app
  namespace: namespace-a
spec:
  containers:
    - name: critical-container
      image: nginx
      resources:
        requests:
          memory: "500Mi"
          cpu: "500m"
        limits:
          memory: "500Mi"
          cpu: "500m"
```

In this configuration, both the requests and limits for memory and CPU are identical (500Mi and 500m, respectively), ensuring that the pod has a fixed allocation of resources.

***

## Burstable QoS

Pods that set resource requests to values lower than their limits belong to the Burstable QoS class. This configuration guarantees a minimum level of resources while allowing the pod to burst beyond that level if additional resources are available. This is particularly useful for workloads that can tolerate variability in resource consumption.

For instance, consider a pod in namespace B running burstable, less critical workloads:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: burstable-app
  namespace: namespace-b
spec:
  containers:
    - name: burstable-container
      image: nginx
      resources:
        requests:
          memory: "200Mi"
          cpu: "200m"
        limits:
          memory: "16Gi"
          cpu: "1"
```

Here, the pod is guaranteed a minimum of 200Mi memory and 200m CPU but can scale up to 16Gi memory and 1 CPU if additional resources are available.

***

## Best-Effort QoS

Pods that do not specify any resource requests or limits fall under the Best-Effort QoS class. These pods do not benefit from guaranteed resources and will only consume resources when they are available. Under high resource pressure, Best-Effort pods are the first candidates to be evicted.

This QoS class is generally appropriate for development and testing workloads where resource guarantees are less critical.

***

## Network QoS

Although Kubernetes does not provide network QoS directly, it can be implemented using Container Network Interface (CNI) plugins such as Calico, or by leveraging Linux traffic control. Network QoS manages the network bandwidth usage of pods, which is essential when tenants have differing network performance requirements.

For example, a network policy implemented with Calico for namespace A might look like this:

```yaml theme={null}
apiVersion: crd.projectcalico.org/v1
kind: NetworkPolicy
metadata:
  name: tenant-a-network-policy
  namespace: namespace-a
spec:
  selector: all()  # Apply to all pods in Namespace A
  ingress:
    - action: Allow
      protocol: TCP
      destination:
        ports: [80]
      limits:
        rate: 10Mbps  # Limit ingress traffic to 10Mbps for tenant pods
  egress:
    - action: Allow
      protocol: TCP
      destination:
        ports: [80]
      limits:
        rate: 10Mbps  # Limit egress traffic to 10Mbps for tenant pods
```

<Callout icon="lightbulb" color="#1CB2FE">
  This network policy sets a maximum bandwidth limit of 10 Mbps, which is well-suited for production workloads such as streaming applications. For development environments (for example, in namespace B), you might enforce stricter bandwidth limits, such as 1 Mbps.
</Callout>

***

## Storage QoS

Storage QoS governs the number of I/O operations a pod can perform on its volumes. This is critical for workloads like databases that require high disk performance. Kubernetes indirectly supports storage QoS using storage classes and the underlying QoS features provided by your storage platform.

For a high-performance database workload in namespace A, you might use a StorageClass configured for high IOPS:

```yaml theme={null}
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: high-performance
provisioner: kubernetes.io/aws-ebs
parameters:
  type: io1            # AWS io1 disks support high IOPS
  iopsPerGB: "50"      # Specify high IOPS per GB
  fsType: ext4
reclaimPolicy: Delete
allowVolumeExpansion: true
volumeBindingMode: Immediate
```

In contrast, namespace B, which may run development workloads, could use a standard storage class with lower IOPS that is adequate for general-purpose applications.

***

## Summary

Kubernetes QoS classes—Guaranteed, Burstable, Best-Effort, Network, and Storage QoS—play a crucial role in managing resource allocation in a multi-tenant environment. These mechanisms ensure that critical workloads receive the resources they need while permitting less critical workloads to access additional resources when available.

For further details, see the [Kubernetes Documentation](https://kubernetes.io/docs/) and explore additional resources on resource management and scheduling to optimize your Kubernetes clusters.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/0c380fce-cff1-4913-8dcf-26f5ac3a6b8e" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Section Introduction
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Section-Introduction/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Section-Introduction/page)

# Section Introduction

> This article explores techniques and best practices for mitigating microservice vulnerabilities in Kubernetes environments, focusing on security enhancements and policy management.

Welcome to this lesson on mitigating microservice vulnerabilities. In this article, we explore advanced techniques and best practices aimed at strengthening your Kubernetes environment. We begin by examining Admission Controllers and their pivotal role in enhancing cluster security.

Previously, we set up a robust cluster environment and discussed hardening techniques, including authorization and authentication strategies. Now, we delve into how Admission Controllers work hand in hand with Pod Security Policies to provide an additional layer of defense.

Next, we introduce the Open Policy Agent (OPA). This section explains OPA's functionality and its critical importance in enforcing security policies within your Kubernetes clusters. We will walk you through deploying OPA in a Kubernetes environment, ensuring you have a solid foundation for policy management.

<Callout icon="lightbulb" color="#1CB2FE">
  Always test security configurations in a staging environment before deploying them in production.
</Callout>

Following the discussion on OPA, the article covers best practices for managing Kubernetes secrets. Secure handling of secrets is vital for protecting sensitive data and maintaining the integrity of your cluster.

The article then shifts focus to container sandboxing technologies such as Kata Containers and gVisor. These tools provide enhanced isolation for workloads, reducing the risk of security breaches by containing potential exposure.

Finally, we conclude by outlining the implementation of pod-to-pod encryption using mTLS. This ensures secure communication between microservices, significantly reducing the risk of data interception.

For additional context and a deeper dive into these topics, explore the following resources:

* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Open Policy Agent (OPA)](https://www.openpolicyagent.org/)
* [Kata Containers](https://katacontainers.io/)
* [gVisor](https://gvisor.dev/)

By following this guide, you will gain a comprehensive understanding of how to secure your Kubernetes clusters and microservices effectively.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/47622eba-6ec7-4595-aa88-30c857b860ad" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Security Contexts
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Security-Contexts/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Security-Contexts/page)

# Security Contexts

> This article explores security contexts in Kubernetes for applying security configurations to containers and pods for enhanced protection.

Welcome to this comprehensive guide on security contexts in Kubernetes. My name is Mumshad Mannambeth, and in this article, we will explore how security configurations can be applied to your containers and pods for enhanced protection.

When running Docker containers, you might recognize that you can specify security standards—such as setting a specific user ID or modifying Linux capabilities. For instance, you can run a container with a designated user or add a capability using the following commands:

```bash theme={null}
docker run --user=1001 ubuntu sleep 3600
docker run --cap-add MAC_ADMIN ubuntu
```

Kubernetes offers similar capabilities, but with the added flexibility of applying these settings at both the Pod and container levels. Configuring security contexts at the Pod level allows the settings to automatically propagate to all containers within that Pod. However, if a container-level security context is defined, those settings take precedence over the Pod-level configurations.

<Callout icon="lightbulb" color="#1CB2FE">
  Security contexts in Kubernetes not only ensure enhanced security but also standardize user privileges across containerized environments.
</Callout>

Below is an example of a Pod definition that demonstrates how to configure a security context for a container. In this example, the Pod uses an Ubuntu image with the `sleep` command. The configuration assigns a user ID using the `runAsUser` option and adds the `MAC_ADMIN` capability:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: web-pod
spec:
  containers:
    - name: ubuntu
      image: ubuntu
      command: ["sleep", "3600"]
      securityContext:
        runAsUser: 1000
        capabilities:
          add: ["MAC_ADMIN"]
```

By understanding and applying these security best practices, you can ensure that your Kubernetes deployments are better protected from unauthorized access and potential vulnerabilities.

Thank you for reading this guide on security contexts in Kubernetes. You are now ready to explore configuring and troubleshooting these security settings in your deployments. For additional insights and best practices, consider exploring the following resources:

* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Container Security Practices](https://kubernetes.io/docs/concepts/security/overview/)
* [Docker Hub](https://hub.docker.com/)

We look forward to seeing you in our next article.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/95fa6a35-2323-4c08-886c-dde070c78692" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/62cc10fa-4d66-40be-87d6-5002112f4a54" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Understanding Ciliums Architecture
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Understanding-Ciliums-Architecture/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Understanding-Ciliums-Architecture/page)

# Understanding Ciliums Architecture

> This article explains Ciliums architecture and its use of eBPF technology to improve Kubernetes networking and security.

Discover how Cilium's innovative architecture harnesses eBPF technology to enhance Kubernetes networking and security.

Cilium stands out by leveraging eBPF, a cutting-edge technology that runs directly within the Linux kernel. This integration enables efficient networking with advanced security measures. At its core, Cilium manages pod networking using the Container Network Interface (CNI), ensuring seamless communication among pods while enforcing strict security policies to allow only authorized traffic.

## Key Features of Cilium

Cilium offers several robust features to optimize your Kubernetes environment:

* **Network Policies:** Secure pod-to-pod communications by enforcing policies that prevent unauthorized access.
* **Services and Load Balancing:** Efficiently route traffic and distribute loads evenly among pods, ensuring high availability.
* **Bandwidth Management:** Regulate traffic consumption per pod to prevent network congestion.
* **Flow and Policy Logging:** Monitor network traffic in real time and gain insights into policy enforcement across your cluster.
* **Security and Operational Metrics:** Obtain deep visibility into your cluster’s security posture and overall performance.

<Frame>
  ![The image illustrates Cilium architecture, showing components like network policy, services, load balancing, and eBPF integration within an EKS node environment.](https://kodekloud.com/kk-media/image/upload/v1752871675/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Understanding-Ciliums-Architecture/frame_60.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  By leveraging eBPF, Cilium achieves high-performance networking with minimal overhead, making it an ideal solution for efficient Kubernetes networking.
</Callout>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/95e1a816-790c-4837-8e20-41392a00c528" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Understanding Resource Quotas
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Understanding-Resource-Quotas/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Understanding-Resource-Quotas/page)

# Understanding Resource Quotas

> This lesson covers implementing resource quotas in Kubernetes for multi-tenant environments to ensure fair resource distribution and prevent resource exhaustion.

In this lesson, we dive into the implementation of resource quotas in Kubernetes, specifically tailored for multi-tenant environments. This refresher builds on concepts covered in the [CKA Certification Course - Certified Kubernetes Administrator](https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator) and focuses on how resource quotas ensure fair resource distribution and prevent resource exhaustion across different teams or services.

Resource quota objects in Kubernetes provide administrators with a mechanism to enforce limits on resources such as CPU, memory, and storage for pods and containers. This control is vital for multi-tenancy as it prevents any single namespace from consuming excessive resources, thereby maintaining balanced and predictable cluster performance.

<Callout icon="lightbulb" color="#1CB2FE">
  Resource quotas help manage and guarantee resource availability, ensuring that all teams have protected access to the required CPU and memory without risking overall cluster stability.
</Callout>

## Example: Resource Quota for a Namespace

The following example demonstrates a Kubernetes resource quota configuration that restricts the resource consumption for a specific namespace named "namespace\_a". This setup limits resource requests to 4 CPUs and 16 GiB of memory, while capping resource limits at 8 CPUs and 32 GiB of memory.

```yaml theme={null}
apiVersion: v1
kind: ResourceQuota
metadata:
  name: cpu-memory-quota
  namespace: namespace_a
spec:
  hard:
    requests.cpu: "4"
    requests.memory: 16Gi
    limits.cpu: "8"
    limits.memory: 32Gi
```

## Example: Pod with Resource Restrictions

Here’s an example of a pod configuration that adheres to the resource constraints defined for "namespace\_a". The pod, using the nginx image, sets specific resource requests and limits to ensure it operates within the allocated boundaries:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: resource-limited-pod
  namespace: namespace_a
spec:
  containers:
  - name: resource-limited-container
    image: nginx
    resources:
      requests:
        cpu: "250m"
        memory: "64Mi"
      limits:
        cpu: "500m"
        memory: "128Mi"
```

This configuration ensures that the pod operates within the specified resource limits, which in turn contributes to a well-balanced resource allocation across multi-tenant environments. By enforcing these limits, Kubernetes helps prevent any single pod from monopolizing cluster resources, supporting a fair and stable operating environment for all users.

For more detailed information on Kubernetes resource management, explore the [Kubernetes Documentation](https://kubernetes.io/docs/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/e0b282e8-1643-44da-9172-cfa722d955b8" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/d1535b18-8e11-4e23-985b-9753a578c274" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Using Node Pools and TaintsTolerations for Isolation
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Using-Node-Pools-and-TaintsTolerations-for-Isolation/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Using-Node-Pools-and-TaintsTolerations-for-Isolation/page)

# Using Node Pools and TaintsTolerations for Isolation

> This guide explores using node pools with taints and tolerations for effective node isolation and multi-tenancy configurations.

In this guide, we explore how to use node pools combined with taints and tolerations to achieve effective node isolation and support multi-tenancy configurations. This approach allows you to dedicate specific nodes to individual tenants, thereby avoiding the issue of workload interference, often known as the noisy neighbor problem.

When implementing node isolation, a common strategy is to assign dedicated nodes to each tenant. For instance, Customer A might operate on Node A, Customer B on Node B, and Customer C on Node C. To enforce this separation, only pods with the matching tolerations can be scheduled on nodes that carry specific taints.

<Callout icon="lightbulb" color="#1CB2FE">
  Node isolation using taints and tolerations prevents unauthorized pods from being scheduled on nodes that are reserved for a particular tenant.
</Callout>

## Step 1: Apply a Taint to the Node

Begin by adding a taint to the node that you want to reserve. The following command applies a taint to Node A, ensuring that only pods with the appropriate toleration (i.e., belonging to Customer A) can be scheduled on Node A.

```bash theme={null}
kubectl taint nodes nodeA customer=customerA:NoSchedule
```

## Step 2: Configure Pod Definitions with Tolerations

Next, update your pod specification to include a toleration that matches the taint on the node. This configuration restricts the pod's scheduling to nodes that accept its designated toleration. Below is an example YAML definition for a pod assigned to Customer A:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: customer-a-pod
  namespace: customer_a
spec:
  containers:
  - name: customer-a-container
    image: nginx
  tolerations:
  - key: "customer"
    operator: "Equal"
    value: "customerA"
    effect: "NoSchedule"
```

With this setup, the pod can only be scheduled on nodes that have been tainted for Customer A, ensuring strict isolation between different tenant workloads.

<Callout icon="lightbulb" color="#1CB2FE">
  If you want to deepen your knowledge of taints and tolerations, consider exploring additional practical exercises and detailed documentation on the topic.
</Callout>

For more details on Kubernetes best practices and workload isolation, refer to the [Kubernetes Documentation](https://kubernetes.io/docs/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/8871fa68-1e25-4f0e-9aef-fdc2570189d9" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/1d21577e-6a9a-4e7d-a8f4-18ab9f127c64" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Validating and Mutating Admission Controllers
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Validating-and-Mutating-Admission-Controllers/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Validating-and-Mutating-Admission-Controllers/page)

# Validating and Mutating Admission Controllers

> This article explores Admission Controllers in Kubernetes, detailing their types, configuration, and examples of custom implementations.

In this lesson, we explore the various types of Admission Controllers in Kubernetes and demonstrate how to configure custom ones. Admission Controllers are plugins that govern and enforce cluster usage. They fall into two main categories:

* **Validating Admission Controllers:** These controllers check incoming requests and either allow or deny them based on predefined rules.
* **Mutating Admission Controllers:** These controllers modify requests by adjusting the object before it is persisted to the cluster.

Below, we provide detailed examples of each type.

***

## Validating Admission Controllers

One example of a validating admission controller is the namespace existence (or namespace lifecycle) controller, which ensures that a namespace exists before allowing a request. If the namespace does not exist, the request is rejected.

Another example is the default storage class admission controller, which is enabled by default. Consider the following scenario: when you submit a request to create a PersistentVolumeClaim (PVC) without specifying a storage class, the built-in admission controller intervenes by modifying the request to include the preconfigured default storage class.

### Example: PVC Request without a Storage Class

```yaml theme={null}
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: myclaim
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 500Mi
```

This PVC creation request passes through several stages: authentication, authorization, and finally, the admission controllers. The default storage class controller detects the missing storage class and automatically adds it to the request. The resulting PVC appears as follows:

```yaml theme={null}
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: myclaim
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 500Mi
  storageClassName: default
```

To inspect the PVC, use:

```bash theme={null}
kubectl describe pvc myclaim
```

You might see an output similar to:

```text theme={null}
Name:          myclaim
Namespace:     default
StorageClass:  default
Status:        Pending
Volume:        <none>
Labels:        <none>
Annotations:   <none>
```

<Callout icon="lightbulb" color="#1CB2FE">
  Mutating admission controllers modify the request (e.g., adding a default storage class), while validating admission controllers only verify the request against set policies. In some cases, controllers perform both actions.
</Callout>

Typically, mutating controllers run before validating controllers so that any modifications are validated. For example, a namespace auto-provisioning controller (a mutating controller) can create missing namespaces before the validating "namespace exists" controller runs. If the order were reversed, the validating controller might reject requests for non-existent namespaces, preventing auto-provisioning from occurring.

If any admission controller in the processing chain rejects a request, the entire operation fails and an error message is returned to the user.

***

## Extending Admission Controllers with Webhooks

In addition to built-in admission controllers, Kubernetes allows you to implement custom logic via two types of external webhooks:

* **Mutating Admission Webhook**
* **Validating Admission Webhook**

These webhooks let you direct admission review requests to a custom server—either within or outside your cluster. After the built-in admission controllers process a request, it is forwarded to the webhook. The webhook server receives an admission review object in JSON format containing details such as the user, requested operation, and the object involved.

### Admission Review JSON Object Example

Below is an example of the JSON object sent to a webhook server:

```json theme={null}
{
  "apiVersion": "admission.k8s.io/v1",
  "kind": "AdmissionReview",
  "request": {
    "uid": "705ab4f5-6393-11e8-b7cc-4201aa800002",
    "kind": {"group": "autoscaling", "version": "v1", "kind": "Scale"},
    "resource": {"group": "apps", "version": "v1", "resource": "deployments"},
    "subResource": "scale",
    "requestKind": {"group": "autoscaling", "version": "v1", "kind": "Scale"},
    "requestResource": {"group": "apps", "version": "v1", "resource": "deployments"}
  }
}
```

The webhook server processes this and responds with an object indicating if the request is allowed. For instance, an approval response might be:

```json theme={null}
{
  "apiVersion": "admission.k8s.io/v1",
  "kind": "AdmissionReview",
  "request": {
    "uid": "705ab4f5-6393-11e8-b7cc-42010aa80002",
    "kind": {"group": "autoscaling", "version": "v1", "kind": "Scale"},
    "resource": {"group": "apps", "version": "v1", "resource": "deployments"},
    "subResource": "scale",
    "requestKind": {"group": "autoscaling", "version": "v1", "kind": "Scale"},
    "requestResource": {"group": "apps", "version": "v1", "resource": "deployments"}
  },
  "response": {
    "uid": "value_from_request.uid",
    "allowed": true
  }
}
```

If the "allowed" field is false, the webhook will cause the API server to reject the request.

***

## Deploying an Admission Webhook Server

To utilize a custom admission controller, you must deploy your own webhook server, which contains the custom logic for mutation and/or validation. The server can be developed using any programming language that supports HTTPS (TLS is required for secure communication with the Kubernetes API server).

### Example: Go Webhook Server

Below is an excerpt from a sample admission webhook server written in Go:

```go theme={null}
package main

import (
    "encoding/json"
    "flag"
    "fmt"
    "io/ioutil"
    "net/http"

    "k8s.io/api/admission/v1beta1"
    metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
    "k8s.io/klog"
)

// toAdmissionResponse is a helper function to create an AdmissionResponse with an embedded error.
func toAdmissionResponse(err error) v1beta1.AdmissionResponse {
    return v1beta1.AdmissionResponse{
        Result: &metav1.Status{
            Message: err.Error(),
        },
    }
}

// admitFunc defines the function signature used for validators and mutators.
type admitFunc func(v1beta1.AdmissionReview) v1beta1.AdmissionResponse

// serve handles the HTTP portion of a request prior to passing it to an admit function.
func serve(w http.ResponseWriter, r *http.Request, admit admitFunc) {
    var body []byte
    if r.Body != nil {
        if data, err := ioutil.ReadAll(r.Body); err == nil {
            body = data
        }
    }
    // Further processing would continue here...
}
```

Although this example is written in Go, you can build your webhook server in any language that accommodates HTTPS and JSON-based API communications.

### Example: Python Webhook Server

The following pseudocode demonstrates a simple webhook server in Python using Flask. It includes two routes: one for validation and another for mutation.

```python theme={null}
from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

@app.route("/validate", methods=["POST"])
def validate():
    object_name = request.json["request"]["object"]["metadata"]["name"]
    user_name = request.json["request"]["userInfo"]["name"]
    status = True
    message = ""
    if object_name == user_name:
        message = "You can't create objects with your own name"
        status = False
    return jsonify(
        {
            "response": {
                "allowed": status,
                "uid": request.json["request"]["uid"],
                "status": {"message": message},
            }
        }
    )

@app.route("/mutate", methods=["POST"])
def mutate():
    user_name = request.json["request"]["userInfo"]["name"]
    patch = [{"op": "add", "path": "/metadata/labels/users", "value": user_name}]
    # Encode the patch using base64
    patch_encoded = base64.b64encode(str(patch).encode()).decode()
    return jsonify(
        {
            "response": {
                "allowed": True,
                "uid": request.json["request"]["uid"],
                "patch": patch_encoded,
                "patchType": "JSONPatch",
            }
        }
    )

if __name__ == "__main__":
    app.run(debug=True, port=443)
```

In this Python example, the validation endpoint rejects requests where the object's name matches the user name, while the mutation endpoint adds a label with the username using a JSON patch.

***

## Configuring the Webhook in Kubernetes

After deploying your webhook server, configure your Kubernetes cluster to use it by creating a webhook configuration object. Below is an example of a ValidatingWebhookConfiguration:

```yaml theme={null}
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  name: "pod-policy.example.com"
webhooks:
  - name: "pod-policy.example.com"
    clientConfig:
      service:
        namespace: "webhook-namespace"
        name: "webhook-service"
      caBundle: "CiOtLS0tQk......tLS0K"
    rules:
      - apiGroups: [""]
        apiVersions: ["v1"]
        operations: ["CREATE"]
        resources: ["pods"]
        scope: "Namespaced"
```

In this configuration:

* The webhook is triggered during pod creation.
* TLS is used for secure communication, as indicated by the `caBundle`.
* The API server references the webhook service by its name and namespace when deployed within the cluster.

For mutating webhooks, a similar configuration is created with `kind: MutatingWebhookConfiguration`.

Once applied, every time a pod is created (or another resource event specified in your rules), the API server calls your webhook server. Depending on whether the response indicates approval or rejection, the API server will allow or reject the request.

***

## Conclusion

This lesson provided an overview of validating and mutating admission controllers in Kubernetes. Key takeaways include:

* An understanding of built-in admission controllers and their roles in request validation and mutation.
* How external admission webhooks can extend Kubernetes by allowing custom logic.
* Practical examples of webhook servers implemented in Go and Python.
* Steps to configure your Kubernetes cluster to integrate with these webhooks.

<Callout icon="lightbulb" color="#1CB2FE">
  Experimenting in a lab environment is crucial to reinforce these concepts. Continue exploring advanced scenarios to further enhance your Kubernetes security and operational flexibility.
</Callout>

<Frame>
  ![The image illustrates a diagram of admission controllers, highlighting mutating and validating processes with examples like AlwaysPullImages and DefaultStorageClass.](https://kodekloud.com/kk-media/image/upload/v1752871678/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Validating-and-Mutating-Admission-Controllers/frame_140.jpg)
</Frame>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/e25733b7-ff01-41ea-b1b7-6dffbd805590" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/65fb07e4-26e5-47c8-a1c2-115b9d934385" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 Writing Effective Encryption Policies
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Writing-Effective-Encryption-Policies/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Writing-Effective-Encryption-Policies/page)

# Writing Effective Encryption Policies

> This guide explains how to configure Pod-to-Pod encryption using a Cilium network policy in a Kubernetes cluster.

In this guide, you'll learn how to configure robust Pod-to-Pod encryption using a Cilium network policy. This policy ensures that outbound traffic (egress) for your application – for example, "myapp" – is encrypted and secure within your Kubernetes cluster.

## Cilium Network Policy Overview

The Cilium network policy is defined with key components to enforce encryption for your application's traffic. Here’s a breakdown of the essential elements:

1. **API Version**: The configuration uses `"cilium.io/v2"`, specifying that this is a Cilium-specific network policy.
2. **Kind**: The policy type is set as `CiliumNetworkPolicy`, indicating that Cilium will manage the enforcement.
3. **Metadata**: The policy is named `allow-encrypted-traffic`.
4. **Endpoint Selector**: It targets all pods with the label `app: myapp`, ensuring that the policy applies specifically to your application.
5. **Egress Rules**: The rules allow outbound traffic directed to pods with the same label (`app: myapp`) over TCP port 80. This ensures encrypted traffic flows only to designated pods.

## Complete Cilium Network Policy

Below is the full YAML configuration for the Cilium network policy:

```yaml theme={null}
apiVersion: cilium.io/v2
kind: CiliumNetworkPolicy
metadata:
  name: allow-encrypted-traffic
spec:
  endpointSelector:
    matchLabels:
      app: myapp
  egress:
  - toEndpoints:
    - matchLabels:
        app: myapp
    toPorts:
    - ports:
      - port: "80"
        protocol: TCP
```

This policy is similar to standard Kubernetes network policies but includes additional settings to handle encrypted traffic effectively.

## Verify Encrypted Traffic Between Pods

To ensure that traffic between pods is properly encrypted, you can capture and inspect network packets using the `tcpdump` utility. Follow these steps:

1. **Launch a Pod Shell**: Open a shell session in one of the pods.
2. **Install tcpdump**: Update the package list and install `tcpdump`.
3. **Monitor Network Traffic**: Use `tcpdump` to capture packets on the `eth0` interface.

Run the following commands:

```bash theme={null}
kubectl exec -it <pod-name> -- /bin/bash
apt-get update && apt-get install -y tcpdump
tcpdump -i eth0 -nn
```

<Callout icon="lightbulb" color="#1CB2FE">
  Ensure you replace `<pod-name>` with the actual name of your pod when executing the commands.
</Callout>

By monitoring the network interface using `tcpdump`, you can verify that no unencrypted packets are transmitted. When encryption is properly enabled, the captured traffic should appear encrypted and secure.

## Conclusion

By following the steps outlined in this tutorial, you can effectively control and secure Pod-to-Pod communication within your Kubernetes environment using Cilium network policies. This approach not only enhances the security of your applications but also ensures compliance with encryption best practices.

For more information about Kubernetes network policies and advanced security configurations, refer to the following resources:

* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Cilium Documentation](https://docs.cilium.io/)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/0ece2d20-ac81-43a2-8732-bd861099d668" />
</CardGroup>

---


# 📂 Section: Minimize Microservice Vulnerabilities
## 📖 gVisor
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/gVisor/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/gVisor/page)

# gVisor

> This article explores gVisor, a Google-developed solution for enhancing container isolation through an additional layer that intercepts system calls.

In this lesson, we explore alternative techniques for continuous sandboxing and introduce gVisor, a robust solution developed by Google to enhance container isolation.

The Linux kernel is a highly complex foundation that supports a vast array of application scenarios—from streaming high-definition Netflix videos to powering critical control systems for space missions. It enables applications to perform thousands of operations via system calls while offering additional privileges and capabilities as needed. However, this extensive functionality also enlarges the attack surface, making the kernel more vulnerable to exploits such as Dirty COW, which can compromise the host system.

While tools like Seccomp and AppArmor can mitigate these risks by enforcing blacklist and whitelist rules to control container actions, the fundamental challenge in multi-tenant environments remains: every container interacts directly with the same operating system and kernel. This shared access amplifies security risks.

<Callout icon="lightbulb" color="#1CB2FE">
  gVisor creates an extra isolation layer between the container and the Linux kernel by intercepting system calls, thereby reducing the attack surface.
</Callout>

Imagine if containers could be further isolated by intercepting system calls before they reach the Linux kernel. This is the principle behind gVisor. When an application within a container makes a system call, gVisor intercepts it instead of allowing direct communication with the kernel. This added abstraction significantly enhances container security.

## gVisor Architecture

gVisor's sandbox architecture comprises two main components that cooperate to provide stronger isolation compared to traditional containers:

1. **Sentry:**\
   Sentry functions as an independent, application-level kernel specifically designed for container environments. It intercepts and processes system calls made by containerized applications. Due to its container-specific design, Sentry supports only a limited set of functionalities compared to the full Linux kernel. This streamlined feature set minimizes the risk of exploitable vulnerabilities.

<Frame>
  ![The image illustrates gVisor's architecture, showing a container interacting with the Sentry through syscalls, layered above the Linux Kernel and hardware.](https://kodekloud.com/kk-media/image/upload/v1752871679/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-gVisor/frame_160.jpg)
</Frame>

2. **Gofer:**\
   When an application inside the container requires file access, Sentry does not forward the call directly to the kernel. Instead, it communicates with a dedicated process called Gofer, which acts as a file proxy. Gofer handles the necessary logic for accessing system files for containerized applications, effectively serving as a middleman between the container and the operating system. This separation further prevents potential exploits.

<Frame>
  ![The image illustrates gVisor's architecture, showing components like Sentry and Gofer interacting with syscalls, the Linux Kernel, and hardware for container isolation.](https://kodekloud.com/kk-media/image/upload/v1752871680/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-gVisor/frame_200.jpg)
</Frame>

For network operations, gVisor utilizes its own network stack. This design choice ensures that containers do not directly interact with the operating system’s network code, thereby further reinforcing isolation.

## Benefits and Considerations

Each container is assigned its own isolated gVisor kernel, which serves as a virtualized sandbox between the application and the Linux kernel. This dedicated approach significantly reduces the overall attack surface by ensuring that even if one gVisor instance fails or is compromised, the isolation prevents other containers from being affected.

<Callout icon="triangle-alert" color="#FF6B6B">
  While gVisor provides enhanced security by intercepting system calls and isolating container environments, not all applications are fully compatible with its architecture. It is essential to test your applications for compatibility issues, as processing system calls through a middleman may introduce a slight performance overhead.
</Callout>

That concludes this lesson on gVisor. In our next discussion, we will examine Kata Containers, another tool used to sandbox containers, and compare its approach to that of gVisor.

For further reading on container security and best practices, be sure to explore additional [Kubernetes documentation](https://kubernetes.io/docs/) and related resources.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/7431dd03-f5c2-4ebb-b94a-2d35615bbd8c/lesson/eba0db3b-fc8e-4c85-bb45-e49382bf96b3" />
</CardGroup>

---


