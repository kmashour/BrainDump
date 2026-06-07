---
title: "Kubernetes Course – Certified Kubernetes Administrator Exam Preparation (2026 Update)"
source: "https://www.youtube.com/watch?v=l57xKN6OBhY"
author:
  - "[[freeCodeCamp.org]]"
published: 2026-02-10
created: 2026-06-07
description: "Learn Kubernetes and prepare to pass the Certified Kubernetes Administrator (CKA) examination. This course is designed to provide a deep, practical understan..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=l57xKN6OBhY)

## Transcript

### Introduction

**0:00** · Welcome to this comprehensive Kubernetes course. This course is perfect for anyone who wants to learn about Kubernetes, but it's specifically designed for those preparing for the certified Kubernetes administrator exam.

**0:13** · My name is Bo KS and I'm teaching this course. As of the latest 2026 update, this course fully aligns with Kubernetes version 1.34 and the refined exam environment. This course provides a deep practical understanding of Kubernetes administration from foundational concepts to advanced troubleshooting.

**0:33** · I'll give detailed explanations and hands-on demonstrations for every topic in the official CKA curriculum.

**0:41** · Kubernetes is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications. In modern software development, applications are often packaged into lightweight portable units called containers. While running a single container is straightforward, managing hundreds or thousands of them across a fleet of machines presents significant challenges.

**1:08** · Kubernetes addresses these challenges by providing a robust framework for running distributed systems resiliently. The core benefits of Kubernetes include self-healing, which automatically restarts failed containers and reschedules them on healthy nodes, automatic scaling, allowing applications to scale based on resource usage, and zero downtime deployments, which are essential for rolling out updates without interrupting service.

**1:38** · Mastery of Kubernetes is a critical skill for DevOps engineers, cloud administrators, and software developers today. The Certified Kubernetes Administrator or CKA program was created by the CloudNative Computing Foundation and the Linux Foundation to validate the skills required to perform the responsibilities of a Kubernetes administrator. And the Linux Foundation provide a grant to make this course possible.

**2:05** · And on the Linux Foundation website, you can use code free code camp to get 30% off training certificates and bundles. You can check that in the video's description. The CKA exam is a rigorous online proctored performance-based test that requires solving multiple hands-on tasks from a command line interface within a 2-hour time limit. Note that as of late 2025, the exam is strictly administered via a remote YUbuntu desktop.

**2:34** · This means you must be comfortable with node hopping via SSH and using the integrated terminal specific copy paste shortcuts.

**2:45** · The curriculum weights remain focused on practical skills as of the latest curriculum update. These are troubleshooting at 30%.

**2:54** · Cluster architecture installation and configuration at 25%, services and networking at 20%, workloads and scheduling at 15%.

**3:06** · And storage at 10%. The significant weight given to troubleshooting and cluster installation underscores the exam's focus on practical realorld administration skills. During the exam, candidates have access to the official Kubernetes documentation, making it a test of knowledge, application, and problem solving speed rather than wrote memorization.

**3:30** · The fundamental principle underpinning Kubernetes is its declarative model.

**3:36** · Instead of issuing a series of imperative commands like run this container or stop that one, an administrator defines the desired state of the system in YAML manifest files.

**3:47** · These files describe what applications should be running, how many replicas they should have, what network policies should be enforced, and so on. Once these manifests are applied to the cluster, Kubernetes controllers work continuously in a control loop to observe the actual state of the cluster and make changes to reconcile it with the desired state. If a pod crashes, a controller notices the discrepancy between the desired replica count and the actual count and creates a new one.

**4:18** · This model is the foundation of Kubernetes self-healing and automation capabilities. A successful CKA must think declaratively and be proficient in reading, writing, and modifying these YAML manifests.

**4:34** · Here's some essential exam day tips.

**4:36** · Since you are working inside a browserbased remote desktop, standard OS shortcuts often don't work. So copy paste. Use control shift C to copy and control shiftV to paste within the Linux terminal. Avoid control W. This will close your browser tab instead of deleting a word in the terminal. Use Ctrl Alt backspace or just get comfortable with AltB or Alt F to move the cursor. The SSH node hopping rule.

**5:04** · In version 1.34 exams, you will almost never stay on the base node. Most tasks require you to SSH into a specific worker or control plane node. Always check your prompt before running a command. Verify which node you're on and elevate immediately. Many tasks require root access. Use pseudo- i once you've logged into a node to avoid permission denied errors while editing system files like the cube api server.yaml. Optimize the browser.

**5:33** · You're permitted one tab for the exam and one tab for official documentation like kubernetes.io/doccks.

**5:41** · Search efficiently. Use the search bar on the official docs site to find YAML templates for gateway API or network policies quickly. Don't over rely on bookmarks. The remote environment may not have your personal bookmarks, so practice navigating the documentation structure manually so you can find what you need in seconds. Fasttrack your YAML. Time is your scarcest resource. So do not write YAML from scratch. Use dry runs.

**6:08** · Always generate your base manifest using this cube controller run command that you can see on the screen right now. Vim essentials ensure you know how to set indentation in Vim RC. Quickly set tab soft equals 2, shift width equals 2, expand tab.

### Kubernetes Fundamentals and Lab

**6:28** · Before diving into advanced administrative tasks, a solid understanding of the Kubernetes architecture and its core components is important. This section covers the conceptual framework of a Kubernetes cluster and provides a step-by-step guide to setting up a local practice environment that mirrors the tools and configurations you will encounter in the CKA exam. A Kubernetes cluster follows a master slave or more accurately a control plane worker node architecture.

**6:59** · The control plane acts as the brain making global decisions and managing the cluster state while the worker nodes are the muscle running the actual application workloads. The control plane is the set of components responsible for container orchestration and maintaining the desired state of the cluster. It can run on a single machine or be replicated across multiple machines for high availability.

**7:26** · The cube API server is the central hub and the front end of the control plane. All communication to and from the cluster goes through the API server. It exposes a Kubernetes API, validates and processes all API requests and coordinates all processes between control plane and worker node components. ETCD is the cluster single source of truth.

**7:50** · It's a consistent and highly available distributed key value store where all cluster data its configuration state and metadata is stored for security and consistency.

**8:02** · Direct access to ECTD is restricted. All interactions must go through the cube API server. The cubeuler acts as the cluster's matchmaker. It watches for newly created pods that do not yet have a node assigned. For every such pod, theuler finds the best node for it to run on based on a complex set of factors including resource requirements, hardware constraints, affinity and anti-affffinity rules, and data locality. The cube controller manager is the autopilot of the cluster.

**8:32** · It runs various controller processes in the background. Each controller is a control loop that watches the shared state of the cluster through the cube API server and works to move the current state towards the desired state. Examples include the node controller which handles node failures and the replication controller which maintains the correct number of pods. Worker nodes are the machines where your applications run.

**8:59** · They are managed by the control plane and contain all the necessary services to run containers. The cublet is the primary node agent that runs on each worker node. It communicates with the cube API server to receive instructions and report the status of the node and its containers. Its main job is to ensure that the containers described in pod specifications are running and healthy. It manages the entire life cycle of the containers on its node.

**9:29** · Cube proxy is a network proxy that runs on each node and is a fundamental part of the Kubernetes service concept. It maintains network rules on the node which allow for network communication to your pods from both inside and outside the cluster. It can use various modes to direct traffic destined for a services virtual IP to the correct backend pod. Finally, the container runtime is the software responsible for running the containers.

**9:59** · Kubernetes supports several container runtimes such as containered and CRIO.

**10:05** · The cublet communicates with the container runtime using the container runtime interface or CRI. To manage container operations like pulling images and starting and stopping containers, Kubernetes objects are persistent entities in the Kubernetes system. By creating an object, you are telling the Kubernetes system what you want your cluster's workload to look like. This is your your cluster's desired state. Pods are the smallest and most fundamental deployable unit in Kubernetes.

**10:35** · They represent a single instance of a running process in your cluster. A pod encapsulates one or more tightly coupled containers which share storage resources, a unique network IP, and options that govern how the container should run. While a pod can contain multiple containers, the most common pattern is one container per pod.

**10:59** · Replica sets and deployments. A replica sets purpose is to maintain a stable set of replica pods running at any given time. It guarantees the availability of a spec of specified number of identical pods. A deployment is a high a higher level object that manages replica sets and provides declarative updates to pods. You describe a desired state in a deployment and the deployment controller changes the actual state to the desired state at a controlled rate.

**11:27** · Deployments are the standard and recommended way to manage stateless applications in Kubernetes services. Since pods are ephemeral and their IP addresses can change, a service provides a stable endpoint to access a logical set of pods. A service acts as an abstraction defining a policy by which to access the pods and provides a stable virtual IP address or the cluster IP and a DNS name.

**11:55** · Any traffic sent to the service is automatically load balanced to the appropriate backend pods. Name spaces provide a mechanism for isolating groups of resources within a single cluster.

**12:07** · They are a way to divide cluster resources between multiple users or teams. The names of resources need to be unique within a namespace but not across name spaces. This allows different teams to use the same resource names without conflict. The CKA exam is entirely hands-on, making practical experience the most important component of preparation. This section details how to create a local Kubernetes cluster using Cube ADM, the same tool used to bootstrap production clusters.

**12:37** · This approach provides deep insight into the cluster's inner workings, which is invaluable for both the exam and real world administration.

**12:48** · Managed Kubernetes services like GKE or EKS abstract away many of these foundational layers, but the CKA certification validates your ability to build and maintain a cluster from the ground up on generic Linux machines.

**13:03** · Understanding why each setup step is necessary is as important as knowing the commands themselves. Before installing Kubernetes, each machine or VM intended to be a node in the cluster must meet certain requirements. A compatible Linux host, for example, Ubuntu 22.04 or CentOS 7, at least 2 GB of RAM per machine, at least at least two CPUs for the control plane node, and full network connectivity between all machines.

**13:31** · So, our first step is to install a container runtime. Kubernetes requires a container runtime on each node to manage containers. While Docker was historically popular, the CKA exam environment and modern clusters typically use runtimes that directly implement the CRI, such as containered or CIO. We'll install containered.

**13:55** · So, these commands I'm about to show you must be run on all nodes uh control plane and workers. So first we're going to load required kernel modules.

**14:09** · Kubernetes networking required relies on the kernel's ability to see bridge traffic. So we have cat eo f pseudo t etc modules-load.dks.com overlay brnet filter and eof. So these commands basically serve two main purposes persistence and immediate activis activation.

