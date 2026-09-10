# 📂 Section: Cluster Setup and Hardening
## 📖 API Groups
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/API-Groups/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/API-Groups/page)

# API Groups

> This article explains the structure of Kubernetes API groups and their interaction with verbs for direct API access and proxy usage.

Before diving into authorization, it is important to understand API groups in Kubernetes. This article explains how the Kubernetes API is structured and how its groups and verbs interact, offering insights into direct API access and the use of proxies.

## Understanding the Kubernetes API

The Kubernetes API forms the foundation for all interactions with a cluster. Whether you use the Kubernetes command-line utility (kubectl) or interact directly via REST, every operation communicates with the API server. For example, to check the version of the Kubernetes API server, you can run the command below to access it on the master node's default port 6443:

```bash theme={null}
curl https://kube-master:6443/version
{
  "major": "1",
  "minor": "13",
  "gitVersion": "v1.13.0",
  "gitCommit": "ddf47ac13c1a9483ea035a79cd7c1005ff21a6d",
  "gitTreeState": "clean",
  "buildDate": "2018-12-03T20:56:12Z",
  "goVersion": "go1.11.2",
  "compiler": "gc",
  "platform": "linux/amd64"
}
```

Similarly, to list your pods, you would use the API endpoint `/api/v1/pods`. This article will focus on API pods, versions, and the overall structure of the Kubernetes API.

The API is divided into multiple groups based on their function. Some groups are dedicated to core resources—such as pods, namespaces, persistent volumes—while others are logically grouped by functionality, such as metrics, health, and logs.

