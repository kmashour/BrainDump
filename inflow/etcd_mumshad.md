> ## Documentation Index
> Fetch the complete documentation index at: https://notes.kodekloud.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ETCD for Beginners

> This article introduces etcd, a distributed key-value store, covering its operation, installation, and transition from API v2 to v3.

This article provides a concise introduction to etcd—a distributed, reliable key-value store that is both simple and fast. Whether you’re new to key-value storage concepts or already familiar with etcd’s role in Kubernetes environments, this guide offers valuable insights into its operation and quick start instructions using the etcdctl client tool.

<Frame>
  ![The image lists objectives for learning about ETCD, including its definition, operation, and related concepts like distributed systems and the RAFT protocol.](https://kodekloud.com/kk-media/image/upload/v1752869713/notes-assets/images/CKA-Certification-Course-Certified-Kubernetes-Administrator-ETCD-for-Beginners/frame_20.jpg)
</Frame>

Later in the article, we will dive deeper into high availability topics. You’ll learn about distributed systems, how etcd operates in cluster mode, the Raft consensus protocol, and best practices for configuring a resilient etcd cluster.

## What Is a Key-Value Store?

Traditional relational databases, such as SQL databases, store data in tables with rows and columns. For example, a table that contains information about individuals might look like this:

* Each row represents a single person.
* Each column holds a specific detail about that person (e.g., name, age).

If you need to include additional information (like salary data for employed individuals or grades for students), you must expand the table. This means adding columns that may not apply universally to every row.

In contrast, a key-value store organizes data as independent documents or files. Each document contains all relevant information for an individual, allowing flexible and dynamic data structures:

* Working individuals can have documents with salary details.
* Students can have documents with grade details.

<Frame>
  ![The image shows a key-value store with tables listing names, ages, locations, and either salaries or grades for different individuals.](https://kodekloud.com/kk-media/image/upload/v1752869714/notes-assets/images/CKA-Certification-Course-Certified-Kubernetes-Administrator-ETCD-for-Beginners/frame_120.jpg)
</Frame>

For complex data transactions, structured formats like JSON or YAML are used. Here are some examples of key-value pairs stored as JSON documents:

```json theme={null}
{
  "name": "John Doe",
  "age": 45,
  "location": "New York",
  "salary": 5000
}
```

```json theme={null}
{
  "name": "Dave Smith",
  "age": 34,
  "location": "New York",
  "salary": 4000,
  "organization": "ACME"
}
```

```json theme={null}
{
  "name": "Aryan Kumar",
  "age": 10,
  "location": "New York",
  "Grade": "A"
}
```

```json theme={null}
{
  "name": "Lily Oliver",
  "age": 15,
  "location": "Bangalore",
  "Grade": "B"
}
```

```json theme={null}
{
  "name": "Lauren Rob",
  "age": 13,
  "location": "Bangalore",
  "Grade": "C"
}
```

## Installing and Getting Started with etcd

Getting started with etcd is straightforward. First, download the correct binary for your operating system from the GitHub releases page, extract the archive, and run the etcd executable. By default, etcd listens on port 2379, allowing you to use the etcdctl client tool to store and retrieve key-value pairs.

For example, you can download etcd using the following command:

```bash theme={null}
curl -L https://github.com/etcd-io/etcd/releases/download/v3.3.11/etcd-v3.3.11-linux-amd64.tar.gz -o etcd-v3.3.11-linux-amd64.tar.gz
```

After extracting and starting etcd, the accompanying command-line client, etcdctl, lets you interact with your etcd instance. To store a key-value pair using the etcd API v2, run:

```bash theme={null}
./etcdctl set key1 value1
```

And to retrieve it:

```bash theme={null}
./etcdctl get key1
```

If you run the etcdctl command without any arguments, it displays a list of available commands similar to this:

```bash theme={null}
./etcdctl
```

```text theme={null}
NAME:
etcdctl - A simple command line client for etcd.

COMMANDS:
  backup          backup an etcd directory
  cluster-health  check the health of the etcd cluster
  mk              make a new key with a given value
  mkdir           make a new directory
  rm              remove a key or a directory
  rmdir           removes the key if it is an empty directory or a key-value pair
  get             retrieve the value of a key
```

<Callout icon="lightbulb" color="#1CB2FE">
  Different articles may reference varying versions of etcd. Understanding its version history—starting with version 0.1 in August 2013, introducing the Raft consensus algorithm in version 2.0 (February 2015), and further optimizations in version 3 (January 2017)—can clarify command differences. The etcd project was incubated in the CNCF in November 2018.
</Callout>

<Frame>
  ![The image lists ETCD versions with their release dates from August 2013 to November 2018, noting CNCF incubation.](https://kodekloud.com/kk-media/image/upload/v1752869715/notes-assets/images/CKA-Certification-Course-Certified-Kubernetes-Administrator-ETCD-for-Beginners/frame_270.jpg)
</Frame>

## Transitioning from API v2 to v3

One critical change between etcd versions is the API version used by etcdctl. Although etcdctl may be configured to use API v2 by default, newer installations typically default to API v3. You can verify the API version by running:

```bash theme={null}
./etcdctl --version
```

This command might output:

```text theme={null}
etcdctl version: 3.3.11
API version: 2
```

When you list available commands in API v2 mode:

```bash theme={null}
./etcdctl
```

the command list includes options like:

```text theme={null}
COMMANDS:
  backup               backup an etcd directory
  cluster-health       check the health of the etcd cluster
  mk                   make a new key with a given value
  mkdir                make a new directory
  rm                   remove a key or a directory
  rmdir                removes the key if it is an empty directory or a key-value pair
  get                  retrieve the value of a key
  ls                   retrieve a directory
  set                  set the value of a key
  setdir               create a new directory or update an existing directory TTL
  update               update an existing key with a given value
  updatedir           update an existing directory
  watch                watch a key for changes
  exec-watch           watch a key for changes and exec an executable
  member               member add, remove and list subcommands
  user                 user add, grant and revoke subcommands
  role                 role add, grant and revoke subcommands
```

To switch etcdctl to use API v3, you have two options:

1. Prepend the environment variable to the command:

   ```bash theme={null}
   ETCDCTL_API=3 ./etcdctl version
   ```

   This produces the output:

   ```text theme={null}
   etcdctl version: 3.3.11
   API version: 3
   ```

2. Or, export the environment variable for your session:

   ```bash theme={null}
   export ETCDCTL_API=3
   ./etcdctl version
   ```

   The output will similarly confirm the switch to API v3.

<Callout icon="lightbulb" color="#1CB2FE">
  In API v3, the command for setting a key changes from "set" to "put", while retrieving a key remains the same ("get"). Note that the `version` command is now a subcommand rather than an option.
</Callout>

After setting the environment variable, you can perform key-value operations with API v3 commands. For example:

```bash theme={null}
export ETCDCTL_API=3
./etcdctl version
```

Expected output:

```text theme={null}
etcdctl version: 3.3.11
API version: 3
```

Then, set a key-value pair:

```bash theme={null}
./etcdctl put key1 value1
```

This should output:

```text theme={null}
OK
```

And retrieve the value:

```bash theme={null}
./etcdctl get key1
```

Expected output:

```text theme={null}
key1
value1
```

## Conclusion

In this article, we explored etcd and the fundamentals of key-value storage, contrasting it with traditional relational databases. We demonstrated how to install etcd, use the etcdctl command-line tool, and navigate the transition from API v2 to API v3. In our upcoming article, we will examine how to configure etcd in a high-availability environment and its seamless integration with Kubernetes.

Thank you for reading, and stay tuned for further insights into etcd and distributed systems.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/c6d2ac7d-8192-4cff-aa54-e36d888c5bd9/lesson/7f4bf5f0-6a1f-4644-8a07-42a1d330c4c3" />
</CardGroup>
> ## Documentation Index
> Fetch the complete documentation index at: https://notes.kodekloud.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ETCD in Kubernetes

> This article explores the role of etcd in Kubernetes, covering deployment methods and high availability considerations.

Welcome to this comprehensive guide on etcd in Kubernetes. In this article, we explore the critical role of etcd in storing cluster state, detail different deployment approaches, and explain high availability considerations. Whether you're setting up a Kubernetes cluster from scratch or using kubeadm, understanding etcd is essential.

etcd is a distributed key-value store that maintains configuration data, state information, and metadata for your Kubernetes cluster. Every object—nodes, pods, configurations, secrets, accounts, roles, and role bindings—is stored within etcd. When you run a command like `kubectl get`, the data is retrieved from this data store.

<Frame>
  ![The image illustrates a Kubernetes architecture with a master node managing an ETCD cluster, listing components like nodes, pods, configs, and more.](https://kodekloud.com/kk-media/image/upload/v1752869716/notes-assets/images/CKA-Certification-Course-Certified-Kubernetes-Administrator-ETCD-in-Kubernetes/frame_20.jpg)
</Frame>

Any changes you make to the cluster—whether adding nodes, deploying pods, or configuring ReplicaSets—are first recorded in etcd. Only after etcd is updated are these changes considered to be complete.

<Callout icon="lightbulb" color="#1CB2FE">
  The etcd server typically listens on port 2379 for client requests. Ensuring that the advertised client URL (via the `--advertise-client-urls` option) is correctly configured is crucial for proper communication between the Kubernetes API Server and etcd.
</Callout>

## Deployment Methods

Depending on your Kubernetes setup, you can deploy etcd in two primary ways: manually from scratch or automatically with kubeadm. Each method has its use cases, with manual setups providing a deeper understanding of etcd configurations and kubeadm streamlining the deployment process.

***

## Deploying etcd from Scratch

When setting up your cluster manually, you'll need to download the etcd binaries, install them, and configure etcd as a service on your master node. Manual deployment gives you more control over configuration options, particularly for setting up TLS certificates.

Below is an example of how you might download the etcd binaries and configure the etcd service:

```bash theme={null}
wget -q --https-only \
"https://github.com/coreos/etcd/releases/download/v3.3.9/etcd-v3.3.9-linux-amd64.tar.gz"

# Example etcd service configuration
ExecStart=/usr/local/bin/etcd \
  --name ${ETCD_NAME} \
  --cert-file=/etc/etcd/kubernetes.pem \
  --key-file=/etc/etcd/kubernetes-key.pem \
  --peer-cert-file=/etc/etcd/kubernetes.pem \
  --peer-key-file=/etc/etcd/kubernetes-key.pem \
  --trusted-ca-file=/etc/etcd/ca.pem \
  --peer-trusted-ca-file=/etc/etcd/ca.pem \
  --peer-client-cert-auth \
  --client-cert-auth \
  --initial-advertise-peer-urls https://${INTERNAL_IP}:2380 \
  --listen-peer-urls https://${INTERNAL_IP}:2380 \
  --listen-client-urls https://${INTERNAL_IP}:2379,https://127.0.0.1:2379 \
  --advertise-client-urls https://${INTERNAL_IP}:2379 \
  --initial-cluster-token etcd-cluster-0 \
  --initial-cluster controller-0=https://${CONTROLLER0_IP}:2380,controller-1=https://${CONTROLLER1_IP}:2380 \
  --initial-cluster-state new \
  --data-dir=/var/lib/etcd
```

<Callout icon="lightbulb" color="#1CB2FE">
  For detailed information on configuring TLS certificates, refer to the Kubernetes documentation on [TLS Configuration](https://kubernetes.io/docs/concepts/cluster-administration/transport-layer-security/). Adjust certificate parameters according to your security requirements.
</Callout>

***

## High Availability Considerations

In a production Kubernetes environment, high availability (HA) is paramount. By running multiple master nodes with corresponding etcd instances, you ensure that your cluster remains resilient even if one node fails.

To enable HA, each etcd instance must know about its peers. This is achieved by configuring the `--initial-cluster` parameter with the details of each member in the cluster. For example:

```bash theme={null}
ExecStart=/usr/local/bin/etcd \
  --name ${ETCD_NAME} \
  --cert-file=/etc/etcd/kubernetes.pem \
  --key-file=/etc/etcd/kubernetes-key.pem \
  --peer-cert-file=/etc/etcd/kubernetes.pem \
  --peer-key-file=/etc/etcd/kubernetes-key.pem \
  --trusted-ca-file=/etc/etcd/ca.pem \
  --peer-trusted-ca-file=/etc/etcd/ca.pem \
  --peer-client-cert-auth \
  --client-cert-auth \
  --initial-advertise-peer-urls=https://${INTERNAL_IP}:2380 \
  --listen-peer-urls=https://${INTERNAL_IP}:2380 \
  --advertise-client-urls=https://${INTERNAL_IP}:2379 \
  --initial-cluster-token=etcd-cluster-0 \
  --initial-cluster controller-0=https://${CONTROLLER0_IP}:2380,controller-1=https://${CONTROLLER1_IP}:2380 \
  --initial-cluster-state=new \
  --data-dir=/var/lib/etcd
```

<Callout icon="lightbulb" color="#1CB2FE">
  In some deployments, you may use separate certificate files for peer communications (e.g., `/etc/etcd/peer.pem` and `/etc/etcd/peer-key.pem`). Always tailor these settings to match your desired security posture.
</Callout>

***

## Deploying etcd with kubeadm

For many test environments and streamlined deployments, kubeadm automatically configures etcd. When you use kubeadm, the etcd server runs as a pod within the kube-system namespace, abstracting away the manual setup details.

To view all the pods running in the kube-system namespace, including etcd, run:

```bash theme={null}
kubectl get pods -n kube-system
```

Example output:

```text theme={null}
NAMESPACE     NAME                                 READY   STATUS      RESTARTS   AGE
kube-system   coredns-78fcdf6894-prwl              1/1     Running     0          1h
kube-system   coredns-78fcdf6894-vqd9w             1/1     Running     0          1h
kube-system   etcd-master                          1/1     Running     0          1h
kube-system   kube-apiserver-master                1/1     Running     0          1h
kube-system   kube-controller-manager-master       1/1     Running     0          1h
kube-system   kube-proxy-f6k26                     1/1     Running     0          1h
kube-system   kube-proxy-hnzw                      1/1     Running     0          1h
kube-system   kube-scheduler-master                1/1     Running     0          1h
kube-system   weave-net-924k8                      2/2     Running     1          1h
kube-system   weave-net-hzfcz                      2/2     Running     1          1h
```

To examine the keys stored in etcd (organized under the registry directory), use the following command:

```bash theme={null}
kubectl exec etcd-master -n kube-system -- etcdctl get / --prefix --keys-only
```

Sample output:

```text theme={null}
/registry/apiregistration.k8s.io/apiservices/v1
/registry/apiregistration.k8s.io/apiservices/v1.apps
/registry/apiregistration.k8s.io/apiservices/v1.authentication.k8s.io
/registry/apiregistration.k8s.io/apiservices/v1.authorization.k8s.io
/registry/apiregistration.k8s.io/apiservices/v1.autoscaling
/registry/apiregistration.k8s.io/apiservices/v1.batch
/registry/apiregistration.k8s.io/apiservices/v1.networking.k8s.io
/registry/apiregistration.k8s.io/apiservices/v1.rbac.authorization.k8s.io
/registry/apiregistration.k8s.io/apiservices/v1beta1.admissionregistration.k8s.io
```

The etcd root directory, organized as the registry, contains subdirectories for various Kubernetes components such as nodes, pods, ReplicaSets, and Deployments.

***

## Conclusion

In this article, we examined etcd’s essential role in Kubernetes by exploring both manual deployment and automated configuration with kubeadm. We also discussed best practices for configuring high availability in multi-master environments. As you advance, further exploration into HA configurations and enhanced security measures will help you operate a robust and resilient Kubernetes cluster.

For more in-depth resources, check out:

* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Kubernetes Basics](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
* [Docker Hub](https://hub.docker.com/)
* [Terraform Registry](https://registry.terraform.io/)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/c6d2ac7d-8192-4cff-aa54-e36d888c5bd9/lesson/a3ab7ad6-62ac-4205-86a5-e977443679e8" />
</CardGroup>