**14:33** · So first we create a new configuration file. That's this right here. And the content of the file simply lists the two modules the overlay and BR net filter.

**14:45** · So these files in the this uh directory are read by the system during boot. Any module listed in these files will be automatically loaded into the kernel every time the system starts. And here's the activation. And we're going to use pseudo mod pro overlay and then pseudo probr net filter to activate those right now. Then we don't have to reboot anything. So Kubernetes components can start immediately and find the networking features they need. And just so you kind of understand them o overlay.

**15:15** · This is the preferred storage driver used by modern container runtimes like containered to build and manage container images. Overlay FS allows a container to use a readonly base image layer and a writable layer on top making container startup fast and efficient in terms of disk space. And then the BR net filter, it's a module that enables the kernel to correctly process network packets coming from aworked bridge.

**15:47** · Okay. Next, we'll configure CIS control for networking. These next settings ensure that IP tables correctly processes processes bridge traffic which is important for cube proxy and the CNI plugin. So just like before we're creating this configuration file and we are putting these custom kernel settings.

**16:12** · So basically these will be configured every time we start the system and then we'll just do this pseudo ciscontrol-system to immediately activate the commands. So and like I said these are these parameters are critical for how Kubernetes internal networking managed by qoxy and the CNI plugin handles data packets. Now we can finally install containered.

**16:42** · So first we'll update pseudo app to do pseudoapp get update and then we just do pseudoapp get installed containered. Okay. And let me clear that out again. So now we're going to configure containered. We'll generate the default configuration file and modify it to use the system croup driver. The cublet and the container runtime must use the same croup driver to properly manage resource limits.

**17:11** · Mismatches here are a common source of cluster instability.

**17:15** · So first we will make a directory and then we have pseudo containered config default pipe pseudo tetcontainered config.tml tl and this and then this line at the bottom pseudo set- i s/system cgroup equals false system croup equals true and we have etc/ontainer config tunnels. So basically finishing updating the configuration like I was saying before and then we'll clear out the screen.

**17:46** · Now we just have to restart and enable containered. So pseudo system controller restart containered and then pseudo systemcontrollered enable containered. Okay. Next we're going to install the kubernetes binaries. We'll install cube adm cublet and cube controller on all nodes. These are basically essential kubernetes tools and ensure the operating system is configured and correctly for stable operation. So let's disable swap.

**18:17** · The cublet requires swap to be disabled to ensure predictable resource management and performance. So pseudo swap off- a and this line is basically to make this persistent across reboots. We comment out the swap line in slash ect stab. Okay. Now let's add the kubernetes apt repository. pseudoepkin install a transport https certificates curl gpg.

**18:55** · Now this directory we just have to make if it doesn't already exist to prepare for our next command. And this is going to download the kubernetes signin key and registers it with a. So we're adding this so appget knows where to look for cube cube adm and cube controller. And we'll do pseudo appgget update to make sure we update the package lists.

**19:22** · Now we'll do pseudo app get install cubelet cubeadm and cube controller. What we'll need for this tutorial. And which service should be restarted? We'll just do none for now. And then we'll do this a mark hold which is going to prevent accidental upgrades which is important an important practice for maintaining a stable cluster vision cluster version.

**19:49** · Okay. Next we're going to configure a single node cluster. So for initial practice a single node cluster is sufficient. This involves initializing the machine as a control plane and then removing a taint that prevents user workloads from running on it. So we have this command pseudo cubadm in it pod network cider and then 10.244.0.016.

**20:16** · The pod network cider flag specifies the AP address range for the pod network.

**20:23** · This is required by most CNI plugins. So next we are going to configure cube controller. So we'll first make the directory. Then we copy the cluster administrator configuration file created by cube adm to the standard location.

**20:41** · And then this uh next command changes the file ownership so the current nonroot user can securely interact with the cluster using the cube controller tool. So the result the user can now run cubecontroller commands to manage the cluster without needing pseudo. Okay.

**21:00** · Now I've just run this command to remove the control plane taint. By default the control plane node is tainted uh to prevent regular application pods from running scheduled from being scheduled on it. But for a single node cluster the taint must be removed. And now it is.

**21:19** · And now for this next command we're going to install a CNI plugin. The cluster is not fully functional until a container network interface or CNI plugin is installed. Without it, pods cannot communicate with each other and core DNS will not start correctly. We'll use flannel for this single node setup.

**21:38** · And now we can verify the cluster. We can check that the node is in the ready state and that all system pods in the cube system namespace are running. So I'll do cubec controller get nodes and we can see that one's ready and then cube controller get pods in cube systems and we can see the pods are running.

**22:00** · Okay, we now have a functional single node Kubernetes cluster ready for the other things we'll be doing with Kubernetes in this course.

### Cluster Architecture, Installation & Configuration

**22:12** · This section covers the core competencies of a Kubernetes administrator.

**22:17** · Building, managing, and securing a multi-node cluster. The tasks detailed here are fundamental to the CKA exam and represent a significant portion of its total score. We'll expand upon the single node setup to construct a production style multi-node cluster, manage its life cycle through upgrades and backups, implement high availability, and configure access control and application management tooling. Building a multi-node cluster involves a coordinated setup process across all machines.

**22:49** · The following steps assume you have at least two nodes, one designated as the control plane and one as a worker. The prerequisite steps from part one must be completed on every node that will be part of the cluster. This includes ensuring unique host names, MAC addresses, and product UU IDs. disabling

**23:13** · swap memory, configuring required kernel modules and CIS control settings, installing a container runtime and ensuring its croup driver is set to systemd and finally installing the Kubernetes binaries cubeadm cublet and cube control and placing them on hold.

**23:30** · The following steps I'm going to go over assumes that you have two machines running or two virtual machines. So, one should be designated the control plane.

**23:40** · That's this one right here. And the other is uh designated a worker. So the one with the white background is the worker.

**23:49** · Now I have two VMs running on my Mac OS using UTM. Now you can follow along in other ways as well, but there were some extra settings I had to do to make sure that they each have a different IP address. when I did not have the VMs running, there were some settings in UTM and just in case you're going to use UTM or something like that. Um, so this is UTM. And to make sure they do not have the same IP address, I had to um stop the VMs.

**24:20** · I'm not going to do that right now, but you can go into edit and then you can go into network preferences and then you can uh change the MAC address of one of them. They have to have different MAC addresses. And then also I have to change the network mode to bridged. So basically I had to go to the settings the network tab and then change the network mode from shared network to bridged. And then I had to restart the virtual machines.

**24:48** · And so the prerequisite steps that we already showed where we installed everything must be completed on every machine that will be part of the cluster. So I've already configured both these machines.

**25:04** · the control plane and the worker the in the same way as I saw as we saw the setup earlier. So now let's continue setting up the control plane Linux or the virtual machine. This one is the one that's going to manage the cluster.

**25:22** · So let's start by removing the old cluster configuration.

**25:28** · We're going to tear down the existing CL cluster that we made before because we are going to now create it within a using a slightly different method.

**25:38** · Now we have to get the IP address. This is something we didn't do when we created the cluster earlier and then we use the pod network cider. This IP range is required by most network plugins CNIs and for Calico this is the common default and then we need to use the private IP address of this control plane VM. Other nodes will use this address to communicate with it.

**26:07** · So I'm just going to copy the IP address and we'll paste it at the end here. Okay. And that worked. If you get an error, it's possible you need to turn the swap off again with pseudo swap off- a. Now, we did that earlier, but sometimes if you restart your machine or something like that, it may not be off anymore. That's one thing you have to look out for.

**26:35** · Okay. Well, the output of this command is important. It provides a cube adm join command containing a token and a discovery token CA certificate hash.

**26:50** · So we need to copy this entire command and save it. We'll need it to connect the worker node. Next, we're going to install a container network interface or CNI plugin. So we're still on the control plane node, the virtual machine.

**27:08** · So immediately after initialization, our control plane node will have a not ready status because it lacks a network plugin. The cluster will not be functional until a CNI is installed. So let's install Calico. Calico is a popular CNI that provides both networking and network policy enforcement. The CKA exam often involves tasks related to network policies which makes Calico an excellent choice for a practice environment.

**27:39** · So we'll just do cubecontroller apply-f and then we have this URL here for Calico. Okay, so we got that installed and now we just want to verify the CNI installation. After a few moments, the calico pod should be running in the cube system namespace and the control plane node status should change to ready. So we'll just run these two commands.

**28:04** · CubeController get pods-cube system and cubecontroller get nodes and we can see from the output that the pods are running and the status is ready.

**28:19** · Okay, now we need to join the worker node to the cluster. So we need to be on the worker virtual machine. Remember the one with the the white background. So we're on the worker virtual machine and we're going to connect it to the cluster. We're going to run the cube adm join command. So we need to paste in the command or use the same command that we saved from the control plane in initialization step. And this command must be run with root privileges. Okay, we got that working.

**28:48** · So, let's go back to the control plane virtual machine and we're going to verify verify the cluster from the control plane. So, we'll return to the control plane and we just want to make sure everything is successfully joined. So, I'm going to use cubecontroller get nodes- o wide. The o wide flag provides additional information including the internal IP of each node. And now we can see both nodes, the the control plane and then the worker node.

**29:18** · So we now have a fully functional production style multi-node Kubernetes cluster. A key responsibility of a Kubernetes administrator is managing the cluster's life cycle, which includes performing version upgrades and ensuring the cluster's state can be recovered in case of a disaster. Cube ADM provides a structured workflow for upgrading a Kubernetes cluster.

**29:42** · The process must be done carefully upgrading the control plane first followed by the worker nodes one at a time to ensure workload availability. So let's upgrade the control plane. U so we'll run three commands. One to the appmark uphold unhold cube QD cube ADM to up unhold the package. Then we'll install the target version and then we will hold it again.

**30:15** · Now in this case um some of these upgrades could also be downgrades. Um you can use the same process whether you're upgrading or downgrading to another different version. And then we want to check for upgrade compatibility and view the target versions with um plan pseudo cube admgrade plan.

**30:37** · Okay. Now we want to apply the upgrade with cubadm upgrade apply and then the version. This command upgrades the static pod manifest for the control plane components like cube API server etc etc.

**30:52** · Now let's upgrade cublet and cube controller.

**30:56** · So we basically want to upgrade the other binaries on the same node. Again we'll unhold cubelet and cube controller. Then we'll install the new versions.

**31:08** · Then we will hold them again. Hold cublet and cube controller again.

