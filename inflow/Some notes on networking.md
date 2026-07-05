controlplane ~ ➜  netstat -plnt

Active Internet connections (only servers)

Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    

tcp        0      0 10.244.105.135:2379     0.0.0.0:*               LISTEN      3214/etcd           

tcp        0      0 10.244.105.135:2380     0.0.0.0:*               LISTEN      3214/etcd           

tcp        0      0 127.0.0.1:2379          0.0.0.0:*               LISTEN      3214/etcd           

tcp        0      0 127.0.0.1:2381          0.0.0.0:*               LISTEN      3214/etcd   

  

Tell me what are thses listening ports for the etcd 

In Kubernetes architecture, `etcd` is the brain of the cluster—it is the highly available key-value store that holds all cluster data and state. Because it has different types of jobs to do, it splits its traffic across distinct ports.

Here is exactly what each of those listening ports is doing:

### 1. Port `2379`: Client Communication (The Front Door)

- **What it does:** This is the primary port used by "clients" to read and write data to the `etcd` database.
    
- **Who connects to it:** In a Kubernetes cluster, the **`kube-apiserver`** is the main client. Every time you run a `kubectl` command to create a pod or read a secret, the API server processes that request and talks to `etcd` over port `2379` to save or retrieve the data. Administrators also use this port when running `etcdctl` commands locally.
    
- **Why two IPs?** You see it listening on both `127.0.0.1` (localhost) and `10.244.105.135` (the Pod/Node IP). This allows local services on the control plane to connect securely via localhost, while also allowing the API server (or other components) to route to it via the network if needed.
    

### 2. Port `2380`: Peer Communication (The Back Channel)

- **What it does:** This port is strictly for **server-to-server** communication between different `etcd` nodes.
    
- **Who connects to it:** Other `etcd` instances in the cluster. If you have a Highly Available (HA) control plane with three master nodes, the three `etcd` databases constantly talk to each other over port `2380`. They use this channel to replicate data, elect a leader, and maintain synchronization using the Raft consensus algorithm.
    
- _Notice it only binds to the routable IP (`10.244.105.135`), because peer nodes need to reach it across the network._
    

### 3. Port `2381`: Metrics & Health (The Dashboard)

- **What it does:** This is a dedicated port for exposing internal metrics and health check endpoints via HTTP.
    
- **Who connects to it:** Monitoring systems like **Prometheus**, or the local `kubelet` performing liveness probes. By isolating metrics to port `2381`, `etcd` ensures that heavy monitoring scrapes do not interfere with the performance or security of the primary client API on `2379`.
    
- _Notice it only binds to `127.0.0.1`. By default, Kubernetes often restricts metrics scraping to local components for security._
    

Interact with etcd

Yes

netstat -pant | grep etcd

tcp        0      0 10.244.105.135:2379     0.0.0.0:*               LISTEN      3214/etcd           

tcp        0      0 10.244.105.135:2380     0.0.0.0:*               LISTEN      3214/etcd           

tcp        0      0 127.0.0.1:2379          0.0.0.0:*               LISTEN      3214/etcd           

tcp        0      0 127.0.0.1:2381          0.0.0.0:*               LISTEN      3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38656         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38708         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38780         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38766         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39048         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38794         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38438         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39248         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38274         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39276         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39324         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39144         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38624         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39394         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38728         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39252         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38612         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39388         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38996         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38406         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38880         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39376         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38260         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39296         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38938         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38744         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39330         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38276         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39176         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39058         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38392         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39194         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39210         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38834         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38336         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38918         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38300         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38580         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38896         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38862         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38808         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38534         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38638         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39012         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38446         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39346         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38490         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39184         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38680         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38530         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38970         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38466         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39006         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39370         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39124         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38872         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38378         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39090         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39098         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39282         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:38922         ESTABLISHED 3214/etcd           

tcp        0      0 127.0.0.1:2379          127.0.0.1:39084         ESTABLISHED 3214/etcd     

  

  

Why would there all this conenction to the 2379 if only the api-server connects to the etcd ? 

You are absolutely right that the `kube-apiserver` is the only component in the cluster that talks directly to `etcd`.

What you are looking at isn't dozens of different components connecting; it is **the `kube-apiserver` opening dozens of simultaneous connections** to `etcd`.

Here is exactly why the API server needs so many open pipes at once:

### 1. The "Watch" Mechanism (Persistent Streams)

Kubernetes operates on a declarative loop. Every controller (like the Deployment controller or ReplicaSet controller), every `kubelet` on every node, and the `kube-scheduler` are constantly asking the API server: _"Tell me the moment something changes."_

Instead of polling the database constantly, the API server translates these requests into persistent **gRPC streams** (Watches) against `etcd`. Because a cluster can have hundreds of active watches running simultaneously to track pod statuses, config maps, and secrets, the API server holds many TCP connections open to `etcd` to multiplex all this streaming data efficiently.

### 2. Connection Pooling for High Throughput

The API server is the central nervous system of Kubernetes. It processes thousands of read and write requests per second. If it tried to shove all that traffic through a single TCP connection, it would bottleneck immediately.

To handle the massive concurrency, the API server uses **connection pooling**. It opens a large batch of connections (the high-numbered ports in your output like `38656`, `38708`, etc.) and keeps them in an `ESTABLISHED` state so it can quickly route traffic across them without the latency of opening a new TCP handshake for every request.

### 3. Localhost Architecture

Because this is a control plane node, both `etcd` and the `kube-apiserver` are running as static pods on this exact same machine. They communicate over the local loopback interface (`127.0.0.1`).

### How to Prove It Yourself

You don't have to take my word for it. You can prove that the API server is on the other end of those high-numbered ports.

Pick one of the high ports from your list (for example, `38656`) and run this:

Bash

```
netstat -pant | grep 38656
```

You will see a matching output line showing the `kube-apiserver` process ID holding the other side of that exact connection!