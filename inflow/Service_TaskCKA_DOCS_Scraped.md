# Consolidated Service TaskCKA DOCS.md

This file is automatically scraped and consolidated by the batch ingestion pipeline.



# Source: https://kubernetes.io/docs/tutorials/services/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Tutorials](https://kubernetes.io/docs/tutorials/)
3. Services

# Services

##### [Connecting Applications with Services](https://kubernetes.io/docs/tutorials/services/connect-applications-service/)

##### [Using Source IP](https://kubernetes.io/docs/tutorials/services/source-ip/)

##### [Explore Termination Behavior for Pods And Their Endpoints](https://kubernetes.io/docs/tutorials/services/pods-and-endpoint-termination-flow/)

---



# Source: https://kubernetes.io/docs/tutorials/services/connect-applications-service/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Tutorials](https://kubernetes.io/docs/tutorials/)
3. [Services](https://kubernetes.io/docs/tutorials/services/)
4. Connecting Applications with Services

# Connecting Applications with Services

## The Kubernetes model for connecting containers[](https://kubernetes.io/docs/tutorials/services/connect-applications-service/#the-kubernetes-model-for-connecting-containers)

Now that you have a continuously running, replicated application you can expose it on a network.

Kubernetes assumes that pods can communicate with other pods, regardless of which host they land on. Kubernetes gives every pod its own cluster-private IP address, so you do not need to explicitly create links between pods or map container ports to host ports. This means that containers within a Pod can all reach each other's ports on localhost, and all pods in a cluster can see each other without NAT. The rest of this document elaborates on how you can run reliable services on such a networking model.

This tutorial uses a simple nginx web server to demonstrate the concept.

## Exposing pods to the cluster[](https://kubernetes.io/docs/tutorials/services/connect-applications-service/#exposing-pods-to-the-cluster)

We did this in a previous example, but let's do it once again and focus on the networking perspective. Create an nginx Pod, and note that it has a container port specification:[`service/networking/run-my-nginx.yaml` ](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/service/networking/run-my-nginx.yaml)

![Diagram](https://kubernetes.io/images/copycode.svg)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx
spec:
  selector:
    matchLabels:
      run: my-nginx
  replicas: 2
  template:
    metadata:
      labels:
        run: my-nginx
    spec:
      containers:
      - name: my-nginx
        image: nginx
        ports:
        - containerPort: 80
```

---



# Source: https://kubernetes.io/docs/tutorials/services/source-ip/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Tutorials](https://kubernetes.io/docs/tutorials/)
3. [Services](https://kubernetes.io/docs/tutorials/services/)
4. Using Source IP

# Using Source IP

Applications running in a Kubernetes cluster find and communicate with each other, and the outside world, through the Service abstraction. This document explains what happens to the source IP of packets sent to different types of Services, and how you can toggle this behavior according to your needs.

## Before you begin[](https://kubernetes.io/docs/tutorials/services/source-ip/#before-you-begin)

### Terminology[](https://kubernetes.io/docs/tutorials/services/source-ip/#terminology)

This document makes use of the following terms:[NAT](https://en.wikipedia.org/wiki/Network_address_translation)Network address translation[Source NAT](https://en.wikipedia.org/wiki/Network_address_translation#SNAT)Replacing the source IP on a packet; in this page, that usually means replacing with the IP address of a node.[Destination NAT](https://en.wikipedia.org/wiki/Network_address_translation#DNAT)Replacing the destination IP on a packet; in this page, that usually means replacing with the IP address of a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/)[VIP](https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies)A virtual IP address, such as the one assigned to every [Service](https://kubernetes.io/docs/concepts/services-networking/service/) in Kubernetes[kube-proxy](https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies)A network daemon that orchestrates Service VIP management on every node

### Prerequisites[](https://kubernetes.io/docs/tutorials/services/source-ip/#prerequisites)

You need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a cluster, you can create one by using [minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/) or you can use one of these Kubernetes playgrounds:
* [iximiuz Labs](https://labs.iximiuz.com/playgrounds?category=kubernetes&filter=all)
* [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
* [KodeKloud](https://kodekloud.com/public-playgrounds)

The examples use a small nginx webserver that echoes back the source IP of requests it receives through an HTTP header. You can create it as follows:

#### Note:The image in the following command only runs on AMD64 architectures.
```yaml
kubectl create deployment source-ip-app --image=registry.k8s.io/echoserver:1.10
```

The output is:
```yaml
deployment.apps/source-ip-app created
```

## Objectives[](https://kubernetes.io/docs/tutorials/services/source-ip/#objectives)
* Expose a simple application through various types of Services
* Understand how each Service type handles source IP NAT
* Understand the tradeoffs involved in preserving source IP

## Source IP for Services with `Type=ClusterIP`[](https://kubernetes.io/docs/tutorials/services/source-ip/#source-ip-for-services-with-type-clusterip)

Packets sent to ClusterIP from within the cluster are never source NAT'd if you're running kube-proxy in [iptables mode](https://kubernetes.io/docs/reference/networking/virtual-ips/#proxy-mode-iptables), (the default). You can query the kube-proxy mode by fetching `http://localhost:10249/proxyMode` on the node where kube-proxy is running.
```yaml
kubectl get nodes
```

---



# Source: https://kubernetes.io/docs/tutorials/services/pods-and-endpoint-termination-flow/

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Tutorials](https://kubernetes.io/docs/tutorials/)
3. [Services](https://kubernetes.io/docs/tutorials/services/)
4. Explore Termination Behavior for Pods And Their Endpoints

# Explore Termination Behavior for Pods And Their Endpoints

Once you connected your Application with Service following steps like those outlined in [Connecting Applications with Services](https://kubernetes.io/docs/tutorials/services/connect-applications-service/), you have a continuously running, replicated application, that is exposed on a network. This tutorial helps you look at the termination flow for Pods and to explore ways to implement graceful connection draining.

## Termination process for Pods and their endpoints[](https://kubernetes.io/docs/tutorials/services/pods-and-endpoint-termination-flow/#termination-process-for-pods-and-their-endpoints)

There are often cases when you need to terminate a Pod - be it to upgrade or scale down. In order to improve application availability, it may be important to implement a proper active connections draining.

This tutorial explains the flow of Pod termination in connection with the corresponding endpoint state and removal by using a simple nginx web server to demonstrate the concept.

## Example flow with endpoint termination[](https://kubernetes.io/docs/tutorials/services/pods-and-endpoint-termination-flow/#example-flow-with-endpoint-termination)

The following is the example flow described in the [Termination of Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination) document.

Let's say you have a Deployment containing a single `nginx` replica (say just for the sake of demonstration purposes) and a Service:[`service/pod-with-graceful-termination.yaml` ](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/service/pod-with-graceful-termination.yaml)

![Diagram](https://kubernetes.io/images/copycode.svg)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      terminationGracePeriodSeconds: 120 # extra long grace period
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
        lifecycle:
          preStop:
            exec:
              # Real life termination may take any time up to terminationGracePeriodSeconds.
              # In this example - just hang around for at least the duration of terminationGracePeriodSeconds,
              # at 120 seconds container will be forcibly terminated.
              # Note, all this time nginx will keep processing requests.
              command: [
                "/bin/sh", "-c", "sleep 180"
              ]
```

---