**31:14** · Now we want to restart the cublet. So we just use a pseudo system controller diamond damon reload and pseudo system controller restart cublet.

**31:25** · Now we have to upgrade the worker nodes.

**31:28** · Uh in this case I just have one, but you'll want to repeat this process for each worker node individually. The first step in upgrading the worker nodes is actually on the control plane node. So first we need to safely evict all workloads from the worker node we are about to upgrade. So we're going to run this um the cube controller drain and then we get the node. But we have the node name from up there and ignore Damon sets. Okay.

**31:57** · Now we go over to the worker node and you can either go to it directly like I'm doing or you can SSH into it and we upgrade the binaries just like we did before. So unhold cube adm and cublet. Then we can do appkit update app install and then the the different the updated versions of cube adm and cublet. And then we just have to hold them again. hold cube adm and cublet.

**32:23** · Now we need to upgrade the node configuration with cube adm upgrade node which is a command that updates the local cublet configuration for the worker node and then restart the cublet.

**32:37** · So system control controller damon reload and system controller restart cublet. Then on the control plane virtual machine, we want to mark the worker node as schedulable again allowing the pods to be placed on it with uncordin cube controller uncordin with the node to upgrade.

**33:00** · Now let's talk about backing up and restoring etc.

**33:06** · So on the control plane virtual machine uh since ECCD stores the entire state of the cluster having a reliable backup is very important. These operations use the etc dctl or the etc controller command line tool.

**33:27** · So we need to perform a backup. So on the cubeadm cluster the etc server runs as a static pod. This command here connects it to connects to it using the required TLS certificates to create a snapshot. DB file. If you get any errors, um you do also have to make sure that there's no swap. You may have to run the pseudo swap off- a again to get these commands to work. Okay. Now we can perform a restore.

**33:56** · This is a destructive operation that replaces the cluster state. So, first we stop the cublet to prevent interference with system controller stop cublet. Then we restore the snapshot to a new directory with this command. And then we're going to have to manually edit the etc static pod manifest and then update its volume mount to point to the new data directory.

**34:24** · So um to update it, we'll use uh nano.

**34:28** · So we need to install nano and then we can use nano to edit the the manifest for etc.

**34:40** · And inside editor we need to find the volume definition for the etc data directory. We'll use the arrow keys to scroll down to find the volume section.

**34:49** · uh under the the that volume find the host path key and change its path to varlibetcdrestored.

**34:58** · We need to add dashrestored. So then we just need to save and exit nano control X. The final step is restart the cublet to start the etc pod with the restored data with system controller start cublet. The cublet will detect the change of the manifest and restart the etc pod using the restored data. The rest of the control plane components will then restart and reconcile their state based on the restored etc data.

**35:28** · A single control plane node represents a single point of failure for for production environments. A highly available or HA control plane with multiple replicated control plane nodes is essential. Cube ADM supports two HA topologies stacked control plane and external ETCD. The stack topology where ETCD members are coll-located on the control plane nodes is simpler to set up and common in CKA scenarios.

**35:54** · An HA setup requires a stable endpoint for all nodes to communicate with the API server. This is typically achieved with an external load balancer. First, provision a load balancer that sits in front of your control plane nodes. Then, configure the load balancer to forward TCP traffic on a specific port to the same port on the private IP addresses of all your control plane nodes.

**36:22** · Finally, the load balancer should perform a TCP check health check on port 6443 to ensure it only routes traffic to healthy cube API server instances. Okay, I have an external load balancer running at this IP address, just another one on my local network here. So on the control plane node, we're just going to run this cube ADM init with the control plane endpoint.

**36:48** · And like I said, this is the low paler IP address and the port. And then we' use the update upload search flag which is critical for security for securely sharing the cluster certificates with the other control plane nodes that will join. Now we're only going to be using one control plane for our example. And then we are going to advertise the address of this of this control plane.

**37:14** · Now the IP addresses have changed since the early earlier part of the video.

**37:20** · So now this is going to give us two commands. So this is the command that says you can now join any number of the control plane nodes running the following command. So basically if we had other control plane nodes we'd run this command and for the worker node we can run this command. Okay. Now we'll just run we'll just paste in the command. And this is the standard worker join command that we're going to use to add the worker nodes to the HA cluster.

**37:53** · All now nodes will now point to the load balancer as the API server endpoint.

**38:01** · Role-based access control or RBAC is the primary mechanism for regulating access to resources within a Kubernetes cluster. It determines what you can do after you've proven who you are. A deep understanding of RBAC is essential for securing a cluster. RBAC is built on four key API objects. A role which contains a set of rules that represent permissions. Roles are namespaced, meaning they only grant access to resources within a single namespace.

**38:30** · A cluster role is the same as RO but is non-namespaced.

**38:38** · It can be used to grant permissions to cluster scoped resources or to resources across all namespaces. A role binding grants the permissions defined in a role to a set of users, groups or service accounts. It's also namespaced and connects a subject to a role within that namespace. And finally, a cluster role binding grants the permissions of a cluster role to subjects clusterwide.

**39:06** · Okay, let's talk about granting readonly access. I'm going to demonstrate the standard workflow for creating a dedicated service account for an application and granting it restricted readonly access to pods within a specific name space. We're going to follow the principle of least privilege.

**39:25** · We don't want to give an application full admin rights if it only needs to read some information. That's why we're creating a special identity for an application called a service account and giving it just enough permission to read pods in a specific name space and nothing more. So we are so let's create an isolated workspace for this experiment. A namespace is like a virtual cluster inside your main cluster. Helps keeps things organized and prevents us from accidentally affecting other applications. So cube controller create namespace RBAC test.

**39:56** · So the name space is called RBAC- test. Okay, we're going to create a service account. We need an identity for our application. In Kubernetes, you don't give permissions directly to a pod. Instead, you give them to a service account and then you tell the pod to use that account. Think of it as a user but for a program instead of a person. So let's create a service account named dev user.

**40:23** · So this command right here we're going to use to create a service account called dev user in our new namespace.

**40:36** · So not the default one. Okay. Service account dev user created.

**40:41** · Now step three define the permissions with a role. So for the core of RBAC we need to define a set of permissions. In Kubernetes, a role is an object that contains rules representing a set of permissions within a single namespace.

**40:59** · So we're going to create a YAML file named roll.yaml. So nano roll.yaml and we're going to define a pod reader ro. So I'm going to paste this ro in here. This role will only allow read only actions on our pods. So we have the kind ro metadata we have the namespace the name. So then the rules are is where we define what actions are allowed.

**41:30** · So for the resources pods that means the permissions only apply only to pods not deployments not services just pods. And then we have the verbs get list and watch. These are the allowed actions. So you can get a single pod, list all pods and watch for changes and we're not including create, delete or update. So that's what makes it read only.

**41:55** · So we'll just save this and now I'm going to apply the manifest to the cluster. So cubecontroller apply ro.yml.

**42:11** · And this command takes the blueprint from our YAML file and creates the actual RO object inside our Kubernetes cluster.

**42:21** · Okay, step four is connect the user and the RO with a RO binding. So far we have a user, the dev user and a set of permissions pod reader, but they are not connected. We need to bind them together. A role binding does exactly that. It grants the permissions defined in RO to a user or a set of users. So first we're going to create a file. So um nano rolebinding.yamel and this is where we'll define our our role binding.

**42:52** · So so I'm just going to paste in the text of this here. So let's break this down.

**43:03** · We have our kind is role binding and then we know the what the name space is we're using the name. So subjects this defines who gets permission. So in our case it's the service account named dev user in this namespace. And then we have the role ref. This defines what permissions they get. We're referencing the pod reader role that we just created. So I can save this.

**43:32** · And now I will apply the manifest to make the connection official.

**43:43** · Okay, we got that created.

**43:47** · Now we'll verify the permissions. So this is a pretty important step. Testing our work. Did we configure everything correctly? Kubernetes has a fantastic built-in command to check this. So just paste in the command here. It's the cube controller o can I? And it this is what we use to ask the Kubernetes API server if a user can perform a certain action.

**44:12** · So can I list pods? So that's the action and then the - flag lets us impersonate our service account. So, we put our account name, the dev dev user, right in there. And then we can just run this to see if we can do it. So, it says yes, that's what we wanted. So, now let's test a negative case. Can our dev user delete pods? So, I'm going to paste in another command here.

**44:43** · Can I delete pods as the the user that we just created?

**44:50** · No. Uh we cannot delete pods. And there you have it. The first command returned yes and the second return no which confirms our the RBAC policy is working perfectly. Our dev user account can read pods but cannot perform any destructive actions. This is a fundamental pattern for securing your Kubernetes applications.

**45:16** · While cubecontroller apply-f is fundamental, managing complex applications with many interdependent manifests can become cumbersome. Helm and customize are two popular tools that streamline this process. Helm is the de facto package manager for Kubernetes. It allows you to define, install, and upgrade even the most complex Kubernetes applications as packages called charts.

**45:45** · Charts are a collection of files that describe a related set of Kubernetes resources packaged as a single unit.

**45:53** · Values are part of a values.yaml file which provides the default configuration values that can be overridden at install time. A release is an instance of a chart running in a Kubernetes cluster.

**46:07** · Customize is a template-free tool for customizing Kubernetes manifests. It's built directly into CubeController via the - K flag and works by applying patches and overlays to a common set of base YAML files. This approach avoids the complexity of templating languages.

**46:25** · Okay, let's see this in action. First, let's install Helm, which is the package manager for Kubernetes. We'll install we'll install it using the official installation script, which is the quickest way to get started on a Linux system like our control plane. So this command is going to download the official Helm installation script and then pipe it directly to the bash shell to be executed. This will install the latest version of Helm onto you into user/loc/bin.

**46:55** · Now we can just check to make sure it works with helm version.

**47:00** · Okay, we got this installed. So let's see things everything in action by installing an engineext web server.

**47:08** · First, we need to tell Helm where to find the charts we want to use. So, we have this command here, Helm repo add bit nami. And then we have the URL here.

**47:17** · So, we're adding the popular Bitnami repository which contains hundreds of readytouse charts. And it's been added to our repositories. Now, we can do Helm rep Helm repo update.

**47:33** · And this is going to fetch the latest list of charts from all our added repos.

**47:39** · And then we get this fun message, happy helming. So now that helm knows where to look, we can install our engineext chart. So we have helm install my engineext bitami/engineext set.type equals nodeport.