<Frame>
  ![The image shows six colored labels with text: /metrics, /healthz, /version, /api, /apis, and /logs, likely representing API endpoints.](https://kodekloud.com/kk-media/image/upload/v1752871324/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-API-Groups/frame_70.jpg)
</Frame>

The `/version` API endpoint displays the cluster version, while `/metrics` and `/healthz` help monitor the cluster's health. Additionally, the `/logs` API facilitates integration with third-party logging applications.

## Core API Group vs. Named API Group

Kubernetes organizes its API resources into two main groups:

1. **Core API Group:** Contains resources integral to cluster operation, including:
   * Namespaces
   * Pods
   * Replication controllers
   * Events
   * Endpoints
   * Nodes
   * Bindings
   * Persistent volumes and persistent volume claims
   * Config maps
   * Secrets
   * Services

2. **Named API Group:** Organizes newer features and additional functionalities into distinct categories, such as:

   * Apps (deployments, replica sets, stateful sets)
   * Extensions
   * Networking (network policies)
   * Storage
   * Authentication
   * Authorization

   For example, certificate signing requests fall under the certificates category.

<Frame>
  ![The image depicts a hierarchical structure of a Kubernetes API, showing core components like namespaces, pods, and services under the /api/v1 endpoint.](https://kodekloud.com/kk-media/image/upload/v1752871325/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-API-Groups/frame_120.jpg)
</Frame>

Within each API group, resources support a range of actions—commonly known as "verbs"—including list, get, create, delete, update, and watch. The following diagram illustrates how Kubernetes API groups, resources, and verbs interact:

<Frame>
  ![The image is a diagram illustrating Kubernetes API groups, resources, and actions like list, get, create, delete, update, and watch.](https://kodekloud.com/kk-media/image/upload/v1752871326/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-API-Groups/frame_170.jpg)
</Frame>

For further details on these interactions and available operations, refer to the Kubernetes API reference documentation. For example, the documentation for "Pod v1 core" includes group details and information on API actions.

<Frame>
  ![The image shows a Kubernetes documentation page for "Pod v1 core," highlighting API details and a warning about creating Pods through a Controller.](https://kodekloud.com/kk-media/image/upload/v1752871327/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-API-Groups/frame_200.jpg)
</Frame>

## Exploring the Kubernetes API Server

To view the available API groups directly, you can query the Kubernetes API server on port 6443 without specifying an endpoint:

```bash theme={null}
curl http://localhost:6443 -k
{
  "paths": [
    "/api",
    "/api/v1",
    "/apis",
    "/apis/",
    "/healthz",
    "/logs",
    "/metrics",
    "/openapi/v2",
    "/swagger-2.0.0.json"
  ]
}
```

This command returns a list of available API groups. Named API groups contain additional resources corresponding to various functional areas of the cluster.

### A Note on Direct API Access

When accessing the API directly using curl without authentication (as shown above), access might be restricted to only certain endpoints—such as the version API. To access other APIs, you need to authenticate using certificate files:

```bash theme={null}
curl http://localhost:6443 -k --key admin.key --cert admin.crt --cacert <path-to-cacert>
```

Alternatively, you can simplify the process using the `kubectl proxy` command. This proxy uses the credentials from your kubeconfig file, eliminating the need to specify certificates with every request. To start the proxy, run:

```bash theme={null}
kubectl proxy
Starting to serve on 127.0.0.1:8001
```

After the proxy is running, you can access the API server through it:

```bash theme={null}
curl http://localhost:8001 -k
{
  "paths": [
    "/api",
    "/api/v1",
    "/apis",
    "/apis/",
    "/healthz",
    "/logs",
    "/metrics",
    "/openapi/v2",
    "/swagger-2.0.0.json"
  ]
}
```

<Callout icon="lightbulb" color="#1CB2FE">
  Both "kube proxy" and "kubectl proxy" might sound similar but serve different functions:

  * "Kube proxy" manages communication between pods and services across nodes.
  * "Kubectl proxy" is an HTTP proxy used to securely access the Kubernetes API server.
</Callout>

<Frame>
  ![The image highlights that "Kube proxy" is not equal to "Kubectl proxy," indicating they are distinct concepts or tools.](https://kodekloud.com/kk-media/image/upload/v1752871328/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-API-Groups/frame_300.jpg)
</Frame>

## Summary

All Kubernetes resources are organized into API groups. The core API group contains essential resources for cluster operation, while named API groups provide a structured approach to additional functionalities. Each resource supports actions (verbs) like list, get, create, delete, update, and watch. In the next discussion, we will explore how authorization leverages these API groups and verbs to control user access.

This concludes the article on API groups.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/fac1b9c3-5d91-48a7-aa96-0ae572853d9f" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/077b6709-d862-450e-8373-a32974990de8" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 Auditing
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Auditing/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Auditing/page)

# Auditing

> This article explores auditing in Kubernetes, focusing on tracking activities, ensuring security, compliance, and troubleshooting through detailed audit logs.

In this lesson, we explore the concept of auditing in Kubernetes. Auditing involves recording and tracking every activity in the cluster to create a detailed history of events. This process is crucial for ensuring security, achieving compliance, and facilitating troubleshooting. With effective auditing, administrators can monitor resource access, detect potential security breaches, and verify that all actions comply with organizational policies. Audit logs capture important details including who made changes, when they were made, what was changed, and how the change was implemented.

Consider this sample audit event where an admin user creates an Nginx deployment. The event details include the user’s identity, the affected resource, and timestamps that indicate when the request was received and processed.

```json theme={null}
{
  "kind": "Event",
  "apiVersion": "audit.k8s.io/v1",
  "level": "Metadata",
  "auditID": "f4d9a5c1-5f4d-48cb-bd27-2f66c9d9c7c6",
  "stage": "ResponseComplete",
  "requestURI": "/apis/apps/v1/namespaces/default/deployments",
  "verb": "create",
  "user": {
    "username": "admin",
    "groups": [
      "system:masters",
      "system:authenticated"
    ]
  },
  "sourceIPs": ["192.168.1.10"],
  "userAgent": "kubectl/v1.20.0 (linux/amd64) kubernetes/af46c47",
  "objectRef": {
    "resource": "deployments",
    "namespace": "default",
    "name": "nginx-deployment",
    "apiVersion": "apps/v1"
  },
  "responseStatus": {
    "metadata": {},
    "code": 201
  },
  "requestReceivedTimestamp": "2024-07-29T07:50:04.123456Z",
  "stageTimestamp": "2024-07-29T07:50:04.223456Z",
  "annotations": {
    "authorization.k8s.io/decision": "allow",
    "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \"cluster-admin\" of ClusterRole \"cluster-admin\" to User \"admin\""
  }
}
```

In the example above, key details such as the API version, operation type, initiating user, and timestamps are logged. The user agent confirms that the request originated from a specific version of the kubectl command-line utility.

<Callout icon="lightbulb" color="#1CB2FE">
  Auditing logs are invaluable for tracing the source of issues, ensuring that resources are secured, and validating compliance with regulations such as GDPR, HIPAA, and PCI DSS.
</Callout>

## Why Audit?

Auditing is essential for tracking who did what, when, and where within a Kubernetes cluster. It plays a pivotal role in detecting unauthorized access and ensuring that resources are managed according to organizational policies. Detailed audit logs are also crucial for compliance with industry regulations and provide a thorough audit trail in the event of security incidents.

<Frame>
  ![The image outlines security and compliance, focusing on tracking user activities, regulatory compliance, and incident response with standards like GDPR, HIPAA, and PCI-DSS.](https://kodekloud.com/kk-media/image/upload/v1752871329/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Auditing/frame_100.jpg)
</Frame>

Furthermore, auditing helps administrators monitor changes to resources and configurations, making it easier to manage and troubleshoot issues by isolating the root cause of problems.

## Audit Policies

Kubernetes supports several audit policy levels that can be tailored to the required detail level:

* **None:** No events are logged.
* **Metadata:** Logs only request metadata (user, timestamp, resource, verb) without request/response bodies.
* **Request:** Logs both event metadata and the request body, but excludes the response body.
* **Request Response:** Logs event metadata, the request body, and the response body.

Below are examples that illustrate these configurations.

### Metadata Audit Policy

The following YAML configuration logs metadata for pod-related activities such as "get", "list", "create", "delete", and "update":

```yaml theme={null}
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
- level: Metadata
  verbs: ["get", "list", "create", "delete", "update"]
  resources:
  - group: ""
    resources: ["pods"]
```

When an event matches this policy, details such as the username, timestamp, and resource information are captured. An example audit event might look like:

```json theme={null}
{
  "kind": "Event",
  "apiVersion": "audit.k8s.io/v1",
  "level": "Metadata",
  "timestamp": "2024-10-11T12:34:56Z",
  "user": {
    "username": "system:serviceaccount:kube-system:default",
    "groups": ["system:serviceaccounts", "system:serviceaccounts:kube-system"]
  },
  "verb": "get",
  "namespace": "default",
  "resource": "pods",
  "stage": "ResponseComplete",
  "objectRef": {
    "resource": "pods",
    "namespace": "default",
    "name": "example-pod"
  }
}
```

### Request Audit Policy

This example shows how to configure an audit policy to capture both metadata and the full request details for "create", "delete", and "update" operations on pods:

```yaml theme={null}
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
- level: Request
  verbs: ["create", "delete", "update"]
  resources:
  - group: ""
    resources: ["pods"]
```

A sample audit event for a "create" operation might include the complete request object details:

```json theme={null}
{
  "kind": "Event",
  "apiVersion": "audit.k8s.io/v1",
  "level": "Request",
  "timestamp": "2024-10-11T12:34:56Z",
  "user": {
    "username": "system:serviceaccount:kube-system:default",
    "groups": ["system:serviceaccounts", "system:serviceaccounts:kube-system"]
  },
  "verb": "create",
  "namespace": "default",
  "resource": "pods",
  "stage": "ResponseComplete",
  "objectRef": {
    "resource": "pods",
    "namespace": "default",
    "name": "example-pod"
  },
  "requestObject": {
    "metadata": {
      "name": "example-pod",
      "namespace": "default"
    },
    "spec": {
      "containers": [
        {
          "name": "example-container",
          "image": "nginx"
        }
      ]
    }
  }
}
```

<Frame>
  ![The image shows an "Audit Policy" with four options: None, Metadata, Request, and Request Response, each in separate boxes.](https://kodekloud.com/kk-media/image/upload/v1752871330/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Auditing/frame_170.jpg)
</Frame>

## Summary

Kubernetes audit logs are essential for securing and managing clusters. These logs provide comprehensive details about every access request and change, making it easier to maintain compliance, detect security incidents, and troubleshoot issues. By understanding and implementing the appropriate audit policies, administrators can ensure a well-monitored and secure Kubernetes environment.

That's the end of this article.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/40739f67-05b7-4bda-9cd8-e8fa9cb5c0ba" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 Authentication
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Authentication/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Authentication/page)

# Authentication

> This article focuses on securing Kubernetes cluster access through authentication mechanisms, including static password and token files for users and service accounts.

Welcome to this detailed lesson on authentication within a Kubernetes cluster. In a typical Kubernetes environment, multiple nodes—either physical or virtual—operate together, supporting various components that provide a robust and scalable system. Users interact with the cluster in different roles: administrators and developers manage the cluster, while end users access deployed applications and third-party services integrate with the system.

<Frame>
  ![The image illustrates a network diagram showing interactions between admins, developers, end users, and bots through a series of connected nodes.](https://kodekloud.com/kk-media/image/upload/v1752871332/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Authentication/frame_30.jpg)
</Frame>

In this lesson, we focus on securing cluster management access by implementing secure communication and robust authentication mechanisms. Although end user security for applications is managed internally by the applications themselves, our discussion centers on authenticating access to the Kubernetes cluster for administrative and automated purposes. This includes human users—such as administrators and developers—and service accounts used by bots or automated processes.

Kubernetes does not manage local user accounts natively. Instead, it depends on external sources like files containing user details, certificate-based authentication, or third-party identity services such as LDAP or Kerberos. While you cannot list or create user accounts directly in Kubernetes, the system handles service accounts natively via the Kubernetes API.

<Frame>
  ![The image categorizes accounts into "User" (Admins, Developers) and "Service Accounts" (Bots) with corresponding icons.](https://kodekloud.com/kk-media/image/upload/v1752871333/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Authentication/frame_90.jpg)
</Frame>

All requests—whether initiated by the kubectl tool or directly sent to the API—are processed by the kube-apiserver. This critical server authenticates each request using various methods, including:

* Static password files
* Static token files
* Certificates
* Integration with third-party authentication protocols such as LDAP and Kerberos

Below, we introduce static password and token file mechanisms, which are among the simplest methods to understand and implement basic authentication in Kubernetes.

## Static Password and Token Files

The most straightforward authentication method involves creating a CSV file that lists users along with their credentials, usernames, and user IDs. Optionally, a fourth column can specify group information. This CSV file is then provided to the kube-apiserver as an authentication option.

### Static Password File Example

To use a static password file, create a CSV file (e.g., `user-details.csv`) with the following format:

```csv theme={null}
password123,user1,u0001,group1
password123,user2,u0002,group1
password123,user3,u0003,group2
password123,user4,u0004,group2
password123,user5,u0005,group2
```

Next, configure the kube-apiserver to utilize this file by including the option:

```bash theme={null}
kube-apiserver --basic-auth-file=user-details.csv
```

If you are using a tool such as kubeadm, modify the kube-apiserver pod definition file accordingly. kubeadm will automatically restart the kube-apiserver after these changes. An example of a modified kube-apiserver startup command might look like this:

```bash theme={null}
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
  -v=2 \
  --basic-auth-file=user-details.csv
```

Below is a sample Kubernetes pod manifest for the kube-apiserver:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
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
      - --enable-admission-plugins=NodeRestriction
      - --enable-bootstrap-token-auth=true
      - --basic-auth-file=user-details.csv
```

### Static Token File Example

Similarly, authentication can be performed using a static token file. The CSV format is nearly identical, except that the password is replaced with a token. For instance, your `user-token-details.csv` might contain:

```csv theme={null}
KpjCVbI7cFAHYPkByTIzRb7gulcUc4B,user10,u0010,group1
rJjncHmvtXHc6MlWQddhtvNyvhgTdXSC,user11,u0011,group1
mjpOFTEiF0kL9toikaRNTt59ePtczZSq,user12,u0012,group2
PG41IXhs7QjqWkmBkgvGT9gIoyUqZiJ,user13,u0013,group2
```

Start the kube-apiserver with the token file option:

```bash theme={null}
kube-apiserver --token-auth-file=user-token-details.csv
```

When sending requests with token authentication, include the token in the header. For example:

```bash theme={null}
curl -v -k https://master-node-ip:6443/api/v1/pods --header "Authorization: Bearer KpjCVbI7cFAHYPkByTIzRb7gulcUc4B"
```

<Frame>
  ![The image illustrates Kubernetes authentication mechanisms, including static password files, static token files, certificates, and identity services, related to the kube-apiserver.](https://kodekloud.com/kk-media/image/upload/v1752871334/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Authentication/frame_180.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Storing usernames, passwords, and tokens in plain text is inherently insecure. In production environments, consider using certificate-based authentication or integrating with trusted third-party identity providers.
</Callout>

<Frame>
  ![The image contains a note advising against a certain authentication mechanism, suggesting volume mount consideration, and setting up role-based authorization for new users in kubeadm.](https://kodekloud.com/kk-media/image/upload/v1752871335/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Authentication/frame_290.jpg)
</Frame>

<Callout icon="triangle-alert" color="#FF6B6B">
  When configuring your cluster using kubeadm, ensure that authentication files are securely mounted as volumes, and deploy appropriate authorization policies for any new users to protect your cluster from unauthorized access.
</Callout>

This lesson covered the use of static password and token file mechanisms to authenticate requests made to Kubernetes. In upcoming sections, we will explore certificate-based authentication in detail and discuss how Kubernetes leverages certificates to secure communication between its components.

For additional information on Kubernetes authentication and security best practices, please visit the following resources:

* [Kubernetes Basics](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Docker Hub](https://hub.docker.com/)
* [Terraform Registry](https://registry.terraform.io/)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/6008a4f2-b1c3-4739-b9d4-4a112e75db86" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 Authorization
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Authorization/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Authorization/page)

# Authorization

> This article explains how Kubernetes manages authorization to control user operations within a cluster.

In this article, we explain how Kubernetes handles authorization. After establishing access to a cluster through authentication (as discussed in our previous article), authorization determines which operations a user—whether human or machine—can perform within the cluster.

For example, a cluster administrator can view, create, or delete objects such as pods, nodes, and deployments. However, when granting access to additional users (e.g., developers, testers, other administrators, or external applications like [Jenkins](https://learn.kodekloud.com/user/courses/jenkins) and monitoring tools), it is best practice to restrict their privileges. Developers might be allowed to view pods and deploy applications but should not modify cluster configurations or delete nodes. Similarly, when sharing a cluster among multiple organizations or teams using namespaces, each user’s access should be confined to their designated namespace.

<Callout icon="lightbulb" color="#1CB2FE">
  Adjust user privileges using authorization policies to ensure cluster security and maintain operational integrity.
</Callout>

Below are some example commands demonstrating typical administrative operations:

```bash theme={null}
kubectl get pods
# Output:
# NAME    READY   STATUS    RESTARTS   AGE
kubectl get nodes
# Output:
# NAME        STATUS   ROLES     AGE     VERSION
# worker-1    Ready    <none>    5d21h   v1.13.0
kubectl delete node worker-2
# Output:
# Node worker-2 Deleted!
```

When non-admin users attempt similar operations, they may encounter authorization errors:

```bash theme={null}
kubectl get pods
kubectl get nodes
kubectl delete node worker-2
# Error from server (Forbidden): nodes "worker-2" is forbidden: User "developer" cannot delete resource "nodes"
```

Kubernetes supports a variety of authorization mechanisms, including:

* Node Authorization
* Attribute-Based Authorization
* Role-Based Access Control (RBAC)
* Webhook-Based Authorization

## Node Authorization

When the Kube API server handles requests from internal components, such as kubelets, it utilizes node authorization. The kubelet is responsible for tasks like reading service and pod information and reporting node status. These requests are authenticated by confirming that they originate from users with a name prefixed by "system:node" who belong to the "system:nodes" group.

<Frame>
  ![The image illustrates a Kubernetes architecture, showing interactions between a user, Kube API, and kubelet, with read/write operations for services, endpoints, nodes, and pods.](https://kodekloud.com/kk-media/image/upload/v1752871337/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Authorization/frame_150.jpg)
</Frame>

Once a kubelet makes a request with the appropriate credentials, the node authorizer grants the necessary privileges.

<Frame>
  ![The image illustrates a Node Authorizer process involving a user, Kube API, kubelet, and a certificate, detailing read and write permissions.](https://kodekloud.com/kk-media/image/upload/v1752871338/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Authorization/frame_180.jpg)
</Frame>

## Attribute-Based Authorization

For external API access, attribute-based authorization enables you to associate specific users or user groups with sets of permissions. For instance, you can define a JSON policy to allow a particular developer user to view, create, and delete pods. Below is an example policy file:

```json theme={null}
{"kind": "Policy", "spec": {"user": "dev-user", "namespace": "*", "resource": "pods", "apiGroup": "*"}}
{"kind": "Policy", "spec": {"user": "dev-user-2", "namespace": "*", "resource": "pods", "apiGroup": "*"}}
{"kind": "Policy", "spec": {"group": "dev-users", "namespace": "*", "resource": "pods", "apiGroup": "*"}}
{"kind": "Policy", "spec": {"user": "security-1", "namespace": "*", "resource": "csr", "apiGroup": "*"}}
```

Every time you need to update security settings, modify this policy file and restart the kube-apiserver. However, as the number of users and policies increases, these attribute-based configurations can become difficult to manage.

## Role-Based Access Control (RBAC)

RBAC offers a more scalable approach compared to directly binding permissions to each user. With RBAC, you define roles that encapsulate necessary permissions (for example, one role for developers and another for security users). When users are assigned to roles, any updates made to a role are immediately reflected for all associated users.

<Frame>
  ![The image illustrates RBAC roles, showing user permissions for developers and security, including actions like viewing, creating, and deleting PODs, and approving CSRs.](https://kodekloud.com/kk-media/image/upload/v1752871340/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Authorization/frame_290.jpg)
</Frame>

## Webhook-Based Authorization

If you prefer to manage authorization externally, third-party tools like [Open Policy Agent](https://www.openpolicyagent.org/) can be used. In this scenario, Kubernetes sends an API call containing user details and request information to the external system. Based on the external decision, the API server either grants or denies access.

## Simple Authorization Modes: AlwaysAllow and AlwaysDeny

Kubernetes also includes two straightforward authorization modes: AlwaysAllow and AlwaysDeny. As their names imply, AlwaysAllow permits all requests without checks, while AlwaysDeny blocks all requests. These modes are configured in the kube-apiserver using the authorization mode option. If not specified, the default mode is AlwaysAllow.

### AlwaysAllow Mode Configuration

Below is an example configuration for the kube-apiserver using the AlwaysAllow mode:

```bash theme={null}
ExecStart=/usr/local/bin/kube-apiserver \
  --advertise-address=${INTERNAL_IP} \
  --allow-privileged=true \
  --apiserver-count=3 \
  --authorization-mode=AlwaysAllow \
  --bind-address=0.0.0.0 \
  --enable-swagger-ui=true \
  --etcd-cafile=/var/lib/kubernetes/ca.pem \
  --etcd-certfile=/var/lib/kubernetes/apiserver-etcd-client.crt \
  --etcd-keyfile=/var/lib/kubernetes/apiserver-etcd-client.key \
  --etcd-servers=https://127.0.0.1:2379 \
  --event-ttl=1h \
  --kubelet-certificate-authority=/var/lib/kubernetes/ca.pem \
  --kubelet-client-certificate=/var/lib/kubernetes/apiserver-etcd-client.crt \
  --kubelet-client-key=/var/lib/kubernetes/apiserver-etcd-client.key \
  --service-node-port-range=30000-32767 \
  --client-ca-file=/var/lib/kubernetes/ca.pem \
  --tls-cert-file=/var/lib/kubernetes/apiserver.crt \
  --tls-private-key-file=/var/lib/kubernetes/apiserver.key \
  -v=2
```

### Configuring Multiple Authorization Modes

It is also possible to enable multiple authorization modes simultaneously by providing a comma-separated list. For example, to enable node authorization, RBAC, and webhook authorization in that order, configure the kube-apiserver as follows:

```bash theme={null}
ExecStart=/usr/local/bin/kube-apiserver \
  --advertise-address=${INTERNAL_IP} \
  --allow-privileged=true \
  --apiserver-count=3 \
  --authorization-mode=Node,RBAC,Webhook \
  --bind-address=0.0.0.0 \
  --enable-swagger-ui=true \
  --etcd-cafile=/var/lib/kubernetes/ca.pem \
  --etcd-certfile=/var/lib/kubernetes/apiserver-etcd-client.crt \
  --etcd-keyfile=/var/lib/kubernetes/apiserver-etcd-client.key \
  --etcd-servers=https://127.0.0.1:2379 \
  --event-ttl=1h \
  --kubelet-certificate-authority=/var/lib/kubernetes/ca.pem \
  --kubelet-client-certificate=/var/lib/kubernetes/apiserver-etcd-client.crt \
  --kubelet-client-key=/var/lib/kubernetes/apiserver-etcd-client.key \
  --service-node-port-range=30000-32767 \
  --client-ca-file=/var/lib/kubernetes/ca.crt \
  --tls-cert-file=/var/lib/kubernetes/apiserver.crt \
  --tls-private-key-file=/var/lib/kubernetes/apiserver.key \
  --v=2
```

When multiple modes are configured, the API server processes each request through the specified modules in the provided order:

1. The node authorizer first examines the request (applicable only for node-related operations). If it denies the request, the process proceeds to the next module.
2. The RBAC controller evaluates the request. If it approves, no additional checks occur.
3. If necessary, the webhook authorizer issues the final decision.

Once any module approves the request, remaining checks are skipped, and the user is granted access to the requested object.

<Callout icon="lightbulb" color="#1CB2FE">
  More details on RBAC and additional Kubernetes security mechanisms will be provided in upcoming articles.
</Callout>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/693206c3-db65-4efc-9e0c-f58671a5818a" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 CIS benchmark for Kubernetes
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/CIS-benchmark-for-Kubernetes/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/CIS-benchmark-for-Kubernetes/page)

# CIS benchmark for Kubernetes

> This article explores the CIS Benchmarks for Kubernetes, focusing on best practices and security recommendations for Kubernetes versions 1.16 to 1.18.

In this lesson, we explore the CIS Benchmarks for Kubernetes. The CIS website provides cybersecurity benchmarks for various vendors—including operating systems, public cloud platforms, network devices, and server software. Here, we focus specifically on Kubernetes.

To begin, register on the CIS website and download the latest CIS Benchmarks for Kubernetes. The most current version covered in this lesson addresses best practices for Kubernetes versions 1.16 through 1.18. This document is invaluable for system administrators, application administrators, security specialists, auditors, and anyone involved in developing, deploying, assessing, or securing Kubernetes environments.

<Frame>
  ![The image is an excerpt from the CIS Kubernetes Benchmark v1.6.0, providing security guidance for Kubernetes versions 1.16 to 1.18.](https://kodekloud.com/kk-media/image/upload/v1752871341/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-CIS-benchmark-for-Kubernetes/frame_40.jpg)
</Frame>

The benchmark document includes hundreds of recommendations that address both control plane and worker node components. For example, it provides detailed guidance on securing master node files. One recommendation mandates that the file permissions for the API server pod specification file should be set to 644, ensuring that only administrators can modify the file.

<Frame>
  ![The image shows a list of security recommendations for Kubernetes master node configuration files from the CIS Kubernetes Benchmark v1.6.0.](https://kodekloud.com/kk-media/image/upload/v1752871343/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-CIS-benchmark-for-Kubernetes/frame_60.jpg)
</Frame>

Additionally, the document explains how to verify current file permissions and provides the necessary commands to correct any discrepancies. Consider using the following commands:

```bash theme={null}
stat -c %a /etc/kubernetes/manifests/kube-apiserver.yaml
```

```bash theme={null}
chmod 644 /etc/kubernetes/manifests/kube-apiserver.yaml
```

Other important recommendations address the command-line arguments for deploying the Kube API server. The guidelines specify the following:

* Disable anonymous authentication.
* Ensure that basic and token authentication files are not specified.
* Require HTTPS and the proper configuration of certificates.

<Frame>
  ![The image shows a list of security configuration guidelines for Kubernetes API Server from the CIS Kubernetes Benchmark v1.6.0.](https://kodekloud.com/kk-media/image/upload/v1752871344/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-CIS-benchmark-for-Kubernetes/frame_100.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Upcoming sections will provide a deeper examination of these recommendations.
</Callout>

At this stage, we present a high-level overview of the CIS Benchmark Assessment Tool. Previously, the CIS CAT tool was discussed. This tool facilitates automated assessments and generates reports in HTML format. However, note that the free lite version of CIS CAT supports only selected benchmarks (e.g., Windows, Ubuntu, Google Chrome, and macOS) and does not include Kubernetes.

For Kubernetes, an alternate open-source tool—available free of charge—will be introduced later in this course. This tool is designed to perform a CIS Benchmark assessment specifically for Kubernetes, ensuring you can check your configuration against established best practices.

This concludes our overview of the CIS Benchmarks for Kubernetes.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/bf3a22c7-9a9b-44b9-8924-5428c4483728" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 Certificates API
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Certificates-API/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Certificates-API/page)

# Certificates API

> This article covers managing certificates using the Kubernetes Certificates API, including automation of signing requests and certificate rotation for cluster security.

Welcome to this lesson on managing certificates and exploring the Kubernetes Certificates API. In this guide, you’ll learn how Kubernetes automates certificate signing, rotation, and how it integrates with cluster security.

When setting up a Kubernetes cluster, administrators initially configure a Certificate Authority (CA) server to generate certificates for various components. After assigning these certificates to the services, the cluster operates securely. As the cluster administrator, you already have your own certificate and key pair. However, when a new administrator joins your team, they need their own certificate and key to access the cluster. The process involves the new user generating a private key, creating a certificate signing request (CSR), and sending it to you. You then use the CA server—which signs the CSR using its private key and root certificate—to generate a certificate for the user. Note that certificates have a validity period and may require periodic renewal, a process known as certificate rotation.

<Callout icon="lightbulb" color="#1CB2FE">
  The CA server is critically important because it consists of a key and certificate file that can sign certificates for the entire cluster. Unauthorized access to these files could potentially allow anyone to grant privileges within your Kubernetes environment. Ensure these files are secured and managed properly.
</Callout>

In many Kubernetes setups, such as those created with kubeadm, these CA files are stored on the master node.

## Automating Certificate Management with the Certificates API

Traditionally, signing requests were handled manually. However, as the size of teams and clusters grows, automation becomes essential. Kubernetes introduces a built-in Certificates API to streamline handling certificate signing requests (CSRs) and to automate certificate rotation.

Instead of logging into the master node to sign certificates manually, administrators can now create a Kubernetes object called "CertificateSigningRequest" to submit CSRs directly to the API. This object is visible to cluster administrators, making it easy to review, approve, and manage CSRs using simple kubectl commands.

The following diagram illustrates the automated process:

<Frame>
  ![The image illustrates a process involving creating, reviewing, and approving certificate signing requests using a Certificates API, depicted with icons and labeled steps.](https://kodekloud.com/kk-media/image/upload/v1752871345/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Certificates-API/frame_200.jpg)
</Frame>

## Step-by-Step Process

1. **Generate a Private Key and CSR**

   A user, such as Jane, first creates a private key and generates a CSR with their details. Run the following commands:

   ```bash theme={null}
   openssl genrsa -out jane.key 2048
   openssl req -new -key jane.key -subj "/CN=jane" -out jane.csr
   ```

   The generated CSR (jane.csr) will have a structure similar to:

   ```text theme={null}
   -----BEGIN CERTIFICATE REQUEST-----
   MIICWDCCCAAwE...dhk
   -----END CERTIFICATE REQUEST-----
   ```

2. **Submit the CSR to the Administrator**

   The user sends the generated CSR to the administrator. The administrator then creates a Kubernetes CSR object with a manifest file. Under the spec section, specify the groups the user qualifies for and the intended usages of the certificate. Make sure to Base64-encode the CSR before including it in the request field. Here’s an example manifest:

   ```yaml theme={null}
   apiVersion: certificates.k8s.io/v1beta1
   kind: CertificateSigningRequest
   metadata:
     name: jane
   spec:
     groups:
     - system:authenticated
     usages:
     - digital signature
     - key encipherment
     - server auth
     request: <base64-encoded-CSR>
   ```

   Replace `<base64-encoded-CSR>` with your actual Base64-encoded CSR output. Once this manifest is applied, you can review all pending CSRs.

3. **Review Pending CSRs**

   To view pending certificate signing requests, use the following command:

   ```bash theme={null}
   kubectl get csr
   ```

   The output may look like:

   ```bash theme={null}
   NAME   AGE   REQUESTOR           CONDITION
   jane   10m   admin@example.com   Pending
   ```

4. **Approve the CSR**

   After thorough review, approve the request by running:

   ```bash theme={null}
   kubectl certificate approve jane
   ```

   Kubernetes will then sign the certificate using the CA key pair.

5. **Retrieve the Signed Certificate**

   To view the signed certificate in YAML format, execute:

   ```bash theme={null}
   kubectl get csr jane -o yaml
   ```

   The signed certificate appears in Base64-encoded format in the YAML output. Decode it using Base64 utilities and share the decoded certificate with the end user.

   Below is an example of a CSR object with its signed certificate in the status field:

   ```yaml theme={null}
   apiVersion: certificates.k8s.io/v1beta1
   kind: CertificateSigningRequest
   metadata:
     creationTimestamp: 2019-02-13T16:36:43Z
     name: new-user
   spec:
     groups:
     - system:masters
     - system:authenticated
     usages:
     - digital signature
     - key encipherment
     - server auth
     username: kubernetes-admin
   status:
     certificate: |
       L$0tS1CRUdJTiBDRVJUSUZJQ09FURS0tL0tCk1SURDakNDQWL
       Z0F3SUJBZ0lVRmwyQ2wxyXYoawl5M3JNVisreFRQUW0uJ3dnd0R
       Wplb1JaHZjTkFRRUkQlfBd0ZURVRNQkVHQTlRVU4FUtHMlZpw
       lKdVpMjkE9UQX1NVE14TmpNeU1QmFGd1dnY0ZFEl2ajNuSyX
       2dFsD1IRmS5u041c0tS0Z0vXUwzTFM5VZ96hlZ0dWCmIEZ2F
       OMWVRMFBXThJ9N0FvNjVwJclWk1weEVHTkVRU5tdulB1NiwH
       S1h6a61d9DwMEd1MGUQYFKWK1WkVmjbVRfcY3dd2xi0C1i9Dk
       L0tLS0tL1FkTQgOVSVELG5UNVE8=
     conditions:
     - lastUpdateTime: 2019-02-13T16:37:21Z
       message: This CSR was approved by kubectl certificate approve.
       reason: KubectlApprove
       type: Approved
   ```

## Certificate Management in the Kubernetes Control Plane

The Kubernetes control plane components, including the kube-apiserver, scheduler, and controller manager, coordinate to manage cluster operations. Certificate-related operations, such as CSR approval and signing, are performed by the controller manager through dedicated controllers.

The diagram below shows the controller manager as part of the Kubernetes architecture:

<Frame>
  ![The image depicts a diagram of a Kubernetes architecture component, showing the Kube-API Server, Scheduler, and Controller Manager within a container-like structure.](https://kodekloud.com/kk-media/image/upload/v1752871346/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Certificates-API/frame_330.jpg)
</Frame>

A closer look at the certificate operations of the controller manager is presented in the following diagram:

<Frame>
  ![The image shows a diagram labeled "Controller Manager" with two buttons: "CSR-APPROVING" and "CSR-SIGNING."](https://kodekloud.com/kk-media/image/upload/v1752871347/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Certificates-API/frame_340.jpg)
</Frame>

The controller manager requires the CA’s root certificate and private key, which are specified in its configuration. Here’s an excerpt from the configuration file:

```yaml theme={null}
spec:
  containers:
    - command:
      - kube-controller-manager
      - --address=127.0.0.1
      - --cluster-signing-cert-file=/etc/kubernetes/pki/ca.crt
      - --cluster-signing-key-file=/etc/kubernetes/pki/ca.key
      - --controllers=*,bootstrapsigner,tokencleaner
      - --kubeconfig=/etc/kubernetes/controller-manager.conf
      - --leader-elect=true
      - --root-ca-file=/etc/kubernetes/pki/ca.crt
      - --service-account-private-key-file=/etc/kubernetes/pki/sa.key
      - --use-service-account-credentials=true
```

This configuration ensures the controller manager can securely sign certificates and manage certificate lifecycles.

That concludes our lesson on the Kubernetes Certificates API. For further hands-on practice with certificate management, head over to our practice test section and deepen your understanding.

See you in the next lesson!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/ccd63e03-2a71-445c-8276-de3e02645fea" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/f1351e20-2750-4c06-9a4b-814169928fa1" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 Cluster Roles and Role Bindings
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Cluster-Roles-and-Role-Bindings/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Cluster-Roles-and-Role-Bindings/page)

# Cluster Roles and Role Bindings

> This article focuses on cluster roles and role bindings in Kubernetes for managing access to cluster-scoped resources.

In previous lessons, we explored namespaced roles and role bindings. In this section, we focus on cluster roles and cluster role bindings. Unlike namespaced roles—which grant permissions within a specific namespace (or the default namespace when none is specified)—cluster roles are used to control access to cluster-scoped resources.

## Kubernetes Resource Classification

Kubernetes resources fall into two distinct groups:

1. **Namespaced resources** (e.g., pods, replica sets, jobs, deployments, services, secrets)
2. **Cluster-scoped resources** (e.g., nodes, persistent volumes, certificate signing requests, namespaces)

<Frame>
  ![The image illustrates Kubernetes resources categorized into "Namespaced" and "Cluster Scoped" groups, showing different components like pods, nodes, and roles.](https://kodekloud.com/kk-media/image/upload/v1752871348/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Cluster-Roles-and-Role-Bindings/frame_100.jpg)
</Frame>

To view a complete list of namespaced and non-namespaced resources, run the following commands:

```bash theme={null}
kubectl api-resources --namespaced=true
kubectl api-resources --namespaced=false
```

<Callout icon="lightbulb" color="#1CB2FE">
  For namespaced resources, roles and role bindings are used. However, when you need to grant permissions for cluster-wide resources such as nodes or persistent volumes, you should use cluster roles and cluster role bindings.
</Callout>

## Use Case: Granting Cluster-Wide Permissions

Imagine you need to create a cluster role that allows a user to view, create, or delete nodes across the entire cluster. Similarly, you might need a storage administrator role to manage persistent volumes and persistent volume claims. The diagram below outlines a conceptual overview of these roles:

<Frame>
  ![The image outlines cluster roles: "Cluster Admin" can view, create, and delete nodes; "Storage Admin" can view, create PVs, and delete PVCs.](https://kodekloud.com/kk-media/image/upload/v1752871349/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Cluster-Roles-and-Role-Bindings/frame_170.jpg)
</Frame>

## Defining a Cluster Role

Below is an example YAML file that defines a cluster role. Save the file as `cluster-admin-role.yaml`:

```yaml theme={null}
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: cluster-administrator
rules:
- apiGroups: [""]
  resources: ["nodes"]
  verbs: ["list", "get", "create", "delete"]
```

## Binding the Cluster Role to a User

After creating the cluster role, you must create a cluster role binding to associate the user with this role. This binding grants the specified permissions across the cluster. Save the following configuration as `cluster-admin-role-binding.yaml`:

```yaml theme={null}
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: cluster-admin-role-binding
subjects:
- kind: User
  name: cluster-admin
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: cluster-administrator
  apiGroup: rbac.authorization.k8s.io
```

Apply these configurations using the following commands:

```bash theme={null}
kubectl create -f cluster-admin-role.yaml
kubectl create -f cluster-admin-role-binding.yaml
```

<Callout icon="lightbulb" color="#1CB2FE">
  While cluster roles are primarily intended for cluster-scoped resources, they can also be used to grant permissions for namespaced resources. When applied in this context, the permissions extend across all namespaces, unlike a namespaced role that restricts access to a specific namespace.
</Callout>

Kubernetes automatically creates several default cluster roles during cluster setup. In practice tests, you may encounter these default roles in various configurations.

Happy studying and good luck with your Kubernetes journey!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/fb2c7589-78d5-4acc-bc16-6c54ef2e85d4" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/1fe8dad2-d540-4669-a0fc-4cb22f1b8abc" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 Cluster Upgrade Process
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Cluster-Upgrade-Process/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Cluster-Upgrade-Process/page)

# Cluster Upgrade Process

> This guide covers the process of upgrading a Kubernetes clusters control plane components while managing dependencies and minimizing downtime.

Welcome to this comprehensive guide on upgrading your Kubernetes cluster. In this lesson, we explore the process of upgrading the core control plane components while temporarily setting aside external dependencies such as etcd and CoreDNS. This guide builds on our previous discussion about Kubernetes software releases and component versioning.

<Frame>
  ![The image shows a diagram of Kubernetes components and their versions, including kube-apiserver, controller-manager, kube-scheduler, kubelet, kube-proxy, kubectl, ETCD cluster, and CoreDNS.](https://kodekloud.com/kk-media/image/upload/v1752871351/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Cluster-Upgrade-Process/frame_20.jpg)
</Frame>

It is not mandatory for all components to run the same version. Typically, the kube-apiserver—the primary control plane component—must have a version that is equal to or higher than that of the other components. The controller manager and scheduler may lag by one minor version, while kubelet and kube-proxy can lag by two minor versions. For example, if the kube-apiserver is running version v1.10, the controller manager and scheduler can run at either v1.10 or v1.9, and kubelet and kube-proxy may run at v1.8. However, none of these components should exceed the kube-apiserver's version (e.g., v1.11).

The kubectl utility is an exception—it can be one minor version ahead, equal to, or one minor version behind the apiserver. This permissible version skew facilitates live upgrades by allowing one component to be upgraded at a time.

<Callout icon="lightbulb" color="#1CB2FE">
  Upgrading your Kubernetes cluster one minor version at a time ensures smoother transitions and minimizes downtime.
</Callout>

## When to Upgrade

Imagine your cluster is running version 1.10 and Kubernetes has released versions 1.11 and 1.12. Kubernetes supports only the three most recent minor versions at any given time. For instance, if v1.12 is the latest release, then versions 1.12, 1.11, and 1.10 are supported. When v1.13 is released, the supported versions become 1.13, 1.12, and 1.11. It is always advisable to upgrade your cluster to a newer release before your current version falls out of the supported list.

<Frame>
  ![The image shows a timeline of Kubernetes components (kube-apiserver, controller-manager, kube-scheduler, kubectl, kubelet, kube-proxy) at version 1.10, with support status updates.](https://kodekloud.com/kk-media/image/upload/v1752871352/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Cluster-Upgrade-Process/frame_160.jpg)
</Frame>

Direct upgrades from version 1.10 to 1.13 are not recommended. Instead, upgrade one minor version at a time—from 1.10 to 1.11, then from 1.11 to 1.12, and finally from 1.12 to 1.13. The upgrade steps vary depending on your cluster setup. Managed Kubernetes clusters (e.g., on Google Kubernetes Engine) offer a more streamlined upgrade process, while clusters deployed using kubeadm benefit from tools that help plan and execute the upgrade. For clusters set up manually, all components require an individual upgrade.

## Upgrading the Control Plane

Consider a production cluster with master and worker nodes running version 1.10 and hosting live applications. The upgrade process is divided into two major steps:

1. Upgrade the master nodes (control plane components).
2. Upgrade the worker nodes.

During the master node upgrade, the control plane components (API server, scheduler, and controller manager) experience a brief downtime. While management functions (such as kubectl access and new deployments) are temporarily unavailable, workloads on the worker nodes continue to serve users. Post-upgrade, the cluster operates in a supported mixed-version state (for example, masters at v1.11 while workers remain at v1.10).

### Upgrading Worker Nodes: Strategies

There are several strategies for upgrading worker nodes:

1. **Upgrade all worker nodes simultaneously:**\
   This method leads to downtime as pods become unavailable until the upgrade is complete.

<Frame>
  ![The image illustrates "Strategy - 1" with four labeled boxes (M and W) and arrows pointing to a group of people, indicating a process or workflow.](https://kodekloud.com/kk-media/image/upload/v1752871353/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Cluster-Upgrade-Process/frame_320.jpg)
</Frame>

2. **Upgrade one node at a time:**\
   This approach minimizes downtime because workloads are automatically rescheduled to the remaining nodes.

<Frame>
  ![The image illustrates "Strategy - 2" with icons representing groups and processes, using arrows and labeled boxes with versions v1.11 and v1.10.](https://kodekloud.com/kk-media/image/upload/v1752871354/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Cluster-Upgrade-Process/frame_360.jpg)
</Frame>

3. **Add new worker nodes:**\
   Deploy new nodes with the updated version, migrate workloads to them, and decommission the older nodes. This strategy is especially effective in cloud environments.

<Frame>
  ![The image illustrates "Strategy - 3" with three labeled boxes (M and W) and arrows pointing to a group of people, indicating a process or workflow.](https://kodekloud.com/kk-media/image/upload/v1752871355/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Cluster-Upgrade-Process/frame_400.jpg)
</Frame>

## Upgrading with kubeadm

Assume you intend to upgrade your cluster from version 1.11 to 1.13. The kubeadm tool simplifies this process by providing an upgrade command that shows the current cluster version, the kubeadm tool version, and the latest stable Kubernetes version, along with the required steps.

Run the following command to plan the upgrade:

```bash theme={null}
kubeadm upgrade plan
```

The output includes:

* The current cluster version.
* The kubeadm tool version.
* The latest available version in your current series.
* A table indicating which components require manual upgrades post control plane upgrade (typically the kubelet).

For example, the output might look like:

```plaintext theme={null}
[preflight] Running pre-flight checks.
[upgrade] Making sure the cluster is healthy:
[upgrade/config] Making sure the configuration is correct:
[upgrade] Fetching available versions to upgrade to
[upgrade/versions] Cluster version: v1.11.8
[upgrade/versions] kubeadm version: v1.11.3
[upgrade/versions] Latest version in the v1.11 series: v1.11.8

Components that must be upgraded manually after you have
upgraded the control plane with 'kubeadm upgrade apply':
COMPONENT       CURRENT   AVAILABLE
Kubelet         3 x v1.11.3 v1.13.4

Upgrade to the latest stable version:

COMPONENT           CURRENT   AVAILABLE
API Server          v1.11.8   v1.13.4
Controller Manager  v1.11.8   v1.13.4
Scheduler           v1.11.8   v1.13.4
Kube Proxy          v1.11.8   v1.13.4
CoreDNS             v1.1.3    v1.1.3
Etcd                3.2.18    N/A

You can now apply the upgrade by executing the following command:
```

Before proceeding, ensure that the kubeadm tool itself is updated to the target version since it must match the Kubernetes release series.

Remember, only one minor version upgrade is permitted at a time. If you are on v1.11 and wish to reach v1.13, you must first upgrade to v1.12. Begin by upgrading the kubeadm tool:

```bash theme={null}
apt-get upgrade -y kubeadm=1.12.0-00
```

Then, apply the control plane upgrade:

```bash theme={null}
kubeadm upgrade apply v1.12.0
```

Upon successful completion, you should see an output similar to:

```plaintext theme={null}
[upgrade/successful] SUCCESS! Your cluster was upgraded to "v1.12". Enjoy!

[upgrade/kubelet] Now that your control plane is upgraded, please proceed with upgrading your kubelets if you haven't already done so.
```

At this stage, the control plane components have been upgraded to version 1.12. However, running `kubectl get nodes` will show the kubelet version on each node, which might not yet reflect the updated control plane version.

## Upgrading the kubelets

If your master nodes are running kubelet processes, you need to upgrade them as well. Upgrade the kubelet package and then restart the kubelet service.

For example, check the current node versions:

```bash theme={null}
kubectl get nodes
```

The output might be:

```plaintext theme={null}
NAME     STATUS   ROLES    AGE   VERSION
master   Ready    master   1d    v1.11.3
node-1   Ready    <none>   1d    v1.11.3
node-2   Ready    <none>   1d    v1.11.3
```

Proceed to upgrade the kubelet on the master node:

```bash theme={null}
apt-get upgrade -y kubelet=1.12.0-00
systemctl restart kubelet
```

After restarting, verify the upgrade:

```bash theme={null}
kubectl get nodes
```

The output should now reflect:

```plaintext theme={null}
NAME     STATUS   ROLES    AGE   VERSION
master   Ready    master   1d    v1.12.0
node-1   Ready    <none>   1d    v1.11.3
node-2   Ready    <none>   1d    v1.11.3
```

## Upgrading Worker Nodes

Upgrading worker nodes should be performed one at a time to prevent downtime and ensure workloads are rescheduled safely.

1. **Drain the node:**\
   Draining a node evicts its pods and marks it as unschedulable.

   ```bash theme={null}
   kubectl drain node-1
   ```

<Callout icon="lightbulb" color="#1CB2FE">
  Draining ensures that the node is safely prepared for an upgrade without impacting running applications.
</Callout>

2. **Upgrade packages on the worker node:**\
   Upgrade both the kubeadm and kubelet packages.

   ```bash theme={null}
   apt-get upgrade -y kubeadm=1.12.0-00
   apt-get upgrade -y kubelet=1.12.0-00
   kubeadm upgrade node config --kubelet-version v1.12.0
   systemctl restart kubelet
   ```

3. **Mark the node schedulable again:**\
   Once the upgrade is complete, make the node available for new pods.

   ```bash theme={null}
   kubectl uncordon node-1
   ```

Repeat these steps for each worker node. For instance, for node-2:

```bash theme={null}
kubectl drain node-2
apt-get upgrade -y kubeadm=1.12.0-00
apt-get upgrade -y kubelet=1.12.0-00
kubeadm upgrade node config --kubelet-version v1.12.0
systemctl restart kubelet
kubectl uncordon node-2
```

Once every node is upgraded, your cluster will be fully running on version 1.12. You can then repeat similar procedures to upgrade from 1.12 to 1.13.

## Conclusion

This step-by-step guide has walked you through the critical phases of the Kubernetes cluster upgrade process—from planning the control plane upgrade using kubeadm to carefully upgrading your worker nodes. By upgrading one minor version at a time, you ensure that your cluster remains healthy and your applications experience minimal downtime.

For further insights, try upgrading a live cluster with running applications and observe how workloads are seamlessly shifted to minimize disruptions. Happy upgrading!

## Additional Resources

* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Kubernetes Basics](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
* [Kubeadm Upgrade Guide](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/3a682588-ec66-4e9e-9071-d68ab198e50f" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 Demo Cluster Upgrade
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Demo-Cluster-Upgrade/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Demo-Cluster-Upgrade/page)

# Demo Cluster Upgrade

> This lesson demonstrates upgrading a Kubernetes cluster from version 1.28 to 1.29 using kubeadm, following official documentation procedures.

In this lesson, we'll demonstrate upgrading a Kubernetes cluster from version 1.28 to 1.29 using kubeadm. The procedure follows the official Kubernetes documentation under "Tasks → Administer Cluster → Administration with KubeADM → Upgrading a KubeADM Cluster." Although the documentation provides upgrade paths for various version transitions, this demo focuses on moving from v1.28 to the latest v1.29 release.

<Frame>
  ![The image shows a webpage from Kubernetes documentation about upgrading kubeadm clusters, detailing version upgrade paths and linking to additional resources.](https://kodekloud.com/kk-media/image/upload/v1752871356/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Demo-Cluster-Upgrade/frame_50.jpg)
</Frame>

Select the upgrade path that best suits your environment and follow the provided commands. The process remains largely consistent regardless of the version specifics.

***

## Preliminary Steps: Updating Package Repositories

Before starting the upgrade, scroll down the official documentation until you find the important note about changing the package repository. Previously, Kubernetes packages were hosted at `app.kubernetes.io` and `yum.kubernetes.io`, but these repositories have been deprecated. You must now use `packages.k8s.io` to download the latest versions of tools such as kubectl and kubeadm.

<Frame>
  ![The image is a webpage from Kubernetes documentation about changing the package repository, highlighting the deprecation of legacy repositories and recommending new ones.](https://kodekloud.com/kk-media/image/upload/v1752871358/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Demo-Cluster-Upgrade/frame_80.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Before proceeding, ensure that you update the package repository configuration on every cluster node.
</Callout>

### Determine Your Operating System Distribution

To see which operating system you are using, run:

```bash theme={null}
kubectl get nodes
```

On a two-node cluster (one control-plane and one worker node), you can verify your distribution with:

```bash theme={null}
cat /etc/*release
```

If the output indicates Ubuntu 20.04 or another Debian-based distribution, follow the Debian/Ubuntu instructions in the documentation and update your package repository accordingly.

For instance, initially run a command like this:

```bash theme={null}
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.23/deb/ /" | sudo tee /etc/apt/sources.list.d/kubernetes.list
curl -fsSL https://pkgs.k8s.io/core/stable/v1.28/deb/Release.key | sudo apt-key add -
```

To upgrade to v1.29, adjust the version in the command as follows:

```bash theme={null}
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.29/deb/ /" | sudo tee /etc/apt/sources.list.d/kubernetes.list
curl -fsSL https://pkgs.k8s.io/core/stable/v1.29/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
```

After modifying the repository configuration on both control-plane and worker nodes, refresh the package list:

```bash theme={null}
sudo apt-get update
```

***

## Determining the Target Version

To identify the latest available version in the 1.29 series, use these commands:

```bash theme={null}
sudo apt update
sudo apt-cache madison kubeadm
```

You should see output resembling:

```plaintext theme={null}
kubeadm | 1.29.3-1 | https://pkgs.k8s.io/core/stable/v1.29/deb Packages
kubeadm | 1.29.2-1 | https://pkgs.k8s.io/core/stable/v1.29/deb Packages
kubeadm | 1.29.1-1 | https://pkgs.k8s.io/core/stable/v1.29/deb Packages
kubeadm | 1.29.0-1 | https://pkgs.k8s.io/core/stable/v1.29/deb Packages
```

Select the highest version available (for example, 1.29.3-1) and note it for subsequent steps.

***

## Upgrading the Control Plane Node

### Step 1: Upgrade the kubeadm Tool

First, update kubeadm on the control plane node to prepare for the upgrade. Replace the version string with the latest version (e.g., 1.29.3-1.1):

```bash theme={null}
sudo apt-mark unhold kubeadm && \
sudo apt-get update && \
sudo apt-get install -y kubeadm='1.29.3-1.1' && \
sudo apt-mark hold kubeadm
```

Verify the upgrade by checking the version:

```bash theme={null}
kubeadm version
```

Expected output:

```plaintext theme={null}
kubeadm version: &version.Info{Major:"1", Minor:"29", GitVersion:"v1.29.3", GitCommit:"6813625b7cd706db5c7388921be03071e14a294", GitTreeState:"clean", BuildDate:"2024-03-15T00:06:16Z", GoVersion:"go1.21.8", Compiler:"gc", Platform:"linux/amd64"}
```

### Step 2: Run the Upgrade Plan

Before applying the upgrade, conduct a dry run to see the available upgrade options. This command will outline which components upgrade automatically and those requiring manual updates (e.g., kubelet):

```bash theme={null}
sudo kubeadm upgrade plan
```

The output should indicate that your cluster is currently at v1.28.0 with the target control plane version of v1.29.3. Typically, kubeadm upgrades essential components such as the API server, controller manager, scheduler, and kube-proxy automatically, while kubelet must be updated separately.

### Step 3: Apply the Upgrade

Initiate the upgrade process for the control plane:

```bash theme={null}
sudo kubeadm upgrade apply v1.29.3
```

Monitor the progress as the system renews certificates, updates static pod manifests, and restarts components. After a successful upgrade, you may see messages similar to:

```plaintext theme={null}
[upgrade/successful] SUCCESS! Your cluster was upgraded to "v1.29.3". Enjoy!
[upgrade/kubelet] Now that your control plane is upgraded, please proceed with upgrading your kubelets if you haven't already done so.
```

Keep in mind that when you verify node versions via `kubectl get nodes`, the displayed version corresponds to the kubelet, which will still show v1.28.0 until its upgrade is completed.

***

## Upgrading kubelet and kubectl on the Control Plane Node

### Drain the Control Plane Node

Before upgrading kubelet (which runs outside the control plane pods), drain the control plane node to ensure safe maintenance:

```bash theme={null}
kubectl drain controlplane --ignore-daemonsets
```

### Upgrade kubelet and kubectl

Next, update kubelet and kubectl on the control plane node by specifying the target version:

```bash theme={null}
sudo apt-mark unhold kubelet kubectl && \
sudo apt-get update && \
sudo apt-get install -y kubelet='1.29.3-1.1' kubectl='1.29.3-1.1' && \
sudo apt-mark hold kubelet kubectl
```

Restart the kubelet service to apply the changes:

```bash theme={null}
sudo systemctl daemon-reload
sudo systemctl restart kubelet
```

Finally, confirm the node version:

```bash theme={null}
kubectl get nodes
```

Since the control plane node might still be marked as “SchedulingDisabled” due to the drain operation, uncordon it to allow scheduling:

```bash theme={null}
kubectl uncordon controlplane
```

***

## Upgrading Worker Nodes

Follow a similar process to upgrade each worker node.

### Step 1: Upgrade kubeadm on the Worker Node

On each worker node, upgrade kubeadm with:

```bash theme={null}
sudo apt-mark unhold kubeadm && \
sudo apt-get update && \
sudo apt-get install -y kubeadm='1.29.3-1.1' && \
sudo apt-mark hold kubeadm
```

Then, from a control plane node, initiate the upgrade for the worker node:

```bash theme={null}
sudo kubeadm upgrade node
```

### Step 2: Drain the Worker Node

Drain the worker node to safely upgrade kubelet. Replace `<node-name>` with the actual name of your worker node:

```bash theme={null}
kubectl drain <node-name> --ignore-daemonsets
```

If you encounter issues related to DaemonSet-managed pods, ensure that the `--ignore-daemonsets` flag is used correctly. Refer to `kubectl drain --help` for further details if needed.

### Step 3: Upgrade kubelet and kubectl on the Worker Node

Upgrade the kubelet and kubectl packages with:

```bash theme={null}
sudo apt-mark unhold kubelet kubectl && \
sudo apt-get update && \
sudo apt-get install -y kubelet='1.29.3-1.1' kubectl='1.29.3-1.1' && \
sudo apt-mark hold kubelet kubectl
```

Restart the kubelet service:

```bash theme={null}
sudo systemctl daemon-reload
sudo systemctl restart kubelet
```

After the upgrade, uncordon the worker node to resume scheduling:

```bash theme={null}
kubectl uncordon <node-name>
```

Finally, verify that all nodes are upgraded:

```bash theme={null}
kubectl get nodes
```

Both control-plane and worker nodes should now display version v1.29.3.

***

## Summary

This guide has detailed the process of upgrading a Kubernetes cluster using kubeadm. The critical steps include:

1. Updating the package repository to `packages.k8s.io`.
2. Determining the target version available from the repository.
3. Upgrading the control plane by updating kubeadm, applying the upgrade, and then updating kubelet and kubectl.
4. Draining nodes before performing kubelet upgrades and uncordoning them afterwards.
5. Repeating the process on each worker node.

By following these steps, you ensure that every component of your Kubernetes cluster is updated properly, maintaining compatibility with the newer version. Happy upgrading!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/28d5ca34-88c2-4e74-b380-cf3667420462" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/f797f920-c9d5-420c-b2b4-3c8904f42b47" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 Developing Network Policies
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Developing-Network-Policies/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Developing-Network-Policies/page)

# Developing Network Policies

> This article explores Kubernetes network policies to secure database pods by controlling traffic from API pods using practical scenarios and YAML configurations.

In this lesson, we will explore network policies in detail using a practical scenario. We have a web API and database pods, and our goal is to secure the database pod such that it only accepts traffic from the API pod on port 3306. Traffic from the web pod is not restricted and can be ignored for this policy.

By default, Kubernetes allows all pods to communicate. To restrict access, we first create a network policy—named "db-policy"—that targets the database pod using labels and selectors. In our example, the database pod has the label "role: db". By applying the network policy with a pod selector based on this label, all incoming (ingress) traffic is blocked until explicit allowances are defined.

Below is the basic YAML for an ingress-only network policy that permits database queries from the API pod on port 3306:

```yaml theme={null}
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: db-policy
spec:
  podSelector:
    matchLabels:
      role: db
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          name: api-pod
    ports:
    - protocol: TCP
      port: 3306
```

In this configuration, ingress traffic is allowed only from pods labeled as "api-pod". Keep in mind that once ingress traffic is accepted, the corresponding response traffic is automatically permitted. Therefore, an egress rule is not required for this scenario unless the database pod initiates connections (for example, calling an API).

<Callout icon="lightbulb" color="#1CB2FE">
  If your database pod ever needs to initiate outbound connections, you'll need to define a separate egress rule to manage that traffic.
</Callout>

## Using Additional Selectors

There are many scenarios where more granular control is needed. For instance, imagine you have multiple API pods in different namespaces (dev, test, and prod), but you only want the API pod in the prod namespace to connect to the database pod. To enforce this, combine a namespace selector with a pod selector in the ingress rule:

```yaml theme={null}
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: db-policy
spec:
  podSelector:
    matchLabels:
      role: db
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          name: api-pod
      namespaceSelector:
        matchLabels:
          name: prod
    ports:
    - protocol: TCP
      port: 3306
```

In the above configuration, traffic is only allowed if a pod meets both conditions: it must be labeled as "api-pod" and reside in a namespace with the label "prod". Be cautious when structuring your selectors. Separating the pod and namespace selectors into different list items (each with its own dash) results in an OR operation, which could unintentionally permit more sources.

Another common scenario involves allowing an external resource, such as a backup server, to access the database pod. Since the backup server is external to the Kubernetes cluster, pod or namespace selectors cannot be used. Instead, define an IP block to specify the allowed address. For example, if the backup server has an IP address of 192.168.5.10, the ingress rule can be defined as follows:

```yaml theme={null}
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: db-policy
spec:
  podSelector:
    matchLabels:
      role: db
  policyTypes:
  - Ingress
  ingress:
  - from:
    - ipBlock:
        cidr: 192.168.5.10/32
    ports:
    - protocol: TCP
      port: 3306
```

Multiple selectors can be combined within a single rule (using an AND condition) or as separate entries (using an OR condition). The example below demonstrates both a combined rule and a rule for a specific IP block:

```yaml theme={null}
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: db-policy
spec:
  podSelector:
    matchLabels:
      role: db
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          name: api-pod
      namespaceSelector:
        matchLabels:
          name: prod
    - ipBlock:
        cidr: 192.168.5.10/32
  ports:
  - protocol: TCP
    port: 3306
```

In this combined configuration, traffic is allowed if it either meets the criteria of being from the API pod in the prod namespace or matches the specific IP block.

## Adding Egress Rules

Consider the situation where the database pod must initiate outbound connections—such as pushing backups to an external backup server. Here, an egress rule is necessary, as this traffic originates from the database pod.

To enable both ingress and egress rules in a single network policy, include "Egress" in the policyTypes array and define an egress section. In the example below, the database pod is allowed to send outbound traffic to the external backup server (using an IP block) on port 80:

```yaml theme={null}
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: db-policy
spec:
  podSelector:
    matchLabels:
      role: db
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          name: api-pod
      namespaceSelector:
        matchLabels:
          name: prod
    - ipBlock:
        cidr: 192.168.5.10/32
  ports:
  - protocol: TCP
    port: 3306
  egress:
  - to:
    - ipBlock:
        cidr: 192.168.5.10/32
    ports:
    - protocol: TCP
      port: 80
```

This complete policy ensures that:

* Only traffic from the API pod in the prod namespace (or the specific external IP) is allowed to access the database pod on port 3306.
* Outbound connections from the database pod to the designated external backup server on port 80 are permitted.

<Callout icon="lightbulb" color="#1CB2FE">
  For more detailed explanations on Kubernetes network policies and advanced configurations, check out the [Kubernetes Documentation](https://kubernetes.io/docs/concepts/services-networking/network-policies/).
</Callout>

That concludes our discussion on network policies, covering the use of selectors, IP blocks, as well as ingress and egress rules. It's time to put your knowledge into practice by working on your own network policy configurations.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/7e0076f4-851d-4b86-ac99-ee9d278bcaaa" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/ef4c8e94-d23b-49e4-83ec-ac284382f1fd" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 Docker Securing the Daemon
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Docker-Securing-the-Daemon/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Docker-Securing-the-Daemon/page)

# Docker Securing the Daemon

> This guide explains securing the Docker daemon to protect containerized infrastructure and demonstrates steps to harden the Docker host and API.

This guide explains why securing the Docker daemon is critical for protecting your containerized infrastructure. It demonstrates practical steps to harden both the Docker host and the Docker API. Inadequate protection can allow attackers to delete containers and volumes, run malicious containers (e.g., for unauthorized cryptocurrency mining), and even gain root access on the host system—potentially compromising your entire network.

## Risks of an Unsecured Docker Daemon

If an unauthorized individual gains access to your Docker daemon, they can:

* Delete containers hosting your applications, leading to service disruptions.
* Erase Docker volumes that store critical application data, which may result in data loss.
* Launch their own containers, possibly with privileged access, to compromise the host system and other networked devices.

By default, Docker restricts access by binding the Docker API to a Unix socket, which limits interaction to users logged into the host. However, if you configure Docker to accept external connections, implementing additional security measures is essential.

## Securing the Docker Host

Before modifying Docker’s configuration, ensure that the host system is secured by following standard server hardening practices:

* Disable direct root user login.
* Limit access exclusively to trusted users.
* Use SSH key-based authentication instead of password-based authentication.
* Restrict or close unused network ports.

<Callout icon="lightbulb" color="#1CB2FE">
  Regularly review and update your server security measures to keep pace with evolving threats.
</Callout>

## Exposing the Docker Daemon Externally

In scenarios such as remote administration or integration with container management tools, you might need to allow external access to the Docker daemon. To do so, modify the Docker daemon configuration file by adding a hosts option. For example, to expose the daemon on a private IP address, update `/etc/docker/daemon.json` as follows:

```json theme={null}
{
  "hosts": [ "tcp://192.168.1.10:2375" ]
}
```

Ensure that the Docker daemon is bound only to private network interfaces. If your host has a public-facing interface, verify that the Docker daemon is not accessible there.

## Encrypting Communication with TLS

Exposing the Docker daemon externally necessitates secure communication through TLS encryption. To enable TLS:

1. Set up a Certificate Authority (CA) and generate server certificates (e.g., `server.pem` and `serverkey.pem`).
2. Modify the configuration to enable TLS and change the port to 2376.

A recommended configuration with certificate-based authentication in `/etc/docker/daemon.json` is as follows:

```json theme={null}
{
  "hosts": ["tcp://192.168.1.10:2376"],
  "tls": true,
  "tlscert": "/var/docker/server.pem",
  "tlskey": "/var/docker/serverkey.pem",
  "tlsverify": true,
  "tlscacert": "/var/docker/cacert.pem"
}
```

With this setup, Docker listens on port 2376, ensuring encrypted communication. However, while TLS ensures that traffic is encrypted, it does not enforce client authentication by itself.

<Callout icon="triangle-alert" color="#FF6B6B">
  Do not rely solely on TLS encryption. Make sure to enable certificate-based authentication to verify the identity of clients connecting to your Docker daemon.
</Callout>

## Enabling Certificate-Based Authentication

To restrict Docker daemon access only to clients with valid CA-signed certificates, follow these steps:

1. On the Server:
   * Copy the Certificate Signing Request (CSR) and set the TLS CSR parameter in the daemon configuration file.
   * Enable `tlsverify` to enforce certificate checks.
2. Generate client certificates (e.g., `client.pem` and `client-key.pem`) signed by your CA.
3. Provide these client certificates along with your CA certificate (`cacert.pem`) only to trusted users.

On the client side, configure Docker to use TLS verification. The Docker client can automatically detect certificates stored in the `.docker` directory in the user’s home folder, or they can be specified manually via command-line options.

For example, set up the client environment as follows:

```bash theme={null}
export DOCKER_TLS_VERIFY=true
export DOCKER_HOST="tcp://192.168.1.10:2376"
docker --tlscert=<path_to_cert> --tlskey=<path_to_key> --tlscacert=<path_to_ca_cert> ps
```

These settings ensure that the Docker CLI communicates securely with the Docker server, permitting only clients with valid, signed certificates to perform operations.

## Summary

* By default, the Docker daemon is bound to a Unix socket, which limits access to the local host.
* When external access is required, update `/etc/docker/daemon.json` to bind the daemon to a TCP interface and enable TLS encryption.
* TLS encrypts traffic, but enforce authentication by enabling `tlsverify` and using CA-signed certificates on both the server and client sides.
* On the client side, configure environment variables or command-line options to supply the necessary TLS certificates.

Following these best practices will enhance the security of your Docker daemon and ensure that the communication between your clients and the Docker server remains both encrypted and authenticated. Happy securing!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/17d0025c-1893-4764-9209-4826c7de5a06" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 Docker Service Configuration
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Docker-Service-Configuration/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Docker-Service-Configuration/page)

# Docker Service Configuration

> This article explains how to configure the Docker daemon service on Linux using systemd, including starting, stopping, and managing the service.

In this lesson, we explore how to configure the Docker daemon service on Linux using systemd. We build on basic service management commands such as start, status, and stop. Note that procedures may vary depending on your operating system and Docker installation method.

## Checking the Docker Service Status

To verify that the Docker service is running, use the following command:

```bash theme={null}
systemctl status docker
```

This command produces output similar to:

```plaintext theme={null}
● docker.service - Docker Application Container Engine
   Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
   Active: active (running) since Wed 2020-10-21 04:21:01 UTC; 3 days ago
     Docs: https://docs.docker.com
 Main PID: 4197 (dockerd)
    Tasks: 13
   Memory: 129.7M
      CPU: 9min 6.980s
   CGroup: /system.slice/docker.service
           └─4197 /usr/bin/dockerd -H fd:// -H tcp://0.0.0.0 --containerd=/run/containerd/containerd.sock
```

## Starting and Stopping the Docker Service

You can control the Docker service using the following commands:

<Callout icon="lightbulb" color="#1CB2FE">
  To start Docker, run:

  ```bash theme={null}
  systemctl start docker
  ```

  To stop Docker, run:

  ```bash theme={null}
  systemctl stop docker
  ```
</Callout>

Running Docker as a systemd service allows the daemon to run in the background and automatically start at boot. Alternatively, you can run the Docker daemon in the foreground using the `dockerd` command, which is particularly useful for troubleshooting.

## Running the Docker Daemon in the Foreground

When you run the daemon in the foreground, log messages are printed directly to the console. For example, you can start the daemon in debug mode with:

```bash theme={null}
dockerd --debug
```

The output will include debug messages similar to the following:

```plaintext theme={null}
INFO[2020-10-24T08:20:40.372653436Z] Starting up
INFO[2020-10-24T08:20:40.375298351Z] parsed scheme: "unix"
INFO[2020-10-24T08:20:40.375510773Z] scheme "unix" not registered, fallback to default scheme  module=grpc
INFO[2020-10-24T08:20:40.375657667Z] ccResolverWrapper: sending update to cc: [{unix:///run/containerd/containerd.sock 0 <nil>}] <nil> module=grpc
INFO[2020-10-24T08:20:40.375973480Z] ClientConn switching balancer to "pick_first"  module=grpc
INFO[2020-10-24T08:20:40.381198263Z] [graphdriver] using prior storage driver: overlay2
WARN[2020-10-24T08:20:40.572888603Z] Your kernel does not support swap memory limit
WARN[2020-10-24T08:20:40.573141192Z] Your kernel does not support cgroup rt period
WARN[2020-10-24T08:20:40.573408479Z] Your kernel does not support cgroup rt runtime
```

For even more detailed logs, the `--debug` flag will output additional information:

```bash theme={null}
dockerd --debug
```

This produces verbose logs, including:

```plaintext theme={null}
INFO[2020-10-24T08:29:00.331925176Z] Starting up
DEBU[2020-10-24T08:29:00.332463203Z] Listener created for HTTP on unix (/var/run/docker.sock)
INFO[2020-10-24T08:29:00.333116936Z] Golang's threads limit set to 6930
INFO[2020-10-24T08:29:00.333695956Z] parsed scheme: "unix"
INFO[2020-10-24T08:29:00.333705237Z] scheme "unix" not registered, fallback to default scheme  module=grpc
INFO[2020-10-24T08:29:00.333712042Z] ccResolverWrapper: sending update to cc: [{unix:///run/containerd/containerd.sock 0 <nil>}] <nil> module=grpc
INFO[2020-10-24T08:29:00.334889983Z] parsed scheme: "unix"
INFO[2020-10-24T08:29:00.334896126Z] scheme "unix" not registered, fallback to default scheme  module=grpc
INFO[2020-10-24T08:29:00.334913273Z] ccResolverWrapper: sending update to cc: [{unix:///run/containerd/containerd.sock 0 <nil>}] <nil> module=grpc
INFO[2020-10-24T08:29:00.335168292Z] Using default logging driver json-file
[graphdriver] priority list: [btrfs zfs overlay2 aufs overlay devicemapper vfs]
INFO[2020-10-24T08:29:00.335695827Z] processing event stream
DEBU[2020-10-24T08:29:00.337633123Z] backingFs=extfs, projectQuotaSupported=false, indexOff="" storage-driver=overlay2
[graphdriver] using prior storage driver: overlay2
WARN[2020-10-24T08:29:00.364679147Z] Initialized graph driver overlay2
WARN[2020-10-24T08:29:00.364679177Z] Your kernel does not support swap memory limit
WARN[2020-10-24T08:29:00.364679192Z] Your kernel does not support cgroup rt period
WARN[2020-10-24T08:29:00.364679207Z] Your kernel does not support cgroup rt runtime
```

## Docker CLI Communication via Unix Socket

When the Docker daemon starts, it listens on an internal Unix socket at `/var/run/docker.sock`. This Inter-Process Communication (IPC) mechanism allows local processes, especially the Docker CLI, to interact with the daemon.

## Remote Access to the Docker Daemon

If you need to manage Docker containers on a remote host—for instance, from your laptop targeting a server—you must configure the Docker daemon to listen on a TCP interface. By default, Docker listens only on the Unix socket, so it is necessary to explicitly specify a TCP host.

For example, if your Docker host has an IP address of `192.168.1.10` and you want to listen on port `2375`, start the daemon as follows:

```bash theme={null}
dockerd --debug \
  --host=tcp://192.168.1.10:2375
```

Then, on your laptop, set the environment variable to interact with the remote Docker host:

```bash theme={null}
export DOCKER_HOST="tcp://192.168.1.10:2375"
docker ps
```

<Callout icon="triangle-alert" color="#FF6B6B">
  Exposing the Docker API over TCP without encryption or authentication represents a significant security risk. Unauthorized users who can access this interface may run containers on your host for malicious purposes.
</Callout>

## Enabling TLS for Secure Communication

To secure the TCP interface, enable TLS encryption. First, generate TLS certificates and then start the Docker daemon with the appropriate TLS flags. TLS-secured Docker daemons typically listen on port `2376`.

Set the `DOCKER_HOST` environment variable accordingly:

```bash theme={null}
export DOCKER_HOST="tcp://192.168.1.10:2376"
docker ps
```

Start the Docker daemon with TLS enabled:

```bash theme={null}
dockerd --debug \
  --host=tcp://192.168.1.10:2376 \
  --tls=true \
  --tlscert=/var/docker/server.pem \
  --tlskey=/var/docker/serverkey.pem
```

## Using a Configuration File

Instead of setting all the options on the command line, you can use a configuration file located at `/etc/docker/daemon.json`. This JSON file is not created by default, so you must create it manually. Here is an example configuration:

```json theme={null}
{
  "debug": true,
  "hosts": ["tcp://192.168.1.10:2376"],
  "tls": true,
  "tlscert": "/var/docker/server.pem",
  "tlskey": "/var/docker/serverkey.pem"
}
```

The `hosts` property is an array that can include multiple listeners. Once this configuration file is in place, you no longer need to pass these options on the command line when starting Docker.

<Callout icon="triangle-alert" color="#FF6B6B">
  If a parameter is specified both in the `daemon.json` file and via command-line flags, Docker will report a conflict and fail to start. For example, conflicting `debug` settings will cause an error.
</Callout>

After updating the configuration file, restart the Docker service with:

```bash theme={null}
systemctl start docker
```

This configuration file is also used when starting Docker as a systemd service.

***

That concludes our lesson on Docker service configuration. For further details on Docker functionalities, please refer to the [Docker Documentation](https://docs.docker.com).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/ba404fff-7bc0-42ff-9430-ba10009a2e47" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 Ingress
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Ingress/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Ingress/page)

# Ingress

> This article explains Ingress in Kubernetes, detailing its role in managing external access to applications and providing routing configurations.

Welcome to this comprehensive lesson on Ingress in Kubernetes. In this article, we revisit Kubernetes services and guide you through the process of understanding and implementing Ingress—a critical component for managing external access to your cluster-based applications.

Imagine deploying an online store application at myonlinestore.com. First, you build your application into a Docker image and deploy it on your Kubernetes cluster as a pod within a Deployment. Your application requires a MySQL database, so you deploy MySQL as a pod and expose it internally using a ClusterIP service named MySQL service.

To enable external access, you create a NodePort service that exposes your application on a high port (for example, port 38080). With this setup, users can access your application by navigating to http\://\<node-IP>:38080. Even when scaling the application by increasing the number of pod replicas, the NodePort service efficiently handles traffic distribution.

However, for production-grade applications, you often need more advanced configurations. Consider these enhancements:

* Configuring a DNS server that points to your node IPs so that users access your application via a friendly domain name (like myonlinestore.com).
* Eliminating the need for users to remember port numbers by using a proxy server that forwards requests from port 80 (or 443 for HTTPS) to the NodePort (38080).

In a public cloud environment such as Google Cloud Platform (GCP), instead of using a NodePort service, you can opt for a LoadBalancer service. Kubernetes will create an internal NodePort and simultaneously instruct GCP to provision a network load balancer. GCP then sets up the load balancer with an external IP address for your DNS settings.

As your business expands, you may introduce additional services (for example, a video streaming service available at myonlinestore.com/watch) while keeping your original application at myonlinestore.com/wear. Although these services are developed separately (with distinct Deployments and LoadBalancer services), managing multiple load balancers can be costly and complex. You need to consolidate traffic by directing it based on URL paths and configure centralized SSL termination.

<Frame>
  ![The image illustrates a network flow diagram for an online store, showing a proxy server and a NodePort service directing traffic to multiple "wear" services.](https://kodekloud.com/kk-media/image/upload/v1752871359/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Ingress/frame_140.jpg)
</Frame>

This is where Ingress proves its value. Ingress offers a single externally accessible URL that routes incoming requests to various services within the cluster based on URL paths or hostnames, while also handling SSL termination. Essentially, Ingress acts as a layer-7 load balancer built into Kubernetes, configured using native Kubernetes objects. Although you still need to expose the Ingress controller via a NodePort or a cloud-native load balancer, all advanced load balancing, authentication, SSL, and URL routing settings are managed on the Ingress controller.

Without Ingress, you would manually deploy and manage reverse proxies like NGINX, HAProxy, or Traefik, configuring URL routes and SSL certificates for each. With Ingress, you simply deploy an Ingress controller (the proxy) and define Ingress resources (the routing rules) as Kubernetes objects.

<Frame>
  ![The image illustrates a load balancing architecture for an online store, distributing traffic between "wear" and "video" services using GCP load balancers.](https://kodekloud.com/kk-media/image/upload/v1752871360/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Ingress/frame_380.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Kubernetes does not include an Ingress controller by default. If you create Ingress resources without one, they will not function. Ensure you deploy a supported Ingress controller, such as NGINX, GCE, Contour, HAProxy, Traefik, or Istio. In this lesson, we use NGINX as an example.
</Callout>

## Deploying an NGINX Ingress Controller

The NGINX Ingress Controller monitors the Kubernetes cluster for Ingress resource definitions and adjusts its configuration accordingly. Typically, it is deployed as a Deployment.

Below is an example Deployment definition for the NGINX Ingress Controller:

```yaml theme={null}
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx-ingress-controller
spec:
  replicas: 1
  selector:
    matchLabels:
      name: nginx-ingress
  template:
    metadata:
      labels:
        name: nginx-ingress
    spec:
      containers:
        - name: nginx-ingress-controller
          image: quay.io/kubernetes-ingress-controller/nginx-ingress-controller:0.21.0
          args:
            - /nginx-ingress-controller
```

This configuration creates a single replica of the NGINX Ingress Controller using an image built specifically for Kubernetes, with the pod appropriately labeled.

To decouple configuration data from the container image (such as log paths and SSL settings), you can provide a reference to a ConfigMap. Here’s an updated Deployment with a ConfigMap reference:

```yaml theme={null}
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx-ingress-controller
spec:
  replicas: 1
  selector:
    matchLabels:
      name: nginx-ingress
  template:
    metadata:
      labels:
        name: nginx-ingress
    spec:
      containers:
      - name: nginx-ingress-controller
        image: quay.io/kubernetes-ingress-controller/nginx-ingress-controller:0.21.0
        args:
        - /nginx-ingress-controller
        - --configmap=$(POD_NAMESPACE)/nginx-configuration
---
kind: ConfigMap
apiVersion: v1
metadata:
  name: nginx-configuration
```

Additionally, the Ingress controller requires specific environment variables (to capture the pod’s name and namespace) and needs to expose ports 80 and 443. Create a Service and ServiceAccount to expose the controller and provide it with the necessary permissions:

```yaml theme={null}
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx-ingress-controller
spec:
  replicas: 1
  selector:
    matchLabels:
      name: nginx-ingress
  template:
    metadata:
      labels:
        name: nginx-ingress
    spec:
      containers:
        - name: nginx-ingress-controller
          image: quay.io/kubernetes-ingress-controller/nginx-ingress-controller:0.21.0
          args:
            - /nginx-ingress-controller
            - --configmap=$(POD_NAMESPACE)/nginx-configuration
          env:
            - name: POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
            - name: POD_NAMESPACE
              valueFrom:
                fieldRef:
                  fieldPath: metadata.namespace
          ports:
            - name: http
              containerPort: 80
            - name: https
              containerPort: 443
```

```yaml theme={null}
apiVersion: v1
kind: Service
metadata:
  name: nginx-ingress
spec:
  type: NodePort
  ports:
    - port: 80
      targetPort: 80
      protocol: TCP
      name: http
    - port: 443
      targetPort: 443
      protocol: TCP
      name: https
  selector:
    name: nginx-ingress
```

```yaml theme={null}
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-configuration
```

```yaml theme={null}
apiVersion: v1
kind: ServiceAccount
metadata:
  name: nginx-ingress-serviceaccount
```

In this complete configuration, the Deployment, Service, ConfigMap, and ServiceAccount work together to deploy the NGINX Ingress Controller with proper exposure and permissions. Once deployed, the controller will continuously monitor the cluster for Ingress resources and dynamically adjust its configuration.

## Configuring Ingress Resources

Ingress resources define routing rules for how external traffic reaches your services within the cluster. These rules can be based on URL paths or the domain name (host).

### Basic Ingress Resource

For a simple setup where all traffic is forwarded to a single backend service, define your Ingress resource as follows:

```yaml theme={null}
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: ingress-wear
spec:
  backend:
    serviceName: wear-service
    servicePort: 80
```

This configuration directs all incoming traffic to the `wear-service` on port 80.

### Ingress with Multiple URL Paths

If you need to route traffic based on different URL paths—such as sending `/wear` traffic to one service and `/watch` traffic to another—define an Ingress resource with explicit rules:

```yaml theme={null}
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: ingress-wear-watch
spec:
  rules:
  - http:
      paths:
      - path: /wear
        backend:
          serviceName: wear-service
          servicePort: 80
      - path: /watch
        backend:
          serviceName: watch-service
          servicePort: 80
```

In this configuration, a single rule handles traffic for the domain (e.g., myonlinestore.com), routing the requests to the appropriate backend based on the URL path.

After you create this Ingress resource using `kubectl create -f`, inspect it with:

```console theme={null}
kubectl describe ingress ingress-wear-watch
```

This command displays the defined rules and backend configurations, ensuring that traffic is properly directed.

### Ingress Based on Domain Names

When you want to split traffic based on host names rather than URL paths, define separate rules using the host field. For example:

```yaml theme={null}
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: ingress-wear-watch
spec:
  rules:
  - host: wear.my-online-store.com
    http:
      paths:
      - backend:
          serviceName: wear-service
          servicePort: 80
  - host: watch.my-online-store.com
    http:
      paths:
      - backend:
          serviceName: watch-service
          servicePort: 80
```

In this case, traffic directed to `wear.my-online-store.com` reaches the `wear-service`, while requests to `watch.my-online-store.com` are forwarded to the `watch-service`. You can also configure multiple paths under each host if needed.

### Default Backend

If a user visits a URL that doesn’t match any defined rule (for example, myonlinestore.com/listen), you can specify a default backend to display a custom 404 page or message.

## Summary

Ingress in Kubernetes provides a unified and simplified approach to managing external access. It enables host- or URL-based routing, handles SSL termination, and minimizes the complexity associated with managing multiple load balancers. By defining Ingress resources and controllers as native Kubernetes objects, you ease the deployment, maintenance, and scalability challenges.

<Frame>
  ![The image illustrates an ingress architecture on Google Cloud Platform, showing load balancing for "wear" and "video" services.](https://kodekloud.com/kk-media/image/upload/v1752871361/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Ingress/frame_440.jpg)
</Frame>

In this article, we compared two approaches to configuring Ingress:

* Splitting traffic by URL within a single rule using multiple paths.
* Splitting traffic by domain name using separate rules.

Both strategies allow detailed routing configurations to ensure that each request is effectively directed based on the defined rules.

<Frame>
  ![The image shows a diagram with URL paths and rules for an online store, including paths for "wear," "watch," "returns," and "support," with associated images.](https://kodekloud.com/kk-media/image/upload/v1752871362/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Ingress/frame_1000.jpg)
</Frame>

<Frame>
  ![The image outlines ingress resource rules for different URLs, categorizing paths like "/wear," "/watch," and "/support" under specific rules with associated images.](https://kodekloud.com/kk-media/image/upload/v1752871363/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Ingress/frame_1030.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  In practice, you can experiment with two types of labs:

  1. An environment where the Ingress controller, resources, and applications are already deployed. Observe the configurations, gather data, and answer related questions.
  2. More challenging scenarios where you deploy the Ingress controller and resources from scratch.
</Callout>

Good luck with your Kubernetes Ingress deployments, and happy learning! See you in the next article.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/1b967f0e-9cd2-4ae0-8d0a-5c1ee62c8063" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 Kube bench
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Kube-bench/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Kube-bench/page)

# Kube bench

> This article explores assessing Kubernetes security configurations using Kube-Bench, an open-source tool for verifying compliance with CIS Benchmarks.

In this article, we explore how to assess Kubernetes security configurations using Kube-Bench. Developed by Aqua Security, Kube-Bench is an open-source tool that automatically verifies whether your Kubernetes deployment follows the best practices outlined in the CIS Benchmarks.

The following image displays an excerpt from the CIS Kubernetes Benchmark. It illustrates various security configuration checks and indicates pass/fail results for master node settings as determined by Kube-Bench.

<Frame>
  ![The image shows a CIS Kubernetes Benchmark excerpt with security configuration checks, displaying pass/fail results for master node settings using kube-bench.](https://kodekloud.com/kk-media/image/upload/v1752871365/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Kube-bench/frame_30.jpg)
</Frame>

## Best Practices and Automated Assessment

Kube-Bench aligns its assessment with the list of recommended CIS best practices for Kubernetes. For each CIS recommendation, there’s a corresponding check performed by the tool. This systematic approach helps you quickly identify potential security issues in your cluster configurations.

## Deploying and Using Kube-Bench

There are several methods available to deploy and run Kube-Bench:

* **As a Docker Container:** Run Kube-Bench in isolation using Docker.
* **As a Kubernetes Job:** Deploy Kube-Bench as a job within your Kubernetes cluster to regularly monitor compliance.
* **Using Binaries or Compiling from Source:** Install the tool directly on a master node or compile it from source for customized use.

<Callout icon="lightbulb" color="#1CB2FE">
  Ensure you select the deployment method that best fits your operational workflow and cluster management strategy. Running Kube-Bench as a Kubernetes job can simplify scheduled assessments.
</Callout>

## Step-by-Step Process

1. **Identify the Stable Kube-Bench Version:**\
   Visit [Kube-Bench on GitHub](https://github.com/aquasecurity/kube-bench) and select a stable release version that is compatible with your Kubernetes cluster.

2. **Install on a Master Node:**\
   Once you have selected the appropriate version, install Kube-Bench on one of your master nodes.

3. **Run the Security Assessment:**\
   Execute the tool to perform an assessment of your Kubernetes configurations against the CIS Benchmarks.

4. **Review the Results:**\
   Kube-Bench will generate a report with the pass/fail statuses for each CIS recommendation. Analyze this report to identify any potential security vulnerabilities.

5. **Remediate Identified Issues:**\
   Follow the remediation steps suggested by Kube-Bench to address security gaps. After applying fixes, re-run the assessment to confirm compliance.

<Callout icon="lightbulb" color="#1CB2FE">
  Regularly updating Kube-Bench and re-evaluating your cluster configurations is crucial to maintaining strong security compliance as both Kubernetes and its security best practices evolve.
</Callout>

Good luck with your security assessment, and happy securing! See you in the next article.

## Additional Resources

* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Docker Hub](https://hub.docker.com/)
* [Terraform Registry](https://registry.terraform.io/)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/2bd4ff25-ce07-4cdd-bdfb-c716be822605" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/c370c677-ee22-4fd3-902b-99a0e58a0e00" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 KubeConfig
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/KubeConfig/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/KubeConfig/page)

# KubeConfig

> This guide explains KubeConfig files in Kubernetes and how they facilitate secure communication with the Kubernetes API server.

Welcome to this guide on KubeConfig files. In this article, we explain how KubeConfig files work in Kubernetes and demonstrate how they simplify secure communication with the Kubernetes API server.

In earlier segments, we covered generating a certificate for a user and how a client uses certificate and key files to query the Kubernetes REST API for a list of pods. In our example, the cluster is named "my-kube-playground". To query the API server using curl, include the client key, client certificate, and CA certificate as options. For instance:

```bash theme={null}
curl https://my-kube-playground:6443/api/v1/pods \
  --key admin.key \
  --cert admin.crt \
  --cacert ca.crt
```

The API server validates these credentials and returns a response similar to the following:

```json theme={null}
{
  "kind": "PodList",
  "apiVersion": "v1",
  "metadata": {
    "selfLink": "/api/v1/pods"
  },
  "items": []
}
```

When using the kubectl command-line tool, you can also supply the certificate and key information as options, eliminating the need to specify them with every command:

```bash theme={null}
kubectl get pods \
  --server my-kube-playground:6443 \
  --client-key admin.key \
  --client-certificate admin.crt \
  --certificate-authority ca.crt
```

This command will output:

```text theme={null}
No resources found.
```

Typing these options repeatedly can be cumbersome. Instead, you can consolidate this information into a configuration file called a kubeconfig file. Place the file at the default location (\$HOME/.kube/config) or specify a custom file using the --kubeconfig option. For example, a kubeconfig file might contain:

```text theme={null}
--server my-kube-playground:6443
--client-key admin.key
--client-certificate admin.crt
--certificate-authority ca.crt

kubectl get pods
No resources found.
```

Once the kubeconfig file is stored at \$HOME/.kube/config, kubectl automatically loads it, so you no longer need to specify all the certificate file paths with each command.

The kubeconfig file follows a defined format and is organized into three main sections:

* **Clusters**: Represent the Kubernetes clusters you need access to (e.g., development, testing, production).
* **Users**: Define the credentials that can interact with those clusters (e.g., admin, dev-user, prod-user).
* **Contexts**: Combine clusters and users to specify which user accesses which cluster. For example, the context "admin\@production" designates that the admin account accesses the production cluster.

Below is an illustrative diagram that shows the structure of a KubeConfig file:

<Frame>
  ![The image illustrates a KubeConfig file structure, showing clusters, contexts, and users, with examples like Development, Admin@Production, and Dev User.](https://kodekloud.com/kk-media/image/upload/v1752871366/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-KubeConfig/frame_160.jpg)
</Frame>

Let's examine a real kubeconfig file in YAML format. Notice it includes the API version set to v1 and the kind set to Config. Clusters, contexts, and users are each specified as an array element, allowing you to store multiple configurations in one file:

```yaml theme={null}
apiVersion: v1
kind: Config
clusters:
- name: my-kube-playground  # (values hidden…)
- name: development
- name: production
- name: google
contexts:
- name: my-kube-admin@my-kube-playground
- name: dev-user@google
- name: prod-user@production
users:
- name: my-kube-admin
- name: admin
- name: dev-user
- name: prod-user
```

Once you have configured this file, you don’t need to create any Kubernetes objects—the kubectl tool reads the file and uses the defined configuration automatically. To set a default context, simply update the current-context field. For instance, to default to the context "dev-user\@google", include the following line:

```yaml theme={null}
current-context: dev-user@google
```

You can view your active configuration with:

```bash theme={null}
kubectl config view
```

This command outputs the clusters, contexts, and users along with the current context. If the kubeconfig file is at the default location, it is automatically picked up by kubectl. If you prefer using a custom configuration file, you can specify it as shown below:

```bash theme={null}
kubectl config view --kubeconfig=my-custom-config
```

Below is a sample output from a custom kubeconfig file:

```yaml theme={null}
apiVersion: v1
kind: Config
current-context: my-kube-admin@my-kube-playground
clusters:
- name: my-kube-playground
- name: development
- name: production
contexts:
- name: my-kube-admin@my-kube-playground
- name: prod-user@production
users:
- name: my-kube-admin
- name: prod-user
```

To change your active context, run the following command. For example, to switch from "my-kube-admin\@my-kube-playground" to "prod-user\@production":

```bash theme={null}
kubectl config use-context prod-user@production
```

After executing this command, your kubeconfig file's current-context is updated accordingly:

```yaml theme={null}
apiVersion: v1
kind: Config
current-context: prod-user@production
clusters:
- name: my-kube-playground
- name: development
- name: production
contexts:
- name: my-kube-admin@my-kube-playground
- name: prod-user@production
users:
- name: my-kube-admin
- name: prod-user
```

Another useful feature of kubeconfig files is the ability to set a default namespace within a context. Since a cluster can manage multiple namespaces, specifying a default namespace allows you to bypass using the --namespace flag with every command.

Consider the following configuration without a namespace:

```yaml theme={null}
apiVersion: v1
kind: Config
clusters:
- name: production
  cluster:
    certificate-authority: ca.crt
    server: https://172.17.0.51:6443
contexts:
- name: admin@production
  context:
    cluster: production
    user: admin
users:
- name: admin
  user:
    client-certificate: admin.crt
    client-key: admin.key
```

By adding the namespace field to the context, kubectl automatically switches to the specified namespace ("finance" in this example):

```yaml theme={null}
apiVersion: v1
kind: Config
clusters:
- name: production
  cluster:
    certificate-authority: ca.crt
    server: https://172.17.0.51:6443
contexts:
- name: admin@production
  context:
    cluster: production
    user: admin
    namespace: finance
users:
- name: admin
  user:
    client-certificate: admin.crt
    client-key: admin.key
```

<Callout icon="lightbulb" color="#1CB2FE">
  For improved security and portability, it is recommended to use the full file paths for certificate files. Alternatively, you can embed the actual certificate content (in base64 format) using the certificate-authority-data field.
</Callout>

For example, you can include the certificate data directly in the kubeconfig file like so:

```yaml theme={null}
apiVersion: v1
kind: Config
clusters:
- name: production
  cluster:
    certificate-authority: /etc/kubernetes/pki/ca.crt
    certificate-authority-data: LS0tLS1CRUdJTiBDRVJU...
```

If you encounter a certificate in base64 encoded format, you can decode it as required, ensuring flexibility in managing your credentials.

That’s the end of this guide. For further practice, explore the practice exercises section to work with KubeConfig files and troubleshoot common issues. Happy learning!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/9e5514eb-f6f7-4a39-95b3-c251ff9d6f6a" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/1166d810-3163-4003-8d54-0f66f5b253f2" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 Kubectl Proxy Port Forward
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Kubectl-Proxy-Port-Forward/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Kubectl-Proxy-Port-Forward/page)

# Kubectl Proxy Port Forward

> This article explains how to use kubectl proxy and port-forward commands for secure interaction with Kubernetes API server and internal services.

In this article, we dive deep into using the kubectl proxy and port-forward commands to securely interact with your Kubernetes API server and internal services. By leveraging your kubeconfig file, these tools enable seamless authentication and allow you to access cluster resources without manually specifying credentials.

When running kubectl, you don't need to embed authentication details in your commands. Your kubeconfig file contains the necessary credentials, letting kubectl connect to your Kubernetes cluster's API server regardless of whether you are on the control plane host or a remote workstation.

For example, running the following command on your local machine or lab setup produces output similar to:

```bash theme={null}
kubectl get nodes
NAME    STATUS   ROLES                  AGE   VERSION
master  Ready    control-plane,master   25h   v1.20.1
worker  Ready    <none>                 25h   v1.20.1
```

The Kubernetes cluster itself might be hosted on a VM, private server, public cloud, or provided by a managed Kubernetes service. In all cases, you can manage it locally with kubectl using the credentials stored in your kubeconfig file.

Another way to directly interact with the Kubernetes API server is by using curl over port 6443. For instance, executing:

```bash theme={null}
curl http://<kube-api-server-ip>:6443 -k
```

yields a response like:

```json theme={null}
{
  "kind": "Status",
  "apiVersion": "v1",
  "metadata": {},
  "status": "Failure",
  "message": "forbidden: User \"system:anonymous\" cannot get path \"/\"",
  "reason": "Forbidden",
  "details": {},
  "code": 403
}
```

<Callout icon="lightbulb" color="#1CB2FE">
  Because no authentication details are provided in the curl command, the Kubernetes API returns a forbidden status. Always ensure proper credentials are used when accessing services.
</Callout>

## Using Kubectl Proxy

The kubectl proxy command simplifies accessing the API server without manually managing credentials. It launches a local proxy service on port 8001 by default, automatically using the client credentials and certificates specified in your kubeconfig file.

To start the proxy, run:

```bash theme={null}
kubectl proxy
```

The output will confirm that the proxy is running:

```bash theme={null}
Starting to serve on 127.0.0.1:8001
```

Now, you can query the API server’s endpoints via the proxy. For instance, use:

```bash theme={null}
curl http://localhost:8001 -k
```

This command returns a list of all available API paths:

```json theme={null}
{
  "paths": [
    "/api",
    "/api/v1",
    "/apis",
    "/apis/",
    "/healthz",
    "/logs",
    "/metrics",
    "/openapi/v2",
    "/swagger-2.0.0.json"
  ]
}
```

In this setup, your local proxy forwards requests to the Kubernetes API server using the credentials in your kubeconfig file. Note that because the proxy binds to the loopback address (127.0.0.1), it is accessible only from your local machine.

## Accessing Cluster Services via Kubectl Proxy

Using kubectl proxy, you can also access services deployed within the cluster. For example, suppose you have an Nginx service running on a ClusterIP in the default namespace. Although not exposed externally via NodePort or LoadBalancer, you can access it locally by constructing the appropriate URL through the proxy:

```bash theme={null}
curl http://localhost:8001/api/v1/namespaces/default/services/nginx/proxy/
```

The response might look like the following HTML page:

```html theme={null}
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and working. Further configuration is required.</p>
<p>For online documentation and support please refer to <a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at <a href="http://nginx.com/">nginx.com</a>.</p>
<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

This approach makes the service appear as if it were running directly on your local machine.

## Accessing Cluster Services via Port Forwarding

In addition to using a proxy, port forwarding offers a convenient method to map a local port directly to a port on a service, pod, or other resource in your cluster. This method is particularly useful when you need to test applications running remotely.

For example, to forward traffic from your local port 28080 to port 80 on an Nginx service, execute:

```bash theme={null}
kubectl port-forward service/nginx 28080:80
```

Once the port-forward is established, access the service using:

```bash theme={null}
curl http://localhost:28080/
```

You should see the Nginx welcome page, confirming that the forwarding is successful:

```html theme={null}
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
body {
    width: 35em;
    margin: 0 auto;
    font-family: Tahoma, Verdana, Arial, sans-serif;
}
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed</p>
</body>
</html>
```

Port forwarding is invaluable when working with remote clusters, as it provides direct, secure access to services as if they were running locally.

## Summary

In this article, we explored two fundamental techniques for interacting with a Kubernetes cluster:

1. Using kubectl proxy to access the Kubernetes API server and internal services without providing manual authentication details.
2. Using kubectl port-forward to map a local port to a cluster service, enabling local access to remote resources.

<Callout icon="lightbulb" color="#1CB2FE">
  Leveraging kubectl proxy and port forwarding streamlines remote cluster management, making it easier to perform diagnostic tasks and access internal services securely.
</Callout>

By mastering these techniques, you can efficiently manage your Kubernetes clusters and securely troubleshoot or test services without exposing them externally. For more detailed Kubernetes documentation and further learning, consider exploring the following resources:

* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Kubernetes Basics](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)

Practice these commands in your lab environments to gain confidence and explore additional use cases in your upcoming projects.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/5ae09904-7026-40c1-8d94-66ce2d244413" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/e572aaf4-1736-4865-9dd1-b2e46aaaca04" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 Kubelet Security
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Kubelet-Security/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Kubelet-Security/page)

# Kubelet Security

> This article discusses securing the Kubelet in Kubernetes by configuring authentication, authorization, and managing access to its APIs.

In this lesson, we revisit the Kubelet and examine multiple approaches for its configuration and hardening on Kubernetes nodes. In the [CKA Certification Course - Certified Kubernetes Administrator](https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator), the Kubelet is compared to a ship’s captain. Much like a captain, it handles onboard operations, manages paperwork to join the cluster, and communicates regularly with the master control. It also loads or unloads containers as instructed by the scheduler and sends continuous status reports.

However, a significant security risk arises if an impersonator masquerades as the master, potentially exposing sensitive information about cargo such as its quantity, content, and destination. Therefore, protecting all communications between the master (kube-apiserver) and the Kubelet is essential.

The Kubelet registers its node with the Kubernetes cluster and, upon receiving commands to deploy a container or pod, delegates tasks to the container runtime (for example, Docker). It then continuously monitors the pod and container states, reporting their status back to the kube-apiserver.

***

## Installing the Kubelet

Traditionally, installing the Kubelet involved manually downloading its binary and configuring it as a service. When using the `kubeadm` tool for cluster deployment, the necessary binaries are downloaded automatically, and the cluster is bootstrapped for you. However, you must still install the Kubelet on each worker node manually.

Below is an example of installing the Kubelet and setting up its service:

```bash theme={null}
wget https://storage.googleapis.com/kubernetes-release/release/v1.20.0/bin/linux/amd64/kubelet
```

```bash theme={null}
# kubelet.service file snippet
ExecStart=/usr/local/bin/kubelet \\
  --container-runtime=docker \\
  --image-pull-progress-deadline=2m \\
  --kubeconfig=/var/lib/kubelet/kubeconfig \\
  --network-plugin=cni \\
  --register-node=true \\
  --v=2 \\
  --cluster-domain=cluster.local \\
  --file-check-frequency=0s \\
  --healthz-port=10248 \\
  --cluster-dns=10.96.0.10 \\
  --http-check-frequency=0s \\
  --sync-frequency=0s \\
```

Starting with version 1.10, many parameters previously passed via command-line flags have been migrated into a dedicated Kubelet configuration file. This file, known as the Kubelet configuration, simplifies deployment and management.

Below is an updated example demonstrating how to configure the Kubelet service to use a remote container runtime:

```bash theme={null}
wget https://storage.googleapis.com/kubernetes-release/release/v1.20.0/bin/linux/amd64/kubelet
```

```bash theme={null}
# kubelet.service file snippet
[Unit]
Description=kubelet

[Service]
ExecStart=/usr/local/bin/kubelet \\
  --container-runtime=remote \\
  --image-pull-progress-deadline=2m \\
  --kubeconfig=/var/lib/kubelet/kubeconfig \\
  --network-plugin=cni \\
  --register-node=true \\
  -v=2 \\
  --cluster-domain=cluster.local \\
  --file-check-frequency=0s \\
  --healthz-port=10248 \\
  --cluster-dns=10.96.0.10 \\
  --http-check-frequency=0s \\
  --sync-frequency=0s
```

```yaml theme={null}
# kubelet-config.yaml file snippet
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
clusterDomain: cluster.local
fileCheckFrequency: 0s
healthzPort: 10248
clusterDNS:
  - 10.96.0.10
httpCheckFrequency: 0s
syncFrequency: 0s
```

When initiating the Kubelet service, specify the path to the configuration file using the `--config` flag. Notice that parameters are defined using camel case (e.g., `httpCheckFrequency`) rather than the command-line flag style (`http-check-frequency`). Also, note that if the same parameter is set in both the command line and the configuration file, the command-line value takes precedence.

<Callout icon="lightbulb" color="#1CB2FE">
  Although `kubeadm` does not install the Kubelet, it can manage Kubelet configuration files across worker nodes during the `kubeadm join` process.
</Callout>

To inspect the running Kubelet process and view its configuration settings, check the process details and the configuration file contents. For example:

```bash theme={null}
ps -aux | grep kubelet
```

```bash theme={null}
# Example output of /var/lib/kubelet/config.yaml
apiVersion: kubelet.config.k8s.io/v1beta1
clusterDNS:
- 10.96.0.10
clusterDomain: cluster.local
cpuManagerReconcilePeriod: 0s
evictionPressureTransitionPeriod: 0s
fileCheckFrequency: 0s
healthzBindAddress: 127.0.0.1
healthzPort: 10248
httpCheckFrequency: 0s
imageMinimumGCAge: 0s
kind: KubeletConfiguration
nodeStatusReportFrequency: 0s
nodeStatusUpdateFrequency: 0s
rotateCertificates: true
runtimeRequestTimeout: 0s
staticPodPath: /etc/kubernetes/manifests
streamingConnectionIdleTimeout: 0s
```

***

## Kubelet Security

Ensuring that the Kubelet only responds to authenticated requests from the kube-apiserver is critical for the security of your cluster. By default, the Kubelet serves on two distinct ports:

1. **Port 10250:** Provides full API access.
2. **Port 10255:** Offers a read-only API for metrics and system data.

By default, anonymous access is permitted to these APIs. For example, running the following command returns a list of pods running on a node:

<Frame>
  ![The image shows a table listing Kubelet ports 10250 and 10255, describing their API access levels: full access and unauthenticated read-only access, respectively.](https://kodekloud.com/kk-media/image/upload/v1752871367/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Kubelet-Security/frame_370.jpg)
</Frame>

```bash theme={null}
curl -sk http://localhost:10250/pods
```

You can also access additional endpoints (e.g., `/logs/syslog`) for node system log inspection. The Kubelet API exposes multiple functions, including node health checks, metrics, port forwarding, and command execution in containers.

The service running on port 10255, however, provides unauthenticated, read-only access. This poses a security risk because anyone with network access could potentially view sensitive data.

***

### Securing the Kubelet

To enhance security, every request to the Kubelet must be properly authenticated and authorized before being processed.

#### 1. Disabling Anonymous Authentication

By default, the Kubelet treats unauthenticated requests as anonymous, using the credentials `system:anonymous` and group `system:unauthenticated`. To disable anonymous access, update the Kubelet service configuration using the `--anonymous-auth=false` flag:

```bash theme={null}
# kubelet.service snippet
ExecStart=/usr/local/bin/kubelet \\
...
--anonymous-auth=false \\
...
```

Alternatively, you can configure this setting within the Kubelet configuration YAML file:

```yaml theme={null}
# kubelet-config.yaml snippet
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
authentication:
  anonymous:
    enabled: false
```

Disabling anonymous authentication is best practice. Once disabled, ensure you enable a supported authentication mechanism.

#### 2. Certificate-Based Authentication

Certificate-based authentication provides secure access by using a pair of certificates. Configure the Kubelet to use the CA certificate with the `--client-ca-file` parameter in the service file or within the Kubelet configuration:

```bash theme={null}
# kubelet.service snippet
ExecStart=/usr/local/bin/kubelet \\
    --client-ca-file=/path/to/ca.crt \\
```

```yaml theme={null}
# kubelet-config.yaml snippet
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
authentication:
  x509:
    clientCAFile: /path/to/ca.crt
```

When performing API calls (for example, with curl), include the client certificate and key since the kube-apiserver is treated as a client from the Kubelet’s perspective. Below is an example configuration for the kube-apiserver service:

```bash theme={null}
# Example command lines and configuration snippets
ExecStart=/usr/local/bin/kubelet \\
    --client-ca-file=/path/to/ca.crt \\

curl -sk https://localhost:10250/pods/ --key kubelet-key.pem --cert kubelet-cert.pem

# Example kube-apiserver.service snippet
[Service]
ExecStart=/usr/local/bin/kube-apiserver \\
    --kubelet-client-certificate=/path/to/kubelet-cert.pem \\
    --kubelet-client-key=/path/to/kubelet-key.pem \\
```

<Callout icon="triangle-alert" color="#FF6B6B">
  If neither certificate-based nor token-based authentication explicitly rejects a request, the Kubelet will fallback to treating it as anonymous. Always ensure your authentication mechanisms are correctly configured.
</Callout>

#### 3. Authorization

After authenticating requests, the Kubelet determines what actions or API resources a user can access. By default, the authorization mode is set to `AlwaysAllow`, meaning all requests are permitted. To secure the Kubelet, configure the authorization mode to `Webhook` so the Kubelet consults the API server to determine if a request should be allowed:

```bash theme={null}
# kubelet.service snippet
ExecStart=/usr/local/bin/kubelet \\
  ...
  --authorization-mode=Webhook \\
  ...
```

```yaml theme={null}
# kubelet-config.yaml snippet
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
authorization:
  mode: Webhook
```

#### 4. Managing the Read-Only Port (10255)

The read-only port (10255) can expose sensitive metrics without authentication. It is advisable to disable this port if not explicitly needed. You can disable it by setting the port value to zero in either the service file or configuration file:

```bash theme={null}
curl -sk http://localhost:10255/metrics
```

```bash theme={null}
# kubelet.service snippet
ExecStart=/usr/local/bin/kubelet \\
  ...
  --read-only-port=10255 \\
  ...
```

```yaml theme={null}
# kubelet-config.yaml snippet
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
readOnlyPort: 0
```

Disabling the read-only port enhances security by preventing unauthorized access to node metrics and other system data.

***

## Summary

In this lesson, we reviewed critical aspects of securing the Kubelet:

* Disable anonymous authentication by setting `--anonymous-auth=false` or configuring it within the YAML file.
* Implement a secure authentication mechanism with certificate-based authentication by setting the `clientCAFile` parameter.
* Configure authorization using the `Webhook` mode so that the API server validates requests.
* Disable the read-only port (10255) by setting it to zero if unauthenticated access is not desired.

By applying these security measures, your Kubelet will be significantly more resilient to unauthorized access. Now, proceed to the labs and practice implementing Kubelet security in your Kubernetes environment.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/da297ecd-2762-48ed-9eb7-c6556bb9658d" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/3d54f860-f552-48a2-8ac2-886bacd00893" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 Kubernetes Security Primitives
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Kubernetes-Security-Primitives/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Kubernetes-Security-Primitives/page)

# Kubernetes Security Primitives

> This article provides an overview of critical security measures in Kubernetes, focusing on securing cluster hosts, API server access, intra-cluster communications, and network policies.

Welcome to our comprehensive guide on Kubernetes security primitives. As Kubernetes has become the industry standard for hosting production-grade applications, ensuring robust security practices is more important than ever. This article provides a high-level overview of critical security measures in Kubernetes, with detailed explorations to follow in subsequent posts.

## Securing the Cluster Hosts

Before diving into the intricacies of Kubernetes security, it is essential to secure the underlying infrastructure. Ensure that all hosts in your Kubernetes cluster are protected by:

* Disabling root access and password-based authentication.
* Enabling SSH key-based authentication.
* Implementing additional security measures to protect the physical or virtual infrastructure hosting Kubernetes.

<Callout icon="triangle-alert" color="#FF6B6B">
  If the underlying infrastructure is compromised, the security of the entire Kubernetes cluster is at risk.
</Callout>

## Kubernetes API Server: The Entry Point

At the core of Kubernetes operations lies the kube API server. Users interact with the cluster through the `kubectl` utility or direct API calls. This interaction is crucial because it governs nearly all cluster operations. Therefore, two fundamental questions arise:

1. Who can access the cluster?
2. What actions can they perform?

### Authentication

Access to the API server is regulated by robust authentication mechanisms. Kubernetes supports multiple methods, including:

* Static files with user IDs and passwords
* Tokens
* Certificates
* Integrations with external providers such as LDAP
* Service accounts for machine-to-machine communications

These diverse approaches ensure that every connection is verified, offering flexibility and security simultaneously.

<Frame>
  ![The image is a slide titled "Authentication" listing access methods: username/password, username/tokens, certificates, LDAP, and service accounts.](https://kodekloud.com/kk-media/image/upload/v1752871371/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Kubernetes-Security-Primitives/frame_120.jpg)
</Frame>

### Authorization

Once users or services are authenticated, authorization mechanisms determine their permitted actions on the cluster. Kubernetes primarily uses Role-Based Access Control (RBAC) to map users to groups with specific permissions. Other authorization modules available include:

* Attribute-Based Access Control (ABAC)
* Node Authorization
* Webhook-based authorization

These systems work together to ensure that every action within the cluster is scrutinized and allowed only if it aligns with the defined permissions.

<Frame>
  ![The image lists types of authorization: RBAC, ABAC, Node Authorization, and Webhook Mode, under the heading "Authorization: What can they do?"](https://kodekloud.com/kk-media/image/upload/v1752871373/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Kubernetes-Security-Primitives/frame_140.jpg)
</Frame>

## Securing Intra-Cluster Communications

A critical element of Kubernetes security involves securing communications between various cluster components. All interactions between components—such as the etcd cluster, kube controller manager, scheduler, API server, and worker node components (including kubelet and kube-proxy)—are protected using TLS encryption.

<Callout icon="lightbulb" color="#1CB2FE">
  Detailed instructions on setting up certificates for secure communications will be provided in a dedicated section.
</Callout>

<Frame>
  ![The image illustrates the relationship between Kubernetes components using TLS certificates, centered around the Kube ApiServer, connecting to ETCD Cluster, Kubelet, Kube Proxy, Kube Controller Manager, and Kube Scheduler.](https://kodekloud.com/kk-media/image/upload/v1752871374/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Kubernetes-Security-Primitives/frame_160.jpg)
</Frame>

## Network Policies Within the Cluster

By default, pods within a Kubernetes cluster can communicate freely with one another. To restrict unwanted access and tighten security, network policies can be implemented. These policies enable you to control traffic flow between pods and are an integral part of securing inter-application communications within the cluster.

<Frame>
  ![The image illustrates network policies using a diagram of four devices, each containing colored circles and interconnected by dashed lines.](https://kodekloud.com/kk-media/image/upload/v1752871375/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Kubernetes-Security-Primitives/frame_190.jpg)
</Frame>

## In Summary

This article has provided an overview of the key security primitives in Kubernetes:

* Securing cluster hosts
* Strong authentication and authorization methods for the API server
* Using TLS encryption for intra-cluster communications
* Implementing network policies for pod-to-pod communication

We will explore these topics in much greater detail in upcoming articles. Stay tuned as we dive deeper into each security aspect to help you ensure that your Kubernetes environment remains secure and resilient.

For more Kubernetes best practices and security tips, continue following our in-depth guides and tutorials.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/c4389944-7651-4660-98bb-d454889d71af" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 Network Policy
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Network-Policy/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Network-Policy/page)

# Network Policy

> This article covers network policies for managing traffic and security in Kubernetes environments.

Welcome to this article on network policies. In this guide, you'll learn the fundamentals of network traffic management and security within a Kubernetes environment. We start by reviewing basic networking and security concepts before diving into a real-world example.

## Understanding Traffic Flow

Let's begin with a simple example that illustrates the traffic flow between a web application and its associated database server. In this scenario, we have the following components:

* A **web server** that delivers the frontend to users.
* An **API server** that handles backend processing.
* A **database server** that stores application data.

The typical flow of traffic is:

1. A user sends a request to the web server on port 80.
2. The web server forwards the request to the API server on port 5000.
3. The API server queries the database server on port 3306 and then returns the response back to the user.

This example highlights two types of traffic:

* **Ingress**: Incoming traffic (e.g., user requests to the web server).
* **Egress**: Outgoing traffic (e.g., web server calling the API server).

<Callout icon="lightbulb" color="#1CB2FE">
  Note that when defining ingress and egress traffic, we focus solely on the direction in which the traffic originates. The response traffic (typically represented by dotted lines in diagrams) is not considered in these definitions.
</Callout>

<Frame>
  ![The image illustrates a network flow diagram showing ingress and egress processes involving a user, web, API, and database with specific ports.](https://kodekloud.com/kk-media/image/upload/v1752871380/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Network-Policy/frame_80.jpg)
</Frame>

### Traffic Details for Each Component

* **API Server**:
  * Receives ingress traffic from the web server on port 5000.
  * Sends out egress traffic to the database server on port 3306.

* **Database Server**:
  * Only receives ingress traffic on port 3306 from the API server.

Based on this setup, the necessary rules are:

1. Ingress rule on the web server to accept HTTP traffic on port 80.
2. Egress rule on the web server to allow traffic to the API server on port 5000.
3. Ingress rule on the API server to accept traffic on port 5000.
4. Egress rule on the API server to allow traffic to the database server on port 3306.
5. Ingress rule on the database server to accept traffic on port 3306.

<Frame>
  ![The image illustrates IT traffic flow with ingress and egress ports, showing connections to web, API, and database services using ports 80, 5000, and 3306.](https://kodekloud.com/kk-media/image/upload/v1752871381/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Network-Policy/frame_120.jpg)
</Frame>

## Network Security in Kubernetes

In a Kubernetes cluster, nodes host a set of pods and services, each assigned an IP address. One of the key prerequisites for Kubernetes networking is that pods can communicate with one another without needing additional configuration such as custom routes. Typically, all pods reside on a shared virtual private network spanning across multiple nodes, and by default, a Kubernetes cluster allows unrestricted communication between pods through their IP addresses, pod names, or associated services. This is due to a default “allow all” rule that permits traffic between any pods or services within the cluster.

<Frame>
  ![The image illustrates a network security concept labeled "All Allow," showing interconnected nodes with various IP addresses within a cloud-like structure.](https://kodekloud.com/kk-media/image/upload/v1752871382/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Network-Policy/frame_210.jpg)
</Frame>

### Applying Network Policies

In our example, each component—the web server, the API server, and the database server—is deployed as a separate pod with its own service to manage both intra-cluster and external communications. Under default settings, these pods can communicate freely. However, consider a scenario where security requirements dictate that the frontend web server should not directly access the database server. In this case, you can implement a network policy to restrict such traffic so that the database server only accepts traffic from the API server.

A network policy in Kubernetes is an object that defines how pods communicate with each other. By adding labels and selectors to pods, similar to associating pods with services or replica sets, you create targeted rules. For example, you might label the database pod and define a policy permitting only ingress traffic on port 3306 coming from the API pod.

<Frame>
  ![The image illustrates a network traffic flow diagram with a user accessing a Web Pod on port 80, which connects to an API Pod on port 5000 and a DB Pod on port 3306.](https://kodekloud.com/kk-media/image/upload/v1752871383/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Network-Policy/frame_250.jpg)
</Frame>

Below is an example of a network policy definition that restricts access to the database pod:

```yaml theme={null}
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: db-policy
spec:
  podSelector:
    matchLabels:
      role: db
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          name: api-pod
    ports:
    - protocol: TCP
      port: 3306
```

In this YAML example:

* The policy applies to pods labeled with `role: db`.
* Only ingress traffic is restricted, as specified by the `policyTypes` field. (Egress traffic from the pod is not limited.)
* The ingress rule allows traffic exclusively from pods labeled with `name: api-pod` on TCP port 3306.

Remember that for ingress or egress isolation to take effect, they must be explicitly defined under `policyTypes`. Without this specification, the pod's corresponding traffic is not isolated.

To apply this policy, run the following command:

```bash theme={null}
kubectl create -f db-policy.yaml
```

<Callout icon="triangle-alert" color="#FF6B6B">
  Keep in mind that network policies are enforced only by network solutions that support them. Network solutions such as Kube-router, Calico, Romana, and Weave Net support network policies, whereas Flannel does not. If you are using a solution that doesn’t support policies, you may still create them without any error, but they won’t be enforced.
</Callout>

<Frame>
  ![The image lists network solutions: Kube-router, Calico, Romana, and Weave-net support network policies, while Flannel does not.](https://kodekloud.com/kk-media/image/upload/v1752871385/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Network-Policy/frame_450.jpg)
</Frame>

## Conclusion

This article has outlined the basics of network policies, detailing how to manage ingress and egress traffic both in a general network environment and within a Kubernetes cluster. By employing network policies, you can enhance your cluster's security by ensuring that only authorized traffic is allowed between application components.

For further details, please consult the [Kubernetes Documentation](https://kubernetes.io/docs/) and explore practical coding challenges to gain hands-on experience with network policies.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/c1a23222-3b06-466a-a19c-f605565424e2" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 Protection Strategies
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Protection-Strategies/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Protection-Strategies/page)

# Protection Strategies

> This article explores Kubernetes security protection strategies using a hotel analogy to illustrate access control, isolation, and monitoring for securing clusters.

In this article, we explore several protection strategies in Kubernetes security using a relatable hotel analogy. By comparing Kubernetes components to elements of a well-run hotel, you'll gain a clearer understanding of how access control, isolation, and monitoring work together to secure your cluster.

Imagine a hotel where different staff members have varying access levels. For instance, managers have complete access to all areas, including secure zones such as the data center or security room, whereas housekeepers are limited to guest rooms.

<Frame>
  ![The image illustrates RBAC in a Kubernetes cluster, comparing it to a hotel where managers access all secure rooms and housekeepers access guest rooms.](https://kodekloud.com/kk-media/image/upload/v1752871386/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Protection-Strategies/frame_30.jpg)
</Frame>

In Kubernetes, role-based access control (RBAC) mirrors this concept by determining who can access and modify node metadata. Specific roles come with defined permissions, ensuring that only authorized users can execute sensitive operations.

Just as a hotel caters to different guest types—offering VIP guests deluxe rooms and regular guests standard rooms—Kubernetes can reserve specific nodes for particular workloads. By isolating nodes, the system prevents non-critical or unauthorized applications from running on nodes dedicated to essential tasks.

<Frame>
  ![The image illustrates Kubernetes node isolation, comparing it to hotel room assignments for VIP and normal guests, ensuring specific workloads are reserved for designated nodes.](https://kodekloud.com/kk-media/image/upload/v1752871387/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Protection-Strategies/frame_70.jpg)
</Frame>

Another layer of protection is akin to having restricted staff-only areas and exclusive VIP guest floors. Within Kubernetes, network policies control communication between pods or nodes. This ensures that only select services or users can interact with designated resources.

<Frame>
  ![The image illustrates Kubernetes network policies using a hotel analogy, highlighting restricted staff-only areas and VIP guest floors to explain controlled communication.](https://kodekloud.com/kk-media/image/upload/v1752871388/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Protection-Strategies/frame_100.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Audit logs in a hotel capture details about which room was accessed, by whom, and at what time. Similarly, Kubernetes maintains comprehensive audit logs to track access and modifications to node metadata, providing a detailed record that is essential for security monitoring and compliance.
</Callout>

<Frame>
  ![The image compares hotel audit logs to Kubernetes audit logs, highlighting tracking of access and modifications to node metadata.](https://kodekloud.com/kk-media/image/upload/v1752871390/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Protection-Strategies/frame_120.jpg)
</Frame>

Keeping security measures up-to-date is critical. Just like hotels upgrade their locks, cameras, and security systems regularly, Kubernetes nodes require systematic updates and patches. This ongoing maintenance helps to identify and mitigate vulnerabilities in a timely manner.

<Frame>
  ![The image illustrates the importance of regular updates and patches for Kubernetes nodes to prevent vulnerabilities, using a hotel analogy with locks, cameras, and software systems.](https://kodekloud.com/kk-media/image/upload/v1752871391/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Protection-Strategies/frame_140.jpg)
</Frame>

By understanding these analogies, you can better appreciate how protection strategies in Kubernetes work collectively to secure your environment, manage access robustly, and ensure workload integrity.

For additional information on Kubernetes security best practices, visit the [Kubernetes Documentation](https://kubernetes.io/docs/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/377bb9dc-745e-4fa7-8700-d3a1b174a7da" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/a794ddd7-e6ea-474e-815c-e31a9e06801a" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 RBAC
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/RBAC/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/RBAC/page)

# RBAC

> Learn about role-based access control in Kubernetes, including creating roles, binding them to users, and managing permissions for secure cluster access.

In this lesson, you'll learn about role-based access control (RBAC) in Kubernetes. RBAC enables you to define roles with specific permissions and bind those roles to users or groups, ensuring secure and controlled access within your cluster. We'll walk through creating a role, binding it to a user, verifying configurations, and restricting access to specific resources.

## Creating a Role

A role in Kubernetes is defined in a YAML file that outlines the permitted actions under the following key elements:

* **apiVersion:** Must be set to `rbac.authorization.k8s.io/v1`.
* **kind:** Should be `Role`.
* **metadata.name:** The name of your role (e.g., "developer").
* **rules:** A list describing the API groups, resources, and verbs (actions) that are allowed.

For example, to create a role that allows developers to manage pods and create ConfigMaps, use the following YAML:

```yaml theme={null}
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: developer
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["list", "get", "create", "update", "delete"]
- apiGroups: [""]
  resources: ["ConfigMap"]
  verbs: ["create"]
```

After saving the YAML file (for instance, as `developer-role.yaml`), create the role with:

```bash theme={null}
kubectl create -f developer-role.yaml
```

<Callout icon="lightbulb" color="#1CB2FE">
  Roles and role bindings are namespaced. In the example above, the role is created in the default namespace unless you specify otherwise within the metadata.
</Callout>

## Binding the Role to a User

To grant the permissions defined in the role to a user, you need to create a role binding. A role binding links a user (or group) to a role. The YAML for a role binding includes:

* **metadata.name:** A unique name for the role binding (e.g., "devuser-developer-binding").
* **subjects:** The user, group, or service account to which permissions are granted.
* **roleRef:** A reference to the role created previously.

Below is an example that binds the "developer" role to the user "dev-user":

```yaml theme={null}
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: devuser-developer-binding
subjects:
- kind: User
  name: dev-user
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: developer
  apiGroup: rbac.authorization.k8s.io
```

Create the role binding by running:

```bash theme={null}
kubectl create -f devuser-developer-binding.yaml
```

## Verifying Roles and Bindings

To confirm that the role and its binding have been created successfully, you can list them using the following commands:

List all roles in the current namespace:

```bash theme={null}
kubectl get roles
```

Example output:

```bash theme={null}
NAME         AGE
developer    4s
```

List all role bindings:

```bash theme={null}
kubectl get rolebindings
```

Example output:

```bash theme={null}
NAME                      AGE
devuser-developer-binding  24s
```

To view detailed information about a specific role, use:

```bash theme={null}
kubectl describe role developer
```

This command displays details such as allowed resources and permissions, for example:

```bash theme={null}
Name:         developer
Labels:       <none>
Annotations:  <none>
PolicyRule:
  Resources  Non-Resource URLs  Resource Names  Verbs
  --------  ------------------  --------------  -----
  ConfigMap  []                  []              [create]
  pods       []                  []              [list, get, create, update, delete]
```

Similarly, inspect the details of the role binding with:

```bash theme={null}
kubectl describe rolebinding devuser-developer-binding
```

The output might look like this:

```bash theme={null}
Name:                     devuser-developer-binding
Labels:                   <none>
Annotations:              <none>
Role:
  Kind:       Role
  Name:       developer
Subjects:
  Kind  Name      Namespace
  ----  ----      ---------
  User  dev-user
```

## Checking Permissions

You can verify if you or another user have access to particular resources using the `kubectl auth can-i` command. For example:

To check if you can create deployments:

```bash theme={null}
kubectl auth can-i create deployments
```

Example output:

```bash theme={null}
yes
```

To check if you have permissions to delete nodes:

```bash theme={null}
kubectl auth can-i delete nodes
```

Example output:

```bash theme={null}
no
```

If you want to check permissions for a different user (like "dev-user") without switching accounts, use the `--as` flag. For example, if the dev user has permission to create pods but not deployments, these commands will reflect that:

```bash theme={null}
kubectl auth can-i create deployments
yes
kubectl auth can-i delete nodes
no
kubectl auth can-i create deployments --as=dev-user
no
kubectl auth can-i create pods --as=dev-user
yes
```

Remember, you can also specify the namespace with the `--namespace` flag if needed.

## Restricting Access to Specific Resources

RBAC in Kubernetes allows you to fine-tune permissions at a granular level. Instead of granting permissions universally to a resource type, you can restrict them to specific resources using the `resourceNames` field. For example, to allow a user to interact only with pods named "blue" and "orange", define the role as follows:

```yaml theme={null}
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: developer
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "create", "update"]
  resourceNames: ["blue", "orange"]
```

This configuration limits actions strictly to the specified pods.

## Conclusion

In this lesson, we covered how to configure RBAC in Kubernetes by:

* Creating a role with defined permissions.
* Binding a user to that role using a role binding.
* Verifying roles and permissions through `kubectl` commands.
* Checking and testing user permissions.
* Restricting access to specific resources for enhanced security.

For additional information on Kubernetes RBAC, consider reviewing the [Kubernetes Documentation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/). Continue practicing by applying these concepts to secure your cluster effectively.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/250ed868-3d01-4c71-bd30-ec82841a7538" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/3a9a1cb3-c889-472b-9fc2-48bff380c595" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 Reasons to Secure Node Metadata
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Reasons-to-Secure-Node-Metadata/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Reasons-to-Secure-Node-Metadata/page)

# Reasons to Secure Node Metadata

> Securing node metadata in Kubernetes is essential for protecting workloads and preventing unauthorized access to sensitive information.

Securing node metadata in Kubernetes is critical for maintaining the integrity and security of your workloads. In this lesson, we explain why protecting this information is essential by using a relatable hotel analogy. Here, different types of guests represent different workloads running on your Kubernetes cluster.

Imagine a hotel hosting various guests. VIP guests represent sensitive workloads in Kubernetes, and they are assigned to specially designated rooms that meet strict security standards. The hotel's database holds detailed metadata about each room, including its type and security conditions. If this metadata is compromised, the hotel might incorrectly assign a VIP guest to an unsuitable room. In Kubernetes, tampered node metadata (such as security labels) can lead to sensitive workloads being scheduled on insecure nodes.

<Frame>
  ![The image illustrates a concept of securing node metadata using a hotel analogy, featuring a Kubernetes cluster, VIP guest, and room details like type and special attributes.](https://kodekloud.com/kk-media/image/upload/v1752871392/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Reasons-to-Secure-Node-Metadata/frame_20.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Ensuring accurate node metadata is essential for the correct scheduling of workloads, preventing misallocations that could expose sensitive applications to risk.
</Callout>

## Risks of Insecure Node Metadata

1. **Improper Workload Scheduling:**\
   Incorrect metadata can cause non-critical workloads to receive resources intended only for high-security tasks. For example, if a critical taint is removed from a production node inadvertently, non-production workloads might be scheduled on that node, leading to resource contention or potential outages.

   An example of modifying node taints:

   ```bash theme={null}
   kubectl taint nodes node-1 key=value:NoSchedule-
   # node/node-1 untainted
   ```

2. **Unauthorized Data Exposure:**\
   If node metadata is not adequately protected, unauthorized users may access the Kubernetes API to list all nodes and gather sensitive information like the Kubelet version. This information can be used to launch targeted, version-specific exploits.

   To discover the Kubelet version, an attacker might run:

   ```bash theme={null}
   kubectl get nodes -o jsonpath='{.items[*].status.nodeInfo.kubeletVersion}'
   ```

3. **Network Mapping and Attacks:**\
   By listing IP addresses of all nodes, an attacker can construct a detailed map of the internal network. This data can be exploited for network-based attacks, such as Distributed Denial of Service (DDoS) attacks.

   For instance, to list internal IP addresses:

   ```bash theme={null}
   kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type=="InternalIP")].address}'
   ```

4. **Compliance Violations:**\
   Unauthorized access to node details, such as kernel versions, could result in breaches of regulations like GDPR or HIPAA. Maintaining tight control over node metadata helps ensure compliance with these regulatory standards.

   To view kernel versions, one could execute:

   ```bash theme={null}
   kubectl get nodes -o jsonpath='{.items[*].status.nodeInfo.kernelVersion}'
   # Example output:
   # 5.4.0-1041-aws  4.15.0-142-generic  5.8.0-53-generic
   ```

<Callout icon="triangle-alert" color="#FF6B6B">
  Improper handling of node metadata can expose your Kubernetes environment to critical vulnerabilities. Always enforce strict access controls and regularly audit metadata for unauthorized changes.
</Callout>

## Summary

Ensuring the security of node metadata is fundamental for:

* Correctly scheduling sensitive workloads.
* Preventing unauthorized access to critical cluster information.
* Maintaining overall system integrity.
* Complying with important regulatory and industry standards.

For further reading on securing a Kubernetes environment, check out the [Kubernetes Documentation](https://kubernetes.io/docs/) and explore best practices for keeping your clusters secure.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/31e4922a-3cf3-4726-910e-b02046786992" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 Section Introduction
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Section-Introduction/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Section-Introduction/page)

# Section Introduction

> This guide covers cluster setup and hardening, focusing on security best practices, tools, and techniques for Kubernetes environments.

Welcome to this comprehensive guide on cluster setup and hardening. In this lesson, we cover a range of essential topics to enhance the security of your infrastructure, including CIS Benchmarks, security tools, and various Kubernetes authentication and authorization mechanisms.

## Overview

Throughout this guide, you will learn:

* The importance of CIS Benchmarks and how to run them on an Ubuntu system.
* Tools available for running security benchmarks on a Kubernetes cluster, which will also be used in our hands-on labs.
* Key Kubernetes security concepts such as Service Accounts, TLS certificates, and methods to secure node metadata and endpoints.
* Strategies to secure the Kubernetes Dashboard and verify platform binaries before installation.
* Techniques for upgrading a Kubernetes cluster.
* An overview of network policies and methods to secure ingress controllers.

<Callout icon="lightbulb" color="#1CB2FE">
  If you have already explored these topics in our [CKA Certification Course - Certified Kubernetes Administrator](https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator), feel free to skip repeated details. You can also review the hands-on labs or refresh your memory as these topics are crucial for the CKS exam.
</Callout>

## CIS Benchmarks

CIS Benchmarks provide a set of security best practices that can be applied to various systems. In this guide, we demonstrate how to run these benchmarks on an Ubuntu system to ensure your server configuration meets the necessary security guidelines.

## Kubernetes Security Essentials

In the next sections, we will delve into several vital areas:

1. **Security Tools for Kubernetes:**\
   Explore the available tools for running security benchmarks on your Kubernetes cluster. These tools help you identify vulnerabilities and apply necessary hardening measures during the lab sessions.

2. **Authentication and Authorization:**\
   Understand different authentication mechanisms in Kubernetes, such as:
   * Service Accounts
   * TLS Certificates\
     Learn how each method contributes to a secure system by protecting your cluster against unauthorized access and ensuring secure communications.

3. **Securing Node Metadata and Endpoints:**\
   Discover techniques to protect node metadata and endpoints, which are critical components of the Kubernetes cluster architecture.

4. **Dashboard Security and Platform Verification:**\
   Review best practices for securing the Kubernetes dashboard. Additionally, learn how to verify platform binaries prior to installation, ensuring that only trusted binaries are deployed in your environment.

5. **Cluster Upgrades and Network Security:**\
   Find out how to upgrade a Kubernetes cluster safely and securely. This section also covers network policies and provides strategies to secure ingress controllers, ensuring a robust and secure networking environment.

By mastering these topics, you'll be well-prepared to enhance the security and reliability of your Kubernetes clusters.

Happy learning and stay secure!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/e40b6c82-ed73-413a-9610-c7c4cd5d98dd" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 Securing Node Metadata in Kubernetes
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Securing-Node-Metadata-in-Kubernetes/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Securing-Node-Metadata-in-Kubernetes/page)

# Securing Node Metadata in Kubernetes

> This article explores how to secure node metadata in Kubernetes, highlighting its importance and best practices for protecting sensitive information.

In this article, we explore how to secure node metadata in Kubernetes. Protecting node metadata is crucial because it contains sensitive information—such as instance details and credentials—that, if exposed, can pose significant security risks. We will cover the key components of node metadata and discuss best practices to secure this information effectively.

## Understanding Node Metadata Through an Analogy

Imagine a Kubernetes cluster as a hotel. Each room in the hotel represents a node, and just like rooms possess various details (room type, occupancy, service notes), nodes have associated metadata. This metadata includes essential attributes such as the node’s unique identity, configuration details, and operational status. In Kubernetes, node metadata is broken down into several components:

* **Node Name/Unique ID:** The unique identifier for each node.
* **Labels:** Key-value pairs used to group nodes, such as by geographic region.
* **Annotations:** Additional data used for debugging, logging, or monitoring.
* **Architecture:** Information on the hardware architecture (e.g., x86-64).
* **System Info:** Detailed system data including machine ID, system UUID, boot ID, kernel version, OS details, container runtime version, and Kubernetes component versions.
* **Addresses:** Lists internal and external IP addresses.
* **Other Key Components:** Node conditions (e.g., Ready, OutOfDisk), resource capacities, taints and tolerations, CIDRs, kubelet version, and cloud-provider-specific IDs.

<Callout icon="lightbulb" color="#1CB2FE">
  Node metadata not only helps in managing the Kubernetes cluster effectively but also plays a critical role in securing your infrastructure.
</Callout>

## Detailed Breakdown of Node Metadata

The diagram below illustrates some of the metadata components associated with a Kubernetes node:

<Frame>
  ![The image illustrates "Understanding Node Metadata" with server icons linked to a Kubernetes cluster node.](https://kodekloud.com/kk-media/image/upload/v1752871394/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Securing-Node-Metadata-in-Kubernetes/frame_70.jpg)
</Frame>

### Node Components

* **Node Name:** The unique identifier for a node.
* **Labels:** Used to categorize nodes. For example, labels can group nodes by region in a cloud environment. An example of node labels:

```yaml theme={null}
Labels:
  beta.kubernetes.io/arch: amd64
  beta.kubernetes.io/os: linux
  kubernetes.io/arch: amd64
  kubernetes.io/hostname: node01
  kubernetes.io/os: linux
  region: us-east-1
```

* **Annotations:** These provide additional context for debugging, logging, and monitoring. For instance, the networking tool Flannel uses annotations for its internal configuration:

```yaml theme={null}
Annotations:
  flannel.alpha.coreos.com/backend-data: '{"VNI":1,"VtepMAC":"a2:bd:8e:41:63:65"}'
  flannel.alpha.coreos.com/backend-type: vxlan
  flannel.alpha.coreos.com/kube-subnet-manager: "true"
  flannel.alpha.coreos.com/public-ip: 192.168.87.255
  kubeadm.alpha.kubernetes.io/cri-socket: unix:///var/run/containerd/containerd.sock
  node.alpha.kubernetes.io/ttl: "0"
  volumes.kubernetes.io/controller-managed-attach-detach: "true"
```

* **Architecture:** Indicates the underlying hardware, such as x86-64.
* **System Info:** Detailed information about the node’s system including operating system, kernel version, container runtime, and more. For example:

```yaml theme={null}
System Info:
  Machine ID: 69ee5c89434f4d5baea262a6ecc698fe
  System UUID: 8ab83d3f-465d-36a9-6ec2-b7e9e7ad6a45
  Boot ID: 8059e764-a637-45f0-abd9-36e9a366e719
  Kernel Version: 5.15.0-1065-gcp
  OS Image: Ubuntu 22.04.4 LTS
  Operating System: linux
  Architecture: amd64
  Container Runtime Version: containerd://1.6.26
  Kubelet Version: v1.30.0
  Kube-Proxy Version: v1.30.0
```

* **Addresses:** Each node has both internal and external IP addresses.
* **Other Details:** These include node conditions (such as Ready, OutOfDisk, MemoryPressure), resource capacities, configured taints and tolerations, pod CIDRs, kubelet version, and cloud provider-specific external IDs.

The following diagram provides further insight into node metadata:

<Frame>
  ![The image explains node metadata in a Kubernetes cluster, showing node name, system info, machine ID, system UUID, and boot ID.](https://kodekloud.com/kk-media/image/upload/v1752871395/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Securing-Node-Metadata-in-Kubernetes/frame_100.jpg)
</Frame>

Additional components such as node conditions, resource capacities, taints, pod CIDRs, kubelet version, and provider-specific IDs combine to offer a comprehensive view of a node within a Kubernetes cluster.

<Frame>
  ![The image outlines key components of node metadata, including node conditions, resource capacities, taints, pod CIDR, kubelet version, and external IDs for EC2, GCE, and Azure.](https://kodekloud.com/kk-media/image/upload/v1752871396/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Securing-Node-Metadata-in-Kubernetes/frame_210.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Securing node metadata is a critical step in safeguarding your Kubernetes environment. Ensure that you follow best practices to restrict access and monitor metadata for any unauthorized modifications.
</Callout>

## Conclusion

In this article, we reviewed the essential components of node metadata within Kubernetes and highlighted the importance of securing this sensitive information. In our next lesson, we will delve deeper into the specific challenges associated with node metadata and explore advanced techniques to enhance security across your Kubernetes clusters.

For further reading, consider these resources:

* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Kubernetes Basics](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
* [Docker Hub](https://hub.docker.com/)
* [Terraform Registry](https://registry.terraform.io/)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/2293d4b5-1622-4e97-8e4f-c6acd0cff669" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 Service Accounts
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Service-Accounts/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Service-Accounts/page)

# Service Accounts

> This article provides a comprehensive guide on service accounts in Kubernetes, focusing on their creation, management, and security features.

Welcome to this comprehensive guide on service accounts in Kubernetes. In this article, we will explain how to work with service accounts—an essential mechanism that enables applications and machines to interact securely with the Kubernetes API. While Kubernetes includes various security features, such as authentication, authorization, and role-based access controls, this guide specifically focuses on service accounts to support application development. For more details on broader security topics, please refer to the [CKA Certification Course - Certified Kubernetes Administrator](https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator).

## Account Types in Kubernetes

Kubernetes supports two types of accounts:

* **User Account:** Used by humans (e.g., administrators or developers).
* **Service Account:** Used by applications or machines (e.g., monitoring tools like Prometheus or CI/CD systems like Jenkins).

Consider a simple example of a Kubernetes dashboard written in Python. The dashboard queries the Kubernetes API to list all Pods and displays the output on a web interface. To authenticate with the Kubernetes API, the dashboard leverages a service account.

<Frame>
  ![The image shows a Kubernetes dashboard interface connected to a Kubernetes cluster with three nodes via the kube-api.](https://kodekloud.com/kk-media/image/upload/v1752871397/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Service-Accounts/frame_110.jpg)
</Frame>

## Creating and Managing Service Accounts

To create a service account for your application, run the following command. In this example, we create a service account named `dashboard-sa`:

```bash theme={null}
kubectl create serviceaccount dashboard-sa
```

After creation, view all service accounts in the current namespace using:

```bash theme={null}
kubectl get serviceaccount
```

When a service account is created, Kubernetes automatically generates a token and stores it as a Secret object. This token is then used by your application for API authentication. An example output could be:

```bash theme={null}
kubectl create serviceaccount dashboard-sa
# Output:
kubectl get serviceaccount
# Output:
# NAME           SECRETS   AGE
# default        1         218d
# dashboard-sa   1         4d
```

You can inspect the details of the service account, including the token, by running:

```bash theme={null}
kubectl describe serviceaccount dashboard-sa
```

This command provides information similar to the following:

```text theme={null}
Name:                dashboard-sa
Namespace:           default
Labels:              <none>
Annotations:         <none>
Image pull secrets:  <none>
Mountable secrets:   dashboard-sa-token-kbbdm
Tokens:              dashboard-sa-token-kbbdm
Events:              <none>
```

The associated token (e.g., `dashboard-sa-token-kbbdm`) is stored in a Secret. To view its details, run:

```bash theme={null}
kubectl describe secret dashboard-sa-token-kbbdm
```

The output will display:

```text theme={null}
Name:         dashboard-sa-token-kbbdm
Namespace:    default
Labels:       <none>
Type:         kubernetes.io/service-account-token

Data
====
ca.crt:     1025 bytes
namespace:  7 bytes
token:      eyJhbGciOiJSUzI1NiIsImtpZCI6Ij...
```

This token is used as a bearer token in API requests. For example, you can use it with a `curl` command:

```bash theme={null}
curl https://192.168.56.70:6443/api -insecure \
  --header "Authorization: Bearer eyJhbgG..."
```

<Callout icon="lightbulb" color="#1CB2FE">
  If your third-party application is deployed within the Kubernetes cluster (for example, a custom dashboard or Prometheus), Kubernetes can automatically mount the service account token as a volume inside the pod. This simplifies token management since the token becomes immediately accessible without manual intervention.
</Callout>

## Default Service Account Behavior

By default, every Kubernetes namespace contains a default service account. When a pod is created without specifying a service account, Kubernetes mounts the default service account's token automatically. Consider the following pod definition for a custom Kubernetes dashboard application:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: my-kubernetes-dashboard
spec:
  containers:
    - name: my-kubernetes-dashboard
      image: my-kubernetes-dashboard
```

When this pod is launched, Kubernetes automatically mounts the default service account token. You can verify this with:

```bash theme={null}
kubectl describe pod my-kubernetes-dashboard
```

The description will include a volume mount similar to:

```text theme={null}
Name:           my-kubernetes-dashboard
Namespace:      default
Annotations:    <none>
Status:         Running
IP:             10.244.0.15
Containers:
  my-kubernetes-dashboard:
    Image:      my-kubernetes-dashboard
Mounts:
  /var/run/secrets/kubernetes.io/serviceaccount from default-token-j4hkv (ro)
Volumes:
  default-token-j4hkv:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-j4hkv
    Optional:    false
```

To inspect the contents of the mounted token, execute:

```bash theme={null}
kubectl exec -it my-kubernetes-dashboard -- ls /var/run/secrets/kubernetes.io/serviceaccount
```

Expected output:

```bash theme={null}
# ca.crt  namespace  token
```

To view the token content:

```bash theme={null}
kubectl exec -it my-kubernetes-dashboard -- cat /var/run/secrets/kubernetes.io/serviceaccount/token
```

The output will be the token string (truncated for brevity).

## Using a Custom Service Account

If you prefer to use the `dashboard-sa` service account created earlier, update your pod specification as shown below. Note that changing the service account for a running pod requires deletion and recreation. Deployments, however, automatically trigger a rollout when updated:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: my-kubernetes-dashboard
spec:
  serviceAccountName: dashboard-sa
  containers:
    - name: my-kubernetes-dashboard
      image: my-kubernetes-dashboard
```

After deployment, verify the pod uses the new service account:

```bash theme={null}
kubectl describe pod my-kubernetes-dashboard
```

The volume mount should now reference `dashboard-sa-token-kbbdm`.

If you wish to prevent the automatic mounting of a service account token, set the field `automountServiceAccountToken: false` as shown:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: my-kubernetes-dashboard
spec:
  automountServiceAccountToken: false
  containers:
    - name: my-kubernetes-dashboard
      image: my-kubernetes-dashboard
```

## Kubernetes Version Changes: 1.22 and 1.24

Before Kubernetes v1.22, every service account was automatically associated with a Secret containing an unbounded token without an expiry date. For example:

```bash theme={null}
kubectl get serviceaccount
# Output:
# NAME      SECRETS   AGE
kubectl describe pod my-kubernetes-dashboard
# (Output shows the secret mounted as described above)
```

With Kubernetes v1.22, the token request API was introduced (KEP 1205). Tokens generated via this API are:

* Audience-bound
* Time-bound
* Object-bound

When a pod is created now, Kubernetes communicates with the token controller API to produce a token with a defined lifetime. The following example demonstrates a pod definition using a projected volume:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  namespace: default
spec:
  containers:
    - name: nginx
      image: nginx
      volumeMounts:
        - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
          name: kube-api-access-6mtg8
          readOnly: true
  volumes:
    - name: kube-api-access-6mtg8
      projected:
        defaultMode: 420
        sources:
          - serviceAccountToken:
              expirationSeconds: 3607
              path: token
          - configMap:
              name: kube-root-ca.crt
              items:
                - key: ca.crt
                  path: ca.crt
          - downwardAPI:
              items:
                - fieldRef:
                    apiVersion: v1
                    fieldPath: metadata.namespace
```

Starting with Kubernetes v1.24, service accounts no longer automatically create a Secret with an unbounded token. Instead, you need to generate a token explicitly through the token request API:

```bash theme={null}
kubectl create token dashboard-sa
```

This command outputs a token with an expiry (default is one hour unless configured otherwise). To inspect token details, you can decode it using tools such as JWT.io or by running:

```bash theme={null}
jq -R 'split(".") | select(length > 0) | .[0] | @base64 | fromjson' <<< eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6ZGVmYXVsdC1kYXNob2FyZC1zYSIsImF1ZCI6WyJodHRwczovL2t1YmVybmV0ZXMuZGVmYXVsdC5zdmMuY2x1c3Rlci5sb2NhbCJdLCJleHBpcmF0aW9uIjoxNjY0MDM3NzYzLCJpc3MiOiJodHRwczovL2t1YmVybmV0ZXMuZGVmYXVsdC5zdmMuY2x1c3Rlci5sb2NhbCJ9.k5Y3R-
```

If you decide to revert to the old method of manually creating a Secret, you can do so by defining a Secret with the type `kubernetes.io/service-account-token` and adding the appropriate annotation:

```yaml theme={null}
apiVersion: v1
kind: Secret
type: kubernetes.io/service-account-token
metadata:
  name: mysecretname
  annotations:
    kubernetes.io/service-account.name: dashboard-sa
```

Ensure that the service account exists before creating the Secret to guarantee proper association. However, the recommended practice is to utilize the token request API for better security and token management.

<Frame>
  ![The image shows a JWT (JSON Web Token) decoding interface with encoded data on the left and decoded JSON data on the right.](https://kodekloud.com/kk-media/image/upload/v1752871398/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Service-Accounts/frame_560.jpg)
</Frame>

The diagram above illustrates how tokens without an expiry can cause security and scalability concerns; these issues are mitigated by the token request API.

<Frame>
  ![The image discusses Kubernetes v1.22's KEP 1205, highlighting security and scalability issues with JWTs in service account tokens.](https://kodekloud.com/kk-media/image/upload/v1752871400/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Service-Accounts/frame_580.jpg)
</Frame>

With Kubernetes v1.22 and later, tokens are audience-bound and time-bound, eliminating issues associated with indefinitely valid tokens. Kubernetes v1.24 further refines this approach by minimizing non-expiring secret-based tokens in favor of tokens generated via the token request API.

<Frame>
  ![The image is a slide about Kubernetes v1.22, focusing on KEP 1205 for Bound Service Account Tokens, featuring TokenRequestAPI with audience and time-bound features.](https://kodekloud.com/kk-media/image/upload/v1752871401/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Service-Accounts/frame_620.jpg)
</Frame>

Below is an additional example of a pod using a projected volume, reflecting the token generation via the token request API:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  namespace: default
spec:
  containers:
    - name: nginx
      image: nginx
      volumeMounts:
        - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
          name: kube-api-access-6mtg8
          readOnly: true
  volumes:
    - name: kube-api-access-6mtg8
      projected:
        defaultMode: 420
        sources:
          - serviceAccountToken:
              expirationSeconds: 3607
              path: token
          - configMap:
              name: kube-root-ca.crt
              items:
                - key: ca.crt
                  path: ca.crt
          - downwardAPI:
              items:
                - fieldRef:
                    apiVersion: v1
                    fieldPath: metadata.namespace
```

Prior to these enhancements, the service account token was mounted as a traditional Secret. Today, it is provided as a projected volume that interacts dynamically with the token controller API.

<Callout icon="triangle-alert" color="#FF6B6B">
  If you require a non-expiring token and are aware of the security implications, you can create a Secret manually. However, using the token request API is strongly recommended for enhanced security.
</Callout>

To generate a token using this approach, run:

```bash theme={null}
kubectl create token dashboard-sa
```

This command returns a token with a defined lifetime, ensuring higher security standards.

<Frame>
  ![The image explains Kubernetes service account token secrets, recommending the TokenRequest API for secure token management since version 1.22.](https://kodekloud.com/kk-media/image/upload/v1752871402/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Service-Accounts/frame_830.jpg)
</Frame>

For further information on these changes, please consult the following resources:

* [Kubernetes Enhancement Proposals](https://github.com/kubernetes/enhancements)
* [Official Kubernetes Documentation on Service Accounts and Secrets](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)

<Frame>
  ![The image lists references related to Kubernetes service account tokens, including links to GitHub and Kubernetes documentation.](https://kodekloud.com/kk-media/image/upload/v1752871403/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Service-Accounts/frame_870.jpg)
</Frame>

Thank you for reading this detailed guide on Kubernetes service accounts.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/ec30ede6-4fb2-44ce-bfa4-9b2d250088b4" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/91ec7013-793b-4d2b-af05-0c0b01fc81c9" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 TLS Basics
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/TLS-Basics/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/TLS-Basics/page)

# TLS Basics

> This article covers the fundamentals of SSL/TLS certificates, their role in securing web communications, and configuring them for SSH access.

Welcome to this comprehensive lesson on SSL/TLS certificates. In this session, you'll learn the fundamentals of TLS certificates, their critical role in securing web communications over HTTPS, and how to properly configure them. We will also explore how key pairs secure SSH access to servers.

When users connect to a web server, TLS certificates encrypt communication and verify the server’s identity. Without secure connectivity, sensitive data—such as online banking credentials—could be transmitted in plaintext, making it vulnerable to interception and misuse. Encryption transforms readable data (plaintext) into ciphertext, ensuring that intercepted data remains unreadable if decryption keys are protected.

Data encryption typically involves keys, sets of random characters that facilitate the transformation of plaintext into ciphertext. In symmetric encryption, the same key is used for both encryption and decryption. This method risks key interception if the key travels over the same network channel.

To mitigate this risk, asymmetric encryption is employed. This method uses a key pair: a private key kept secret and a public key that anyone can use to encrypt data. Data encrypted with the public key can only be decrypted using the private key, ensuring secure communication even if the public key is known.

<Frame>
  ![The image illustrates asymmetric encryption, showing a private key and a public key with corresponding icons.](https://kodekloud.com/kk-media/image/upload/v1752871404/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-TLS-Basics/frame_150.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Asymmetric encryption uses a public/private key pair. The private key remains confidential, while the public key is distributed openly for encrypting data.
</Callout>

## Securing SSH with Key Pairs

Securing SSH access to servers is a common use case for key pairs. Instead of traditional passwords—which are prone to compromise—you generate a pair of keys. The public key is placed on the server, while the private key remains with you, ensuring that only you can access the server.

To generate SSH keys, run the following command:

```bash theme={null}
ssh-keygen
```

This creates two files:

* `id_rsa`: the private key
* `id_rsa.pub`: the public key

To secure your server, add the contents of your public key file to the `~/.ssh/authorized_keys` file on the server:

```bash theme={null}
# Display authorized keys on the server
cat ~/.ssh/authorized_keys
```

Then, access the server using your private key with:

```bash theme={null}
ssh -i id_rsa user1@server1
```

A successful login message confirms that your secure SSH access is established. If you need to secure multiple servers, simply copy your public key to each server. Likewise, other users can generate their own key pairs and have their public keys added to the appropriate `authorized_keys` files.

## Securing Web Servers with TLS

Using only symmetric encryption for a web server poses a risk because the encryption key must be transmitted over the network. Asymmetric encryption resolves this by securely transmitting a symmetric key between the client and server.

For HTTPS, when a user visits a website, the server sends its public key within an SSL/TLS certificate. Even if an attacker intercepts the public key, they cannot decrypt the symmetric key because only the server holds the corresponding private key.

Use OpenSSL to generate a pair of RSA keys for your web server:

```bash theme={null}
openssl genrsa -out my-bank.key 1024
openssl rsa -in my-bank.key -pubout > mybank.pem
```

When a user connects:

1. The server sends its public key embedded in a certificate.
2. The browser encrypts a newly generated symmetric key with this public key.
3. The server uses its private key to decrypt the symmetric key.
4. Future communication is secured using the symmetric key.

This mechanism ensures that even if the symmetric key and the public key are intercepted, only the server (with its private key) can decrypt the key and maintain secure communications.

## The Role of Digital Certificates

Digital certificates serve as more than just containers for public keys. They provide essential details including:

* Certificate owner's identity (subject)
* Issuer’s identity
* Validity dates
* Subject Alternative Names (SANs) for multiple domain support

For example, a certificate may contain details such as:

```text theme={null}
Certificate:
    Data:
        Serial Number: 420327018966204255
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN=kubernetes
        Validity
            Not After : Feb  9 13:41:28 2020 GMT
        Subject: CN=my-bank.com
        X509v3 Subject Alternative Name:
            DNS:mybank.com, DNS:i-bank.com,
            DNS:we-bank.com,
        Subject Public Key Info:
            00:b9:b0:55:24:fb:a4:ef:77:73:7c:9b
```

<Frame>
  ![The image shows a digital certificate for "my-bank.com" with details like serial number, signature algorithm, issuer, validity, and subject alternative names.](https://kodekloud.com/kk-media/image/upload/v1752871413/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-TLS-Basics/frame_630.jpg)
</Frame>

If the domain name on the certificate doesn’t match the URL or if the certificate is self-signed by an unknown entity, browsers will display a warning.

## Certifying Trust with Certificate Authorities

While anyone can create a certificate (including fraudulent ones), trusted Certificate Authorities (CAs) such as Symantec, DigiCert, Komodo, or GlobalSign play a vital role in establishing trust. The process is as follows:

1. Generate a Certificate Signing Request (CSR) using your private key and domain name:

   ```bash theme={null}
   openssl req -new -key my-bank.key -out my-bank.csr -subj "/C=US/ST=CA/O=MyOrg, Inc./CN=my-bank.com"
   ```

2. Submit the CSR to a CA.

3. The CA verifies your information and, once validated, signs your certificate.

4. The signed certificate is returned and installed on your server, ensuring that browsers trust your website.

<Frame>
  ![The image illustrates a Certificate Authority (CA) process, featuring logos of Symantec, GlobalSign, and DigiCert, with steps for certificate signing, validation, and issuance to "MY-BANK.COM".](https://kodekloud.com/kk-media/image/upload/v1752871414/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-TLS-Basics/frame_790.jpg)
</Frame>

Browsers inherently trust certificates from recognized CAs because they come preloaded with the public keys of these authorities. This allows browsers to verify that a certificate is legitimate.

While public CAs secure external websites like e-commerce platforms, private CAs can also be used to secure internal applications, such as corporate intranets and payroll systems.

<Frame>
  ![The image illustrates the concept of Certificate Authorities (CAs) with logos, a secure online banking webpage, and a digital certificate for "MY-BANK.COM."](https://kodekloud.com/kk-media/image/upload/v1752871415/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-TLS-Basics/frame_900.jpg)
</Frame>

## Recap of TLS Communication

Below is an overview of the TLS communication process:

| Step                            | Process Description                                                                                          |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **1. Key Pair Generation**      | An administrator generates a key pair for SSH and the web server generates a key pair for HTTPS.             |
| **2. CSR Creation**             | The web server creates a Certificate Signing Request (CSR) and submits it to a CA.                           |
| **3. Certificate Signing**      | The CA signs the certificate with its private key and returns the signed certificate to the server.          |
| **4. Certificate Distribution** | When users visit the website, the server sends its signed certificate containing its public key.             |
| **5. Certificate Validation**   | The browser validates the certificate using the CA’s public key.                                             |
| **6. Symmetric Key Exchange**   | The browser generates a symmetric key, encrypts it with the server’s public key, and sends it to the server. |
| **7. Secure Communication**     | The server decrypts the symmetric key with its private key, and all subsequent communication is secured.     |

In some advanced scenarios, the server may require a client certificate for mutual authentication, though this is less common for general web access.

This complete framework, which includes CAs, key pairs, digital certificates, and database practices for key management, is known as Public Key Infrastructure (PKI).

<Frame>
  ![The image illustrates Public Key Infrastructure (PKI) with elements like Certificate Authority, client and server certificates, keys, and locks, highlighting security processes.](https://kodekloud.com/kk-media/image/upload/v1752871416/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-TLS-Basics/frame_1100.jpg)
</Frame>

## A Note on Key and Certificate Naming Conventions

Certificates that include a public key typically use the extensions .crt or .pem (for example, server.crt, server.pem, client.crt, or client.pem). Private keys are usually indicated by the extension .key or may include the word “key” in the filename (e.g., server.key or server-key.pem). Adhering to these naming conventions helps distinguish between public certificates and private keys.

<Frame>
  ![The image illustrates the difference between public and private keys, showing file extensions and representations for each type.](https://kodekloud.com/kk-media/image/upload/v1752871417/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-TLS-Basics/frame_1180.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  In this lesson, we've covered how SSL/TLS certificates secure web and SSH communications, the process of certificate generation and signing, and the importance of Certificate Authorities. By understanding these concepts, you can ensure your applications and services maintain robust security.
</Callout>

That concludes our lesson on TLS certificates. We hope this content has provided you with a clearer understanding of how SSL/TLS certificates function to secure communications and verify identities in both SSH and HTTPS scenarios. For more information on related topics, consider visiting the [Kubernetes Documentation](https://kubernetes.io/docs/) or the [Docker Hub](https://hub.docker.com/).

See you in the next lesson!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/f4cd550a-0810-45f4-b594-9e23eab2e1cc" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 TLS Introduction
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/TLS-Introduction/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/TLS-Introduction/page)

# TLS Introduction

> This lesson explores securing Kubernetes clusters using TLS certificates and addresses common troubleshooting issues related to them.

Welcome to this lesson on TLS certificates in Kubernetes. In this guide, we explore how to secure your Kubernetes cluster using TLS certificates while also addressing common troubleshooting issues. Many users have expressed uncertainty when it comes to handling TLS certificates, which is why this lecture series is designed to help you gain the necessary understanding and confidence to work effectively with certificates in Kubernetes.

By the end of this section, you'll be well-prepared to configure and troubleshoot certificates both in general environments and within Kubernetes clusters. Mastering this topic starts with a solid grasp of how TLS certificates function and how certificate authorities play a critical role.

<Frame>
  ![The image lists goals related to TLS certificates, including understanding, generating, configuring, viewing, and troubleshooting them, particularly in the context of Kubernetes.](https://kodekloud.com/kk-media/image/upload/v1752871418/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-TLS-Introduction/frame_70.jpg)
</Frame>

We begin with an overview of certificates, detailing the roles of certificate authorities and the fundamental workings of TLS certificates. If you are already confident in these foundational concepts, you may skip ahead to the sections that focus on Kubernetes-specific implementations and troubleshooting techniques.

<Callout icon="lightbulb" color="#1CB2FE">
  For users new to TLS, don't hesitate to review the basic concepts before diving into Kubernetes-specific details. A strong foundation will make advanced topics easier to understand.
</Callout>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/5dda5c1c-fe69-41f0-a69d-5f86467c3f19" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 TLS in Kubernetes Certificate Creation
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/TLS-in-Kubernetes-Certificate-Creation/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/TLS-in-Kubernetes-Certificate-Creation/page)

# TLS in Kubernetes Certificate Creation

> This article explains generating certificates for a Kubernetes cluster using OpenSSL, focusing on CA, client, and server certificates for secure communication.

In this article, we explain how to generate certificates for a Kubernetes cluster using OpenSSL. While tools like EasyRSA and CFSSL are also available, our focus here is on using OpenSSL. We will start by creating the Certificate Authority (CA) certificates, and then move on to generating client certificates for users and server certificates for core components.

## Generating the CA Certificate

To begin, generate the CA private key, create a certificate signing request (CSR) with the common name "KUBERNETES-CA", and then self-sign it. The CSR includes all certificate details but is unsigned until the CA key is applied.

Run these commands to create your CA certificates:

```bash theme={null}
openssl genrsa -out ca.key 2048
openssl req -new -key ca.key -subj "/CN=KUBERNETES-CA" -out ca.csr
openssl x509 -req -in ca.csr -signkey ca.key -out ca.crt
```

At this point, you have successfully created the CA certificate (`ca.crt`) and its corresponding private key (`ca.key`).

## Generating Client Certificates

### Admin User Certificate

For the admin user, a private key is generated first. Then, a CSR is created with the common name "kube-admin". The certificate is signed using the CA certificate and private key. This naming is essential since it is used within audit logs and other system functions.

Run the following commands to generate the admin user's certificate:

```bash theme={null}
openssl genrsa -out admin.key 2048
openssl req -new -key admin.key -subj "/CN=kube-admin" -out admin.csr
openssl x509 -req -in admin.csr -CA ca.crt -CAkey ca.key -out admin.crt
```

<Callout icon="lightbulb" color="#1CB2FE">
  To differentiate admin users from basic users, you can include group details in the CSR by specifying the Organizational Unit (OU). For example, adding the group `system:masters` grants administrative privileges:

  ```bash theme={null}
  openssl genrsa -out admin.key 2048
  openssl req -new -key admin.key -subj "/CN=kube-admin/O=system:masters" -out admin.csr
  openssl x509 -req -in admin.csr -CA ca.crt -CAkey ca.key -out admin.crt
  ```
</Callout>

The above commands create a signed certificate indicating admin privileges. Similar procedures are used to generate certificates for other Kubernetes components (such as the kube scheduler, controller manager, and kube proxy). These certificates enable secure authentication with the kube API server, allowing REST API calls that use the key, client certificate, and CA certificate. For example:

```bash theme={null}
curl https://kube-apiserver:6443/api/v1/pods \
  --key admin.key --cert admin.crt --cacert ca.crt
```

This call returns a JSON response similar to:

```json theme={null}
{
  "kind": "PodList",
  "apiVersion": "v1",
  "metadata": {
    "selfLink": "/api/v1/pods"
  },
  "items": []
}
```

Most Kubernetes clients consolidate these parameters into a configuration file called KubeConfig, which details the API server endpoint and corresponding certificates.

## Certificate Authorities and Mutual Trust

Both clients and servers must use a shared CA root certificate for secure communication. This mutual trust ensures that the certificates presented by each party are signed by a trusted authority, much like how browsers validate a website’s certificate.

## Generating Server-Side Certificates

### ETCD Server Certificate

For the etcd server, which is critical in high-availability deployments, the certificate generation process is analogous to that for clients. The etcd server may also require additional peer certificates for secure inter-cluster communication.

After generating the key and certificate for the etcd server, reference them in your etcd configuration file. For example, review your configuration via:

```bash theme={null}
cat etcd.yaml
```

And the content of `etcd.yaml` might look like this:

```yaml theme={null}
etcd:
  --advertise-client-urls=https://127.0.0.1:2379
  --key-file=/path-to-certs/etcdserver.key
  --cert-file=/path-to-certs/etcdserver.crt
  --client-cert-auth=true
  --data-dir=/var/lib/etcd
  --initial-advertise-peer-urls=https://127.0.0.1:2380
  --initial-cluster=master=https://127.0.0.1:2380
  --listen-client-urls=https://127.0.0.1:2379
  --listen-peer-urls=https://127.0.0.1:2380
  --name=master
  --peer-cert-file=/path-to-certs/etcdpeer1.crt
  --peer-client-cert-auth=true
  --peer-key-file=/path/to/etcd/peer.key
  --peer-trusted-ca-file=/etc/kubernetes/pki/etcd/ca.crt
  --snapshot-count=10000
  --trusted-ca-file=/etc/kubernetes/pki/etcd/ca.crt
```

<Callout icon="lightbulb" color="#1CB2FE">
  The CA root certificate is critical to verify that only valid clients can establish connections with the etcd server.
</Callout>

### Kube API Server Certificate

The kube API server is the central component of the Kubernetes control plane. This server is recognized by multiple DNS names and IP addresses, so its certificate must include all alternate names.

1. Generate a key and CSR for the kube API server:

   ```bash theme={null}
   openssl req -new -key apiserver.key -subj "/CN=kube-apiserver" -out apiserver.csr
   ```

2. Create an OpenSSL configuration file (e.g., `openssl.cnf`) with the following content to define Subject Alternative Names (SAN):

   ```ini theme={null}
   [req]
   req_extensions = v3_req
   distinguished_name = req_distinguished_name

   [ v3_req ]
   basicConstraints = CA:FALSE
   keyUsage = nonRepudiation
   subjectAltName = @alt_names

   [alt_names]
   DNS.1 = kubernetes
   DNS.2 = kubernetes.default
   DNS.3 = kubernetes.default.svc
   DNS.4 = kubernetes.default.svc.cluster.local
   IP.1 = 10.96.0.1
   IP.2 = 172.17.0.87
   ```

3. Sign the certificate using the CA certificate and key. Once complete, the kube API server certificate is ready for use.

The kube API server’s configuration references these certificates to secure communications. For example:

```bash theme={null}
ExecStart=/usr/local/bin/kube-apiserver \\
  --advertise-address=${INTERNAL_IP} \\
  --allow-privileged=true \\
  --apiserver-count=3 \\
  --authorization-mode=Node,RBAC \\
  --bind-address=0.0.0.0 \\
  --enable-swagger-ui=true \\
  --etcd-cafile=/var/lib/kubernetes/ca.pem \\
  --etcd-certfile=/var/lib/kubernetes/apiserver-etcd-client.crt \\
  --etcd-keyfile=/var/lib/kubernetes/apiserver-etcd-client.key \\
  --etcd-servers=https://127.0.0.1:2379 \\
  --event-ttl=1h \\
  --kubelet-certificate-authority=/var/lib/kubernetes/ca.pem \\
  --kubelet-client-certificate=/var/lib/kubernetes/apiserver-kubelet-client.crt \\
  --kubelet-client-key=/var/lib/kubernetes/apiserver-kubelet-client.key \\
  --kubelet-https=true \\
  --runtime-config=api/all \\
  --service-account-key-file=/var/lib/kubernetes/service-account.pem \\
  --service-cluster-ip-range=10.32.0.0/24 \\
  --service-node-port-range=30000-32767 \\
  --client-ca-file=/var/lib/kubernetes/ca.pem \\
  --tls-cert-file=/var/lib/kubernetes/apiserver.crt \\
  --tls-private-key-file=/var/lib/kubernetes/apiserver.key \\
  --v=2
```

### Kubelet Server and Client Certificates

Each Kubernetes node runs a kubelet, which serves as an HTTPS API server to manage node operations. Every node must possess its own key and certificate pair, typically named after the node (e.g., node-01, node-02, node-03).

The node-specific certificates are then referenced inside the kubelet configuration file. For example:

```yaml theme={null}
kind: KubeletConfiguration
apiVersion: kubelet.config.k8s.io/v1beta1
authentication:
  x509:
    clientCAFile: "/var/lib/kubernetes/ca.pem"
authorization:
  mode: Webhook
clusterDomain: "cluster.local"
```

Client certificates for the kubelet enable authentication against the kube API server. They follow a naming convention using the prefix "system:node:" followed by the node name, ensuring that the API server assigns the correct permissions.

<Frame>
  ![The image illustrates Kubernetes node certificates for nodes 01, 02, and 03, showing their association with kubelet client certificates and keys for secure communication.](https://kodekloud.com/kk-media/image/upload/v1752871420/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-TLS-in-Kubernetes-Certificate-Creation/frame_630.jpg)
</Frame>

## Summary

In this article, we covered the following key steps:

1. **Generating the CA Certificates:**\
   Creating a self-signed CA to sign all other certificates.

2. **Creating Client Certificates:**\
   Generating certificates for admin users and control plane components (like the kube scheduler, controller manager, and kube proxy) for secure authentication.

3. **Securing the Kube API Server:**\
   Producing a kube API server certificate that includes multiple DNS names and IP addresses to guarantee trust.

4. **Generating Server-Side Certificates:**\
   Producing certificates for the etcd server and node-specific certificates for kubelets to enable secure component-to-component communications.

All these certificates play a crucial role in ensuring secure communication within the Kubernetes cluster by verifying the identity of each component via the shared CA certificate.

<Frame>
  ![The image illustrates the process of generating and signing certificates for "Kube Scheduler," showing keys, certificate signing requests, and a certificate.](https://kodekloud.com/kk-media/image/upload/v1752871604/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-TLS-in-Kubernetes-Certificate-Creation/frame_230.jpg)
</Frame>

<Frame>
  ![The image illustrates client and server certificates for Kubernetes components, including admin, scheduler, controller-manager, kube-proxy, etcd server, kube-api server, and kubelet server.](https://kodekloud.com/kk-media/image/upload/v1752871606/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-TLS-in-Kubernetes-Certificate-Creation/frame_300.jpg)
</Frame>

<Frame>
  ![The image illustrates ETCD server and peer configurations, showing certificates and keys, alongside a certificate labeled "ETCD-SERVER" with a decorative border.](https://kodekloud.com/kk-media/image/upload/v1752871607/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-TLS-in-Kubernetes-Certificate-Creation/frame_350.jpg)
</Frame>

<Frame>
  ![The image shows a certificate for a Kube API server, including details like IP addresses and domain names, alongside icons representing a certificate and key.](https://kodekloud.com/kk-media/image/upload/v1752871610/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-TLS-in-Kubernetes-Certificate-Creation/frame_420.jpg)
</Frame>

In the next article, we will explore how to view certificate information and how KubeADM automates certificate configuration.

Happy securing!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/ba0dbcbe-ece9-4738-8ac8-b2d0c1853e5b" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 TLS in Kubernetes
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/TLS-in-Kubernetes/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/TLS-in-Kubernetes/page)

# TLS in Kubernetes

> This article explains securing Kubernetes clusters with TLS certificates, detailing their roles, naming conventions, and application within the environment.

Welcome to this in-depth lesson on securing your Kubernetes cluster with TLS certificates. In this guide, we'll explain the roles and naming conventions of various certificates, and then demonstrate how these concepts apply within a Kubernetes environment.

In a previous discussion, we explored the basics of public and private keys and their role in securing connections. The certificates we reviewed included:

* **Server Certificates:** Deployed on servers.
* **Root Certificates:** Held by the Certificate Authority (CA) to sign server certificates.
* **Client Certificates:** Used by clients to authenticate themselves to the server.

<Callout icon="lightbulb" color="#1CB2FE">
  Certificate files follow specific naming conventions:

  * Certificates containing public keys typically use `.crt` or `.pem` extensions (e.g., `server.crt` or `client.pem`).
  * Private keys often have the term "key" as their extension (e.g., `.key`) or within the filename (e.g., `server-key.pem`).
</Callout>

The image below illustrates the Certificate Authority (CA) system, showing the root, client, and server certificates along with their public and private keys:

<Frame>
  ![The image illustrates a Certificate Authority (CA) system, showing root, client, and server certificates, along with public and private keys for secure communication.](https://kodekloud.com/kk-media/image/upload/v1752871611/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-TLS-in-Kubernetes/frame_60.jpg)
</Frame>

## TLS Components in a Kubernetes Cluster

A secure Kubernetes cluster requires encrypted TLS communications between the master and worker nodes. Whether you are an administrator using `kubectl` or an internal service within the cluster, every interaction relies on TLS-secured connections. There are two main requirements:

1. Server components (e.g., API server, etcd, kubelet) must use TLS certificates to secure communications.
2. Client components (e.g., administrative users, scheduler, controller-manager, kube-proxy) must present valid client certificates for authentication.

### Server Certificates

Below we identify the key server components and their associated certificates:

* **Kube API Server:**\
  The Kube API server provides an HTTPS service for internal components and external users. It requires a server certificate and a private key (`api-server.cert` and `api-server.key`) to secure these communications.

* **etcd Server:**\
  Acting as the primary data store for the cluster, the etcd server necessitates its certificate and key pair, named `etcd-server.crt` and `etcd-server.key`.

* **Kubelet (Worker Nodes):**\
  Every worker node runs the kubelet service, which exposes an HTTPS API endpoint for communication with the API server. For these endpoints, a certificate and key pair (`kubelet.cert` and `kubelet.key`) is used.

The diagram below summarizes the server certificates used by the Kube API, etcd, and kubelet services:

<Frame>
  ![The image illustrates server certificates for Kube-API, ETCD, and Kubelet servers, showing their respective certificate and key files.](https://kodekloud.com/kk-media/image/upload/v1752871613/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-TLS-in-Kubernetes/frame_240.jpg)
</Frame>

### Client Certificates

Now, review the client components that interact with the servers:

* **Admin User:**\
  Administrators connect to the Kubernetes cluster via `kubectl` or direct REST API calls. The admin user authenticates with a client certificate (`admin.crt`) and corresponding key (`admin.key`).

* **Scheduler:**\
  The scheduler queries the API server for pending pods and orchestrates their deployment on the appropriate worker nodes. It uses a certificate and key pairing (`scheduler.cert` and `scheduler.key`) for authentication.

* **Kube Controller Manager:**\
  Similar to the scheduler, the controller manager communicates with the API server using its own certificate for secure authentication.

* **Kube Proxy:**\
  The kube proxy manages network rules on worker nodes and requires a dedicated client certificate (`kube-proxy.crt` and `kube-proxy.key`).

<Callout icon="lightbulb" color="#1CB2FE">
  Sometimes, servers also act as clients when communicating with other services. For example, the Kube API server communicates with the etcd server. In these scenarios, it can use its own certificate (`api-server.crt`/`api-server.key`) or a separate certificate pair specifically generated for authenticating with etcd.
</Callout>

The diagram below provides an overview of how client certificates and keys are used for authentication among Kubernetes components:

<Frame>
  ![The image illustrates the client certificates and keys used for authentication between Kubernetes components like Kube-API server, ETCD server, and others.](https://kodekloud.com/kk-media/image/upload/v1752871614/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-TLS-in-Kubernetes/frame_390.jpg)
</Frame>

### Grouping Certificates

To simplify management, certificates in a Kubernetes cluster can be categorized into two groups:

| Certificate Group   | Description                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------------- |
| Client Certificates | Used by administrators, the scheduler, controller-manager, and kube-proxy to access the Kube API server. |
| Server Certificates | Employed by the Kube API server, etcd server, and kubelet to authenticate incoming client connections.   |

### The Role of the Certificate Authority (CA)

A Certificate Authority (CA) is needed to sign both client and server certificates. Kubernetes requires at least one CA per cluster. In some deployments, a separate CA may be used for the control plane and for etcd. In this lesson, we focus on a single CA whose certificate and key are named `CA.crt` and `CA.key`.

The following diagram offers a comprehensive overview of the client and server certificates for various Kubernetes components, all signed by the CA:

<Frame>
  ![The image illustrates client and server certificates for Kubernetes components, including admin, scheduler, controller-manager, kube-proxy, etcd server, kube-API server, and kubelet server.](https://kodekloud.com/kk-media/image/upload/v1752871615/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-TLS-in-Kubernetes/frame_420.jpg)
</Frame>

This concludes the overview of the TLS certificates used in a Kubernetes cluster along with their respective roles. In the next section of this lesson, we will explore how to generate and sign these certificates using the CA.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/acb7948c-cae2-4fba-8c38-af1e97ffa190" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 Verify Platform Binaries Before Deploying
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Verify-Platform-Binaries-Before-Deploying/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/Verify-Platform-Binaries-Before-Deploying/page)

# Verify platform binaries before deploying

> This lesson covers verifying Kubernetes platform binaries to ensure they are secure and untampered before deployment.

In this lesson, we will learn how to verify platform binaries before deploying a Kubernetes cluster. Verifying these binaries is a critical security step that ensures the downloaded files have not been tampered with during transit over the internet.

The Kubernetes platform binaries are available on the [Kubernetes GitHub release page](https://github.com/kubernetes/kubernetes/releases).

<Frame>
  ![The image shows Kubernetes v1.20.0 release notes, including download links and SHA512 hashes for files and client binaries.](https://kodekloud.com/kk-media/image/upload/v1752871616/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Verify-platform-binaries-before-deploying/frame_10.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Downloading binaries from the internet may expose your system to risks. An attacker with access to your network could potentially intercept download requests and replace genuine files with malicious ones. Since every file has a unique checksum, even a slight modification will result in a completely different hash.
</Callout>

## Steps to Verify the Integrity of Kubernetes Binaries

1. **Download the Binary**\
   Use `curl` to download the Kubernetes binary, as shown in the example below:

   ```bash theme={null}
   curl https://dl.k8s.io/v1.20.0/kubernetes.tar.gz -L -o kubernetes.tar.gz
   ```

2. **Generate the Checksum**\
   After downloading, generate the checksum of the binary file using a checksum utility. Compare this generated hash with the one provided on the release page.

   Here’s how to do it using two different commands based on your operating system:

   * **macOS and Linux (using shasum):**

     ```bash theme={null}
     shasum -a 512 kubernetes.tar.gz
     ```

   * **Linux (using sha512sum):**

     ```bash theme={null}
     sha512sum kubernetes.tar.gz
     ```

<Callout icon="lightbulb" color="#1CB2FE">
  Ensure that the output of the chosen checksum command exactly matches the hash available on the release page. A mismatch may indicate that the file has been tampered with.
</Callout>

## Command Comparison Table

| Operating System | Command Example                   | Description                                   |
| ---------------- | --------------------------------- | --------------------------------------------- |
| macOS            | `shasum -a 512 kubernetes.tar.gz` | Verify file integrity using SHA-512 checksum. |
| Linux            | `sha512sum kubernetes.tar.gz`     | Alternative for generating a 512-bit hash.    |
| Linux/macOS      | `shasum -a 512 kubernetes.tar.gz` | Common command available on multiple systems. |

This lesson walks you through the process of downloading and verifying Kubernetes binaries as a security measure. Further deployment steps will be addressed in subsequent lessons.

For more detailed information on Kubernetes security practices, visit the [Kubernetes Documentation](https://kubernetes.io/docs/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/c2f4a58e-1e1d-49e2-adc9-79e1452c65de" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/65d51a5d-42ab-4594-9ef0-2603ba1d5ffe" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 View Certificate Details
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/View-Certificate-Details/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/View-Certificate-Details/page)

# View Certificate Details

> How to locate, inspect, and validate Kubernetes control plane TLS certificates, check SANs and expiry, and troubleshoot certificate-related failures

Hello — welcome to this lesson. You'll learn how to locate, inspect, and validate TLS certificates used by Kubernetes control plane components so you can perform a cluster-wide certificate health check.

Scenario: you're a new administrator asked to audit certificates in an existing cluster. The first diagnostic step is to identify how the cluster was provisioned, because certificate storage and component invocation change depending on the provisioning method:

* If the control plane runs as native systemd services (custom from-scratch installs), certificate file paths and TLS flags are visible from unit files or the running processes.
* If the cluster was provisioned with kubeadm, control plane components run as static pods; manifests live under /etc/kubernetes/manifests and certificates are typically under /etc/kubernetes/pki.

Note: kubeadm places static manifests under /etc/kubernetes/manifests and certificates under /etc/kubernetes/pki by default.

<Callout icon="lightbulb" color="#1CB2FE">
  When doing a certificate health check, create a simple spreadsheet (paths, CN, SANs, organization, issuer, expiry) to track the findings across all nodes. Use this spreadsheet format to guide your tracking.
</Callout>

Why inspect certificates?

* Confirm each component presents the correct Subject Common Name (CN) for identity.
* Ensure required Subject Alternative Names (SANs) — DNS and IP — are present.
* Verify the issuer matches your expected CA.
* Detect expired or soon-to-expire certificates to plan rotations and prevent outages.

How to identify certificate files used by control plane components

1. Systemd-managed control plane

* If the control plane is managed via systemd, inspect unit files (typically in /etc/systemd/system or /lib/systemd/system) to find flags pointing at cert/key files. Example unit excerpt for kube-apiserver:

```bash theme={null}
$ cat /etc/systemd/system/kube-apiserver.service
[Service]
ExecStart=/usr/local/bin/kube-apiserver \
  --advertise-address=172.17.0.32 \
  --allow-privileged=true \
  --apiserver-count=3 \
  --authorization-mode=Node,RBAC \
  --bind-address=0.0.0.0 \
  --client-ca-file=/var/lib/kubernetes/ca.pem \
  --enable-swagger-ui=true \
  --etcd-cafile=/var/lib/kubernetes/ca.pem \
  --etcd-certfile=/var/lib/kubernetes/kubernetes.pem \
  --etcd-keyfile=/var/lib/kubernetes/kubernetes-key.pem \
  --event-ttl=1h \
  --kubelet-certificate-authority=/var/lib/kubernetes/ca.pem \
  --kubelet-client-key=/var/lib/kubernetes/kubernetes-key.pem \
  --kubelet-https=true \
  --service-node-port-range=30000-32767 \
  --tls-cert-file=/var/lib/kubernetes/kubernetes.pem \
  --tls-private-key-file=/var/lib/kubernetes/kubernetes-key.pem \
  --v=2
```

2. kubeadm / static pod control plane

* Inspect the static pod manifest for the kube-apiserver under /etc/kubernetes/manifests to find the exact certificate paths and filenames used by the control plane container:

```bash theme={null}
$ cat /etc/kubernetes/manifests/kube-apiserver.yaml
spec:
  containers:
  - command:
    - kube-apiserver
    - --authorization-mode=Node,RBAC
    - --advertise-address=172.17.0.32
    - --allow-privileged=true
    - --client-ca-file=/etc/kubernetes/pki/ca.crt
    - --disable-admission-plugins=PersistentVolumeLabel
    - --enable-admission-plugins=NodeRestriction
    - --enable-bootstrap-token-auth=true
    - --etcd-cafile=/etc/kubernetes/pki/etcd/ca.crt
    - --etcd-certfile=/etc/kubernetes/pki/apiserver-etcd-client.crt
    - --etcd-keyfile=/etc/kubernetes/pki/apiserver-etcd-client.key
    - --etcd-servers=https://127.0.0.1:2379
    - --insecure-port=0
    - --kubelet-client-certificate=/etc/kubernetes/pki/apiserver-kubelet-client.crt
    - --kubelet-client-key=/etc/kubernetes/pki/apiserver-kubelet-client.key
    - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
    - --proxy-client-cert-file=/etc/kubernetes/pki/front-proxy-client.crt
    - --proxy-client-key-file=/etc/kubernetes/pki/front-proxy-client.key
    - --requestheader-allowed-names=front-proxy-client
    - --requestheader-client-ca-file=/etc/kubernetes/pki/front-proxy-ca.crt
    - --requestheader-extra-headers-prefix=X-Remote-Extra-
    - --requestheader-group-headers=X-Remote-Group
    - --requestheader-username-headers=X-Remote-User
    - --secure-port=6443
    - --service-account-key-file=/etc/kubernetes/pki/sa.pub
    - --service-cluster-ip-range=10.96.0.0/12
    - --tls-cert-file=/etc/kubernetes/pki/apiserver.crt
    - --tls-private-key-file=/etc/kubernetes/pki/apiserver.key
```

Once you have the certificate file list, inspect each certificate to extract metadata (subject CN, SANs, issuer, validity, etc.).

How to decode and inspect certificates

* Use openssl to read a PEM certificate and inspect its fields:

```bash theme={null}
$ openssl x509 -in /etc/kubernetes/pki/apiserver.crt -text -noout
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 3147495682089747350 (0x2bae26a58f090396)
    Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN=kubernetes
        Validity
            Not Before: Feb 11 05:39:19 2019 GMT
            Not After : Feb 11 05:39:20 2020 GMT
        Subject: CN=kube-apiserver
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
            Public-Key: (2048 bit)
            Modulus:
                00:d9:69:38:80:68:3b:b7:2e:9e:25:00:e8:fd:01:
            Exponent: 65537 (0x10001)
    X509v3 extensions:
        X509v3 Key Usage: critical
            Digital Signature, Key Encipherment
        X509v3 Extended Key Usage:
            TLS Web Server Authentication
        X509v3 Subject Alternative Name:
            DNS:master, DNS:kubernetes, DNS:kubernetes.default,
            DNS:kubernetes.default.svc, DNS:kubernetes.default.svc.cluster.local, IP
            Address:10.96.0.1, IP Address:172.17.0.27
```

What to verify for each certificate

* Subject CN matches the component (e.g., CN=kube-apiserver).
* Expected DNS and IP SANs are present.
* Issuer is the expected CA (kubeadm typically uses CA with CN=kubernetes).
* Certificate validity period is current (check the Not After date for expiry).

Use the table in the first figure below as a pattern for your spreadsheet: include certificate path, CN, SANs, organization, issuer, and expiration.

<Frame>
  <img src="https://mintcdn.com/kodekloud-c4ac6d9a/1UnYm26nZTOghZP0/images/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/View-Certificate-Details/kubeadm-kubernetes-certs-table-paths-expiry.jpg?fit=max&auto=format&n=1UnYm26nZTOghZP0&q=85&s=e301b5beccd8413090ad8f9305a3af43" alt="A dark-themed slide titled &#x22;kubeadm&#x22; showing a table of Kubernetes certificate files with columns for certificate path, CN name, ALT names (DNS/IP SANs), organization, issuer, and expiration dates. It lists entries like /etc/kubernetes/pki/apiserver.crt, ca.crt, kubelet-client and etcd client certificates with their SANs and expiry timestamps." width="1920" height="1080" data-path="images/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/View-Certificate-Details/kubeadm-kubernetes-certs-table-paths-expiry.jpg" />
</Frame>

Reference the official Kubernetes documentation for recommended certificate CNs, default paths, and component requirements: [https://kubernetes.io/docs/concepts/cluster-administration/certificates/](https://kubernetes.io/docs/concepts/cluster-administration/certificates/). The docs include tables of default CNs and expected parent CA relationships.

<Frame>
  <img src="https://mintcdn.com/kodekloud-c4ac6d9a/1UnYm26nZTOghZP0/images/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/View-Certificate-Details/kubernetes-documentation-cert-paths.jpg?fit=max&auto=format&n=1UnYm26nZTOghZP0&q=85&s=97b66972eac2bb793f0c1f8557b85b92" alt="A slide titled &#x22;Kubernetes Documentation Page&#x22; showing two tables that list default CNs, parent CAs, recommended key/cert paths, commands and cert/key arguments for Kubernetes components. The content is on a dark teal background with a small &#x22;© Copyright KodeKloud&#x22; notice in the corner." width="1920" height="1080" data-path="images/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/View-Certificate-Details/kubernetes-documentation-cert-paths.jpg" />
</Frame>

Checking logs when certificates fail

* If components run under systemd, start with the system journal to find TLS handshake and certificate errors:

```bash theme={null}
$ journalctl -u etcd.service -l
```

Example etcd log snippets showing TLS configuration and handshake failure:

```text theme={null}
2019-02-13 02:53:28.144631 I | etcdmain: etcd Version: 3.2.18
2019-02-13 02:53:28.185588 I | embed: ClientTLS: cert = /etc/kubernetes/pki/etcd/server.crt, key = /etc/kubernetes/pki/etcd/server.key, ca = , trusted-ca = /etc/kubernetes/pki/etcd/old-ca.crt, client-cert-auth = true
2019-02-13 02:53:30.080130 I | etcdserver: published {Name:master ClientURLs:[https://127.0.0.1:2379]} to cluster
WARNING: 2019/02/13 02:53:30 Failed to dial 127.0.0.1:2379: connection error: desc = "transport: authentication handshake failed: remote error: tls: bad certificate"; please retry.
```

* If control plane components are running as static pods (kubeadm), view pod logs with kubectl. Replace \<etcd-pod> with the actual pod name and add -n kube-system if necessary:

```bash theme={null}
$ kubectl logs <etcd-pod> -n kube-system
```

Example pod log output (you may see TLS/handshake errors similar to the systemd example above).

* If the control plane is down and kubectl cannot reach the API server, check the container runtime logs directly:
  * For CRI-based runtimes (containerd/crio) use crictl:

```bash theme={null}
$ crictl ps -a
$ crictl logs <container-id>
```

* For Docker runtime:

```bash theme={null}
$ docker ps -a
$ docker logs <container-id>
```

What to do with findings

* Missing SANs: reissue the certificate including the correct DNS/IP SANs.
* Expired certificates: rotate/reissue them. Kubeadm provides certificate management helpers (see kubeadm certs docs).
* Unexpected issuer: investigate whether a certificate was manually replaced or issued by an unknown CA.

Quick verification checklist

| Check                                        | Command / Method                                   | Expected result                                                            |
| -------------------------------------------- | -------------------------------------------------- | -------------------------------------------------------------------------- |
| Locate kube-apiserver cert flags             | Inspect systemd unit or static manifest            | Flags point to cert/key paths under /etc/kubernetes or /var/lib/kubernetes |
| Read certificate metadata                    | openssl x509 -in /path/to/cert -text -noout        | CN, SANs, issuer and Not After present and correct                         |
| Check certificate expiry                     | openssl x509 -in /path/to/cert -noout -dates       | Not After should be in the future                                          |
| Search component TLS errors                  | journalctl -u \<service> -l or kubectl logs \<pod> | TLS handshake errors or bad certificate messages indicate issues           |
| Inspect container logs if control plane down | crictl logs / docker logs                          | Determine why the control plane cannot present or validate certs           |

Useful links and references

* Kubernetes Certificates concept: [https://kubernetes.io/docs/concepts/cluster-administration/certificates/](https://kubernetes.io/docs/concepts/cluster-administration/certificates/)
* kubeadm certificate management: [https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-certs/](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-certs/)

Closing notes

* Collect findings into the spreadsheet described in the callout to track certificate path, CN, SANs, issuer, and expiry across nodes.
* Test these steps in a lab environment before running them on production clusters to avoid accidental outages.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/39c4246e-7a13-4187-beac-585ff0d7b1fa" />
</CardGroup>

---


# 📂 Section: Cluster Setup and Hardening
## 📖 What are CIS Benchmarks
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/What-are-CIS-Benchmarks/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Cluster-Setup-and-Hardening/What-are-CIS-Benchmarks/page)

# What are CIS Benchmarks

> This article explores the importance of CIS benchmarks in securing systems and best practices for safeguarding IT environments.

Welcome to this lesson on CIS benchmarks. In this article, we will explore the importance of CIS benchmarks in securing systems and walk through the best practices used to safeguard IT environments.

## Understanding Security Benchmarks

Before diving into CIS benchmarks, it is essential to understand what a security benchmark entails. If you have experience as a systems administrator or have performed security audits, you are likely familiar with the process of hardening systems. For instance, imagine deploying a fresh Ubuntu 18.04 server in your data center. Before hosting production applications on it, securing the system is a critical first step.

Systems face numerous vulnerabilities. For example, an unauthorized individual might plug a USB drive into your server to introduce malware. To counter such risks, unused USB ports and peripheral slots should be disabled. Similarly, robust access control measures are necessary; instead of enabling direct root logins, administrators should configure individual user accounts with sudo privileges. This approach promotes accountability and minimizes the risk of inadvertent or unauthorized changes.

Here are some key security best practices to consider:

* Configure sudo so that only designated users receive elevated permissions.
* Implement strict firewall or IPTables rules to allow only essential network traffic.
* Disable all non-essential services, ensuring that mission-critical services such as NTP for time synchronization remain active.
* Set proper file permissions and disable unnecessary file systems.
* Enable auditing and logging to monitor any modifications or potential intrusions.

<Frame>
  ![The image outlines a "Security Benchmark" with categories: Access, Network, Services, Physical Devices (USB), Logging, Auditing, and Filesystems, centered around a device icon.](https://kodekloud.com/kk-media/image/upload/v1752871619/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-What-are-CIS-Benchmarks/frame_140.jpg)
</Frame>

New vulnerabilities are continuously emerging. It is crucial to stay updated by continually upgrading, patching, and reconfiguring your systems to mitigate potential attacks.

## Introduction to CIS Benchmarks

CIS, or the Center for Internet Security, is a nonprofit organization focused on enhancing cybersecurity through community-driven best practices. Their mission is to create a safer connected world by developing, validating, and promoting actionable security recommendations. Visit the [CIS website](https://www.cisecurity.org) to explore cybersecurity benchmarks across more than 25 technology categories, such as:

* Operating Systems (Linux, Windows, macOS)
* Public Cloud Platforms (Google Cloud, Azure, AWS)
* Mobile Platforms (iOS, Android)
* Network Devices (Check Point, Cisco, Juniper, Palo Alto Networks)
* Desktop Software (web browsers, MS Office, Zoom)
* Server Software (web servers like Tomcat and Nginx)
* Virtualization Technologies (VMware, Docker, Kubernetes)

Users can register on the CIS website to download the benchmarks that suit their specific environment.

<Frame>
  ![The image is a table from the Center for Internet Security, listing various technology categories like OS, Cloud, Mobile, Network, Desktop, and Server, with examples under each.](https://kodekloud.com/kk-media/image/upload/v1752871620/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-What-are-CIS-Benchmarks/frame_250.jpg)
</Frame>

Each CIS benchmark includes detailed security recommendations:

* An explanation of the risks associated with non-compliant configurations.
* Step-by-step instructions to verify if a security risk exists, including the necessary commands.
* Procedures to resolve identified issues.

For example, to check the configuration for USB storage, you can execute the following command:

```bash theme={null}
# modprobe -n -v usb-storage
```

<Callout icon="lightbulb" color="#1CB2FE">
  CIS not only provides these best practices but also offers tools for automated assessments. The [CIS CAT](https://www.cisecurity.org/cis-cat-pro/) (Configuration Assessment Tool) automates the process of comparing your server's configuration against CIS benchmarks and generates a comprehensive HTML report.
</Callout>

The CIS CAT report summarizes which security recommendations have been implemented and identifies areas requiring attention.

<Frame>
  ![The image shows a security configuration summary from the Center for Internet Security, detailing test results with pass, fail, and scoring percentages for various setup and service categories.](https://kodekloud.com/kk-media/image/upload/v1752871621/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-What-are-CIS-Benchmarks/frame_310.jpg)
</Frame>

This assessment displays which tests passed and which failed, along with corresponding scores for each category. Users can click on each group for a detailed breakdown of the results.

<Frame>
  ![The image shows a CIS assessment results table, listing filesystem configuration checks with "Fail" and "Pass" results for various benchmark items.](https://kodekloud.com/kk-media/image/upload/v1752871623/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-What-are-CIS-Benchmarks/frame_330.jpg)
</Frame>

In a later section of this lesson, you will perform a CIS Benchmark assessment on an Ubuntu system. You will review the generated report, remediate specific issues based on the findings, and run the assessment again to confirm that all security concerns have been addressed.

Good luck, and we look forward to guiding you through the next lesson on enhancing system security with CIS benchmarks.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/9ae0e34b-1251-45d2-8b10-12e59f2d3c83" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/eac6dac8-4481-4138-96ef-a2135f20e05e/lesson/1f579418-522f-4c04-81f8-4b8ae7f6a2dc" />
</CardGroup>

---