**47:57** · So this creates a new release. So we have the name for our release that's my engine X is the name that we're giving it and the chart to install here and then the set flag uh will override a default value in the charts configuration to expose EngineX using a nodeport service making it accessible from outside the cluster

**48:24** · and just like that with one command Helm has created deployment a service and another and other resources the engineext chart needed. We do have some warnings, but none of those will make this not work. You can now manage the entire life cycle of this application with commands like helm upgrade, helm roll black, roll back, and helm uninstall. It's very powerful. Now, let's talk about customize template free customization.

**48:51** · So, while Helm uses a templating language, customize takes a different template-free approach. It lets you define a common set of base YAML files and then apply layers of customizations or overlays on top of them. This is perfect for when you have a core application that needs slight modifications for different environments like de development, staging and production. So let's set up a project to see how it works.

**49:22** · Imagine we have a simple engineext application. So first we'll create our base configuration.

**49:28** · This is the standard default version of our app. So first I'm going to make a directory my app/space.

**49:36** · And now and now we'll create our deployment file. You can create the file in any way you want. Previously I use nano. Now we're just using cat. Here you can see this deployment has one replica and we have it we have the labels. We have the the app the name of the app. We have containers engine x and the image we're using. And every customized directory needs a customization.yamel file. That's what we're creating here.

**50:04** · This tells it which resources to manage.

**50:08** · So the resources are just the ones specified in the deployment.yamel file that we just created. Okay. Now that we have our base, we can create an overlay for our production environment. In production, we need higher availability.

**50:27** · So, we want to run three replicas instead of one. So, I'm going to make our the production directory the overlays production directory. And now we're creating a patch.yaml file.

**50:42** · This file contains only the changes we want to make. Customize will strategically merge this into the base deployment. So now we are saying that it's going to be three replicas.

**50:54** · Okay. Now just like before we need to make our customization.yamel file in the production directory and we uh basically this file for overlay points to the base and then lists the patches to apply. So we're just going to apply this patch.yaml YAML file that we made.

**51:17** · So, we're all set. We have our base. We have our production overlay that changes the replica count. Now, to deploy our production configuration, we use the same cube controller apply command. You can see it down at the bottom. And now we but now we have a - K flag that will point to our overlay directory.

**51:42** · So this will read the base apply the production pass patch and then send the final merge configuration to the Kubernetes API server.

**51:53** · And it is notifying that we should not use bases, we should use resources.

**52:01** · But it looks like we can just fix that with customizeedit fix. Oh yeah, we don't have the customize command line tool. So we just have to fix that manually with nano and then the name of our file and then we can change this word bases to resources and then we can just exit out of that. Okay. So now we have that updated.

**52:29** · So now the next time we run the cubernetes cube controller apply we won't see that warning but it's going to work either way. Okay. Now let's see if everything worked. We're going to run cubecontroller getit deployment my app and we can see that it has three it has three replicas or zero out of three replicas uh just as we specified in our production overlay. We've successfully customized our application without ever touching the base files or dealing with complex templates.

**52:58** · It's a very clean and declarative way to manage environment specific configurations.

**53:05** · While they have different philosophies, Helm and Customize can be used together.

**53:13** · A common pattern is to use Helm template to generate the base manifests from a chart and then use customize to apply environment specific patches before applying them to the cluster. And this chart shows the key differences between Helm and Customize.

**53:41** · Kubernetes is designed to be extensible.

**53:44** · Its core functionality can be enhanced through standardized interfaces and by adding custom resource types. The CRI or container runtime interface is a plug-in interface that enables the cublet to use a wide variety of container runtimes without needing to recompile Kubernetes.

**54:04** · The CNI or container network interface is a specification for configuring network interfaces for Linux containers.

**54:12** · It allows different networking solutions to integrate with Kubernetes to provide pod networking. The CSI or container storage interface is a standard for exposing storage systems to containerized workloads. It allows third-party storage vendors to develop plugins that work across different container orchestrators, including Kubernetes, without having to add their code to the core Kubernetes repository.

**54:41** · A custom resource definition or CRD is a powerful feature that allows you to extend the Kubernetes API with your own custom resource types. If you want to manage a new type of object like a database, you can create a CRD for it and then interact interact with it using cube controller just like a built-in resource like a pod. An operator is a custom controller that uses CRDs to manage applications and their components. It follows Kubernetes principles, notably the control loop, to automate complex operational tasks.

**55:12** · For example, a database operator could automate backups, failovers, and upgrades for a database cluster defined by a custom resource.

### Workloads & Scheduling

**55:27** · This part focuses on the core objects used to run applications on Kubernetes.

**55:32** · It covers how to manage application life cycles with deployments, how to inject configuration data, how to automatically scale workloads, and how to control where and how pods are scheduled on the clusters nodes. Deployments are the standard way to run stateless applications. They provide fine grain control over updating and rolling back application versions with zero downtime.

**56:01** · The default update strategy for deployments is rolling update. This strategy ensures that the application remains available during an update by incrementally replacing old pods with new ones. The behavior of a rolling update is controlled by two key parameters in the deployment spec.

**56:21** · Spec.strategy.rollingupdate.mmax unavailable is the maximum number of pods that can be unavailable during the update. Spec.st strategy.rollingupdate Rolling update.mmax surge is the maximum number of new pods that can be created over the desired number of replicas.

**56:41** · A rolling update is Kubernetes elegant solution to the challenge of updating a running application. Instead of taking everything down at once, Kubernetes carefully replaces old pods with new ones one by one, ensuring your application remains available to users throughout the entire process. So let's see this in action. First, we need an application to work with. Now, in a previous section, we created an application, but we're just going to create one again for this section.

**57:08** · We'll create a simple EngineX deployment running an older version of the software.

**57:16** · So I did nano deployment.yamel to create this deployment file. And so this manifest defines deployment named engineext deployment that maintains three replicas of pods. Each pod runs a single container with the engineext image and specifically the 1.24.0 which is an older version. So I'll just save this and then we can deploy it to our cluster with cubecontroller apply-f deployment.yaml.

**57:48** · Okay, we got that deployed. Okay, so now we're going to trigger the rolling update. So we're going to update our application to a newer version of EngineX. The simplest way to trigger a rolling update is to change the container image tag in the deployment spec. We can do this directly from the command line. So I have this command here. QController set image deployment X deployment. That's what we just created up here. And then engineext equals enginex 1.25.0.

**58:21** · Remember it was 1.24.0.

**58:24** · So this basically tells Kubernetes to find the deployment, locate the container name engine X, and update its image to engineext 1.25.0. So we can do this. Okay, image updated. So this is the cool part. Kubernetes is now performing the rolling updates the update in the background. We can watch it happen from two different perspectives. First we can use the rollout status command.

**58:51** · So if I paste this in cubecontroller rollout status and we put the name of the deployment and you can see wait it waiting to finish uh one out of three new replicas have been updated. So this command will block and give you live updates on the rollout process. It's basically a highle overview. Now I'm going to open up a new another terminal tab and I'll zoom in a bit. Here we can watch the individual pods as they replaced.

**59:18** · So we have cubecontroller get pods-l and then this is the label that we're looking for. The pods with that label-w means we're going to get a real time feed. Okay. Okay. And here's what it looks like after they've all been updated. Now they're running again after they're stopped and created and running again.

**59:45** · Kubernetes maintains a revision history for each deployment, allowing you to easily roll back to a previous stable version if an update introduces a bug.

**59:56** · This triggers another rolling update.

**59:58** · This time replacing the new pods with pods running the image from the previous revision. Now let's talk about executing and verifying rollbacks.

**1:00:08** · What if our new version 1.25.0 has a critical bug? One of the most powerful features of deployments is the built-in revision history which acts as a safety net. So let's see the history of changes we've made to our deployment. So put in this command cubecontroller rollout history deployment engineext deployment.

**1:00:27** · Okay, we can see the list of revisions.

**1:00:29** · So revision one was our initial deployment with 1.24.0 and then we have our current update 1.25.0.

**1:00:38** · So let's roll back to the previous version. Let's say the new version is faulty. We can instantly revert to the last known good configuration with a simple undo command. So I'll just undo the deployment. So now if we're going to watch the pods again, we would see the same rolling update process but in reverse. Uh so it it go it terminates the 1.25.0 pods and replace them with the 1.24.0 pods. You can also roll back to a specific version.

**1:01:06** · So if we use this command undo and then two revision equals one. So this is useful if you need to go back more than one step in your deployment history. uh in our case we only have one one or two steps.

**1:01:24** · It's a best practice to decouple application code from configuration.

**1:01:29** · Kubernetes provides two primary resources for this. Config maps for nonsensitive data and secrets for sensitive data. A config map is an API object used to store non-confidential data in key value pairs. Pods can consume config maps as environment variables, command line arguments or as configuration files in a volume. So let's see how to create a config map imperatively. So this line here is going to create a config map named app config with two key value pairs.

**1:02:01** · See app.color is blue and app.m mode is production. So see it says config map created. You can also create a a config map from a files contents. So here we're going to put the retries equals 3 into the file config.properties and then cubecontroller create config map app-config from file config.properties. So we're creating it from that file. You can also create a config map declaratively.

**1:02:31** · So for production it's always better to define resources in YAML files so you can check them into version control. So I'm going to create a file called config map.yaml and then I'll paste in the code here or the YAML and then you can see we have the name and then we have the data. So database URL is the URL ui.the is dark.

**1:02:58** · So these are the settings and now after creating our config.yaml we just have to do qcontroller apply to apply the config map. A secret is an object that stores sensitive information like passwords, API keys, or TLS certificates. The data in a secret is stored in B 64 encoding.

**1:03:17** · It's important to understand that B 64 is an encoding, not an encryption. It provides no real security and can be easily decoded. True security for secrets relies on enabling encryption at rest for ATCD and using RBAC to restrict access to the secrets objects themselves. So let's look at the creation method. So here's how to create a secret imperatively. Kubernetes will automatically base 64 encode the string values here admin and secret the S3C R3T.

**1:03:51** · So they'll be encoded and our secret our db-credentials is created and you can also create with YAML creating a secrets declaratively. So if I create this YAML file I'll paste in some YAML here. Uh so with when using YAML you have a very convenient field called string data.

**1:04:14** · This lets you provide plain text values and Kubernetes will handle the base 64 encoding for you automatically when the secret is created. This is much easier than encoding the values yourself. So if I save this. Okay. Now let's talk about using config maps and secrets in pods.

**1:04:34** · So I've created our configuration objects. So we're now going to use them.

**1:04:39** · So one common method is to expose keys from config maps and secrets as environment variables inside a container. So let's create a pod that does this. So I'm going to create the file pod config.yaml. So we're creating a pod just like we've shown before and we can inject a values from the config map. So value from config map keyref. So this is the config map's name and this is the key.

**1:05:10** · So we're pulling this value from this the config map and putting it into our theme environment variable. And then we can inject a value from our secret very similar way. Secret key ref from db-credentials and the password. And so that's going to be injected into our db password environment variable. So I'm just going to save this and let's create this pod with qcontroller reply podconfig.yaml.

**1:05:41** · And now let's check its logs.

**1:05:43** · QController logs config demo pod. Okay.

**1:05:47** · Now if we look at the logs here, we can see that the theme and the password have been set. Now let's talk about mounting as a volume. Another powerful method is to mount a config map or secret as a volume. This makes the data appear as files inside the container which is perfect for applications that expect to read configuration from disk.

**1:06:13** · So let me just put in this YAML here.

**1:06:15** · This manifest tells Kubernetes to create a volume called config volume using the data from our app-config config map. It then mounts the volume inside our container at /cconfig.

**1:06:33** · So this is what we're mounting here. And each key in the config map becomes a file in that directory. So let's exit out of this and we'll save it. So we'll create this and check the logs. So cubecontroller apply pod-vol.yaml YAML and then cubecontroller logs volume-demo-pod and the output is retries equals 3 which is the content of the file we created by mounting our config map.

**1:07:01** · This shows just how flexible Kubernetes is for managing application configuration.

**1:07:12** · Kubernetes can automatically scale the number of pods in a workload based on resource utilization. This is handled by the horizontal pod autoscaler or HPA.

**1:07:23** · The HPA relies on a source of metrics to make scaling decisions. The most common source of basic CPU and memory metrics is the metric server, a cluster add-on that collects resource metrics from each cublet and exposes them through the cubernetes API. So this is how you install the metric server. basically just cubecontroller reply-f and then we have the URL where we download the metric server from and then we can see metric server created.

**1:07:51** · So we should be able to verify the installation and fetch metrics using this cube controller top nodes. If you get an error that sometimes can happen in self-hosted Kubernetes clusters like this one and it's trying to securely verify the self-signed certificates of the nodes or the cublets which it cannot do by default. So the fix is to edit the metric server deployment and add a command line argument that tells it to skip this verification.

**1:08:19** · Now, you may not have this problem, but we'll do cubecontroller edit deployment metric server and then and then we'll just go down here to the args and then we can just add an extra line here. Cubullet cubit insecure TLS and then just save and quit. We just finished editing that.

**1:08:38** · Now, we just have to wait a minute for the pods to start and become ready. We can always use get pods to check the status. I mean cube controller get pods.

**1:08:49** · Okay, the metric server is running. So we should be able to do get controller top nodes. Okay, now we can see that we can see the metrics here and then we can also do get cubecontroller top pods a and we can see the metrics for the pods.

**1:09:08** · Okay, the metric server is working correctly.

**1:09:14** · The HPA controller periodically queries the metrics API and adjusts the replicas field of a target resource to bring the current metric value closer to the target value you define. A critical prerequisite for CPU or memory based autoscaling is that the containers in the target workload must have resource requests defined. The HPA calculates utilization as a percentage of these requests. Without them, the HPA cannot function. So the HPA needs a target to scale.

**1:09:46** · Let's create a simple PHP Apache deployment. The most critical part of this manifest is the resource request.

**1:09:55** · So do nano HPA demo deployment.yml and then we'll create the deployment. So we'll look closely at the resources.request.cpu 2000M line. This is essential. It tells Kubernetes that this pod needs about 20% of a CPU core to run. The HPA uses this request as a baseline. When we tell the HPA to target 50% CPU utilization, it means 50% of this 200 millores request.

**1:10:30** · Without a resource request, the HBA has no idea what the processing percentage is relative to and it won't work. So I'm going to save that and let's apply this manifest and then expose it as a service so we can send traffic to it. So we apply with cubecontroller apply and then we'll create a cluster IP service named PHP Apache to explo expose the deployment on port 80.

**1:10:57** · Okay, now that we have our application running, let's create the HPA the horizontal pod autoscaler to manage it. We'll use a simple cube controller autoscale command. So this command here creates an HPA resource. So the autoscale deployment a PHP Apache. We're telling the HPA to target our PHP Apache deployment. Then the CPU percent 50.

**1:11:24** · This is our goal. The HPA will try to keep the average CPU utilization across all pods at 50% of their requested CPU.

**1:11:33** · And then the min equals 1. This is the minimum number of replicas. The HPA will never scale down below one pod. And then we have max 10, which is our safety limit. The HPA will never create more than 10 pods, protecting us from runaway scaling event that could crash our cluster or run up a huge cloud bill.

**1:11:54** · Okay, our HPA is ready, but right now it's just sitting idle because our application has no traffic. Let's fix that. We'll run a temporary pod that sits in an infinite loop constantly sending requests to our PHP Apache service. This will drive up the CPU usage and trigger the autoscaler. So this is what we're going to be running.

**1:12:16** · So this is going to be the loop while true. And then basically it's just going to So you see the -at runs the pod interactively. The dash rm cleans it up automatically when we exit. And we're using a tiny busy box image. And this command is a simple shell script that downloads the homepage from our service over and over again. Okay, it looks like our server needs a file to serve.

**1:12:43** · So we just need to create a file for it to serve. So, so we're going to delete the deployment and delete the service. We're going to have to redo something here.

**1:12:58** · And then this command is going to create a new config map named PHP-index that contains a simple PHP script. The script is designed to perform some calculations to generate the CPU load needed for our HPA demo. Now we need to tell our deployment to mount the file from our config map into Apache's web root directory. And I added a new section to the file. We have this volume mounts section and then the the volume section down here.

**1:13:26** · So we'll save and close the file and then we'll apply the updated deployment and then we just have to uh ex expose as a service again. Now in one terminal we're going to watch the HVA with this cube control get HVA and then I'm going to open up a new terminal and then we'll run the load generator again. Okay, that's working.

**1:13:46** · So now over here we can see we have the cube controller get HPA-W and we can watch the HPA status the because we have the -w it's giving us a live feed and we can see we can see the initial state. So in the targets uh we can see it's um a very low number 2% of 50 0% of 50 but then the load increases.

**1:14:18** · So a after mint the metric server reports the high CPU usage from our load generator we see the target is going to 270% 134% this means that the current average CPU is is like here is 270% of our 50% target so now we can see um as soon as the HPA sees the target is exceeded it springs in action. So we'll see the replica count.

**1:14:50** · So see it was 114 610. It's come that's the maximum is 10.

**1:14:57** · The HPA is adding more pods to spread the load. And then so uh since more pods are being act added we can see the load goes back down. Now we're just at 41%.

**1:15:11** · So everything's been stabilized. So we can go over here and stop this. I'll just do command or control C. If we go back over here, we can now see a scale down. If if we wait a little bit. So now we can see this has gone to 4%. 4% of 50. And then eventually the replicas would also go back down to one. So that's it. We just witnessed a fully automated resource-based scaling in Kubernetes.

**1:15:40** · This is a fundamental concept for building resilient and efficient applications.

**1:15:49** · Beyond basic configuration, Kubernetes offers several mechanisms to create robust self-healing application deployments.

**1:15:58** · Health probes are checks performed by the cublet to determine the health of a container. A livveness probe determines if a container is running. If the livveness probe fails, the cublet kills the container and the container is subject to its restart policy. A readiness probe determines if a container is ready to serve traffic. If the readiness probe fails, the endpoints controller removes the pod's IP address from the endpoints of all services that match the pod.

**1:16:27** · A startup probe indicates whether the containerized application has started successfully. If a startup probe is configured, it disables livveness and readiness checks until it succeeds, protecting slow starting applications from being killed prematurely. Okay, let's get hands-on and see how to make our applications more robust and control exactly where they run in our cluster. We'll start by configuring health probes to teach Kubernetes how to tell if our application is truly health healthy.

**1:16:58** · So, we're going to create a pod with two different types of probes. A readiness probe to see if the app is ready for traffic and a livveness probe to check if it's still running correctly. Okay, I'm creating this file pod probe.yaml we'll use to set up set this up. Okay, so here's our file. Let's break this down before we apply it. Under readiness probe, we're using an HTTP getit probe.

**1:17:24** · This tells the Kubernetes the cublet to send an HTTP get request to the container's port 80 on the path just the home path or slash. If it gets a successful response, a 200 level status code, the container is considered ready.

**1:17:40** · The initial delay seconds, the cublet will wait five seconds after the container starts before performing the first readiness check, which gives our app time to start up. And then we have the period seconds of 10. The cublet will perform this readiness check check every 10 seconds. And then under liveness probe, we're using a TCP socket probe. That's right here. And this is a simpler check. The cublet just tries to obtain a TCP connection on port 80. If it can connect, the app is considered alive.

**1:18:12** · And uh these ones are just the same as before. Okay. So we can save this and we'll start. We'll create the pod controller reply. So we got that created. Now to now to see this in action, we will do cubecontrol describe pod. And if we look at this events section, we can see messages from the cublet as it executes the probes. You'll see it successfully checked the livveness and readiness of the container. Now let's see what happen when a probe fails.

**1:18:43** · The readiness probe is the easiest to demonstrate. Let's say we deploy a new version with a typo in the health check endpoint. We can simulate this by deleting the pod and changing the path and a readiness probe to something that doesn't exist.

**1:19:00** · So do cube control delete pod probe demo and then we'll go into the editing and then so for this path we'll just change this to bad and then we can just save this again and then we just have to reapply it and then we can go back to the describe pod. Now I'm going to do get pod uh probe demo. We can see it's zero out of one already. The pro the pod is running but it's not ready to accept traffic.

**1:19:31** · And then if we do the describe again, we can see the readiness probe fails. HTV probe failed with status 404.

**1:19:42** · If this pod were part of a service, Kubernetes would already have removed it from the pool of available endpoints, protecting our users from serious errors. This is an this is an important tool for zero downtime deployments.

**1:20:00** · Setting resource requests and limits is important for stable cluster operation.

**1:20:05** · Requests are the amount of CPU and memory that is guaranteed for a container. The Kubernetes uses the request value to decide which node to place the pod on. Limits are the maximum amount of CPU memory that a container is allowed to use. The cublet enforces these limits. If a container exceeds its CPU limit, it will be throttled. If it exceeds its memory limit, it will be terminated with an OOM killed or out of memory error.

**1:20:32** · The relationship between resource requests, scheduling, and autoscaling is a critical system to understand. A failure to set requests prevents the HPA from functioning.

**1:20:45** · Setting requests too high can cause pods to become stuck in a pending state if no single node has enough allocatable resources to satisfy the request.

**1:20:56** · Setting limits too low can cause applications to be killed unexpectedly under load. A competent administrator must grasp this entire causal chain to design and troubleshoot workloads effectively.

**1:21:12** · The Kubernetes scheduler makes intelligent decisions about where to place pods. Administrators can influence these decisions using several mechanisms.

**1:21:23** · Node affinity attracts pods to a set of nodes based on labels on the nodes. It allows you to constrain which nodes your pod is eligible to be scheduled on.

**1:21:34** · There are two types. Required during scheduling ignored during execution, which is a hard requirement. The scheduler will only place the pod on a node that matches the rule. And preferred during scheduling ignored during execution, which is a soft requirement. The scheduler will try to find a node that matches the rule, but will schedule the pod elsewhere if it cannot. Now, let's control where our pods get scheduled. Node affinity is like telling a pod, I'd like you to run on nodes that have this specific characteristic. We do this with labels.

**1:22:07** · So, uh, first let's add a label to our worker node. So, I do cubecontroller get nodes to get the nodes. We can see our worker node is just ks worker. So, cubecontroller label node and we're on the control plane node, but we can label the worker node from here. And so we're giving it the label disk type equals SSD. Uh so we're kind of pretending like it has a solid state drive. Okay, we got that labeled. So now we can create a pod that requires this label. So I'm going to create a file affinity pod.yaml.

**1:22:43** · And inside the affinity section here, uh we are setting a hard requirement. The match expressions part says the scheduler must place the key the the pod on a node where the disk type label has a value that is in this list of values here which in this case is just SSD. So we're just going to close that or save that and close it and then I'll apply with cubecontroller apply-finity pod.yml.

**1:23:14** · And to verify that it worked, we'll get our pods and use the - o wide flag, which shows us which node each pod is running on. And let me just zoom out a little bit so it's easier to see this.

**1:23:26** · And we can see the SSD pod which is being run on the KS worker node because that's the only node that matched our affinity rule. Actually, in this case, that's the only node we even have. But if we had multiple nodes then we this would make sure that the SSD pod or it's only worker node we have and that's how you would make it go to a very specific worker node. Theuler correctly ignored the control plane node because it didn't have the required label. It did not get scheduled on the control plane node.

**1:23:58** · Taints and tolerations work together to ensure that pods are not scheduled onto inappropriate nodes. A taint is applied to a node which marks it as repelling certain pods. A toleration is applied to a pod allowing it to be scheduled on a node with a matching taint. Taints have one of three effects. No schedule, which means no new pods will be scheduled on the tainted node unless they have a matching toleration.

**1:24:25** · Prefer no schedule, which means the scheduler will try to avoid placing pods without a matching toleration on the node. and no execute which evicts any running pods from the node that do not tolerate the taint. So let's taint our worker node. So we will add a taint that says this node is reserved for GPU application. So unless it's GPU no schedule.

**1:24:50** · Um so the no schedule effect means no new pods will be scheduled on this node unless they have a matching toleration. Okay, so it's tainted now.

**1:25:02** · Now let's try to schedule a regular engineext pod without any special permission. So it's created and if we do get pods o wide and normal pod this is one we just created we can see it's not on any node because uh it in it avoided the tainted worker node in a real cluster it would say pending if no other nodes are available. So now let's create a special pod that can run on our GPU node.

**1:25:30** · So we're creating this file toleration pod.yaml and we can see that we have a value of GPU effect no schedule. So let's close this save it and we can apply that. And then we will go to our get pods again. And we can see our GPU pod did get scheduled onto our worker node here. It has the right key to bypass the no trespassing sign.

**1:25:56** · So this is how you create a dedicated nodes for special workloads ensuring that only the right applications can run on them.

### Services & Networking

**1:26:07** · Networking is a central and complex part of Kubernetes. This section covers how Kubernetes facilitates communication between pods, exposes applications to internal and external traffic, and secures network pathways. A solid grasp of these concepts is important for deploying and troubleshooting multicomponent applications. The fundamental networking model in Kubernetes is that every pod receives its own unique IP address within the cluster.

**1:26:38** · Crucially, every pod can communicate with every other pod on any other node without needing network address translation ornat. This flat networking model is implemented by a container network interface or CNI plug-in. When you install a CNI like Calico or Flannel, it takes responsibility for assigning IP addresses to pods and configuring the necessary routing on each node to enable this direct communication. While pods have unique IPs, they are ephemeral.

**1:27:09** · They can be created and destroyed and their IPs can change. This makes direct communication with pod IPs unreliable.

**1:27:19** · The service object solves this problem by providing a stable abstraction layer over a logical set of pods. A service gets a stable virtual IP address or the cluster IP and a DNS name and it uses a selector to identify the group of backend pods it should forward traffic to. There are several types of services each designed for a different use case.

**1:27:40** · This is the default service type. It exposes the service on a cluster internal IP address. This makes the service reachable only from within the cluster. It's the standard way to enable communication between different microservices running inside the same cluster. Okay, let's see how Kubernetes networking works in practice. We'll start with the most fundamental object for exposing applications which is the service. So this is about the cluster IP service. We need an application to expose.

**1:28:10** · So this time we'll create a simple enginex deployment with two replicas. The important thing to notice here is that Kubernetes will automatically add the label app equals my app to the pods it creates. Okay, we got that created. If you've been following along, you may have to do delete deployment my app to delete the one that we already created earlier in this tutorial because I want to make sure it's um different for this section of the tutorial.

**1:28:37** · So now that our pods are running, we'll create um a cluster IP service to give them a stable internal IP address. So like usual, we'll do this declaratively using a YAML file. So I'm going to create this file cluster IP service.yaml. And let's look at this file. We have the type of cluster IP, which is uh default, but we're being explicit here. The most important line selector app my app, the critical link.

**1:29:05** · Um, this tells a service, find all the pods in this name space that have the label app equals my app and send traffic to them. It's the bridge between the service and the pods.

**1:29:16** · So, I will exit this, save it, and now we'll apply it. So, now that the service is created, we can test it. Since it's a cluster IP, it's only accessible from inside the cluster. So, we will launch a temporary pod and use it as a shell to test our connection. That's what this line is doing right here. Okay. Now that we're inside our temporary pod, we can access our EngineX application simply by using the services name. So, I'm just going to w get my app service. And there it is, the EngineX welcome page.

**1:29:48** · This proves our service is currently routing traffic to our backend pods. Now, we'll just type an exit to destroy our temporary pod.

**1:30:03** · A nodeport service exposes the application on a static port on each node's IP address. A node port service automatically creates a cluster IP service and the node port routes traffic to this internal cluster IP. This is useful for development or for exposing a service when a cloud load balancer is not available. Now let's expose our application to the outside world using a node port. This is great for development or when you don't have a cloud load balancer. So let's create a file called node nodeport service.yaml.

**1:30:38** · And the only major change here is this type nodeport. So let's create this. So I'll save it. And now we'll just apply the node port service. Uh what we created that. And to access this we need two pieces of information. The IP address of one of our nodes and the port that kuberneti kubernetes uh assigned.

**1:31:01** · So let's get the service details to find the port. So in the output we can look at the port column and that is our node port the 3 32149.

**1:31:14** · Now we'll do the get nodes wide to make sure we can get our worker nodes IP address which is right here 192.1681.161.

**1:31:24** · So we'll just try doing a curl hp slash and then we can put in the IP address and then the node port number.

**1:31:34** · Okay. And we can see the engineext welcome page. So we've successfully accessed our cluster from the outside.

**1:31:43** · And now look at this. Um, I've been running Kubernetes in a virtual machine on my Mac OS and now I just went to a web web browser on my Mac OS, not even in the virtual machine and I can still access the EngineX welcome page from that URL from the IP address and the port number.

**1:32:09** · Creating a load balancer service automatically provisions a node port and a cluster IP service to which the external load balancer will route traffic as each service requires its own load balancer and public IP. Ingress and the newer gateway API provide more sophisticated ways to manage external access enabling L7 or HTTP/HTPS routing.

**1:32:35** · An ingress is a Kubernetes API object that manages external access to the services in a cluster, typically HTTP. It can provide load balancing, SSL termination, and namebased virtual hosting. An ingress resource itself does nothing. It requires an ingress controller to be running in the cluster to be fulfilled. The ingress controller is a reverse proxy that watches the Kubernetes API for ingress resources and configures itself accordingly.

**1:33:02** · Now let's talk about path-based routing with ingress. What if we have multiple services but only want to use one external IP? That's what ingress is used for. It's a smart router for our cluster. So first we need to install an ingress controller. We'll use the popular EngineX ingress controller.

**1:33:24** · Okay. Now let's deploy two different applications. We'll use a simple echo server image that just echoes back information about the request. So here we are going to deploy and expose the first app. Create deployment app one and then we get the echos server and then we expose it. And so that one is done. And now we'll do the same thing with app two. And so we got that one ready as well. Okay.

**1:33:54** · Now for the core of the demo, we'll create an ingress resource that defines our routing roles. So let me start by creating a YAML file. And now we have this file that says if an incoming request is going to slapp one, route it to our app one service. And then if it's going to app 2, route it to our app 2 service. So I will save that.

**1:34:22** · And then we can apply it just with cubecontroller apply ingress at yaml.

**1:34:26** · Okay, now we need to test it. Uh there's kind of a few ways. If uh we could get the external IP, but we're not going to have an external IP because we're just running it locally. But the load balancer service automatically creates a node port as a fallback and we can use this port along with the worker nodes IP address to access the ingress controller. So let's get the details of the ingress engineext controller service to find out the port it's exposed on. So here we can see it's 32733.

**1:34:57** · And basically this is very similar to what we did just very recently in the tutorial where we get the IP address of our worker node and then we can just combine it with the port here. Okay. Can run this curl command with the IP address and the port number we got and then the slash app one and we got it.

**1:35:18** · Now let's go to app two. And it works.

**1:35:22** · The first command returns a response from the app one pod. The second returns a response from app two. So we've successfully read traffic to two different services using a single IP address and different URL paths. So that's the power of ingress.

**1:35:39** · The gateway API is an official Kubernetes project that represents the next generation of Ingress. It's designed to be more expressive, flexible, and rooriented. It decouples the configuration into three main resource types. Gateway class is a cluster scoped template defining lo a type of load balancer. Gateway defines where and how the load balancer listens for traffic. And finally, HTTP route and others like TCP route defines protocol specific routing rules.

**1:36:09** · The separation of roles allows infrastructure teams to manage the gateways while application teams manage their own routing rules safely.

**1:36:24** · While a load balancer service is effective for exposing a single service, it can be inefficient and costly. By default, all pods in a Kubernetes cluster can communicate with all other pods. Network policies act as a firewall for pods, allowing you to control traffic flow at the IP address and port level or layer three and four. To enforce network policies, you must use a CNI plugin that supports them, such as Calico, Celium, or WeaveNet.

**1:36:49** · A common and highly recommended security practice is to start with a default deny policy that blocks all traffic and then explicitly add allow rules for required communication paths. Let's talk about securing an application with network policies. By default, any pod can talk to any other pod. Let's lock that down using network policies which act as a firewall. So, we're going to create a default policy, a default deny policy, which is a security best practice.

**1:37:19** · So, we got this file deny all and then we got a this is how you make it. The pod selector, it's empty. So select all p all pods and then it we're providing no ingress rules which means it blocks all incoming traffic. So we can save that.

**1:37:39** · We can apply it and then I'll just create a engineext server really quick and then we will expose it deploy it. So I'm going to try to connect. So basically we're creating a temporary shell. And then I'm going to run this wget command with a timeout of two because we expect it to fail. Okay, it failed which is perfect. Our deny policy is working. Now let's create a specific allow rule. We'll create a policy that allows our web server but only from pods that have the act the label access true.

**1:38:14** · Okay. So I'll create a new YAML file and then we're allowing from uh from pods that have the label access equals true.

**1:38:24** · So I will save that. I will apply it.

**1:38:27** · And now we'll run our client pod again, but this time we will give it a label access true. Okay. Now we should be able to get the EngineX welcome page. We have successfully implemented the firewall inside our cluster locking down traffic and only allowing specific required connections.

**1:38:47** · Core DNS is the default DNS server for Kubernetes. It's a flexible extensible DNS server that provides service discovery within the cluster. When you create a service, core DNS automatically creates DNS records that allow other pods in the cluster to resolve the service by its name. The standard DNS records follow this pattern. For a service, it's service name.namespace.

**1:39:15** · SVC.cluster.local.

**1:39:17** · And for a pod, it's pod-ip-namespace.pod.cluster.local.

**1:39:24** · CoreDNS is configured via a config map in the cube system namespace which contains a core file. The core file uses a plug-in base architecture to process DNS queries. Key default plugins include Kubernetes which answers DNS queries based on Kubernetes services and pods.

**1:39:44** · Forward which forwards queries that cannot be resolved within the cluster to an upstream DNS server. and cache which provides a caching layer to improve performance. Okay, now let's talk about customizing core DNS. By default, it knows how to find any service we create.

**1:40:01** · But what if our pods need to talk to a server on a private corporate network?

**1:40:06** · Let's say we have an internal domain like u mycorp.com that can only be resolved by our company's private DNS server. We're going to customize core DNS to teach it how to resolve these private addresses all without disrupting its normal cluster duties. So the first step is to inspect the current DNS configuration. So before we change anything, let's look at the default configuration. Core DNS is configured via a config map located in the cube system namespace and we can edit it directly.

**1:40:39** · So we have the config map and this is a live config map in the cluster. So we'll see a key called core file. This is the main configuration. So notice this block the col53.

**1:40:56** · The dot means the block is the default for any query. Inside you'll see a forward plugin pointing to the etc/resolve.

**1:41:07** · This is the default behavior. If core DNS can't resolve a name without the cluster like google.com, it forwards the request to the same upstream DNS servers that the node itself uses. You'll also see the reload plugin, which is the line right here. This is important. It means cordiness watches this file for changes and will automatically apply them without needing a restart. It's what allows us to do this live edit safely.

**1:41:39** · So, we're going to add a custom forward for forwarding rule. We're going to add a new specific server block. This block will only handle queries for our internal domain, which is going to be uh mycorp.com. So, let's go down past this curly brace right here, right before kind. And I have to press I to go to insert mode. And now I'm going to add a new block for our internal domain.

**1:42:03** · Okay, so we have the domain 53 errors and we have errors cast 30 and then the forward where it's going to be forwarding to. So basically the my corp 53 defines a new DNS zone. U core DNS now knows that any query ending in my corp.com should be handled by this block specifically. CDNs always picks the most specific matching block.

**1:42:29** · So this will be used before the default block for these queries. where it says errors, that just tells it to log any errors to standard output. The cache 30, we're telling it to uh cache responses for 30 seconds to reduce load on our internal server. And then the forward line is the key part. It tells core DNS to forward any query it receives in this block to our private DNS server, which we are saying is at the IP address 10.10.0.53.

**1:42:58** · So, let's save this. So we'll hit escape and then colon wq. Okay. Now let's verify the custom rule works. So the final which is the final most important step. We need to test the nest resolution from inside a pod. So let's run a temporary pod with some networking tools. So I'll just run the temporary pod with this. I'll use a debris box image and use and get an interactive shell.

**1:43:25** · So, we'll use this nsookup command to query for a fake server on our corporate domain. And even though the server doesn't exist, okay, there it goes. So, even though the server doesn't exist, it should return a response from our fake internal DNS.

### Storage

**1:43:48** · While many containerized applications are stateless, stateful applications like databases require storage that persists beyond the life cycle of a single pod. Kubernetes provides a powerful and abstract storage framework built around persistent volumes, persistent volume claims, and storage classes. It's important to distinguish between the different volume concepts in Kubernetes.

**1:44:15** · A volume is a directory containing data that is accessible to the containers in a pod. The life cycle of a volume is tied to the life cycle of the pod that encloses it. When the pod ceases to exist, the volume is destroyed and its data is lost. This is suitable for ephemeral data. A persistent volume or PV is a piece of storage in the cluster that has been provisioned by an administrator or dynamically provisioned using a storage class.

**1:44:45** · It's a resource in the cluster just like a CPU or memory. The key feature of a PV is that its life cycle is independent of any individual pod that uses it. When a pod is deleted, the data in the PV persists.

**1:45:00** · A persistent volume claim or PVC is a request for storage by a user. A developer creates a PVC specifying the required size and access mode without needing to know the details of the underlying storage infrastructure. The PVC acts as a claim on a PV resource.

**1:45:20** · When a user creates a PVC, the Kubernetes control plane looks for a PV that can satisfy the claims requirements. If a suitable available PV is found, the control plane binds the PVC to that PV. This is a onetoone mapping. Once bound, no other PVC can claim that PV. A pod can then request the storage by referencing the PVC in its volume definition. When defining PVs and PVCs, two of the most important specifications are the access mode and the reclaim policy.

**1:45:50** · Access modes define how a volume can be mounted by nodes in the cluster. The chosen access mode must be supported by the underlying storage provider. The primary access modes are read write once or RWO which means the volume can be mounted as read write by a single node. This is the most common access mode and is supported by most volume types. Read only mini or ROX which means the volume can be mounted as readon by many nodes simultaneously.

**1:46:24** · Read write many or RWX which means the volume can be mounted as read write by many nodes simultaneously. This is supported by network file systems like NFS or SEF FS and read write once pod or RWOP which is a newer model that restricts volume access to a single pod.

**1:46:44** · This is the most restrictive and secure option. The reclaim policy of a persistent volume tells the cluster what to do with the volume after its bound persistent volume claim has been deleted. A retain policy means that when the PVC is deleted, the PV remains. The volume, its data, and its underlying storage asset are not deleted. The cluster administrator must manually clean up the volume and its data. This is the safest policy for production data.

**1:47:14** · A delete policy means that when the PVC is deleted, the PV and the associated external storage asset are automatically deleted. This is often the default for dynamically provisioned volumes. A recycle policy performs a basic scrub on the volume and makes it available again for a new claim. This policy is no longer recommended due to security concerns and has been replaced by dynamic provisioning. Okay.

**1:47:43** · Kubernetes storage. We're going to start with the foundational manual method called static provisioning which is a great way to understand the building blocks of how Kubernetes handles persistent data. So in this example, I'm going to play two roles. The first I'll be the cluster administrator who is responsible for creating the available storage. Then I'll switch hats and become the application developer who needs to request and use the storage.

**1:48:06** · So the admin's job with the admin's hat on, my first job is to make some storage available to the cluster. So I'll define a persistent volume or PV in a YAML file. So nanopv.yaml.

**1:48:28** · So let's break this down. For the capacity, I'm making 5 GB of storage.

**1:48:33** · Then the access mode is read write once which means that the voling can only be mounted for reading and writing by a single node at a time. And then the storage class name is manual which means we're using uh which basically it's a custom name I've created which is like a label. It's how developers will find and request this specific type of storage.

**1:48:55** · And then the host path is simply maps to a directory on the node's file system.

**1:49:01** · But be careful. This is great for local demos, but you would never use this in production because the data is tied to a single node. So, let's apply this. I'm going to save this and then we'll apply the file to create a PV. Now, let's see what we've done.

**1:49:21** · So, we'll do cube control get pv. Okay.

**1:49:26** · So, we can see right there the status is available. It's like a reserve parking spot, empty and waiting for a car to claim it. So, let's go to step two, which uh basically I'm switching hats.

**1:49:40** · I'm a developer who needs to store data for my application. I don't need to know about the underlying storage. I just need to make a request. This request is a persistent volume claim or PVC. So, I'll do nano pvc.yaml.

**1:49:56** · So, this is what I want. I'm requesting storage with the storage class name manual. So this tells Kubernetes to find a PV with that same class name. And then I'm also requesting a readwrite once access which must match the PV. I'm asking for 2 GB. Kubernetes will find the smallest available PV that can satisfy the request and our 5 GB volume is a perfect match. So I'll save that and then I will apply it.

**1:50:26** · And now we can list both our PV and PVC's at the same time. Um, whips with a comma. And let me zoom out a little bit. Okay, now we can see it all on one screen here. So we can now see the status of this is bound. The developer's claim has been successfully matched with the administrators volume.

**1:50:52** · Kubernetes will now hold this PV for our PVC until we release it. So now let's talk about using the PVC in a pod. The final step is to actually use the storage in an application. So we'll create a pod that references our PVC. So we'll start with creating a YAML file pod storage.yamel.

**1:51:11** · And then under volumes, we're defining our a volume for our pod named my storage. and we're telling it to get its storage from the persistent volume claim named task pv claim. Then in the volume mounts section, we mount that volume into our engineext container at this path here which is the web route. So we'll save that and then we will apply. Okay, that's it.

**1:51:43** · Our EngineX pod is now running and any files it writes to its website directory will actually be saved to the /mount/data on our host node. The data is now persistent and will survive even if this pod is deleted and recreated.

**1:52:02** · Manually creating PVs is inflexible and doesn't scale well. Dynamic provisioning automates the creation of PVs. Instead of pre-provisioning PVs, an administrator defines one or more storage class objects. A storage class provides a way for administrators to describe the classes of storage they offer. Each storage class specifies a provisioner which knows how to create the storage and parameters specific to that provisioner.

**1:52:29** · When a user creates a PVC that specifies a storage class name, the corresponding provisioner is triggered to automatically create a matching PV and bind it to the PVC.

**1:52:44** · Dynamic provisioning with storage classes. That static method was a lot of work for the admin. Now let's look at the modern automated way. Dynamic provisioning. Here the admin just sets up a template and storage is created on demand. So let's inspect the storage class. The template for creating storage is called a storage class. Most Kubernetes environments come with a default one already set up. So let's see what we have with get storage class.

**1:53:11** · Okay, none are found. But don't worry that none is found. This is completely normal and expected for a cluster you've built yourself with cube ADM. Cloud providers like Google Cloud or AWS automatically provide a default storage class that's that's linked to their block storage services. But our local cluster doesn't have one because Kubernetes has no idea what kind of storage hardware we have available. So we need to install one ourselves. For a local lab environment like ours, the easiest solution is to install a host path provisioner.

**1:53:42** · This will create a storage class that provisions storage by simply creating directories on our worker nodes local disk. But before we install it, it's important to understand that this hostpad path method is fantastic for learning and development, but it should never be used in a real production environment. It ties all of our data to the disk of a single node, which is not durable or highly available. So with that invi in mind, we're going to install the rancher local path provisioner.

**1:54:12** · So this command that I have here will download its manifest and create all the necessary components in our cluster. Once that's installed, we can run our git storage command. And we can see that there is now a storage command or a storage class here. So our cluster now has a way to automatically provide storage. So let's see this in action. This is the magic of dynamic provisioning.

**1:54:41** · As an application developer, I don't need to ask an admin to create storage for me anymore. I can just request it by creating a persistent volume plc. So I'm going to create a file named my PVC.yml to define our storage request. So we can see we're going to be using the storage class we just created local path and this volume can be mounted by a single node and we're requesting one gigabyte.

**1:55:10** · So let me save that and then we will apply it. So do cubecontroller get PVC.

**1:55:16** · We can see this claim is pending and basically that's what we want to see.

**1:55:23** · It's waiting the storage provisioner is waiting for a pod that actually uses this PVC to be created before it binds.

### Troubleshooting

**1:55:34** · Troubleshooting is the most heavily weighted domain in the CKA exam, reflecting its importance in the day-to-day work of a Kubernetes administrator. A systematic and logical approach is key to efficiently diagnosing and resolving issues in a complex distributed system like Kubernetes. A chaotic approach to troubleshooting leads to wasted time and potential misdiagnosis.

**1:56:00** · A structured methodology is essential especially in a timed exam environment.

**1:56:06** · The recommended approach involves five steps. First, identify the problem.

**1:56:11** · Clearly define what is not working. Is a pod crashing? Is a service unreachable?

**1:56:16** · Is the cluster unresponsive? Start with a highle check like cube controller get pods. Second, gather information.

**1:56:24** · collect logs, events, and resource definitions to understand the context of the failure. The cube controller describe command is one of the most powerful tools for this step. Third, analyze the data. Examine the collected information to form a hypothesis about the root cause. Look for error messages, status conditions, and relevant events.

**1:56:48** · Fourth, implement a solution. Apply a fix based on your hypothesis. This might involve editing a YAML manifest, correcting a command, or restarting a component. And fifth, verify the solution. Confirm that the fix has resolved the issue and has not introduced any new problems. When troubleshooting, it's often effective to work from the application layer down to the infrastructure layer. Pod, service, node, cluster components.

**1:57:21** · Pod failures are the most common issues an administrator will face. Pods can fail to start or crash during runtime for many reasons. The status of a pod provides the first clue to what might be wrong. A pending status means the pod has been accepted by the cluster, but one or more of its containers has not been created yet. This could be because it's waiting to be scheduled or is downloading images.

**1:57:47** · Container creating means the pod has been scheduled to a node but the container runtime is in the process of starting a container. Image pull back off or error image pull means the cublet was in unable to pull the container image from the registry. Crash loop back off means a container in the pod started but then executed with an error. The cublet is repeatedly trying to restart it but it keeps crashing.

**1:58:13** · An error status means the pod has failed and the phase is not succeeded and om killed means the container was terminated because it exceeded its memory limit. The most common reason for a pod to be stuck in pending is a scheduling failure. This can be due to insufficient resources, failing node affinity anti-affffinity rules, the node being tainted and the pod lacking a toleration or an unbound persistent volume claim.

**1:58:43** · The cube controller describe pod command is the most important tool here. The event section at the bottom will provide a clear reason such as 0/3 nodes are available three insufficient CPU. If the cause is resource related, check node capacity with cube controller describe node. The cause is usually an incorrect image name or tag in the pod manifest, an error authenticating with a private registry, or the registry being unreachable.

**1:59:12** · Your best debug step here is to again use cube controller describe pod. The events will show a failed event with the message failed to pull image and a specific error. This is often the most complex issue as it indicates a problem within the application or its configuration. The cause is likely an error in the application code or a misconfiguration, a failing lightness probe or incorrect file permissions. The most critical step here is to check the logs.

**1:59:42** · The logs will almost always contain the error message or stack trace that reveals the root cause. You can also check the pod description to look for clues and the container's exit code.

**1:59:55** · If the container starts but crashes too quickly to get logs, you may need to modify its command to keep it alive for debugging. For example, change the command to sleep 3600 and then use cubecontroller exec to get a shell inside.

**2:00:14** · Kubernetes provides another mechanism for containers to report fatal events.

**2:00:19** · Termination messages. A container can write a brief message to a file and Kubernetes will surface this message in the last state. Terminated message field of the container status which is visible in the output of cube control describe pod. This can be useful for providing a concise summary of a failure when full logs are too verbose.

**2:00:44** · If applications are failing clusterwide, the problem may lie with the nodes or the control plane itself. Nodes can be in several states. The most common problematic states are not ready and scheduling disabled. A not ready node means the cublet on the node is not reporting a healthy status to the control plane. This could be because the cublet process is not running. The node has a network partition preventing it from reaching the API server or the underlying machine is down.

**2:01:15** · Your first debug step here is to SSH into the affected node and check the status of the cublet service. If it's not running, try starting it. You can also examine the cublet logs for errors. A scheduling disabled node means the scheduler will not place any new pods on it. The cause is usually that an administrator manually cordone the node often for maintenance. The fix is to use the cube controller uncordone command on a cube ADM installed cluster.

**2:01:48** · The control plane components run as static pods. Their YAML manifests are located in etc/ubernetes/manifests on the control plane node. The cublet on that node is responsible for ensuring these pods are running. API service failure. If the API server is down, cube controller commands will fail with a connection refused error.

**2:02:11** · To debug SSH into the control plane node, check if the cube API server container is running using the container runtimes command line interface. Check its logs. And finally, inspect its manifest file for syntax errors or incorrect parameters.

**2:02:28** · scheduler or controller manager failure.

**2:02:31** · Symptoms include new pods remaining pending indefinitely in the case of a scheduler failure or deployments not creating new pods for a controller manager failure. The process for debugging is the same as for the API server. SSH into the control plane node and inspect the corresponding static pod and its logs.

**2:02:57** · Service connectivity issues can be complex. A systematic check is the best approach. Assume you have a client pod that cannot connect to a service. First, check DNS resolution. From the client pod, try to resolve the service name with NS lookup. If this fails, the problem is likely with core DNS. Second, check the service and endpoints. Verify that the service exists and that it has selected the correct back-end pods using cubecontroller describe service.

**2:03:26** · If the endpoints list is empty, it means the services selector does not match the labels on any running pods. Correct the labels on the pods or the selector in the service. Third, check pod connectivity. Try to connect directly to a back-end pod's IP address from the client pod. If this fails, the issue is at a lower level, possibly with the CNI plugin or a network policy. And finally, check network policies. If network policies are in effect, they might be blocking the traffic.

**2:03:55** · Temporarily delete any relevant policies to see if connectivity is restored. If it is, the policy needs to be adjusted to allow the required traffic.

**2:04:09** · Understanding resource consumption is important to diagnosing performance issues and scheduling failures. The cube control top command which relies on the metric server is the primary tool for this. You can check node resource usage to get an overview of the CPU and memory utilization of each node. This helps identify nodes that are under pressure, which could explain why pods are being throttled or evicted. You can also drill down to see the resource usage of individual pods.

**2:04:40** · This is invaluable for diagnosing om killed errors, for example, by comparing usage to the pod's memory limit and for tuning HPA and for tuning HPA targets by observing typical CPU usage under load.

### Conclusion

**2:05:00** · This guide provides a comprehensive hands-on pathway to preparing for the certified Kubernetes administrator exam.

**2:05:08** · By progressing throughout each section from foundational architecture to advanced troubleshooting, candidates will build not only the theoretical knowledge, but also the critical command line muscle memory required to succeed.

**2:05:25** · The core themes that emerge are the importance of a declarative mindset, a deep understanding of the clusters underlying components, and a systematic approach to problem solving. The CKA is not a test of memorization, but of practical application.

**2:05:42** · Success hinges on the ability to quickly and accurately diagnose issues within a live Kubernetes environment, manipulate resources using cube controller and YAML, and manage the entire cluster life cycle with tools like CubeADM.

**2:05:58** · By diligently working through the demonstrations and labs presented here, aspiring administrators will be well equipped to tackle the challenges of the CKA exam and more importantly to effectively manage production Kubernetes clusters in the real world. Thanks for watching and good luck on your certified Kubernetes administrator exam.