# 📂 Section: https:
## 📖 https:
**Source:** [https://notes.kodekloud.com/docs/Ultimate-Certified-Kubernetes-Security-Specialist-CKS-Mock-Exam-Series/Course-Introduction/Introduction/page](https://notes.kodekloud.com/docs/Ultimate-Certified-Kubernetes-Security-Specialist-CKS-Mock-Exam-Series/Course-Introduction/Introduction/page)

# Introduction

> Hands-on timed CKS mock exam series offering multi-cluster scenario practice to prepare Kubernetes administrators for security tasks, runtime detection, supply chain hardening, and exam readiness

Hello — I’m Nourhan Mohamed from KodeKloud. Welcome to the Ultimate CKS Mock Exam series.

This course is built for candidates who are already comfortable with Kubernetes administration and who are preparing to take the Certified Kubernetes Security Specialist (CKS) exam. If your CKS exam is approaching, this mock exam series is designed to simulate the real exam environment and reinforce hands-on security skills across the full Kubernetes stack.

Before you begin

* You should already be familiar with Kubernetes core concepts and administration workflows (cluster architecture, `kubectl`, scheduling, networking, storage, and troubleshooting).
* If you have not completed the Certified Kubernetes Administrator (CKA) curriculum or you’re not confident with cluster administration, stop and complete CKA-level preparation first. The CKS builds on those fundamentals and focuses specifically on securing clusters, workloads, and runtime environments.

<Frame>
  <img src="https://mintcdn.com/kodekloud-c4ac6d9a/fqOZr4eJXKRMketP/images/Ultimate-Certified-Kubernetes-Security-Specialist-CKS-Mock-Exam-Series/Course-Introduction/Introduction/person-speaking-microphone-topics-list.jpg?fit=max&auto=format&n=fqOZr4eJXKRMketP&q=85&s=6bb31f54afc2e5a78410e2f46283a609" alt="A person is sitting in a chair, speaking into a microphone, with a list of topics on the left that includes &#x22;Cluster Operations,&#x22; &#x22;Networking,&#x22; &#x22;Workloads,&#x22; &#x22;Troubleshooting,&#x22; and &#x22;Administration Tasks.&#x22;" width="1920" height="1080" data-path="images/Ultimate-Certified-Kubernetes-Security-Specialist-CKS-Mock-Exam-Series/Course-Introduction/Introduction/person-speaking-microphone-topics-list.jpg" />
</Frame>

Why CKA first

<Callout icon="lightbulb" color="#1CB2FE">
  Prioritize the [CKA](https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator)-level skills (cluster architecture, `kubectl` usage, control plane components, and troubleshooting) before attempting CKS-focused security tasks — the CKS assumes those fundamentals.
</Callout>

Course format and environment

This series contains multiple, full-length, scenario-based mock exams that mirror the CKS testing model. Each mock exam:

* Is hands-on and timed.
* Uses multiple Kubernetes clusters, with a student node provided as your starting point. From there, you’ll SSH into other clusters and nodes as needed.
* Includes 16 realistic tasks covering cluster and workload security, runtime detection, supply chain protection, and incident response.

Example interaction in the exam lab (you’ll work from a shell similar to this):

```bash theme={null}
root@controlPlane ~ ⮞ kubectl get pod -n crypto-monitor
NAME                                READY   STATUS    RESTARTS   AGE
suspicious-app-596699676-fxlvp      1/1     Running   0          94s
root@controlPlane ~ ⮞ systemctl status kubelet
● kubelet.service - kubelet: The Kubernetes Node Agent
   Loaded: loaded (/lib/systemd/system/kubelet.service; enabled; vendor preset: enabled)
   Active: active (running) since Wed 2026-07-15 10:02:13 UTC; 2min 30s ago
```

Core CKS domains and weightings

The CKS exam evaluates your security skills across six domains. Below is a concise summary of each domain, its weighting, and a short description of the security focus so you can prioritize study and practice.

| Domain                                    | Weight | Focus                                                                           |
| ----------------------------------------- | -----: | ------------------------------------------------------------------------------- |
| Cluster setup                             |    15% | Secure installation, control plane configuration, and secure defaults.          |
| Cluster hardening                         |    15% | API access control, RBAC, admission controls, and control plane hardening.      |
| System hardening                          |    10% | Host-level security, kernel hardening, and minimizing the node attack surface.  |
| Minimizing microservice vulnerabilities   |    20% | Pod security, container configuration, secrets management, and least privilege. |
| Supply chain security                     |    20% | Image provenance, scanning, SBOMs, signing, and secure build pipelines.         |
| Monitoring, logging, and runtime security |    20% | Detection, alerting, forensics, and runtime protection (e.g., Falco).           |

<Frame>
  <img src="https://mintcdn.com/kodekloud-c4ac6d9a/fqOZr4eJXKRMketP/images/Ultimate-Certified-Kubernetes-Security-Specialist-CKS-Mock-Exam-Series/Course-Introduction/Introduction/person-speaking-microphone-pie-chart.jpg?fit=max&auto=format&n=fqOZr4eJXKRMketP&q=85&s=de96361eabed96a67b0cf3608ae7b54b" alt="The image shows a person sitting in a chair with a microphone, speaking. Next to them is a colorful pie chart labeled with different security topics and percentages." width="1920" height="1080" data-path="images/Ultimate-Certified-Kubernetes-Security-Specialist-CKS-Mock-Exam-Series/Course-Introduction/Introduction/person-speaking-microphone-pie-chart.jpg" />
</Frame>

What you’ll practice

Typical tasks and tools included in each mock exam reflect real-world responsibilities and CKS learning objectives:

* Enforcing pod security standards and admission controls (e.g., Pod Security Admission, OPA/Gatekeeper).
* Implementing network segmentation and network policies.
* Applying least-privilege access with RBAC and service accounts.
* Managing secrets securely and validating encryption at rest.
* Runtime detection and response using tools such as [Falco](https://falco.org).
* Supply chain hardening with image scanning and SBOMs, e.g., [Trivy](https://github.com/aquasecurity/trivy).
* Node and control plane hardening using tools like [kube-bench](https://github.com/aquasecurity/kube-bench).
* Securing ingress and service-to-service traffic with TLS/mTLS and service mesh options such as [Istio](https://istio.io).

Each mock exam is designed to reflect the difficulty and scope of the actual CKS exam, providing realistic practice in a timed, multi-cluster environment.

<Frame>
  <img src="https://mintcdn.com/kodekloud-c4ac6d9a/fqOZr4eJXKRMketP/images/Ultimate-Certified-Kubernetes-Security-Specialist-CKS-Mock-Exam-Series/Course-Introduction/Introduction/person-speaking-microphone-security-topics.jpg?fit=max&auto=format&n=fqOZr4eJXKRMketP&q=85&s=ddf67586e4a95c9cbc0ef08e5389dc61" alt="The image shows a person speaking into a microphone, seated on a chair with a list of security-related topics displayed on the side." width="1920" height="1080" data-path="images/Ultimate-Certified-Kubernetes-Security-Specialist-CKS-Mock-Exam-Series/Course-Introduction/Introduction/person-speaking-microphone-security-topics.jpg" />
</Frame>

Logistics and scoring

* Duration: 2 hours per mock exam (matches the real exam time constraints and pressure).
* Tasks per exam: 16 hands-on tasks that require command-line work, configuration edits, policy creation, and investigative troubleshooting.
* Environment: Multiple clusters and nodes; you will begin on a student node and connect to other targets as required.

Who should take this series

* Candidates who have completed CKA-level training and are now focused on Kubernetes security.
* Engineers responsible for cluster security, DevSecOps professionals, and incident responders who need hands-on practice.
* Anyone preparing to pass the CKS and wanting realistic, timed practice with exam-style scenarios.

What you’ll gain

* Practical experience securing Kubernetes clusters end-to-end.
* Improved confidence responding to runtime incidents and hardening clusters.
* Familiarity with common security tooling and best practices required for the CKS.

Links and references

* [Certified Kubernetes Administrator (CKA) — KodeKloud](https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator)
* [Falco — runtime security](https://falco.org)
* [Trivy — vulnerability scanner](https://github.com/aquasecurity/trivy)
* [kube-bench — CIS benchmark checks](https://github.com/aquasecurity/kube-bench)
* [Istio — service mesh with mTLS](https://istio.io)
* [Kubernetes Documentation — Concepts and Tasks](https://kubernetes.io/docs/)

Ready to begin?
If you’ve completed your CKA-level preparation and you’re comfortable administering clusters, proceed with the mock exams to validate and sharpen your CKS-level security skills. Good luck — and use each exam as a chance to identify gaps and focus further study.

This concludes the introduction to the CKS full mock exam series.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/ultimate-certified-kubernetes-security-specialist-cks-mock-exam-series/module/b9d31b0e-81ad-4408-9df7-4700ec4e734a/lesson/c508638f-727d-4080-9d7c-4f54990643d9" />
</CardGroup>

---


---

## 🌐 Scraped Reference Content

> [!NOTE]
> The content below has been automatically scraped from official documentation and related sub-links for deeper context.

### 📄 Source: [https://kubernetes.io/docs/](https://kubernetes.io/docs/)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - বাংলা (Bengali)   - 中文 (Chinese)   - Français (French)   - Deutsch (German)   - हिन्दी (Hindi)   - Bahasa Indonesia (Indonesian)   - Italiano (Italian)   - 日本語 (Japanese)   - 한국어 (Korean)   - فارسی (Persian)   - Polski (Polish)   - Português (Portuguese)   - Русский (Russian)   - Español (Spanish)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# Kubernetes Documentation 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- - 
Kubernetes is an open source container orchestration engine for automating deployment, scaling, and management of containerized applications. The open source project is hosted by the Cloud Native Computing Foundation ( CNCF ). 
## Understand Kubernetes 
Learn about Kubernetes and its fundamental concepts. 
- Why Kubernetes? - Components of a cluster - The Kubernetes API - Objects In Kubernetes - kubectl - Containers - Workloads and Pods View Concepts 
## Try Kubernetes 
Follow tutorials to learn how to deploy applications in Kubernetes. 
- Hello Minikube - Walkthrough the basics - Stateless Example: PHP Guestbook with Redis - Stateful Example: Wordpress with Persistent Volumes View Tutorials 
## Set up a K8s cluster 
Get Kubernetes running based on your resources and needs. 
- Learning environment - Production environment - Install the kubeadm setup tool - Metrics - Logs - Traces - Securing a cluster - kubeadm command reference Set up Kubernetes 
## Learn how to use Kubernetes 
Look up common tasks and how to perform them using a short sequence of steps. 
- kubectl Quick Reference - Install kubectl - Configure access to clusters - Use the Web UI Dashboard - Configure a Pod to Use a ConfigMap - Getting help View Tasks 
## Look up reference information 
Browse terminology, command line syntax, API resource types, and setup tool documentation. 
- Glossary - kubectl command line tool - Labels, annotations and taints - Kubernetes API reference - Overview of API - Feature Gates View Reference 
## Contribute to Kubernetes 
Find out how you can help make Kubernetes better. 
- Contribute to Kubernetes - Contribute to documentation - Suggest content improvements - Opening a pull request - Documenting a feature for a release - Localizing the docs - Participating in SIG Docs - Viewing Site Analytics See Ways to Contribute 
## Training 
Get certified in Kubernetes and make your cloud native projects successful! 
View training 
## Download Kubernetes 
Install Kubernetes or upgrade to the newest version. 
Download Kubernetes 
## About the documentation 
This website contains documentation for the current and previous 4 versions of Kubernetes. 
See available versions 
- - - - - - 

- - - - 

#### 📄 Sub-topic: [https://kubernetes.io/docs/concepts](https://kubernetes.io/docs/concepts)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - বাংলা (Bengali)   - 中文 (Chinese)   - Français (French)   - Deutsch (German)   - हिन्दी (Hindi)   - Bahasa Indonesia (Indonesian)   - Italiano (Italian)   - 日本語 (Japanese)   - 한국어 (Korean)   - Polski (Polish)   - Português (Portuguese)   - Русский (Russian)   - Español (Spanish)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese)   - فارسی (Persian) - 
  - Light   - Dark   - Auto 
# Concepts 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- - 
# Concepts 
The Concepts section helps you learn about the parts of the Kubernetes system and the abstractions Kubernetes uses to represent your cluster , and helps you obtain a deeper understanding of how Kubernetes works. 
##### Overview 
Kubernetes is a portable, extensible, open source platform for managing containerized workloads and services that facilitate both declarative configuration and automation. It has a large, rapidly growing ecosystem. Kubernetes services, support, and tools are widely available. 
##### Cluster Architecture 
The architectural concepts behind Kubernetes. 
##### Containers 
Technology for packaging an application along with its runtime dependencies. 
##### Workloads 
Understand Pods, the smallest deployable compute object in Kubernetes, and the higher-level abstractions that help you to run them. 
##### Services, Load Balancing, and Networking 
Concepts and resources behind networking in Kubernetes. 
##### Storage 
Ways to provide both long-term and temporary storage to Pods in your cluster. 
##### Configuration 
Resources that Kubernetes provides for configuring Pods. 
##### Security 
Concepts for keeping your cloud-native workload secure. 
##### Policies 
Manage security and best-practices with policies. 
##### Scheduling, Preemption and Eviction 

##### Resource Management 
How Kubernetes represents, requests, allocates, and constrains the resources that workloads consume. 
##### Cluster Administration 
Lower-level detail relevant to creating or administering a Kubernetes cluster. 
##### Windows in Kubernetes 
Kubernetes supports nodes that run Microsoft Windows. 
##### Extending Kubernetes 
Different ways to change the behavior of your Kubernetes cluster. 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified June 22, 2020 at 11:01 PM PST: Add descriptions to Concept sections (3ff7312cff) 
- - - - - - 

- - - - 

#### 📄 Sub-topic: [https://kubernetes.io/docs/concepts/architecture](https://kubernetes.io/docs/concepts/architecture)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - বাংলা (Bengali)   - 中文 (Chinese)   - Français (French)   - Deutsch (German)   - Bahasa Indonesia (Indonesian)   - Italiano (Italian)   - 日本語 (Japanese)   - 한국어 (Korean)   - Polski (Polish)   - Português (Portuguese)   - Русский (Russian)   - Español (Spanish)   - Tiếng Việt (Vietnamese)   - हिन्दी (Hindi)   - فارسی (Persian)   - Українська (Ukrainian) - 
  - Light   - Dark   - Auto 
# Cluster Architecture 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- 
  -   -   -   -   - - 
  -   -   - - 
  -   -   -   -   - - 
  -   -   -   - - 
- - - 
# Cluster Architecture The architectural concepts behind Kubernetes. 
A Kubernetes cluster consists of a control plane plus a set of worker machines, called nodes, that run containerized applications. Every cluster needs at least one worker node in order to run Pods. 
The worker node(s) host the Pods that are the components of the application workload. The control plane manages the worker nodes and the Pods in the cluster. In production environments, the control plane usually runs across multiple computers and a cluster usually runs multiple nodes, providing fault-tolerance and high availability. 
This document outlines the various components you need to have for a complete and working Kubernetes cluster. 
Figure 1. Kubernetes cluster components. About this architecture 
The diagram in Figure 1 presents an example reference architecture for a Kubernetes cluster. The actual distribution of components can vary based on specific cluster setups and requirements. 
In the diagram, each node runs the kube-proxycomponent. You need a network proxy component on each node to ensure that the Service API and associated behaviors are available on your cluster network. However, some network plugins provide their own, third party implementation of proxying. When you use that kind of network plugin, the node does not need to run kube-proxy. 
## Control plane components 
The control plane's components make global decisions about the cluster (for example, scheduling), as well as detecting and responding to cluster events (for example, starting up a new pod when a Deployment's replicasfield is unsatisfied). 
Control plane components can be run on any machine in the cluster. However, for simplicity, setup scripts typically start all control plane components on the same machine, and do not run user containers on this machine. See Creating Highly Available clusters with kubeadm for an example control plane setup that runs across multiple machines. 
### kube-apiserver 
The API server is a component of the Kubernetes control plane that exposes the Kubernetes API. The API server is the front end for the Kubernetes control plane. 
The main implementation of a Kubernetes API server is kube-apiserver . kube-apiserver is designed to scale horizontally—that is, it scales by deploying more instances. You can run several instances of kube-apiserver and balance traffic between those instances. 
### etcd 
Consistent and highly-available key value store used as Kubernetes' backing store for all cluster data. 
If your Kubernetes cluster uses etcd as its backing store, make sure you have a back up plan for the data. 
You can find in-depth information about etcd in the official documentation . 
### kube-scheduler 
Control plane component that watches for newly created Pods with no assigned node , and selects a node for them to run on. 
Factors taken into account for scheduling decisions include: individual and collective resource requirements, hardware/software/policy constraints, affinity and anti-affinity specifications, data locality, inter-workload interference, and deadlines. 
### kube-controller-manager 
Control plane component that runs controller processes. 
Logically, each controller is a separate process, but to reduce complexity, they are all compiled into a single binary and run in a single process. 
There are many different types of controllers. Some examples of them are: 
- Node controller: Responsible for noticing and responding when nodes go down. - Job controller: Watches for Job objects that represent one-off tasks, then creates Pods to run those tasks to completion. - EndpointSlice controller: Populates EndpointSlice objects (to provide a link between Services and Pods). - ServiceAccount controller: Create default ServiceAccounts for new namespaces. 
The above is not an exhaustive list. 
### cloud-controller-manager A Kubernetes control plane component that embeds cloud-specific control logic. The cloud controller manager lets you link your cluster into your cloud provider's API, and separates out the components that interact with that cloud platform from components that only interact with your cluster. 
The cloud-controller-manager only runs controllers that are specific to your cloud provider. If you are running Kubernetes on your own premises, or in a learning environment inside your own PC, the cluster does not have a cloud controller manager. 
As with the kube-controller-manager, the cloud-controller-manager combines several logically independent control loops into a single binary that you run as a single process. You can scale horizontally (run more than one copy) to improve performance or to help tolerate failures. 
The following controllers can have cloud provider dependencies: 
- Node controller: For checking the cloud provider to determine if a node has been deleted in the cloud after it stops responding - Route controller: For setting up routes in the underlying cloud infrastructure - Service controller: For creating, updating and deleting cloud provider load balancers 
## Node components 
Node components run on every node, maintaining running pods and providing the Kubernetes runtime environment. 
### kubelet 
An agent that runs on each node in the cluster. It makes sure that containers are running in a Pod . 
The kubelet takes a set of PodSpecs that are provided through various mechanisms and ensures that the containers described in those PodSpecs are running and healthy. The kubelet doesn't manage containers which were not created by Kubernetes. 
### kube-proxy (optional) 

kube-proxy is a network proxy that runs on each node in your cluster, implementing part of the Kubernetes Service concept. 
kube-proxy maintains network rules on nodes. These network rules allow network communication to your Pods from network sessions inside or outside of your cluster. 
kube-proxy uses the operating system packet filtering layer if there is one and it's available. Otherwise, kube-proxy forwards the traffic itself. If you use a network plugin that implements packet forwarding for Services by itself, and providing equivalent behavior to kube-proxy, then you do not need to run kube-proxy on the nodes in your cluster. 
### Container runtime 
A fundamental component that empowers Kubernetes to run containers effectively. It is responsible for managing the execution and lifecycle of containers within the Kubernetes environment. 
Kubernetes supports container runtimes such as containerd , CRI-O , and any other implementation of the Kubernetes CRI (Container Runtime Interface) . 
## Addons 
Addons use Kubernetes resources ( DaemonSet , Deployment , etc) to implement cluster features. Because these are providing cluster-level features, namespaced resources for addons belong within the kube-systemnamespace. 
Selected addons are described below; for an extended list of available addons, please see Addons . 
### DNS 
While the other addons are not strictly required, all Kubernetes clusters should have cluster DNS , as many examples rely on it. 
Cluster DNS is a DNS server, in addition to the other DNS server(s) in your environment, which serves DNS records for Kubernetes services. 
Containers started by Kubernetes automatically include this DNS server in their DNS searches. 
### Web UI (Dashboard) 
Dashboard is a general purpose, web-based UI for Kubernetes clusters. It allows users to manage and troubleshoot applications running in the cluster, as well as the cluster itself. 
### Container resource monitoring 
Container Resource Monitoring records generic time-series metrics about containers in a central database, and provides a UI for browsing that data. 
### Cluster-level Logging 
A cluster-level logging mechanism is responsible for saving container logs to a central log store with a search/browsing interface. 
### Network plugins 
Network plugins are software components that implement the container network interface (CNI) specification. They are responsible for allocating IP addresses to pods and enabling them to communicate with each other within the cluster. 
## Architecture variations 
While the core components of Kubernetes remain consistent, the way they are deployed and managed can vary. Understanding these variations is crucial for designing and maintaining Kubernetes clusters that meet specific operational needs. 
### Control plane deployment options 
The control plane components can be deployed in several ways: Traditional deployment Control plane components run directly on dedicated machines or VMs, often managed as systemd services. Static Pods Control plane components are deployed as static Pods, managed by the kubelet on specific nodes. This is a common approach used by tools like kubeadm. Self-hosted The control plane runs as Pods within the Kubernetes cluster itself, managed by Deployments and StatefulSets or other Kubernetes primitives. Managed Kubernetes services Cloud providers often abstract away the control plane, managing its components as part of their service offering. 
### Workload placement considerations 
The placement of workloads, including the control plane components, can vary based on cluster size, performance requirements, and operational policies: 
- In smaller or development clusters, control plane components and user workloads might run on the same nodes. - Larger production clusters often dedicate specific nodes to control plane components, separating them from user workloads. - Some organizations run critical add-ons or monitoring tools on control plane nodes. 
### Cluster management tools 
Tools like kubeadm, kops, and Kubespray offer different approaches to deploying and managing clusters, each with its own method of component layout and management. 
### Customization and extensibility 
Kubernetes architecture allows for significant customization: 
- Custom schedulers can be deployed to work alongside the default Kubernetes scheduler or to replace it entirely. - API servers can be extended with CustomResourceDefinitions and API Aggregation. - Cloud providers can integrate deeply with Kubernetes using the cloud-controller-manager. 
The flexibility of Kubernetes architecture allows organizations to tailor their clusters to specific needs, balancing factors such as operational complexity, performance, and management overhead. 
## What's next 
Learn more about the following: 
- Nodes and their communication with the control plane. - Kubernetes controllers . - Garbage collection of cluster objects. - kube-scheduler which is the default scheduler for Kubernetes. - Etcd's official documentation . - Several container runtimes in Kubernetes. - Integrating with cloud providers using cloud-controller-manager . - kubectl commands. 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified March 27, 2026 at 11:01 PM PST: fix architecture page orphan link (61fcd63f2a) 
- - - - - - 

- - - - 

#### 📄 Sub-topic: [https://kubernetes.io/docs/concepts/architecture/cgroups](https://kubernetes.io/docs/concepts/architecture/cgroups)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - Français (French)   - Deutsch (German)   - Bahasa Indonesia (Indonesian)   - 日本語 (Japanese)   - 한국어 (Korean)   - Español (Spanish)   - বাংলা (Bengali)   - हिन्दी (Hindi)   - Italiano (Italian)   - فارسی (Persian)   - Polski (Polish)   - Português (Portuguese)   - Русский (Russian)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# About cgroup v2 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- - 
  -   -   - - - - 
- - - - 
# About cgroup v2 
On Linux, control groups constrain resources that are allocated to processes. 
The kubelet and the underlying container runtime need to interface with cgroups to enforce resource management for pods and containers which includes cpu/memory requests and limits for containerized workloads. 
There are two versions of cgroups in Linux: cgroup v1 and cgroup v2. cgroup v2 is the new generation of the cgroupAPI. 
## What is cgroup v2? Feature state: Stable since Kubernetes v1.25 
cgroup v2 is the next version of the Linux cgroupAPI. cgroup v2 provides a unified control system with enhanced resource management capabilities. 
cgroup v2 offers several improvements over cgroup v1, such as the following: 
- Single unified hierarchy design in API - Safer sub-tree delegation to containers - Newer features like Pressure Stall Information - Enhanced resource allocation management and isolation across multiple resources 
  - Unified accounting for different types of memory allocations (network memory, kernel memory, etc)   - Accounting for non-immediate resource changes such as page cache write backs 
Some Kubernetes features exclusively use cgroup v2 for enhanced resource management and isolation. For example, the MemoryQoS feature improves memory QoS and relies on cgroup v2 primitives. 
## Using cgroup v2 
The recommended way to use cgroup v2 is to use a Linux distribution that enables and uses cgroup v2 by default. 
To check if your distribution uses cgroup v2, refer to Identify cgroup version on Linux nodes . 
### Requirements 
cgroup v2 has the following requirements: 
- OS distribution enables cgroup v2 - Linux Kernel version is 5.8 or later - Container runtime supports cgroup v2. For example: 
  - containerd v1.4 and later   - cri-o v1.20 and later - The kubelet and the container runtime are configured to use the systemd cgroup driver 
### Linux Distribution cgroup v2 support 
For a list of Linux distributions that use cgroup v2, refer to the cgroup v2 documentation 
- Container Optimized OS (since M97) - Ubuntu (since 21.10, 22.04+ recommended) - Debian GNU/Linux (since Debian 11 bullseye) - Fedora (since 31) - Arch Linux (since April 2021) - RHEL and RHEL-like distributions (since 9) 
To check if your distribution is using cgroup v2, refer to your distribution's documentation or follow the instructions in Identify the cgroup version on Linux nodes . 
You can also enable cgroup v2 manually on your Linux distribution by modifying the kernel cmdline boot arguments. If your distribution uses GRUB, systemd.unified_cgroup_hierarchy=1should be added in GRUB_CMDLINE_LINUXunder /etc/default/grub, followed by sudo update-grub. However, the recommended approach is to use a distribution that already enables cgroup v2 by default. 
### Migrating to cgroup v2 
To migrate to cgroup v2, ensure that you meet the requirements , then upgrade to a kernel version that enables cgroup v2 by default. 
The kubelet automatically detects that the OS is running on cgroup v2 and performs accordingly with no additional configuration required. 
There should not be any noticeable difference in the user experience when switching to cgroup v2, unless users are accessing the cgroup file system directly, either on the node or from within the containers. 
cgroup v2 uses a different API than cgroup v1, so if there are any applications that directly access the cgroup file system, they need to be updated to newer versions that support cgroup v2. For example: 
- Some third-party monitoring and security agents may depend on the cgroup filesystem. Update these agents to versions that support cgroup v2. - If you run cAdvisor as a stand-alone DaemonSet for monitoring pods and containers, update it to v0.43.0 or later. - If you deploy Java applications, prefer to use versions which fully support cgroup v2: 
  - OpenJDK / HotSpot : jdk8u372, 11.0.16, 15 and later   - IBM Semeru Runtimes : 8.0.382.0, 11.0.20.0, 17.0.8.0, and later   - IBM Java : 8.0.8.6 and later - If you are using the uber-go/automaxprocs package, make sure the version you use is v1.5.1 or higher. - If you deploy Node.js applications, prefer to use versions that detect cgroup v2 memory limits. Node.js reads cgroup v2 memory limits (through libuv ) starting with Node.js v20.3.0. The v18 release line does not reliably detect cgroup v2 memory limits. Versions without this support may read the host's total memory instead of the limit applied to the pod, which can lead to an incorrectly sized heap and out-of-memory (OOM) terminations. On affected versions, set the heap size explicitly, for example with the --max-old-space-sizeflag. 
## Identify the cgroup version on Linux Nodes 
The cgroup version depends on the Linux distribution being used and the default cgroup version configured on the OS. To check which cgroup version your distribution uses, run the stat -fc %T /sys/fs/cgroup/command on the node: 
```
stat -fc %T /sys/fs/cgroup/

```

For cgroup v2, the output is cgroup2fs. 
For cgroup v1, the output is tmpfs.
## Deprecation of cgroup v1 Feature state: Deprecated since Kubernetes v1.35 
Kubernetes has deprecated cgroup v1. Removal will follow Kubernetes deprecation policy . 
Kubelet will no longer start on a cgroup v1 node by default. To disable this setting a cluster admin should set failCgroupV1to false in the kubelet configuration file . 
## What's next 
- Learn more about cgroups - Learn more about container runtime - Learn more about cgroup drivers 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified June 25, 2026 at 10:12 AM PST: cgroupv2 node.js update (fbe3e16b10) 
- - - - - - 

- - - - 

#### 📄 Sub-topic: [https://kubernetes.io/docs/concepts/architecture/cloud-controller](https://kubernetes.io/docs/concepts/architecture/cloud-controller)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - Français (French)   - Deutsch (German)   - Bahasa Indonesia (Indonesian)   - Italiano (Italian)   - 日本語 (Japanese)   - 한국어 (Korean)   - Português (Portuguese)   - Русский (Russian)   - Español (Spanish)   - Tiếng Việt (Vietnamese)   - বাংলা (Bengali)   - हिन्दी (Hindi)   - فارسی (Persian)   - Polski (Polish)   - Українська (Ukrainian) - Theme fixed for this page 
# Cloud Controller Manager 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- - 
  -   -   - - 
  -   -   -   - - 
- - - - 
# Cloud Controller Manager Feature state: Beta since Kubernetes v1.11 
Cloud infrastructure technologies let you run Kubernetes on public, private, and hybrid clouds. Kubernetes believes in automated, API-driven infrastructure without tight coupling between components. 

The cloud-controller-manager is a Kubernetes control plane component that embeds cloud-specific control logic. The cloud controller manager lets you link your cluster into your cloud provider's API, and separates out the components that interact with that cloud platform from components that only interact with your cluster. 
By decoupling the interoperability logic between Kubernetes and the underlying cloud infrastructure, the cloud-controller-manager component enables cloud providers to release features at a different pace compared to the main Kubernetes project. 
The cloud-controller-manager is structured using a plugin mechanism that allows different cloud providers to integrate their platforms with Kubernetes. 
## Design 

The cloud controller manager runs in the control plane as a replicated set of processes (usually, these are containers in Pods). Each cloud-controller-manager implements multiple controllers in a single process. 
#### Note: You can also run the cloud controller manager as a Kubernetes addon rather than as part of the control plane. 
## Cloud controller manager functions 
The controllers inside the cloud controller manager include: 
### Node controller 
The node controller is responsible for updating Node objects when new servers are created in your cloud infrastructure. The node controller obtains information about the hosts running inside your tenancy with the cloud provider. The node controller performs the following functions: 
- Update a Node object with the corresponding server's unique identifier obtained from the cloud provider API. - Annotating and labelling the Node object with cloud-specific information, such as the region the node is deployed into and the resources (CPU, memory, etc) that it has available. - Obtain the node's hostname and network addresses. - Verifying the node's health. In case a node becomes unresponsive, this controller checks with your cloud provider's API to see if the server has been deactivated / deleted / terminated. If the node has been deleted from the cloud, the controller deletes the Node object from your Kubernetes cluster. 
Some cloud provider implementations split this into a node controller and a separate node lifecycle controller. 
### Route controller 
The route controller is responsible for configuring routes in the cloud appropriately so that containers on different nodes in your Kubernetes cluster can communicate with each other. 
Depending on the cloud provider, the route controller might also allocate blocks of IP addresses for the Pod network. 
### Service controller 
Services integrate with cloud infrastructure components such as managed load balancers, IP addresses, network packet filtering, and target health checking. The service controller interacts with your cloud provider's APIs to set up load balancers and other infrastructure components when you declare a Service resource that requires them. 
## Authorization 
This section breaks down the access that the cloud controller manager requires on various API objects, in order to perform its operations. 
### Node controller 
The Node controller only works with Node objects. It requires full access to read and modify Node objects. 
v1/Node: 
- get - list - create - update - patch - watch - delete 
### Route controller 
The route controller listens to Node object creation and configures routes appropriately. It requires Get access to Node objects. 
v1/Node: 
- get 
### Service controller 
The service controller watches for Service object create , update and delete events and then configures load balancers for those Services appropriately. 
To access Services, it requires list , and watch access. To update Services, it requires patch and update access to the statussubresource. 
v1/Service: 
- list - get - watch - patch - update 
### Others 
The implementation of the core of the cloud controller manager requires access to create Event objects, and to ensure secure operation, it requires access to create ServiceAccounts. 
v1/Event: 
- create - patch - update 
v1/ServiceAccount: 
- create 
The RBAC ClusterRole for the cloud controller manager looks like: 
```
apiVersion:rbac.authorization.k8s.io/v1kind:ClusterRolemetadata:name:cloud-controller-managerrules:- apiGroups:- ""resources:- eventsverbs:- create- patch- update- apiGroups:- ""resources:- nodesverbs:- '*'- apiGroups:- ""resources:- nodes/statusverbs:- patch- apiGroups:- ""resources:- servicesverbs:- list- watch- apiGroups:- ""resources:- services/statusverbs:- patch- update- apiGroups:- ""resources:- serviceaccountsverbs:- create- apiGroups:- ""resources:- persistentvolumesverbs:- get- list- update- watch
```

## What's next 
- 
Cloud Controller Manager Administration has instructions on running and managing the cloud controller manager. - 
To upgrade a HA control plane to use the cloud controller manager, see Migrate Replicated Control Plane To Use Cloud Controller Manager . - 
Want to know how to implement your own cloud controller manager, or extend an existing project? 
  - The cloud controller manager uses Go interfaces, specifically, CloudProviderinterface defined in cloud.gofrom kubernetes/cloud-provider to allow implementations from any cloud to be plugged in.   - The implementation of the shared controllers highlighted in this document (Node, Route, and Service), and some scaffolding along with the shared cloudprovider interface, is part of the Kubernetes core. Implementations specific to cloud providers are outside the core of Kubernetes and implement the CloudProviderinterface.   - For more information about developing plugins, see Developing Cloud Controller Manager . 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified May 30, 2026 at 6:09 PM PST: Add theme_lock front matter to concepts overview pages (6e5065edcf) 
- - - - - - 

- - - - 

#### 📄 Sub-topic: [https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication](https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - Français (French)   - Deutsch (German)   - Bahasa Indonesia (Indonesian)   - Italiano (Italian)   - 日本語 (Japanese)   - 한국어 (Korean)   - Português (Portuguese)   - Русский (Russian)   - Español (Spanish)   - বাংলা (Bengali)   - हिन्दी (Hindi)   - فارسی (Persian)   - Polski (Polish)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# Communication between Nodes and the Control Plane 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- - 
  -   -   -   - - 
- - - - 
# Communication between Nodes and the Control Plane 
This document catalogs the communication paths between the API server and the Kubernetes cluster . The intent is to allow users to customize their installation to harden the network configuration such that the cluster can be run on an untrusted network (or on fully public IPs on a cloud provider). 
## Node to Control Plane 
Kubernetes has a "hub-and-spoke" API pattern. All API usage from nodes (or the pods they run) terminates at the API server. None of the other control plane components are designed to expose remote services. The API server is configured to listen for remote connections on a secure HTTPS port (typically 443) with one or more forms of client authentication enabled. One or more forms of authorization should be enabled, especially if anonymous requests or service account tokens are allowed. 
Nodes should be provisioned with the public root certificate for the cluster such that they can connect securely to the API server along with valid client credentials. A good approach is that the client credentials provided to the kubelet are in the form of a client certificate. See kubelet TLS bootstrapping for automated provisioning of kubelet client certificates. 
Pods that wish to connect to the API server can do so securely by leveraging a service account so that Kubernetes will automatically inject the public root certificate and a valid bearer token into the pod when it is instantiated. The kubernetesservice (in defaultnamespace) is configured with a virtual IP address that is redirected (via kube-proxy) to the HTTPS endpoint on the API server. 
The control plane components also communicate with the API server over the secure port. 
As a result, the default operating mode for connections from the nodes and pod running on the nodes to the control plane is secured by default and can run over untrusted and/or public networks. 
## Control plane to node 
There are two primary communication paths from the control plane (the API server) to the nodes. The first is from the API server to the kubelet process which runs on each node in the cluster. The second is from the API server to any node, pod, or service through the API server's proxy functionality. 
### API server to kubelet 
The connections from the API server to the kubelet are used for: 
- Fetching logs for pods. - Attaching (usually through kubectl) to running pods. - Providing the kubelet's port-forwarding functionality. 
These connections terminate at the kubelet's HTTPS endpoint. By default, the API server does not verify the kubelet's serving certificate, which makes the connection subject to man-in-the-middle attacks and unsafe to run over untrusted and/or public networks. 
To verify this connection, use the --kubelet-certificate-authorityflag to provide the API server with a root certificate bundle to use to verify the kubelet's serving certificate. 
If that is not possible, use SSH tunneling between the API server and kubelet if required to avoid connecting over an untrusted or public network. 
Finally, Kubelet authentication and/or authorization should be enabled to secure the kubelet API. 
### API server to nodes, pods, and services 
The connections from the API server to a node, pod, or service default to plain HTTP connections and are therefore neither authenticated nor encrypted. They can be run over a secure HTTPS connection by prefixing https:to the node, pod, or service name in the API URL, but they will not validate the certificate provided by the HTTPS endpoint nor provide client credentials. So while the connection will be encrypted, it will not provide any guarantees of integrity. These connections are not currently safe to run over untrusted or public networks. 
### SSH tunnels 
Kubernetes supports SSH tunnels to protect the control plane to nodes communication paths. In this configuration, the API server initiates an SSH tunnel to each node in the cluster (connecting to the SSH server listening on port 22) and passes all traffic destined for a kubelet, node, pod, or service through the tunnel. This tunnel ensures that the traffic is not exposed outside of the network in which the nodes are running. 
#### Note: SSH tunnels are currently deprecated, so you shouldn't opt to use them unless you know what you are doing. The Konnectivity service is a replacement for this communication channel. 
### Konnectivity service Feature state: Beta since Kubernetes v1.18 
As a replacement to the SSH tunnels, the Konnectivity service provides TCP level proxy for the control plane to cluster communication. The Konnectivity service consists of two parts: the Konnectivity server in the control plane network and the Konnectivity agents in the nodes network. The Konnectivity agents initiate connections to the Konnectivity server and maintain the network connections. After enabling the Konnectivity service, all control plane to nodes traffic goes through these connections. 
Follow the Konnectivity service task to set up the Konnectivity service in your cluster. 
## What's next 
- Read about the Kubernetes control plane components - Learn more about Hubs and Spoke model - Learn how to Secure a Cluster - Learn more about the Kubernetes API - Set up Konnectivity service - Use Port Forwarding to Access Applications in a Cluster - Learn how to Fetch logs for Pods , use kubectl port-forward 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified September 01, 2024 at 1:54 AM PST: Fix broken links from "overview/components/#..." to "architecture/#..." (#47724) (7e64c2db82) 
- - - - - - 

- - - - 

#### 📄 Sub-topic: [https://kubernetes.io/docs/concepts/architecture/controller](https://kubernetes.io/docs/concepts/architecture/controller)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - Français (French)   - Deutsch (German)   - Bahasa Indonesia (Indonesian)   - Italiano (Italian)   - 日本語 (Japanese)   - 한국어 (Korean)   - Português (Portuguese)   - Русский (Russian)   - Español (Spanish)   - বাংলা (Bengali)   - हिन्दी (Hindi)   - فارسی (Persian)   - Polski (Polish)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# Controllers 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- 
  -   - - - - - 
- - - - 
# Controllers 
In robotics and automation, a control loop is a non-terminating loop that regulates the state of a system. 
Here is one example of a control loop: a thermostat in a room. 
When you set the temperature, that's telling the thermostat about your desired state . The actual room temperature is the current state . The thermostat acts to bring the current state closer to the desired state, by turning equipment on or off. In Kubernetes, controllers are control loops that watch the state of your cluster , then make or request changes where needed. Each controller tries to move the current cluster state closer to the desired state. 
## Controller pattern 
A controller tracks at least one Kubernetes resource type. These objects have a spec field that represents the desired state. The controller(s) for that resource are responsible for making the current state come closer to that desired state. 
The controller might carry the action out itself; more commonly, in Kubernetes, a controller will send messages to the API server that have useful side effects. You'll see examples of this below. 
### Control via API server 
The Job controller is an example of a Kubernetes built-in controller. Built-in controllers manage state by interacting with the cluster API server. 
Job is a Kubernetes resource that runs a Pod , or perhaps several Pods, to carry out a task and then stop. 
(Once scheduled , Pod objects become part of the desired state for a kubelet). 
When the Job controller sees a new task it makes sure that, somewhere in your cluster, the kubelets on a set of Nodes are running the right number of Pods to get the work done. The Job controller does not run any Pods or containers itself. Instead, the Job controller tells the API server to create or remove Pods. Other components in the control plane act on the new information (there are new Pods to schedule and run), and eventually the work is done. 
After you create a new Job, the desired state is for that Job to be completed. The Job controller makes the current state for that Job be nearer to your desired state: creating Pods that do the work you wanted for that Job, so that the Job is closer to completion. 
Controllers also update the objects that configure them. For example: once the work is done for a Job, the Job controller updates that Job object to mark it Finished. 
(This is a bit like how some thermostats turn a light off to indicate that your room is now at the temperature you set). 
### Direct control 
In contrast with Job, some controllers need to make changes to things outside of your cluster. 
For example, if you use a control loop to make sure there are enough Nodes in your cluster, then that controller needs something outside the current cluster to set up new Nodes when needed. 
Controllers that interact with external state find their desired state from the API server, then communicate directly with an external system to bring the current state closer in line. 
(There actually is a controller that horizontally scales the nodes in your cluster.) 
The important point here is that the controller makes some changes to bring about your desired state, and then reports the current state back to your cluster's API server. Other control loops can observe that reported data and take their own actions. 
In the thermostat example, if the room is very cold then a different controller might also turn on a frost protection heater. With Kubernetes clusters, the control plane indirectly works with IP address management tools, storage services, cloud provider APIs, and other services by extending Kubernetes to implement that. 
## Desired versus current state 
Kubernetes takes a cloud-native view of systems, and is able to handle constant change. 
Your cluster could be changing at any point as work happens and control loops automatically fix failures. This means that, potentially, your cluster never reaches a stable state. 
As long as the controllers for your cluster are running and able to make useful changes, it doesn't matter if the overall state is stable or not. 
## Design 
As a tenet of its design, Kubernetes uses lots of controllers that each manage a particular aspect of cluster state. Most commonly, a particular control loop (controller) uses one kind of resource as its desired state, and has a different kind of resource that it manages to make that desired state happen. For example, a controller for Jobs tracks Job objects (to discover new work) and Pod objects (to run the Jobs, and then to see when the work is finished). In this case something else creates the Jobs, whereas the Job controller creates Pods. 
It's useful to have simple controllers rather than one, monolithic set of control loops that are interlinked. Controllers can fail, so Kubernetes is designed to allow for that. 
#### Note: 
There can be several controllers that create or update the same kind of object. Behind the scenes, Kubernetes controllers make sure that they only pay attention to the resources linked to their controlling resource. 
For example, you can have Deployments and Jobs; these both create Pods. The Job controller does not delete the Pods that your Deployment created, because there is information ( labels ) the controllers can use to tell those Pods apart. 
## Ways of running controllers 
Kubernetes comes with a set of built-in controllers that run inside the kube-controller-manager . These built-in controllers provide important core behaviors. 
The Deployment controller and Job controller are examples of controllers that come as part of Kubernetes itself ("built-in" controllers). Kubernetes lets you run a resilient control plane, so that if any of the built-in controllers were to fail, another part of the control plane will take over the work. 
You can find controllers that run outside the control plane, to extend Kubernetes. Or, if you want, you can write a new controller yourself. You can run your own controller as a set of Pods, or externally to Kubernetes. What fits best will depend on what that particular controller does. 
## What's next 
- Read about the Kubernetes control plane - Discover some of the basic Kubernetes objects - Learn more about the Kubernetes API - If you want to write your own controller, see Kubernetes extension patterns and the sample-controller repository. 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified September 01, 2024 at 1:54 AM PST: Fix broken links from "overview/components/#..." to "architecture/#..." (#47724) (7e64c2db82) 
- - - - - - 

- - - - 

#### 📄 Sub-topic: [https://kubernetes.io/docs/concepts/architecture/garbage-collection](https://kubernetes.io/docs/concepts/architecture/garbage-collection)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - Français (French)   - 日本語 (Japanese)   - 한국어 (Korean)   - Português (Portuguese)   - Русский (Russian)   - বাংলা (Bengali)   - Deutsch (German)   - हिन्दी (Hindi)   - Bahasa Indonesia (Indonesian)   - Italiano (Italian)   - فارسی (Persian)   - Polski (Polish)   - Español (Spanish)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# Garbage Collection 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- - 
  -   -   - - 
  -   - - - 
- - - - 
# Garbage Collection 
Garbage collection is a collective term for the various mechanisms Kubernetes uses to clean up cluster resources. This allows the clean up of resources like the following: 
- Terminated pods - Completed Jobs - Objects without owner references - Unused containers and container images - Dynamically provisioned PersistentVolumes with a StorageClass reclaim policy of Delete - Stale or expired CertificateSigningRequests (CSRs) - Nodes deleted in the following scenarios: 
  - On a cloud when the cluster uses a cloud controller manager   - On-premises when the cluster uses an addon similar to a cloud controller manager - Node Lease objects 
## Owners and dependents 
Many objects in Kubernetes link to each other through owner references . Owner references tell the control plane which objects are dependent on others. Kubernetes uses owner references to give the control plane, and other API clients, the opportunity to clean up related resources before deleting an object. In most cases, Kubernetes manages owner references automatically. 
Ownership is different from the labels and selectors mechanism that some resources also use. For example, consider a Service that creates EndpointSliceobjects. The Service uses labels to allow the control plane to determine which EndpointSliceobjects are used for that Service. In addition to the labels, each EndpointSlicethat is managed on behalf of a Service has an owner reference. Owner references help different parts of Kubernetes avoid interfering with objects they don’t control. 
#### Note: 
Cross-namespace owner references are disallowed by design. Namespaced dependents can specify cluster-scoped or namespaced owners. A namespaced owner must exist in the same namespace as the dependent. If it does not, the owner reference is treated as absent, and the dependent is subject to deletion once all owners are verified absent. 
Cluster-scoped dependents can only specify cluster-scoped owners. In v1.20+, if a cluster-scoped dependent specifies a namespaced kind as an owner, it is treated as having an unresolvable owner reference, and is not able to be garbage collected. 
In v1.20+, if the garbage collector detects an invalid cross-namespace ownerReference, or a cluster-scoped dependent with an ownerReferencereferencing a namespaced kind, a warning Event with a reason of OwnerRefInvalidNamespaceand an involvedObjectof the invalid dependent is reported. You can check for that kind of Event by running kubectl get events -A --field-selector=reason=OwnerRefInvalidNamespace. 
## Cascading deletion 
Kubernetes checks for and deletes objects that no longer have owner references, like the pods left behind when you delete a ReplicaSet. When you delete an object, you can control whether Kubernetes deletes the object's dependents automatically, in a process called cascading deletion . There are two types of cascading deletion, as follows: 
- Foreground cascading deletion - Background cascading deletion 
You can also control how and when garbage collection deletes resources that have owner references using Kubernetes finalizers . 
### Foreground cascading deletion 
In foreground cascading deletion, the owner object you're deleting first enters a deletion in progress state. In this state, the following happens to the owner object: 
- The Kubernetes API server sets the object's metadata.deletionTimestampfield to the time the object was marked for deletion. - The Kubernetes API server also sets the metadata.finalizersfield to foregroundDeletion. - The object remains visible through the Kubernetes API until the deletion process is complete. 
After the owner object enters the deletion in progress state, the controller deletes dependents it knows about. After deleting all the dependent objects it knows about, the controller deletes the owner object. At this point, the object is no longer visible in the Kubernetes API. 
During foreground cascading deletion, the only dependents that block owner deletion are those that have the ownerReference.blockOwnerDeletion=truefield and are in the garbage collection controller cache. The garbage collection controller cache may not contain objects whose resource type cannot be listed / watched successfully, or objects that are created concurrent with deletion of an owner object. See Use foreground cascading deletion to learn more. 
### Background cascading deletion 
In background cascading deletion, the Kubernetes API server deletes the owner object immediately and the garbage collector controller (custom or default) cleans up the dependent objects in the background. If a finalizer exists, it ensures that objects are not deleted until all necessary clean-up tasks are completed. By default, Kubernetes uses background cascading deletion unless you manually use foreground deletion or choose to orphan the dependent objects. 
See Use background cascading deletion to learn more. 
### Orphaned dependents 
When Kubernetes deletes an owner object, the dependents left behind are called orphan objects. By default, Kubernetes deletes dependent objects. To learn how to override this behaviour, see Delete owner objects and orphan dependents . 
## Garbage collection of unused containers and images 
The kubelet performs garbage collection on unused images every five minutes and on unused containers every minute. You should avoid using external garbage collection tools, as these can break the kubelet behavior and remove containers that should exist. 
To configure options for unused container and image garbage collection, tune the kubelet using a configuration file and change the parameters related to garbage collection using the KubeletConfigurationresource type. 
### Container image lifecycle 
Kubernetes manages the lifecycle of all images through its image manager , which is part of the kubelet, with the cooperation of cadvisor . The kubelet considers the following disk usage limits when making garbage collection decisions: 
- HighThresholdPercent- LowThresholdPercent
Disk usage above the configured HighThresholdPercentvalue triggers garbage collection, which deletes images in order based on the last time they were used, starting with the oldest first. The kubelet deletes images until disk usage reaches the LowThresholdPercentvalue. 
#### Garbage collection for unused container images 
You can specify the maximum time a local image can be unused for, regardless of disk usage. This is a kubelet setting that you configure for each node. 
To configure the setting, you need to set a value for the imageMaximumGCAgefield in the kubelet configuration file. 
The value is specified as a Kubernetes duration . See duration in the glossary for more details. 
For example, you can set the configuration field to 12h45m, which means 12 hours and 45 minutes. 
#### Note: This feature does not track image usage across kubelet restarts. If the kubelet is restarted, the tracked image age is reset, causing the kubelet to wait the full imageMaximumGCAgeduration before qualifying images for garbage collection based on image age. 
### Container garbage collection 
The kubelet garbage collects unused containers based on the following variables, which you can define: 
- MinAge: the minimum age at which the kubelet can garbage collect a container. Disable by setting to 0. - MaxPerPodContainer: the maximum number of dead containers each Pod can have. Disable by setting to less than 0. - MaxContainers: the maximum number of dead containers the cluster can have. Disable by setting to less than 0. 
In addition to these variables, the kubelet garbage collects unidentified and deleted containers, typically starting with the oldest first. 
MaxPerPodContainerand MaxContainersmay potentially conflict with each other in situations where retaining the maximum number of containers per Pod ( MaxPerPodContainer) would go outside the allowable total of global dead containers ( MaxContainers). In this situation, the kubelet adjusts MaxPerPodContainerto address the conflict. A worst-case scenario would be to downgrade MaxPerPodContainerto 1and evict the oldest containers. Additionally, containers owned by pods that have been deleted are removed once they are older than MinAge. 
#### Note: The kubelet only garbage collects the containers it manages. 
## Configuring garbage collection 
You can tune garbage collection of resources by configuring options specific to the controllers managing those resources. The following pages show you how to configure garbage collection: 
- Configuring cascading deletion of Kubernetes objects - Configuring cleanup of finished Jobs 
## What's next 
- Learn more about ownership of Kubernetes objects . - Learn more about Kubernetes finalizers . - Learn about the TTL controller that cleans up finished Jobs. 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified October 20, 2025 at 3:58 PM PST: 4210: mark as stable (c6459d7dca) 
- - - - - - 

- - - - 

#### 📄 Sub-topic: [https://kubernetes.io/docs/concepts/architecture/leases](https://kubernetes.io/docs/concepts/architecture/leases)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - Français (French)   - 日本語 (Japanese)   - 한국어 (Korean)   - Español (Spanish)   - Tiếng Việt (Vietnamese)   - বাংলা (Bengali)   - Deutsch (German)   - हिन्दी (Hindi)   - Bahasa Indonesia (Indonesian)   - Italiano (Italian)   - فارسی (Persian)   - Polski (Polish)   - Português (Portuguese)   - Русский (Russian)   - Українська (Ukrainian) - 
  - Light   - Dark   - Auto 
# Leases 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- - 
  - - - 
- - - - 
# Leases 
Distributed systems often have a need for leases , which provide a mechanism to lock shared resources and coordinate activity between members of a set. In Kubernetes, the lease concept is represented by Lease objects in the coordination.k8s.ioAPI Group , which are used for system-critical capabilities such as node heartbeats and component-level leader election. 
## Node heartbeats 
Kubernetes uses the Lease API to communicate kubelet node heartbeats to the Kubernetes API server. For every Node, there is a Leaseobject with a matching name in the kube-node-leasenamespace. Under the hood, every kubelet heartbeat is an update request to this Leaseobject, updating the spec.renewTimefield for the Lease. The Kubernetes control plane uses the time stamp of this field to determine the availability of this Node. 
See Node Lease objects for more details. 
## Leader election 
Kubernetes also uses Leases to ensure only one instance of a component is running at any given time. This is used by control plane components like kube-controller-managerand kube-schedulerin HA configurations, where only one instance of the component should be actively running while the other instances are on stand-by. 
Read coordinated leader election to learn about how Kubernetes builds on the Lease API to select which component instance acts as leader. 
### Kube controller manager lock release on exit Feature state: Alpha since Kubernetes v1.36; disabled by default More information about this feature 
To use this feature, you (or a cluster administrator) will need to enable the ControllerManagerReleaseLeaderElectionLockOnExit feature gate for all relevant components in your cluster. 
See Enable Or Disable Feature Gates for more information. 
When the ControllerManagerReleaseLeaderElectionLockOnExitfeature gate is enabled, the kube-controller-manageractively releases its leader election lock during leader transitions, rather than waiting for the lock's TTL to expire. This allows a new leader to be elected more quickly, reducing leader transition latency. 
## API server identity Feature state: Beta since Kubernetes v1.26; enabled by default 
Starting in Kubernetes v1.26, each kube-apiserveruses the Lease API to publish its identity to the rest of the system. While not particularly useful on its own, this provides a mechanism for clients to discover how many instances of kube-apiserverare operating the Kubernetes control plane. Existence of kube-apiserver leases enables future capabilities that may require coordination between each kube-apiserver. 
You can inspect Leases owned by each kube-apiserver by checking for lease objects in the kube-systemnamespace with the name apiserver-<sha256-hash>. Alternatively you can use the label selector apiserver.kubernetes.io/identity=kube-apiserver: 
```
kubectl -n kube-system get lease -l apiserver.kubernetes.io/identity=kube-apiserver

```

```
NAME                                        HOLDER                                                                           AGE
apiserver-07a5ea9b9b072c4a5f3d1c3702        apiserver-07a5ea9b9b072c4a5f3d1c3702_0c8914f7-0f35-440e-8676-7844977d3a05        5m33s
apiserver-7be9e061c59d368b3ddaf1376e        apiserver-7be9e061c59d368b3ddaf1376e_84f2a85d-37c1-4b14-b6b9-603e62e4896f        4m23s
apiserver-1dfef752bcb36637d2763d1868        apiserver-1dfef752bcb36637d2763d1868_c5ffa286-8a9a-45d4-91e7-61118ed58d2e        4m43s

```

The SHA256 hash used in the lease name is based on the OS hostname as seen by that API server. Each kube-apiserver should be configured to use a hostname that is unique within the cluster. New instances of kube-apiserver that use the same hostname will take over existing Leases using a new holder identity, as opposed to instantiating new Lease objects. You can check the hostname used by kube-apiserver by checking the value of the kubernetes.io/hostnamelabel: 
```
kubectl -n kube-system get lease apiserver-07a5ea9b9b072c4a5f3d1c3702 -o yaml

```

```
apiVersion:coordination.k8s.io/v1kind:Leasemetadata:creationTimestamp:"2023-07-02T13:16:48Z"labels:apiserver.kubernetes.io/identity:kube-apiserverkubernetes.io/hostname:master-1name:apiserver-07a5ea9b9b072c4a5f3d1c3702namespace:kube-systemresourceVersion:"334899"uid:90870ab5-1ba9-4523-b215-e4d4e662acb1spec:holderIdentity:apiserver-07a5ea9b9b072c4a5f3d1c3702_0c8914f7-0f35-440e-8676-7844977d3a05leaseDurationSeconds:3600renewTime:"2023-07-04T21:58:48.065888Z"
```

Expired leases from kube-apiservers that no longer exist are garbage collected by new kube-apiservers after 1 hour. 
You can disable API server identity leases by disabling the APIServerIdentityfeature gate . 
## Workloads 
Your own workload can define its own use of Leases. For example, you might run a custom controller where a primary or leader member performs operations that its peers do not. You define a Lease so that the controller replicas can select or elect a leader, using the Kubernetes API for coordination. If you do use a Lease, it's a good practice to define a name for the Lease that is obviously linked to the product or component. For example, if you have a component named Example Foo, use a Lease named example-foo. 
If a cluster operator or another end user could deploy multiple instances of a component, select a name prefix and pick a mechanism (such as hash of the name of the Deployment) to avoid name collisions for the Leases. 
You can use another approach so long as it achieves the same outcome: different software products do not conflict with one another. 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified March 31, 2026 at 1:39 PM PST: Add docs for KEP-5366 ControllerManagerReleaseLeaderElectionLockOnExit feature gate (70b8f1d1c4) 
- - - - - - 

- - - - 

#### 📄 Sub-topic: [https://kubernetes.io/docs/concepts/architecture/mixed-version-proxy](https://kubernetes.io/docs/concepts/architecture/mixed-version-proxy)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - Français (French)   - 日本語 (Japanese)   - Tiếng Việt (Vietnamese)   - বাংলা (Bengali)   - Deutsch (German)   - हिन्दी (Hindi)   - Bahasa Indonesia (Indonesian)   - Italiano (Italian)   - 한국어 (Korean)   - فارسی (Persian)   - Polski (Polish)   - Português (Portuguese)   - Русский (Russian)   - Español (Spanish)   - Українська (Ukrainian) - 
  - Light   - Dark   - Auto 
# Mixed Version Proxy 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- 
  -   - - - 
  - 
- - - - 
# Mixed Version Proxy Feature state: Beta since Kubernetes v1.36; enabled by default 
Kubernetes 1.37 includes a beta feature that lets an API Server proxy resource requests to other peer API servers. It also lets clients get a holistic view of resources served across the entire cluster through discovery. This is useful when there are multiple API servers running different versions of Kubernetes in one cluster (for example, during a long-lived rollout to a new release of Kubernetes). 
This enables cluster administrators to configure highly available clusters that can be upgraded more safely, by : 
- ensuring that controllers relying on discovery to show a comprehensive list of resources for important tasks always get the complete view of all resources. We call this complete cluster-wide discovery Peer-aggregated discovery . - directing resource requests (made during the upgrade) to the correct kube-apiserver. This proxying prevents users from seeing unexpected 404 Not Found errors that stem from the upgrade process. This mechanism is called the Mixed Version Proxy . 
## Enabling Peer-aggregated Discovery and Mixed Version Proxy 
Ensure that UnknownVersionInteroperabilityProxyfeature gate is enabled when you start the API Server : 
```
kube-apiserver \
--feature-gates=UnknownVersionInteroperabilityProxy=true\
# required command line arguments for this feature--peer-ca-file=<path to kube-apiserver CA cert>
--proxy-client-cert-file=<path to aggregator proxy cert>,
--proxy-client-key-file=<path to aggregator proxy key>,
--requestheader-client-ca-file=<path to aggregator CA cert>,
# requestheader-allowed-names can be set to blank to allow any Common Name--requestheader-allowed-names=<valid Common Names to verify proxy client cert against>,
# optional flags for this feature--peer-advertise-ip=`IP of this kube-apiserver that should be used by peers to proxy requests`--peer-advertise-port=`port of this kube-apiserver that should be used by peers to proxy requests`# …and other flags as usual
```

### Proxy transport and authentication between API servers 
- 
The source kube-apiserver reuses the existing APIserver client authentication flags --proxy-client-cert-fileand --proxy-client-key-fileto present its identity that will be verified by its peer (the destination kube-apiserver). The destination API server verifies that peer connection based on the configuration you specify using the --requestheader-client-ca-filecommand line argument. - 
To authenticate the destination server's serving certs, you must configure a certificate authority bundle by specifying the --peer-ca-filecommand line argument to the source API server. 
### Configuration for peer API server connectivity 
To set the network location of a kube-apiserver that peers will use to proxy requests, use the --peer-advertise-ipand --peer-advertise-portcommand line arguments to kube-apiserver or specify these fields in the API server configuration file. If these flags are unspecified, peers will use the value from either --advertise-addressor --bind-addresscommand line argument to the kube-apiserver. If those too, are unset, the host's default interface is used. 
## Peer-aggregated discovery 
When you enable the feature, discovery requests are automatically enabled to serve a comprehensive discovery document (listing all resources served by any apiserver in the cluster) by default. 
If you would like to request a non peer-aggregated discovery document, you can indicate so by adding the following Accept header to the discovery request: 
```
application/json;g=apidiscovery.k8s.io;v=v2;as=APIGroupDiscoveryList;profile=nopeer

```

#### Note: Peer-aggregated discovery is only supported for Aggregated Discovery requests to the /apisendpoint and not for Unaggregated (Legacy) Discovery requests. 
## Mixed version proxying 
When you enable mixed version proxying, the aggregation layer loads a special filter that does the following: 
- When a resource request reaches an API server that cannot serve that API (either because it is at a version pre-dating the introduction of the API or the API is turned off on the API server) the API server attempts to send the request to a peer API server that can serve the requested API. It does so by identifying API groups / versions / resources that the local server doesn't recognise, and tries to proxy those requests to a peer API server that is capable of handling the request. - If the peer API server fails to respond, the source API server responds with 503 ("Service Unavailable") error. 
### How it works under the hood 
When an API Server receives a resource request, it first checks which API servers can serve the requested resource. This check happens using the non peer-aggregated discovery document. 
- 
If the resource is listed in the non peer-aggregated discovery document retrieved from the API server that received the request(for example, GET /api/v1/pods/some-pod), the request is handled locally. - 
If the resource in a request (for example, GET /apis/resource.k8s.io/v1beta1/resourceclaims) is not found in the non peer-aggregated discovery document retrieved from the API server trying to handle the request (the handling API server ), likely because the resource.k8s.io/v1beta1API was introduced in a newer Kubernetes version and the handling API server is running an older version that does not support it, then the handling API server fetches the peer API servers that do serve the relevant API group / version / resource ( resource.k8s.io/v1beta1/resourceclaimsin this case) by checking the non peer-aggregated discovery documents from all peer API servers. The handling API server then proxies the request to one of the matching peer kube-apiservers that are aware of the requested resource. - 
If there is no peer known for that API group / version / resource, the handling API server passes the request to its own handler chain which should eventually return a 404 ("Not Found") response. - 
If the handling API server has identified and selected a peer API server, but that peer fails to respond (for reasons such as network connectivity issues, or a data race between the request being received and a controller registering the peer's info into the control plane), then the handling API server responds with a 503 ("Service Unavailable") error. 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified February 25, 2026 at 4:10 PM PST: Doc update about MVP graduation to beta in 1.36 (3370ba38de) 
- - - - - - 

- - - - 

#### 📄 Sub-topic: [https://kubernetes.io/docs/concepts/architecture/nodes](https://kubernetes.io/docs/concepts/architecture/nodes)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - Français (French)   - Deutsch (German)   - Bahasa Indonesia (Indonesian)   - 日本語 (Japanese)   - 한국어 (Korean)   - Português (Portuguese)   - Русский (Russian)   - Español (Spanish)   - বাংলা (Bengali)   - हिन्दी (Hindi)   - Italiano (Italian)   - فارسی (Persian)   - Polski (Polish)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# Nodes 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- 
  -   -   - - - - 
  - - - - 
- - - - 
# Nodes 
Kubernetes runs your workload by placing containers into Pods to run on Nodes . A node may be a virtual or physical machine, depending on the cluster. Each node is managed by the control plane and contains the services necessary to run Pods . 
Typically you have several nodes in a cluster; in a learning or resource-limited environment, you might have only one node. 
The components on a node include the kubelet , a container runtime , and the kube-proxy . 
## Management 
There are two main ways to have Nodes added to the API server : 
- The kubelet on a node self-registers to the control plane - You (or another human user) manually add a Node object 
After you create a Node object , or the kubelet on a node self-registers, the control plane checks whether the new Node object is valid. For example, if you try to create a Node from the following JSON manifest: 
```
{"kind":"Node","apiVersion":"v1","metadata":{"name":"10.240.79.157","labels":{"name":"my-first-k8s-node"}}}
```

Kubernetes creates a Node object internally (the representation). Kubernetes checks that a kubelet has registered to the API server that matches the metadata.namefield of the Node. If the node is healthy (i.e. all necessary services are running), then it is eligible to run a Pod. Otherwise, that node is ignored for any cluster activity until it becomes healthy. 
#### Note: 
Kubernetes keeps the object for the invalid Node and continues checking to see whether it becomes healthy. 
You, or a controller , must explicitly delete the Node object to stop that health checking. 
The name of a Node object must be a valid DNS subdomain name . 
### Node name uniqueness 
The name identifies a Node. Two Nodes cannot have the same name at the same time. Kubernetes also assumes that a resource with the same name is the same object. In the case of a Node, it is implicitly assumed that an instance using the same name will have the same state (e.g. network settings, root disk contents) and attributes like node labels. This may lead to inconsistencies if an instance was modified without changing its name. If the Node needs to be replaced or updated significantly, the existing Node object needs to be removed from API server first and re-added after the update. 
### Self-registration of Nodes 
When the kubelet flag --register-nodeis true (the default), the kubelet will attempt to register itself with the API server. This is the preferred pattern, used by most distros. 
For self-registration, the kubelet is started with the following options: 
- 
--kubeconfig- Path to credentials to authenticate itself to the API server. - 
--cloud-provider- How to talk to a cloud provider to read metadata about itself. - 
--register-node- Automatically register with the API server. - 
--register-with-taints- Register the node with the given list of taints (comma separated <key>=<value>:<effect>). 
No-op if register-nodeis false. - 
--node-ip- Optional comma-separated list of the IP addresses for the node. You can only specify a single address for each address family. For example, in a single-stack IPv4 cluster, you set this value to be the IPv4 address that the kubelet should use for the node. See configure IPv4/IPv6 dual stack for details of running a dual-stack cluster. 
If you don't provide this argument, the kubelet uses the node's default IPv4 address, if any; if the node has no IPv4 addresses then the kubelet uses the node's default IPv6 address. - 
--node-labels- Labels to add when registering the node in the cluster (see label restrictions enforced by the NodeRestriction admission plugin ). - 
--node-status-update-frequency- Specifies how often kubelet posts its node status to the API server. 
When the Node authorization mode and NodeRestriction admission plugin are enabled, kubelets are only authorized to create/modify their own Node resource. 
#### Note: 
As mentioned in the Node name uniqueness section, when Node configuration needs to be updated, it is a good practice to re-register the node with the API server. For example, if the kubelet is being restarted with a new set of --node-labels, but the same Node name is used, the change will not take effect, as labels are only set (or modified) upon Node registration with the API server. 
Pods already scheduled on the Node may misbehave or cause issues if the Node configuration will be changed on kubelet restart. For example, an already running Pod may be tainted against the new labels assigned to the Node, while other Pods, that are incompatible with that Pod will be scheduled based on this new label. Node re-registration ensures all Pods will be drained and properly re-scheduled. 
### Manual Node administration 
You can create and modify Node objects using kubectl . 
When you want to create Node objects manually, set the kubelet flag --register-node=false. 
You can modify Node objects regardless of the setting of --register-node. For example, you can set labels on an existing Node or mark it unschedulable. 
You can set optional node role(s) for nodes by adding one or more node-role.kubernetes.io/<role>: <role>labels to the node where characters of <role>are limited by the syntax rules for labels. 
Kubernetes ignores the label value for node roles; by convention, you can set it to the same string you used for the node role in the label key. 
You can use labels on Nodes in conjunction with node selectors on Pods to control scheduling. For example, you can constrain a Pod to only be eligible to run on a subset of the available nodes. 
Marking a node as unschedulable prevents the scheduler from placing new pods onto that Node but does not affect existing Pods on the Node. This is useful as a preparatory step before a node reboot or other maintenance. 
To mark a Node unschedulable, run: 
```
kubectl cordon $NODENAME
```

See Safely Drain a Node for more details. 
#### Note: Pods that are part of a DaemonSet tolerate being run on an unschedulable Node. DaemonSets typically provide node-local services that should run on the Node even if it is being drained of workload applications. 
## Node status 
A Node's status contains the following information: 
- Addresses - Conditions - Capacity and Allocatable - Info 
You can use kubectlto view a Node's status and other details: 
```
kubectl describe node <insert-node-name-here>

```

See Node Status for more details. 
## Node heartbeats 
Heartbeats, sent by Kubernetes nodes, help your cluster determine the availability of each node, and to take action when failures are detected. 
For nodes there are two forms of heartbeats: 
- Updates to the .statusof a Node. - Lease objects within the kube-node-leasenamespace . Each Node has an associated Lease object. 
## Node controller 
The node controller is a Kubernetes control plane component that manages various aspects of nodes. 
The node controller has multiple roles in a node's life. The first is assigning a CIDR block to the node when it is registered (if CIDR assignment is turned on). 
The second is keeping the node controller's internal list of nodes up to date with the cloud provider's list of available machines. When running in a cloud environment and whenever a node is unhealthy, the node controller asks the cloud provider if the VM for that node is still available. If not, the node controller deletes the node from its list of nodes. 
The third is monitoring the nodes' health. The node controller is responsible for: 
- In the case that a node becomes unreachable, updating the Readycondition in the Node's .statusfield. In this case the node controller sets the Readycondition to Unknown. - If a node remains unreachable: triggering API-initiated eviction for all of the Pods on the unreachable node. By default, the node controller waits 5 minutes between marking the node as Unknownand submitting the first eviction request. 
By default, the node controller checks the state of each node every 5 seconds. This period can be configured using the --node-monitor-periodflag on the kube-controller-managercomponent. 
### Rate limits on eviction 
In most cases, the node controller limits the eviction rate to --node-eviction-rate(default 0.1) per second, meaning it won't evict pods from more than 1 node per 10 seconds. 
The node eviction behavior changes when a node in a given availability zone becomes unhealthy. The node controller checks what percentage of nodes in the zone are unhealthy (the Readycondition is Unknownor False) at the same time: 
- If the fraction of unhealthy nodes is at least --unhealthy-zone-threshold(default 0.55), then the eviction rate is reduced. - If the cluster is small (i.e. has less than or equal to --large-cluster-size-thresholdnodes - default 50), then evictions are stopped. - Otherwise, the eviction rate is reduced to --secondary-node-eviction-rate(default 0.01) per second. 
The reason these policies are implemented per availability zone is because one availability zone might become partitioned from the control plane while the others remain connected. If your cluster does not span multiple cloud provider availability zones, then the eviction mechanism does not take per-zone unavailability into account. 
A key reason for spreading your nodes across availability zones is so that the workload can be shifted to healthy zones when one entire zone goes down. Therefore, if all nodes in a zone are unhealthy, then the node controller evicts at the normal rate of --node-eviction-rate. The corner case is when all zones are completely unhealthy (none of the nodes in the cluster are healthy). In such a case, the node controller assumes that there is some problem with connectivity between the control plane and the nodes, and doesn't perform any evictions. (If there has been an outage and some nodes reappear, the node controller does evict pods from the remaining nodes that are unhealthy or unreachable). 
The node controller is also responsible for evicting pods running on nodes with NoExecutetaints, unless those pods tolerate that taint. The node controller also adds taints corresponding to node problems like node unreachable or not ready. This means that the scheduler won't place Pods onto unhealthy nodes. 
## Resource capacity tracking 
Node objects track information about the Node's resource capacity: for example, the amount of memory available and the number of CPUs. Nodes that self register report their capacity during registration. If you manually add a Node, then you need to set the node's capacity information when you add it. 
The Kubernetes scheduler ensures that there are enough resources for all the Pods on a Node. The scheduler checks that the sum of the requests of containers on the node is no greater than the node's capacity. That sum of requests includes all containers managed by the kubelet, but excludes any containers started directly by the container runtime, and also excludes any processes running outside of the kubelet's control. 
#### Note: If you want to explicitly reserve resources for non-Pod processes, see reserve resources for system daemons . 
## Node topology 
This is a stable feature in Kubernetes, and has been since the 1.27 release. You can no longer toggle this feature (the associated feature gate has been removed). 
If you have enabled the TopologyManagerfeature gate , then the kubelet can use topology hints when making resource assignment decisions. See Control Topology Management Policies on a Node for more information. 
## What's next 
Learn more about the following: 
- Components that make up a node. - API definition for Node . - Node section of the architecture design document. - Graceful/non-graceful node shutdown . - Node autoscaling to manage the number and size of nodes in your cluster. - Taints and Tolerations . - Node Resource Managers . - Resource Management for Windows nodes . 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified May 17, 2026 at 2:33 PM PST: docs: use glossary tooltip shortcode for containers on Nodes page (2646f8153a) 
- - - - - - 

- - - - 

### 📄 Source: [https://kubernetes.io/docs/concepts/cluster-administration/certificates/](https://kubernetes.io/docs/concepts/cluster-administration/certificates/)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - Français (French)   - Bahasa Indonesia (Indonesian)   - 日本語 (Japanese)   - 한국어 (Korean)   - Português (Portuguese)   - Русский (Russian)   - Español (Spanish)   - বাংলা (Bengali)   - Deutsch (German)   - हिन्दी (Hindi)   - Italiano (Italian)   - فارسی (Persian)   - Polski (Polish)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# Certificates 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- - - - 
# Certificates 
To learn how to generate certificates for your cluster, see Certificates . 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified January 16, 2021 at 7:16 PM PST: Migrate https://kubernetes.io/docs/concepts/cluster-administration/certificates/ to tasks section (41220636ec) 
- - - - - - 

- - - - 

### 📄 Source: [https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - বাংলা (Bengali)   - 中文 (Chinese)   - Français (French)   - Deutsch (German)   - हिन्दी (Hindi)   - Bahasa Indonesia (Indonesian)   - Italiano (Italian)   - 日本語 (Japanese)   - 한국어 (Korean)   - Polski (Polish)   - Português (Portuguese)   - Русский (Russian)   - Español (Spanish)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese)   - فارسی (Persian) - Theme fixed for this page 
# Overview 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- - - - 
- - - 
# Overview Kubernetes is a portable, extensible, open source platform for managing containerized workloads and services that facilitate both declarative configuration and automation. It has a large, rapidly growing ecosystem. Kubernetes services, support, and tools are widely available. 
This page is an overview of Kubernetes. 
The name Kubernetes originates from Greek, meaning helmsman or pilot. K8s as an abbreviation results from counting the eight letters between the "K" and the "s". Google open sourced the Kubernetes project in 2014. Kubernetes combines over 15 years of Google's experience running production workloads at scale with best-of-breed ideas and practices from the community. 
## Why you need Kubernetes and what it can do 
Containers are a good way to bundle and run your applications. In a production environment, you need to manage the containers that run the applications and ensure that there is no downtime. For example, if a container goes down, another container needs to start. Wouldn't it be easier if this behavior was handled by a system? 
That's how Kubernetes comes to the rescue! Kubernetes provides you with a framework to run distributed systems resiliently. It takes care of scaling and failover for your application, provides deployment patterns, and more. For example: Kubernetes can easily manage a canary deployment for your system. 
Kubernetes provides you with: 
- Service discovery and load balancing Kubernetes can expose a container using a DNS name or its own IP address. If traffic to a container is high, Kubernetes is able to load balance and distribute the network traffic so that the deployment is stable. - Storage orchestration Kubernetes allows you to automatically mount a storage system of your choice, such as local storage, public cloud providers, and more. - Automated rollouts and rollbacks You can describe the desired state for your deployed containers using Kubernetes, and it can change the actual state to the desired state at a controlled rate. For example, you can automate Kubernetes to create new containers for your deployment, remove existing containers and adopt all their resources to the new container. - Automatic bin packing You provide Kubernetes with a cluster of nodes that it can use to run containerized tasks. You tell Kubernetes how much CPU and memory (RAM) each container needs. Kubernetes can fit containers onto your nodes to make the best use of your resources. - Self-healing Kubernetes restarts containers that fail, replaces containers, kills containers that don't respond to your user-defined health check, and doesn't advertise them to clients until they are ready to serve. - Secret and configuration management Kubernetes lets you store and manage sensitive information, such as passwords, OAuth tokens, and SSH keys. You can deploy and update secrets and application configuration without rebuilding your container images, and without exposing secrets in your stack configuration. - Batch execution In addition to services, Kubernetes can manage your batch and CI workloads, replacing containers that fail, if desired. - Horizontal scaling Scale your application up and down with a simple command, with a UI, or automatically based on CPU usage. - IPv4/IPv6 dual-stack Allocation of IPv4 and IPv6 addresses to Pods and Services. - Designed for extensibility Add features to your Kubernetes cluster without changing upstream source code. 
## What Kubernetes is not 
Kubernetes is not a traditional, all-inclusive PaaS (Platform as a Service) system. Since Kubernetes operates at the container level rather than at the hardware level, it provides some generally applicable features common to PaaS offerings, such as deployment, scaling, load balancing, and lets users integrate their logging, monitoring, and alerting solutions. However, Kubernetes is not monolithic, and these default solutions are optional and pluggable. Kubernetes provides the building blocks for building developer platforms, but preserves user choice and flexibility where it is important. 
Kubernetes: 
- Does not limit the types of applications supported. Kubernetes aims to support an extremely diverse variety of workloads, including stateless, stateful, and data-processing workloads. If an application can run in a container, it should run great on Kubernetes. - Does not deploy source code and does not build your application. Continuous Integration, Delivery, and Deployment (CI/CD) workflows are determined by organization cultures and preferences as well as technical requirements. - Does not provide application-level services, such as middleware (for example, message buses), data-processing frameworks (for example, Spark), databases (for example, MySQL), caches, nor cluster storage systems (for example, Ceph) as built-in services. Such components can run on Kubernetes, and/or can be accessed by applications running on Kubernetes through portable mechanisms, such as the Open Service Broker . - Does not dictate logging, monitoring, or alerting solutions. It provides some integrations as proof of concept, and mechanisms to collect and export metrics. - Does not provide nor mandate a configuration language/system (for example, Jsonnet). It provides a declarative API that may be targeted by arbitrary forms of declarative specifications. - Does not provide nor adopt any comprehensive machine configuration, maintenance, management, or self-healing systems. - Additionally, Kubernetes is not a mere orchestration system. In fact, it eliminates the need for orchestration. The technical definition of orchestration is execution of a defined workflow: first do A, then B, then C. In contrast, Kubernetes comprises a set of independent, composable control processes that continuously drive the current state towards the provided desired state. It shouldn't matter how you get from A to C. Centralized control is also not required. This results in a system that is easier to use and more powerful, robust, resilient, and extensible. 
## Historical context for Kubernetes 
Let's take a look at why Kubernetes is so useful by going back in time. 

Traditional deployment era: 
Early on, organizations ran applications on physical servers. There was no way to define resource boundaries for applications in a physical server, and this caused resource allocation issues. For example, if multiple applications run on a physical server, there can be instances where one application would take up most of the resources, and as a result, the other applications would underperform. A solution for this would be to run each application on a different physical server. But this did not scale as resources were underutilized, and it was expensive for organizations to maintain many physical servers. 
Virtualized deployment era: 
As a solution, virtualization was introduced. It allows you to run multiple Virtual Machines (VMs) on a single physical server's CPU. Virtualization allows applications to be isolated between VMs and provides a level of security as the information of one application cannot be freely accessed by another application. 
Virtualization allows better utilization of resources in a physical server and allows better scalability because an application can be added or updated easily, reduces hardware costs, and much more. With virtualization you can present a set of physical resources as a cluster of disposable virtual machines. 
Each VM is a full machine running all the components, including its own operating system, on top of the virtualized hardware. 
Container deployment era: 
Containers are similar to VMs, but they have relaxed isolation properties to share the Operating System (OS) among the applications. Therefore, containers are considered lightweight. Similar to a VM, a container has its own filesystem, share of CPU, memory, process space, and more. As they are decoupled from the underlying infrastructure, they are portable across clouds and OS distributions. 
Containers have become popular because they provide extra benefits, such as: 
- Agile application creation and deployment: increased ease and efficiency of container image creation compared to VM image use. - Continuous development, integration, and deployment: provides reliable and frequent container image build and deployment with quick and efficient rollbacks (due to image immutability). - Dev and Ops separation of concerns: create application container images at build/release time rather than deployment time, thereby decoupling applications from infrastructure. - Observability: not only surfaces OS-level information and metrics, but also application health and other signals. - Environmental consistency across development, testing, and production: runs the same on a laptop as it does in the cloud. - Cloud and OS distribution portability: runs on Ubuntu, RHEL, CoreOS, on-premises, on major public clouds, and anywhere else. - Application-centric management: raises the level of abstraction from running an OS on virtual hardware to running an application on an OS using logical resources. - Loosely coupled, distributed, elastic, liberated micro-services: applications are broken into smaller, independent pieces and can be deployed and managed dynamically – not a monolithic stack running on one big single-purpose machine. - Resource isolation: predictable application performance. - Resource utilization: high efficiency and density. 
## What's next 
- Take a look at the Kubernetes Components - Take a look at the Kubernetes API - Take a look at kubectl : the primary CLI for Kubernetes - Take a look at the Cluster Architecture - Ready to Get Started ? 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified May 30, 2026 at 6:09 PM PST: Add theme_lock front matter to concepts overview pages (6e5065edcf) 
- - - - - - 

- - - - 

### 📄 Source: [https://kubernetes.io/docs/concepts/policy/pod-security-policy/](https://kubernetes.io/docs/concepts/policy/pod-security-policy/)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - 日本語 (Japanese)   - 한국어 (Korean)   - Português (Portuguese)   - Español (Spanish)   - বাংলা (Bengali)   - Français (French)   - Deutsch (German)   - हिन्दी (Hindi)   - Bahasa Indonesia (Indonesian)   - Italiano (Italian)   - فارسی (Persian)   - Polski (Polish)   - Русский (Russian)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# Pod Security Policies 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- - - - 
# Pod Security Policies 
#### Removed feature PodSecurityPolicy was deprecated in Kubernetes v1.21, and removed from Kubernetes in v1.25. 
Instead of using PodSecurityPolicy, you can enforce similar restrictions on Pods using either or both: 
- Pod Security Admission - a 3rd party admission plugin, that you deploy and configure yourself 
For a migration guide, see Migrate from PodSecurityPolicy to the Built-In PodSecurity Admission Controller . For more information on the removal of this API, see PodSecurityPolicy Deprecation: Past, Present, and Future . 
If you are not running Kubernetes v1.37, check the documentation for your version of Kubernetes. 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified November 05, 2022 at 6:22 PM PST: Tweak page about PSP removal (4e006c898d) 
- - - - - - 

- - - - 

### 📄 Source: [https://kubernetes.io/docs/concepts/security/overview/](https://kubernetes.io/docs/concepts/security/overview/)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - বাংলা (Bengali)   - 中文 (Chinese)   - Français (French)   - Bahasa Indonesia (Indonesian)   - 日本語 (Japanese)   - 한국어 (Korean)   - Polski (Polish)   - Português (Portuguese)   - Español (Spanish)   - Deutsch (German)   - हिन्दी (Hindi)   - Italiano (Italian)   - فارسی (Persian)   - Русский (Russian)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# Security 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- 
  -   -   -   -   - - - - 
- - - 
# Security Concepts for keeping your cloud-native workload secure. 
This section of the Kubernetes documentation aims to help you learn to run workloads more securely, and about the essential aspects of keeping a Kubernetes cluster secure. 
Kubernetes is based on a cloud-native architecture, and draws on advice from the CNCF about good practice for cloud native information security. 
Read Cloud Native Security and Kubernetes for the broader context about how to secure your cluster and the applications that you're running on it. 
## Kubernetes security mechanisms 
Kubernetes includes several APIs and security controls, as well as ways to define policies that can form part of how you manage information security. 
### Control plane protection 
A key security mechanism for any Kubernetes cluster is to control access to the Kubernetes API . 
Kubernetes expects you to configure and use TLS to provide data encryption in transit within the control plane, and between the control plane and its clients. You can also enable encryption at rest for the data stored within Kubernetes control plane; this is separate from using encryption at rest for your own workloads' data, which might also be a good idea. 
### Secrets 
The Secret API provides basic protection for configuration values that require confidentiality. 
### Workload protection 
Enforce Pod security standards to ensure that Pods and their containers are isolated appropriately. You can also use RuntimeClasses to define custom isolation if you need it. 
Network policies let you control network traffic between Pods, or between Pods and the network outside your cluster. 
You can deploy security controls from the wider ecosystem to implement preventative or detective controls around Pods, their containers, and the images that run in them. 
### Admission control 
Admission controllers are plugins that intercept Kubernetes API requests and can validate or mutate the requests based on specific fields in the request. Thoughtfully designing these controllers helps to avoid unintended disruptions as Kubernetes APIs change across version updates. For design considerations, see Admission Webhook Good Practices . 
### Auditing 
Kubernetes audit logging provides a security-relevant, chronological set of records documenting the sequence of actions in a cluster. The cluster audits the activities generated by users, by applications that use the Kubernetes API, and by the control plane itself. 
## Cloud provider security Note: Items on this page refer to vendors external to Kubernetes. The Kubernetes project authors aren't responsible for those third-party products or projects. To add a vendor, product or project to this list, read the content guide before submitting a change. More information. 
If you are running a Kubernetes cluster on your own hardware or a different cloud provider, consult your documentation for security best practices. Here are links to some of the popular cloud providers' security documentation: Cloud provider security 
|  IaaS Provider  | Link  |
|  Alibaba Cloud  | https://www.alibabacloud.com/trust-center  |
|  Amazon Web Services  | https://aws.amazon.com/security  |
|  Google Cloud Platform  | https://cloud.google.com/security  |
|  Huawei Cloud  | https://www.huaweicloud.com/intl/en-us/securecenter/overallsafety  |
|  IBM Cloud  | https://www.ibm.com/cloud/security  |
|  Microsoft Azure  | https://docs.microsoft.com/en-us/azure/security/azure-security  |
|  Oracle Cloud Infrastructure  | https://www.oracle.com/security  |
|  Tencent Cloud  | https://www.tencentcloud.com/solutions/data-security-and-information-protection  |
|  VMware vSphere  | https://www.vmware.com/solutions/security/hardening-guides  |
## Policies 
You can define security policies using Kubernetes-native mechanisms, such as NetworkPolicy (declarative control over network packet filtering) or ValidatingAdmissionPolicy (declarative restrictions on what changes someone can make using the Kubernetes API). 
However, you can also rely on policy implementations from the wider ecosystem around Kubernetes. Kubernetes provides extension mechanisms to let those ecosystem projects implement their own policy controls on source code review, container image approval, API access controls, networking, and more. 
For more information about policy mechanisms and Kubernetes, read Policies . 
## What's next 
Learn about related Kubernetes security topics: 
- Securing your cluster - Known vulnerabilities in Kubernetes (and links to further information) - Data encryption in transit for the control plane - Data encryption at rest - Controlling Access to the Kubernetes API - Network policies for Pods - Secrets in Kubernetes - Pod security standards - RuntimeClasses 
Learn the context: 
- Cloud Native Security and Kubernetes 
Get certified: 
- Certified Kubernetes Security Specialist certification and official training course. 
Read more in this section: 
- Pod Security Standards - Pod Security Admission - Service Accounts - Pod Security Policies - Security For Linux Nodes - Security For Windows Nodes - Controlling Access to the Kubernetes API - Role Based Access Control Good Practices - Good practices for Kubernetes Secrets - Multi-tenancy - Hardening Guide - Authentication Mechanisms - Hardening Guide - Dynamic Resource Allocation - Hardening Guide - Scheduler Configuration - Kubernetes API Server Bypass Risks - Linux kernel security constraints for Pods and containers - Security Checklist - Application Security Checklist 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified February 03, 2025 at 5:28 PM PST: Add a new page for mutating webhook good practices. (bf971d28d3) 
Items on this page refer to third party products or projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for those third-party products or projects. See the CNCF website guidelines for more details. 
You should read the content guide before proposing a change that adds an extra third-party link. 
- - - - - - 

- - - - 

### 📄 Source: [https://kubernetes.io/docs/concepts/security/pod-security-standards/](https://kubernetes.io/docs/concepts/security/pod-security-standards/)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - 日本語 (Japanese)   - 한국어 (Korean)   - বাংলা (Bengali)   - Français (French)   - Deutsch (German)   - हिन्दी (Hindi)   - Bahasa Indonesia (Indonesian)   - Italiano (Italian)   - فارسی (Persian)   - Polski (Polish)   - Português (Portuguese)   - Русский (Russian)   - Español (Spanish)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
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

### 📄 Source: [https://kubernetes.io/docs/concepts/services-networking/network-policies/](https://kubernetes.io/docs/concepts/services-networking/network-policies/)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - Bahasa Indonesia (Indonesian)   - 日本語 (Japanese)   - 한국어 (Korean)   - Português (Portuguese)   - Español (Spanish)   - বাংলা (Bengali)   - Français (French)   - Deutsch (German)   - हिन्दी (Hindi)   - Italiano (Italian)   - فارسی (Persian)   - Polski (Polish)   - Русский (Russian)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# Network Policies 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- - - - - 
  -   -   -   -   - - - - - - - - - - 
- - - - 
# Network Policies If you want to control traffic flow at the IP address or port level (OSI layer 3 or 4), NetworkPolicies allow you to specify rules for traffic flow within your cluster, and also between Pods and the outside world. Your cluster must use a network plugin that supports NetworkPolicy enforcement. 
If you want to control traffic flow at the IP address or port level for TCP, UDP, and SCTP protocols, then you might consider using Kubernetes NetworkPolicies for particular applications in your cluster. NetworkPolicies are an application-centric construct which allow you to specify how a pod is allowed to communicate with various network "entities" (we use the word "entity" here to avoid overloading the more common terms such as "endpoints" and "services", which have specific Kubernetes connotations) over the network. NetworkPolicies apply to a connection with a pod on one or both ends, and are not relevant to other connections. 
The entities that a Pod can communicate with are identified through a combination of the following three identifiers: 
- Other pods that are allowed (exception: a pod cannot block access to itself) - Namespaces that are allowed - IP blocks (exception: traffic to and from the node where a Pod is running is always allowed, regardless of the IP address of the Pod or the node) 
When defining a pod- or namespace-based NetworkPolicy, you use a selector to specify what traffic is allowed to and from the Pod(s) that match the selector. 
Meanwhile, when IP-based NetworkPolicies are created, we define policies based on IP blocks (CIDR ranges). 
## Prerequisites 
Network policies are implemented by the network plugin . To use network policies, you must be using a networking solution which supports NetworkPolicy. Creating a NetworkPolicy resource without a controller that implements it will have no effect. 
## The two sorts of pod isolation 
There are two sorts of isolation for a pod: isolation for egress, and isolation for ingress. They concern what connections may be established. "Isolation" here is not absolute, rather it means "some restrictions apply". The alternative, "non-isolated for $direction", means that no restrictions apply in the stated direction. The two sorts of isolation (or not) are declared independently, and are both relevant for a connection from one pod to another. 
By default, a pod is non-isolated for egress; all outbound connections are allowed. A pod is isolated for egress if there is any NetworkPolicy that both selects the pod and has "Egress" in its policyTypes; we say that such a policy applies to the pod for egress. When a pod is isolated for egress, the only allowed connections from the pod are those allowed by the egresslist of some NetworkPolicy that applies to the pod for egress. Reply traffic for those allowed connections will also be implicitly allowed. The effects of those egresslists combine additively. 
By default, a pod is non-isolated for ingress; all inbound connections are allowed. A pod is isolated for ingress if there is any NetworkPolicy that both selects the pod and has "Ingress" in its policyTypes; we say that such a policy applies to the pod for ingress. When a pod is isolated for ingress, the only allowed connections into the pod are those from the pod's node and those allowed by the ingresslist of some NetworkPolicy that applies to the pod for ingress. Reply traffic for those allowed connections will also be implicitly allowed. The effects of those ingresslists combine additively. 
Network policies do not conflict; they are additive. If any policy or policies apply to a given pod for a given direction, the connections allowed in that direction from that pod is the union of what the applicable policies allow. Thus, order of evaluation does not affect the policy result. 
For a connection from a source pod to a destination pod to be allowed, both the egress policy on the source pod and the ingress policy on the destination pod need to allow the connection. If either side does not allow the connection, it will not happen. 
## The NetworkPolicy resource 
See the NetworkPolicy reference for a full definition of the resource. 
An example NetworkPolicy might look like this: service/networking/networkpolicy.yaml
```
apiVersion:networking.k8s.io/v1kind:NetworkPolicymetadata:name:test-network-policynamespace:defaultspec:podSelector:matchLabels:role:dbpolicyTypes:- Ingress- Egressingress:- from:- ipBlock:cidr:172.17.0.0/16except:- 172.17.1.0/24- namespaceSelector:matchLabels:project:myproject- podSelector:matchLabels:role:frontendports:- protocol:TCPport:6379egress:- to:- ipBlock:cidr:10.0.0.0/24ports:- protocol:TCPport:5978
```

#### Note: POSTing this to the API server for your cluster will have no effect unless your chosen networking solution supports network policy. 
Mandatory Fields : As with all other Kubernetes config, a NetworkPolicy needs apiVersion, kind, and metadatafields. For general information about working with config files, see Configure a Pod to Use a ConfigMap , and Object Management . 
spec : NetworkPolicy spec has all the information needed to define a particular network policy in the given namespace. 
podSelector : Each NetworkPolicy includes a podSelectorwhich selects the grouping of pods to which the policy applies. The example policy selects pods with the label "role=db". An empty podSelectorselects all pods in the namespace. 
policyTypes : Each NetworkPolicy includes a policyTypeslist which may include either Ingress, Egress, or both. The policyTypesfield indicates whether or not the given policy applies to ingress traffic to selected pod, egress traffic from selected pods, or both. If no policyTypesare specified on a NetworkPolicy then by default Ingresswill always be set and Egresswill be set if the NetworkPolicy has any egress rules. 
ingress : Each NetworkPolicy may include a list of allowed ingressrules. Each rule allows traffic which matches both the fromand portssections. The example policy contains a single rule, which matches traffic on a single port, from one of three sources, the first specified via an ipBlock, the second via a namespaceSelectorand the third via a podSelector. 
egress : Each NetworkPolicy may include a list of allowed egressrules. Each rule allows traffic which matches both the toand portssections. The example policy contains a single rule, which matches traffic on a single port to any destination in 10.0.0.0/24. 
So, the example NetworkPolicy: 
- 
isolates role=dbpods in the defaultnamespace for both ingress and egress traffic (if they weren't already isolated) - 
(Ingress rules) allows connections to all pods in the defaultnamespace with the label role=dbon TCP port 6379 from: 
  - any pod in the defaultnamespace with the label role=frontend  - any pod in a namespace with the label project=myproject  - IP addresses in the ranges 172.17.0.0– 172.17.0.255and 172.17.2.0– 172.17.255.255(ie, all of 172.17.0.0/16except 172.17.1.0/24) - 
(Egress rules) allows connections from any pod in the defaultnamespace with the label role=dbto CIDR 10.0.0.0/24on TCP port 5978 
See the Declare Network Policy walkthrough for further examples. 
## Behavior of toand fromselectors 
There are four kinds of selectors that can be specified in an ingressfromsection or egresstosection: 
podSelector : This selects particular Pods in the same namespace as the NetworkPolicy which should be allowed as ingress sources or egress destinations. 
namespaceSelector : This selects particular namespaces for which all Pods should be allowed as ingress sources or egress destinations. 
namespaceSelector and podSelector : A single to/ fromentry that specifies both namespaceSelectorand podSelectorselects particular Pods within particular namespaces. Be careful to use correct YAML syntax. For example: 
```
...ingress:- from:- namespaceSelector:matchLabels:user:alicepodSelector:matchLabels:role:client...
```

This policy contains a single fromelement allowing connections from Pods with the label role=clientin namespaces with the label user=alice. But the following policy is different: 
```
...ingress:- from:- namespaceSelector:matchLabels:user:alice- podSelector:matchLabels:role:client...
```

It contains two elements in the fromarray, and allows connections from Pods in the local Namespace with the label role=client, or from any Pod in any namespace with the label user=alice. 
When in doubt, use kubectl describeto see how Kubernetes has interpreted the policy. 
ipBlock : This selects particular IP CIDR ranges to allow as ingress sources or egress destinations. These should be cluster-external IPs, since Pod IPs are ephemeral and unpredictable. 
Cluster ingress and egress mechanisms often require rewriting the source or destination IP of packets. In cases where this happens, it is not defined whether this happens before or after NetworkPolicy processing, and the behavior may be different for different combinations of network plugin, cloud provider, Serviceimplementation, etc. 
In the case of ingress, this means that in some cases you may be able to filter incoming packets based on the actual original source IP, while in other cases, the "source IP" that the NetworkPolicy acts on may be the IP of a LoadBalanceror of the Pod's node, etc. 
For egress, this means that connections from pods to ServiceIPs that get rewritten to cluster-external IPs may or may not be subject to ipBlock-based policies. 
## Default policies 
By default, if no policies exist in a namespace, then all ingress and egress traffic is allowed to and from pods in that namespace. The following examples let you change the default behavior in that namespace. 
### Default deny all ingress traffic 
You can create a "default" ingress isolation policy for a namespace by creating a NetworkPolicy that selects all pods but does not allow any ingress traffic to those pods. service/networking/network-policy-default-deny-ingress.yaml
```
---apiVersion:networking.k8s.io/v1kind:NetworkPolicymetadata:name:default-deny-ingressspec:podSelector:{}policyTypes:- Ingress
```

This ensures that even pods that aren't selected by any other NetworkPolicy will still be isolated for ingress. This policy does not affect isolation for egress from any pod. 
### Allow all ingress traffic 
If you want to allow all incoming connections to all pods in a namespace, you can create a policy that explicitly allows that. service/networking/network-policy-allow-all-ingress.yaml
```
---apiVersion:networking.k8s.io/v1kind:NetworkPolicymetadata:name:allow-all-ingressspec:podSelector:{}ingress:- {}policyTypes:- Ingress
```

With this policy in place, no additional policy or policies can cause any incoming connection to those pods to be denied. This policy has no effect on isolation for egress from any pod. 
### Default deny all egress traffic 
You can create a "default" egress isolation policy for a namespace by creating a NetworkPolicy that selects all pods but does not allow any egress traffic from those pods. service/networking/network-policy-default-deny-egress.yaml
```
---apiVersion:networking.k8s.io/v1kind:NetworkPolicymetadata:name:default-deny-egressspec:podSelector:{}policyTypes:- Egress
```

This ensures that even pods that aren't selected by any other NetworkPolicy will not be allowed egress traffic. This policy does not change the ingress isolation behavior of any pod. 
#### Caution: A default deny-all egress policy also blocks DNS traffic. If your workloads need DNS resolution, you must add a separate NetworkPolicy that allows egress to your cluster's DNS service. 
### Allow all egress traffic 
If you want to allow all connections from all pods in a namespace, you can create a policy that explicitly allows all outgoing connections from pods in that namespace. service/networking/network-policy-allow-all-egress.yaml
```
---apiVersion:networking.k8s.io/v1kind:NetworkPolicymetadata:name:allow-all-egressspec:podSelector:{}egress:- {}policyTypes:- Egress
```

With this policy in place, no additional policy or policies can cause any outgoing connection from those pods to be denied. This policy has no effect on isolation for ingress to any pod. 
### Default deny all ingress and all egress traffic 
You can create a "default" policy for a namespace which prevents all ingress AND egress traffic by creating the following NetworkPolicy in that namespace. service/networking/network-policy-default-deny-all.yaml
```
---apiVersion:networking.k8s.io/v1kind:NetworkPolicymetadata:name:default-deny-allspec:podSelector:{}policyTypes:- Ingress- Egress
```

This ensures that even pods that aren't selected by any other NetworkPolicy will not be allowed ingress or egress traffic. 
## Network traffic filtering 
NetworkPolicy is defined for layer 4 connections (TCP, UDP, and optionally SCTP). For all the other protocols, the behaviour may vary across network plugins. 
#### Note: You must be using a CNI plugin that supports SCTP protocol NetworkPolicies. 
When a deny allnetwork policy is defined, it is only guaranteed to deny TCP, UDP and SCTP connections. For other protocols, such as ARP or ICMP, the behaviour is undefined. The same applies to allow rules: when a specific pod is allowed as ingress source or egress destination, it is undefined what happens with (for example) ICMP packets. Protocols such as ICMP may be allowed by some network plugins and denied by others. 
## Targeting a range of ports Feature state: Stable since Kubernetes v1.25 
When writing a NetworkPolicy, you can target a range of ports instead of a single port. 
This is achievable with the usage of the endPortfield, as the following example: service/networking/networkpolicy-multiport-egress.yaml
```
apiVersion:networking.k8s.io/v1kind:NetworkPolicymetadata:name:multi-port-egressnamespace:defaultspec:podSelector:matchLabels:role:dbpolicyTypes:- Egressegress:- to:- ipBlock:cidr:10.0.0.0/24ports:- protocol:TCPport:32000endPort:32768
```

The above rule allows any Pod with label role=dbon the namespace defaultto communicate with any IP within the range 10.0.0.0/24over TCP, provided that the target port is between the range 32000 and 32768. 
The following restrictions apply when using this field: 
- The endPortfield must be equal to or greater than the portfield. - endPortcan only be defined if portis also defined. - Both ports must be numeric. 
#### Note: Your cluster must be using a CNI plugin that supports the endPortfield in NetworkPolicy specifications. If your network plugin does not support the endPortfield and you specify a NetworkPolicy with that, the policy will be applied only for the single portfield. 
## Targeting multiple namespaces by label 
In this scenario, your EgressNetworkPolicy targets more than one namespace using their label names. For this to work, you need to label the target namespaces. For example: 
```
kubectl label namespace frontend namespace=frontend
kubectl label namespace backend namespace=backend

```

Add the labels under namespaceSelectorin your NetworkPolicy document. For example: 
```
apiVersion:networking.k8s.io/v1kind:NetworkPolicymetadata:name:egress-namespacesspec:podSelector:matchLabels:app:myapppolicyTypes:- Egressegress:- to:- namespaceSelector:matchExpressions:- key:namespaceoperator:Invalues:["frontend","backend"]
```

#### Note: It is not possible to directly specify the name of the namespaces in a NetworkPolicy. You must use a namespaceSelectorwith matchLabelsor matchExpressionsto select the namespaces based on their labels. 
## Targeting a Namespace by its name 
The Kubernetes control plane sets an immutable label kubernetes.io/metadata.nameon all namespaces, the value of the label is the namespace name. 
While NetworkPolicy cannot target a namespace by its name with some object field, you can use the standardized label to target a specific namespace. 
## Pod lifecycle 
#### Note: The following applies to clusters with a conformant networking plugin and a conformant implementation of NetworkPolicy. 
When a new NetworkPolicy object is created, it may take some time for a network plugin to handle the new object. If a pod that is affected by a NetworkPolicy is created before the network plugin has completed NetworkPolicy handling, that pod may be started unprotected, and isolation rules will be applied when the NetworkPolicy handling is completed. 
Once the NetworkPolicy is handled by a network plugin, 
- 
All newly created pods affected by a given NetworkPolicy will be isolated before they are started. Implementations of NetworkPolicy must ensure that filtering is effective throughout the Pod lifecycle, even from the very first instant that any container in that Pod is started. Because they are applied at Pod level, NetworkPolicies apply equally to init containers, sidecar containers, and regular containers. - 
Allow rules will be applied eventually after the isolation rules (or may be applied at the same time). In the worst case, a newly created pod may have no network connectivity at all when it is first started, if isolation rules were already applied, but no allow rules were applied yet. 
Every created NetworkPolicy will be handled by a network plugin eventually, but there is no way to tell from the Kubernetes API when exactly that happens. 
Therefore, pods must be resilient against being started up with different network connectivity than expected. If you need to make sure the pod can reach certain destinations before being started, you can use an init container to wait for those destinations to be reachable before kubelet starts the app containers. 
Every NetworkPolicy will be applied to all selected pods eventually. Because the network plugin may implement NetworkPolicy in a distributed manner, it is possible that pods may see a slightly inconsistent view of network policies when the pod is first created, or when pods or policies change. For example, a newly-created pod that is supposed to be able to reach both Pod A on Node 1 and Pod B on Node 2 may find that it can reach Pod A immediately, but cannot reach Pod B until a few seconds later. 
## NetworkPolicy and hostNetworkpods 
NetworkPolicy behaviour for hostNetworkpods is undefined, but it should be limited to 2 possibilities: 
- The network plugin can distinguish hostNetworkpod traffic from all other traffic (including being able to distinguish traffic from different hostNetworkpods on the same node), and will apply NetworkPolicy to hostNetworkpods just like it does to pod-network pods. - The network plugin cannot properly distinguish hostNetworkpod traffic, and so it ignores hostNetworkpods when matching podSelectorand namespaceSelector. Traffic to/from hostNetworkpods is treated the same as all other traffic to/from the node IP. (This is the most common implementation.) 
This applies when 
- 
a hostNetworkpod is selected by spec.podSelector. 
```
...spec:podSelector:matchLabels:role:client...
```
- 
a hostNetworkpod is selected by a podSelectoror namespaceSelectorin an ingressor egressrule. 
```
...ingress:- from:- podSelector:matchLabels:role:client...
```

At the same time, since hostNetworkpods have the same IP addresses as the nodes they reside on, their connections will be treated as node connections. For example, you can allow traffic from a hostNetworkPod using an ipBlockrule. 
## What you can't do with network policies (at least, not yet) 
As of Kubernetes 1.37, the following functionality does not exist in the NetworkPolicy API, but you might be able to implement workarounds using Operating System components (such as SELinux, OpenVSwitch, IPTables, and so on) or Layer 7 technologies (Ingress controllers, Service Mesh implementations) or admission controllers. In case you are new to network security in Kubernetes, its worth noting that the following User Stories cannot (yet) be implemented using the NetworkPolicy API. 
- Forcing internal cluster traffic to go through a common gateway (this might be best served with a service mesh or other proxy). - Anything TLS related (use a service mesh or ingress controller for this). - Node specific policies (you can use CIDR notation for these, but you cannot target nodes by their Kubernetes identities specifically). - Targeting of services by name (you can, however, target pods or namespaces by their labels , which is often a viable workaround). - Creation or management of "Policy requests" that are fulfilled by a third party. - Default policies which are applied to all namespaces or pods (there are some third party Kubernetes distributions and projects which can do this). - Advanced policy querying and reachability tooling. - The ability to log network security events (for example connections that are blocked or accepted). - The ability to explicitly deny policies (currently the model for NetworkPolicies are deny by default, with only the ability to add allow rules). - The ability to prevent loopback or incoming host traffic (Pods cannot currently block localhost access, nor do they have the ability to block access from their resident node). 
## NetworkPolicy's impact on existing connections 
When the set of NetworkPolicies that applies to an existing connection changes - this could happen either due to a change in NetworkPolicies or if the relevant labels of the namespaces/pods selected by the policy (both subject and peers) are changed in the middle of an existing connection - it is implementation defined as to whether the change will take effect for that existing connection or not. Example: A policy is created that leads to denying a previously allowed connection, the underlying network plugin implementation is responsible for defining if that new policy will close the existing connections or not. It is recommended not to modify policies/pods/namespaces in ways that might affect existing connections. 
## What's next 
- See the Declare Network Policy walkthrough for further examples. - See more recipes for common scenarios enabled by the NetworkPolicy resource. 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified April 14, 2026 at 1:15 AM PST: fix(links): update kubernetes/community links from master to main (03c191bcc4) 
- - - - - - 

- - - - 

### 📄 Source: [https://kubernetes.io/docs/concepts/storage/](https://kubernetes.io/docs/concepts/storage/)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - বাংলা (Bengali)   - 中文 (Chinese)   - Français (French)   - Deutsch (German)   - Bahasa Indonesia (Indonesian)   - 日本語 (Japanese)   - 한국어 (Korean)   - Polski (Polish)   - Português (Portuguese)   - Español (Spanish)   - Українська (Ukrainian)   - हिन्दी (Hindi)   - Italiano (Italian)   - فارسی (Persian)   - Русский (Russian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# Storage 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- - - 
# Storage Ways to provide both long-term and temporary storage to Pods in your cluster. 
##### Volumes 

##### Persistent Volumes 

##### Projected Volumes 

##### Ephemeral Volumes 

##### Storage Classes 

##### Volume Attributes Classes 

##### Dynamic Volume Provisioning 

##### Volume Snapshots 

##### Volume Snapshot Classes 

##### CSI Volume Cloning 

##### Volume Populators and Data Sources 

##### Storage Capacity 

##### Node-specific Volume Limits 

##### Local ephemeral storage 

##### Volume Health Monitoring 

##### Windows Storage 

## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified June 16, 2021 at 5:57 PM PST: Remove exec permission on markdown files (e9703497a1) 
- - - - - - 

- - - - 

#### 📄 Sub-topic: [https://kubernetes.io/docs/concepts/storage/_print](https://kubernetes.io/docs/concepts/storage/_print)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - বাংলা (Bengali)   - 中文 (Chinese)   - Français (French)   - Deutsch (German)   - Bahasa Indonesia (Indonesian)   - 日本語 (Japanese)   - 한국어 (Korean)   - Polski (Polish)   - Português (Portuguese)   - Español (Spanish)   - Українська (Ukrainian)   - हिन्दी (Hindi)   - Italiano (Italian)   - فارسی (Persian)   - Русский (Russian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
This is the multi-page printable view of this section. Click here to print . 
Return to the regular view of this page . 
# Storage Ways to provide both long-term and temporary storage to Pods in your cluster. 
- 1: Volumes - 2: Persistent Volumes - 3: Projected Volumes - 4: Ephemeral Volumes - 5: Storage Classes - 6: Volume Attributes Classes - 7: Dynamic Volume Provisioning - 8: Volume Snapshots - 9: Volume Snapshot Classes - 10: CSI Volume Cloning - 11: Volume Populators and Data Sources - 12: Storage Capacity - 13: Node-specific Volume Limits - 14: Local ephemeral storage - 15: Volume Health Monitoring - 16: Windows Storage 
# 1 - Volumes 
Kubernetes volumes provide a way for containers in a Pod to access and share data via the filesystem. There are different kinds of volume that you can use for different purposes, such as: 
- populating a configuration file based on a ConfigMap or a Secret - providing some temporary scratch space for a Pod - sharing a filesystem between two different containers in the same Pod - sharing a filesystem between two different Pods (even if those Pods run on different nodes) - durably storing data so that it stays available even if the Pod restarts or is replaced - passing configuration information to an app running in a container, based on details of the Pod the container is in (for example: telling a sidecar container what namespace the Pod is running in) - providing read-only access to data in a different container image 
Data sharing can be between different local processes within a container, or between different containers, or between Pods. 
## Why volumes are important 
- 
Data persistence: On-disk files in a container are ephemeral, which presents some problems for non-trivial applications when running in containers. One problem occurs when a container crashes or is stopped; the container state is not saved, so all of the files that were created or modified during the lifetime of the container are lost. After a crash, kubelet restarts the container with a clean state. - 
Shared storage: Another problem occurs when multiple containers are running in a Podand need to share files. It can be challenging to set up and access a shared filesystem across all of the containers. 
The Kubernetes volume abstraction can help you to solve both of these problems. 
Before you learn about volumes, PersistentVolumes, and PersistentVolumeClaims, you should read up about Pods and make sure that you understand how Kubernetes uses Pods to run containers. 
## How volumes work 
Kubernetes supports many types of volumes. A Pod can use any number of volume types simultaneously. Ephemeral volume types have a lifetime linked to a specific Pod, but persistent volumes exist beyond the lifetime of any individual Pod. When a Pod ceases to exist, Kubernetes destroys ephemeral volumes; however, Kubernetes does not destroy persistent volumes. For any kind of volume in a given Pod, data is preserved across container restarts. 
At its core, a volume is a directory, possibly with some data in it, which is accessible to the containers in a pod. How that directory comes to be, the medium that backs it, and the contents of it are determined by the particular volume type used. 
To use a volume, specify the volumes to provide for the Pod in .spec.volumesand declare where to mount those volumes into containers in .spec.containers[*].volumeMounts. 
When a Pod is launched, a process in the container sees a filesystem view composed from the initial contents of the container image , plus volumes (if defined) mounted inside the container. The process sees a root filesystem that initially matches the contents of the container image. Any writes to within that filesystem hierarchy, if allowed, affect what that process views when it performs a subsequent filesystem access. Volumes are mounted at specified paths within the container filesystem. For each container defined within a Pod, you must independently specify where to mount each volume that the container uses. 
Volumes cannot mount within other volumes (but see Using subPath for a related mechanism). Also, a volume cannot contain a hard link to anything in a different volume. 
## Types of volumes 
Kubernetes supports several types of volumes. 
### configMap 
A ConfigMap provides a way to inject configuration data into Pods. The data stored in a ConfigMap can be referenced in a volume of type configMapand then consumed by containerized applications running in a Pod. 
When referencing a ConfigMap, you provide the name of the ConfigMap in the volume. You can customize the path to use for a specific entry in the ConfigMap. The following configuration shows how to mount the log-configConfigMap onto a Pod called configmap-pod: 
```
apiVersion:v1kind:Podmetadata:name:configmap-podspec:containers:- name:testimage:busybox:1.28command:['sh','-c','echo "The app is running!" && tail -f /dev/null']volumeMounts:- name:config-volmountPath:/etc/configvolumes:- name:config-volconfigMap:name:log-configitems:- key:log_levelpath:log_level.conf
```

The log-configConfigMap is mounted as a volume, and all contents stored in its log_levelentry are mounted into the Pod at path /etc/config/log_level.conf. Note that this path is derived from the volume's mountPathand the pathkeyed with log_level. 
#### Note: 
- 
You must create a ConfigMap before you can use it. - 
A ConfigMap is always mounted as readOnly. - 
A container using a ConfigMap as a subPathvolume mount will not receive updates when the ConfigMap changes. - 
Text data is exposed as files using the UTF-8 character encoding. For other character encodings, use binaryData. 
### downwardAPI 
A downwardAPIvolume makes downward API data available to applications. Within the volume, you can find the exposed data as read-only files in plain text format. 
#### Note: A container using the downward API as a subPathvolume mount does not receive updates when field values change. 
See Expose Pod Information to Containers Through Files to learn more. 
### emptyDir 
For a Pod that defines an emptyDirvolume, the volume is created when the Pod is assigned to a node. As the name says, the emptyDirvolume is initially empty. All containers in the Pod can read and write the same files in the emptyDirvolume, though that volume can be mounted at the same or different paths in each container. When a Pod is removed from a node for any reason, the data in the emptyDiris deleted permanently. 
#### Note: A container crashing does not remove a Pod from a node. The data in an emptyDirvolume is safe across container crashes. 
Some uses for an emptyDirare: 
- scratch space, such as for a disk-based merge sort - checkpointing a long computation for recovery from crashes - holding files that a content-manager container fetches while a webserver container serves the data 
The emptyDir.mediumfield controls where emptyDirvolumes are stored. By default emptyDirvolumes are stored on whatever medium that backs the node such as disk, SSD, or network storage, depending on your environment. If you set the emptyDir.mediumfield to "Memory", Kubernetes mounts a tmpfs (RAM-backed filesystem) for you instead. While tmpfs is very fast, be aware that, unlike disks, files you write count against the memory limit of the container that wrote them. 
A size limit can be specified for the default medium, which limits the capacity of the emptyDirvolume. The storage is allocated from node ephemeral storage . If that is filled up from another source (for example, log files or image overlays), the emptyDirmay run out of capacity before this limit. If no size is specified, memory-backed volumes are sized to node allocatable memory. 
#### Caution: Please check here for points to note in terms of resource management when using memory-backed emptyDir. Feature state: Alpha since Kubernetes v1.37; disabled by default More information about this feature 
To use this feature, you (or a cluster administrator) will need to enable the EmptyDirVolumeMode feature gate for all relevant components in your cluster. 
See Enable Or Disable Feature Gates for more information. 
The emptyDir.modefield lets you set Unix permission bits on the emptyDir directory, specifying a value between 0000and 01777(octal). This follows the same pattern as the defaultModefield on Secret and ConfigMap volumes. If modeis not specified, the directory is created with the default 0777permissions. 
Setting a custom mode is useful when you want to restrict access to owner and group only (for example, 0750), or set the sticky bit on a shared directory so that only file owners can delete their own files (for example, 01777). 
#### Note: If fsGroupis set in the Pod's security context, the group permissions applied by fsGroupoverride the modespecified here. The modefield has no effect on Windows. 
#### emptyDir configuration example 
```
apiVersion:v1kind:Podmetadata:name:test-pdspec:containers:- image:registry.k8s.io/test-webservername:test-containervolumeMounts:- mountPath:/cachename:cache-volumevolumes:- name:cache-volumeemptyDir:sizeLimit:500Mi
```

#### emptyDir memory configuration example 
```
apiVersion:v1kind:Podmetadata:name:test-pdspec:containers:- image:registry.k8s.io/test-webservername:test-containervolumeMounts:- mountPath:/cachename:cache-volumevolumes:- name:cache-volumeemptyDir:sizeLimit:500Mimedium:Memory
```

#### Note: 
```
        <div class="feature-state-notice feature-alpha" title="Feature Gate: InPlacePodVerticalScalingMemoryBackedVolumes">
          <span class="feature-state-name">Feature state:</span>
          <span class="feature-state-details">
           
             <span class="feature-state-stage">Alpha</span> since Kubernetes v1.37; disabled by default
           </span>
        </div>
        
        
        <div class="feature-alpha">
          
          
            <details>
            <summary>More information about this feature</summary>
            <p>To use this feature, you (or a cluster administrator) will need to enable the <a href="/docs/reference/command-line-tools-reference/feature-gates/#InPlacePodVerticalScalingMemoryBackedVolumes"><tt>InPlacePodVerticalScalingMemoryBackedVolumes</tt></a> feature gate for all relevant components in your cluster.</p>

```

See Enable Or Disable Feature Gates for more information. 
```
            </details>
            </div>

```

When the InPlacePodVerticalScalingMemoryBackedVolumesfeature gate is enabled, you can dynamically adjust the sizeLimitof memory-backed ( medium: Memory) emptyDirvolumes without restarting the Pod. For more details, see Resize CPU and Memory Resources assigned to Containers . 
#### emptyDir permissions configuration example 
```
apiVersion:v1kind:Podmetadata:name:test-pdspec:containers:- image:registry.k8s.io/test-webservername:test-containervolumeMounts:- mountPath:/cachename:cache-volumevolumes:- name:cache-volumeemptyDir:mode:01777
```

### fc (fibre channel) 
An fcvolume type allows an existing fibre channel block storage volume to be mounted in a Pod. You can specify single or multiple target world wide names (WWNs) using the parameter targetWWNsin your Volume configuration. If multiple WWNs are specified, targetWWNs expect that those WWNs are from multi-path connections. 
#### Note: You must configure FC SAN Zoning to allocate and mask those LUNs (volumes) to the target WWNs beforehand so that Kubernetes hosts can access them. 
### gcePersistentDisk (deprecated) 
In Kubernetes 1.37, all operations for the in-tree gcePersistentDisktype are redirected to the pd.csi.storage.gke.ioCSI driver. 
The gcePersistentDiskin-tree storage driver was deprecated in the Kubernetes v1.17 release and then removed entirely in the v1.28 release. 
The Kubernetes project suggests that you use the Google Compute Engine Persistent Disk CSI third party storage driver instead. 
### gitRepo (disabled) 
#### Warning: 
Kubernetes 1.37 does not include the gitRepovolume driver. The last version that provided a way to use this driver was Kubernetes v1.35, and it has been deprecated since the v1.11 minor release. 
To provision a Pod that has a Git repository mounted, you can mount an emptyDirvolume into an init container that clones the repo using Git, then mount the EmptyDir into the Pod's container. 
You can restrict the use of gitRepovolumes in your cluster using policies , such as ValidatingAdmissionPolicy . You can use the following Common Expression Language (CEL) expression as part of a policy to reject use of gitRepovolumes: 
```
!has(object.spec.volumes) || !object.spec.volumes.exists(v, has(v.gitRepo))

```

### hostPath 
A hostPathvolume mounts a file or directory from the host node's filesystem into your Pod. This is not something that most Pods will need, but it offers a powerful escape hatch for some applications. 
#### Warning: 
Using the hostPathvolume type presents many security risks. If you can avoid using a hostPathvolume, you should. For example, define a localPersistentVolume , and use that instead. 
If you are restricting access to specific directories on the node using admission-time validation, that restriction is only effective when you additionally require that any mounts of that hostPathvolume are read only . If you allow a read-write mount of any host path by an untrusted Pod, the containers in that Pod may be able to subvert the read-write host mount. 
Take care when using hostPathvolumes, whether these are mounted as read-only or as read-write, because: 
- Access to the host filesystem can expose privileged system credentials (such as for the kubelet) or privileged APIs (such as the container runtime socket) that can be used for container escape or to attack other parts of the cluster. - Pods with identical configuration (such as created from a PodTemplate) may behave differently on different nodes due to different files on the nodes. - hostPathvolume usage is not treated as ephemeral storage usage. You need to monitor the disk usage by yourself because excessive hostPathdisk usage will lead to disk pressure on the node. 
Some uses for a hostPathare: 
- running a container that needs access to node-level system components (such as a container that transfers system logs to a central location, accessing those logs using a read-only mount of /var/log) - making a configuration file stored on the host system available read-only to a static Pod ; unlike normal Pods, static Pods cannot access ConfigMaps 
#### hostPathvolume types 
In addition to the required pathproperty, you can optionally specify a typefor a hostPathvolume. 
The available values for typeare: 
|  Value  | Behavior  |
|  ‌"" | Empty string (default) is for backward compatibility, which means that no checks will be performed before mounting the hostPathvolume.  |
|  DirectoryOrCreate | If nothing exists at the given path, an empty directory will be created there as needed with permission set to 0755, having the same group and ownership with Kubelet.  |
|  Directory | A directory must exist at the given path.  |
|  FileOrCreate | If nothing exists at the given path, an empty file will be created there as needed with permission set to 0644, having the same group and ownership with Kubelet.  |
|  File | A file must exist at the given path.  |
|  Socket | A UNIX socket must exist at the given path.  |
|  CharDevice | (Linux nodes only) A character device must exist at the given path.  |
|  BlockDevice | (Linux nodes only) A block device must exist at the given path.  |
#### Caution: The FileOrCreatemode does not create the parent directory of the file. If the parent directory of the mounted file does not exist, the Pod fails to start. To ensure that this mode works, you can try to mount directories and files separately, as shown in the FileOrCreateexample for hostPath. 
Some files or directories created on the underlying hosts might only be accessible by root. You then either need to run your process as root in a privileged container or modify the file permissions on the host to read from or write to a hostPathvolume. 
#### hostPath configuration example 
- Linux node - Windows node 
```
---# This manifest mounts /data/foo on the host as /foo inside the# single container that runs within the hostpath-example-linux Pod.## The mount into the container is read-only.apiVersion:v1kind:Podmetadata:name:hostpath-example-linuxspec:os:{name:linux }nodeSelector:kubernetes.io/os:linuxcontainers:- name:example-containerimage:registry.k8s.io/test-webservervolumeMounts:- mountPath:/fooname:example-volumereadOnly:truevolumes:- name:example-volume# mount /data/foo, but only if that directory already existshostPath:path:/data/foo# directory location on hosttype:Directory# this field is optional
```

```
---# This manifest mounts C:\Data\foo on the host as C:\foo, inside the# single container that runs within the hostpath-example-windows Pod.## The mount into the container is read-only.apiVersion:v1kind:Podmetadata:name:hostpath-example-windowsspec:os:{name:windows }nodeSelector:kubernetes.io/os:windowscontainers:- name:example-containerimage:microsoft/windowsservercore:1709volumeMounts:- name:example-volumemountPath:"C:\\foo"readOnly:truevolumes:# mount C:\Data\foo from the host, but only if that directory already exists- name:example-volumehostPath:path:"C:\\Data\\foo"# directory location on hosttype:Directory      # this field is optional
```

#### hostPath FileOrCreate configuration example 
The following manifest defines a Pod that mounts /var/local/aaainside the single container in the Pod. If the node does not already have a path /var/local/aaa, the kubelet creates it as a directory and then mounts it into the Pod. 
If /var/local/aaaalready exists but is not a directory, the Pod fails. Additionally, the kubelet attempts to make a file named /var/local/aaa/1.txtinside that directory (as seen from the host); if something already exists at that path and isn't a regular file, the Pod fails. 
Here's the example manifest: 
```
apiVersion:v1kind:Podmetadata:name:test-webserverspec:os:{name:linux }nodeSelector:kubernetes.io/os:linuxcontainers:- name:test-webserverimage:registry.k8s.io/test-webserver:latestvolumeMounts:- mountPath:/var/local/aaaname:mydir- mountPath:/var/local/aaa/1.txtname:myfilevolumes:- name:mydirhostPath:# Ensure the file directory is created.path:/var/local/aaatype:DirectoryOrCreate- name:myfilehostPath:path:/var/local/aaa/1.txttype:FileOrCreate
```

### image Feature state: Stable since Kubernetes v1.36; enabled by default More information about this feature 
This is a stable feature in , and has been since version 1.36. It was first available in the v1.31 release. 
An imagevolume source represents an OCI object (a container image or artifact) which is available on the kubelet's host machine. 
An example of using the imagevolume source is: pods/image-volumes.yaml
```
apiVersion:v1kind:Podmetadata:name:image-volumespec:containers:- name:shellcommand:["sleep","infinity"]image:debianvolumeMounts:- name:volumemountPath:/volumevolumes:- name:volumeimage:reference:quay.io/crio/artifact:v2pullPolicy:IfNotPresent
```

The volume is resolved at Pod startup, depending on which pullPolicyvalue is provided: AlwaysThe kubelet always attempts to pull the reference. If the pull fails, the kubelet sets the Pod to Failed. NeverThe kubelet never pulls the reference and only uses a local image or artifact. The Pod becomes Failedif any layers of the image aren't already present locally, or if the manifest for that image isn't already cached. IfNotPresentThe kubelet pulls if the reference isn't already present on disk. The Pod becomes Failedif the reference isn't present and the pull fails. 
The volume gets re-resolved if the Pod gets deleted and recreated, which means that new remote content will become available on Pod recreation. A failure to resolve or pull the image during Pod startup will block containers from starting and may add significant latency. Failures will be retried using normal volume backoff and will be reported on the Pod reason and message. 
The types of objects that may be mounted by this volume are defined by the container runtime implementation on a host machine. At a minimum, they must include all valid types supported by the container image field. The OCI object gets mounted in a single directory ( spec.containers[*].volumeMounts[*].mountPath) and will be mounted read-only. 
Besides that: 
- subPathor subPathExprmounts for containers ( spec.containers[*].volumeMounts[*].subPath, spec.containers[*].volumeMounts[*].subPathExpr) are only supported from Kubernetes v1.33. - The field spec.securityContext.fsGroupChangePolicyhas no effect on this volume type. - The AlwaysPullImagesAdmission Controller does also work for this volume source like for container images. 
The following fields are available for the imagetype: referenceArtifact reference to be used. For example, you could specify registry.k8s.io/conformance:v1.37.0to load the files from the Kubernetes conformance test image. Behaves in the same way as pod.spec.containers[*].image. Pull secrets will be assembled in the same way as for the container image by looking up node credentials, service account image pull secrets, and Pod spec image pull secrets. This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets. More info about container images . pullPolicyPolicy for pulling OCI objects. Possible values are: Always, Never, or IfNotPresent. Defaults to Alwaysif :latesttag is specified, or IfNotPresentotherwise. 
See the Use an Image Volume With a Pod example for more details on how to use the volume source. 
#### Pod status and imagevolumes Feature state: Alpha since Kubernetes v1.35; disabled by default More information about this feature 
To use this feature, you (or a cluster administrator) will need to enable the ImageVolumeWithDigest feature gate for all relevant components in your cluster. 
See Enable Or Disable Feature Gates for more information. 
If the ImageVolumeWithDigestfeature gate is enabled in your cluster, then whenever you specify an imagevolume for a Pod, the kubelet updates the Pod status to record the digest of the container image that's being used as a volume source. 
Here's a simplified example of a running Pod, represented as YAML, including the status update. Note the new ImageReffield under volumeMountsin the container status. 
```
apiVersion:v1kind:Podmetadata:name:my-podnamespace:defaultspec:containers:- name:shellcommand:["sleep","infinity"]image:docker.io/library/debian:12volumeMounts:- name:artifactmountPath:/datavolumes:- name:artifactimage:reference:quay.io/crio/artifact:v2pullPolicy:IfNotPresentstatus:containerStatuses:- containerID:containerd://examplecontainerid1234567890abcdefimage:docker.io/library/debian:12imageID:docker-pullable://docker.io/library/debian@sha256:3f1d6c17773a45c97bd8f158d665c9709d7b29ed7917ac934086ad96f92e4510volumeMounts:- name:artifactmountPath:/datareadOnly:trueimageRef:quay.io/crio/artifact@sha256:abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890
```

### iscsi 
An iscsivolume allows an existing iSCSI (SCSI over IP) volume to be mounted into your Pod. Unlike emptyDir, which is erased when a Pod is removed, the contents of an iscsivolume are preserved, and the volume is merely unmounted. This means that an iscsi volume can be pre-populated with data, and that data can be shared between Pods. 
#### Note: You must have your own iSCSI server running with the volume created before you can use it. 
A feature of iSCSI is that it can be mounted as read-only by multiple consumers simultaneously. This means that you can pre-populate a volume with your dataset and then serve it in parallel from as many Pods as you need. Unfortunately, iSCSI volumes can only be mounted by a single consumer in read-write mode. Simultaneous writers are not allowed. 
### local 
A localvolume represents a mounted local storage device such as a disk, partition or directory. 
Local volumes can only be used as a statically created PersistentVolume. Dynamic provisioning is not supported. 
Compared to hostPathvolumes, localvolumes are used in a durable and portable manner without manually scheduling Pods to nodes. The system is aware of the volume's node constraints by looking at the node affinity on the PersistentVolume. 
However, localvolumes are subject to the availability of the underlying node and are not suitable for all applications. If a node becomes unhealthy, then the localvolume becomes inaccessible to the Pod. The Pod using this volume is unable to run. Applications using localvolumes must be able to tolerate this reduced availability, as well as potential data loss, depending on the durability characteristics of the underlying disk. 
The following example shows a PersistentVolume using a localvolume and nodeAffinity: 
```
apiVersion:v1kind:PersistentVolumemetadata:name:example-pvspec:capacity:storage:100GivolumeMode:FilesystemaccessModes:- ReadWriteOncepersistentVolumeReclaimPolicy:DeletestorageClassName:local-storagelocal:path:/mnt/disks/ssd1nodeAffinity:required:nodeSelectorTerms:- matchExpressions:- key:kubernetes.io/hostnameoperator:Invalues:- example-node
```

You must set a PersistentVolume nodeAffinitywhen using localvolumes. The Kubernetes scheduler uses the PersistentVolume nodeAffinityto schedule these Pods to the correct node. 
PersistentVolume volumeModecan be set to "Block" (instead of the default value "Filesystem") to expose the local volume as a raw block device. 
When using local volumes, it is recommended to create a StorageClass with volumeBindingModeset to WaitForFirstConsumer. For more details, see the local StorageClass example. Delaying volume binding ensures that the PersistentVolumeClaim binding decision will also be evaluated with any other node constraints the Pod may have, such as node resource requirements, node selectors, Pod affinity, and Pod anti-affinity. 
An external static provisioner can be run separately for improved management of the local volume lifecycle. Note that this provisioner does not support dynamic provisioning yet. For an example on how to run an external local provisioner, see the local volume provisioner user guide . 
#### Note: The local PersistentVolume requires manual cleanup and deletion by the user if the external static provisioner is not used to manage the volume lifecycle. 
### nfs 
An nfsvolume allows an existing NFS (Network File System) share to be mounted into a Pod. Unlike emptyDir, which is erased when a Pod is removed, the contents of an nfsvolume are preserved, and the volume is merely unmounted. This means that an NFS volume can be pre-populated with data, and that data can be shared between Pods. NFS can be mounted by multiple writers simultaneously. 
```
apiVersion:v1kind:Podmetadata:name:test-pdspec:containers:- image:registry.k8s.io/test-webservername:test-containervolumeMounts:- mountPath:/my-nfs-dataname:test-volumevolumes:- name:test-volumenfs:server:my-nfs-server.example.compath:/my-nfs-volumereadOnly:true
```

#### Note: 
You must have your own NFS server running with the share exported before you can use it. 
Also note that you can't specify NFS mount options in a Pod spec. You can either set mount options server-side or use /etc/nfsmount.conf . You can also mount NFS volumes via PersistentVolumes, which do allow you to set mount options. 
### persistentVolumeClaim 
A persistentVolumeClaimvolume is used to mount a PersistentVolume into a Pod. PersistentVolumeClaims are a way for users to "claim" durable storage (such as an iSCSI volume) without knowing the details of the particular cloud environment. 
See the information about PersistentVolumes for more details. 
### portworxVolume (deprecated) Feature state: Deprecated since Kubernetes v1.25 
A portworxVolumeis an elastic block storage layer that runs hyperconverged with Kubernetes. Portworx fingerprints storage in a server, tiers based on capabilities, and aggregates capacity across multiple servers. Portworx runs in-guest in virtual machines or on bare metal Linux nodes. 
A portworxVolumecan be dynamically created through Kubernetes, or it can also be pre-provisioned and referenced inside a Pod. Here is an example Pod referencing a pre-provisioned Portworx volume: 
```
apiVersion:v1kind:Podmetadata:name:test-portworx-volume-podspec:containers:- image:registry.k8s.io/test-webservername:test-containervolumeMounts:- mountPath:/mntname:pxvolvolumes:- name:pxvol# This Portworx volume must already exist.portworxVolume:volumeID:"pxvol"fsType:"<fs-type>"
```

#### Note: Make sure you have an existing PortworxVolume with the name pxvolbefore using it in the Pod. 
#### Portworx CSI migration 
This is a stable feature in Kubernetes, and has been since the 1.33 release. You can no longer toggle this feature (the associated feature gate has been removed). 
In Kubernetes 1.37, all operations for the in-tree Portworx volumes are redirected to the pxd.portworx.comContainer Storage Interface (CSI) Driver by default. Portworx CSI Driver must be installed on the cluster. 
### projected 
A projected volume maps several existing volume sources into the same directory. For more details, see projected volumes . 
### secret 
A secretvolume is used to pass sensitive information, such as passwords, to Pods. You can store secrets in the Kubernetes API and mount them as files for use by Pods without coupling to Kubernetes directly. secretvolumes are backed by tmpfs (a RAM-backed filesystem), so they are never written to non-volatile storage. 
#### Note: 
- 
You must create a Secret in the Kubernetes API before you can use it. - 
A Secret is always mounted as readOnly. - 
A container using a Secret as a subPathvolume mount will not receive Secret updates. 
For more details, see Configuring Secrets . 
## Using subPath 
Sometimes, it is useful to share one volume for multiple uses in a single Pod. The volumeMounts[*].subPathproperty specifies a sub-path inside the referenced volume instead of its root. 
The following example shows how to configure a Pod with a LAMP stack (Linux, Apache, MySQL, PHP) using a single, shared volume. This sample subPathconfiguration is not recommended for production use. 
The PHP application's code and assets map to the volume's htmlfolder and the MySQL database is stored in the volume's mysqlfolder. For example: 
```
apiVersion:v1kind:Podmetadata:name:my-lamp-sitespec:containers:- name:mysqlimage:mysqlenv:- name:MYSQL_ROOT_PASSWORDvalue:"rootpasswd"volumeMounts:- mountPath:/var/lib/mysqlname:site-datasubPath:mysql- name:phpimage:php:7.0-apachevolumeMounts:- mountPath:/var/www/htmlname:site-datasubPath:htmlvolumes:- name:site-datapersistentVolumeClaim:claimName:my-lamp-site-data
```

### Using subPath with expanded environment variables Feature state: Stable since Kubernetes v1.17 
Use the subPathExprfield to construct subPathdirectory names from downward API environment variables. The subPathand subPathExprproperties are mutually exclusive. 
In this example, a Poduses subPathExprto create a directory pod1within the hostPathvolume /var/log/pods. The hostPathvolume takes the Podname from the downwardAPI. The host directory /var/log/pods/pod1is mounted at /logsin the container. 
```
apiVersion:v1kind:Podmetadata:name:pod1spec:containers:- name:container1env:- name:POD_NAMEvalueFrom:fieldRef:apiVersion:v1fieldPath:metadata.nameimage:busybox:1.28command:["sh","-c","while [ true ]; do echo 'Hello'; sleep 10; done | tee -a /logs/hello.txt"]volumeMounts:- name:workdir1mountPath:/logs# The variable expansion uses round brackets (not curly brackets).subPathExpr:$(POD_NAME)restartPolicy:Nevervolumes:- name:workdir1hostPath:path:/var/log/pods
```

## Resources 
The storage medium (such as Disk or SSD) of an emptyDirvolume is determined by the medium of the filesystem holding the kubelet root dir (typically /var/lib/kubelet). There is no limit on how much space an emptyDiror hostPathvolume can consume, and no isolation between containers or Pods. 
To learn about requesting space using a resource specification, see how to manage resources . 
## Out-of-tree volume plugins 
The out-of-tree volume plugins include Container Storage Interface (CSI), and also FlexVolume (which is deprecated). These plugins enable storage vendors to create custom storage plugins without adding their plugin source code to the Kubernetes repository. 
Previously, all volume plugins were "in-tree". The "in-tree" plugins were built, linked, compiled, and shipped with the core Kubernetes binaries. This meant that adding a new storage system to Kubernetes (a volume plugin) required checking code into the core Kubernetes code repository. 
Both CSI and FlexVolume allow volume plugins to be developed independently of the Kubernetes code base, and deployed (installed) on Kubernetes clusters as extensions. 
For storage vendors looking to create an out-of-tree volume plugin, please refer to the volume plugin FAQ . 
### csi 
Container Storage Interface (CSI) defines a standard interface for container orchestration systems (like Kubernetes) to expose arbitrary storage systems to their container workloads. 
Please read the CSI design proposal for more information. 
#### Note: Support for CSI spec versions 0.2 and 0.3 is deprecated in Kubernetes v1.13 and will be removed in a future release. 
#### Note: CSI drivers may not be compatible across all Kubernetes releases. Please check the specific CSI driver's documentation for supported deployment steps for each Kubernetes release and a compatibility matrix. 
Once a CSI-compatible volume driver is deployed on a Kubernetes cluster, users may use the csivolume type to attach or mount the volumes exposed by the CSI driver. 
A csivolume can be used in a Pod in three different ways: 
- through a reference to a PersistentVolumeClaim - with a generic ephemeral volume - with a CSI ephemeral volume if the driver supports that 
The following fields are available to storage administrators to configure a CSI persistent volume: 
- driver: A string value that specifies the name of the volume driver to use. This value must correspond to the value returned in the GetPluginInfoResponseby the CSI driver as defined in the CSI spec . It is used by Kubernetes to identify which CSI driver to call out to, and by CSI driver components to identify which PV objects belong to the CSI driver. - volumeHandle: A string value that uniquely identifies the volume. This value must correspond to the value returned in the volume.idfield of the CreateVolumeResponseby the CSI driver as defined in the CSI spec . The value is passed as volume_idin all calls to the CSI volume driver when referencing the volume. - readOnly: An optional boolean value indicating whether the volume is to be "ControllerPublished" (attached) as read-only. Default is false. This value is passed to the CSI driver via the readonlyfield in the ControllerPublishVolumeRequest. - fsType: If the PV's VolumeModeis Filesystem, then this field may be used to specify the filesystem that should be used to mount the volume. If the volume has not been formatted and formatting is supported, this value will be used to format the volume. This value is passed to the CSI driver via the VolumeCapabilityfield of ControllerPublishVolumeRequest, NodeStageVolumeRequest, and NodePublishVolumeRequest. - volumeAttributes: A map of string to string that specifies static properties of a volume. This map must correspond to the map returned in the volume.attributesfield of the CreateVolumeResponseby the CSI driver as defined in the CSI spec . The map is passed to the CSI driver via the volume_contextfield in the ControllerPublishVolumeRequest, NodeStageVolumeRequest, and NodePublishVolumeRequest. - controllerPublishSecretRef: A reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerPublishVolumeand ControllerUnpublishVolumecalls. This field is optional, and may be empty if no secret is required. If the Secret contains more than one secret, all secrets are passed. - nodeExpandSecretRef: A reference to the secret containing sensitive information to pass to the CSI driver to complete the CSI NodeExpandVolumecall. This field is optional and may be empty if no secret is required. If the object contains more than one secret, all secrets are passed. When you have configured secret data for node-initiated volume expansion, the kubelet passes that data via the NodeExpandVolume()call to the CSI driver. All supported versions of Kubernetes offer the nodeExpandSecretReffield, and have it available by default. Kubernetes releases prior to v1.25 did not include this support. - Enable the feature gate named CSINodeExpandSecretfor each kube-apiserver and for the kubelet on every node. Since Kubernetes version 1.27, this feature has been enabled by default and no explicit enablement of the feature gate is required. You must also be using a CSI driver that supports or requires secret data during node-initiated storage resize operations. - nodePublishSecretRef: A reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolumecall. This field is optional and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. - nodeStageSecretRef: A reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeStageVolumecall. This field is optional and may be empty if no secret is required. If the Secret contains more than one secret, all secrets are passed. 
#### CSI raw block volume support Feature state: Stable since Kubernetes v1.18 
Vendors with external CSI drivers can implement raw block volume support in Kubernetes workloads. 
You can set up your PersistentVolume/PersistentVolumeClaim with raw block volume support as usual, without any CSI-specific changes. 
#### CSI ephemeral volumes Feature state: Stable since Kubernetes v1.25 
You can directly configure CSI volumes within the Pod specification. Volumes specified in this way are ephemeral and do not persist across Pod restarts. See Ephemeral Volumes for more information. 
For more information on how to develop a CSI driver, refer to the kubernetes-csi documentation 
#### Windows CSI proxy Feature state: Stable since Kubernetes v1.22 
CSI node plugins need to perform various privileged operations like scanning of disk devices and mounting of file systems. These operations differ for each host operating system. For Linux worker nodes, containerized CSI node plugins are typically deployed as privileged containers. For Windows worker nodes, privileged operations for containerized CSI node plugins are supported using csi-proxy , a community-managed, stand-alone binary that needs to be pre-installed on each Windows node. 
For more details, refer to the deployment guide of the CSI plugin you wish to deploy. 
#### Migrating to CSI drivers from in-tree plugins Feature state: Stable since Kubernetes v1.25 
The CSIMigrationfeature directs operations against existing in-tree plugins to corresponding CSI plugins (which are expected to be installed and configured). As a result, operators do not have to make any configuration changes to existing Storage Classes, PersistentVolumes, or PersistentVolumeClaims (referring to in-tree plugins) when transitioning to a CSI driver that supersedes an in-tree plugin. 
#### Note: 
Existing PVs created by an in-tree volume plugin can still be used in the future without any configuration changes, even after the migration to CSI is completed for that volume type, and even after you upgrade to a version of Kubernetes that doesn't have compiled-in support for that kind of storage. 
As part of that migration, you - or another cluster administrator - must have installed and configured the appropriate CSI driver for that storage. The core of Kubernetes does not install that software for you. 
After that migration, you can also define new PVCs and PVs that refer to the legacy, built-in storage integrations. Provided you have the appropriate CSI driver installed and configured, the PV creation continues to work, even for brand-new volumes. The actual storage management now happens through the CSI driver. 
The operations and features that are supported include: provisioning/delete, attach/detach, mount/unmount, and resizing of volumes. 
In-tree plugins that support CSIMigrationand have a corresponding CSI driver implemented are listed in Types of Volumes . 
### flexVolume (deprecated) Feature state: Deprecated since Kubernetes v1.23 
FlexVolume is an out-of-tree plugin interface that uses an exec-based model to interface with storage drivers. The FlexVolume driver binaries must be installed in a pre-defined volume plugin path on each node, and in some cases, the control plane nodes as well. 
Pods interact with FlexVolume drivers through the flexVolumein-tree volume plugin. 
The following FlexVolume plugins , deployed as PowerShell scripts on the host, support Windows nodes: 
- SMB - iSCSI 
#### Note: 
FlexVolume is deprecated. Using an out-of-tree CSI driver is the recommended way to integrate external storage with Kubernetes. 
Maintainers of the FlexVolume driver should implement a CSI Driver and help migrate users of FlexVolume drivers to CSI. Users of FlexVolume should move their workloads to use the equivalent CSI Driver. 
## Mount propagation 
#### Caution: Mount propagation is a low-level feature that does not work consistently on all volume types. The Kubernetes project recommends only using mount propagation with hostPathor memory-backed emptyDirvolumes. See Kubernetes issue #95049 for more context. 
Mount propagation allows for sharing volumes mounted by a container to other containers in the same Pod, or even to other Pods on the same node. 
Mount propagation of a volume is controlled by the mountPropagationfield in containers[*].volumeMounts. Its values are: 
- 
None- This volume mount will not receive any subsequent mounts that are mounted to this volume or any of its subdirectories by the host. In a similar fashion, no mounts created by the container will be visible on the host. This is the default mode. 
This mode is equal to rprivatemount propagation as described in mount(8)
However, the CRI runtime may choose rslavemount propagation (i.e., HostToContainer) when rprivatepropagation is not applicable. cri-dockerd (Docker) is known to choose rslavemount propagation when the mount source contains the Docker daemon's root directory ( /var/lib/docker). - 
HostToContainer- This volume mount will receive all subsequent mounts that are mounted to this volume or any of its subdirectories. 
In other words, if the host mounts anything inside the volume mount, the container will see it mounted there. 
Similarly, if any Pod with Bidirectionalmount propagation to the same volume mounts anything there, the container with HostToContainermount propagation will see it. 
This mode is equal to rslavemount propagation as described in the mount(8)- 
Bidirectional- This volume mount behaves the same as the HostToContainermount. In addition, all volume mounts created by the container will be propagated back to the host and to all containers of all Pods that use the same volume. 
A typical use case for this mode is a Pod with a FlexVolume or CSI driver, or a Pod that needs to mount something on the host using a hostPathvolume. 
This mode is equal to rsharedmount propagation as described in the mount(8)
#### Warning: Bidirectionalmount propagation can be dangerous. It can damage the host operating system, and therefore, it is allowed only in privileged containers. Familiarity with Linux kernel behavior is strongly recommended. In addition, any volume mounts created by containers in Pods must be destroyed (unmounted) by the containers on termination. 
## Read-only mounts 
A mount can be made read-only by setting the .spec.containers[*].volumeMounts[*].readOnlyfield to true. This does not make the volume itself read-only, but that specific container will not be able to write to it. Other containers in the Pod may mount the same volume as read-write. 
On Linux, read-only mounts are not recursively read-only by default. For example, consider a Pod that mounts the hosts /mntas a hostPathvolume. If there is another filesystem mounted read-write on /mnt/<SUBMOUNT>(such as tmpfs, NFS, or USB storage), the volume mounted into the container(s) will also have a writeable /mnt/<SUBMOUNT>, even if the mount itself was specified as read-only. 
### Recursive read-only mounts Feature state: Stable since Kubernetes v1.33 More information about this feature 
This is a stable feature in Kubernetes, and has been since version v1.33. It was first available in the v1.30 release. You can no longer disable or opt out of this feature or behavior (it is locked); if you explicitly set a value for the associated feature gate RecursiveReadOnlyMounts , Kubernetes ignores it but does not report any error. 
Recursive read-only mounts can be enabled by setting the RecursiveReadOnlyMountsfeature gate for kubelet and kube-apiserver, and setting the .spec.containers[*].volumeMounts[*].recursiveReadOnlyfield for a Pod. 
The allowed values are: 
- 
Disabled(default): no effect. - 
Enabled: makes the mount recursively read-only. Needs all the following requirements to be satisfied: 
  - readOnlyis set to true  - mountPropagationis unset, or set to None  - The host is running with Linux kernel v5.12 or later   - The CRI-level container runtime supports recursive read-only mounts   - The OCI-level container runtime supports recursive read-only mounts. 
It will fail if any of these is not true. - 
IfPossible: attempts to apply Enabled, and falls back to Disabledif the feature is not supported by the kernel or the runtime class. 
Example: storage/rro.yaml
```
apiVersion:v1kind:Podmetadata:name:rrospec:volumes:- name:mnthostPath:# tmpfs is mounted on /mnt/tmpfspath:/mntcontainers:- name:busyboximage:busyboxargs:["sleep","infinity"]volumeMounts:# /mnt-rro/tmpfs is not writable- name:mntmountPath:/mnt-rroreadOnly:truemountPropagation:NonerecursiveReadOnly:Enabled# /mnt-ro/tmpfs is writable- name:mntmountPath:/mnt-roreadOnly:true# /mnt-rw/tmpfs is writable- name:mntmountPath:/mnt-rw
```

When this property is recognized by kubelet and kube-apiserver, the .status.containerStatuses[*].volumeMounts[*].recursiveReadOnlyfield is set to either Enabledor Disabled. 
## File owner 
### Group ownership (GID) 
Volume file group ownership (GID) is controlled by the pod's spec.securityContext.fsGroup. 
For detailed configuration steps, refer to Configure a Security Context for a Pod or Container . 
### User ownership (UID) Feature state: Alpha since Kubernetes v1.37; disabled by default More information about this feature 
To use this feature, you (or a cluster administrator) will need to enable the AtomicWriteVolumeUserFields feature gate for all relevant components in your cluster. 
See Enable Or Disable Feature Gates for more information. 
Setting the AtomicWriteVolumeUserFieldsfeature gate enables file user ownership (UID) fields of configMap, secret, downwardAPIand projectedvolumes. 
When defaultUseris specified at the volume level, it sets the owner UID for all its data files at creation time. At the item level, the userfield controls owner UID of an individual file and takes precedence over defaultUser. 
Example: 
```
apiVersion:v1kind:Podmetadata:name:volume-user-fields-examplespec:containers:- name:testimage:busybox:1.28command:['sh','-c','echo "The app is running!" && tail -f /dev/null']volumeMounts:- name:volAmountPath:/mnt/volA- name:volBmountPath:/mnt/volB- name:volCmountPath:/mnt/volCvolumes:- name:volAconfigMap:defaultUser:1000name:cm1items:- key:foo# Owner=defaultUserpath:foo- key:bar# Owner=userpath:baruser:1001- name:volBsecret:# Owner=defaultUserdefaultUser:1000secretName:secret1- name:volCprojected:sources:- secret:name:secret2items:- key:moo# Owner=rootpath:moo- key:baa# Owner=userpath:baauser:1000
```

#### Implementations Note: This section links to third party projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for these projects, which are listed alphabetically. To add a project to this list, read the content guide before submitting a change. More information. 
The following container runtimes are known to support recursive read-only mounts. 
CRI-level: 
- containerd , since v2.0 - CRI-O , since v1.30 
OCI-level: 
- runc , since v1.1 - crun , since v1.8.6 
## Bind mount options Feature state: Alpha since Kubernetes v1.37; disabled by default More information about this feature 
To use this feature, you (or a cluster administrator) will need to enable the VolumeBindMountOptions feature gate for all relevant components in your cluster. 
See Enable Or Disable Feature Gates for more information. 
The .spec.containers[*].volumeMounts[*].bindMountOptionsfield lets you apply security-related Linux bind mount flags to any volume mount. The allowed values are: 
- noexec- prevents execution of binaries on the mounted volume - nodev- ignores device special files on the mounted volume - nosuid- ignores set-user-identifier or set-group-identifier bits on the mounted volume 
These options apply per container, so different containers in the same Pod can mount the same volume with different bind mount options. The field is not supported with image volumes . 
#### Note: The container runtime (such as containerd or CRI-O) must support the mount_optionsfield in the CRI Mountmessage. If the runtime does not advertise support, the kubelet rejects Pods that use bindMountOptions. This field has no effect on Windows nodes. 
## What's next 
Follow an example of deploying WordPress and MySQL with Persistent Volumes . 
# 2 - Persistent Volumes 
This document describes persistent volumes in Kubernetes. Familiarity with volumes , StorageClasses and VolumeAttributesClasses is suggested. 
## Introduction 
Managing storage is a distinct problem from managing compute instances. The PersistentVolume subsystem provides an API for users and administrators that abstracts details of how storage is provided from how it is consumed. To do this, we introduce two new API resources: PersistentVolume and PersistentVolumeClaim. 
A PersistentVolume (PV) is a piece of storage in the cluster that has been provisioned by an administrator or dynamically provisioned using Storage Classes . It is a resource in the cluster just like a node is a cluster resource. PVs are volume plugins like Volumes, but have a lifecycle independent of any individual Pod that uses the PV. This API object captures the details of the implementation of the storage, be that NFS, iSCSI, or a cloud-provider-specific storage system. 
A PersistentVolumeClaim (PVC) is a request for storage by a user. It is similar to a Pod. Pods consume node resources and PVCs consume PV resources. Pods can request specific levels of resources (CPU and Memory). Claims can request specific size and access modes (e.g., they can be mounted ReadWriteOnce, ReadOnlyMany, ReadWriteMany, or ReadWriteOncePod, see AccessModes ). 
While PersistentVolumeClaims allow a user to consume abstract storage resources, it is common that users need PersistentVolumes with varying properties, such as performance, for different problems. Cluster administrators need to be able to offer a variety of PersistentVolumes that differ in more ways than size and access modes, without exposing users to the details of how those volumes are implemented. For these needs, there is the StorageClass resource. 
See the detailed walkthrough with working examples . 
## Lifecycle of a volume and claim 
PVs are resources in the cluster. PVCs are requests for those resources and also act as claim checks to the resource. The interaction between PVs and PVCs follows this lifecycle: 
### Provisioning 
There are two ways PVs may be provisioned: statically or dynamically. 
#### Static 
A cluster administrator creates a number of PVs. They carry the details of the real storage, which is available for use by cluster users. They exist in the Kubernetes API and are available for consumption. 
#### Dynamic 
When none of the static PVs the administrator created match a user's PersistentVolumeClaim, the cluster may try to dynamically provision a volume specially for the PVC. This provisioning is based on StorageClasses: the PVC must request a storage class and the administrator must have created and configured that class for dynamic provisioning to occur. Claims that request the class ""effectively disable dynamic provisioning for themselves. 
To enable dynamic storage provisioning based on storage class, the cluster administrator needs to enable the DefaultStorageClassadmission controller on the API server. This can be done, for example, by ensuring that DefaultStorageClassis among the comma-delimited, ordered list of values for the --enable-admission-pluginsflag of the API server component. For more information on API server command-line flags, check kube-apiserver documentation. 
### Binding 
A user creates, or in the case of dynamic provisioning, has already created, a PersistentVolumeClaim with a specific amount of storage requested and with certain access modes. A control loop in the control plane watches for new PVCs, finds a matching PV (if possible), and binds them together. If a PV was dynamically provisioned for a new PVC, the loop will always bind that PV to the PVC. Otherwise, the user will always get at least what they asked for, but the volume may be in excess of what was requested. Once bound, PersistentVolumeClaim binds are exclusive, regardless of how they were bound. A PVC to PV binding is a one-to-one mapping, using a ClaimRef which is a bi-directional binding between the PersistentVolume and the PersistentVolumeClaim. 
Claims will remain unbound indefinitely if a matching volume does not exist. Claims will be bound as matching volumes become available. For example, a cluster provisioned with many 50Gi PVs would not match a PVC requesting 100Gi. The PVC can be bound when a 100Gi PV is added to the cluster. 
### Using 
Pods use claims as volumes. The cluster inspects the claim to find the bound volume and mounts that volume for a Pod. For volumes that support multiple access modes, the user specifies which mode is desired when using their claim as a volume in a Pod. 
Once a user has a claim and that claim is bound, the bound PV belongs to the user for as long as they need it. Users schedule Pods and access their claimed PVs by including a persistentVolumeClaimsection in a Pod's volumesblock. See Claims As Volumes for more details on this. 
### Storage Object in Use Protection 
The purpose of the Storage Object in Use Protection feature is to ensure that PersistentVolumeClaims (PVCs) in active use by a Pod and PersistentVolume (PVs) that are bound to PVCs are not removed from the system, as this may result in data loss. 
#### Note: PVC is in active use by a Pod when a Pod object exists that is using the PVC. 
If a user deletes a PVC in active use by a Pod, the PVC is not removed immediately. PVC removal is postponed until the PVC is no longer actively used by any Pods. Also, if an admin deletes a PV that is bound to a PVC, the PV is not removed immediately. PV removal is postponed until the PV is no longer bound to a PVC. 
You can see that a PVC is protected when the PVC's status is Terminatingand the Finalizerslist includes kubernetes.io/pvc-protection: 
```
kubectl describe pvc hostpath
Name:          hostpath
Namespace:     default
StorageClass:  example-hostpath
Status:        Terminating
Volume:
Labels:        <none>
Annotations:   volume.beta.kubernetes.io/storage-class=example-hostpath
               volume.beta.kubernetes.io/storage-provisioner=example.com/hostpath
Finalizers:    [kubernetes.io/pvc-protection]...

```

You can see that a PV is protected when the PV's status is Terminatingand the Finalizerslist includes kubernetes.io/pv-protectiontoo: 
```
kubectl describe pv task-pv-volume
Name:            task-pv-volume
Labels:          type=localAnnotations:     <none>
Finalizers:      [kubernetes.io/pv-protection]StorageClass:    standard
Status:          Terminating
Claim:
Reclaim Policy:  Delete
Access Modes:    RWO
Capacity:        1Gi
Message:
Source:
    Type:          HostPath (bare host directory volume)    Path:          /tmp/data
    HostPathType:
Events:            <none>

```

### Reclaiming 
When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource. The reclaim policy for a PersistentVolume tells the cluster what to do with the volume after it has been released of its claim. Currently, volumes can either be Retained, Recycled, or Deleted. 
#### Retain 
The Retainreclaim policy allows for manual reclamation of the resource. When the PersistentVolumeClaim is deleted, the PersistentVolume still exists and the volume is considered "released". But it is not yet available for another claim because the previous claimant's data remains on the volume. An administrator can manually reclaim the volume with the following steps. 
- Delete the PersistentVolume. The associated storage asset in external infrastructure still exists after the PV is deleted. - Manually clean up the data on the associated storage asset accordingly. - Manually delete the associated storage asset. 
If you want to reuse the same storage asset, create a new PersistentVolume with the same storage asset definition. 
#### Delete 
For volume plugins that support the Deletereclaim policy, deletion removes both the PersistentVolume object from Kubernetes, as well as the associated storage asset in the external infrastructure. Volumes that were dynamically provisioned inherit the reclaim policy of their StorageClass , which defaults to Delete. The administrator should configure the StorageClass according to users' expectations; otherwise, the PV must be edited or patched after it is created. See Change the Reclaim Policy of a PersistentVolume . 
#### Recycle 
#### Warning: The Recyclereclaim policy is deprecated. Instead, the recommended approach is to use dynamic provisioning. 
If supported by the underlying volume plugin, the Recyclereclaim policy performs a basic scrub ( rm -rf /thevolume/*) on the volume and makes it available again for a new claim. 
However, an administrator can configure a custom recycler Pod template using the Kubernetes controller manager command line arguments as described in the reference . The custom recycler Pod template must contain a volumesspecification, as shown in the example below: 
```
apiVersion:v1kind:Podmetadata:name:pv-recyclernamespace:defaultspec:restartPolicy:Nevervolumes:- name:volhostPath:path:/any/path/it/will/be/replacedcontainers:- name:pv-recyclerimage:"registry.k8s.io/busybox"command:["/bin/sh","-c","test -e /scrub && rm -rf /scrub/..?* /scrub/.[!.]* /scrub/*  && test -z \"$(ls -A /scrub)\" || exit 1"]volumeMounts:- name:volmountPath:/scrub
```

However, the particular path specified in the custom recycler Pod template in the volumespart is replaced with the particular path of the volume that is being recycled. 
### PersistentVolume deletion protection finalizer 
This is a stable feature in Kubernetes, and has been since the 1.33 release. You can no longer toggle this feature (the associated feature gate has been removed). 
Finalizers can be added on a PersistentVolume to ensure that PersistentVolumes having Deletereclaim policy are deleted only after the backing storage are deleted. 
The finalizer external-provisioner.volume.kubernetes.io/finalizer(introduced in v1.31) is added to both dynamically provisioned and statically provisioned CSI volumes. 
The finalizer kubernetes.io/pv-controller(introduced in v1.31) is added to dynamically provisioned in-tree plugin volumes and skipped for statically provisioned in-tree plugin volumes. 
The following is an example of dynamically provisioned in-tree plugin volume: 
```
kubectl describe pv pvc-74a498d6-3929-47e8-8c02-078c1ece4d78
Name:            pvc-74a498d6-3929-47e8-8c02-078c1ece4d78
Labels:          <none>
Annotations:     kubernetes.io/createdby: vsphere-volume-dynamic-provisioner
                 pv.kubernetes.io/bound-by-controller: yes
                 pv.kubernetes.io/provisioned-by: kubernetes.io/vsphere-volume
Finalizers:      [kubernetes.io/pv-protection kubernetes.io/pv-controller]StorageClass:    vcp-sc
Status:          Bound
Claim:           default/vcp-pvc-1
Reclaim Policy:  Delete
Access Modes:    RWO
VolumeMode:      Filesystem
Capacity:        1Gi
Node Affinity:   <none>
Message:
Source:
    Type:               vSphereVolume (a Persistent Disk resource in vSphere)    VolumePath:         [vsanDatastore] d49c4a62-166f-ce12-c464-020077ba5d46/kubernetes-dynamic-pvc-74a498d6-3929-47e8-8c02-078c1ece4d78.vmdk
    FSType:             ext4
    StoragePolicyName:  vSAN Default Storage Policy
Events:                 <none>

```

The finalizer external-provisioner.volume.kubernetes.io/finalizeris added for CSI volumes. The following is an example: 
```
Name:            pvc-2f0bab97-85a8-4552-8044-eb8be45cf48d
Labels:          <none>
Annotations:     pv.kubernetes.io/provisioned-by: csi.vsphere.vmware.com
Finalizers:      [kubernetes.io/pv-protection external-provisioner.volume.kubernetes.io/finalizer]StorageClass:    fast
Status:          Bound
Claim:           demo-app/nginx-logs
Reclaim Policy:  Delete
Access Modes:    RWO
VolumeMode:      Filesystem
Capacity:        200Mi
Node Affinity:   <none>
Message:
Source:
    Type:              CSI (a Container Storage Interface (CSI) volume source)    Driver:            csi.vsphere.vmware.com
    FSType:            ext4
    VolumeHandle:      44830fa8-79b4-406b-8b58-621ba25353fd
    ReadOnly:          false    VolumeAttributes:      storage.kubernetes.io/csiProvisionerIdentity=1648442357185-8081-csi.vsphere.vmware.com
type=vSphere CNS Block Volume
Events:                <none>

```

When the CSIMigration{provider}feature flag is enabled for a specific in-tree volume plugin, the kubernetes.io/pv-controllerfinalizer is replaced by the external-provisioner.volume.kubernetes.io/finalizerfinalizer. 
The finalizers ensure that the PV object is removed only after the volume is deleted from the storage backend provided the reclaim policy of the PV is Delete. This also ensures that the volume is deleted from storage backend irrespective of the order of deletion of PV and PVC. 
### Reserving a PersistentVolume 
The control plane can bind PersistentVolumeClaims to matching PersistentVolumes in the cluster. However, if you want a PVC to bind to a specific PV, you need to pre-bind them. 
By specifying a PersistentVolume in a PersistentVolumeClaim, you declare a binding between that specific PV and PVC. If the PersistentVolume exists and has not reserved PersistentVolumeClaims through its claimReffield, then the PersistentVolume and PersistentVolumeClaim will be bound. 
The binding happens regardless of some volume matching criteria, including node affinity. The control plane still checks that storage class , access modes, and requested storage size are valid. 
```
apiVersion:v1kind:PersistentVolumeClaimmetadata:name:foo-pvcnamespace:foospec:storageClassName:""# Empty string must be explicitly set otherwise default StorageClass will be setvolumeName:foo-pv...
```

This method does not guarantee any binding privileges to the PersistentVolume. If other PersistentVolumeClaims could use the PV that you specify, you first need to reserve that storage volume. Specify the relevant PersistentVolumeClaim in the claimReffield of the PV so that other PVCs can not bind to it. 
```
apiVersion:v1kind:PersistentVolumemetadata:name:foo-pvspec:storageClassName:""claimRef:name:foo-pvcnamespace:foo...
```

This is useful if you want to consume PersistentVolumes that have their persistentVolumeReclaimPolicyset to Retain, including cases where you are reusing an existing PV. 
### Expanding Persistent Volumes Claims Feature state: Stable since Kubernetes v1.24 
Support for expanding PersistentVolumeClaims (PVCs) is enabled by default. You can expand the following types of volumes: 
- csi (including some CSI migrated volume types) - flexVolume (deprecated) - portworxVolume (deprecated) 
You can only expand a PVC if its storage class's allowVolumeExpansionfield is set to true. 
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:example-vol-defaultprovisioner:vendor-name.example/magicstorageparameters:resturl:"http://192.168.10.100:8080"restuser:""secretNamespace:""secretName:""allowVolumeExpansion:true
```

To request a larger volume for a PVC, edit the PVC object and specify a larger size. This triggers expansion of the volume that backs the underlying PersistentVolume. A new PersistentVolume is never created to satisfy the claim. Instead, an existing volume is resized. 
#### Warning: Directly editing the size of a PersistentVolume can prevent an automatic resize of that volume. If you edit the capacity of a PersistentVolume, and then edit the .specof a matching PersistentVolumeClaim to make the size of the PersistentVolumeClaim match the PersistentVolume, then no storage resize happens. The Kubernetes control plane will see that the desired state of both resources matches, conclude that the backing volume size has been manually increased and that no resize is necessary. 
#### CSI Volume expansion Feature state: Stable since Kubernetes v1.24 
Support for expanding CSI volumes is enabled by default but it also requires a specific CSI driver to support volume expansion. Refer to documentation of the specific CSI driver for more information. 
#### Resizing a volume containing a file system 
You can only resize volumes containing a file system if the file system is XFS, Ext3, or Ext4. 
When a volume contains a file system, the file system is only resized when a new Pod is using the PersistentVolumeClaim in ReadWritemode. File system expansion is either done when a Pod is starting up or when a Pod is running and the underlying file system supports online expansion. 
FlexVolumes (deprecated since Kubernetes v1.23) allow resize if the driver is configured with the RequiresFSResizecapability to true. The FlexVolume can be resized on Pod restart. 
#### Resizing an in-use PersistentVolumeClaim Feature state: Stable since Kubernetes v1.24 
In this case, you don't need to delete and recreate a Pod or deployment that is using an existing PVC. Any in-use PVC automatically becomes available to its Pod as soon as its file system has been expanded. This feature has no effect on PVCs that are not in use by a Pod or deployment. You must create a Pod that uses the PVC before the expansion can complete. 
Similar to other volume types - FlexVolume volumes can also be expanded when in-use by a Pod. 
#### Note: FlexVolume resize is possible only when the underlying driver supports resize. 
#### Recovering from Failure when Expanding Volumes 
If a user specifies a new size that is too big to be satisfied by underlying storage system, expansion of PVC will be continuously retried until user or cluster administrator takes some action. This can be undesirable and hence Kubernetes provides following methods of recovering from such failures. 
- Manually with Cluster Administrator access - By requesting expansion to smaller size 
If expanding underlying storage fails, the cluster administrator can manually recover the Persistent Volume Claim (PVC) state and cancel the resize requests. Otherwise, the resize requests are continuously retried by the controller without administrator intervention. 
- Mark the PersistentVolume(PV) that is bound to the PersistentVolumeClaim(PVC) with Retainreclaim policy. - Delete the PVC. Since PV has Retainreclaim policy - we will not lose any data when we recreate the PVC. - Delete the claimRefentry from PV specs, so as new PVC can bind to it. This should make the PV Available. - Re-create the PVC with smaller size than PV and set volumeNamefield of the PVC to the name of the PV. This should bind new PVC to existing PV. - Don't forget to restore the reclaim policy of the PV. 
If expansion has failed for a PVC, you can retry expansion with a smaller size than the previously requested value. To request a new expansion attempt with a smaller proposed size, edit .spec.resourcesfor that PVC and choose a value that is less than the value you previously tried. This is useful if expansion to a higher value did not succeed because of capacity constraint. If that has happened, or you suspect that it might have, you can retry expansion by specifying a size that is within the capacity limits of underlying storage provider. You can monitor status of resize operation by watching .status.allocatedResourceStatusesand events on the PVC. 
Note that, although you can specify a lower amount of storage than what was requested previously, the new value must still be higher than .status.capacity. Kubernetes does not support shrinking a PVC to less than its current size. 
## Types of Persistent Volumes 
PersistentVolume types are implemented as plugins. Kubernetes currently supports the following plugins: 
- csi- Container Storage Interface (CSI) - fc- Fibre Channel (FC) storage - hostPath- HostPath volume (for single node testing only; WILL NOT WORK in a multi-node cluster; consider using localvolume instead) - iscsi- iSCSI (SCSI over IP) storage - local- local storage devices mounted on nodes. - nfs- Network File System (NFS) storage 
The following types of PersistentVolume are deprecated but still available. If you are using these volume types except for flexVolume, cephfsand rbd, please install corresponding CSI drivers. 
- awsElasticBlockStore- AWS Elastic Block Store (EBS) ( migration on by default starting v1.23) - azureDisk- Azure Disk ( migration on by default starting v1.23) - azureFile- Azure File ( migration on by default starting v1.24) - cinder- Cinder (OpenStack block storage) ( migration on by default starting v1.21) - flexVolume- FlexVolume ( deprecated starting v1.23, no migration plan and no plan to remove support) - gcePersistentDisk- GCE Persistent Disk ( migration on by default starting v1.23) - portworxVolume- Portworx volume ( migration on by default starting v1.31) - vsphereVolume- vSphere VMDK volume ( migration on by default starting v1.25) 
Older versions of Kubernetes also supported the following in-tree PersistentVolume types: 
- cephfs( not available starting v1.31) - flocker- Flocker storage. ( not available starting v1.25) - glusterfs- GlusterFS storage. ( not available starting v1.26) - photonPersistentDisk- Photon controller persistent disk. ( not available starting v1.15) - quobyte- Quobyte volume. ( not available starting v1.25) - rbd- Rados Block Device (RBD) volume ( not available starting v1.31) - scaleIO- ScaleIO volume. ( not available starting v1.21) - storageos- StorageOS volume. ( not available starting v1.25) 
## Persistent Volumes 
Each PV contains a spec and status, which is the specification and status of the volume. The name of a PersistentVolume object must be a valid DNS subdomain name . 
```
apiVersion:v1kind:PersistentVolumemetadata:name:pv0003spec:capacity:storage:5GivolumeMode:FilesystemaccessModes:- ReadWriteOncepersistentVolumeReclaimPolicy:RecyclestorageClassName:slowmountOptions:- hard- nfsvers=4.1nfs:path:/tmpserver:172.17.0.2
```

#### Note: Helper programs relating to the volume type may be required for consumption of a PersistentVolume within a cluster. In this example, the PersistentVolume is of type NFS and the helper program /sbin/mount.nfs is required to support the mounting of NFS filesystems. 
### Capacity 
Generally, a PV will have a specific storage capacity. This is set using the PV's capacityattribute which is a Quantity value. 
Currently, storage size is the only resource that can be set or requested. Future attributes may include IOPS, throughput, etc. 
### Volume Mode Feature state: Stable since Kubernetes v1.18 
Kubernetes supports two volumeModesof PersistentVolumes: Filesystemand Block. 
volumeModeis an optional API parameter. Filesystemis the default mode used when volumeModeparameter is omitted. 
A volume with volumeMode: Filesystemis mounted into Pods into a directory. If the volume is backed by a block device and the device is empty, Kubernetes creates a filesystem on the device before mounting it for the first time. 
You can set the value of volumeModeto Blockto use a volume as a raw block device. Such volume is presented into a Pod as a block device, without any filesystem on it. This mode is useful to provide a Pod the fastest possible way to access a volume, without any filesystem layer between the Pod and the volume. On the other hand, the application running in the Pod must know how to handle a raw block device. See Raw Block Volume Support for an example on how to use a volume with volumeMode: Blockin a Pod. 
### Access Modes 
A PersistentVolume can be mounted on a host in any way supported by the resource provider. As shown in the table below, providers will have different capabilities and each PV's access modes are set to the specific modes supported by that particular volume. For example, NFS can support multiple read/write clients, but a specific NFS PV might be exported on the server as read-only. Each PV gets its own set of access modes describing that specific PV's capabilities. 
The access modes are: ReadWriteOncethe volume can be mounted as read-write by a single node. ReadWriteOnce access mode still can allow multiple pods to access (read from or write to) that volume when the pods are running on the same node. For single pod access, please see ReadWriteOncePod. ReadOnlyManythe volume can be mounted as read-only by many nodes. ReadWriteManythe volume can be mounted as read-write by many nodes. ReadWriteOncePodFeature state: Stable since Kubernetes v1.29 the volume can be mounted as read-write by a single Pod. Use ReadWriteOncePod access mode if you want to ensure that only one pod across the whole cluster can read that PVC or write to it. 
#### Note: 
The ReadWriteOncePodaccess mode is only supported for CSI volumes and Kubernetes version 1.22+. To use this feature you will need to update the following CSI sidecars to these versions or greater: 
- csi-provisioner:v3.0.0+ - csi-attacher:v3.3.0+ - csi-resizer:v1.3.0+ 
In the CLI, the access modes are abbreviated to: 
- RWO - ReadWriteOnce - ROX - ReadOnlyMany - RWX - ReadWriteMany - RWOP - ReadWriteOncePod 
#### Note: Kubernetes uses volume access modes to match PersistentVolumeClaims and PersistentVolumes. In some cases, the volume access modes also constrain where the PersistentVolume can be mounted. Volume access modes do not enforce write protection once the storage has been mounted. Even if the access modes are specified as ReadWriteOnce, ReadOnlyMany, or ReadWriteMany, they don't set any constraints on the volume. For example, even if a PersistentVolume is created as ReadOnlyMany, it is no guarantee that it will be read-only. If the access modes are specified as ReadWriteOncePod, the volume is constrained and can be mounted on only a single Pod. 
Important! A volume can only be mounted using one access mode at a time, even if it supports many. 
|  Volume Plugin  | ReadWriteOnce  | ReadOnlyMany  | ReadWriteMany  | ReadWriteOncePod  |
|  AzureFile  | ✓  | ✓  | ✓  | -  |
|  CephFS  | ✓  | ✓  | ✓  | -  |
|  CSI  | depends on the driver  | depends on the driver  | depends on the driver  | depends on the driver  |
|  FC  | ✓  | ✓  | -  | -  |
|  FlexVolume  | ✓  | ✓  | depends on the driver  | -  |
|  HostPath  | ✓  | -  | -  | -  |
|  iSCSI  | ✓  | ✓  | -  | -  |
|  NFS  | ✓  | ✓  | ✓  | -  |
|  RBD  | ✓  | ✓  | -  | -  |
|  VsphereVolume  | ✓  | -  | - (works when Pods are collocated)  | -  |
|  PortworxVolume  | ✓  | -  | ✓  | -  |
### Class 
A PV can have a class, which is specified by setting the storageClassNameattribute to the name of a StorageClass . A PV of a particular class can only be bound to PVCs requesting that class. A PV with no storageClassNamehas no class and can only be bound to PVCs that request no particular class. 
In the past, the annotation volume.beta.kubernetes.io/storage-classwas used instead of the storageClassNameattribute. This annotation is still working; however, it will become fully deprecated in a future Kubernetes release. 
### Reclaim Policy 
Current reclaim policies are: 
- Retain -- manual reclamation - Recycle -- basic scrub ( rm -rf /thevolume/*) - Delete -- delete the volume 
For Kubernetes 1.37, only nfsand hostPathvolume types support recycling. 
### Mount Options 
A Kubernetes administrator can specify additional mount options for when a Persistent Volume is mounted on a node. 
#### Note: Not all Persistent Volume types support mount options. 
The following volume types support mount options: 
- csi(including CSI migrated volume types) - iscsi- nfs
Mount options are not validated. If a mount option is invalid, the mount fails. 
In the past, the annotation volume.beta.kubernetes.io/mount-optionswas used instead of the mountOptionsattribute. This annotation is still working; however, it will become fully deprecated in a future Kubernetes release. 
### Node Affinity 
#### Note: For most volume types, you do not need to set this field. You need to explicitly set this for local volumes. 
A PV can specify node affinity to define constraints that limit what nodes this volume can be accessed from. Pods that use a PV will only be scheduled to nodes that are selected by the node affinity. To specify node affinity, set nodeAffinityin the .specof a PV. The PersistentVolume API reference has more details on this field. 
#### Updates to node affinity Feature state: Alpha since Kubernetes v1.35; disabled by default More information about this feature 
To use this feature, you (or a cluster administrator) will need to enable the MutablePVNodeAffinity feature gate for all relevant components in your cluster. 
See Enable Or Disable Feature Gates for more information. 
If the MutablePVNodeAffinityfeature gate is enabled in your cluster, the .spec.nodeAffinityfield of a PersistentVolume is mutable. This allows cluster administrators or external storage controller to update the node affinity of a PersistentVolume when the data is migrated, without interrupting the running pods. 
When updating the node affinity, you should ensure that the new node affinity still matches the nodes where the volume is currently in use. For the pods violating the new affinity, if the pod is already running, it may continue to run. But Kubernetes does not support this configuration. You should terminate the violating pods soon. Due to in memory caching, the pods created after the update may still be scheduled according to the old node affinity for a short period of time. 
To use this feature, you should enable the MutablePVNodeAffinityfeature gate on the following components: 
- kube-apiserver- kubelet
### Phase 
A PersistentVolume will be in one of the following phases: Availablea free resource that is not yet bound to a claim Boundthe volume is bound to a claim Releasedthe claim has been deleted, but the associated storage resource is not yet reclaimed by the cluster Failedthe volume has failed its (automated) reclamation 
You can see the name of the PVC bound to the PV using kubectl describe persistentvolume <name>. 
#### Phase transition timestamp 
This is a stable feature in Kubernetes, and has been since the 1.31 release. You can no longer toggle this feature (the associated feature gate has been removed). 
The .statusfield for a PersistentVolume can include an alpha lastPhaseTransitionTimefield. This field records the timestamp of when the volume last transitioned its phase. For newly created volumes the phase is set to Pendingand lastPhaseTransitionTimeis set to the current time. 
## PersistentVolumeClaims 
Each PVC contains a spec and status, which is the specification and status of the claim. The name of a PersistentVolumeClaim object must be a valid DNS subdomain name . 
```
apiVersion:v1kind:PersistentVolumeClaimmetadata:name:myclaimspec:accessModes:- ReadWriteOncevolumeMode:Filesystemresources:requests:storage:8GistorageClassName:slowselector:matchLabels:release:"stable"matchExpressions:- {key: environment, operator: In, values:[dev]}
```

### Access Modes 
Claims use the same conventions as volumes when requesting storage with specific access modes. 
### Volume Modes 
Claims use the same convention as volumes to indicate the consumption of the volume as either a filesystem or block device. 
### Volume Name 
Claims can use the volumeNamefield to explicitly bind to a specific PersistentVolume. You can also leave volumeNameunset, indicating that you'd like Kubernetes to set up a new PersistentVolume that matches the claim. If the specified PV is already bound to another PVC, the binding will be stuck in a pending state. 
### Resources 
Claims, like Pods, can request specific quantities of a resource. In this case, the request is for storage. The same resource model applies to both volumes and claims. 
#### Note: For Filesystemvolumes, the storage request refers to the "outer" volume size (i.e. the allocated size from the storage backend). This means that the writeable size may be slightly lower for providers that build a filesystem on top of a block device, due to filesystem overhead. This is especially visible with XFS, where many metadata features are enabled by default. 
### Selector 
Claims can specify a label selector to further filter the set of volumes. Only the volumes whose labels match the selector can be bound to the claim. The selector can consist of two fields: 
- matchLabels- the volume must have a label with this value - matchExpressions- a list of requirements made by specifying key, list of values, and operator that relates the key and values. Valid operators include In, NotIn, Exists, and DoesNotExist. 
All of the requirements, from both matchLabelsand matchExpressions, are ANDed together – they must all be satisfied in order to match. 
### Class 
A claim can request a particular class by specifying the name of a StorageClass using the attribute storageClassName. Only PVs of the requested class, ones with the same storageClassNameas the PVC, can be bound to the PVC. 
PVCs don't necessarily have to request a class. A PVC with its storageClassNameset equal to ""is always interpreted to be requesting a PV with no class, so it can only be bound to PVs with no class (no annotation or one set equal to ""). A PVC with no storageClassNameis not quite the same and is treated differently by the cluster, depending on whether the DefaultStorageClassadmission plugin is turned on. 
- If the admission plugin is turned on, the administrator may specify a default StorageClass. All PVCs that have no storageClassNamecan be bound only to PVs of that default. Specifying a default StorageClass is done by setting the annotation storageclass.kubernetes.io/is-default-classequal to truein a StorageClass object. If the administrator does not specify a default, the cluster responds to PVC creation as if the admission plugin were turned off. If more than one default StorageClass is specified, the newest default is used when the PVC is dynamically provisioned. - If the admission plugin is turned off, there is no notion of a default StorageClass. All PVCs that have storageClassNameset to ""can be bound only to PVs that have storageClassNamealso set to "". However, PVCs with missing storageClassNamecan be updated later once default StorageClass becomes available. If the PVC gets updated it will no longer bind to PVs that have storageClassNamealso set to "". 
See retroactive default StorageClass assignment for more details. 
Depending on installation method, a default StorageClass may be deployed to a Kubernetes cluster by addon manager during installation. 
When a PVC specifies a selectorin addition to requesting a StorageClass, the requirements are ANDed together: only a PV of the requested class and with the requested labels may be bound to the PVC. 
#### Note: Currently, a PVC with a non-empty selectorcan't have a PV dynamically provisioned for it. 
In the past, the annotation volume.beta.kubernetes.io/storage-classwas used instead of storageClassNameattribute. This annotation is still working; however, it won't be supported in a future Kubernetes release. 
#### Retroactive default StorageClass assignment Feature state: Stable since Kubernetes v1.28 
You can create a PersistentVolumeClaim without specifying a storageClassNamefor the new PVC, and you can do so even when no default StorageClass exists in your cluster. In this case, the new PVC creates as you defined it, and the storageClassNameof that PVC remains unset until default becomes available. 
When a default StorageClass becomes available, the control plane identifies any existing PVCs without storageClassName. For the PVCs that either have an empty value for storageClassNameor do not have this key, the control plane then updates those PVCs to set storageClassNameto match the new default StorageClass. If you have an existing PVC where the storageClassNameis "", and you configure a default StorageClass, then this PVC will not get updated. 
In order to keep binding to PVs with storageClassNameset to ""(while a default StorageClass is present), you need to set the storageClassNameof the associated PVC to "". 
This behavior helps administrators change default StorageClass by removing the old one first and then creating or setting another one. This brief window while there is no default causes PVCs without storageClassNamecreated at that time to not have any default, but due to the retroactive default StorageClass assignment this way of changing defaults is safe. 
### Unused PVC tracking Feature state: Beta since Kubernetes v1.37; enabled by default 
When enabled, the PVC protection controller adds an Unusedcondition to each PersistentVolumeClaim to indicate whether it is currently referenced by any non-terminal Pod. 
The condition has two states: Unusedwith status "True"(reason NoPodsUsingPVC) No non-terminal Pod references this PVC. The lastTransitionTimerecords when the PVC became unused. Unusedwith status "False"(reason PodUsingPVC) At least one non-terminal Pod currently references this PVC. The lastTransitionTimerecords when the PVC started being used. 
A Pod is considered non-terminal if its phase is not Succeededor Failed. This means that a Pending Pod (even one that has not yet been scheduled) counts as using the PVC. 
The lastTransitionTimeof the Unusedcondition can be used by cluster administrators, monitoring tools, and external controllers to identify PVCs that have been unused for a long time. For example, to find all PVCs that have been unused for more than 30 days, you could query for PVCs where the Unusedcondition has status: "True"and lastTransitionTimeis older than 30 days. 
#### Note: The unused duration indicated by this condition may be shorter than the actual unused time because of processing delays in the controller or because the feature was enabled after the PVC was already unused. The condition is not updated when a PVC has deletionTimestampset (that is, PVCs that are being deleted). 
## Claims As Volumes 
Pods access storage by using the claim as a volume. Claims must exist in the same namespace as the Pod using the claim. The cluster finds the claim in the Pod's namespace and uses it to get the PersistentVolume backing the claim. The volume is then mounted to the host and into the Pod. 
```
apiVersion:v1kind:Podmetadata:name:mypodspec:containers:- name:myfrontendimage:nginxvolumeMounts:- mountPath:"/var/www/html"name:mypdvolumes:- name:mypdpersistentVolumeClaim:claimName:myclaim
```

### A Note on Namespaces 
PersistentVolumes binds are exclusive, and since PersistentVolumeClaims are namespaced objects, mounting claims with "Many" modes ( ROX, RWX) is only possible within one namespace. 
### PersistentVolumes typed hostPath
A hostPathPersistentVolume uses a file or directory on the Node to emulate network-attached storage. See an example of hostPathtyped volume . 
## Raw Block Volume Support Feature state: Stable since Kubernetes v1.18 
The following volume plugins support raw block volumes, including dynamic provisioning where applicable: 
- CSI (including some CSI migrated volume types) - FC (Fibre Channel) - iSCSI - Local volume 
### PersistentVolume using a Raw Block Volume 
```
apiVersion:v1kind:PersistentVolumemetadata:name:block-pvspec:capacity:storage:10GiaccessModes:- ReadWriteOncevolumeMode:BlockpersistentVolumeReclaimPolicy:Retainfc:targetWWNs:["50060e801049cfd1"]lun:0readOnly:false
```

### PersistentVolumeClaim requesting a Raw Block Volume 
```
apiVersion:v1kind:PersistentVolumeClaimmetadata:name:block-pvcspec:accessModes:- ReadWriteOncevolumeMode:Blockresources:requests:storage:10Gi
```

### Pod specification adding Raw Block Device path in container 
```
apiVersion:v1kind:Podmetadata:name:pod-with-block-volumespec:containers:- name:fc-containerimage:fedora:26command:["/bin/sh","-c"]args:["tail -f /dev/null"]volumeDevices:- name:datadevicePath:/dev/xvdavolumes:- name:datapersistentVolumeClaim:claimName:block-pvc
```

#### Note: When adding a raw block device for a Pod, you specify the device path in the container instead of a mount path. 
### Binding Block Volumes 
If a user requests a raw block volume by indicating this using the volumeModefield in the PersistentVolumeClaim spec, the binding rules differ slightly from previous releases that didn't consider this mode as part of the spec. Listed is a table of possible combinations the user and admin might specify for requesting a raw block device. The table indicates if the volume will be bound or not given the combinations: Volume binding matrix for statically provisioned volumes: 
|  PV volumeMode  | PVC volumeMode  | Result  |
|  unspecified  | unspecified  | BIND  |
|  unspecified  | Block  | NO BIND  |
|  unspecified  | Filesystem  | BIND  |
|  Block  | unspecified  | NO BIND  |
|  Block  | Block  | BIND  |
|  Block  | Filesystem  | NO BIND  |
|  Filesystem  | Filesystem  | BIND  |
|  Filesystem  | Block  | NO BIND  |
|  Filesystem  | unspecified  | BIND  |
#### Note: Only statically provisioned volumes are supported for alpha release. Administrators should take care to consider these values when working with raw block devices. 
## Volume Snapshot and Restore Volume from Snapshot Support Feature state: Stable since Kubernetes v1.20 
Volume snapshots only support the out-of-tree CSI volume plugins. For details, see Volume Snapshots . In-tree volume plugins are deprecated. You can read about the deprecated volume plugins in the Volume Plugin FAQ . 
### Create a PersistentVolumeClaim from a Volume Snapshot 
```
apiVersion:v1kind:PersistentVolumeClaimmetadata:name:restore-pvcspec:storageClassName:csi-hostpath-scdataSource:name:new-snapshot-testkind:VolumeSnapshotapiGroup:snapshot.storage.k8s.ioaccessModes:- ReadWriteOnceresources:requests:storage:10Gi
```

## Volume Cloning 
Volume Cloning only available for CSI volume plugins. 
### Create PersistentVolumeClaim from an existing PVC 
```
apiVersion:v1kind:PersistentVolumeClaimmetadata:name:cloned-pvcspec:storageClassName:my-csi-plugindataSource:name:existing-src-pvc-namekind:PersistentVolumeClaimaccessModes:- ReadWriteOnceresources:requests:storage:10Gi
```

## Volume populators and data sources 
Volume cloning and snapshot restore pre-populate a new volume from a built-in data source . Volume populators extend this mechanism so that a PersistentVolumeClaim can be pre-populated from other kinds of source (a custom resource), referenced through its dataSourceReffield: 
```
apiVersion:v1kind:PersistentVolumeClaimmetadata:name:populated-pvcspec:dataSourceRef:name:example-namekind:ExampleDataSourceapiGroup:example.storage.k8s.ioaccessModes:- ReadWriteOnceresources:requests:storage:10Gi
```

For details, including cross-namespace data sources, see Volume Populators and Data Sources . 
## Writing Portable Configuration 
If you're writing configuration templates or examples that run on a wide range of clusters and need persistent storage, it is recommended that you use the following pattern: 
- Include PersistentVolumeClaim objects in your bundle of config (alongside Deployments, ConfigMaps, etc). - Do not include PersistentVolume objects in the config, since the user instantiating the config may not have permission to create PersistentVolumes. - Give the user the option of providing a storage class name when instantiating the template. 
  - If the user provides a storage class name, put that value into the persistentVolumeClaim.storageClassNamefield. This will cause the PVC to match the right storage class if the cluster has StorageClasses enabled by the admin.   - If the user does not provide a storage class name, leave the persistentVolumeClaim.storageClassNamefield as nil. This will cause a PV to be automatically provisioned for the user with the default StorageClass in the cluster. Many cluster environments have a default StorageClass installed, or administrators can create their own default StorageClass. - In your tooling, watch for PVCs that are not getting bound after some time and surface this to the user, as this may indicate that the cluster has no dynamic storage support (in which case the user should create a matching PV) or the cluster has no storage system (in which case the user cannot deploy config requiring PVCs). 
## What's next 
- Learn more about Creating a PersistentVolume . - Learn more about Creating a PersistentVolumeClaim . - Read the Persistent Storage design document . 
### API references 
Read about the APIs described in this page: 
- PersistentVolume- PersistentVolumeClaim
# 3 - Projected Volumes 
This document describes projected volumes in Kubernetes. Familiarity with volumes is suggested. 
## Introduction 
A projectedvolume maps several existing volume sources into the same directory. 
Currently, the following types of volume sources can be projected: 
- secret- downwardAPI- configMap- serviceAccountToken- clusterTrustBundle- podCertificate
All sources are required to be in the same namespace as the Pod. For more details, see the all-in-one volume design document. 
### Example configuration with a secret, a downwardAPI, and a configMap pods/storage/projected-secret-downwardapi-configmap.yaml
```
apiVersion:v1kind:Podmetadata:name:volume-testspec:containers:- name:container-testimage:busybox:1.28command:["sleep","3600"]volumeMounts:- name:all-in-onemountPath:"/projected-volume"readOnly:truevolumes:- name:all-in-oneprojected:sources:- secret:name:mysecretitems:- key:usernamepath:my-group/my-username- downwardAPI:items:- path:"labels"fieldRef:fieldPath:metadata.labels- path:"cpu_limit"resourceFieldRef:containerName:container-testresource:limits.cpu- configMap:name:myconfigmapitems:- key:configpath:my-group/my-config
```

### Example configuration: secrets with a non-default permission mode set pods/storage/projected-secrets-nondefault-permission-mode.yaml
```
apiVersion:v1kind:Podmetadata:name:volume-testspec:containers:- name:container-testimage:busybox:1.28command:["sleep","3600"]volumeMounts:- name:all-in-onemountPath:"/projected-volume"readOnly:truevolumes:- name:all-in-oneprojected:sources:- secret:name:mysecretitems:- key:usernamepath:my-group/my-username- secret:name:mysecret2items:- key:passwordpath:my-group/my-passwordmode:0777
```

Each projected volume source is listed in the spec under sources. The parameters are nearly the same with two exceptions: 
- For secrets, the secretNamefield has been changed to nameto be consistent with ConfigMap naming. - The defaultModecan only be specified at the projected level and not for each volume source. However, as illustrated above, you can explicitly set the modefor each individual projection. 
## serviceAccountToken projected volumes 
You can inject the token for the current service account into a Pod at a specified path. For example: pods/storage/projected-service-account-token.yaml
```
apiVersion:v1kind:Podmetadata:name:sa-token-testspec:containers:- name:container-testimage:busybox:1.28command:["sleep","3600"]volumeMounts:- name:token-volmountPath:"/service-account"readOnly:trueserviceAccountName:defaultvolumes:- name:token-volprojected:sources:- serviceAccountToken:audience:apiexpirationSeconds:3600path:token
```

The example Pod has a projected volume containing the injected service account token. Containers in this Pod can use that token to access the Kubernetes API server, authenticating with the identity of the pod's ServiceAccount . The audiencefield contains the intended audience of the token. A recipient of the token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. This field is optional and it defaults to the identifier of the API server. 
The expirationSecondsis the expected duration of validity of the service account token. It defaults to 1 hour and must be at least 10 minutes (600 seconds). An administrator can also limit its maximum value by specifying the --service-account-max-token-expirationoption for the API server. The pathfield specifies a relative path to the mount point of the projected volume. 
#### Note: A container using a projected volume source as a subPathvolume mount will not receive updates for those volume sources. 
## clusterTrustBundle projected volumes Feature state: Stable since Kubernetes v1.37; enabled by default More information about this feature 
This is a stable feature in , and has been since version 1.37. It was first available in the v1.29 release. 
The clusterTrustBundleprojected volume source injects the contents of one or more ClusterTrustBundle objects as an automatically-updating file in the container filesystem. 
ClusterTrustBundles can be selected either by name or by signer name . 
To select by name, use the namefield to designate a single ClusterTrustBundle object. 
To select by signer name, use the signerNamefield (and optionally the labelSelectorfield) to designate a set of ClusterTrustBundle objects that use the given signer name. If labelSelectoris not present, then all ClusterTrustBundles for that signer are selected. 
The kubelet deduplicates the certificates in the selected ClusterTrustBundle objects, normalizes the PEM representations (discarding comments and headers), reorders the certificates, and writes them into the file named by path. As the set of selected ClusterTrustBundles or their content changes, kubelet keeps the file up-to-date. 
By default, the kubelet will prevent the pod from starting if the named ClusterTrustBundle is not found, or if signerName/ labelSelectordo not match any ClusterTrustBundles. If this behavior is not what you want, then set the optionalfield to true, and the pod will start up with an empty file at path. pods/storage/projected-clustertrustbundle.yaml
```
apiVersion:v1kind:Podmetadata:name:sa-ctb-name-testspec:containers:- name:container-testimage:busyboxcommand:["sleep","3600"]volumeMounts:- name:token-volmountPath:"/root-certificates"readOnly:trueserviceAccountName:defaultvolumes:- name:token-volprojected:sources:- clusterTrustBundle:name:examplepath:example-roots.pem- clusterTrustBundle:signerName:"example.com/mysigner"labelSelector:matchLabels:version:livepath:mysigner-roots.pemoptional:true
```

## podCertificate projected volumes Feature state: Stable since Kubernetes v1.37; enabled by default More information about this feature 
This is a stable feature in , and has been since version 1.37. It was first available in the v1.34 release. 
The podCertificateprojected volumes source securely provisions a private key and X.509 certificate chain for pod to use as client or server credentials. Kubelet will then handle refreshing the private key and certificate chain when they get close to expiration. The application just has to make sure that it reloads the file promptly when it changes, with a mechanism like inotifyor polling. 
Each podCertificateprojection supports the following configuration fields: 
- signerName: The signer you want to issue the certificate. Note that signers may have their own access requirements, and may refuse to issue certificates to your pod. - keyType: The type of private key that should be generated. Valid values are ED25519, ECDSAP256, ECDSAP384, ECDSAP521, RSA3072, and RSA4096. - maxExpirationSeconds: The maximum lifetime you will accept for the certificate issued to the pod. If not set, will be defaulted to 86400(24 hours). Must be at least 3600(1 hour), and at most 7862400(91 days). Kubernetes built-in signers are restricted to a max lifetime of 86400(1 day). The signer is allowed to issue a certificate with a lifetime shorter than what you've specified. - credentialBundlePath: Relative path within the projection where the credential bundle should be written. The credential bundle is a PEM-formatted file, where the first block is a "PRIVATE KEY" block that contains a PKCS#8-serialized private key, and the remaining blocks are "CERTIFICATE" blocks that comprise the certificate chain (leaf certificate and any intermediates). - keyPathand certificateChainPath: Separate paths where Kubelet should write just the private key or certificate chain. - userAnnotations: a map that allows you to pass additional information to the signer implementation. It is copied verbatim into the spec.unverifiedUserAnnotationsfield of the PodCertificateRequest objects that Kubelet creates. Entries are subject to the same validation as object metadata annotations, with the addition that all keys must be domain-prefixed. No restrictions are placed on values, except an overall size limitation on the entire field. Other than these basic validations, the API server does not conduct any extra validations. The signer implementations should be very careful when consuming this data. Signers must not inherently trust this data without first performing the appropriate verification steps. Signers should document the keys and values they support. Signers should deny requests that contain keys they do not recognize. 
#### Note: Most applications should prefer using credentialBundlePathunless they need the key and certificates in separate files for compatibility reasons. Kubelet uses an atomic writing strategy based on symlinks to make sure that when you open the files it projects, you read either the old content or the new content. However, if you read the key and certificate chain from separate files, Kubelet may rotate the credentials after your first read and before your second read, resulting in your application loading a mismatched key and certificate. pods/storage/projected-podcertificate.yaml
```
# Sample Pod spec that uses a podCertificate projection to request an ED25519# private key, a certificate from the `coolcert.example.com/foo` signer, and# write the results to `/var/run/my-x509-credentials/credentialbundle.pem`.apiVersion:v1kind:Podmetadata:namespace:defaultname:podcertificate-podspec:serviceAccountName:defaultcontainers:- image:debianname:maincommand:["sleep","infinity"]volumeMounts:- name:my-x509-credentialsmountPath:/var/run/my-x509-credentialsvolumes:- name:my-x509-credentialsprojected:defaultMode:0644sources:- podCertificate:keyType:ED25519signerName:coolcert.example.com/foocredentialBundlePath:credentialbundle.pemuserAnnotations:example.com/annotation1:"value1"example.com/annotation2:"value2"
```

## SecurityContext interactions 
The proposal for file permission handling in projected service account volume enhancement introduced the projected files having the correct owner permissions set. 
### Linux 
In Linux pods that have a projected volume and RunAsUserset in the Pod SecurityContext, the projected files have the correct ownership set including container user ownership. 
When all containers in a pod have the same runAsUserset in their PodSecurityContextor container SecurityContext, then the kubelet ensures that the contents of the serviceAccountTokenvolume are owned by that user, and the token file has its permission mode set to 0600. 
#### Note: 
Ephemeral containers added to a Pod after it is created do not change volume permissions that were set when the pod was created. 
If a Pod's serviceAccountTokenvolume permissions were set to 0600because all other containers in the Pod have the same runAsUser, ephemeral containers must use the same runAsUserto be able to read the token. 
### Windows 
In Windows pods that have a projected volume and RunAsUsernameset in the Pod SecurityContext, the ownership is not enforced due to the way user accounts are managed in Windows. Windows stores and manages local user and group accounts in a database file called Security Account Manager (SAM). Each container maintains its own instance of the SAM database, to which the host has no visibility into while the container is running. Windows containers are designed to run the user mode portion of the OS in isolation from the host, hence the maintenance of a virtual SAM database. As a result, the kubelet running on the host does not have the ability to dynamically configure host file ownership for virtualized container accounts. It is recommended that if files on the host machine are to be shared with the container then they should be placed into their own volume mount outside of C:\. 
By default, the projected files will have the following ownership as shown for an example projected volume file: 
```
PS C:\>Get-AclC:\var\run\secrets\kubernetes.io\serviceaccount\..2021_08_31_22_22_18.318230061\ca.crt|Format-ListPath:Microsoft.PowerShell.Core\FileSystem::C:\var\run\secrets\kubernetes.io\serviceaccount\..2021_08_31_22_22_18.318230061\ca.crtOwner:BUILTIN\AdministratorsGroup :NTAUTHORITY\SYSTEMAccess:NTAUTHORITY\SYSTEMAllowFullControlBUILTIN\AdministratorsAllowFullControlBUILTIN\UsersAllowReadAndExecute,SynchronizeAudit:Sddl:O:BAG:SYD:AI(A;ID;FA;;;SY)(A;ID;FA;;;BA)(A;ID;0x1200a9;;;BU)
```

This implies all administrator users like ContainerAdministratorwill have read, write and execute access while, non-administrator users will have read and execute access. 
#### Note: 
In general, granting the container access to the host is discouraged as it can open the door for potential security exploits. 
Creating a Windows Pod with RunAsUserin it's SecurityContextwill result in the Pod being stuck at ContainerCreatingforever. So it is advised to not use the Linux only RunAsUseroption with Windows Pods. 
# 4 - Ephemeral Volumes 
This document describes ephemeral volumes in Kubernetes. Familiarity with volumes is suggested, in particular PersistentVolumeClaim and PersistentVolume. 
Some applications need additional storage but don't care whether that data is stored persistently across restarts. For example, caching services are often limited by memory size and can move infrequently used data into storage that is slower than memory with little impact on overall performance. 
Other applications expect some read-only input data to be present in files, like configuration data or secret keys. 
Ephemeral volumes are designed for these use cases. Because volumes follow the Pod's lifetime and get created and deleted along with the Pod, Pods can be stopped and restarted without being limited to where some persistent volume is available. 
Ephemeral volumes are specified inline in the Pod spec, which simplifies application deployment and management. 
### Types of ephemeral volumes 
Kubernetes supports several different kinds of ephemeral volumes for different purposes: 
- emptyDir : empty at Pod startup, with storage coming locally from the kubelet base directory (usually the root disk) or RAM - configMap , downwardAPI , secret : inject different kinds of Kubernetes data into a Pod - image : allows mounting container image files or artifacts, directly to a Pod. - CSI ephemeral volumes : similar to the previous volume kinds, but provided by special CSI drivers which specifically support this feature - generic ephemeral volumes , which can be provided by all storage drivers that also support persistent volumes 
emptyDir, configMap, downwardAPI, secretare provided as local ephemeral storage . They are managed by kubelet on each node. 
CSI ephemeral volumes must be provided by third-party CSI storage drivers. 
Generic ephemeral volumes can be provided by third-party CSI storage drivers, but also by any other storage driver that supports dynamic provisioning. Some CSI drivers are written specifically for CSI ephemeral volumes and do not support dynamic provisioning: those then cannot be used for generic ephemeral volumes. 
The advantage of using third-party drivers is that they can offer functionality that Kubernetes itself does not support, for example storage with different performance characteristics than the disk that is managed by kubelet, or injecting different data. 
### CSI ephemeral volumes Feature state: Stable since Kubernetes v1.25 
#### Note: CSI ephemeral volumes are only supported by a subset of CSI drivers. The Kubernetes CSI Drivers list shows which drivers support ephemeral volumes. 
Conceptually, CSI ephemeral volumes are similar to configMap, downwardAPIand secretvolume types: the storage is managed locally on each node and is created together with other local resources after a Pod has been scheduled onto a node. Kubernetes has no concept of rescheduling Pods anymore at this stage. Volume creation has to be unlikely to fail, otherwise Pod startup gets stuck. In particular, storage capacity aware Pod scheduling is not supported for these volumes. They are currently also not covered by the storage resource usage limits of a Pod, because that is something that kubelet can only enforce for storage that it manages itself. 
Here's an example manifest for a Pod that uses CSI ephemeral storage: 
```
kind:PodapiVersion:v1metadata:name:my-csi-appspec:containers:- name:my-frontendimage:busybox:1.28volumeMounts:- mountPath:"/data"name:my-csi-inline-volcommand:["sleep","1000000"]volumes:- name:my-csi-inline-volcsi:driver:inline.storage.kubernetes.iovolumeAttributes:foo:bar
```

The volumeAttributesdetermine what volume is prepared by the driver. These attributes are specific to each driver and not standardized. See the documentation of each CSI driver for further instructions. 
### CSI driver restrictions 
CSI ephemeral volumes allow users to provide volumeAttributesdirectly to the CSI driver as part of the Pod spec. A CSI driver allowing volumeAttributesthat are typically restricted to administrators is NOT suitable for use in an inline ephemeral volume. For example, parameters that are normally defined in the StorageClass should not be exposed to users through the use of inline ephemeral volumes. 
Cluster administrators who need to restrict the CSI drivers that are allowed to be used as inline volumes within a Pod spec may do so by: 
- Removing Ephemeralfrom volumeLifecycleModesin the CSIDriver spec, which prevents the driver from being used as an inline ephemeral volume. - Using an admission webhook to restrict how this driver is used. 
### Generic ephemeral volumes Feature state: Stable since Kubernetes v1.23 
Generic ephemeral volumes are similar to emptyDirvolumes in the sense that they provide a per-pod directory for scratch data that is usually empty after provisioning. But they may also have additional features: 
- Storage can be local or network-attached. - Volumes can have a fixed size that Pods are not able to exceed. - Volumes may have some initial data, depending on the driver and parameters. - Typical operations on volumes are supported assuming that the driver supports them, including snapshotting , cloning , resizing , and storage capacity tracking . 
Example: 
```
kind:PodapiVersion:v1metadata:name:my-appspec:containers:- name:my-frontendimage:busybox:1.28volumeMounts:- mountPath:"/scratch"name:scratch-volumecommand:["sleep","1000000"]volumes:- name:scratch-volumeephemeral:volumeClaimTemplate:metadata:labels:type:my-frontend-volumespec:accessModes:["ReadWriteOnce"]storageClassName:"scratch-storage-class"resources:requests:storage:1Gi
```

### Lifecycle and PersistentVolumeClaim 
The key design idea is that the parameters for a volume claim are allowed inside a volume source of the Pod. Labels, annotations and the whole set of fields for a PersistentVolumeClaim are supported. When such a Pod gets created, the ephemeral volume controller then creates an actual PersistentVolumeClaim object in the same namespace as the Pod and ensures that the PersistentVolumeClaim gets deleted when the Pod gets deleted. 
That triggers volume binding and/or provisioning, either immediately if the StorageClass uses immediate volume binding or when the Pod is tentatively scheduled onto a node ( WaitForFirstConsumervolume binding mode). The latter is recommended for generic ephemeral volumes because then the scheduler is free to choose a suitable node for the Pod. With immediate binding, the scheduler is forced to select a node that has access to the volume once it is available. 
In terms of resource ownership , a Pod that has generic ephemeral storage is the owner of the PersistentVolumeClaim(s) that provide that ephemeral storage. When the Pod is deleted, the Kubernetes garbage collector deletes the PVC, which then usually triggers deletion of the volume because the default reclaim policy of storage classes is to delete volumes. You can create quasi-ephemeral local storage using a StorageClass with a reclaim policy of retain: the storage outlives the Pod, and in this case you need to ensure that volume clean up happens separately. 
While these PVCs exist, they can be used like any other PVC. In particular, they can be referenced as data source in volume cloning or snapshotting. The PVC object also holds the current status of the volume. 
### PersistentVolumeClaim naming 
Naming of the automatically created PVCs is deterministic: the name is a combination of the Pod name and volume name, with a hyphen ( -) in the middle. In the example above, the PVC name will be my-app-scratch-volume. This deterministic naming makes it easier to interact with the PVC because one does not have to search for it once the Pod name and volume name are known. 
The deterministic naming also introduces a potential conflict between different Pods (a Pod "pod-a" with volume "scratch" and another Pod with name "pod" and volume "a-scratch" both end up with the same PVC name "pod-a-scratch") and between Pods and manually created PVCs. 
Such conflicts are detected: a PVC is only used for an ephemeral volume if it was created for the Pod. This check is based on the ownership relationship. An existing PVC is not overwritten or modified. But this does not resolve the conflict because without the right PVC, the Pod cannot start. 
#### Caution: Take care when naming Pods and volumes inside the same namespace, so that these conflicts can't occur. 
### Security 
Using generic ephemeral volumes allows users to create PVCs indirectly if they can create Pods, even if they do not have permission to create PVCs directly. Cluster administrators must be aware of this. If this does not fit their security model, they should use an admission webhook that rejects objects like Pods that have a generic ephemeral volume. 
The normal namespace quota for PVCs still applies, so even if users are allowed to use this new mechanism, they cannot use it to circumvent other policies. 
## What's next 
### Ephemeral volumes managed by kubelet 
See local ephemeral storage . 
### CSI ephemeral volumes 
- For more information on the design, see the Ephemeral Inline CSI volumes KEP . - For more information on further development of this feature, see the enhancement tracking issue #596 . 
### Generic ephemeral volumes 
- For more information on the design, see the Generic ephemeral inline volumes KEP . 
# 5 - Storage Classes 
This document describes the concept of a StorageClass in Kubernetes. Familiarity with volumes and persistent volumes is suggested. 
A StorageClass provides a way for administrators to describe the classes of storage they offer. Different classes might map to quality-of-service levels, or to backup policies, or to arbitrary policies determined by the cluster administrators. Kubernetes itself is unopinionated about what classes represent. 
The Kubernetes concept of a storage class is similar to “profiles” in some other storage system designs. 
## StorageClass objects 
Each StorageClass contains the fields provisioner, parameters, and reclaimPolicy, which are used when a PersistentVolume belonging to the class needs to be dynamically provisioned to satisfy a PersistentVolumeClaim (PVC). 
The name of a StorageClass object is significant, and is how users can request a particular class. Administrators set the name and other parameters of a class when first creating StorageClass objects. 
As an administrator, you can specify a default StorageClass that applies to any PVCs that don't request a specific class. For more details, see the PersistentVolumeClaim concept . 
Here's an example of a StorageClass: storage/storageclass-low-latency.yaml
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:low-latencyannotations:storageclass.kubernetes.io/is-default-class:"false"provisioner:csi-driver.example-vendor.examplereclaimPolicy:Retain# default value is DeleteallowVolumeExpansion:truemountOptions:- discard# this might enable UNMAP / TRIM at the block storage layervolumeBindingMode:WaitForFirstConsumerparameters:guaranteedReadWriteLatency:"true"# provider-specific
```

## Default StorageClass 
You can mark a StorageClass as the default for your cluster. For instructions on setting the default StorageClass, see Change the default StorageClass . 
When a PVC does not specify a storageClassName, the default StorageClass is used. 
If you set the storageclass.kubernetes.io/is-default-classannotation to true on more than one StorageClass in your cluster, and you then create a PersistentVolumeClaim with no storageClassNameset, Kubernetes uses the most recently created default StorageClass. 
#### Note: You should try to only have one StorageClass in your cluster that is marked as the default. The reason that Kubernetes allows you to have multiple default StorageClasses is to allow for seamless migration. 
You can create a PersistentVolumeClaim without specifying a storageClassNamefor the new PVC, and you can do so even when no default StorageClass exists in your cluster. In this case, the new PVC creates as you defined it, and the storageClassNameof that PVC remains unset until a default becomes available. 
You can have a cluster without any default StorageClass. If you don't mark any StorageClass as default (and one hasn't been set for you by, for example, a cloud provider), then Kubernetes cannot apply that defaulting for PersistentVolumeClaims that need it. 
If or when a default StorageClass becomes available, the control plane identifies any existing PVCs without storageClassName. For the PVCs that either have an empty value for storageClassNameor do not have this key, the control plane then updates those PVCs to set storageClassNameto match the new default StorageClass. If you have an existing PVC where the storageClassNameis "", and you configure a default StorageClass, then this PVC will not get updated. 
In order to keep binding to PVs with storageClassNameset to ""(while a default StorageClass is present), you need to set the storageClassNameof the associated PVC to "". 
## Provisioner 
Each StorageClass has a provisioner that determines what volume plugin is used for provisioning PVs. This field must be specified. 
|  Volume Plugin  | Internal Provisioner  | Config Example  |
|  AzureFile  | ✓  | Azure File  |
|  CephFS  | -  | -  |
|  FC  | -  | -  |
|  FlexVolume  | -  | -  |
|  iSCSI  | -  | -  |
|  Local  | -  | Local  |
|  NFS  | -  | NFS  |
|  PortworxVolume  | ✓  | Portworx Volume  |
|  RBD  | -  | Ceph RBD  |
|  VsphereVolume  | ✓  | vSphere  |
You are not restricted to specifying the "internal" provisioners listed here (whose names are prefixed with "kubernetes.io" and shipped alongside Kubernetes). You can also run and specify external provisioners, which are independent programs that follow a specification defined by Kubernetes. Authors of external provisioners have full discretion over where their code lives, how the provisioner is shipped, how it needs to be run, what volume plugin it uses (including Flex), etc. The repository kubernetes-sigs/sig-storage-lib-external-provisioner houses a library for writing external provisioners that implements the bulk of the specification. Some external provisioners are listed under the repository kubernetes-sigs/sig-storage-lib-external-provisioner . 
For example, NFS doesn't provide an internal provisioner, but an external provisioner can be used. There are also cases when 3rd party storage vendors provide their own external provisioner. 
## Reclaim policy 
PersistentVolumes that are dynamically created by a StorageClass will have the reclaim policy specified in the reclaimPolicyfield of the class, which can be either Deleteor Retain. If no reclaimPolicyis specified when a StorageClass object is created, it will default to Delete. 
PersistentVolumes that are created manually and managed via a StorageClass will have whatever reclaim policy they were assigned at creation. 
## Volume expansion 
PersistentVolumes can be configured to be expandable. This allows you to resize the volume by editing the corresponding PVC object, requesting a new larger amount of storage. 
The following types of volumes support volume expansion, when the underlying StorageClass has the field allowVolumeExpansionset to true. Table of Volume types and the version of Kubernetes they require 
|  Volume type  | Required Kubernetes version for volume expansion  |
|  Azure File  | 1.11  |
|  CSI  | 1.24  |
|  FlexVolume  | 1.13  |
|  Portworx  | 1.11  |
|  rbd  | 1.11  |
#### Note: You can only use the volume expansion feature to grow a Volume, not to shrink it. 
## Mount options 
PersistentVolumes that are dynamically created by a StorageClass will have the mount options specified in the mountOptionsfield of the class. 
If the volume plugin does not support mount options but mount options are specified, provisioning will fail. Mount options are not validated on either the class or PV. If a mount option is invalid, the PV mount fails. 
## Volume binding mode 
The volumeBindingModefield controls when volume binding and dynamic provisioning should occur. When unset, Immediatemode is used by default. 
The Immediatemode indicates that volume binding and dynamic provisioning occurs once the PersistentVolumeClaim is created. For storage backends that are topology-constrained and not globally accessible from all Nodes in the cluster, PersistentVolumes will be bound or provisioned without knowledge of the Pod's scheduling requirements. This may result in unschedulable Pods. 
A cluster administrator can address this issue by specifying the WaitForFirstConsumermode which will delay the binding and provisioning of a PersistentVolume until a Pod using the PersistentVolumeClaim is created. PersistentVolumes will be selected or provisioned conforming to the topology that is specified by the Pod's scheduling constraints. These include, but are not limited to, resource requirements , node selectors , pod affinity and anti-affinity , and taints and tolerations . 
The following plugins support WaitForFirstConsumerwith dynamic provisioning: 
- CSI volumes, provided that the specific CSI driver supports this 
The following plugins support WaitForFirstConsumerwith pre-created PersistentVolume binding: 
- CSI volumes, provided that the specific CSI driver supports this - local
#### Note: 
If you choose to use WaitForFirstConsumer, do not use nodeNamein the Pod spec to specify node affinity. If nodeNameis used in this case, the scheduler will be bypassed and PVC will remain in pendingstate. 
Instead, you can use node selector for kubernetes.io/hostname: storage/storageclass/pod-volume-binding.yaml
```
apiVersion:v1kind:Podmetadata:name:task-pv-podspec:nodeSelector:kubernetes.io/hostname:kube-01volumes:- name:task-pv-storagepersistentVolumeClaim:claimName:task-pv-claimcontainers:- name:task-pv-containerimage:nginxports:- containerPort:80name:"http-server"volumeMounts:- mountPath:"/usr/share/nginx/html"name:task-pv-storage
```

## Allowed topologies 
When a cluster operator specifies the WaitForFirstConsumervolume binding mode, it is no longer necessary to restrict provisioning to specific topologies in most situations. However, if still required, allowedTopologiescan be specified. 
This example demonstrates how to restrict the topology of provisioned volumes to specific zones and should be used as a replacement for the zoneand zonesparameters for the supported plugins. storage/storageclass/storageclass-topology.yaml
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:standardprovisioner:example.com/exampleparameters:type:pd-standardvolumeBindingMode:WaitForFirstConsumerallowedTopologies:- matchLabelExpressions:- key:topology.kubernetes.io/zonevalues:- us-central-1a- us-central-1b
```

## Parameters 
StorageClasses have parameters that describe volumes belonging to the storage class. Different parameters may be accepted depending on the provisioner. When a parameter is omitted, some default is used. 
There can be at most 512 parameters defined for a StorageClass. The total length of the parameters object including its keys and values cannot exceed 256 KiB. 
### AWS EBS 
Kubernetes 1.37 does not include a awsElasticBlockStorevolume type. 
The AWSElasticBlockStore in-tree storage driver was deprecated in the Kubernetes v1.19 release and then removed entirely in the v1.27 release. 
The Kubernetes project suggests that you use the AWS EBS out-of-tree storage driver instead. 
Here is an example StorageClass for the AWS EBS CSI driver: storage/storageclass/storageclass-aws-ebs.yaml
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:ebs-scprovisioner:ebs.csi.aws.comvolumeBindingMode:WaitForFirstConsumerparameters:csi.storage.k8s.io/fstype:xfstype:io1iopsPerGB:"50"encrypted:"true"tagSpecification_1:"key1=value1"tagSpecification_2:"key2=value2"allowedTopologies:- matchLabelExpressions:- key:topology.ebs.csi.aws.com/zonevalues:- us-east-2c
```

tagSpecification: Tags with this prefix are applied to dynamically provisioned EBS volumes. 
### AWS EFS 
To configure AWS EFS storage, you can use the out-of-tree AWS_EFS_CSI_DRIVER . storage/storageclass/storageclass-aws-efs.yaml
```
kind:StorageClassapiVersion:storage.k8s.io/v1metadata:name:efs-scprovisioner:efs.csi.aws.comparameters:provisioningMode:efs-apfileSystemId:fs-92107410directoryPerms:"700"
```

- provisioningMode: The type of volume to be provisioned by Amazon EFS. Currently, only access point based provisioning is supported ( efs-ap). - fileSystemId: The file system under which the access point is created. - directoryPerms: The directory permissions of the root directory created by the access point. 
For more details, refer to the AWS_EFS_CSI_Driver Dynamic Provisioning documentation. 
### NFS 
To configure NFS storage, you can use the in-tree driver or the NFS CSI driver for Kubernetes (recommended). storage/storageclass/storageclass-nfs.yaml
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:example-nfsprovisioner:example.com/external-nfsparameters:server:nfs-server.example.compath:/sharereadOnly:"false"
```

- server: Server is the hostname or IP address of the NFS server. - path: Path that is exported by the NFS server. - readOnly: A flag indicating whether the storage will be mounted as read only (default false). 
Kubernetes doesn't include an internal NFS provisioner. You need to use an external provisioner to create a StorageClass for NFS. Here are some examples: 
- NFS Ganesha server and external provisioner - NFS subdir external provisioner 
### vSphere 
There are two types of provisioners for vSphere storage classes: 
- CSI provisioner : csi.vsphere.vmware.com- vCP provisioner : kubernetes.io/vsphere-volume
In-tree provisioners are deprecated . For more information on the CSI provisioner, see Kubernetes vSphere CSI Driver and vSphereVolume CSI migration . 
#### CSI Provisioner 
The vSphere CSI StorageClass provisioner works with Tanzu Kubernetes clusters. For an example, refer to the vSphere CSI repository . 
#### vCP Provisioner 
The following examples use the VMware Cloud Provider (vCP) StorageClass provisioner. 
- 
Create a StorageClass with a user specified disk format. 
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:fastprovisioner:kubernetes.io/vsphere-volumeparameters:diskformat:zeroedthick
```

diskformat: thin, zeroedthickand eagerzeroedthick. Default: "thin". - 
Create a StorageClass with a disk format on a user specified datastore. 
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:fastprovisioner:kubernetes.io/vsphere-volumeparameters:diskformat:zeroedthickdatastore:VSANDatastore
```

datastore: The user can also specify the datastore in the StorageClass. The volume will be created on the datastore specified in the StorageClass, which in this case is VSANDatastore. This field is optional. If the datastore is not specified, then the volume will be created on the datastore specified in the vSphere config file used to initialize the vSphere Cloud Provider. - 
Storage Policy Management inside kubernetes 
  - 
Using existing vCenter SPBM policy 
One of the most important features of vSphere for Storage Management is policy based Management. Storage Policy Based Management (SPBM) is a storage policy framework that provides a single unified control plane across a broad range of data services and storage solutions. SPBM enables vSphere administrators to overcome upfront storage provisioning challenges, such as capacity planning, differentiated service levels and managing capacity headroom. 
The SPBM policies can be specified in the StorageClass using the storagePolicyNameparameter.   - 
Virtual SAN policy support inside Kubernetes 
Vsphere Infrastructure (VI) Admins will have the ability to specify custom Virtual SAN Storage Capabilities during dynamic volume provisioning. You can now define storage requirements, such as performance and availability, in the form of storage capabilities during dynamic volume provisioning. The storage capability requirements are converted into a Virtual SAN policy which are then pushed down to the Virtual SAN layer when a persistent volume (virtual disk) is being created. The virtual disk is distributed across the Virtual SAN datastore to meet the requirements. 
You can see Storage Policy Based Management for dynamic provisioning of volumes for more details on how to use storage policies for persistent volumes management. 
### Ceph RBD (deprecated) 
#### Note: 
```
<div class="feature-state-notice feature-deprecated">
  <span class="feature-state-name">Feature state:</span>
  <span class="feature-state-details">
  <span class="feature-state-stage">Deprecated</span> since Kubernetes v1.28
  </span>
</div>

```

This internal provisioner of Ceph RBD is deprecated. Please use CephFS RBD CSI driver . storage/storageclass/storageclass-ceph-rbd.yaml
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:fastprovisioner:kubernetes.io/rbd# This provisioner is deprecatedparameters:monitors:198.19.254.105:6789adminId:kubeadminSecretName:ceph-secretadminSecretNamespace:kube-systempool:kubeuserId:kubeuserSecretName:ceph-secret-useruserSecretNamespace:defaultfsType:ext4imageFormat:"2"imageFeatures:"layering"
```

- 
monitors: Ceph monitors, comma delimited. This parameter is required. - 
adminId: Ceph client ID that is capable of creating images in the pool. Default is "admin". - 
adminSecretName: Secret Name for adminId. This parameter is required. The provided secret must have type "kubernetes.io/rbd". - 
adminSecretNamespace: The namespace for adminSecretName. Default is "default". - 
pool: Ceph RBD pool. Default is "rbd". - 
userId: Ceph client ID that is used to map the RBD image. Default is the same as adminId. - 
userSecretName: The name of Ceph Secret for userIdto map RBD image. It must exist in the same namespace as PVCs. This parameter is required. The provided secret must have type "kubernetes.io/rbd", for example created in this way: 
```
kubectl create secret generic ceph-secret --type="kubernetes.io/rbd"\
  --from-literal=key='QVFEQ1pMdFhPUnQrSmhBQUFYaERWNHJsZ3BsMmNjcDR6RFZST0E9PQ=='\
  --namespace=kube-system

```
- 
userSecretNamespace: The namespace for userSecretName. - 
fsType: fsType that is supported by kubernetes. Default: "ext4". - 
imageFormat: Ceph RBD image format, "1" or "2". Default is "2". - 
imageFeatures: This parameter is optional and should only be used if you set imageFormatto "2". Currently supported features are layeringonly. Default is "", and no features are turned on. 
### Azure Disk 
Kubernetes 1.37 does not include a azureDiskvolume type. 
The azureDiskin-tree storage driver was deprecated in the Kubernetes v1.19 release and then removed entirely in the v1.27 release. 
The Kubernetes project suggests that you use the Azure Disk third party storage driver instead. 
### Azure File (deprecated) storage/storageclass/storageclass-azure-file.yaml
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:azurefileprovisioner:kubernetes.io/azure-fileparameters:skuName:Standard_LRSlocation:eastusstorageAccount:azure_storage_account_name# example value
```

- skuName: Azure storage account SKU tier. Default is empty. - location: Azure storage account location. Default is empty. - storageAccount: Azure storage account name. Default is empty. If a storage account is not provided, all storage accounts associated with the resource group are searched to find one that matches skuNameand location. If a storage account is provided, it must reside in the same resource group as the cluster, and skuNameand locationare ignored. - secretNamespace: the namespace of the secret that contains the Azure Storage Account Name and Key. Default is the same as the Pod. - secretName: the name of the secret that contains the Azure Storage Account Name and Key. Default is azure-storage-account-<accountName>-secret- readOnly: a flag indicating whether the storage will be mounted as read only. Defaults to false which means a read/write mount. This setting will impact the ReadOnlysetting in VolumeMounts as well. 
During storage provisioning, a secret named by secretNameis created for the mounting credentials. If the cluster has enabled both RBAC and Controller Roles , add the createpermission of resource secretfor clusterrole system:controller:persistent-volume-binder. 
In a multi-tenancy context, it is strongly recommended to set the value for secretNamespaceexplicitly, otherwise the storage account credentials may be read by other users. 
### Portworx volume (deprecated) storage/storageclass/storageclass-portworx-volume.yaml
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:portworx-io-priority-highprovisioner:kubernetes.io/portworx-volume# This provisioner is deprecatedparameters:repl:"1"snap_interval:"70"priority_io:"high"
```

- fs: filesystem to be laid out: none/xfs/ext4(default: ext4). - block_size: block size in Kbytes (default: 32). - repl: number of synchronous replicas to be provided in the form of replication factor 1..3(default: 1) A string is expected here i.e. "1"and not 1. - priority_io: determines whether the volume will be created from higher performance or a lower priority storage high/medium/low(default: low). - snap_interval: clock/time interval in minutes for when to trigger snapshots. Snapshots are incremental based on difference with the prior snapshot, 0 disables snaps (default: 0). A string is expected here i.e. "70"and not 70. - aggregation_level: specifies the number of chunks the volume would be distributed into, 0 indicates a non-aggregated volume (default: 0). A string is expected here i.e. "0"and not 0- ephemeral: specifies whether the volume should be cleaned-up after unmount or should be persistent. emptyDiruse case can set this value to true and persistent volumesuse case such as for databases like Cassandra should set to false, true/false(default false). A string is expected here i.e. "true"and not true. 
### Local storage/storageclass/storageclass-local.yaml
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:local-storageprovisioner:kubernetes.io/no-provisioner# indicates that this StorageClass does not support automatic provisioningvolumeBindingMode:WaitForFirstConsumer
```

Local volumes do not support dynamic provisioning in Kubernetes 1.37; however a StorageClass should still be created to delay volume binding until a Pod is actually scheduled to the appropriate node. This is specified by the WaitForFirstConsumervolume binding mode. 
Delaying volume binding allows the scheduler to consider all of a Pod's scheduling constraints when choosing an appropriate PersistentVolume for a PersistentVolumeClaim. 
# 6 - Volume Attributes Classes Feature state: Stable since Kubernetes v1.36 More information about this feature 
This is a stable feature in Kubernetes, and has been since version v1.36. It was first available in the v1.29 release. You can no longer disable or opt out of this feature or behavior (it is locked); if you explicitly set a value for the associated feature gate VolumeAttributesClass , Kubernetes ignores it but does not report any error. 
This page assumes that you are familiar with StorageClasses , volumes and PersistentVolumes in Kubernetes. 
A VolumeAttributesClass provides a way for administrators to describe the mutable "classes" of storage they offer. Different classes might map to different quality-of-service levels. Kubernetes itself is un-opinionated about what these classes represent. 
This feature is generally available (GA) as of version 1.34, and users have the option to disable it. 
You can also only use VolumeAttributesClasses with storage backed by Container Storage Interface , and only where the relevant CSI driver implements the ModifyVolumeAPI. 
## The VolumeAttributesClass API 
Each VolumeAttributesClass contains the driverNameand parameters, which are used when a PersistentVolume (PV) belonging to the class needs to be dynamically provisioned or modified. 
The name of a VolumeAttributesClass object is significant and is how users can request a particular class. Administrators set the name and other parameters of a class when first creating VolumeAttributesClass objects. While the name of a VolumeAttributesClass object in a PersistentVolumeClaimis mutable, the parameters in an existing class are immutable. 
```
apiVersion:storage.k8s.io/v1kind:VolumeAttributesClassmetadata:name:silverdriverName:pd.csi.storage.gke.ioparameters:provisioned-iops:"3000"provisioned-throughput:"50"
```

### Provisioner 
Each VolumeAttributesClass has a provisioner that determines what volume plugin is used for provisioning PVs. The field driverNamemust be specified. 
The feature support for VolumeAttributesClass is implemented in kubernetes-csi/external-provisioner . 
You are not restricted to specifying the kubernetes-csi/external-provisioner . You can also run and specify external provisioners, which are independent programs that follow a specification defined by Kubernetes. Authors of external provisioners have full discretion over where their code lives, how the provisioner is shipped, how it needs to be run, what volume plugin it uses, etc. 
To understand how the provisioner works with VolumeAttributesClass, refer to the CSI external-provisioner documentation . 
### Resizer 
Each VolumeAttributesClass has a resizer that determines what volume plugin is used for modifying PVs. The field driverNamemust be specified. 
The modifying volume feature support for VolumeAttributesClass is implemented in kubernetes-csi/external-resizer . 
For example, an existing PersistentVolumeClaim is using a VolumeAttributesClass named silver: 
```
apiVersion:v1kind:PersistentVolumeClaimmetadata:name:test-pv-claimspec:…volumeAttributesClassName:silver…
```

A new VolumeAttributesClass gold is available in the cluster: 
```
apiVersion:storage.k8s.io/v1kind:VolumeAttributesClassmetadata:name:golddriverName:pd.csi.storage.gke.ioparameters:iops:"4000"throughput:"60"
```

The end user can update the PVC with the new VolumeAttributesClass gold and apply: 
```
apiVersion:v1kind:PersistentVolumeClaimmetadata:name:test-pv-claimspec:…volumeAttributesClassName:gold…
```

To understand how the resizer works with VolumeAttributesClass, refer to the CSI external-resizer documentation . 
## Parameters 
VolumeAttributeClasses have parameters that describe volumes belonging to them. Different parameters may be accepted depending on the provisioner or the resizer. For example, the value 4000, for the parameter iops, and the parameter throughputare specific to GCE PD. When a parameter is omitted, the default is used at volume provisioning. If a user applies the PVC with a different VolumeAttributesClass with omitted parameters, the default value of the parameters may be used depending on the CSI driver implementation. Please refer to the related CSI driver documentation for more details. 
There can be at most 512 parameters defined for a VolumeAttributesClass. The total length of the parameters object including its keys and values cannot exceed 256 KiB. 
# 7 - Dynamic Volume Provisioning 
Dynamic volume provisioning allows storage volumes to be created on-demand. Without dynamic provisioning, cluster administrators have to manually make calls to their cloud or storage provider to create new storage volumes, and then create PersistentVolumeobjects to represent them in Kubernetes. The dynamic provisioning feature eliminates the need for cluster administrators to pre-provision storage. Instead, it automatically provisions storage when users create PersistentVolumeClaimobjects . 
## Background 
The implementation of dynamic volume provisioning is based on the API object StorageClassfrom the API group storage.k8s.io. A cluster administrator can define as many StorageClassobjects as needed, each specifying a volume plugin (aka provisioner ) that provisions a volume and the set of parameters to pass to that provisioner when provisioning. A cluster administrator can define and expose multiple flavors of storage (from the same or different storage systems) within a cluster, each with a custom set of parameters. This design also ensures that end users don't have to worry about the complexity and nuances of how storage is provisioned, but still have the ability to select from multiple storage options. 
For more details, see the Storage Classes concept. 
## Enabling Dynamic Provisioning 
To enable dynamic provisioning, a cluster administrator needs to pre-create one or more StorageClass objects for users. StorageClass objects define which provisioner should be used and what parameters should be passed to that provisioner when dynamic provisioning is invoked. The name of a StorageClass object must be a valid DNS subdomain name . 
The following manifest creates a storage class "slow" which provisions standard disk-like persistent disks. 
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:slowprovisioner:kubernetes.io/gce-pdparameters:type:pd-standard
```

The following manifest creates a storage class "fast" which provisions SSD-like persistent disks. 
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:fastprovisioner:kubernetes.io/gce-pdparameters:type:pd-ssd
```

## Using Dynamic Provisioning 
Users request dynamically provisioned storage by including a storage class in their PersistentVolumeClaim. Before Kubernetes v1.6, this was done via the volume.beta.kubernetes.io/storage-classannotation. However, this annotation is deprecated since v1.9. Users now can and should instead use the storageClassNamefield of the PersistentVolumeClaimobject. The value of this field must match the name of a StorageClassconfigured by the administrator (see Enabling Dynamic Provisioning ). 
To select the "fast" storage class, for example, a user would create the following PersistentVolumeClaim: 
```
apiVersion:v1kind:PersistentVolumeClaimmetadata:name:claim1spec:accessModes:- ReadWriteOncestorageClassName:fastresources:requests:storage:30Gi
```

This claim results in an SSD-like Persistent Disk being automatically provisioned. When the claim is deleted, the volume is destroyed. 
## Defaulting Behavior 
Dynamic provisioning can be enabled on a cluster such that all claims are dynamically provisioned if no storage class is specified. A cluster administrator can enable this behavior by: 
- Marking one StorageClassobject as default . - Making sure that the DefaultStorageClassadmission controller is enabled on the API server. 
An administrator can mark a specific StorageClassas default by adding the storageclass.kubernetes.io/is-default-classannotation to it. When a default StorageClassexists in a cluster and a user creates a PersistentVolumeClaimwith storageClassNameunspecified, the DefaultStorageClassadmission controller automatically adds the storageClassNamefield pointing to the default storage class. 
Note that if you set the storageclass.kubernetes.io/is-default-classannotation to true on more than one StorageClass in your cluster, and you then create a PersistentVolumeClaimwith no storageClassNameset, Kubernetes uses the most recently created default StorageClass. 
## Topology Awareness 
In Multi-Zone clusters, Pods can be spread across Zones in a Region. Single-Zone storage backends should be provisioned in the Zones where Pods are scheduled. This can be accomplished by setting the Volume Binding Mode . 
# 8 - Volume Snapshots 
In Kubernetes, a VolumeSnapshot represents a snapshot of a volume on a storage system. This document assumes that you are already familiar with Kubernetes persistent volumes . 
## Introduction 
Similar to how API resources PersistentVolumeand PersistentVolumeClaimare used to provision volumes for users and administrators, VolumeSnapshotContentand VolumeSnapshotAPI resources are provided to create volume snapshots for users and administrators. 
A VolumeSnapshotContentis a snapshot taken from a volume in the cluster that has been provisioned by an administrator. It is a resource in the cluster just like a PersistentVolume is a cluster resource. 
A VolumeSnapshotis a request for snapshot of a volume by a user. It is similar to a PersistentVolumeClaim. 
VolumeSnapshotClassallows you to specify different attributes belonging to a VolumeSnapshot. These attributes may differ among snapshots taken from the same volume on the storage system and therefore cannot be expressed by using the same StorageClassof a PersistentVolumeClaim. 
Volume snapshots provide Kubernetes users with a standardized way to copy a volume's contents at a particular point in time without creating an entirely new volume. This functionality enables, for example, database administrators to backup databases before performing edit or delete modifications. 
Users need to be aware of the following when using this feature: 
- API Objects VolumeSnapshot, VolumeSnapshotContent, and VolumeSnapshotClassare CRDs , not part of the core API. - VolumeSnapshotsupport is only available for CSI drivers. - As part of the deployment process of VolumeSnapshot, the Kubernetes team provides a snapshot controller to be deployed into the control plane, and a sidecar helper container called csi-snapshotter to be deployed together with the CSI driver. The snapshot controller watches VolumeSnapshotand VolumeSnapshotContentobjects and is responsible for the creation and deletion of VolumeSnapshotContentobject. The sidecar csi-snapshotter watches VolumeSnapshotContentobjects and triggers CreateSnapshotand DeleteSnapshotoperations against a CSI endpoint. - There is also a validating webhook server which provides tightened validation on snapshot objects. This should be installed by the Kubernetes distros along with the snapshot controller and CRDs, not CSI drivers. It should be installed in all Kubernetes clusters that has the snapshot feature enabled. - CSI drivers may or may not have implemented the volume snapshot functionality. The CSI drivers that have provided support for volume snapshot will likely use the csi-snapshotter. See CSI Driver documentation for details. - The CRDs and snapshot controller installations are the responsibility of the Kubernetes distribution. 
For advanced use cases, such as creating group snapshots of multiple volumes, see the external CSI Volume Group Snapshot documentation . 
In clusters where a snapshot is only usable from part of the cluster (for example, a snapshot of a volume in one zone of a multi-zone cluster without shared storage), the snapshot's topology can be recorded and honored when restoring from it. For details, see the external CSI Documentation . 
## Lifecycle of a volume snapshot and volume snapshot content 
VolumeSnapshotContentsare resources in the cluster. VolumeSnapshotsare requests for those resources. The interaction between VolumeSnapshotContentsand VolumeSnapshotsfollow this lifecycle: 
### Provisioning Volume Snapshot 
There are two ways snapshots may be provisioned: pre-provisioned or dynamically provisioned. 
#### Pre-provisioned 
A cluster administrator creates a number of VolumeSnapshotContents. They carry the details of the real volume snapshot on the storage system which is available for use by cluster users. They exist in the Kubernetes API and are available for consumption. 
#### Dynamic 
Instead of using a pre-existing snapshot, you can request that a snapshot to be dynamically taken from a PersistentVolumeClaim. The VolumeSnapshotClass specifies storage provider-specific parameters to use when taking a snapshot. 
### Binding 
The snapshot controller handles the binding of a VolumeSnapshotobject with an appropriate VolumeSnapshotContentobject, in both pre-provisioned and dynamically provisioned scenarios. The binding is a one-to-one mapping. 
In the case of pre-provisioned binding, the VolumeSnapshot will remain unbound until the requested VolumeSnapshotContent object is created. 
### Persistent Volume Claim as Snapshot Source Protection 
The purpose of this protection is to ensure that in-use PersistentVolumeClaim API objects are not removed from the system while a snapshot is being taken from it (as this may result in data loss). 
While a snapshot is being taken of a PersistentVolumeClaim, that PersistentVolumeClaim is in-use. If you delete a PersistentVolumeClaim API object in active use as a snapshot source, the PersistentVolumeClaim object is not removed immediately. Instead, removal of the PersistentVolumeClaim object is postponed until the snapshot is readyToUse or aborted. 
### Delete 
Deletion is triggered by deleting the VolumeSnapshotobject, and the DeletionPolicywill be followed. If the DeletionPolicyis Delete, then the underlying storage snapshot will be deleted along with the VolumeSnapshotContentobject. If the DeletionPolicyis Retain, then both the underlying snapshot and VolumeSnapshotContentremain. 
## VolumeSnapshots 
Each VolumeSnapshot contains a spec and a status. 
```
apiVersion:snapshot.storage.k8s.io/v1kind:VolumeSnapshotmetadata:name:new-snapshot-testspec:volumeSnapshotClassName:csi-hostpath-snapclasssource:persistentVolumeClaimName:pvc-test
```

persistentVolumeClaimNameis the name of the PersistentVolumeClaim data source for the snapshot. This field is required for dynamically provisioning a snapshot. 
A volume snapshot can request a particular class by specifying the name of a VolumeSnapshotClass using the attribute volumeSnapshotClassName. If nothing is set, then the default class is used if available. 
For pre-provisioned snapshots, you need to specify a volumeSnapshotContentNameas the source for the snapshot as shown in the following example. The volumeSnapshotContentNamesource field is required for pre-provisioned snapshots. 
```
apiVersion:snapshot.storage.k8s.io/v1kind:VolumeSnapshotmetadata:name:test-snapshotspec:source:volumeSnapshotContentName:test-content
```

## Volume Snapshot Contents 
Each VolumeSnapshotContent contains a spec and status. In dynamic provisioning, the snapshot common controller creates VolumeSnapshotContentobjects. Here is an example: 
```
apiVersion:snapshot.storage.k8s.io/v1kind:VolumeSnapshotContentmetadata:name:snapcontent-72d9a349-aacd-42d2-a240-d775650d2455spec:deletionPolicy:Deletedriver:hostpath.csi.k8s.iosource:volumeHandle:ee0cfb94-f8d4-11e9-b2d8-0242ac110002sourceVolumeMode:FilesystemvolumeSnapshotClassName:csi-hostpath-snapclassvolumeSnapshotRef:name:new-snapshot-testnamespace:defaultuid:72d9a349-aacd-42d2-a240-d775650d2455
```

volumeHandleis the unique identifier of the volume created on the storage backend and returned by the CSI driver during the volume creation. This field is required for dynamically provisioning a snapshot. It specifies the volume source of the snapshot. 
For pre-provisioned snapshots, you (as cluster administrator) are responsible for creating the VolumeSnapshotContentobject as follows. 
```
apiVersion:snapshot.storage.k8s.io/v1kind:VolumeSnapshotContentmetadata:name:new-snapshot-content-testspec:deletionPolicy:Deletedriver:hostpath.csi.k8s.iosource:snapshotHandle:7bdd0de3-aaeb-11e8-9aae-0242ac110002sourceVolumeMode:FilesystemvolumeSnapshotRef:name:new-snapshot-testnamespace:default
```

snapshotHandleis the unique identifier of the volume snapshot created on the storage backend. This field is required for the pre-provisioned snapshots. It specifies the CSI snapshot id on the storage system that this VolumeSnapshotContentrepresents. 
sourceVolumeModeis the mode of the volume whose snapshot is taken. The value of the sourceVolumeModefield can be either Filesystemor Block. If the source volume mode is not specified, Kubernetes treats the snapshot as if the source volume's mode is unknown. 
volumeSnapshotRefis the reference of the corresponding VolumeSnapshot. Note that when the VolumeSnapshotContentis being created as a pre-provisioned snapshot, the VolumeSnapshotreferenced in volumeSnapshotRefmight not exist yet. 
## Converting the volume mode of a Snapshot 
If the VolumeSnapshotsAPI installed on your cluster supports the sourceVolumeModefield, then the API has the capability to prevent unauthorized users from converting the mode of a volume. 
To check if your cluster has capability for this feature, run the following command: 
```
$ kubectl get crd volumesnapshotcontent -o yaml
```

If you want to allow users to create a PersistentVolumeClaimfrom an existing VolumeSnapshot, but with a different volume mode than the source, the annotation snapshot.storage.kubernetes.io/allow-volume-mode-change: "true"needs to be added to the VolumeSnapshotContentthat corresponds to the VolumeSnapshot. 
For pre-provisioned snapshots, spec.sourceVolumeModeneeds to be populated by the cluster administrator. 
An example VolumeSnapshotContentresource with this feature enabled would look like: 
```
apiVersion:snapshot.storage.k8s.io/v1kind:VolumeSnapshotContentmetadata:name:new-snapshot-content-testannotations:- snapshot.storage.kubernetes.io/allow-volume-mode-change:"true"spec:deletionPolicy:Deletedriver:hostpath.csi.k8s.iosource:snapshotHandle:7bdd0de3-aaeb-11e8-9aae-0242ac110002sourceVolumeMode:FilesystemvolumeSnapshotRef:name:new-snapshot-testnamespace:default
```

## Volume Snapshot Topology 
In some clusters a snapshot is only usable from part of the cluster. For example, in a multi-zone cluster where storage is not shared across zones, a snapshot of a volume in one zone is only usable from that zone: volumes restored from the snapshot can only be created where the snapshot data resides. 
When the VolumeSnapshotTopologyfeature is enabled, this topology is recorded and honored: 
- A cluster administrator can set allowedTopologieson a VolumeSnapshotClass to request where dynamically created snapshots should be usable from. - The CSI driver reports where a snapshot is usable from, and the csi-snapshotter sidecar records it on VolumeSnapshotContent.spec.nodeAffinity. - When you provision a volume from a snapshot, this topology is used to place the restored volume where the snapshot data is accessible. 
This is an alpha feature of the CSI sidecars, enabled with the VolumeSnapshotTopologyfeature gate on the csi-snapshotter and external-provisioner. For details, see the external CSI Documentation . 
## Provisioning Volumes from Snapshots 
You can provision a new volume, pre-populated with data from a snapshot, by using the dataSource field in the PersistentVolumeClaimobject. 
For more details, see Volume Snapshot and Restore Volume from Snapshot . 
# 9 - Volume Snapshot Classes 
This document describes the concept of VolumeSnapshotClass in Kubernetes. Familiarity with volume snapshots and storage classes is suggested. 
## Introduction 
Just like StorageClass provides a way for administrators to describe the "classes" of storage they offer when provisioning a volume, VolumeSnapshotClass provides a way to describe the "classes" of storage when provisioning a volume snapshot. 
## The VolumeSnapshotClass Resource 
Each VolumeSnapshotClass contains the fields driver, deletionPolicy, and parameters, which are used when a VolumeSnapshot belonging to the class needs to be dynamically provisioned. 
The name of a VolumeSnapshotClass object is significant, and is how users can request a particular class. Administrators set the name and other parameters of a class when first creating VolumeSnapshotClass objects, and the objects cannot be updated once they are created. 
#### Note: Installation of the CRDs is the responsibility of the Kubernetes distribution. Without the required CRDs present, the creation of a VolumeSnapshotClass fails. 
```
apiVersion:snapshot.storage.k8s.io/v1kind:VolumeSnapshotClassmetadata:name:csi-hostpath-snapclassdriver:hostpath.csi.k8s.iodeletionPolicy:Deleteparameters:
```

Administrators can specify a default VolumeSnapshotClass for VolumeSnapshots that don't request any particular class to bind to by adding the snapshot.storage.kubernetes.io/is-default-class: "true"annotation: 
```
apiVersion:snapshot.storage.k8s.io/v1kind:VolumeSnapshotClassmetadata:name:csi-hostpath-snapclassannotations:snapshot.storage.kubernetes.io/is-default-class:"true"driver:hostpath.csi.k8s.iodeletionPolicy:Deleteparameters:
```

If multiple CSI drivers exist, a default VolumeSnapshotClass can be specified for each of them. 
### VolumeSnapshotClass dependencies 
When you create a VolumeSnapshot without specifying a VolumeSnapshotClass, Kubernetes automatically selects a default VolumeSnapshotClass that has a CSI driver matching the CSI driver of the PVC’s StorageClass. 
This behavior allows multiple default VolumeSnapshotClass objects to coexist in a cluster, as long as each one is associated with a unique CSI driver. 
Always ensure that there is only one default VolumeSnapshotClass for each CSI driver. If multiple default VolumeSnapshotClass objects are created using the same CSI driver, a VolumeSnapshot creation will fail because Kubernetes cannot determine which one to use. 
### Driver 
Volume snapshot classes have a driver that determines what CSI volume plugin is used for provisioning VolumeSnapshots. This field must be specified. 
### DeletionPolicy 
Volume snapshot classes have a deletionPolicy . It enables you to configure what happens to a VolumeSnapshotContent when the VolumeSnapshot object it is bound to is to be deleted. The deletionPolicy of a volume snapshot class can either be Retainor Delete. This field must be specified. 
If the deletionPolicy is Delete, then the underlying storage snapshot will be deleted along with the VolumeSnapshotContent object. If the deletionPolicy is Retain, then both the underlying snapshot and VolumeSnapshotContent remain. 
## Parameters 
Volume snapshot classes have parameters that describe volume snapshots belonging to the volume snapshot class. Different parameters may be accepted depending on the driver. 
# 10 - CSI Volume Cloning 
This document describes the concept of cloning existing CSI Volumes in Kubernetes. Familiarity with Volumes is suggested. 
## Introduction 
The CSI Volume Cloning feature adds support for specifying existing PVC s in the dataSourcefield to indicate a user would like to clone a Volume . 
A Clone is defined as a duplicate of an existing Kubernetes Volume that can be consumed as any standard Volume would be. The only difference is that upon provisioning, rather than creating a "new" empty Volume, the back end device creates an exact duplicate of the specified Volume. 
The implementation of cloning, from the perspective of the Kubernetes API, adds the ability to specify an existing PVC as a dataSource during new PVC creation. The source PVC must be bound and available (not in use). 
Users need to be aware of the following when using this feature: 
- Cloning support ( VolumePVCDataSource) is only available for CSI drivers. - Cloning support is only available for dynamic provisioners. - CSI drivers may or may not have implemented the volume cloning functionality. - You can only clone a PVC when it exists in the same namespace as the destination PVC (source and destination must be in the same namespace). - Cloning is supported with a different Storage Class. 
  - Destination volume can be the same or a different storage class as the source.   - Default storage class can be used and storageClassName omitted in the spec. - Cloning can only be performed between two volumes that use the same VolumeMode setting (if you request a block mode volume, the source MUST also be block mode) 
## Provisioning 
Clones are provisioned like any other PVC with the exception of adding a dataSource that references an existing PVC in the same namespace. 
```
apiVersion:v1kind:PersistentVolumeClaimmetadata:name:clone-of-pvc-1namespace:mynsspec:accessModes:- ReadWriteOncestorageClassName:cloningresources:requests:storage:5GidataSource:kind:PersistentVolumeClaimname:pvc-1
```

#### Note: You must specify a capacity value for spec.resources.requests.storage, and the value you specify must be the same or larger than the capacity of the source volume. 
The result is a new PVC with the name clone-of-pvc-1that has the exact same content as the specified source pvc-1. 
## Usage 
Upon availability of the new PVC, the cloned PVC is consumed the same as other PVC. It's also expected at this point that the newly created PVC is an independent object. It can be consumed, cloned, snapshotted, or deleted independently and without consideration for it's original dataSource PVC. This also implies that the source is not linked in any way to the newly created clone, it may also be modified or deleted without affecting the newly created clone. 
# 11 - Volume Populators and Data Sources 
This document describes volume populators and data sources in Kubernetes. Familiarity with persistent volumes is suggested. 
When you create a PersistentVolumeClaim , the volume that Kubernetes provisions for it normally starts empty. A data source lets you instead request that the new volume be pre-populated with existing data. Volume populators are the controllers that carry out that population, based on the data source that the PersistentVolumeClaim references. 
Kubernetes has built-in support for data sources that clone an existing volume or that restore a volume snapshot . Custom volume populators extend this mechanism. The data source is a custom resource, that is, an object whose type is defined by a CustomResourceDefinition . A populator controller watches for PersistentVolumeClaims that reference such a resource and fills the new volume from it. 
## Volume populators and data sources Feature state: Beta since Kubernetes v1.24 
Kubernetes supports custom volume populators. To use custom volume populators, you must enable the AnyVolumeDataSourcefeature gate for the kube-apiserver and kube-controller-manager. 
Volume populators take advantage of a PVC spec field called dataSourceRef. Unlike the dataSourcefield, which can only contain either a reference to another PersistentVolumeClaim or to a VolumeSnapshot, the dataSourceReffield can contain a reference to any object in the same namespace, except for core objects other than PVCs. For clusters that have the feature gate enabled, use of the dataSourceRefis preferred over dataSource. 
## Data source references 
The dataSourceReffield behaves almost the same as the dataSourcefield. If one is specified while the other is not, the API server will give both fields the same value. Neither field can be changed after creation, and attempting to specify different values for the two fields will result in a validation error. Therefore the two fields will always have the same contents. 
There are two differences between the dataSourceReffield and the dataSourcefield that users should be aware of: 
- The dataSourcefield ignores invalid values (as if the field was blank) while the dataSourceReffield never ignores values and will cause an error if an invalid value is used. Invalid values are any core object (objects with no apiGroup) except for PVCs. - The dataSourceReffield may contain different types of objects, while the dataSourcefield only allows PVCs and VolumeSnapshots. 
When the CrossNamespaceVolumeDataSourcefeature is enabled, there are additional differences: 
- The dataSourcefield only allows local objects, while the dataSourceReffield allows objects in any namespaces. - When namespace is specified, dataSourceand dataSourceRefare not synced. 
Users should always use dataSourceRefon clusters that have the feature gate enabled, and fall back to dataSourceon clusters that do not. It is not necessary to look at both fields under any circumstance. The duplicated values with slightly different semantics exist only for backwards compatibility. In particular, a mixture of older and newer controllers are able to interoperate because the fields are the same. 
### Using volume populators 
Volume populators are controllers that can create non-empty volumes, where the contents of the volume are determined by a Custom Resource. Users create a populated volume by referring to a Custom Resource using the dataSourceReffield: 
```
apiVersion:v1kind:PersistentVolumeClaimmetadata:name:populated-pvcspec:dataSourceRef:name:example-namekind:ExampleDataSourceapiGroup:example.storage.k8s.ioaccessModes:- ReadWriteOnceresources:requests:storage:10Gi
```

Because volume populators are external components, attempts to create a PVC that uses one can fail if not all the correct components are installed. External controllers should generate events on the PVC to provide feedback on the status of the creation, including warnings if the PVC cannot be created due to some missing component. 
You can install the alpha volume data source validator controller into your cluster. That controller generates warning Events on a PVC in the case that no populator is registered to handle that kind of data source. When a suitable populator is installed for a PVC, it's the responsibility of that populator controller to report Events that relate to volume creation and issues during the process. 
## Cross namespace data sources Feature state: Alpha since Kubernetes v1.26 
Kubernetes supports cross namespace volume data sources. To use cross namespace volume data sources, you must enable the AnyVolumeDataSourceand CrossNamespaceVolumeDataSourcefeature gates for the kube-apiserver and kube-controller-manager. Also, you must enable the CrossNamespaceVolumeDataSourcefeature gate for the csi-provisioner. 
Enabling the CrossNamespaceVolumeDataSourcefeature gate allows you to specify a namespace in the dataSourceRef field. 
#### Note: When you specify a namespace for a volume data source, Kubernetes checks for a ReferenceGrant in the other namespace before accepting the reference. ReferenceGrant is part of the gateway.networking.k8s.ioextension APIs. See ReferenceGrant in the Gateway API documentation for details. This means that you must extend your Kubernetes cluster with at least ReferenceGrant from the Gateway API before you can use this mechanism. 
### Using a cross-namespace volume data source Feature state: Alpha since Kubernetes v1.26 
Create a ReferenceGrant to allow the namespace owner to accept the reference. You define a populated volume by specifying a cross namespace volume data source using the dataSourceReffield. You must already have a valid ReferenceGrant in the source namespace: 
```
apiVersion:gateway.networking.k8s.io/v1beta1kind:ReferenceGrantmetadata:name:allow-ns1-pvcnamespace:defaultspec:from:- group:""kind:PersistentVolumeClaimnamespace:ns1to:- group:snapshot.storage.k8s.iokind:VolumeSnapshotname:new-snapshot-demo
```

```
apiVersion:v1kind:PersistentVolumeClaimmetadata:name:foo-pvcnamespace:ns1spec:storageClassName:exampleaccessModes:- ReadWriteOnceresources:requests:storage:1GidataSourceRef:apiGroup:snapshot.storage.k8s.iokind:VolumeSnapshotname:new-snapshot-demonamespace:defaultvolumeMode:Filesystem
```

## What's next 
- Learn about Persistent Volumes . - Learn about CSI Volume Cloning . - Learn about Volume Snapshots . - Read about the feature gates mentioned on this page. 
# 12 - Storage Capacity 
Storage capacity is limited and may vary depending on the node on which a pod runs: network-attached storage might not be accessible by all nodes, or storage is local to a node to begin with. Feature state: Stable since Kubernetes v1.24 
This page describes how Kubernetes keeps track of storage capacity and how the scheduler uses that information to schedule Pods onto nodes that have access to enough storage capacity for the remaining missing volumes. Without storage capacity tracking, the scheduler may choose a node that doesn't have enough capacity to provision a volume and multiple scheduling retries will be needed. 
## Before you begin 
Kubernetes v1.37 includes cluster-level API support for storage capacity tracking. To use this you must also be using a CSI driver that supports capacity tracking. Consult the documentation for the CSI drivers that you use to find out whether this support is available and, if so, how to use it. If you are not running Kubernetes v1.37, check the documentation for that version of Kubernetes. 
## API 
There are two API extensions for this feature: 
- CSIStorageCapacity objects: these get produced by a CSI driver in the namespace where the driver is installed. Each object contains capacity information for one storage class and defines which nodes have access to that storage. - The CSIDriverSpec.StorageCapacityfield : when set to true, the Kubernetes scheduler will consider storage capacity for volumes that use the CSI driver. 
## Scheduling 
Storage capacity information is used by the Kubernetes scheduler if: 
- a Pod uses a volume that has not been created yet, - that volume uses a StorageClass which references a CSI driver and uses WaitForFirstConsumervolume binding mode , and - the CSIDriverobject for the driver has StorageCapacityset to true. 
In that case, the scheduler only considers nodes for the Pod which have enough storage available to them. This check is very simplistic and only compares the size of the volume against the capacity listed in CSIStorageCapacityobjects with a topology that includes the node. 
For volumes with Immediatevolume binding mode, the storage driver decides where to create the volume, independently of Pods that will use the volume. The scheduler then schedules Pods onto nodes where the volume is available after the volume has been created. 
For CSI ephemeral volumes , scheduling always happens without considering storage capacity. This is based on the assumption that this volume type is only used by special CSI drivers which are local to a node and do not need significant resources there. 
## Rescheduling 
When a node has been selected for a Pod with WaitForFirstConsumervolumes, that decision is still tentative. The next step is that the CSI storage driver gets asked to create the volume with a hint that the volume is supposed to be available on the selected node. 
Because Kubernetes might have chosen a node based on out-dated capacity information, it is possible that the volume cannot really be created. The node selection is then reset and the Kubernetes scheduler tries again to find a node for the Pod. 
## Limitations 
Storage capacity tracking increases the chance that scheduling works on the first try, but cannot guarantee this because the scheduler has to decide based on potentially out-dated information. Usually, the same retry mechanism as for scheduling without any storage capacity information handles scheduling failures. 
One situation where scheduling can fail permanently is when a Pod uses multiple volumes: one volume might have been created already in a topology segment which then does not have enough capacity left for another volume. Manual intervention is necessary to recover from this, for example by increasing capacity or deleting the volume that was already created. 
## What's next 
- For more information on the design, see the Storage Capacity Constraints for Pod Scheduling KEP . 
# 13 - Node-specific Volume Limits 
This page describes the maximum number of volumes that can be attached to a Node for various cloud providers. 
Cloud providers like Google, Amazon, and Microsoft typically have a limit on how many volumes can be attached to a Node. It is important for Kubernetes to respect those limits. Otherwise, Pods scheduled on a Node could get stuck waiting for volumes to attach. 
## Kubernetes default limits 
The Kubernetes scheduler has default limits on the number of volumes that can be attached to a Node: 
|  Cloud service  | Maximum volumes per Node  |
|  Amazon Elastic Block Store (EBS)  | 39  |
|  Google Persistent Disk  | 16  |
|  Microsoft Azure Disk Storage  | 16  |
## Dynamic volume limits Feature state: Stable since Kubernetes v1.17 
Dynamic volume limits are supported for following volume types. 
- Amazon EBS - Google Persistent Disk - Azure Disk - CSI 
For volumes managed by in-tree volume plugins, Kubernetes automatically determines the Node type and enforces the appropriate maximum number of volumes for the node. For example: 
- 
On Google Compute Engine , up to 127 volumes can be attached to a node, depending on the node type . - 
For Amazon EBS disks on M5,C5,R5,T3 and Z1D instance types, Kubernetes allows only 25 volumes to be attached to a Node. For other instance types on Amazon Elastic Compute Cloud (EC2) , Kubernetes allows 39 volumes to be attached to a Node. - 
On Azure, up to 64 disks can be attached to a node, depending on the node type. For more details, refer to Sizes for virtual machines in Azure . - 
If a CSI storage driver advertises a maximum number of volumes for a Node (using NodeGetInfo), the kube-scheduler honors that limit. Refer to the CSI specifications for details. - 
For volumes managed by in-tree plugins that have been migrated to a CSI driver, the maximum number of volumes will be the one reported by the CSI driver. 
### Mutable CSI Node Allocatable Count Feature state: Stable since Kubernetes v1.36; enabled by default More information about this feature 
This is a stable feature in , and has been since version 1.36. It was first available in the v1.33 release. 
CSI drivers can dynamically adjust the maximum number of volumes that can be attached to a Node at runtime. This enhances scheduling accuracy and reduces pod scheduling failures due to changes in resource availability. 
To use this feature, you must enable the MutableCSINodeAllocatableCountfeature gate on the following components: 
- kube-apiserver- kubelet
#### Periodic Updates 
When enabled, CSI drivers can request periodic updates to their volume limits by setting the nodeAllocatableUpdatePeriodSecondsfield in the CSIDriverspecification. For example: 
```
apiVersion:storage.k8s.io/v1kind:CSIDrivermetadata:name:hostpath.csi.k8s.iospec:nodeAllocatableUpdatePeriodSeconds:60
```

Kubelet will periodically call the corresponding CSI driver’s NodeGetInfoendpoint to refresh the maximum number of attachable volumes, using the interval specified in nodeAllocatableUpdatePeriodSeconds. The minimum allowed value for this field is 10 seconds. 
If a volume attachment operation fails with a ResourceExhaustederror (gRPC code 8), Kubernetes triggers an immediate update to the allocatable volume count for that Node. Additionally, kubelet marks affected pods as Failed, allowing their controllers to handle recreation. This prevents pods from getting stuck indefinitely in the ContainerCreatingstate. 
### Preventing Pod placement without CSI driver Feature state: Beta since Kubernetes v1.37; enabled by default 
The VolumeLimitScalingfeature gate is enabled by default in Kubernetes v1.37. 
However, preventing pod placement on nodes without a CSI driver requires explicit opt-in via the spec.preventPodSchedulingIfMissingfield of the CSIDriverobject. 
The preventPodSchedulingIfMissingfield defaults to falseand must be set to trueif you do not want pods to be scheduled on nodes without a CSI driver. This decision to default to falsewas made for backward compatibility reasons and compatibility with Cluster AutoScaler which may not be aware of CSI volume limits during the autoscaling phase (see section below). 
```
apiVersion:storage.k8s.io/v1kind:CSIDrivermetadata:name:hostpath.csi.k8s.iospec:preventPodSchedulingIfMissing:true
```

### CSI volume attach limits and cluster autoscaler 
Cluster autoscaler can account for CSI volume limits when --enable-csi-node-aware-scheduling=true. This option is independent of the VolumeLimitScalingfeature gate. 
If you use cluster autoscaler, only set spec.preventPodSchedulingIfMissingto truewhen cluster autoscaler is configured with --enable-csi-node-aware-scheduling=true. Otherwise, its scheduling simulations do not include the required CSINodeinformation for new nodes, and cluster autoscaler might fail to scale up for pending Pods that use CSI volumes. 
# 14 - Local ephemeral storage 
Nodes have local ephemeral storage, backed by locally-attached writeable devices or, sometimes, by RAM. "Ephemeral" means that there is no long-term guarantee about durability. 
Pods use ephemeral local storage for scratch space, caching, and for logs. The kubelet can provide scratch space to Pods using local ephemeral storage to mount emptyDirvolumes into containers. 
The kubelet also uses this kind of storage to hold node-level container logs , container images, and the writable layers of running containers. 
#### Caution: If a node fails, the data in its ephemeral storage can be lost. Your applications cannot expect any performance SLAs (disk IOPS for example) from local ephemeral storage. 
#### Note: 
To make the resource quota work on ephemeral-storage, two things need to be done: 
- An admin sets the resource quota for ephemeral-storage in a namespace. - A user needs to specify limits for the ephemeral-storage resource in the Pod spec. 
If the user doesn't specify the ephemeral-storage resource limit in the Pod spec, the resource quota is not enforced on ephemeral-storage. 
Kubernetes lets you track, reserve and limit the amount of ephemeral local storage a Pod can consume. 
## Configurations for local ephemeral storage 
Kubernetes supports the following ways to configure local ephemeral storage on a node: 
- Single filesystem - Runtime filesystem - Split image filesystem 
In this configuration, you place all different kinds of ephemeral local data ( emptyDirvolumes, writeable layers, container images, logs) into one filesystem. 
The kubelet also writes node-level container logs and treats these similarly to ephemeral local storage. 
The kubelet writes logs to files inside its configured log directory ( /var/logby default); and has a base directory for other locally stored data ( /var/lib/kubeletby default). 
Typically, both /var/lib/kubeletand /var/logare on the system root filesystem, and the kubelet is designed with that layout in mind. 
Your node can have as many other filesystems, not used for Kubernetes, as you like. 
You use one filesystem on the node for ephemeral data from running Pods, such as logs and emptyDirvolumes. You can also use this filesystem for other data, such as system logs that are not related to Kubernetes; it can even be the root filesystem. 
The kubelet also writes node-level container logs into the first filesystem, and treats these similarly to ephemeral local storage. 
You also use a separate filesystem, backed by a different logical storage device. In this configuration, the container runtime stores both container image layers and writeable layers on this second filesystem. Configure this storage location in your container runtime, not in the kubelet. 
The first filesystem does not hold any image layers or writeable layers. 
Your node can have as many other filesystems, not used for Kubernetes, as you like. 
In this configuration, container image layers are on a separate filesystem, and container writeable layers are on the same filesystem as the kubelet's ephemeral data, such as logs and emptyDirvolumes. 
This layout requires support for the containerfseviction signals. For details about the feature gate and the container runtimes that support this layout, see node-pressure eviction . 
The node-pressure eviction page refers to these observed filesystems as nodefs, imagefs, and containerfs. Those names do not always mean separate mount points. 
The kubelet can measure local storage use when you set up the node using one of the supported configurations for local ephemeral storage. 
If you have a different configuration, then the kubelet does not apply resource limits for ephemeral local storage. 
#### Note: The kubelet tracks tmpfsemptyDir volumes as container memory use, rather than as local ephemeral storage. 
#### Note: The kubelet can only track ephemeral storage on the filesystems it observes through the supported layouts. If you mount extra filesystems under paths such as /var/lib/kubelet, /var/log, or the container runtime storage directory outside those layouts, the kubelet might not report ephemeral storage correctly. 
## Setting requests and limits for local ephemeral storage 
You can specify ephemeral-storagefor managing local ephemeral storage. Each container of a Pod can specify either or both of the following: 
- spec.containers[].resources.limits.ephemeral-storage- spec.containers[].resources.requests.ephemeral-storage
Limits and requests for ephemeral-storageare measured in byte quantities. You can express storage as a plain integer or as a fixed-point number using one of these suffixes: E, P, T, G, M, k. You can also use the power-of-two equivalents: Ei, Pi, Ti, Gi, Mi, Ki. For example, the following quantities all represent roughly the same value: 
- 128974848- 129e6- 129M- 123Mi
Pay attention to the case of the suffixes. If you request 400mof ephemeral-storage, this is a request for 0.4 bytes. Someone who types that probably meant to ask for 400 mebibytes ( 400Mi) or 400 megabytes ( 400M). 
In the following example, the Pod has two containers. Each container has a request of 2GiB of local ephemeral storage. Each container has a limit of 4GiB of local ephemeral storage. Therefore, the Pod has a request of 4GiB of local ephemeral storage, and a limit of 8GiB of local ephemeral storage. 500Mi of that limit could be consumed by the emptyDirvolume. 
```
apiVersion:v1kind:Podmetadata:name:frontendspec:containers:- name:appimage:images.my-company.example/app:v4resources:requests:ephemeral-storage:"2Gi"limits:ephemeral-storage:"4Gi"volumeMounts:- name:ephemeralmountPath:"/tmp"- name:log-aggregatorimage:images.my-company.example/log-aggregator:v6resources:requests:ephemeral-storage:"2Gi"limits:ephemeral-storage:"4Gi"volumeMounts:- name:ephemeralmountPath:"/tmp"volumes:- name:ephemeralemptyDir:sizeLimit:500Mi
```

## How Pods with ephemeral-storage requests are scheduled 
When you create a Pod, the Kubernetes scheduler selects a node for the Pod to run on. Each node has a maximum amount of local ephemeral storage it can provide for Pods. For more information, see Node Allocatable . 
The scheduler ensures that the sum of the resource requests of the scheduled containers is less than the capacity of the node. 
## Ephemeral storage consumption management 
If the kubelet is managing local ephemeral storage as a resource, then the kubelet measures storage use in: 
- emptyDirvolumes, except tmpfs emptyDirvolumes - directories holding node-level logs - writeable container layers 
If a Pod is using more ephemeral storage than you allow it to, the kubelet sets an eviction signal that triggers Pod eviction. 
For container-level isolation, if a container's writable layer and log usage exceeds its storage limit, the kubelet marks the Pod for eviction. 
For pod-level isolation the kubelet works out an overall Pod storage limit by summing the limits for the containers in that Pod. In this case, if the sum of the local ephemeral storage usage from all containers and also the Pod's emptyDirvolumes exceeds the overall Pod storage limit, then the kubelet also marks the Pod for eviction. 
#### Caution: 
If the kubelet is not measuring local ephemeral storage, then a Pod that exceeds its local storage limit will not be evicted for breaching local storage resource limits. 
However, if the filesystem space for writeable container layers, node-level logs, or emptyDirvolumes falls low, the node taints itself as short on local storage and this taint triggers eviction for any Pods that don't specifically tolerate the taint. 
See the supported configurations for ephemeral local storage. 
The kubelet supports different ways to measure Pod storage use: 
- Periodic scanning - Filesystem project quota 
The kubelet performs regular, scheduled checks that scan each emptyDirvolume, container log directory, and writeable container layer. 
The scan measures how much space is used. 
#### Note: 
In this mode, the kubelet does not track open file descriptors for deleted files. 
If you (or a container) create a file inside an emptyDirvolume, something then opens that file, and you delete the file while it is still open, then the inode for the deleted file stays until you close that file but the kubelet does not categorize the space as in use. 
```
        <div class="feature-state-notice feature-beta" title="Feature Gate: LocalStorageCapacityIsolationFSQuotaMonitoring">
          <span class="feature-state-name">Feature state:</span>
          <span class="feature-state-details">
           
             <span class="feature-state-stage">Beta</span> since Kubernetes v1.31; disabled by default
           </span>
        </div>
        
        
        <div class="feature-beta">
          
          
            <details>
            <summary>More information about this feature</summary>
            <p>To use this feature, you (or a cluster administrator) will need to enable the <a href="/docs/reference/command-line-tools-reference/feature-gates/#LocalStorageCapacityIsolationFSQuotaMonitoring"><tt>LocalStorageCapacityIsolationFSQuotaMonitoring</tt></a> feature gate for all relevant components in your cluster.</p>

```

See Enable Or Disable Feature Gates for more information. 
```
            </details>
            </div>

```

Project quotas are an operating-system level feature for managing storage use on filesystems. With Kubernetes, you can enable project quotas for monitoring storage use. Make sure that the filesystem backing the emptyDirvolumes, on the node, provides project quota support. For example, XFS and ext4fs offer project quotas. 
#### Note: Project quotas let you monitor storage use; they do not enforce limits. 
Kubernetes uses project IDs starting from 1048576. The IDs in use are registered in /etc/projectsand /etc/projid. If project IDs in this range are used for other purposes on the system, those project IDs must be registered in /etc/projectsand /etc/projidso that Kubernetes does not use them. 
Quotas are faster and more accurate than directory scanning. When a directory is assigned to a project, all files created under a directory are created in that project, and the kernel merely has to keep track of how many blocks are in use by files in that project. If a file is created and deleted, but has an open file descriptor, it continues to consume space. Quota tracking records that space accurately whereas directory scans overlook the storage used by deleted files. 
To use quotas to track a pod's resource usage, the pod must be in a user namespace. Within user namespaces, the kernel restricts changes to projectIDs on the filesystem, ensuring the reliability of storage metrics calculated by quotas. 
If you want to use project quotas, you should: 
- 
Enable the LocalStorageCapacityIsolationFSQuotaMonitoring=truefeature gate using the featureGatesfield in the kubelet configuration . - 
Ensure the UserNamespacesSupportfeature gate is enabled, and that the kernel, CRI implementation and OCI runtime support user namespaces. - 
Ensure that the root filesystem (or optional runtime filesystem) has project quotas enabled. All XFS filesystems support project quotas. For ext4 filesystems, you need to enable the project quota tracking feature while the filesystem is not mounted. 
```
# For ext4, with /dev/block-device not mountedsudo tune2fs -O project -Q prjquota /dev/block-device

```
- 
Ensure that the root filesystem (or optional runtime filesystem) is mounted with project quotas enabled. For both XFS and ext4fs, the mount option is named prjquota. 
If you don't want to use project quotas, you should: 
- Disable the LocalStorageCapacityIsolationFSQuotaMonitoringfeature gate using the featureGatesfield in the kubelet configuration . 
## What's next 
- Read about project quotas in XFS 
# 15 - Volume Health Monitoring Feature state: Alpha since Kubernetes v1.21; disabled by default More information about this feature 
To use this feature, you (or a cluster administrator) will need to enable the CSIVolumeHealth feature gate for all relevant components in your cluster. 
See Enable Or Disable Feature Gates for more information. 
CSI volume health monitoring lets a CSI driver report health problems with a volume or with its storage backend directly to Kubernetes. The driver reports through CSI RPCs, and Kubernetes surfaces the reports on three status fields: PersistentVolumeClaim .status.healthStatus, Pod .status.volumeHealth, and CSINode .status.storageHealth. Automation can watch these durable status fields instead of having to reconstruct volume health from ephemeral Events or from vendor-specific dashboards. 
#### Note: The CSIVolumeHealthfeature gate has existed since Kubernetes v1.21, but the mechanism described on this page is a redesign that replaces the original alpha implementation. See Limitations for what changed. 
## How it works 
The CSI spec defines four RPCs for health reporting: 
- On the CSI controller plugin: ControllerListVolumeHealthand ControllerGetVolumeHealth, for controller-observed, per-volume health. - On the CSI node plugin: NodeGetVolumeHealth, for node-observed, per-volume health, and NodeGetStorageHealth, for the health of the storage backend as seen from that node. 
A driver only needs to implement the RPCs it wants to support, and advertises support through CSI plugin capabilities. A driver that implements none of these RPCs is never probed, and reporting stays dormant for that driver. A driver that advertises the controller LIST_VOLUME_HEALTHcapability must also advertise GET_VOLUME_HEALTH; the csi-external-health-monitor-controllersidecar enforces this requirement. 
Each health report carries a statusdrawn from a small, machine-parseable set of values, together with a driver-defined reasonand an optional human-readable message: 
- Volume-level status values (used for PersistentVolumeClaim.status.healthStatusand Pod.status.volumeHealth): Inaccessible, DataLoss, Degraded. - Storage-backend status values (used for CSINode.status.storageHealth): StorageUnreachable, StorageDegraded. 
The node-side and controller-side reports are independent: a volume can be Inaccessiblefrom one node that lost its data path to the backend while the controller plugin still reports the volume as healthy, and vice versa. 
## Health reported on Pods 
For volumes that use a CSI driver supporting the node-side NodeGetVolumeHealthRPC, the kubelet periodically calls that RPC for each CSI volume it has mounted for a Pod, and writes the result to pod.status.volumeHealth, keyed by the volume name from pod.spec.volumes. The probe interval is the kubelet's volumeStatsAggPeriodsetting (the --volume-stats-agg-periodcommand line flag). 
```
apiVersion:v1kind:Pod# ...status:volumeHealth:- name:my-volumehealthConditions:- status:Inaccessiblereason:VolumeNotFoundmessage:"volume not found on the storage backend"lastTransitionTime:"2026-07-20T12:00:00Z"
```

The kubelet only writes pods/status, a subresource it is already authorized to update for Pods bound to its own node, so no new authorization is required for this field. 
## Health reported on CSINode 
For each CSI driver registered on a node that supports NodeGetStorageHealth, the kubelet periodically calls that RPC and writes the result to csinode.status.storageHealth, keyed by driver name. 
```
apiVersion:storage.k8s.io/v1kind:CSINode# ...status:storageHealth:- name:csi.example.comhealthConditions:- status:StorageUnreachablereason:NetworkPartitionmessage:"data path to the storage backend is unreachable from this node"
```

A StorageHealthConditionentry can optionally scope itself to a specific accessModeor volumeMode, for backends that degrade asymmetrically (for example, a network problem that affects ReadWriteManyaccess but not ReadWriteOnce). 
Writing to csinodes/statusis a new capability added by this feature: the Node authorization mode and the NodeRestriction admission plugin only allow a kubelet to patch the CSINodeobject that matches its own node, and only while the CSIVolumeHealthfeature gate is enabled. 
## Health reported on PersistentVolumeClaims 
Controller-observed volume health is written to persistentvolumeclaim.status.healthStatusby the csi-external-health-monitor-controllersidecar that runs alongside a CSI driver's controller plugin. The sidecar calls ControllerListVolumeHealth(or falls back to ControllerGetVolumeHealthper volume) and writes the result: 
```
apiVersion:v1kind:PersistentVolumeClaim# ...status:healthStatus:healthConditions:- status:Inaccessiblereason:VolumeNotFoundmessage:"volume not found on the storage backend"lastTransitionTime:"2026-07-20T12:00:00Z"
```

No node ever writes this field; only the sidecar, running in the control plane, does. This keeps a compromised or misbehaving node from being able to influence what other users of the cluster see on a PVC. 
Whether this path is available for a given driver depends on that driver, and its deployment of the csi-external-health-monitor-controllersidecar, having adopted the new controller RPCs. 
## Enabling volume health monitoring 
Volume health monitoring is controlled by a single feature gate , CSIVolumeHealth, on both kube-apiserverand the kubelet: 
- On kube-apiserver, enabling the feature gate allows the new status fields to be written and read; disabling it drops the fields on the next write to the object, while preserving values already stored. - On the kubelet, enabling the feature gate starts the periodic node-side probing described above. 
Controller-side monitoring, which populates persistentvolumeclaim.status.healthStatus, does not have its own feature gate. Deploying the csi-external-health-monitor-controllersidecar alongside your CSI driver's controller plugin is itself the controller-side opt-in. 
Enabling the feature gate does not, by itself, cause any health information to appear: a CSI driver also has to advertise and implement the corresponding RPCs. Check your CSI driver's documentation to see which of the four RPCs, if any, it supports. 
## Monitoring 
The kubelet exposes a csi_node_storage_health_statusgauge metric, labeled by driver_name, status, and reason, with a value of 1for each storage-backend condition currently reported for a driver on that node. 
## Limitations 
- Kubernetes only surfaces these health reports; it does not act on them. Nothing in Kubernetes reschedules Pods, fails over volumes, or otherwise reacts to a reported condition on its own. Building a remediation controller on top of these status fields is left to cluster operators and vendors. - An older, alpha implementation of the same CSIVolumeHealthfeature gate (available starting in Kubernetes v1.21) reported abnormal volume conditions using Kubernetes Events and a kubelet_volume_stats_health_status_abnormalmetric. That mechanism has been replaced by the status fields and RPCs described on this page, and no longer exists. 
## What's next 
- Read KEP-1432 for the full design. - See the CSI driver documentation to find out which CSI drivers implement volume health monitoring. 
# 16 - Windows Storage 
This page provides an storage overview specific to the Windows operating system. 
## Persistent storage 
Windows has a layered filesystem driver to mount container layers and create a copy filesystem based on NTFS. All file paths in the container are resolved only within the context of that container. 
- With Docker, volume mounts can only target a directory in the container, and not an individual file. This limitation does not apply to containerd. - Volume mounts cannot project files or directories back to the host filesystem. - Read-only filesystems are not supported because write access is always required for the Windows registry and SAM database. However, read-only volumes are supported. - Volume user-masks and permissions are not available. Because the SAM is not shared between the host & container, there's no mapping between them. All permissions are resolved within the context of the container. 
As a result, the following storage functionality is not supported on Windows nodes: 
- Volume subpath mounts: only the entire volume can be mounted in a Windows container - Subpath volume mounting for Secrets - Host mount projection - Read-only root filesystem (mapped volumes still support readOnly) - Block device mapping - Memory as the storage medium (for example, emptyDir.mediumset to Memory) - File system features like uid/gid; per-user Linux filesystem permissions - Setting secret permissions with DefaultMode (due to UID/GID dependency) - NFS based storage/volume support - Expanding the mounted volume (resizefs) 
Kubernetes volumes enable complex applications, with data persistence and Pod volume sharing requirements, to be deployed on Kubernetes. Management of persistent volumes associated with a specific storage back-end or protocol includes actions such as provisioning/de-provisioning/resizing of volumes, attaching/detaching a volume to/from a Kubernetes node and mounting/dismounting a volume to/from individual containers in a pod that needs to persist data. 
Volume management components are shipped as Kubernetes volume plugin . The following broad classes of Kubernetes volume plugins are supported on Windows: 
- FlexVolume plugins
  - Please note that FlexVolumes have been deprecated as of 1.23 - CSI Plugins
##### In-tree volume plugins 
The following in-tree plugins support persistent storage on Windows nodes: 
- azureFile- vsphereVolume
- - - - - - 

- - - - 

#### 📄 Sub-topic: [https://kubernetes.io/docs/concepts/storage/dynamic-provisioning](https://kubernetes.io/docs/concepts/storage/dynamic-provisioning)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - Bahasa Indonesia (Indonesian)   - 日本語 (Japanese)   - 한국어 (Korean)   - Español (Spanish)   - বাংলা (Bengali)   - Français (French)   - Deutsch (German)   - हिन्दी (Hindi)   - Italiano (Italian)   - فارسی (Persian)   - Polski (Polish)   - Português (Portuguese)   - Русский (Russian)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# Dynamic Volume Provisioning 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- - - - - 
- - - - 
# Dynamic Volume Provisioning 
Dynamic volume provisioning allows storage volumes to be created on-demand. Without dynamic provisioning, cluster administrators have to manually make calls to their cloud or storage provider to create new storage volumes, and then create PersistentVolumeobjects to represent them in Kubernetes. The dynamic provisioning feature eliminates the need for cluster administrators to pre-provision storage. Instead, it automatically provisions storage when users create PersistentVolumeClaimobjects . 
## Background 
The implementation of dynamic volume provisioning is based on the API object StorageClassfrom the API group storage.k8s.io. A cluster administrator can define as many StorageClassobjects as needed, each specifying a volume plugin (aka provisioner ) that provisions a volume and the set of parameters to pass to that provisioner when provisioning. A cluster administrator can define and expose multiple flavors of storage (from the same or different storage systems) within a cluster, each with a custom set of parameters. This design also ensures that end users don't have to worry about the complexity and nuances of how storage is provisioned, but still have the ability to select from multiple storage options. 
For more details, see the Storage Classes concept. 
## Enabling Dynamic Provisioning 
To enable dynamic provisioning, a cluster administrator needs to pre-create one or more StorageClass objects for users. StorageClass objects define which provisioner should be used and what parameters should be passed to that provisioner when dynamic provisioning is invoked. The name of a StorageClass object must be a valid DNS subdomain name . 
The following manifest creates a storage class "slow" which provisions standard disk-like persistent disks. 
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:slowprovisioner:kubernetes.io/gce-pdparameters:type:pd-standard
```

The following manifest creates a storage class "fast" which provisions SSD-like persistent disks. 
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:fastprovisioner:kubernetes.io/gce-pdparameters:type:pd-ssd
```

## Using Dynamic Provisioning 
Users request dynamically provisioned storage by including a storage class in their PersistentVolumeClaim. Before Kubernetes v1.6, this was done via the volume.beta.kubernetes.io/storage-classannotation. However, this annotation is deprecated since v1.9. Users now can and should instead use the storageClassNamefield of the PersistentVolumeClaimobject. The value of this field must match the name of a StorageClassconfigured by the administrator (see Enabling Dynamic Provisioning ). 
To select the "fast" storage class, for example, a user would create the following PersistentVolumeClaim: 
```
apiVersion:v1kind:PersistentVolumeClaimmetadata:name:claim1spec:accessModes:- ReadWriteOncestorageClassName:fastresources:requests:storage:30Gi
```

This claim results in an SSD-like Persistent Disk being automatically provisioned. When the claim is deleted, the volume is destroyed. 
## Defaulting Behavior 
Dynamic provisioning can be enabled on a cluster such that all claims are dynamically provisioned if no storage class is specified. A cluster administrator can enable this behavior by: 
- Marking one StorageClassobject as default . - Making sure that the DefaultStorageClassadmission controller is enabled on the API server. 
An administrator can mark a specific StorageClassas default by adding the storageclass.kubernetes.io/is-default-classannotation to it. When a default StorageClassexists in a cluster and a user creates a PersistentVolumeClaimwith storageClassNameunspecified, the DefaultStorageClassadmission controller automatically adds the storageClassNamefield pointing to the default storage class. 
Note that if you set the storageclass.kubernetes.io/is-default-classannotation to true on more than one StorageClass in your cluster, and you then create a PersistentVolumeClaimwith no storageClassNameset, Kubernetes uses the most recently created default StorageClass. 
## Topology Awareness 
In Multi-Zone clusters, Pods can be spread across Zones in a Region. Single-Zone storage backends should be provisioned in the Zones where Pods are scheduled. This can be accomplished by setting the Volume Binding Mode . 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified October 29, 2025 at 10:49 AM PST: fix style in concepts/storage/dynamic-provisioning.md (47b7c6f6b3) 
- - - - - - 

- - - - 

#### 📄 Sub-topic: [https://kubernetes.io/docs/concepts/storage/ephemeral-storage](https://kubernetes.io/docs/concepts/storage/ephemeral-storage)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - 日本語 (Japanese)   - বাংলা (Bengali)   - Français (French)   - Deutsch (German)   - हिन्दी (Hindi)   - Bahasa Indonesia (Indonesian)   - Italiano (Italian)   - 한국어 (Korean)   - فارسی (Persian)   - Polski (Polish)   - Português (Portuguese)   - Русский (Russian)   - Español (Spanish)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# Local ephemeral storage 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- - - - - 
- - - - 
# Local ephemeral storage 
Nodes have local ephemeral storage, backed by locally-attached writeable devices or, sometimes, by RAM. "Ephemeral" means that there is no long-term guarantee about durability. 
Pods use ephemeral local storage for scratch space, caching, and for logs. The kubelet can provide scratch space to Pods using local ephemeral storage to mount emptyDirvolumes into containers. 
The kubelet also uses this kind of storage to hold node-level container logs , container images, and the writable layers of running containers. 
#### Caution: If a node fails, the data in its ephemeral storage can be lost. Your applications cannot expect any performance SLAs (disk IOPS for example) from local ephemeral storage. 
#### Note: 
To make the resource quota work on ephemeral-storage, two things need to be done: 
- An admin sets the resource quota for ephemeral-storage in a namespace. - A user needs to specify limits for the ephemeral-storage resource in the Pod spec. 
If the user doesn't specify the ephemeral-storage resource limit in the Pod spec, the resource quota is not enforced on ephemeral-storage. 
Kubernetes lets you track, reserve and limit the amount of ephemeral local storage a Pod can consume. 
## Configurations for local ephemeral storage 
Kubernetes supports the following ways to configure local ephemeral storage on a node: 
- Single filesystem - Runtime filesystem - Split image filesystem 
In this configuration, you place all different kinds of ephemeral local data ( emptyDirvolumes, writeable layers, container images, logs) into one filesystem. 
The kubelet also writes node-level container logs and treats these similarly to ephemeral local storage. 
The kubelet writes logs to files inside its configured log directory ( /var/logby default); and has a base directory for other locally stored data ( /var/lib/kubeletby default). 
Typically, both /var/lib/kubeletand /var/logare on the system root filesystem, and the kubelet is designed with that layout in mind. 
Your node can have as many other filesystems, not used for Kubernetes, as you like. 
You use one filesystem on the node for ephemeral data from running Pods, such as logs and emptyDirvolumes. You can also use this filesystem for other data, such as system logs that are not related to Kubernetes; it can even be the root filesystem. 
The kubelet also writes node-level container logs into the first filesystem, and treats these similarly to ephemeral local storage. 
You also use a separate filesystem, backed by a different logical storage device. In this configuration, the container runtime stores both container image layers and writeable layers on this second filesystem. Configure this storage location in your container runtime, not in the kubelet. 
The first filesystem does not hold any image layers or writeable layers. 
Your node can have as many other filesystems, not used for Kubernetes, as you like. 
In this configuration, container image layers are on a separate filesystem, and container writeable layers are on the same filesystem as the kubelet's ephemeral data, such as logs and emptyDirvolumes. 
This layout requires support for the containerfseviction signals. For details about the feature gate and the container runtimes that support this layout, see node-pressure eviction . 
The node-pressure eviction page refers to these observed filesystems as nodefs, imagefs, and containerfs. Those names do not always mean separate mount points. 
The kubelet can measure local storage use when you set up the node using one of the supported configurations for local ephemeral storage. 
If you have a different configuration, then the kubelet does not apply resource limits for ephemeral local storage. 
#### Note: The kubelet tracks tmpfsemptyDir volumes as container memory use, rather than as local ephemeral storage. 
#### Note: The kubelet can only track ephemeral storage on the filesystems it observes through the supported layouts. If you mount extra filesystems under paths such as /var/lib/kubelet, /var/log, or the container runtime storage directory outside those layouts, the kubelet might not report ephemeral storage correctly. 
## Setting requests and limits for local ephemeral storage 
You can specify ephemeral-storagefor managing local ephemeral storage. Each container of a Pod can specify either or both of the following: 
- spec.containers[].resources.limits.ephemeral-storage- spec.containers[].resources.requests.ephemeral-storage
Limits and requests for ephemeral-storageare measured in byte quantities. You can express storage as a plain integer or as a fixed-point number using one of these suffixes: E, P, T, G, M, k. You can also use the power-of-two equivalents: Ei, Pi, Ti, Gi, Mi, Ki. For example, the following quantities all represent roughly the same value: 
- 128974848- 129e6- 129M- 123Mi
Pay attention to the case of the suffixes. If you request 400mof ephemeral-storage, this is a request for 0.4 bytes. Someone who types that probably meant to ask for 400 mebibytes ( 400Mi) or 400 megabytes ( 400M). 
In the following example, the Pod has two containers. Each container has a request of 2GiB of local ephemeral storage. Each container has a limit of 4GiB of local ephemeral storage. Therefore, the Pod has a request of 4GiB of local ephemeral storage, and a limit of 8GiB of local ephemeral storage. 500Mi of that limit could be consumed by the emptyDirvolume. 
```
apiVersion:v1kind:Podmetadata:name:frontendspec:containers:- name:appimage:images.my-company.example/app:v4resources:requests:ephemeral-storage:"2Gi"limits:ephemeral-storage:"4Gi"volumeMounts:- name:ephemeralmountPath:"/tmp"- name:log-aggregatorimage:images.my-company.example/log-aggregator:v6resources:requests:ephemeral-storage:"2Gi"limits:ephemeral-storage:"4Gi"volumeMounts:- name:ephemeralmountPath:"/tmp"volumes:- name:ephemeralemptyDir:sizeLimit:500Mi
```

## How Pods with ephemeral-storage requests are scheduled 
When you create a Pod, the Kubernetes scheduler selects a node for the Pod to run on. Each node has a maximum amount of local ephemeral storage it can provide for Pods. For more information, see Node Allocatable . 
The scheduler ensures that the sum of the resource requests of the scheduled containers is less than the capacity of the node. 
## Ephemeral storage consumption management 
If the kubelet is managing local ephemeral storage as a resource, then the kubelet measures storage use in: 
- emptyDirvolumes, except tmpfs emptyDirvolumes - directories holding node-level logs - writeable container layers 
If a Pod is using more ephemeral storage than you allow it to, the kubelet sets an eviction signal that triggers Pod eviction. 
For container-level isolation, if a container's writable layer and log usage exceeds its storage limit, the kubelet marks the Pod for eviction. 
For pod-level isolation the kubelet works out an overall Pod storage limit by summing the limits for the containers in that Pod. In this case, if the sum of the local ephemeral storage usage from all containers and also the Pod's emptyDirvolumes exceeds the overall Pod storage limit, then the kubelet also marks the Pod for eviction. 
#### Caution: 
If the kubelet is not measuring local ephemeral storage, then a Pod that exceeds its local storage limit will not be evicted for breaching local storage resource limits. 
However, if the filesystem space for writeable container layers, node-level logs, or emptyDirvolumes falls low, the node taints itself as short on local storage and this taint triggers eviction for any Pods that don't specifically tolerate the taint. 
See the supported configurations for ephemeral local storage. 
The kubelet supports different ways to measure Pod storage use: 
- Periodic scanning - Filesystem project quota 
The kubelet performs regular, scheduled checks that scan each emptyDirvolume, container log directory, and writeable container layer. 
The scan measures how much space is used. 
#### Note: 
In this mode, the kubelet does not track open file descriptors for deleted files. 
If you (or a container) create a file inside an emptyDirvolume, something then opens that file, and you delete the file while it is still open, then the inode for the deleted file stays until you close that file but the kubelet does not categorize the space as in use. 
```
        <div class="feature-state-notice feature-beta" title="Feature Gate: LocalStorageCapacityIsolationFSQuotaMonitoring">
          <span class="feature-state-name">Feature state:</span>
          <span class="feature-state-details">
           
             <span class="feature-state-stage">Beta</span> since Kubernetes v1.31; disabled by default
           </span>
        </div>
        
        
        <div class="feature-beta">
          
          
            <details>
            <summary>More information about this feature</summary>
            <p>To use this feature, you (or a cluster administrator) will need to enable the <a href="/docs/reference/command-line-tools-reference/feature-gates/#LocalStorageCapacityIsolationFSQuotaMonitoring"><tt>LocalStorageCapacityIsolationFSQuotaMonitoring</tt></a> feature gate for all relevant components in your cluster.</p>

```

See Enable Or Disable Feature Gates for more information. 
```
            </details>
            </div>

```

Project quotas are an operating-system level feature for managing storage use on filesystems. With Kubernetes, you can enable project quotas for monitoring storage use. Make sure that the filesystem backing the emptyDirvolumes, on the node, provides project quota support. For example, XFS and ext4fs offer project quotas. 
#### Note: Project quotas let you monitor storage use; they do not enforce limits. 
Kubernetes uses project IDs starting from 1048576. The IDs in use are registered in /etc/projectsand /etc/projid. If project IDs in this range are used for other purposes on the system, those project IDs must be registered in /etc/projectsand /etc/projidso that Kubernetes does not use them. 
Quotas are faster and more accurate than directory scanning. When a directory is assigned to a project, all files created under a directory are created in that project, and the kernel merely has to keep track of how many blocks are in use by files in that project. If a file is created and deleted, but has an open file descriptor, it continues to consume space. Quota tracking records that space accurately whereas directory scans overlook the storage used by deleted files. 
To use quotas to track a pod's resource usage, the pod must be in a user namespace. Within user namespaces, the kernel restricts changes to projectIDs on the filesystem, ensuring the reliability of storage metrics calculated by quotas. 
If you want to use project quotas, you should: 
- 
Enable the LocalStorageCapacityIsolationFSQuotaMonitoring=truefeature gate using the featureGatesfield in the kubelet configuration . - 
Ensure the UserNamespacesSupportfeature gate is enabled, and that the kernel, CRI implementation and OCI runtime support user namespaces. - 
Ensure that the root filesystem (or optional runtime filesystem) has project quotas enabled. All XFS filesystems support project quotas. For ext4 filesystems, you need to enable the project quota tracking feature while the filesystem is not mounted. 
```
# For ext4, with /dev/block-device not mountedsudo tune2fs -O project -Q prjquota /dev/block-device

```
- 
Ensure that the root filesystem (or optional runtime filesystem) is mounted with project quotas enabled. For both XFS and ext4fs, the mount option is named prjquota. 
If you don't want to use project quotas, you should: 
- Disable the LocalStorageCapacityIsolationFSQuotaMonitoringfeature gate using the featureGatesfield in the kubelet configuration . 
## What's next 
- Read about project quotas in XFS 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified April 23, 2026 at 12:35 PM PST: docs: clarify kubelet filesystem layouts (6dc6c3a989) 
- - - - - - 

- - - - 

#### 📄 Sub-topic: [https://kubernetes.io/docs/concepts/storage/ephemeral-volumes](https://kubernetes.io/docs/concepts/storage/ephemeral-volumes)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - 日本語 (Japanese)   - 한국어 (Korean)   - Español (Spanish)   - বাংলা (Bengali)   - Français (French)   - Deutsch (German)   - हिन्दी (Hindi)   - Bahasa Indonesia (Indonesian)   - Italiano (Italian)   - فارسی (Persian)   - Polski (Polish)   - Português (Portuguese)   - Русский (Russian)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# Ephemeral Volumes 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- 
  -   -   -   -   -   -   - - 
  -   -   - 
- - - - 
# Ephemeral Volumes 
This document describes ephemeral volumes in Kubernetes. Familiarity with volumes is suggested, in particular PersistentVolumeClaim and PersistentVolume. 
Some applications need additional storage but don't care whether that data is stored persistently across restarts. For example, caching services are often limited by memory size and can move infrequently used data into storage that is slower than memory with little impact on overall performance. 
Other applications expect some read-only input data to be present in files, like configuration data or secret keys. 
Ephemeral volumes are designed for these use cases. Because volumes follow the Pod's lifetime and get created and deleted along with the Pod, Pods can be stopped and restarted without being limited to where some persistent volume is available. 
Ephemeral volumes are specified inline in the Pod spec, which simplifies application deployment and management. 
### Types of ephemeral volumes 
Kubernetes supports several different kinds of ephemeral volumes for different purposes: 
- emptyDir : empty at Pod startup, with storage coming locally from the kubelet base directory (usually the root disk) or RAM - configMap , downwardAPI , secret : inject different kinds of Kubernetes data into a Pod - image : allows mounting container image files or artifacts, directly to a Pod. - CSI ephemeral volumes : similar to the previous volume kinds, but provided by special CSI drivers which specifically support this feature - generic ephemeral volumes , which can be provided by all storage drivers that also support persistent volumes 
emptyDir, configMap, downwardAPI, secretare provided as local ephemeral storage . They are managed by kubelet on each node. 
CSI ephemeral volumes must be provided by third-party CSI storage drivers. 
Generic ephemeral volumes can be provided by third-party CSI storage drivers, but also by any other storage driver that supports dynamic provisioning. Some CSI drivers are written specifically for CSI ephemeral volumes and do not support dynamic provisioning: those then cannot be used for generic ephemeral volumes. 
The advantage of using third-party drivers is that they can offer functionality that Kubernetes itself does not support, for example storage with different performance characteristics than the disk that is managed by kubelet, or injecting different data. 
### CSI ephemeral volumes Feature state: Stable since Kubernetes v1.25 
#### Note: CSI ephemeral volumes are only supported by a subset of CSI drivers. The Kubernetes CSI Drivers list shows which drivers support ephemeral volumes. 
Conceptually, CSI ephemeral volumes are similar to configMap, downwardAPIand secretvolume types: the storage is managed locally on each node and is created together with other local resources after a Pod has been scheduled onto a node. Kubernetes has no concept of rescheduling Pods anymore at this stage. Volume creation has to be unlikely to fail, otherwise Pod startup gets stuck. In particular, storage capacity aware Pod scheduling is not supported for these volumes. They are currently also not covered by the storage resource usage limits of a Pod, because that is something that kubelet can only enforce for storage that it manages itself. 
Here's an example manifest for a Pod that uses CSI ephemeral storage: 
```
kind:PodapiVersion:v1metadata:name:my-csi-appspec:containers:- name:my-frontendimage:busybox:1.28volumeMounts:- mountPath:"/data"name:my-csi-inline-volcommand:["sleep","1000000"]volumes:- name:my-csi-inline-volcsi:driver:inline.storage.kubernetes.iovolumeAttributes:foo:bar
```

The volumeAttributesdetermine what volume is prepared by the driver. These attributes are specific to each driver and not standardized. See the documentation of each CSI driver for further instructions. 
### CSI driver restrictions 
CSI ephemeral volumes allow users to provide volumeAttributesdirectly to the CSI driver as part of the Pod spec. A CSI driver allowing volumeAttributesthat are typically restricted to administrators is NOT suitable for use in an inline ephemeral volume. For example, parameters that are normally defined in the StorageClass should not be exposed to users through the use of inline ephemeral volumes. 
Cluster administrators who need to restrict the CSI drivers that are allowed to be used as inline volumes within a Pod spec may do so by: 
- Removing Ephemeralfrom volumeLifecycleModesin the CSIDriver spec, which prevents the driver from being used as an inline ephemeral volume. - Using an admission webhook to restrict how this driver is used. 
### Generic ephemeral volumes Feature state: Stable since Kubernetes v1.23 
Generic ephemeral volumes are similar to emptyDirvolumes in the sense that they provide a per-pod directory for scratch data that is usually empty after provisioning. But they may also have additional features: 
- Storage can be local or network-attached. - Volumes can have a fixed size that Pods are not able to exceed. - Volumes may have some initial data, depending on the driver and parameters. - Typical operations on volumes are supported assuming that the driver supports them, including snapshotting , cloning , resizing , and storage capacity tracking . 
Example: 
```
kind:PodapiVersion:v1metadata:name:my-appspec:containers:- name:my-frontendimage:busybox:1.28volumeMounts:- mountPath:"/scratch"name:scratch-volumecommand:["sleep","1000000"]volumes:- name:scratch-volumeephemeral:volumeClaimTemplate:metadata:labels:type:my-frontend-volumespec:accessModes:["ReadWriteOnce"]storageClassName:"scratch-storage-class"resources:requests:storage:1Gi
```

### Lifecycle and PersistentVolumeClaim 
The key design idea is that the parameters for a volume claim are allowed inside a volume source of the Pod. Labels, annotations and the whole set of fields for a PersistentVolumeClaim are supported. When such a Pod gets created, the ephemeral volume controller then creates an actual PersistentVolumeClaim object in the same namespace as the Pod and ensures that the PersistentVolumeClaim gets deleted when the Pod gets deleted. 
That triggers volume binding and/or provisioning, either immediately if the StorageClass uses immediate volume binding or when the Pod is tentatively scheduled onto a node ( WaitForFirstConsumervolume binding mode). The latter is recommended for generic ephemeral volumes because then the scheduler is free to choose a suitable node for the Pod. With immediate binding, the scheduler is forced to select a node that has access to the volume once it is available. 
In terms of resource ownership , a Pod that has generic ephemeral storage is the owner of the PersistentVolumeClaim(s) that provide that ephemeral storage. When the Pod is deleted, the Kubernetes garbage collector deletes the PVC, which then usually triggers deletion of the volume because the default reclaim policy of storage classes is to delete volumes. You can create quasi-ephemeral local storage using a StorageClass with a reclaim policy of retain: the storage outlives the Pod, and in this case you need to ensure that volume clean up happens separately. 
While these PVCs exist, they can be used like any other PVC. In particular, they can be referenced as data source in volume cloning or snapshotting. The PVC object also holds the current status of the volume. 
### PersistentVolumeClaim naming 
Naming of the automatically created PVCs is deterministic: the name is a combination of the Pod name and volume name, with a hyphen ( -) in the middle. In the example above, the PVC name will be my-app-scratch-volume. This deterministic naming makes it easier to interact with the PVC because one does not have to search for it once the Pod name and volume name are known. 
The deterministic naming also introduces a potential conflict between different Pods (a Pod "pod-a" with volume "scratch" and another Pod with name "pod" and volume "a-scratch" both end up with the same PVC name "pod-a-scratch") and between Pods and manually created PVCs. 
Such conflicts are detected: a PVC is only used for an ephemeral volume if it was created for the Pod. This check is based on the ownership relationship. An existing PVC is not overwritten or modified. But this does not resolve the conflict because without the right PVC, the Pod cannot start. 
#### Caution: Take care when naming Pods and volumes inside the same namespace, so that these conflicts can't occur. 
### Security 
Using generic ephemeral volumes allows users to create PVCs indirectly if they can create Pods, even if they do not have permission to create PVCs directly. Cluster administrators must be aware of this. If this does not fit their security model, they should use an admission webhook that rejects objects like Pods that have a generic ephemeral volume. 
The normal namespace quota for PVCs still applies, so even if users are allowed to use this new mechanism, they cannot use it to circumvent other policies. 
## What's next 
### Ephemeral volumes managed by kubelet 
See local ephemeral storage . 
### CSI ephemeral volumes 
- For more information on the design, see the Ephemeral Inline CSI volumes KEP . - For more information on further development of this feature, see the enhancement tracking issue #596 . 
### Generic ephemeral volumes 
- For more information on the design, see the Generic ephemeral inline volumes KEP . 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified October 05, 2025 at 9:09 PM PST: Move ephemeral storage contents out of container resource page (b94586af73) 
- - - - - - 

- - - - 

#### 📄 Sub-topic: [https://kubernetes.io/docs/concepts/storage/persistent-volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - Français (French)   - Bahasa Indonesia (Indonesian)   - 日本語 (Japanese)   - 한국어 (Korean)   - Português (Portuguese)   - Español (Spanish)   - Tiếng Việt (Vietnamese)   - বাংলা (Bengali)   - Deutsch (German)   - हिन्दी (Hindi)   - Italiano (Italian)   - فارسی (Persian)   - Polski (Polish)   - Русский (Russian)   - Українська (Ukrainian) - 
  - Light   - Dark   - Auto 
# Persistent Volumes 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- - 
  -   -   -   -   -   -   -   - - - 
  -   -   -   -   -   -   -   - - 
  -   -   -   -   -   -   - - 
  -   - - 
  -   -   -   - - 
  - - 
  - - - - 
  - 
- - - - 
# Persistent Volumes 
This document describes persistent volumes in Kubernetes. Familiarity with volumes , StorageClasses and VolumeAttributesClasses is suggested. 
## Introduction 
Managing storage is a distinct problem from managing compute instances. The PersistentVolume subsystem provides an API for users and administrators that abstracts details of how storage is provided from how it is consumed. To do this, we introduce two new API resources: PersistentVolume and PersistentVolumeClaim. 
A PersistentVolume (PV) is a piece of storage in the cluster that has been provisioned by an administrator or dynamically provisioned using Storage Classes . It is a resource in the cluster just like a node is a cluster resource. PVs are volume plugins like Volumes, but have a lifecycle independent of any individual Pod that uses the PV. This API object captures the details of the implementation of the storage, be that NFS, iSCSI, or a cloud-provider-specific storage system. 
A PersistentVolumeClaim (PVC) is a request for storage by a user. It is similar to a Pod. Pods consume node resources and PVCs consume PV resources. Pods can request specific levels of resources (CPU and Memory). Claims can request specific size and access modes (e.g., they can be mounted ReadWriteOnce, ReadOnlyMany, ReadWriteMany, or ReadWriteOncePod, see AccessModes ). 
While PersistentVolumeClaims allow a user to consume abstract storage resources, it is common that users need PersistentVolumes with varying properties, such as performance, for different problems. Cluster administrators need to be able to offer a variety of PersistentVolumes that differ in more ways than size and access modes, without exposing users to the details of how those volumes are implemented. For these needs, there is the StorageClass resource. 
See the detailed walkthrough with working examples . 
## Lifecycle of a volume and claim 
PVs are resources in the cluster. PVCs are requests for those resources and also act as claim checks to the resource. The interaction between PVs and PVCs follows this lifecycle: 
### Provisioning 
There are two ways PVs may be provisioned: statically or dynamically. 
#### Static 
A cluster administrator creates a number of PVs. They carry the details of the real storage, which is available for use by cluster users. They exist in the Kubernetes API and are available for consumption. 
#### Dynamic 
When none of the static PVs the administrator created match a user's PersistentVolumeClaim, the cluster may try to dynamically provision a volume specially for the PVC. This provisioning is based on StorageClasses: the PVC must request a storage class and the administrator must have created and configured that class for dynamic provisioning to occur. Claims that request the class ""effectively disable dynamic provisioning for themselves. 
To enable dynamic storage provisioning based on storage class, the cluster administrator needs to enable the DefaultStorageClassadmission controller on the API server. This can be done, for example, by ensuring that DefaultStorageClassis among the comma-delimited, ordered list of values for the --enable-admission-pluginsflag of the API server component. For more information on API server command-line flags, check kube-apiserver documentation. 
### Binding 
A user creates, or in the case of dynamic provisioning, has already created, a PersistentVolumeClaim with a specific amount of storage requested and with certain access modes. A control loop in the control plane watches for new PVCs, finds a matching PV (if possible), and binds them together. If a PV was dynamically provisioned for a new PVC, the loop will always bind that PV to the PVC. Otherwise, the user will always get at least what they asked for, but the volume may be in excess of what was requested. Once bound, PersistentVolumeClaim binds are exclusive, regardless of how they were bound. A PVC to PV binding is a one-to-one mapping, using a ClaimRef which is a bi-directional binding between the PersistentVolume and the PersistentVolumeClaim. 
Claims will remain unbound indefinitely if a matching volume does not exist. Claims will be bound as matching volumes become available. For example, a cluster provisioned with many 50Gi PVs would not match a PVC requesting 100Gi. The PVC can be bound when a 100Gi PV is added to the cluster. 
### Using 
Pods use claims as volumes. The cluster inspects the claim to find the bound volume and mounts that volume for a Pod. For volumes that support multiple access modes, the user specifies which mode is desired when using their claim as a volume in a Pod. 
Once a user has a claim and that claim is bound, the bound PV belongs to the user for as long as they need it. Users schedule Pods and access their claimed PVs by including a persistentVolumeClaimsection in a Pod's volumesblock. See Claims As Volumes for more details on this. 
### Storage Object in Use Protection 
The purpose of the Storage Object in Use Protection feature is to ensure that PersistentVolumeClaims (PVCs) in active use by a Pod and PersistentVolume (PVs) that are bound to PVCs are not removed from the system, as this may result in data loss. 
#### Note: PVC is in active use by a Pod when a Pod object exists that is using the PVC. 
If a user deletes a PVC in active use by a Pod, the PVC is not removed immediately. PVC removal is postponed until the PVC is no longer actively used by any Pods. Also, if an admin deletes a PV that is bound to a PVC, the PV is not removed immediately. PV removal is postponed until the PV is no longer bound to a PVC. 
You can see that a PVC is protected when the PVC's status is Terminatingand the Finalizerslist includes kubernetes.io/pvc-protection: 
```
kubectl describe pvc hostpath
Name:          hostpath
Namespace:     default
StorageClass:  example-hostpath
Status:        Terminating
Volume:
Labels:        <none>
Annotations:   volume.beta.kubernetes.io/storage-class=example-hostpath
               volume.beta.kubernetes.io/storage-provisioner=example.com/hostpath
Finalizers:    [kubernetes.io/pvc-protection]...

```

You can see that a PV is protected when the PV's status is Terminatingand the Finalizerslist includes kubernetes.io/pv-protectiontoo: 
```
kubectl describe pv task-pv-volume
Name:            task-pv-volume
Labels:          type=localAnnotations:     <none>
Finalizers:      [kubernetes.io/pv-protection]StorageClass:    standard
Status:          Terminating
Claim:
Reclaim Policy:  Delete
Access Modes:    RWO
Capacity:        1Gi
Message:
Source:
    Type:          HostPath (bare host directory volume)    Path:          /tmp/data
    HostPathType:
Events:            <none>

```

### Reclaiming 
When a user is done with their volume, they can delete the PVC objects from the API that allows reclamation of the resource. The reclaim policy for a PersistentVolume tells the cluster what to do with the volume after it has been released of its claim. Currently, volumes can either be Retained, Recycled, or Deleted. 
#### Retain 
The Retainreclaim policy allows for manual reclamation of the resource. When the PersistentVolumeClaim is deleted, the PersistentVolume still exists and the volume is considered "released". But it is not yet available for another claim because the previous claimant's data remains on the volume. An administrator can manually reclaim the volume with the following steps. 
- Delete the PersistentVolume. The associated storage asset in external infrastructure still exists after the PV is deleted. - Manually clean up the data on the associated storage asset accordingly. - Manually delete the associated storage asset. 
If you want to reuse the same storage asset, create a new PersistentVolume with the same storage asset definition. 
#### Delete 
For volume plugins that support the Deletereclaim policy, deletion removes both the PersistentVolume object from Kubernetes, as well as the associated storage asset in the external infrastructure. Volumes that were dynamically provisioned inherit the reclaim policy of their StorageClass , which defaults to Delete. The administrator should configure the StorageClass according to users' expectations; otherwise, the PV must be edited or patched after it is created. See Change the Reclaim Policy of a PersistentVolume . 
#### Recycle 
#### Warning: The Recyclereclaim policy is deprecated. Instead, the recommended approach is to use dynamic provisioning. 
If supported by the underlying volume plugin, the Recyclereclaim policy performs a basic scrub ( rm -rf /thevolume/*) on the volume and makes it available again for a new claim. 
However, an administrator can configure a custom recycler Pod template using the Kubernetes controller manager command line arguments as described in the reference . The custom recycler Pod template must contain a volumesspecification, as shown in the example below: 
```
apiVersion:v1kind:Podmetadata:name:pv-recyclernamespace:defaultspec:restartPolicy:Nevervolumes:- name:volhostPath:path:/any/path/it/will/be/replacedcontainers:- name:pv-recyclerimage:"registry.k8s.io/busybox"command:["/bin/sh","-c","test -e /scrub && rm -rf /scrub/..?* /scrub/.[!.]* /scrub/*  && test -z \"$(ls -A /scrub)\" || exit 1"]volumeMounts:- name:volmountPath:/scrub
```

However, the particular path specified in the custom recycler Pod template in the volumespart is replaced with the particular path of the volume that is being recycled. 
### PersistentVolume deletion protection finalizer 
This is a stable feature in Kubernetes, and has been since the 1.33 release. You can no longer toggle this feature (the associated feature gate has been removed). 
Finalizers can be added on a PersistentVolume to ensure that PersistentVolumes having Deletereclaim policy are deleted only after the backing storage are deleted. 
The finalizer external-provisioner.volume.kubernetes.io/finalizer(introduced in v1.31) is added to both dynamically provisioned and statically provisioned CSI volumes. 
The finalizer kubernetes.io/pv-controller(introduced in v1.31) is added to dynamically provisioned in-tree plugin volumes and skipped for statically provisioned in-tree plugin volumes. 
The following is an example of dynamically provisioned in-tree plugin volume: 
```
kubectl describe pv pvc-74a498d6-3929-47e8-8c02-078c1ece4d78
Name:            pvc-74a498d6-3929-47e8-8c02-078c1ece4d78
Labels:          <none>
Annotations:     kubernetes.io/createdby: vsphere-volume-dynamic-provisioner
                 pv.kubernetes.io/bound-by-controller: yes
                 pv.kubernetes.io/provisioned-by: kubernetes.io/vsphere-volume
Finalizers:      [kubernetes.io/pv-protection kubernetes.io/pv-controller]StorageClass:    vcp-sc
Status:          Bound
Claim:           default/vcp-pvc-1
Reclaim Policy:  Delete
Access Modes:    RWO
VolumeMode:      Filesystem
Capacity:        1Gi
Node Affinity:   <none>
Message:
Source:
    Type:               vSphereVolume (a Persistent Disk resource in vSphere)    VolumePath:         [vsanDatastore] d49c4a62-166f-ce12-c464-020077ba5d46/kubernetes-dynamic-pvc-74a498d6-3929-47e8-8c02-078c1ece4d78.vmdk
    FSType:             ext4
    StoragePolicyName:  vSAN Default Storage Policy
Events:                 <none>

```

The finalizer external-provisioner.volume.kubernetes.io/finalizeris added for CSI volumes. The following is an example: 
```
Name:            pvc-2f0bab97-85a8-4552-8044-eb8be45cf48d
Labels:          <none>
Annotations:     pv.kubernetes.io/provisioned-by: csi.vsphere.vmware.com
Finalizers:      [kubernetes.io/pv-protection external-provisioner.volume.kubernetes.io/finalizer]StorageClass:    fast
Status:          Bound
Claim:           demo-app/nginx-logs
Reclaim Policy:  Delete
Access Modes:    RWO
VolumeMode:      Filesystem
Capacity:        200Mi
Node Affinity:   <none>
Message:
Source:
    Type:              CSI (a Container Storage Interface (CSI) volume source)    Driver:            csi.vsphere.vmware.com
    FSType:            ext4
    VolumeHandle:      44830fa8-79b4-406b-8b58-621ba25353fd
    ReadOnly:          false    VolumeAttributes:      storage.kubernetes.io/csiProvisionerIdentity=1648442357185-8081-csi.vsphere.vmware.com
type=vSphere CNS Block Volume
Events:                <none>

```

When the CSIMigration{provider}feature flag is enabled for a specific in-tree volume plugin, the kubernetes.io/pv-controllerfinalizer is replaced by the external-provisioner.volume.kubernetes.io/finalizerfinalizer. 
The finalizers ensure that the PV object is removed only after the volume is deleted from the storage backend provided the reclaim policy of the PV is Delete. This also ensures that the volume is deleted from storage backend irrespective of the order of deletion of PV and PVC. 
### Reserving a PersistentVolume 
The control plane can bind PersistentVolumeClaims to matching PersistentVolumes in the cluster. However, if you want a PVC to bind to a specific PV, you need to pre-bind them. 
By specifying a PersistentVolume in a PersistentVolumeClaim, you declare a binding between that specific PV and PVC. If the PersistentVolume exists and has not reserved PersistentVolumeClaims through its claimReffield, then the PersistentVolume and PersistentVolumeClaim will be bound. 
The binding happens regardless of some volume matching criteria, including node affinity. The control plane still checks that storage class , access modes, and requested storage size are valid. 
```
apiVersion:v1kind:PersistentVolumeClaimmetadata:name:foo-pvcnamespace:foospec:storageClassName:""# Empty string must be explicitly set otherwise default StorageClass will be setvolumeName:foo-pv...
```

This method does not guarantee any binding privileges to the PersistentVolume. If other PersistentVolumeClaims could use the PV that you specify, you first need to reserve that storage volume. Specify the relevant PersistentVolumeClaim in the claimReffield of the PV so that other PVCs can not bind to it. 
```
apiVersion:v1kind:PersistentVolumemetadata:name:foo-pvspec:storageClassName:""claimRef:name:foo-pvcnamespace:foo...
```

This is useful if you want to consume PersistentVolumes that have their persistentVolumeReclaimPolicyset to Retain, including cases where you are reusing an existing PV. 
### Expanding Persistent Volumes Claims Feature state: Stable since Kubernetes v1.24 
Support for expanding PersistentVolumeClaims (PVCs) is enabled by default. You can expand the following types of volumes: 
- csi (including some CSI migrated volume types) - flexVolume (deprecated) - portworxVolume (deprecated) 
You can only expand a PVC if its storage class's allowVolumeExpansionfield is set to true. 
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:example-vol-defaultprovisioner:vendor-name.example/magicstorageparameters:resturl:"http://192.168.10.100:8080"restuser:""secretNamespace:""secretName:""allowVolumeExpansion:true
```

To request a larger volume for a PVC, edit the PVC object and specify a larger size. This triggers expansion of the volume that backs the underlying PersistentVolume. A new PersistentVolume is never created to satisfy the claim. Instead, an existing volume is resized. 
#### Warning: Directly editing the size of a PersistentVolume can prevent an automatic resize of that volume. If you edit the capacity of a PersistentVolume, and then edit the .specof a matching PersistentVolumeClaim to make the size of the PersistentVolumeClaim match the PersistentVolume, then no storage resize happens. The Kubernetes control plane will see that the desired state of both resources matches, conclude that the backing volume size has been manually increased and that no resize is necessary. 
#### CSI Volume expansion Feature state: Stable since Kubernetes v1.24 
Support for expanding CSI volumes is enabled by default but it also requires a specific CSI driver to support volume expansion. Refer to documentation of the specific CSI driver for more information. 
#### Resizing a volume containing a file system 
You can only resize volumes containing a file system if the file system is XFS, Ext3, or Ext4. 
When a volume contains a file system, the file system is only resized when a new Pod is using the PersistentVolumeClaim in ReadWritemode. File system expansion is either done when a Pod is starting up or when a Pod is running and the underlying file system supports online expansion. 
FlexVolumes (deprecated since Kubernetes v1.23) allow resize if the driver is configured with the RequiresFSResizecapability to true. The FlexVolume can be resized on Pod restart. 
#### Resizing an in-use PersistentVolumeClaim Feature state: Stable since Kubernetes v1.24 
In this case, you don't need to delete and recreate a Pod or deployment that is using an existing PVC. Any in-use PVC automatically becomes available to its Pod as soon as its file system has been expanded. This feature has no effect on PVCs that are not in use by a Pod or deployment. You must create a Pod that uses the PVC before the expansion can complete. 
Similar to other volume types - FlexVolume volumes can also be expanded when in-use by a Pod. 
#### Note: FlexVolume resize is possible only when the underlying driver supports resize. 
#### Recovering from Failure when Expanding Volumes 
If a user specifies a new size that is too big to be satisfied by underlying storage system, expansion of PVC will be continuously retried until user or cluster administrator takes some action. This can be undesirable and hence Kubernetes provides following methods of recovering from such failures. 
- Manually with Cluster Administrator access - By requesting expansion to smaller size 
If expanding underlying storage fails, the cluster administrator can manually recover the Persistent Volume Claim (PVC) state and cancel the resize requests. Otherwise, the resize requests are continuously retried by the controller without administrator intervention. 
- Mark the PersistentVolume(PV) that is bound to the PersistentVolumeClaim(PVC) with Retainreclaim policy. - Delete the PVC. Since PV has Retainreclaim policy - we will not lose any data when we recreate the PVC. - Delete the claimRefentry from PV specs, so as new PVC can bind to it. This should make the PV Available. - Re-create the PVC with smaller size than PV and set volumeNamefield of the PVC to the name of the PV. This should bind new PVC to existing PV. - Don't forget to restore the reclaim policy of the PV. 
If expansion has failed for a PVC, you can retry expansion with a smaller size than the previously requested value. To request a new expansion attempt with a smaller proposed size, edit .spec.resourcesfor that PVC and choose a value that is less than the value you previously tried. This is useful if expansion to a higher value did not succeed because of capacity constraint. If that has happened, or you suspect that it might have, you can retry expansion by specifying a size that is within the capacity limits of underlying storage provider. You can monitor status of resize operation by watching .status.allocatedResourceStatusesand events on the PVC. 
Note that, although you can specify a lower amount of storage than what was requested previously, the new value must still be higher than .status.capacity. Kubernetes does not support shrinking a PVC to less than its current size. 
## Types of Persistent Volumes 
PersistentVolume types are implemented as plugins. Kubernetes currently supports the following plugins: 
- csi- Container Storage Interface (CSI) - fc- Fibre Channel (FC) storage - hostPath- HostPath volume (for single node testing only; WILL NOT WORK in a multi-node cluster; consider using localvolume instead) - iscsi- iSCSI (SCSI over IP) storage - local- local storage devices mounted on nodes. - nfs- Network File System (NFS) storage 
The following types of PersistentVolume are deprecated but still available. If you are using these volume types except for flexVolume, cephfsand rbd, please install corresponding CSI drivers. 
- awsElasticBlockStore- AWS Elastic Block Store (EBS) ( migration on by default starting v1.23) - azureDisk- Azure Disk ( migration on by default starting v1.23) - azureFile- Azure File ( migration on by default starting v1.24) - cinder- Cinder (OpenStack block storage) ( migration on by default starting v1.21) - flexVolume- FlexVolume ( deprecated starting v1.23, no migration plan and no plan to remove support) - gcePersistentDisk- GCE Persistent Disk ( migration on by default starting v1.23) - portworxVolume- Portworx volume ( migration on by default starting v1.31) - vsphereVolume- vSphere VMDK volume ( migration on by default starting v1.25) 
Older versions of Kubernetes also supported the following in-tree PersistentVolume types: 
- cephfs( not available starting v1.31) - flocker- Flocker storage. ( not available starting v1.25) - glusterfs- GlusterFS storage. ( not available starting v1.26) - photonPersistentDisk- Photon controller persistent disk. ( not available starting v1.15) - quobyte- Quobyte volume. ( not available starting v1.25) - rbd- Rados Block Device (RBD) volume ( not available starting v1.31) - scaleIO- ScaleIO volume. ( not available starting v1.21) - storageos- StorageOS volume. ( not available starting v1.25) 
## Persistent Volumes 
Each PV contains a spec and status, which is the specification and status of the volume. The name of a PersistentVolume object must be a valid DNS subdomain name . 
```
apiVersion:v1kind:PersistentVolumemetadata:name:pv0003spec:capacity:storage:5GivolumeMode:FilesystemaccessModes:- ReadWriteOncepersistentVolumeReclaimPolicy:RecyclestorageClassName:slowmountOptions:- hard- nfsvers=4.1nfs:path:/tmpserver:172.17.0.2
```

#### Note: Helper programs relating to the volume type may be required for consumption of a PersistentVolume within a cluster. In this example, the PersistentVolume is of type NFS and the helper program /sbin/mount.nfs is required to support the mounting of NFS filesystems. 
### Capacity 
Generally, a PV will have a specific storage capacity. This is set using the PV's capacityattribute which is a Quantity value. 
Currently, storage size is the only resource that can be set or requested. Future attributes may include IOPS, throughput, etc. 
### Volume Mode Feature state: Stable since Kubernetes v1.18 
Kubernetes supports two volumeModesof PersistentVolumes: Filesystemand Block. 
volumeModeis an optional API parameter. Filesystemis the default mode used when volumeModeparameter is omitted. 
A volume with volumeMode: Filesystemis mounted into Pods into a directory. If the volume is backed by a block device and the device is empty, Kubernetes creates a filesystem on the device before mounting it for the first time. 
You can set the value of volumeModeto Blockto use a volume as a raw block device. Such volume is presented into a Pod as a block device, without any filesystem on it. This mode is useful to provide a Pod the fastest possible way to access a volume, without any filesystem layer between the Pod and the volume. On the other hand, the application running in the Pod must know how to handle a raw block device. See Raw Block Volume Support for an example on how to use a volume with volumeMode: Blockin a Pod. 
### Access Modes 
A PersistentVolume can be mounted on a host in any way supported by the resource provider. As shown in the table below, providers will have different capabilities and each PV's access modes are set to the specific modes supported by that particular volume. For example, NFS can support multiple read/write clients, but a specific NFS PV might be exported on the server as read-only. Each PV gets its own set of access modes describing that specific PV's capabilities. 
The access modes are: ReadWriteOncethe volume can be mounted as read-write by a single node. ReadWriteOnce access mode still can allow multiple pods to access (read from or write to) that volume when the pods are running on the same node. For single pod access, please see ReadWriteOncePod. ReadOnlyManythe volume can be mounted as read-only by many nodes. ReadWriteManythe volume can be mounted as read-write by many nodes. ReadWriteOncePodFeature state: Stable since Kubernetes v1.29 the volume can be mounted as read-write by a single Pod. Use ReadWriteOncePod access mode if you want to ensure that only one pod across the whole cluster can read that PVC or write to it. 
#### Note: 
The ReadWriteOncePodaccess mode is only supported for CSI volumes and Kubernetes version 1.22+. To use this feature you will need to update the following CSI sidecars to these versions or greater: 
- csi-provisioner:v3.0.0+ - csi-attacher:v3.3.0+ - csi-resizer:v1.3.0+ 
In the CLI, the access modes are abbreviated to: 
- RWO - ReadWriteOnce - ROX - ReadOnlyMany - RWX - ReadWriteMany - RWOP - ReadWriteOncePod 
#### Note: Kubernetes uses volume access modes to match PersistentVolumeClaims and PersistentVolumes. In some cases, the volume access modes also constrain where the PersistentVolume can be mounted. Volume access modes do not enforce write protection once the storage has been mounted. Even if the access modes are specified as ReadWriteOnce, ReadOnlyMany, or ReadWriteMany, they don't set any constraints on the volume. For example, even if a PersistentVolume is created as ReadOnlyMany, it is no guarantee that it will be read-only. If the access modes are specified as ReadWriteOncePod, the volume is constrained and can be mounted on only a single Pod. 
Important! A volume can only be mounted using one access mode at a time, even if it supports many. 
|  Volume Plugin  | ReadWriteOnce  | ReadOnlyMany  | ReadWriteMany  | ReadWriteOncePod  |
|  AzureFile  | ✓  | ✓  | ✓  | -  |
|  CephFS  | ✓  | ✓  | ✓  | -  |
|  CSI  | depends on the driver  | depends on the driver  | depends on the driver  | depends on the driver  |
|  FC  | ✓  | ✓  | -  | -  |
|  FlexVolume  | ✓  | ✓  | depends on the driver  | -  |
|  HostPath  | ✓  | -  | -  | -  |
|  iSCSI  | ✓  | ✓  | -  | -  |
|  NFS  | ✓  | ✓  | ✓  | -  |
|  RBD  | ✓  | ✓  | -  | -  |
|  VsphereVolume  | ✓  | -  | - (works when Pods are collocated)  | -  |
|  PortworxVolume  | ✓  | -  | ✓  | -  |
### Class 
A PV can have a class, which is specified by setting the storageClassNameattribute to the name of a StorageClass . A PV of a particular class can only be bound to PVCs requesting that class. A PV with no storageClassNamehas no class and can only be bound to PVCs that request no particular class. 
In the past, the annotation volume.beta.kubernetes.io/storage-classwas used instead of the storageClassNameattribute. This annotation is still working; however, it will become fully deprecated in a future Kubernetes release. 
### Reclaim Policy 
Current reclaim policies are: 
- Retain -- manual reclamation - Recycle -- basic scrub ( rm -rf /thevolume/*) - Delete -- delete the volume 
For Kubernetes 1.37, only nfsand hostPathvolume types support recycling. 
### Mount Options 
A Kubernetes administrator can specify additional mount options for when a Persistent Volume is mounted on a node. 
#### Note: Not all Persistent Volume types support mount options. 
The following volume types support mount options: 
- csi(including CSI migrated volume types) - iscsi- nfs
Mount options are not validated. If a mount option is invalid, the mount fails. 
In the past, the annotation volume.beta.kubernetes.io/mount-optionswas used instead of the mountOptionsattribute. This annotation is still working; however, it will become fully deprecated in a future Kubernetes release. 
### Node Affinity 
#### Note: For most volume types, you do not need to set this field. You need to explicitly set this for local volumes. 
A PV can specify node affinity to define constraints that limit what nodes this volume can be accessed from. Pods that use a PV will only be scheduled to nodes that are selected by the node affinity. To specify node affinity, set nodeAffinityin the .specof a PV. The PersistentVolume API reference has more details on this field. 
#### Updates to node affinity Feature state: Alpha since Kubernetes v1.35; disabled by default More information about this feature 
To use this feature, you (or a cluster administrator) will need to enable the MutablePVNodeAffinity feature gate for all relevant components in your cluster. 
See Enable Or Disable Feature Gates for more information. 
If the MutablePVNodeAffinityfeature gate is enabled in your cluster, the .spec.nodeAffinityfield of a PersistentVolume is mutable. This allows cluster administrators or external storage controller to update the node affinity of a PersistentVolume when the data is migrated, without interrupting the running pods. 
When updating the node affinity, you should ensure that the new node affinity still matches the nodes where the volume is currently in use. For the pods violating the new affinity, if the pod is already running, it may continue to run. But Kubernetes does not support this configuration. You should terminate the violating pods soon. Due to in memory caching, the pods created after the update may still be scheduled according to the old node affinity for a short period of time. 
To use this feature, you should enable the MutablePVNodeAffinityfeature gate on the following components: 
- kube-apiserver- kubelet
### Phase 
A PersistentVolume will be in one of the following phases: Availablea free resource that is not yet bound to a claim Boundthe volume is bound to a claim Releasedthe claim has been deleted, but the associated storage resource is not yet reclaimed by the cluster Failedthe volume has failed its (automated) reclamation 
You can see the name of the PVC bound to the PV using kubectl describe persistentvolume <name>. 
#### Phase transition timestamp 
This is a stable feature in Kubernetes, and has been since the 1.31 release. You can no longer toggle this feature (the associated feature gate has been removed). 
The .statusfield for a PersistentVolume can include an alpha lastPhaseTransitionTimefield. This field records the timestamp of when the volume last transitioned its phase. For newly created volumes the phase is set to Pendingand lastPhaseTransitionTimeis set to the current time. 
## PersistentVolumeClaims 
Each PVC contains a spec and status, which is the specification and status of the claim. The name of a PersistentVolumeClaim object must be a valid DNS subdomain name . 
```
apiVersion:v1kind:PersistentVolumeClaimmetadata:name:myclaimspec:accessModes:- ReadWriteOncevolumeMode:Filesystemresources:requests:storage:8GistorageClassName:slowselector:matchLabels:release:"stable"matchExpressions:- {key: environment, operator: In, values:[dev]}
```

### Access Modes 
Claims use the same conventions as volumes when requesting storage with specific access modes. 
### Volume Modes 
Claims use the same convention as volumes to indicate the consumption of the volume as either a filesystem or block device. 
### Volume Name 
Claims can use the volumeNamefield to explicitly bind to a specific PersistentVolume. You can also leave volumeNameunset, indicating that you'd like Kubernetes to set up a new PersistentVolume that matches the claim. If the specified PV is already bound to another PVC, the binding will be stuck in a pending state. 
### Resources 
Claims, like Pods, can request specific quantities of a resource. In this case, the request is for storage. The same resource model applies to both volumes and claims. 
#### Note: For Filesystemvolumes, the storage request refers to the "outer" volume size (i.e. the allocated size from the storage backend). This means that the writeable size may be slightly lower for providers that build a filesystem on top of a block device, due to filesystem overhead. This is especially visible with XFS, where many metadata features are enabled by default. 
### Selector 
Claims can specify a label selector to further filter the set of volumes. Only the volumes whose labels match the selector can be bound to the claim. The selector can consist of two fields: 
- matchLabels- the volume must have a label with this value - matchExpressions- a list of requirements made by specifying key, list of values, and operator that relates the key and values. Valid operators include In, NotIn, Exists, and DoesNotExist. 
All of the requirements, from both matchLabelsand matchExpressions, are ANDed together – they must all be satisfied in order to match. 
### Class 
A claim can request a particular class by specifying the name of a StorageClass using the attribute storageClassName. Only PVs of the requested class, ones with the same storageClassNameas the PVC, can be bound to the PVC. 
PVCs don't necessarily have to request a class. A PVC with its storageClassNameset equal to ""is always interpreted to be requesting a PV with no class, so it can only be bound to PVs with no class (no annotation or one set equal to ""). A PVC with no storageClassNameis not quite the same and is treated differently by the cluster, depending on whether the DefaultStorageClassadmission plugin is turned on. 
- If the admission plugin is turned on, the administrator may specify a default StorageClass. All PVCs that have no storageClassNamecan be bound only to PVs of that default. Specifying a default StorageClass is done by setting the annotation storageclass.kubernetes.io/is-default-classequal to truein a StorageClass object. If the administrator does not specify a default, the cluster responds to PVC creation as if the admission plugin were turned off. If more than one default StorageClass is specified, the newest default is used when the PVC is dynamically provisioned. - If the admission plugin is turned off, there is no notion of a default StorageClass. All PVCs that have storageClassNameset to ""can be bound only to PVs that have storageClassNamealso set to "". However, PVCs with missing storageClassNamecan be updated later once default StorageClass becomes available. If the PVC gets updated it will no longer bind to PVs that have storageClassNamealso set to "". 
See retroactive default StorageClass assignment for more details. 
Depending on installation method, a default StorageClass may be deployed to a Kubernetes cluster by addon manager during installation. 
When a PVC specifies a selectorin addition to requesting a StorageClass, the requirements are ANDed together: only a PV of the requested class and with the requested labels may be bound to the PVC. 
#### Note: Currently, a PVC with a non-empty selectorcan't have a PV dynamically provisioned for it. 
In the past, the annotation volume.beta.kubernetes.io/storage-classwas used instead of storageClassNameattribute. This annotation is still working; however, it won't be supported in a future Kubernetes release. 
#### Retroactive default StorageClass assignment Feature state: Stable since Kubernetes v1.28 
You can create a PersistentVolumeClaim without specifying a storageClassNamefor the new PVC, and you can do so even when no default StorageClass exists in your cluster. In this case, the new PVC creates as you defined it, and the storageClassNameof that PVC remains unset until default becomes available. 
When a default StorageClass becomes available, the control plane identifies any existing PVCs without storageClassName. For the PVCs that either have an empty value for storageClassNameor do not have this key, the control plane then updates those PVCs to set storageClassNameto match the new default StorageClass. If you have an existing PVC where the storageClassNameis "", and you configure a default StorageClass, then this PVC will not get updated. 
In order to keep binding to PVs with storageClassNameset to ""(while a default StorageClass is present), you need to set the storageClassNameof the associated PVC to "". 
This behavior helps administrators change default StorageClass by removing the old one first and then creating or setting another one. This brief window while there is no default causes PVCs without storageClassNamecreated at that time to not have any default, but due to the retroactive default StorageClass assignment this way of changing defaults is safe. 
### Unused PVC tracking Feature state: Beta since Kubernetes v1.37; enabled by default 
When enabled, the PVC protection controller adds an Unusedcondition to each PersistentVolumeClaim to indicate whether it is currently referenced by any non-terminal Pod. 
The condition has two states: Unusedwith status "True"(reason NoPodsUsingPVC) No non-terminal Pod references this PVC. The lastTransitionTimerecords when the PVC became unused. Unusedwith status "False"(reason PodUsingPVC) At least one non-terminal Pod currently references this PVC. The lastTransitionTimerecords when the PVC started being used. 
A Pod is considered non-terminal if its phase is not Succeededor Failed. This means that a Pending Pod (even one that has not yet been scheduled) counts as using the PVC. 
The lastTransitionTimeof the Unusedcondition can be used by cluster administrators, monitoring tools, and external controllers to identify PVCs that have been unused for a long time. For example, to find all PVCs that have been unused for more than 30 days, you could query for PVCs where the Unusedcondition has status: "True"and lastTransitionTimeis older than 30 days. 
#### Note: The unused duration indicated by this condition may be shorter than the actual unused time because of processing delays in the controller or because the feature was enabled after the PVC was already unused. The condition is not updated when a PVC has deletionTimestampset (that is, PVCs that are being deleted). 
## Claims As Volumes 
Pods access storage by using the claim as a volume. Claims must exist in the same namespace as the Pod using the claim. The cluster finds the claim in the Pod's namespace and uses it to get the PersistentVolume backing the claim. The volume is then mounted to the host and into the Pod. 
```
apiVersion:v1kind:Podmetadata:name:mypodspec:containers:- name:myfrontendimage:nginxvolumeMounts:- mountPath:"/var/www/html"name:mypdvolumes:- name:mypdpersistentVolumeClaim:claimName:myclaim
```

### A Note on Namespaces 
PersistentVolumes binds are exclusive, and since PersistentVolumeClaims are namespaced objects, mounting claims with "Many" modes ( ROX, RWX) is only possible within one namespace. 
### PersistentVolumes typed hostPath
A hostPathPersistentVolume uses a file or directory on the Node to emulate network-attached storage. See an example of hostPathtyped volume . 
## Raw Block Volume Support Feature state: Stable since Kubernetes v1.18 
The following volume plugins support raw block volumes, including dynamic provisioning where applicable: 
- CSI (including some CSI migrated volume types) - FC (Fibre Channel) - iSCSI - Local volume 
### PersistentVolume using a Raw Block Volume 
```
apiVersion:v1kind:PersistentVolumemetadata:name:block-pvspec:capacity:storage:10GiaccessModes:- ReadWriteOncevolumeMode:BlockpersistentVolumeReclaimPolicy:Retainfc:targetWWNs:["50060e801049cfd1"]lun:0readOnly:false
```

### PersistentVolumeClaim requesting a Raw Block Volume 
```
apiVersion:v1kind:PersistentVolumeClaimmetadata:name:block-pvcspec:accessModes:- ReadWriteOncevolumeMode:Blockresources:requests:storage:10Gi
```

### Pod specification adding Raw Block Device path in container 
```
apiVersion:v1kind:Podmetadata:name:pod-with-block-volumespec:containers:- name:fc-containerimage:fedora:26command:["/bin/sh","-c"]args:["tail -f /dev/null"]volumeDevices:- name:datadevicePath:/dev/xvdavolumes:- name:datapersistentVolumeClaim:claimName:block-pvc
```

#### Note: When adding a raw block device for a Pod, you specify the device path in the container instead of a mount path. 
### Binding Block Volumes 
If a user requests a raw block volume by indicating this using the volumeModefield in the PersistentVolumeClaim spec, the binding rules differ slightly from previous releases that didn't consider this mode as part of the spec. Listed is a table of possible combinations the user and admin might specify for requesting a raw block device. The table indicates if the volume will be bound or not given the combinations: Volume binding matrix for statically provisioned volumes: 
|  PV volumeMode  | PVC volumeMode  | Result  |
|  unspecified  | unspecified  | BIND  |
|  unspecified  | Block  | NO BIND  |
|  unspecified  | Filesystem  | BIND  |
|  Block  | unspecified  | NO BIND  |
|  Block  | Block  | BIND  |
|  Block  | Filesystem  | NO BIND  |
|  Filesystem  | Filesystem  | BIND  |
|  Filesystem  | Block  | NO BIND  |
|  Filesystem  | unspecified  | BIND  |
#### Note: Only statically provisioned volumes are supported for alpha release. Administrators should take care to consider these values when working with raw block devices. 
## Volume Snapshot and Restore Volume from Snapshot Support Feature state: Stable since Kubernetes v1.20 
Volume snapshots only support the out-of-tree CSI volume plugins. For details, see Volume Snapshots . In-tree volume plugins are deprecated. You can read about the deprecated volume plugins in the Volume Plugin FAQ . 
### Create a PersistentVolumeClaim from a Volume Snapshot 
```
apiVersion:v1kind:PersistentVolumeClaimmetadata:name:restore-pvcspec:storageClassName:csi-hostpath-scdataSource:name:new-snapshot-testkind:VolumeSnapshotapiGroup:snapshot.storage.k8s.ioaccessModes:- ReadWriteOnceresources:requests:storage:10Gi
```

## Volume Cloning 
Volume Cloning only available for CSI volume plugins. 
### Create PersistentVolumeClaim from an existing PVC 
```
apiVersion:v1kind:PersistentVolumeClaimmetadata:name:cloned-pvcspec:storageClassName:my-csi-plugindataSource:name:existing-src-pvc-namekind:PersistentVolumeClaimaccessModes:- ReadWriteOnceresources:requests:storage:10Gi
```

## Volume populators and data sources 
Volume cloning and snapshot restore pre-populate a new volume from a built-in data source . Volume populators extend this mechanism so that a PersistentVolumeClaim can be pre-populated from other kinds of source (a custom resource), referenced through its dataSourceReffield: 
```
apiVersion:v1kind:PersistentVolumeClaimmetadata:name:populated-pvcspec:dataSourceRef:name:example-namekind:ExampleDataSourceapiGroup:example.storage.k8s.ioaccessModes:- ReadWriteOnceresources:requests:storage:10Gi
```

For details, including cross-namespace data sources, see Volume Populators and Data Sources . 
## Writing Portable Configuration 
If you're writing configuration templates or examples that run on a wide range of clusters and need persistent storage, it is recommended that you use the following pattern: 
- Include PersistentVolumeClaim objects in your bundle of config (alongside Deployments, ConfigMaps, etc). - Do not include PersistentVolume objects in the config, since the user instantiating the config may not have permission to create PersistentVolumes. - Give the user the option of providing a storage class name when instantiating the template. 
  - If the user provides a storage class name, put that value into the persistentVolumeClaim.storageClassNamefield. This will cause the PVC to match the right storage class if the cluster has StorageClasses enabled by the admin.   - If the user does not provide a storage class name, leave the persistentVolumeClaim.storageClassNamefield as nil. This will cause a PV to be automatically provisioned for the user with the default StorageClass in the cluster. Many cluster environments have a default StorageClass installed, or administrators can create their own default StorageClass. - In your tooling, watch for PVCs that are not getting bound after some time and surface this to the user, as this may indicate that the cluster has no dynamic storage support (in which case the user should create a matching PV) or the cluster has no storage system (in which case the user cannot deploy config requiring PVCs). 
## What's next 
- Learn more about Creating a PersistentVolume . - Learn more about Creating a PersistentVolumeClaim . - Read the Persistent Storage design document . 
### API references 
Read about the APIs described in this page: 
- PersistentVolume- PersistentVolumeClaim
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified June 17, 2026 at 12:08 AM PST: add volume populators page (71016f5329) 
- - - - - - 

- - - - 

#### 📄 Sub-topic: [https://kubernetes.io/docs/concepts/storage/projected-volumes](https://kubernetes.io/docs/concepts/storage/projected-volumes)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - 日本語 (Japanese)   - 한국어 (Korean)   - Español (Spanish)   - বাংলা (Bengali)   - Français (French)   - Deutsch (German)   - हिन्दी (Hindi)   - Bahasa Indonesia (Indonesian)   - Italiano (Italian)   - فارسی (Persian)   - Polski (Polish)   - Português (Portuguese)   - Русский (Russian)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# Projected Volumes 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- 
  -   - - - - - 
  -   - 
- - - - 
# Projected Volumes 
This document describes projected volumes in Kubernetes. Familiarity with volumes is suggested. 
## Introduction 
A projectedvolume maps several existing volume sources into the same directory. 
Currently, the following types of volume sources can be projected: 
- secret- downwardAPI- configMap- serviceAccountToken- clusterTrustBundle- podCertificate
All sources are required to be in the same namespace as the Pod. For more details, see the all-in-one volume design document. 
### Example configuration with a secret, a downwardAPI, and a configMap pods/storage/projected-secret-downwardapi-configmap.yaml
```
apiVersion:v1kind:Podmetadata:name:volume-testspec:containers:- name:container-testimage:busybox:1.28command:["sleep","3600"]volumeMounts:- name:all-in-onemountPath:"/projected-volume"readOnly:truevolumes:- name:all-in-oneprojected:sources:- secret:name:mysecretitems:- key:usernamepath:my-group/my-username- downwardAPI:items:- path:"labels"fieldRef:fieldPath:metadata.labels- path:"cpu_limit"resourceFieldRef:containerName:container-testresource:limits.cpu- configMap:name:myconfigmapitems:- key:configpath:my-group/my-config
```

### Example configuration: secrets with a non-default permission mode set pods/storage/projected-secrets-nondefault-permission-mode.yaml
```
apiVersion:v1kind:Podmetadata:name:volume-testspec:containers:- name:container-testimage:busybox:1.28command:["sleep","3600"]volumeMounts:- name:all-in-onemountPath:"/projected-volume"readOnly:truevolumes:- name:all-in-oneprojected:sources:- secret:name:mysecretitems:- key:usernamepath:my-group/my-username- secret:name:mysecret2items:- key:passwordpath:my-group/my-passwordmode:0777
```

Each projected volume source is listed in the spec under sources. The parameters are nearly the same with two exceptions: 
- For secrets, the secretNamefield has been changed to nameto be consistent with ConfigMap naming. - The defaultModecan only be specified at the projected level and not for each volume source. However, as illustrated above, you can explicitly set the modefor each individual projection. 
## serviceAccountToken projected volumes 
You can inject the token for the current service account into a Pod at a specified path. For example: pods/storage/projected-service-account-token.yaml
```
apiVersion:v1kind:Podmetadata:name:sa-token-testspec:containers:- name:container-testimage:busybox:1.28command:["sleep","3600"]volumeMounts:- name:token-volmountPath:"/service-account"readOnly:trueserviceAccountName:defaultvolumes:- name:token-volprojected:sources:- serviceAccountToken:audience:apiexpirationSeconds:3600path:token
```

The example Pod has a projected volume containing the injected service account token. Containers in this Pod can use that token to access the Kubernetes API server, authenticating with the identity of the pod's ServiceAccount . The audiencefield contains the intended audience of the token. A recipient of the token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. This field is optional and it defaults to the identifier of the API server. 
The expirationSecondsis the expected duration of validity of the service account token. It defaults to 1 hour and must be at least 10 minutes (600 seconds). An administrator can also limit its maximum value by specifying the --service-account-max-token-expirationoption for the API server. The pathfield specifies a relative path to the mount point of the projected volume. 
#### Note: A container using a projected volume source as a subPathvolume mount will not receive updates for those volume sources. 
## clusterTrustBundle projected volumes Feature state: Stable since Kubernetes v1.37; enabled by default More information about this feature 
This is a stable feature in , and has been since version 1.37. It was first available in the v1.29 release. 
The clusterTrustBundleprojected volume source injects the contents of one or more ClusterTrustBundle objects as an automatically-updating file in the container filesystem. 
ClusterTrustBundles can be selected either by name or by signer name . 
To select by name, use the namefield to designate a single ClusterTrustBundle object. 
To select by signer name, use the signerNamefield (and optionally the labelSelectorfield) to designate a set of ClusterTrustBundle objects that use the given signer name. If labelSelectoris not present, then all ClusterTrustBundles for that signer are selected. 
The kubelet deduplicates the certificates in the selected ClusterTrustBundle objects, normalizes the PEM representations (discarding comments and headers), reorders the certificates, and writes them into the file named by path. As the set of selected ClusterTrustBundles or their content changes, kubelet keeps the file up-to-date. 
By default, the kubelet will prevent the pod from starting if the named ClusterTrustBundle is not found, or if signerName/ labelSelectordo not match any ClusterTrustBundles. If this behavior is not what you want, then set the optionalfield to true, and the pod will start up with an empty file at path. pods/storage/projected-clustertrustbundle.yaml
```
apiVersion:v1kind:Podmetadata:name:sa-ctb-name-testspec:containers:- name:container-testimage:busyboxcommand:["sleep","3600"]volumeMounts:- name:token-volmountPath:"/root-certificates"readOnly:trueserviceAccountName:defaultvolumes:- name:token-volprojected:sources:- clusterTrustBundle:name:examplepath:example-roots.pem- clusterTrustBundle:signerName:"example.com/mysigner"labelSelector:matchLabels:version:livepath:mysigner-roots.pemoptional:true
```

## podCertificate projected volumes Feature state: Stable since Kubernetes v1.37; enabled by default More information about this feature 
This is a stable feature in , and has been since version 1.37. It was first available in the v1.34 release. 
The podCertificateprojected volumes source securely provisions a private key and X.509 certificate chain for pod to use as client or server credentials. Kubelet will then handle refreshing the private key and certificate chain when they get close to expiration. The application just has to make sure that it reloads the file promptly when it changes, with a mechanism like inotifyor polling. 
Each podCertificateprojection supports the following configuration fields: 
- signerName: The signer you want to issue the certificate. Note that signers may have their own access requirements, and may refuse to issue certificates to your pod. - keyType: The type of private key that should be generated. Valid values are ED25519, ECDSAP256, ECDSAP384, ECDSAP521, RSA3072, and RSA4096. - maxExpirationSeconds: The maximum lifetime you will accept for the certificate issued to the pod. If not set, will be defaulted to 86400(24 hours). Must be at least 3600(1 hour), and at most 7862400(91 days). Kubernetes built-in signers are restricted to a max lifetime of 86400(1 day). The signer is allowed to issue a certificate with a lifetime shorter than what you've specified. - credentialBundlePath: Relative path within the projection where the credential bundle should be written. The credential bundle is a PEM-formatted file, where the first block is a "PRIVATE KEY" block that contains a PKCS#8-serialized private key, and the remaining blocks are "CERTIFICATE" blocks that comprise the certificate chain (leaf certificate and any intermediates). - keyPathand certificateChainPath: Separate paths where Kubelet should write just the private key or certificate chain. - userAnnotations: a map that allows you to pass additional information to the signer implementation. It is copied verbatim into the spec.unverifiedUserAnnotationsfield of the PodCertificateRequest objects that Kubelet creates. Entries are subject to the same validation as object metadata annotations, with the addition that all keys must be domain-prefixed. No restrictions are placed on values, except an overall size limitation on the entire field. Other than these basic validations, the API server does not conduct any extra validations. The signer implementations should be very careful when consuming this data. Signers must not inherently trust this data without first performing the appropriate verification steps. Signers should document the keys and values they support. Signers should deny requests that contain keys they do not recognize. 
#### Note: Most applications should prefer using credentialBundlePathunless they need the key and certificates in separate files for compatibility reasons. Kubelet uses an atomic writing strategy based on symlinks to make sure that when you open the files it projects, you read either the old content or the new content. However, if you read the key and certificate chain from separate files, Kubelet may rotate the credentials after your first read and before your second read, resulting in your application loading a mismatched key and certificate. pods/storage/projected-podcertificate.yaml
```
# Sample Pod spec that uses a podCertificate projection to request an ED25519# private key, a certificate from the `coolcert.example.com/foo` signer, and# write the results to `/var/run/my-x509-credentials/credentialbundle.pem`.apiVersion:v1kind:Podmetadata:namespace:defaultname:podcertificate-podspec:serviceAccountName:defaultcontainers:- image:debianname:maincommand:["sleep","infinity"]volumeMounts:- name:my-x509-credentialsmountPath:/var/run/my-x509-credentialsvolumes:- name:my-x509-credentialsprojected:defaultMode:0644sources:- podCertificate:keyType:ED25519signerName:coolcert.example.com/foocredentialBundlePath:credentialbundle.pemuserAnnotations:example.com/annotation1:"value1"example.com/annotation2:"value2"
```

## SecurityContext interactions 
The proposal for file permission handling in projected service account volume enhancement introduced the projected files having the correct owner permissions set. 
### Linux 
In Linux pods that have a projected volume and RunAsUserset in the Pod SecurityContext, the projected files have the correct ownership set including container user ownership. 
When all containers in a pod have the same runAsUserset in their PodSecurityContextor container SecurityContext, then the kubelet ensures that the contents of the serviceAccountTokenvolume are owned by that user, and the token file has its permission mode set to 0600. 
#### Note: 
Ephemeral containers added to a Pod after it is created do not change volume permissions that were set when the pod was created. 
If a Pod's serviceAccountTokenvolume permissions were set to 0600because all other containers in the Pod have the same runAsUser, ephemeral containers must use the same runAsUserto be able to read the token. 
### Windows 
In Windows pods that have a projected volume and RunAsUsernameset in the Pod SecurityContext, the ownership is not enforced due to the way user accounts are managed in Windows. Windows stores and manages local user and group accounts in a database file called Security Account Manager (SAM). Each container maintains its own instance of the SAM database, to which the host has no visibility into while the container is running. Windows containers are designed to run the user mode portion of the OS in isolation from the host, hence the maintenance of a virtual SAM database. As a result, the kubelet running on the host does not have the ability to dynamically configure host file ownership for virtualized container accounts. It is recommended that if files on the host machine are to be shared with the container then they should be placed into their own volume mount outside of C:\. 
By default, the projected files will have the following ownership as shown for an example projected volume file: 
```
PS C:\>Get-AclC:\var\run\secrets\kubernetes.io\serviceaccount\..2021_08_31_22_22_18.318230061\ca.crt|Format-ListPath:Microsoft.PowerShell.Core\FileSystem::C:\var\run\secrets\kubernetes.io\serviceaccount\..2021_08_31_22_22_18.318230061\ca.crtOwner:BUILTIN\AdministratorsGroup :NTAUTHORITY\SYSTEMAccess:NTAUTHORITY\SYSTEMAllowFullControlBUILTIN\AdministratorsAllowFullControlBUILTIN\UsersAllowReadAndExecute,SynchronizeAudit:Sddl:O:BAG:SYD:AI(A;ID;FA;;;SY)(A;ID;FA;;;BA)(A;ID;0x1200a9;;;BU)
```

This implies all administrator users like ContainerAdministratorwill have read, write and execute access while, non-administrator users will have read and execute access. 
#### Note: 
In general, granting the container access to the host is discouraged as it can open the door for potential security exploits. 
Creating a Windows Pod with RunAsUserin it's SecurityContextwill result in the Pod being stuck at ContainerCreatingforever. So it is advised to not use the Linux only RunAsUseroption with Windows Pods. 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified July 28, 2026 at 4:54 AM PST: Update docs and feature gates for Pod Certificates and ClusterTrustBundles GA (v1) in 1.37 (da72567af4) 
- - - - - - 

- - - - 

#### 📄 Sub-topic: [https://kubernetes.io/docs/concepts/storage/storage-capacity](https://kubernetes.io/docs/concepts/storage/storage-capacity)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - 日本語 (Japanese)   - 한국어 (Korean)   - Español (Spanish)   - বাংলা (Bengali)   - Français (French)   - Deutsch (German)   - हिन्दी (Hindi)   - Bahasa Indonesia (Indonesian)   - Italiano (Italian)   - فارسی (Persian)   - Polski (Polish)   - Português (Portuguese)   - Русский (Russian)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# Storage Capacity 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- - - - - - 
- - - - 
# Storage Capacity 
Storage capacity is limited and may vary depending on the node on which a pod runs: network-attached storage might not be accessible by all nodes, or storage is local to a node to begin with. Feature state: Stable since Kubernetes v1.24 
This page describes how Kubernetes keeps track of storage capacity and how the scheduler uses that information to schedule Pods onto nodes that have access to enough storage capacity for the remaining missing volumes. Without storage capacity tracking, the scheduler may choose a node that doesn't have enough capacity to provision a volume and multiple scheduling retries will be needed. 
## Before you begin 
Kubernetes v1.37 includes cluster-level API support for storage capacity tracking. To use this you must also be using a CSI driver that supports capacity tracking. Consult the documentation for the CSI drivers that you use to find out whether this support is available and, if so, how to use it. If you are not running Kubernetes v1.37, check the documentation for that version of Kubernetes. 
## API 
There are two API extensions for this feature: 
- CSIStorageCapacity objects: these get produced by a CSI driver in the namespace where the driver is installed. Each object contains capacity information for one storage class and defines which nodes have access to that storage. - The CSIDriverSpec.StorageCapacityfield : when set to true, the Kubernetes scheduler will consider storage capacity for volumes that use the CSI driver. 
## Scheduling 
Storage capacity information is used by the Kubernetes scheduler if: 
- a Pod uses a volume that has not been created yet, - that volume uses a StorageClass which references a CSI driver and uses WaitForFirstConsumervolume binding mode , and - the CSIDriverobject for the driver has StorageCapacityset to true. 
In that case, the scheduler only considers nodes for the Pod which have enough storage available to them. This check is very simplistic and only compares the size of the volume against the capacity listed in CSIStorageCapacityobjects with a topology that includes the node. 
For volumes with Immediatevolume binding mode, the storage driver decides where to create the volume, independently of Pods that will use the volume. The scheduler then schedules Pods onto nodes where the volume is available after the volume has been created. 
For CSI ephemeral volumes , scheduling always happens without considering storage capacity. This is based on the assumption that this volume type is only used by special CSI drivers which are local to a node and do not need significant resources there. 
## Rescheduling 
When a node has been selected for a Pod with WaitForFirstConsumervolumes, that decision is still tentative. The next step is that the CSI storage driver gets asked to create the volume with a hint that the volume is supposed to be available on the selected node. 
Because Kubernetes might have chosen a node based on out-dated capacity information, it is possible that the volume cannot really be created. The node selection is then reset and the Kubernetes scheduler tries again to find a node for the Pod. 
## Limitations 
Storage capacity tracking increases the chance that scheduling works on the first try, but cannot guarantee this because the scheduler has to decide based on potentially out-dated information. Usually, the same retry mechanism as for scheduling without any storage capacity information handles scheduling failures. 
One situation where scheduling can fail permanently is when a Pod uses multiple volumes: one volume might have been created already in a topology segment which then does not have enough capacity left for another volume. Manual intervention is necessary to recover from this, for example by increasing capacity or deleting the volume that was already created. 
## What's next 
- For more information on the design, see the Storage Capacity Constraints for Pod Scheduling KEP . 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified October 24, 2022 at 3:55 PM PST: KubeCon Docs Sprint: Update page weights for content/en/docs/concepts/storage. (54ecdc4896) 
- - - - - - 

- - - - 

#### 📄 Sub-topic: [https://kubernetes.io/docs/concepts/storage/storage-classes](https://kubernetes.io/docs/concepts/storage/storage-classes)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - Bahasa Indonesia (Indonesian)   - 日本語 (Japanese)   - 한국어 (Korean)   - Español (Spanish)   - বাংলা (Bengali)   - Français (French)   - Deutsch (German)   - हिन्दी (Hindi)   - Italiano (Italian)   - فارسی (Persian)   - Polski (Polish)   - Português (Portuguese)   - Русский (Russian)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# Storage Classes 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- - - - - - - - - 
  -   -   -   -   -   -   -   -   - 
- - - - 
# Storage Classes 
This document describes the concept of a StorageClass in Kubernetes. Familiarity with volumes and persistent volumes is suggested. 
A StorageClass provides a way for administrators to describe the classes of storage they offer. Different classes might map to quality-of-service levels, or to backup policies, or to arbitrary policies determined by the cluster administrators. Kubernetes itself is unopinionated about what classes represent. 
The Kubernetes concept of a storage class is similar to “profiles” in some other storage system designs. 
## StorageClass objects 
Each StorageClass contains the fields provisioner, parameters, and reclaimPolicy, which are used when a PersistentVolume belonging to the class needs to be dynamically provisioned to satisfy a PersistentVolumeClaim (PVC). 
The name of a StorageClass object is significant, and is how users can request a particular class. Administrators set the name and other parameters of a class when first creating StorageClass objects. 
As an administrator, you can specify a default StorageClass that applies to any PVCs that don't request a specific class. For more details, see the PersistentVolumeClaim concept . 
Here's an example of a StorageClass: storage/storageclass-low-latency.yaml
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:low-latencyannotations:storageclass.kubernetes.io/is-default-class:"false"provisioner:csi-driver.example-vendor.examplereclaimPolicy:Retain# default value is DeleteallowVolumeExpansion:truemountOptions:- discard# this might enable UNMAP / TRIM at the block storage layervolumeBindingMode:WaitForFirstConsumerparameters:guaranteedReadWriteLatency:"true"# provider-specific
```

## Default StorageClass 
You can mark a StorageClass as the default for your cluster. For instructions on setting the default StorageClass, see Change the default StorageClass . 
When a PVC does not specify a storageClassName, the default StorageClass is used. 
If you set the storageclass.kubernetes.io/is-default-classannotation to true on more than one StorageClass in your cluster, and you then create a PersistentVolumeClaim with no storageClassNameset, Kubernetes uses the most recently created default StorageClass. 
#### Note: You should try to only have one StorageClass in your cluster that is marked as the default. The reason that Kubernetes allows you to have multiple default StorageClasses is to allow for seamless migration. 
You can create a PersistentVolumeClaim without specifying a storageClassNamefor the new PVC, and you can do so even when no default StorageClass exists in your cluster. In this case, the new PVC creates as you defined it, and the storageClassNameof that PVC remains unset until a default becomes available. 
You can have a cluster without any default StorageClass. If you don't mark any StorageClass as default (and one hasn't been set for you by, for example, a cloud provider), then Kubernetes cannot apply that defaulting for PersistentVolumeClaims that need it. 
If or when a default StorageClass becomes available, the control plane identifies any existing PVCs without storageClassName. For the PVCs that either have an empty value for storageClassNameor do not have this key, the control plane then updates those PVCs to set storageClassNameto match the new default StorageClass. If you have an existing PVC where the storageClassNameis "", and you configure a default StorageClass, then this PVC will not get updated. 
In order to keep binding to PVs with storageClassNameset to ""(while a default StorageClass is present), you need to set the storageClassNameof the associated PVC to "". 
## Provisioner 
Each StorageClass has a provisioner that determines what volume plugin is used for provisioning PVs. This field must be specified. 
|  Volume Plugin  | Internal Provisioner  | Config Example  |
|  AzureFile  | ✓  | Azure File  |
|  CephFS  | -  | -  |
|  FC  | -  | -  |
|  FlexVolume  | -  | -  |
|  iSCSI  | -  | -  |
|  Local  | -  | Local  |
|  NFS  | -  | NFS  |
|  PortworxVolume  | ✓  | Portworx Volume  |
|  RBD  | -  | Ceph RBD  |
|  VsphereVolume  | ✓  | vSphere  |
You are not restricted to specifying the "internal" provisioners listed here (whose names are prefixed with "kubernetes.io" and shipped alongside Kubernetes). You can also run and specify external provisioners, which are independent programs that follow a specification defined by Kubernetes. Authors of external provisioners have full discretion over where their code lives, how the provisioner is shipped, how it needs to be run, what volume plugin it uses (including Flex), etc. The repository kubernetes-sigs/sig-storage-lib-external-provisioner houses a library for writing external provisioners that implements the bulk of the specification. Some external provisioners are listed under the repository kubernetes-sigs/sig-storage-lib-external-provisioner . 
For example, NFS doesn't provide an internal provisioner, but an external provisioner can be used. There are also cases when 3rd party storage vendors provide their own external provisioner. 
## Reclaim policy 
PersistentVolumes that are dynamically created by a StorageClass will have the reclaim policy specified in the reclaimPolicyfield of the class, which can be either Deleteor Retain. If no reclaimPolicyis specified when a StorageClass object is created, it will default to Delete. 
PersistentVolumes that are created manually and managed via a StorageClass will have whatever reclaim policy they were assigned at creation. 
## Volume expansion 
PersistentVolumes can be configured to be expandable. This allows you to resize the volume by editing the corresponding PVC object, requesting a new larger amount of storage. 
The following types of volumes support volume expansion, when the underlying StorageClass has the field allowVolumeExpansionset to true. Table of Volume types and the version of Kubernetes they require 
|  Volume type  | Required Kubernetes version for volume expansion  |
|  Azure File  | 1.11  |
|  CSI  | 1.24  |
|  FlexVolume  | 1.13  |
|  Portworx  | 1.11  |
|  rbd  | 1.11  |
#### Note: You can only use the volume expansion feature to grow a Volume, not to shrink it. 
## Mount options 
PersistentVolumes that are dynamically created by a StorageClass will have the mount options specified in the mountOptionsfield of the class. 
If the volume plugin does not support mount options but mount options are specified, provisioning will fail. Mount options are not validated on either the class or PV. If a mount option is invalid, the PV mount fails. 
## Volume binding mode 
The volumeBindingModefield controls when volume binding and dynamic provisioning should occur. When unset, Immediatemode is used by default. 
The Immediatemode indicates that volume binding and dynamic provisioning occurs once the PersistentVolumeClaim is created. For storage backends that are topology-constrained and not globally accessible from all Nodes in the cluster, PersistentVolumes will be bound or provisioned without knowledge of the Pod's scheduling requirements. This may result in unschedulable Pods. 
A cluster administrator can address this issue by specifying the WaitForFirstConsumermode which will delay the binding and provisioning of a PersistentVolume until a Pod using the PersistentVolumeClaim is created. PersistentVolumes will be selected or provisioned conforming to the topology that is specified by the Pod's scheduling constraints. These include, but are not limited to, resource requirements , node selectors , pod affinity and anti-affinity , and taints and tolerations . 
The following plugins support WaitForFirstConsumerwith dynamic provisioning: 
- CSI volumes, provided that the specific CSI driver supports this 
The following plugins support WaitForFirstConsumerwith pre-created PersistentVolume binding: 
- CSI volumes, provided that the specific CSI driver supports this - local
#### Note: 
If you choose to use WaitForFirstConsumer, do not use nodeNamein the Pod spec to specify node affinity. If nodeNameis used in this case, the scheduler will be bypassed and PVC will remain in pendingstate. 
Instead, you can use node selector for kubernetes.io/hostname: storage/storageclass/pod-volume-binding.yaml
```
apiVersion:v1kind:Podmetadata:name:task-pv-podspec:nodeSelector:kubernetes.io/hostname:kube-01volumes:- name:task-pv-storagepersistentVolumeClaim:claimName:task-pv-claimcontainers:- name:task-pv-containerimage:nginxports:- containerPort:80name:"http-server"volumeMounts:- mountPath:"/usr/share/nginx/html"name:task-pv-storage
```

## Allowed topologies 
When a cluster operator specifies the WaitForFirstConsumervolume binding mode, it is no longer necessary to restrict provisioning to specific topologies in most situations. However, if still required, allowedTopologiescan be specified. 
This example demonstrates how to restrict the topology of provisioned volumes to specific zones and should be used as a replacement for the zoneand zonesparameters for the supported plugins. storage/storageclass/storageclass-topology.yaml
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:standardprovisioner:example.com/exampleparameters:type:pd-standardvolumeBindingMode:WaitForFirstConsumerallowedTopologies:- matchLabelExpressions:- key:topology.kubernetes.io/zonevalues:- us-central-1a- us-central-1b
```

## Parameters 
StorageClasses have parameters that describe volumes belonging to the storage class. Different parameters may be accepted depending on the provisioner. When a parameter is omitted, some default is used. 
There can be at most 512 parameters defined for a StorageClass. The total length of the parameters object including its keys and values cannot exceed 256 KiB. 
### AWS EBS 
Kubernetes 1.37 does not include a awsElasticBlockStorevolume type. 
The AWSElasticBlockStore in-tree storage driver was deprecated in the Kubernetes v1.19 release and then removed entirely in the v1.27 release. 
The Kubernetes project suggests that you use the AWS EBS out-of-tree storage driver instead. 
Here is an example StorageClass for the AWS EBS CSI driver: storage/storageclass/storageclass-aws-ebs.yaml
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:ebs-scprovisioner:ebs.csi.aws.comvolumeBindingMode:WaitForFirstConsumerparameters:csi.storage.k8s.io/fstype:xfstype:io1iopsPerGB:"50"encrypted:"true"tagSpecification_1:"key1=value1"tagSpecification_2:"key2=value2"allowedTopologies:- matchLabelExpressions:- key:topology.ebs.csi.aws.com/zonevalues:- us-east-2c
```

tagSpecification: Tags with this prefix are applied to dynamically provisioned EBS volumes. 
### AWS EFS 
To configure AWS EFS storage, you can use the out-of-tree AWS_EFS_CSI_DRIVER . storage/storageclass/storageclass-aws-efs.yaml
```
kind:StorageClassapiVersion:storage.k8s.io/v1metadata:name:efs-scprovisioner:efs.csi.aws.comparameters:provisioningMode:efs-apfileSystemId:fs-92107410directoryPerms:"700"
```

- provisioningMode: The type of volume to be provisioned by Amazon EFS. Currently, only access point based provisioning is supported ( efs-ap). - fileSystemId: The file system under which the access point is created. - directoryPerms: The directory permissions of the root directory created by the access point. 
For more details, refer to the AWS_EFS_CSI_Driver Dynamic Provisioning documentation. 
### NFS 
To configure NFS storage, you can use the in-tree driver or the NFS CSI driver for Kubernetes (recommended). storage/storageclass/storageclass-nfs.yaml
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:example-nfsprovisioner:example.com/external-nfsparameters:server:nfs-server.example.compath:/sharereadOnly:"false"
```

- server: Server is the hostname or IP address of the NFS server. - path: Path that is exported by the NFS server. - readOnly: A flag indicating whether the storage will be mounted as read only (default false). 
Kubernetes doesn't include an internal NFS provisioner. You need to use an external provisioner to create a StorageClass for NFS. Here are some examples: 
- NFS Ganesha server and external provisioner - NFS subdir external provisioner 
### vSphere 
There are two types of provisioners for vSphere storage classes: 
- CSI provisioner : csi.vsphere.vmware.com- vCP provisioner : kubernetes.io/vsphere-volume
In-tree provisioners are deprecated . For more information on the CSI provisioner, see Kubernetes vSphere CSI Driver and vSphereVolume CSI migration . 
#### CSI Provisioner 
The vSphere CSI StorageClass provisioner works with Tanzu Kubernetes clusters. For an example, refer to the vSphere CSI repository . 
#### vCP Provisioner 
The following examples use the VMware Cloud Provider (vCP) StorageClass provisioner. 
- 
Create a StorageClass with a user specified disk format. 
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:fastprovisioner:kubernetes.io/vsphere-volumeparameters:diskformat:zeroedthick
```

diskformat: thin, zeroedthickand eagerzeroedthick. Default: "thin". - 
Create a StorageClass with a disk format on a user specified datastore. 
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:fastprovisioner:kubernetes.io/vsphere-volumeparameters:diskformat:zeroedthickdatastore:VSANDatastore
```

datastore: The user can also specify the datastore in the StorageClass. The volume will be created on the datastore specified in the StorageClass, which in this case is VSANDatastore. This field is optional. If the datastore is not specified, then the volume will be created on the datastore specified in the vSphere config file used to initialize the vSphere Cloud Provider. - 
Storage Policy Management inside kubernetes 
  - 
Using existing vCenter SPBM policy 
One of the most important features of vSphere for Storage Management is policy based Management. Storage Policy Based Management (SPBM) is a storage policy framework that provides a single unified control plane across a broad range of data services and storage solutions. SPBM enables vSphere administrators to overcome upfront storage provisioning challenges, such as capacity planning, differentiated service levels and managing capacity headroom. 
The SPBM policies can be specified in the StorageClass using the storagePolicyNameparameter.   - 
Virtual SAN policy support inside Kubernetes 
Vsphere Infrastructure (VI) Admins will have the ability to specify custom Virtual SAN Storage Capabilities during dynamic volume provisioning. You can now define storage requirements, such as performance and availability, in the form of storage capabilities during dynamic volume provisioning. The storage capability requirements are converted into a Virtual SAN policy which are then pushed down to the Virtual SAN layer when a persistent volume (virtual disk) is being created. The virtual disk is distributed across the Virtual SAN datastore to meet the requirements. 
You can see Storage Policy Based Management for dynamic provisioning of volumes for more details on how to use storage policies for persistent volumes management. 
### Ceph RBD (deprecated) 
#### Note: 
```
<div class="feature-state-notice feature-deprecated">
  <span class="feature-state-name">Feature state:</span>
  <span class="feature-state-details">
  <span class="feature-state-stage">Deprecated</span> since Kubernetes v1.28
  </span>
</div>

```

This internal provisioner of Ceph RBD is deprecated. Please use CephFS RBD CSI driver . storage/storageclass/storageclass-ceph-rbd.yaml
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:fastprovisioner:kubernetes.io/rbd# This provisioner is deprecatedparameters:monitors:198.19.254.105:6789adminId:kubeadminSecretName:ceph-secretadminSecretNamespace:kube-systempool:kubeuserId:kubeuserSecretName:ceph-secret-useruserSecretNamespace:defaultfsType:ext4imageFormat:"2"imageFeatures:"layering"
```

- 
monitors: Ceph monitors, comma delimited. This parameter is required. - 
adminId: Ceph client ID that is capable of creating images in the pool. Default is "admin". - 
adminSecretName: Secret Name for adminId. This parameter is required. The provided secret must have type "kubernetes.io/rbd". - 
adminSecretNamespace: The namespace for adminSecretName. Default is "default". - 
pool: Ceph RBD pool. Default is "rbd". - 
userId: Ceph client ID that is used to map the RBD image. Default is the same as adminId. - 
userSecretName: The name of Ceph Secret for userIdto map RBD image. It must exist in the same namespace as PVCs. This parameter is required. The provided secret must have type "kubernetes.io/rbd", for example created in this way: 
```
kubectl create secret generic ceph-secret --type="kubernetes.io/rbd"\
  --from-literal=key='QVFEQ1pMdFhPUnQrSmhBQUFYaERWNHJsZ3BsMmNjcDR6RFZST0E9PQ=='\
  --namespace=kube-system

```
- 
userSecretNamespace: The namespace for userSecretName. - 
fsType: fsType that is supported by kubernetes. Default: "ext4". - 
imageFormat: Ceph RBD image format, "1" or "2". Default is "2". - 
imageFeatures: This parameter is optional and should only be used if you set imageFormatto "2". Currently supported features are layeringonly. Default is "", and no features are turned on. 
### Azure Disk 
Kubernetes 1.37 does not include a azureDiskvolume type. 
The azureDiskin-tree storage driver was deprecated in the Kubernetes v1.19 release and then removed entirely in the v1.27 release. 
The Kubernetes project suggests that you use the Azure Disk third party storage driver instead. 
### Azure File (deprecated) storage/storageclass/storageclass-azure-file.yaml
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:azurefileprovisioner:kubernetes.io/azure-fileparameters:skuName:Standard_LRSlocation:eastusstorageAccount:azure_storage_account_name# example value
```

- skuName: Azure storage account SKU tier. Default is empty. - location: Azure storage account location. Default is empty. - storageAccount: Azure storage account name. Default is empty. If a storage account is not provided, all storage accounts associated with the resource group are searched to find one that matches skuNameand location. If a storage account is provided, it must reside in the same resource group as the cluster, and skuNameand locationare ignored. - secretNamespace: the namespace of the secret that contains the Azure Storage Account Name and Key. Default is the same as the Pod. - secretName: the name of the secret that contains the Azure Storage Account Name and Key. Default is azure-storage-account-<accountName>-secret- readOnly: a flag indicating whether the storage will be mounted as read only. Defaults to false which means a read/write mount. This setting will impact the ReadOnlysetting in VolumeMounts as well. 
During storage provisioning, a secret named by secretNameis created for the mounting credentials. If the cluster has enabled both RBAC and Controller Roles , add the createpermission of resource secretfor clusterrole system:controller:persistent-volume-binder. 
In a multi-tenancy context, it is strongly recommended to set the value for secretNamespaceexplicitly, otherwise the storage account credentials may be read by other users. 
### Portworx volume (deprecated) storage/storageclass/storageclass-portworx-volume.yaml
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:portworx-io-priority-highprovisioner:kubernetes.io/portworx-volume# This provisioner is deprecatedparameters:repl:"1"snap_interval:"70"priority_io:"high"
```

- fs: filesystem to be laid out: none/xfs/ext4(default: ext4). - block_size: block size in Kbytes (default: 32). - repl: number of synchronous replicas to be provided in the form of replication factor 1..3(default: 1) A string is expected here i.e. "1"and not 1. - priority_io: determines whether the volume will be created from higher performance or a lower priority storage high/medium/low(default: low). - snap_interval: clock/time interval in minutes for when to trigger snapshots. Snapshots are incremental based on difference with the prior snapshot, 0 disables snaps (default: 0). A string is expected here i.e. "70"and not 70. - aggregation_level: specifies the number of chunks the volume would be distributed into, 0 indicates a non-aggregated volume (default: 0). A string is expected here i.e. "0"and not 0- ephemeral: specifies whether the volume should be cleaned-up after unmount or should be persistent. emptyDiruse case can set this value to true and persistent volumesuse case such as for databases like Cassandra should set to false, true/false(default false). A string is expected here i.e. "true"and not true. 
### Local storage/storageclass/storageclass-local.yaml
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:local-storageprovisioner:kubernetes.io/no-provisioner# indicates that this StorageClass does not support automatic provisioningvolumeBindingMode:WaitForFirstConsumer
```

Local volumes do not support dynamic provisioning in Kubernetes 1.37; however a StorageClass should still be created to delay volume binding until a Pod is actually scheduled to the appropriate node. This is specified by the WaitForFirstConsumervolume binding mode. 
Delaying volume binding allows the scheduler to consider all of a Pod's scheduling constraints when choosing an appropriate PersistentVolume for a PersistentVolumeClaim. 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified August 11, 2026 at 5:45 PM PST: docs: fix volume-provisioning design proposal link (2bd65cc47e) 
- - - - - - 

- - - - 

#### 📄 Sub-topic: [https://kubernetes.io/docs/concepts/storage/storage-limits](https://kubernetes.io/docs/concepts/storage/storage-limits)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - Bahasa Indonesia (Indonesian)   - 日本語 (Japanese)   - 한국어 (Korean)   - Español (Spanish)   - বাংলা (Bengali)   - Français (French)   - Deutsch (German)   - हिन्दी (Hindi)   - Italiano (Italian)   - فارسی (Persian)   - Polski (Polish)   - Português (Portuguese)   - Русский (Russian)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# Node-specific Volume Limits 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- - 
  -   -   - 
- - - - 
# Node-specific Volume Limits 
This page describes the maximum number of volumes that can be attached to a Node for various cloud providers. 
Cloud providers like Google, Amazon, and Microsoft typically have a limit on how many volumes can be attached to a Node. It is important for Kubernetes to respect those limits. Otherwise, Pods scheduled on a Node could get stuck waiting for volumes to attach. 
## Kubernetes default limits 
The Kubernetes scheduler has default limits on the number of volumes that can be attached to a Node: 
|  Cloud service  | Maximum volumes per Node  |
|  Amazon Elastic Block Store (EBS)  | 39  |
|  Google Persistent Disk  | 16  |
|  Microsoft Azure Disk Storage  | 16  |
## Dynamic volume limits Feature state: Stable since Kubernetes v1.17 
Dynamic volume limits are supported for following volume types. 
- Amazon EBS - Google Persistent Disk - Azure Disk - CSI 
For volumes managed by in-tree volume plugins, Kubernetes automatically determines the Node type and enforces the appropriate maximum number of volumes for the node. For example: 
- 
On Google Compute Engine , up to 127 volumes can be attached to a node, depending on the node type . - 
For Amazon EBS disks on M5,C5,R5,T3 and Z1D instance types, Kubernetes allows only 25 volumes to be attached to a Node. For other instance types on Amazon Elastic Compute Cloud (EC2) , Kubernetes allows 39 volumes to be attached to a Node. - 
On Azure, up to 64 disks can be attached to a node, depending on the node type. For more details, refer to Sizes for virtual machines in Azure . - 
If a CSI storage driver advertises a maximum number of volumes for a Node (using NodeGetInfo), the kube-scheduler honors that limit. Refer to the CSI specifications for details. - 
For volumes managed by in-tree plugins that have been migrated to a CSI driver, the maximum number of volumes will be the one reported by the CSI driver. 
### Mutable CSI Node Allocatable Count Feature state: Stable since Kubernetes v1.36; enabled by default More information about this feature 
This is a stable feature in , and has been since version 1.36. It was first available in the v1.33 release. 
CSI drivers can dynamically adjust the maximum number of volumes that can be attached to a Node at runtime. This enhances scheduling accuracy and reduces pod scheduling failures due to changes in resource availability. 
To use this feature, you must enable the MutableCSINodeAllocatableCountfeature gate on the following components: 
- kube-apiserver- kubelet
#### Periodic Updates 
When enabled, CSI drivers can request periodic updates to their volume limits by setting the nodeAllocatableUpdatePeriodSecondsfield in the CSIDriverspecification. For example: 
```
apiVersion:storage.k8s.io/v1kind:CSIDrivermetadata:name:hostpath.csi.k8s.iospec:nodeAllocatableUpdatePeriodSeconds:60
```

Kubelet will periodically call the corresponding CSI driver’s NodeGetInfoendpoint to refresh the maximum number of attachable volumes, using the interval specified in nodeAllocatableUpdatePeriodSeconds. The minimum allowed value for this field is 10 seconds. 
If a volume attachment operation fails with a ResourceExhaustederror (gRPC code 8), Kubernetes triggers an immediate update to the allocatable volume count for that Node. Additionally, kubelet marks affected pods as Failed, allowing their controllers to handle recreation. This prevents pods from getting stuck indefinitely in the ContainerCreatingstate. 
### Preventing Pod placement without CSI driver Feature state: Beta since Kubernetes v1.37; enabled by default 
The VolumeLimitScalingfeature gate is enabled by default in Kubernetes v1.37. 
However, preventing pod placement on nodes without a CSI driver requires explicit opt-in via the spec.preventPodSchedulingIfMissingfield of the CSIDriverobject. 
The preventPodSchedulingIfMissingfield defaults to falseand must be set to trueif you do not want pods to be scheduled on nodes without a CSI driver. This decision to default to falsewas made for backward compatibility reasons and compatibility with Cluster AutoScaler which may not be aware of CSI volume limits during the autoscaling phase (see section below). 
```
apiVersion:storage.k8s.io/v1kind:CSIDrivermetadata:name:hostpath.csi.k8s.iospec:preventPodSchedulingIfMissing:true
```

### CSI volume attach limits and cluster autoscaler 
Cluster autoscaler can account for CSI volume limits when --enable-csi-node-aware-scheduling=true. This option is independent of the VolumeLimitScalingfeature gate. 
If you use cluster autoscaler, only set spec.preventPodSchedulingIfMissingto truewhen cluster autoscaler is configured with --enable-csi-node-aware-scheduling=true. Otherwise, its scheduling simulations do not include the required CSINodeinformation for new nodes, and cluster autoscaler might fail to scale up for pending Pods that use CSI volumes. 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified August 06, 2026 at 10:11 AM PST: Add links for Cluster Autoscaler (d525c3e375) 
- - - - - - 

- - - - 

#### 📄 Sub-topic: [https://kubernetes.io/docs/concepts/storage/volume-attributes-classes](https://kubernetes.io/docs/concepts/storage/volume-attributes-classes)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - 日本語 (Japanese)   - বাংলা (Bengali)   - Français (French)   - Deutsch (German)   - हिन्दी (Hindi)   - Bahasa Indonesia (Indonesian)   - Italiano (Italian)   - 한국어 (Korean)   - فارسی (Persian)   - Polski (Polish)   - Português (Portuguese)   - Русский (Russian)   - Español (Spanish)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# Volume Attributes Classes 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- 
  -   - - 
- - - - 
# Volume Attributes Classes Feature state: Stable since Kubernetes v1.36 More information about this feature 
This is a stable feature in Kubernetes, and has been since version v1.36. It was first available in the v1.29 release. You can no longer disable or opt out of this feature or behavior (it is locked); if you explicitly set a value for the associated feature gate VolumeAttributesClass , Kubernetes ignores it but does not report any error. 
This page assumes that you are familiar with StorageClasses , volumes and PersistentVolumes in Kubernetes. 
A VolumeAttributesClass provides a way for administrators to describe the mutable "classes" of storage they offer. Different classes might map to different quality-of-service levels. Kubernetes itself is un-opinionated about what these classes represent. 
This feature is generally available (GA) as of version 1.34, and users have the option to disable it. 
You can also only use VolumeAttributesClasses with storage backed by Container Storage Interface , and only where the relevant CSI driver implements the ModifyVolumeAPI. 
## The VolumeAttributesClass API 
Each VolumeAttributesClass contains the driverNameand parameters, which are used when a PersistentVolume (PV) belonging to the class needs to be dynamically provisioned or modified. 
The name of a VolumeAttributesClass object is significant and is how users can request a particular class. Administrators set the name and other parameters of a class when first creating VolumeAttributesClass objects. While the name of a VolumeAttributesClass object in a PersistentVolumeClaimis mutable, the parameters in an existing class are immutable. 
```
apiVersion:storage.k8s.io/v1kind:VolumeAttributesClassmetadata:name:silverdriverName:pd.csi.storage.gke.ioparameters:provisioned-iops:"3000"provisioned-throughput:"50"
```

### Provisioner 
Each VolumeAttributesClass has a provisioner that determines what volume plugin is used for provisioning PVs. The field driverNamemust be specified. 
The feature support for VolumeAttributesClass is implemented in kubernetes-csi/external-provisioner . 
You are not restricted to specifying the kubernetes-csi/external-provisioner . You can also run and specify external provisioners, which are independent programs that follow a specification defined by Kubernetes. Authors of external provisioners have full discretion over where their code lives, how the provisioner is shipped, how it needs to be run, what volume plugin it uses, etc. 
To understand how the provisioner works with VolumeAttributesClass, refer to the CSI external-provisioner documentation . 
### Resizer 
Each VolumeAttributesClass has a resizer that determines what volume plugin is used for modifying PVs. The field driverNamemust be specified. 
The modifying volume feature support for VolumeAttributesClass is implemented in kubernetes-csi/external-resizer . 
For example, an existing PersistentVolumeClaim is using a VolumeAttributesClass named silver: 
```
apiVersion:v1kind:PersistentVolumeClaimmetadata:name:test-pv-claimspec:…volumeAttributesClassName:silver…
```

A new VolumeAttributesClass gold is available in the cluster: 
```
apiVersion:storage.k8s.io/v1kind:VolumeAttributesClassmetadata:name:golddriverName:pd.csi.storage.gke.ioparameters:iops:"4000"throughput:"60"
```

The end user can update the PVC with the new VolumeAttributesClass gold and apply: 
```
apiVersion:v1kind:PersistentVolumeClaimmetadata:name:test-pv-claimspec:…volumeAttributesClassName:gold…
```

To understand how the resizer works with VolumeAttributesClass, refer to the CSI external-resizer documentation . 
## Parameters 
VolumeAttributeClasses have parameters that describe volumes belonging to them. Different parameters may be accepted depending on the provisioner or the resizer. For example, the value 4000, for the parameter iops, and the parameter throughputare specific to GCE PD. When a parameter is omitted, the default is used at volume provisioning. If a user applies the PVC with a different VolumeAttributesClass with omitted parameters, the default value of the parameters may be used depending on the CSI driver implementation. Please refer to the related CSI driver documentation for more details. 
There can be at most 512 parameters defined for a VolumeAttributesClass. The total length of the parameters object including its keys and values cannot exceed 256 KiB. 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified July 29, 2025 at 6:02 PM PST: KEP-3751 VolumeAttributesClass GA in 1.34 Doc Update (2d15dba7b5) 
- - - - - - 

- - - - 

### 📄 Source: [https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - বাংলা (Bengali)   - Français (French)   - Deutsch (German)   - हिन्दी (Hindi)   - Bahasa Indonesia (Indonesian)   - Italiano (Italian)   - 日本語 (Japanese)   - 한국어 (Korean)   - فارسی (Persian)   - Polski (Polish)   - Português (Portuguese)   - Русский (Russian)   - Español (Spanish)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# Admission Control in Kubernetes 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- 
  -   - - - - - - 
  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   - - 
- - - - 
# Admission Control in Kubernetes 
This page provides an overview of admission controllers . 
An admission controller is a piece of code that intercepts requests to the Kubernetes API server prior to persistence of the resource, but after the request is authenticated and authorized. 
Several important features of Kubernetes require an admission controller to be enabled in order to properly support the feature. As a result, a Kubernetes API server that is not properly configured with the right set of admission controllers is an incomplete server that will not support all the features you expect. 
## What are they? 
Admission controllers are code within the Kubernetes API server that check the data arriving in a request to modify a resource. 
Admission controllers apply to requests that create, delete, or modify objects. Admission controllers can also block custom verbs, such as a request to connect to a pod via an API server proxy. Admission controllers do not (and cannot) block requests to read ( get , watch or list ) objects, because reads bypass the admission control layer. 
Admission control mechanisms may be validating , mutating , or both. Mutating controllers may modify the data for the resource being modified; validating controllers may not. 
The admission controllers in Kubernetes 1.37 consist of the list below, are compiled into the kube-apiserverbinary, and may only be configured by the cluster administrator. 
### Admission control extension points 
Within the full list , there are three special controllers: MutatingAdmissionWebhook , ValidatingAdmissionWebhook , and ValidatingAdmissionPolicy . The two webhook controllers execute the mutating and validating (respectively) admission control webhooks which are configured in the API. ValidatingAdmissionPolicy provides a way to embed declarative validation code within the API, without relying on any external HTTP callouts. 
You can use these three admission controllers to customize cluster behavior at admission time. 
### Admission control phases 
The admission control process proceeds in two phases. In the first phase, mutating admission controllers are run. In the second phase, validating admission controllers are run. Note again that some of the controllers are both. 
If any of the controllers in either phase reject the request, the entire request is rejected immediately and an error is returned to the end-user. 
Finally, in addition to sometimes mutating the object in question, admission controllers may sometimes have side effects, that is, mutate related resources as part of request processing. Incrementing quota usage is the canonical example of why this is necessary. Any such side-effect needs a corresponding reclamation or reconciliation process, as a given admission controller does not know for sure that a given request will pass all of the other admission controllers. 
The ordering of these calls can be seen below. 
## Why do I need them? 
Several important features of Kubernetes require an admission controller to be enabled in order to properly support the feature. As a result, a Kubernetes API server that is not properly configured with the right set of admission controllers is an incomplete server and will not support all the features you expect. 
## How do I turn on an admission controller? 
The Kubernetes API server flag enable-admission-pluginstakes a comma-delimited list of admission control plugins to invoke prior to modifying objects in the cluster. For example, the following command line enables the NamespaceLifecycleand the LimitRangeradmission control plugins: 
```
kube-apiserver --enable-admission-plugins=NamespaceLifecycle,LimitRanger ...

```

#### Note: Depending on the way your Kubernetes cluster is deployed and how the API server is started, you may need to apply the settings in different ways. For example, you may have to modify the systemd unit file if the API server is deployed as a systemd service, you may modify the manifest file for the API server if Kubernetes is deployed in a self-hosted way. 
## How do I turn off an admission controller? 
The Kubernetes API server flag disable-admission-pluginstakes a comma-delimited list of admission control plugins to be disabled, even if they are in the list of plugins enabled by default. 
```
kube-apiserver --disable-admission-plugins=PodNodeSelector,AlwaysDeny ...

```

## Which plugins are enabled by default? 
To see which admission plugins are enabled: 
```
kube-apiserver -h | grep enable-admission-plugins

```

In Kubernetes 1.37, the default ones are: 
```
CertificateApproval, CertificateSigning, CertificateSubjectRestriction, DefaultIngressClass, DefaultStorageClass, DefaultTolerationSeconds, LimitRanger, MutatingAdmissionWebhook, NamespaceLifecycle, PersistentVolumeClaimResize, PodSecurity, Priority, ResourceQuota, RuntimeClass, ServiceAccount, StorageObjectInUseProtection, TaintNodesByCondition, ValidatingAdmissionPolicy, ValidatingAdmissionWebhook

```

## What does each admission controller do? 
### AlwaysAdmit Feature state: Deprecated since Kubernetes v1.13 
Type : Validating. 
This admission controller allows all pods into the cluster. It is deprecated because its behavior is the same as if there were no admission controller at all. 
### AlwaysDeny Feature state: Deprecated since Kubernetes v1.13 
Type : Validating. 
Rejects all requests. AlwaysDeny is deprecated as it has no real meaning. 
### AlwaysPullImages 
Type : Mutating and Validating. 
This admission controller modifies every new Pod to force the image pull policy to Always. This is useful in a multitenant cluster so that users can be assured that their private images can only be used by those who have the credentials to pull them. Without this admission controller, once an image has been pulled to a node, any pod from any user can use it by knowing the image's name (assuming the Pod is scheduled onto the right node), without any authorization check against the image. When this admission controller is enabled, images are always pulled prior to starting containers, which means valid credentials are required. 
### CertificateApproval 
Type : Validating. 
This admission controller observes requests to approve CertificateSigningRequest resources and performs additional authorization checks to ensure the approving user has permission to approve certificate requests with the spec.signerNamerequested on the CertificateSigningRequest resource. 
See Certificate Signing Requests for more information on the permissions required to perform different actions on CertificateSigningRequest resources. 
### CertificateSigning 
Type : Validating. 
This admission controller observes updates to the status.certificatefield of CertificateSigningRequest resources and performs an additional authorization checks to ensure the signing user has permission to sign certificate requests with the spec.signerNamerequested on the CertificateSigningRequest resource. 
See Certificate Signing Requests for more information on the permissions required to perform different actions on CertificateSigningRequest resources. 
### CertificateSubjectRestriction 
Type : Validating. 
This admission controller observes creation of CertificateSigningRequest resources that have a spec.signerNameof kubernetes.io/kube-apiserver-client. It rejects any request that specifies a 'group' (or 'organization attribute') of system:masters. 
### DefaultIngressClass 
Type : Mutating. 
This admission controller observes creation of Ingressobjects that do not request any specific ingress class and automatically adds a default ingress class to them. This way, users that do not request any special ingress class do not need to care about them at all and they will get the default one. 
This admission controller does not do anything when no default ingress class is configured. When more than one ingress class is marked as default, it rejects any creation of Ingresswith an error and an administrator must revisit their IngressClassobjects and mark only one as default (with the annotation "ingressclass.kubernetes.io/is-default-class"). This admission controller ignores any Ingressupdates; it acts only on creation. 
See the Ingress documentation for more about ingress classes and how to mark one as default. 
### DefaultStorageClass 
Type : Mutating. 
This admission controller observes creation of PersistentVolumeClaimobjects that do not request any specific storage class and automatically adds a default storage class to them. This way, users that do not request any special storage class do not need to care about them at all and they will get the default one. 
This admission controller does nothing when no default StorageClassexists. When more than one storage class is marked as default, and you then create a PersistentVolumeClaimwith no storageClassNameset, Kubernetes uses the most recently created default StorageClass. When a PersistentVolumeClaimis created with a specified volumeName, it remains in a pending state if the static volume's storageClassNamedoes not match the storageClassNameon the PersistentVolumeClaimafter any default StorageClass is applied to it. This admission controller ignores any PersistentVolumeClaimupdates; it acts only on creation. 
See persistent volume documentation about persistent volume claims and storage classes and how to mark a storage class as default. 
### DefaultTolerationSeconds 
Type : Mutating. 
This admission controller sets the default forgiveness toleration for pods to tolerate the taints notready:NoExecuteand unreachable:NoExecutebased on the k8s-apiserver input parameters default-not-ready-toleration-secondsand default-unreachable-toleration-secondsif the pods don't already have toleration for taints node.kubernetes.io/not-ready:NoExecuteor node.kubernetes.io/unreachable:NoExecute. The default value for default-not-ready-toleration-secondsand default-unreachable-toleration-secondsis 5 minutes. 
### DenyServiceExternalIPs 
Type : Validating. 
This admission controller rejects all net-new usage of the Servicefield externalIPs. This feature is very powerful (allows network traffic interception) and not well controlled by policy. When enabled, users of the cluster may not create new Services which use externalIPsand may not add new values to externalIPson existing Serviceobjects. Existing uses of externalIPsare not affected, and users may remove values from externalIPson existing Serviceobjects. 
Most users do not need this feature at all, and cluster admins should consider disabling it. Clusters that do need to use this feature should consider using some custom policy to manage usage of it. 
This admission controller is disabled by default. 
### EventRateLimit Feature state: Alpha since Kubernetes v1.13 
Type : Validating. 
This admission controller mitigates the problem where the API server gets flooded by requests to store new Events. The cluster admin can specify event rate limits by: 
- Enabling the EventRateLimitadmission controller; - Referencing an EventRateLimitconfiguration file from the file provided to the API server's command line flag --admission-control-config-file: 
```
apiVersion:apiserver.config.k8s.io/v1kind:AdmissionConfigurationplugins:- name:EventRateLimitpath:eventconfig.yaml...
```

There are four types of limits that can be specified in the configuration: 
- Server: All Event requests (creation or modifications) received by the API server share a single bucket. - Namespace: Each namespace has a dedicated bucket. - User: Each user is allocated a bucket. - SourceAndObject: A bucket is assigned by each combination of source and involved object of the event. 
Below is a sample eventconfig.yamlfor such a configuration: 
```
apiVersion:eventratelimit.admission.k8s.io/v1alpha1kind:Configurationlimits:- type:Namespaceqps:50burst:100cacheSize:2000- type:Userqps:10burst:50
```

See the EventRateLimit Config API (v1alpha1) for more details. 
This admission controller is disabled by default. 
### ExtendedResourceToleration 
Type : Mutating. 
This plug-in facilitates creation of dedicated nodes with extended resources. If operators want to create dedicated nodes with extended resources (like GPUs, FPGAs etc.), they are expected to taint the node with the extended resource name as the key. This admission controller, if enabled, automatically adds tolerations for such taints to pods requesting extended resources, so users don't have to manually add these tolerations. 
This admission controller is disabled by default. 
### ImagePolicyWebhook 
Type : Validating. 
The ImagePolicyWebhook admission controller allows a backend webhook to make admission decisions. 
This admission controller is disabled by default. 
#### Configuration file format 
ImagePolicyWebhook uses a configuration file to set options for the behavior of the backend. This file may be json or yaml and has the following format: 
```
imagePolicy:kubeConfigFile:/path/to/kubeconfig/for/backend# time in s to cache approvalallowTTL:50# time in s to cache denialdenyTTL:50# time in ms to wait between retriesretryBackoff:500# determines behavior if the webhook backend failsdefaultAllow:true
```

Reference the ImagePolicyWebhook configuration file from the file provided to the API server's command line flag --admission-control-config-file: 
```
apiVersion:apiserver.config.k8s.io/v1kind:AdmissionConfigurationplugins:- name:ImagePolicyWebhookpath:imagepolicyconfig.yaml...
```

Alternatively, you can embed the configuration directly in the file: 
```
apiVersion:apiserver.config.k8s.io/v1kind:AdmissionConfigurationplugins:- name:ImagePolicyWebhookconfiguration:imagePolicy:kubeConfigFile:<path-to-kubeconfig-file>allowTTL:50denyTTL:50retryBackoff:500defaultAllow:true
```

The ImagePolicyWebhook config file must reference a kubeconfig formatted file which sets up the connection to the backend. It is required that the backend communicate over TLS. 
The kubeconfig file's clusterfield must point to the remote service, and the userfield must contain the returned authorizer. 
```
# clusters refers to the remote service.clusters:- name:name-of-remote-imagepolicy-servicecluster:certificate-authority:/path/to/ca.pem   # CA for verifying the remote service.server:https://images.example.com/policy# URL of remote service to query. Must use 'https'.# users refers to the API server's webhook configuration.users:- name:name-of-api-serveruser:client-certificate:/path/to/cert.pem# cert for the webhook admission controller to useclient-key:/path/to/key.pem         # key matching the cert
```

For additional HTTP configuration, refer to the kubeconfig documentation. 
#### Request payloads 
When faced with an admission decision, the API Server POSTs a JSON serialized imagepolicy.k8s.io/v1alpha1ImageReviewobject describing the action. This object contains fields describing the containers being admitted, as well as any pod annotations that match *.image-policy.k8s.io/*. 
#### Note: The webhook API objects are subject to the same versioning compatibility rules as other Kubernetes API objects. Implementers should be aware of looser compatibility promises for alpha objects and check the apiVersionfield of the request to ensure correct deserialization. Additionally, the API Server must enable the imagepolicy.k8s.io/v1alpha1API extensions group ( --runtime-config=imagepolicy.k8s.io/v1alpha1=true). 
An example request body: 
```
{"apiVersion":"imagepolicy.k8s.io/v1alpha1","kind":"ImageReview","spec":{"containers":[{"image":"myrepo/myimage:v1"},{"image":"myrepo/myimage@sha256:beb6bd6a68f114c1dc2ea4b28db81bdf91de202a9014972bec5e4d9171d90ed"}],"annotations":{"mycluster.image-policy.k8s.io/ticket-1234":"break-glass"},"namespace":"mynamespace"}}
```

The remote service is expected to fill the statusfield of the request and respond to either allow or disallow access. The response body's specfield is ignored, and may be omitted. A permissive response would return: 
```
{"apiVersion":"imagepolicy.k8s.io/v1alpha1","kind":"ImageReview","status":{"allowed":true}}
```

To disallow access, the service would return: 
```
{"apiVersion":"imagepolicy.k8s.io/v1alpha1","kind":"ImageReview","status":{"allowed":false,"reason":"image currently blacklisted"}}
```

#### Note: ImageReviewobjects will include all images in Pods intended to be executed as containers. This covers images specified as part of the containers, initContainers, or ephemeralContainers fields in a Pod specification. As a result, images included under image volumes are not in scope for the ImagePolicyWebhook. 
For further documentation refer to the imagepolicy.v1alpha1API . 
#### Extending with Annotations 
All annotations on a Pod that match *.image-policy.k8s.io/*are sent to the webhook. Sending annotations allows users who are aware of the image policy backend to send extra information to it, and for different backends implementations to accept different information. 
Examples of information you might put here are: 
- request to "break glass" to override a policy, in case of emergency. - a ticket number from a ticket system that documents the break-glass request - provide a hint to the policy server as to the imageID of the image being provided, to save it a lookup 
In any case, the annotations are provided by the user and are not validated by Kubernetes in any way. 
### LimitPodHardAntiAffinityTopology 
Type : Validating. 
This admission controller denies any pod that defines an AntiAffinitytopology key other than kubernetes.io/hostnamein requiredDuringSchedulingIgnoredDuringExecution. 
This admission controller is disabled by default. 
### LimitRanger 
Type : Mutating and Validating. 
This admission controller will observe the incoming request and ensure that it does not violate any of the constraints enumerated in the LimitRangeobject in a Namespace. If you are using LimitRangeobjects in your Kubernetes deployment, you MUST use this admission controller to enforce those constraints. LimitRanger can also be used to apply default resource requests to Pods that don't specify any; currently, the default LimitRanger applies a 0.1 CPU requirement to all Pods in the defaultnamespace. 
See the LimitRange API reference and the example of LimitRange for more details. 
### MutatingAdmissionWebhook 
Type : Mutating. 
This admission controller calls any mutating webhooks which match the request. Matching webhooks are called in serial; each one may modify the object if it desires. 
This admission controller (as implied by the name) only runs in the mutating phase. 
If a webhook called by this has side effects (for example, decrementing quota) it must have a reconciliation system, as it is not guaranteed that subsequent webhooks or validating admission controllers will permit the request to finish. 
If you disable the MutatingAdmissionWebhook, you must also disable the MutatingWebhookConfigurationobject in the admissionregistration.k8s.io/v1group/version via the --runtime-configflag, both are on by default. 
#### Use caution when authoring and installing mutating webhooks 
- Users may be confused when the objects they try to create are different from what they get back. - Built in control loops may break when the objects they try to create are different when read back. 
  - Setting originally unset fields is less likely to cause problems than overwriting fields set in the original request. Avoid doing the latter. - Future changes to control loops for built-in resources or third-party resources may break webhooks that work well today. Even when the webhook installation API is finalized, not all possible webhook behaviors will be guaranteed to be supported indefinitely. 
### NamespaceAutoProvision 
Type : Mutating. 
This admission controller examines all incoming requests on namespaced resources and checks if the referenced namespace does exist. It creates a namespace if it cannot be found. This admission controller is useful in deployments that do not want to restrict creation of a namespace prior to its usage. 
### NamespaceExists 
Type : Validating. 
This admission controller checks all requests on namespaced resources other than Namespaceitself. If the namespace referenced from a request doesn't exist, the request is rejected. 
### NamespaceLifecycle 
Type : Validating. 
This admission controller enforces that a Namespacethat is undergoing termination cannot have new objects created in it, and ensures that requests in a non-existent Namespaceare rejected. This admission controller also prevents deletion of three system reserved namespaces default, kube-system, kube-public. 
A Namespacedeletion kicks off a sequence of operations that remove all objects (pods, services, etc.) in that namespace. In order to enforce integrity of that process, we strongly recommend running this admission controller. 
### NodeDeclaredFeatureValidator Feature state: Stable since Kubernetes v1.37 More information about this feature 
This is a stable feature in Kubernetes, and has been since version v1.37. It was first available in the v1.35 release. You can no longer disable or opt out of this feature or behavior (it is locked); if you explicitly set a value for the associated feature gate NodeDeclaredFeatures , Kubernetes ignores it but does not report any error. 
Type : Validating. 
This admission controller intercepts writes to bound Pods, to ensure that the changes are compatible with the features declared by the node where the Pod is currently running. It uses the .status.declaredFeaturesfield of the Node to determine the set of enabled features. If a Pod update requires a feature that is not listed in the features of its current node, the admission controller will reject the update request. This prevents runtime failures due to feature mismatch after a Pod has been scheduled. 
This admission controller is enabled by default if the NodeDeclaredFeaturesfeature gate is enabled. 
### NodeRestriction 
Type : Validating. 
This admission controller limits the Nodeand Podobjects a kubelet can modify. In order to be limited by this admission controller, kubelets must use credentials in the system:nodesgroup, with a username in the form system:node:<nodeName>. Such kubelets will only be allowed to modify their own NodeAPI object, and only modify PodAPI objects that are bound to their node. kubelets are not allowed to update or remove taints from their NodeAPI object. 
The NodeRestrictionadmission plugin prevents kubelets from deleting their NodeAPI object, and enforces kubelet modification of labels under the kubernetes.io/or k8s.io/prefixes as follows: 
- Forbidden (Kubelets are blocked from modifying these): 
  - Labels with a node-restriction.kubernetes.io/prefix. This prefix is reserved for administrators to label Nodeobjects for workload isolation.   - Labels with a node-role.kubernetes.io/prefix (for example: node-role.kubernetes.io/control-plane). These are restricted to prevent unprivileged nodes from self-declaring cluster roles. - Allowed (Kubelets can add/remove/update these): 
  - kubernetes.io/hostname  - kubernetes.io/arch  - kubernetes.io/os  - beta.kubernetes.io/instance-type  - node.kubernetes.io/instance-type  - failure-domain.beta.kubernetes.io/region(deprecated)   - failure-domain.beta.kubernetes.io/zone(deprecated)   - topology.kubernetes.io/region  - topology.kubernetes.io/zone  - kubelet.kubernetes.io/-prefixed labels   - node.kubernetes.io/-prefixed labels - Reserved : Use of any other labels under the kubernetes.ioor k8s.ioprefixes by kubelets is reserved. The NodeRestrictionadmission plugin generally disallows these to prevent unauthorized self-labeling, but may allow additional labels under these prefixes in the future as part of future features. 
When the ServiceAccountNodeAudienceRestrictionfeature gate is enabled, this admission plugin also restricts the audiences for which a kubelet can request service account tokens via the TokenRequestAPI. The kubelet can only request tokens for audiences already referenced by pods on that node (through projected service account token volumes or CSI driver token requests), or for audiences explicitly granted through RBAC using the request-serviceaccounts-token-audienceverb. For more details, see Service account token audience restriction . 
Future versions may add additional restrictions to ensure kubelets have the minimal set of permissions required to operate correctly. 
### OwnerReferencesPermissionEnforcement 
Type : Validating. 
This admission controller protects the access to the metadata.ownerReferencesof an object so that only users with delete permission to the object can change it. This admission controller also protects the access to metadata.ownerReferences[x].blockOwnerDeletionof an object, so that only users with update permission to the finalizerssubresource of the referenced owner can change it. 
### PersistentVolumeClaimResize Feature state: Stable since Kubernetes v1.24 
Type : Validating. 
This admission controller implements additional validations for checking incoming PersistentVolumeClaimresize requests. 
Enabling the PersistentVolumeClaimResizeadmission controller is recommended. This admission controller prevents resizing of all claims by default unless a claim's StorageClassexplicitly enables resizing by setting allowVolumeExpansionto true. 
For example: all PersistentVolumeClaims created from the following StorageClasssupport volume expansion: 
```
apiVersion:storage.k8s.io/v1kind:StorageClassmetadata:name:gluster-vol-defaultprovisioner:kubernetes.io/glusterfsparameters:resturl:"http://192.168.10.100:8080"restuser:""secretNamespace:""secretName:""allowVolumeExpansion:true
```

For more information about persistent volume claims, see PersistentVolumeClaims . 
### PodNodeSelector Feature state: Alpha since Kubernetes v1.5 
Type : Validating. 
This admission controller defaults and limits what node selectors may be used within a namespace by reading a namespace annotation and a global configuration. 
This admission controller is disabled by default. 
#### Configuration file format 
PodNodeSelectoruses a configuration file to set options for the behavior of the backend. Note that the configuration file format will move to a versioned file in a future release. This file may be json or yaml and has the following format: 
```
podNodeSelectorPluginConfig:clusterDefaultNodeSelector:name-of-node-selectornamespace1:name-of-node-selectornamespace2:name-of-node-selector
```

Reference the PodNodeSelectorconfiguration file from the file provided to the API server's command line flag --admission-control-config-file: 
```
apiVersion:apiserver.config.k8s.io/v1kind:AdmissionConfigurationplugins:- name:PodNodeSelectorpath:podnodeselector.yaml...
```

#### Configuration Annotation Format 
PodNodeSelectoruses the annotation key scheduler.alpha.kubernetes.io/node-selectorto assign node selectors to namespaces. 
```
apiVersion:v1kind:Namespacemetadata:annotations:scheduler.alpha.kubernetes.io/node-selector:name-of-node-selectorname:namespace3
```

#### Internal Behavior 
This admission controller has the following behavior: 
- If the Namespacehas an annotation with a key scheduler.alpha.kubernetes.io/node-selector, use its value as the node selector. - If the namespace lacks such an annotation, use the clusterDefaultNodeSelectordefined in the PodNodeSelectorplugin configuration file as the node selector. - Evaluate the pod's node selector against the namespace node selector for conflicts. Conflicts result in rejection. - Evaluate the pod's node selector against the namespace-specific allowed selector defined the plugin configuration file. Conflicts result in rejection. 
#### Note: PodNodeSelector allows forcing pods to run on specifically labeled nodes. Also see the PodTolerationRestriction admission plugin, which allows preventing pods from running on specifically tainted nodes. 
### PodSecurity Feature state: Stable since Kubernetes v1.25 
Type : Validating. 
The PodSecurity admission controller checks new Pods before they are admitted, determines if it should be admitted based on the requested security context and the restrictions on permitted Pod Security Standards for the namespace that the Pod would be in. 
See the Pod Security Admission documentation for more information. 
PodSecurity replaced an older admission controller named PodSecurityPolicy. 
### PodTolerationRestriction Feature state: Alpha since Kubernetes v1.7 
Type : Mutating and Validating. 
The PodTolerationRestriction admission controller verifies any conflict between tolerations of a pod and the tolerations of its namespace. It rejects the pod request if there is a conflict. It then merges the tolerations annotated on the namespace into the tolerations of the pod. The resulting tolerations are checked against a list of allowed tolerations annotated to the namespace. If the check succeeds, the pod request is admitted otherwise it is rejected. 
If the namespace of the pod does not have any associated default tolerations or allowed tolerations annotated, the cluster-level default tolerations or cluster-level list of allowed tolerations are used instead if they are specified. 
Tolerations to a namespace are assigned via the scheduler.alpha.kubernetes.io/defaultTolerationsannotation key. The list of allowed tolerations can be added via the scheduler.alpha.kubernetes.io/tolerationsWhitelistannotation key. 
Example for namespace annotations: 
```
apiVersion:v1kind:Namespacemetadata:name:apps-that-need-nodes-exclusivelyannotations:scheduler.alpha.kubernetes.io/defaultTolerations:'[{"operator": "Exists", "effect": "NoSchedule", "key": "dedicated-node"}]'scheduler.alpha.kubernetes.io/tolerationsWhitelist:'[{"operator": "Exists", "effect": "NoSchedule", "key": "dedicated-node"}]'
```

This admission controller is disabled by default. 
### PodTopologyLabels Feature state: Beta since Kubernetes v1.35; enabled by default 
Type : Mutating 
The PodTopologyLabels admission controller mutates the pods/bindingsubresources for all pods bound to a Node, adding topology labels matching those of the bound Node. This allows Node topology labels to be available as pod labels, which can be surfaced to running containers using the Downward API . The labels available as a result of this controller are the topology.kubernetes.io/region and topology.kubernetes.io/zone labels. 
#### Note: If any mutating admission webhook adds or modifies labels of the pods/bindingsubresource, these changes will propagate to pod labels as a result of this controller, overwriting labels with conflicting keys. 
This admission controller is enabled when the PodTopologyLabelsAdmissionfeature gate is enabled. 
### Priority 
Type : Mutating and Validating. 
The priority admission controller uses the priorityClassNamefield and populates the integer value of the priority. If the priority class is not found, the Pod is rejected. 
### ResourceQuota 
Type : Validating. 
This admission controller will observe the incoming request and ensure that it does not violate any of the constraints enumerated in the ResourceQuotaobject in a Namespace. If you are using ResourceQuotaobjects in your Kubernetes deployment, you MUST use this admission controller to enforce quota constraints. 
See the ResourceQuota API reference and the example of Resource Quota for more details. 
### RuntimeClass 
Type : Mutating and Validating. 
If you define a RuntimeClass with Pod overhead configured, this admission controller checks incoming Pods. When enabled, this admission controller rejects any Pod create requests that have the overhead already set. For Pods that have a RuntimeClass configured and selected in their .spec, this admission controller sets .spec.overheadin the Pod based on the value defined in the corresponding RuntimeClass. 
See also Pod Overhead for more information. 
### ServiceAccount 
Type : Mutating and Validating. 
This admission controller implements automation for serviceAccounts . The Kubernetes project strongly recommends enabling this admission controller. You should enable this admission controller if you intend to make any use of Kubernetes ServiceAccountobjects. 
To enhance the security measures around Secrets, use separate namespaces to isolate access to mounted secrets. 
### StorageObjectInUseProtection 
Type : Mutating. 
The StorageObjectInUseProtectionplugin adds the kubernetes.io/pvc-protectionor kubernetes.io/pv-protectionfinalizers to newly created Persistent Volume Claims (PVCs) or Persistent Volumes (PV). In case a user deletes a PVC or PV the PVC or PV is not removed until the finalizer is removed from the PVC or PV by PVC or PV Protection Controller. Refer to the Storage Object in Use Protection for more detailed information. 
### TaintNodesByCondition 
Type : Mutating. 
This admission controller taints newly created Nodes as NotReadyand NoSchedule. That tainting avoids a race condition that could cause Pods to be scheduled on new Nodes before their taints were updated to accurately reflect their reported conditions. 
### ValidatingAdmissionPolicy 
Type : Validating. 
This admission controller implements the CEL validation for incoming matched requests. It is enabled when both feature gate validatingadmissionpolicyand admissionregistration.k8s.io/v1alpha1group/version are enabled. If any of the ValidatingAdmissionPolicy fails, the request fails. 
### ValidatingAdmissionWebhook 
Type : Validating. 
This admission controller calls any validating webhooks which match the request. Matching webhooks are called in parallel; if any of them rejects the request, the request fails. This admission controller only runs in the validation phase; the webhooks it calls may not mutate the object, as opposed to the webhooks called by the MutatingAdmissionWebhookadmission controller. 
If a webhook called by this has side effects (for example, decrementing quota) it must have a reconciliation system, as it is not guaranteed that subsequent webhooks or other validating admission controllers will permit the request to finish. 
If you disable the ValidatingAdmissionWebhook, you must also disable the ValidatingWebhookConfigurationobject in the admissionregistration.k8s.io/v1group/version via the --runtime-configflag. 
## Is there a recommended set of admission controllers to use? 
Yes. The recommended admission controllers are enabled by default (shown here ), so you do not need to explicitly specify them. You can enable additional admission controllers beyond the default set using the --enable-admission-pluginsflag ( order doesn't matter ). 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified August 21, 2026 at 1:36 AM PST: Fix misspelled topology.kubernetes.io/zone label name (e0b7a21889) 
- - - - - - 

- - - - 

### 📄 Source: [https://kubernetes.io/docs/reference/access-authn-authz/rbac/](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - Français (French)   - Bahasa Indonesia (Indonesian)   - 日本語 (Japanese)   - বাংলা (Bengali)   - Deutsch (German)   - हिन्दी (Hindi)   - Italiano (Italian)   - 한국어 (Korean)   - فارسی (Persian)   - Polski (Polish)   - Português (Portuguese)   - Русский (Russian)   - Español (Spanish)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# Using RBAC Authorization 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- 
  -   -   -   -   - - 
  -   -   -   -   -   - - 
  -   - - 
  -   -   -   -   - - - - 
  -   - 
- - - - 
# Using RBAC Authorization 
Role-based access control (RBAC) is a method of regulating access to computer or network resources based on the roles of individual users within your organization. 
RBAC authorization uses the rbac.authorization.k8s.ioAPI group to drive authorization decisions, allowing you to dynamically configure policies through the Kubernetes API. 
To enable RBAC, start the API server with the --authorization-configflag set to a file that includes the RBACauthorizer; for example: 
```
apiVersion:apiserver.config.k8s.io/v1kind:AuthorizationConfigurationauthorizers:...- type:RBAC...
```

Or, start the API server with the --authorization-modeflag set to a comma-separated list that includes RBAC; for example: 
```
kube-apiserver --authorization-mode=...,RBAC --other-options --more-options

```

## API objects 
The RBAC API declares four kinds of Kubernetes object: Role , ClusterRole , RoleBinding and ClusterRoleBinding . You can describe or amend the RBAC objects using tools such as kubectl, just like any other Kubernetes object. 
#### Caution: These objects, by design, impose access restrictions. If you are making changes to a cluster as you learn, see privilege escalation prevention and bootstrapping to understand how those restrictions can prevent you making some changes. 
### Role and ClusterRole 
An RBAC Role or ClusterRole contains rules that represent a set of permissions. Permissions are purely additive (there are no "deny" rules). 
A Role always sets permissions within a particular namespace ; when you create a Role, you have to specify the namespace it belongs in. 
ClusterRole, by contrast, is a non-namespaced resource. The resources have different names (Role and ClusterRole) because a Kubernetes object always has to be either namespaced or not namespaced; it can't be both. 
ClusterRoles have several uses. You can use a ClusterRole to: 
- define permissions on namespaced resources and be granted access within individual namespace(s) - define permissions on namespaced resources and be granted access across all namespaces - define permissions on cluster-scoped resources 
If you want to define a role within a namespace, use a Role; if you want to define a role cluster-wide, use a ClusterRole. 
#### Role example 
Here's an example Role in the "default" namespace that can be used to grant read access to pods : access/simple-role.yaml
```
apiVersion:rbac.authorization.k8s.io/v1kind:Rolemetadata:namespace:defaultname:pod-readerrules:- apiGroups:[""]# "" indicates the core API groupresources:["pods"]verbs:["get","watch","list"]
```

#### ClusterRole example 
A ClusterRole can be used to grant the same permissions as a Role. Because ClusterRoles are cluster-scoped, you can also use them to grant access to: 
- 
cluster-scoped resources (like nodes ) - 
non-resource endpoints (like /healthz) - 
namespaced resources (like Pods), across all namespaces 
For example: you can use a ClusterRole to allow a particular user to run kubectl get pods --all-namespaces
Here is an example of a ClusterRole that can be used to grant read access to secrets in any particular namespace, or across all namespaces (depending on how it is bound ): access/simple-clusterrole.yaml
```
apiVersion:rbac.authorization.k8s.io/v1kind:ClusterRolemetadata:# "namespace" omitted since ClusterRoles are not namespacedname:secret-readerrules:- apiGroups:[""]## at the HTTP level, the name of the resource for accessing Secret# objects is "secrets"resources:["secrets"]verbs:["get","watch","list"]
```

The name of a Role or a ClusterRole object must be a valid path segment name . 
### RoleBinding and ClusterRoleBinding 
A role binding grants the permissions defined in a role to a user or set of users. It holds a list of subjects (users, groups, or service accounts), and a reference to the role being granted. A RoleBinding grants permissions within a specific namespace whereas a ClusterRoleBinding grants that access cluster-wide. 
A RoleBinding may reference any Role in the same namespace. Alternatively, a RoleBinding can reference a ClusterRole and bind that ClusterRole to the namespace of the RoleBinding. If you want to bind a ClusterRole to all the namespaces in your cluster, you use a ClusterRoleBinding. 
The name of a RoleBinding or ClusterRoleBinding object must be a valid path segment name . 
#### RoleBinding examples 
Here is an example of a RoleBinding that grants the "pod-reader" Role to the user "jane" within the "default" namespace. This allows "jane" to read pods in the "default" namespace. access/simple-rolebinding-with-role.yaml
```
apiVersion:rbac.authorization.k8s.io/v1# This role binding allows "jane" to read pods in the "default" namespace.# You need to already have a Role named "pod-reader" in that namespace.kind:RoleBindingmetadata:name:read-podsnamespace:defaultsubjects:# You can specify more than one "subject"- kind:Username:jane# "name" is case sensitiveapiGroup:rbac.authorization.k8s.ioroleRef:# "roleRef" specifies the binding to a Role / ClusterRolekind:Role#this must be Role or ClusterRolename:pod-reader# this must match the name of the Role or ClusterRole you wish to bind toapiGroup:rbac.authorization.k8s.io
```

A RoleBinding can also reference a ClusterRole to grant the permissions defined in that ClusterRole to resources inside the RoleBinding's namespace. This kind of reference lets you define a set of common roles across your cluster, then reuse them within multiple namespaces. 
For instance, even though the following RoleBinding refers to a ClusterRole, "dave" (the subject, case sensitive) will only be able to read Secrets in the "development" namespace, because the RoleBinding's namespace (in its metadata) is "development". access/simple-rolebinding-with-clusterrole.yaml
```
apiVersion:rbac.authorization.k8s.io/v1# This role binding allows "dave" to read secrets in the "development" namespace.# You need to already have a ClusterRole named "secret-reader".kind:RoleBindingmetadata:name:read-secrets## The namespace of the RoleBinding determines where the permissions are granted.# This only grants permissions within the "development" namespace.namespace:developmentsubjects:- kind:Username:dave# Name is case sensitiveapiGroup:rbac.authorization.k8s.ioroleRef:kind:ClusterRolename:secret-readerapiGroup:rbac.authorization.k8s.io
```

#### ClusterRoleBinding example 
To grant permissions across a whole cluster, you can use a ClusterRoleBinding. The following ClusterRoleBinding allows any user in the group "manager" to read secrets in any namespace. access/simple-clusterrolebinding.yaml
```
apiVersion:rbac.authorization.k8s.io/v1# This cluster role binding allows anyone in the "manager" group to read secrets in any namespace.kind:ClusterRoleBindingmetadata:name:read-secrets-globalsubjects:- kind:Groupname:manager# Name is case sensitiveapiGroup:rbac.authorization.k8s.ioroleRef:kind:ClusterRolename:secret-readerapiGroup:rbac.authorization.k8s.io
```

After you create a binding, you cannot change the Role or ClusterRole that it refers to. If you try to change a binding's roleRef, you get a validation error. If you do want to change the roleReffor a binding, you need to remove the binding object and create a replacement. 
There are two reasons for this restriction: 
- Making roleRefimmutable allows granting someone updatepermission on an existing binding object, so that they can manage the list of subjects, without being able to change the role that is granted to those subjects. - A binding to a different role is a fundamentally different binding. Requiring a binding to be deleted/recreated in order to change the roleRefensures the full list of subjects in the binding is intended to be granted the new role (as opposed to enabling or accidentally modifying only the roleRef without verifying all of the existing subjects should be given the new role's permissions). 
The kubectl auth reconcilecommand-line utility creates or updates a manifest file containing RBAC objects, and handles deleting and recreating binding objects if required to change the role they refer to. See command usage and examples for more information. 
### Referring to resources 
In the Kubernetes API, most resources are represented and accessed using a string representation of their object name, such as podsfor a Pod. RBAC refers to resources using exactly the same name that appears in the URL for the relevant API endpoint. Some Kubernetes APIs involve a subresource , such as the logs for a Pod. A request for a Pod's logs looks like: 
```
GET /api/v1/namespaces/{namespace}/pods/{name}/log

```

In this case, podsis the namespaced resource for Pod resources, and logis a subresource of pods. To represent this in an RBAC role, use a slash ( /) to delimit the resource and subresource. To allow a subject to read podsand also access the logsubresource for each of those Pods, you write: 
```
apiVersion:rbac.authorization.k8s.io/v1kind:Rolemetadata:namespace:defaultname:pod-and-pod-logs-readerrules:- apiGroups:[""]resources:["pods","pods/log"]verbs:["get","list"]
```

You can also refer to resources by name for certain requests through the resourceNameslist. When specified, requests can be restricted to individual instances of a resource. Here is an example that restricts its subject to only getor updatea ConfigMap named my-configmap: 
```
apiVersion:rbac.authorization.k8s.io/v1kind:Rolemetadata:namespace:defaultname:configmap-updaterrules:- apiGroups:[""]## at the HTTP level, the name of the resource for accessing ConfigMap# objects is "configmaps"resources:["configmaps"]resourceNames:["my-configmap"]verbs:["update","get"]
```

#### Note: You cannot restrict deletecollection or top-level create requests by resource name. For create , this limitation is because the name of the new object may not be known at authorization time. However, the create limitation applies only to top-level resources, not subresources. For example, you can use the resourceNamesfield with pods/exec. If you restrict list or watch by resourceName, clients must include a metadata.namefield selector in their list or watch request (that matches the specified resourceName) in order to be authorized. For example: kubectl get configmaps --field-selector=metadata.name=my-configmap
Rather than referring to individual resources, apiGroups, and verbs, you can use the wildcard *symbol to refer to all such objects. For nonResourceURLs, you can use the wildcard *as a suffix glob match. For resourceNames, an empty set means that everything is allowed. Here is an example that allows access to perform any current and future action on all current and future resources in the example.comAPI group. This is similar to the built-in cluster-adminrole. 
```
apiVersion:rbac.authorization.k8s.io/v1kind:Rolemetadata:namespace:defaultname:example.com-superuser# DO NOT USE THIS ROLE, IT IS JUST AN EXAMPLErules:- apiGroups:["example.com"]resources:["*"]verbs:["*"]
```

#### Caution: Using wildcards in resource and verb entries could result in overly permissive access being granted to sensitive resources. For instance, if a new resource type is added, or a new subresource is added, or a new custom verb is checked, the wildcard entry automatically grants access, which may be undesirable. The principle of least privilege should be employed, using specific resources and verbs to ensure only the permissions required for the workload to function correctly are applied. 
### Aggregated ClusterRoles 
You can aggregate several ClusterRoles into one combined ClusterRole. A controller, running as part of the cluster control plane, watches for ClusterRole objects with an aggregationRuleset. The aggregationRuledefines a label selector that the controller uses to match other ClusterRole objects that should be combined into the rulesfield of this one. 
#### Caution: 
The control plane overwrites any values that you manually specify in the rulesfield of an aggregate ClusterRole. If you want to change or add rules, do so in the ClusterRoleobjects that are selected by the aggregationRule. 
Omit the rulesfield from manifests for aggregated ClusterRoles. Setting it, even to an empty list, claims ownership of the field when the manifest is applied with server-side apply . That ownership causes conflicts between the applier and the control plane: subsequent applies either fail with a field manager conflict on .rules, or (if conflicts are forced, as GitOps controllers typically do) repeatedly clear the aggregated rules, which the control plane then fills in again. 
Here is an example aggregated ClusterRole: 
```
apiVersion:rbac.authorization.k8s.io/v1kind:ClusterRolemetadata:name:monitoringaggregationRule:clusterRoleSelectors:- matchLabels:rbac.example.com/aggregate-to-monitoring:"true"# The control plane automatically fills in the rules
```

If you create a new ClusterRole that matches the label selector of an existing aggregated ClusterRole, that change triggers adding the new rules into the aggregated ClusterRole. Here is an example that adds rules to the "monitoring" ClusterRole, by creating another ClusterRole labeled rbac.example.com/aggregate-to-monitoring: true. 
```
apiVersion:rbac.authorization.k8s.io/v1kind:ClusterRolemetadata:name:monitoring-endpointsliceslabels:rbac.example.com/aggregate-to-monitoring:"true"# When you create the "monitoring-endpointslices" ClusterRole,# the rules below will be added to the "monitoring" ClusterRole.rules:- apiGroups:[""]resources:["services","pods"]verbs:["get","list","watch"]- apiGroups:["discovery.k8s.io"]resources:["endpointslices"]verbs:["get","list","watch"]
```

The default user-facing roles use ClusterRole aggregation. This lets you, as a cluster administrator, include rules for custom resources, such as those served by CustomResourceDefinitions or aggregated API servers, to extend the default roles. 
For example: the following ClusterRoles let the "admin" and "edit" default roles manage the custom resource named CronTab, whereas the "view" role can perform only read actions on CronTab resources. You can assume that CronTab objects are named "crontabs"in URLs as seen by the API server. 
```
apiVersion:rbac.authorization.k8s.io/v1kind:ClusterRolemetadata:name:aggregate-cron-tabs-editlabels:# Add these permissions to the "admin" and "edit" default roles.rbac.authorization.k8s.io/aggregate-to-admin:"true"rbac.authorization.k8s.io/aggregate-to-edit:"true"rules:- apiGroups:["stable.example.com"]resources:["crontabs"]verbs:["get","list","watch","create","update","patch","delete"]---kind:ClusterRoleapiVersion:rbac.authorization.k8s.io/v1metadata:name:aggregate-cron-tabs-viewlabels:# Add these permissions to the "view" default role.rbac.authorization.k8s.io/aggregate-to-view:"true"rules:- apiGroups:["stable.example.com"]resources:["crontabs"]verbs:["get","list","watch"]
```

#### Role examples 
The following examples are excerpts from Role or ClusterRole objects, showing only the rulessection. 
Allow reading "pods"resources in the core API Group : 
```
rules:- apiGroups:[""]## at the HTTP level, the name of the resource for accessing Pod# objects is "pods"resources:["pods"]verbs:["get","list","watch"]
```

Allow reading/writing Deployments (at the HTTP level: objects with "deployments"in the resource part of their URL) in the "apps"API groups: 
```
rules:- apiGroups:["apps"]## at the HTTP level, the name of the resource for accessing Deployment# objects is "deployments"resources:["deployments"]verbs:["get","list","watch","create","update","patch","delete"]
```

Allow reading Pods in the core API group, as well as reading or writing Job resources in the "batch"API group: 
```
rules:- apiGroups:[""]## at the HTTP level, the name of the resource for accessing Pod# objects is "pods"resources:["pods"]verbs:["get","list","watch"]- apiGroups:["batch"]## at the HTTP level, the name of the resource for accessing Job# objects is "jobs"resources:["jobs"]verbs:["get","list","watch","create","update","patch","delete"]
```

Allow reading a ConfigMap named "my-config" (must be bound with a RoleBinding to limit to a single ConfigMap in a single namespace): 
```
rules:- apiGroups:[""]## at the HTTP level, the name of the resource for accessing ConfigMap# objects is "configmaps"resources:["configmaps"]resourceNames:["my-config"]verbs:["get"]
```

Allow reading the resource "nodes"in the core group (because a Node is cluster-scoped, this must be in a ClusterRole bound with a ClusterRoleBinding to be effective): 
```
rules:- apiGroups:[""]## at the HTTP level, the name of the resource for accessing Node# objects is "nodes"resources:["nodes"]verbs:["get","list","watch"]
```

Allow GET and POST requests to the non-resource endpoint /healthzand all subpaths (must be in a ClusterRole bound with a ClusterRoleBinding to be effective): 
```
rules:- nonResourceURLs:["/healthz","/healthz/*"]# '*' in a nonResourceURL is a suffix glob matchverbs:["get","post"]
```

### Referring to subjects 
A RoleBinding or ClusterRoleBinding binds a role to subjects. Subjects can be groups, users or ServiceAccounts . 
Kubernetes represents usernames as strings. These can be: plain names, such as "alice"; email-style names, like "bob@example.com"; or numeric user IDs represented as a string. It is up to you as a cluster administrator to configure the authentication modules so that authentication produces usernames in the format you want. 
#### Caution: The prefix system:is reserved for Kubernetes system use, so you should ensure that you don't have users or groups with names that start with system:by accident. Other than this special prefix, the RBAC authorization system does not require any format for usernames. 
In Kubernetes, Authenticator modules provide group information. Groups, like users, are represented as strings, and that string has no format requirements, other than that the prefix system:is reserved. 
ServiceAccounts have names prefixed with system:serviceaccount:, and belong to groups that have names prefixed with system:serviceaccounts:. 
#### Note: 
- system:serviceaccount:(singular) is the prefix for service account usernames. - system:serviceaccounts:(plural) is the prefix for service account groups. 
#### RoleBinding examples 
The following examples are RoleBindingexcerpts that only show the subjectssection. 
For a user named alice@example.com: 
```
subjects:- kind:Username:"alice@example.com"apiGroup:rbac.authorization.k8s.io
```

For a group named frontend-admins: 
```
subjects:- kind:Groupname:"frontend-admins"apiGroup:rbac.authorization.k8s.io
```

For the default service account in the "kube-system" namespace: 
```
subjects:- kind:ServiceAccountname:defaultnamespace:kube-system
```

For all service accounts in the "qa" namespace: 
```
subjects:- kind:Groupname:system:serviceaccounts:qaapiGroup:rbac.authorization.k8s.io
```

For all service accounts in any namespace: 
```
subjects:- kind:Groupname:system:serviceaccountsapiGroup:rbac.authorization.k8s.io
```

For all authenticated users: 
```
subjects:- kind:Groupname:system:authenticatedapiGroup:rbac.authorization.k8s.io
```

For all unauthenticated users: 
```
subjects:- kind:Groupname:system:unauthenticatedapiGroup:rbac.authorization.k8s.io
```

For all users: 
```
subjects:- kind:Groupname:system:authenticatedapiGroup:rbac.authorization.k8s.io- kind:Groupname:system:unauthenticatedapiGroup:rbac.authorization.k8s.io
```

## Default roles and role bindings 
API servers create a set of default ClusterRole and ClusterRoleBinding objects. Many of these are system:prefixed, which indicates that the resource is directly managed by the cluster control plane. All of the default ClusterRoles and ClusterRoleBindings are labeled with kubernetes.io/bootstrapping=rbac-defaults. 
#### Caution: Take care when modifying ClusterRoles and ClusterRoleBindings with names that have a system:prefix. Modifications to these resources can result in non-functional clusters. 
### Auto-reconciliation 
At each start-up, the API server updates default cluster roles with any missing permissions, and updates default cluster role bindings with any missing subjects. This allows the cluster to repair accidental modifications, and helps to keep roles and role bindings up-to-date as permissions and subjects change in new Kubernetes releases. 
To opt out of this reconciliation, set the rbac.authorization.kubernetes.io/autoupdateannotation on a default cluster role or default cluster RoleBinding to false. Be aware that missing default permissions and subjects can result in non-functional clusters. 
Auto-reconciliation is enabled by default if the RBAC authorizer is active. 
### API discovery roles 
Default cluster role bindings authorize unauthenticated and authenticated users to read API information that is deemed safe to be publicly accessible (including CustomResourceDefinitions). To disable anonymous unauthenticated access, add --anonymous-auth=falseflag to the API server configuration. 
To view the configuration of these roles via kubectlrun: 
```
kubectl get clusterroles system:discovery -o yaml

```

#### Note: If you edit that ClusterRole, your changes will be overwritten on API server restart via auto-reconciliation . To avoid that overwriting, either do not manually edit the role, or disable auto-reconciliation. Kubernetes RBAC API discovery roles 
|  Default ClusterRole  | Default ClusterRoleBinding  | Description  |
|  system:basic-user  | system:authenticated group  | Allows a user read-only access to basic information about themselves. Prior to v1.14, this role was also bound to system:unauthenticated by default.  |
|  system:discovery  | system:authenticated group  | Allows read-only access to API discovery endpoints needed to discover and negotiate an API level. Prior to v1.14, this role was also bound to system:unauthenticated by default.  |
|  system:public-info-viewer  | system:authenticated and system:unauthenticated groups  | Allows read-only access to non-sensitive information about the cluster. Introduced in Kubernetes v1.14.  |
### User-facing roles 
Some of the default ClusterRoles are not system:prefixed. These are intended to be user-facing roles. They include super-user roles ( cluster-admin), roles intended to be granted cluster-wide using ClusterRoleBindings, and roles intended to be granted within particular namespaces using RoleBindings ( admin, edit, view). 
User-facing ClusterRoles use ClusterRole aggregation to allow admins to include rules for custom resources on these ClusterRoles. To add rules to the admin, edit, or viewroles, create a ClusterRole with one or more of the following labels: 
```
metadata:labels:rbac.authorization.k8s.io/aggregate-to-admin:"true"rbac.authorization.k8s.io/aggregate-to-edit:"true"rbac.authorization.k8s.io/aggregate-to-view:"true"
```

|  Default ClusterRole  | Default ClusterRoleBinding  | Description  |
|  cluster-admin  | system:masters group  | Allows super-user access to perform any action on any resource. When used in a ClusterRoleBinding , it gives full control over every resource in the cluster and in all namespaces. When used in a RoleBinding , it gives full control over every resource in the role binding's namespace, including the namespace itself.  |
|  admin  | None  | Allows admin access, intended to be granted within a namespace using a RoleBinding . 
If used in a RoleBinding , allows read/write access to most resources in a namespace, including the ability to create roles and role bindings within the namespace. This role does not allow write access to resource quota or to the namespace itself. This role also does not allow write access to EndpointSlices in clusters created using Kubernetes v1.22+. More information is available in the "Write Access for EndpointSlices" section .  |
|  edit  | None  | Allows read/write access to most objects in a namespace. 
This role does not allow viewing or modifying roles or role bindings. However, this role allows accessing Secrets and running Pods as any ServiceAccount in the namespace, so it can be used to gain the API access levels of any ServiceAccount in the namespace. This role also does not allow write access to EndpointSlices in clusters created using Kubernetes v1.22+. More information is available in the "Write Access for EndpointSlices" section .  |
|  view  | None  | Allows read-only access to see most objects in a namespace. It does not allow viewing roles or role bindings. 
This role does not allow viewing Secrets, since reading the contents of Secrets enables access to ServiceAccount credentials in the namespace, which would allow API access as any ServiceAccount in the namespace (a form of privilege escalation).  |
### Core component roles 
|  Default ClusterRole  | Default ClusterRoleBinding  | Description  |
|  system:kube-scheduler  | system:kube-scheduler user  | Allows access to the resources required by the scheduler component.  |
|  system:volume-scheduler  | system:kube-scheduler user  | Allows access to the volume resources required by the kube-scheduler component.  |
|  system:kube-controller-manager  | system:kube-controller-manager user  | Allows access to the resources required by the controller manager component. The permissions required by individual controllers are detailed in the controller roles .  |
|  system:node  | None  | Allows access to resources required by the kubelet, including read access to all secrets, and write access to all pod status objects . 
You should use the Node authorizer and NodeRestriction admission plugin instead of the system:node role, and allow granting API access to kubelets based on the Pods scheduled to run on them. 
The system:node role only exists for compatibility with Kubernetes clusters upgraded from versions prior to v1.8.  |
|  system:node-proxier  | system:kube-proxy user  | Allows access to the resources required by the kube-proxy component.  |
### Other component roles 
|  Default ClusterRole  | Default ClusterRoleBinding  | Description  |
|  system:auth-delegator  | None  | Allows delegated authentication and authorization checks. This is commonly used by add-on API servers for unified authentication and authorization.  |
|  system:heapster  | None  | Role for the Heapster component (deprecated).  |
|  system:kube-aggregator  | None  | Role for the kube-aggregator component.  |
|  system:kube-dns  | kube-dns service account in the kube-system namespace  | Role for the deprecated kube-dns component. ( CoreDNS does not use this role.)  |
|  system:kubelet-api-admin  | None  | Allows full access to the kubelet API.  |
|  system:node-bootstrapper  | None  | Allows access to the resources required to perform kubelet TLS bootstrapping .  |
|  system:node-problem-detector  | None  | Role for the node-problem-detector component.  |
|  system:persistent-volume-provisioner  | None  | Allows access to the resources required by most dynamic volume provisioners .  |
|  system:monitoring  | system:monitoring group  | Allows read access to control-plane monitoring endpoints (i.e. kube-apiserver liveness and readiness endpoints ( /healthz , /livez , /readyz ), the individual health-check endpoints ( /healthz/* , /livez/* , /readyz/* ), /metrics ), and causes the kube-apiserver to respect the traceparent header provided with requests for tracing. Note that individual health check endpoints and the metric endpoint may expose sensitive information.  |
### Roles for built-in controllers 
The Kubernetes controller manager runs controllers that are built in to the Kubernetes control plane. When invoked with --use-service-account-credentials, kube-controller-manager starts each controller using a separate service account. Corresponding roles exist for each built-in controller, prefixed with system:controller:. If the controller manager is not started with --use-service-account-credentials, it runs all control loops using its own credential, which must be granted all the relevant roles. These roles include: 
- system:controller:attachdetach-controller- system:controller:certificate-controller- system:controller:clusterrole-aggregation-controller- system:controller:cronjob-controller- system:controller:daemon-set-controller- system:controller:deployment-controller- system:controller:disruption-controller- system:controller:endpoint-controller- system:controller:expand-controller- system:controller:generic-garbage-collector- system:controller:horizontal-pod-autoscaler- system:controller:job-controller- system:controller:namespace-controller- system:controller:node-controller- system:controller:persistent-volume-binder- system:controller:pod-garbage-collector- system:controller:pv-protection-controller- system:controller:pvc-protection-controller- system:controller:replicaset-controller- system:controller:replication-controller- system:controller:resourcequota-controller- system:controller:root-ca-cert-publisher- system:controller:route-controller- system:controller:service-account-controller- system:controller:service-controller- system:controller:statefulset-controller- system:controller:ttl-controller
## Privilege escalation prevention and bootstrapping 
The RBAC API prevents users from escalating privileges by editing roles or role bindings. Because this is enforced at the API level, it applies even when the RBAC authorizer is not in use. 
### Restrictions on role creation or update 
You can only create/update a role if at least one of the following things is true: 
- You already have all the permissions contained in the role, at the same scope as the object being modified (cluster-wide for a ClusterRole, within the same namespace or cluster-wide for a Role). - You are granted explicit permission to perform the escalateverb on the rolesor clusterrolesresource in the rbac.authorization.k8s.ioAPI group. 
For example, if user-1does not have the ability to list Secrets cluster-wide, they cannot create a ClusterRole containing that permission. To allow a user to create/update roles: 
- Grant them a role that allows them to create/update Role or ClusterRole objects, as desired. - Grant them permission to include specific permissions in the roles they create/update: 
  - implicitly, by giving them those permissions (if they attempt to create or modify a Role or ClusterRole with permissions they themselves have not been granted, the API request will be forbidden)   - or explicitly allow specifying any permission in a Roleor ClusterRoleby giving them permission to perform the escalateverb on rolesor clusterrolesresources in the rbac.authorization.k8s.ioAPI group 
### Restrictions on role binding creation or update 
You can only create/update a role binding if you already have all the permissions contained in the referenced role (at the same scope as the role binding) or if you have been authorized to perform the bindverb on the referenced role. For example, if user-1does not have the ability to list Secrets cluster-wide, they cannot create a ClusterRoleBinding to a role that grants that permission. To allow a user to create/update role bindings: 
- Grant them a role that allows them to create/update RoleBinding or ClusterRoleBinding objects, as desired. - Grant them permissions needed to bind a particular role: 
  - implicitly, by giving them the permissions contained in the role.   - explicitly, by giving them permission to perform the bindverb on the particular Role (or ClusterRole). 
For example, this ClusterRole and RoleBinding would allow user-1to grant other users the admin, edit, and viewroles in the namespace user-1-namespace: 
```
apiVersion:rbac.authorization.k8s.io/v1kind:ClusterRolemetadata:name:role-grantorrules:- apiGroups:["rbac.authorization.k8s.io"]resources:["rolebindings"]verbs:["create"]- apiGroups:["rbac.authorization.k8s.io"]resources:["clusterroles"]verbs:["bind"]# omit resourceNames to allow binding any ClusterRoleresourceNames:["admin","edit","view"]---apiVersion:rbac.authorization.k8s.io/v1kind:RoleBindingmetadata:name:role-grantor-bindingnamespace:user-1-namespaceroleRef:apiGroup:rbac.authorization.k8s.iokind:ClusterRolename:role-grantorsubjects:- apiGroup:rbac.authorization.k8s.iokind:Username:user-1
```

When bootstrapping the first roles and role bindings, it is necessary for the initial user to grant permissions they do not yet have. To bootstrap initial roles and role bindings: 
- Use a credential with the "system:masters" group, which is bound to the "cluster-admin" super-user role by the default bindings. 
## Command-line utilities 
### kubectl create role
Creates a Role object defining permissions within a single namespace. Examples: 
- 
Create a Role named "pod-reader" that allows users to perform get, watchand liston pods: 
```
kubectl create role pod-reader --verb=get --verb=list --verb=watch --resource=pods

```
- 
Create a Role named "pod-reader" with resourceNames specified: 
```
kubectl create role pod-reader --verb=get --resource=pods --resource-name=readablepod --resource-name=anotherpod

```
- 
Create a Role named "foo" with apiGroups specified: 
```
kubectl create role foo --verb=get,list,watch --resource=replicasets.apps

```
- 
Create a Role named "foo" with subresource permissions: 
```
kubectl create role foo --verb=get,list,watch --resource=pods,pods/status

```
- 
Create a Role named "my-component-lease-holder" with permissions to get/update a resource with a specific name: 
```
kubectl create role my-component-lease-holder --verb=get,list,watch,update --resource=lease --resource-name=my-component

```

### kubectl create clusterrole
Creates a ClusterRole. Examples: 
- 
Create a ClusterRole named "pod-reader" that allows user to perform get, watchand liston pods: 
```
kubectl create clusterrole pod-reader --verb=get,list,watch --resource=pods

```
- 
Create a ClusterRole named "pod-reader" with resourceNames specified: 
```
kubectl create clusterrole pod-reader --verb=get --resource=pods --resource-name=readablepod --resource-name=anotherpod

```
- 
Create a ClusterRole named "foo" with apiGroups specified: 
```
kubectl create clusterrole foo --verb=get,list,watch --resource=replicasets.apps

```
- 
Create a ClusterRole named "foo" with subresource permissions: 
```
kubectl create clusterrole foo --verb=get,list,watch --resource=pods,pods/status

```
- 
Create a ClusterRole named "foo" with nonResourceURL specified: 
```
kubectl create clusterrole "foo" --verb=get --non-resource-url=/logs/*

```
- 
Create a ClusterRole named "monitoring" with an aggregationRule specified: 
```
kubectl create clusterrole monitoring --aggregation-rule="rbac.example.com/aggregate-to-monitoring=true"
```

### kubectl create rolebinding
Grants a Role or ClusterRole within a specific namespace. Examples: 
- 
Within the namespace "acme", grant the permissions in the "admin" ClusterRole to a user named "bob": 
```
kubectl create rolebinding bob-admin-binding --clusterrole=admin --user=bob --namespace=acme

```
- 
Within the namespace "acme", grant the permissions in the "view" ClusterRole to the service account in the namespace "acme" named "myapp": 
```
kubectl create rolebinding myapp-view-binding --clusterrole=view --serviceaccount=acme:myapp --namespace=acme

```
- 
Within the namespace "acme", grant the permissions in the "view" ClusterRole to a service account in the namespace "myappnamespace" named "myapp": 
```
kubectl create rolebinding myappnamespace-myapp-view-binding --clusterrole=view --serviceaccount=myappnamespace:myapp --namespace=acme

```

### kubectl create clusterrolebinding
Grants a ClusterRole across the entire cluster (all namespaces). Examples: 
- 
Across the entire cluster, grant the permissions in the "cluster-admin" ClusterRole to a user named "root": 
```
kubectl create clusterrolebinding root-cluster-admin-binding --clusterrole=cluster-admin --user=root

```
- 
Across the entire cluster, grant the permissions in the "system:node-proxier" ClusterRole to a user named "system:kube-proxy": 
```
kubectl create clusterrolebinding kube-proxy-binding --clusterrole=system:node-proxier --user=system:kube-proxy

```
- 
Across the entire cluster, grant the permissions in the "view" ClusterRole to a service account named "myapp" in the namespace "acme": 
```
kubectl create clusterrolebinding myapp-view-binding --clusterrole=view --serviceaccount=acme:myapp

```

### kubectl auth reconcile
Creates or updates rbac.authorization.k8s.io/v1API objects from a manifest file. 
Missing objects are created, and the containing namespace is created for namespaced objects, if required. 
Existing roles are updated to include the permissions in the input objects, and remove extra permissions if --remove-extra-permissionsis specified. 
Existing bindings are updated to include the subjects in the input objects, and remove extra subjects if --remove-extra-subjectsis specified. 
Examples: 
- 
Test applying a manifest file of RBAC objects, displaying changes that would be made: 
```
kubectl auth reconcile -f my-rbac-rules.yaml --dry-run=client

```
- 
Apply a manifest file of RBAC objects, preserving any extra permissions (in roles) and any extra subjects (in bindings): 
```
kubectl auth reconcile -f my-rbac-rules.yaml

```
- 
Apply a manifest file of RBAC objects, removing any extra permissions (in roles) and any extra subjects (in bindings): 
```
kubectl auth reconcile -f my-rbac-rules.yaml --remove-extra-subjects --remove-extra-permissions

```

## ServiceAccount permissions 
Default RBAC policies grant scoped permissions to control-plane components, nodes, and controllers, but grant no permissions to service accounts outside the kube-systemnamespace (beyond the permissions given by API discovery roles ). 
This allows you to grant particular roles to particular ServiceAccounts as needed. Fine-grained role bindings provide greater security, but require more effort to administrate. Broader grants can give unnecessary (and potentially escalating) API access to ServiceAccounts, but are easier to administrate. 
In order from most secure to least secure, the approaches are: 
- 
Grant a role to an application-specific service account (best practice) 
This requires the application to specify a serviceAccountNamein its pod spec, and for the service account to be created (via the API, application manifest, kubectl create serviceaccount, etc.). 
For example, grant read-only permission within "my-namespace" to the "my-sa" service account: 
```
kubectl create rolebinding my-sa-view \
  --clusterrole=view \
  --serviceaccount=my-namespace:my-sa \
  --namespace=my-namespace

```
- 
Grant a role to the "default" service account in a namespace 
If an application does not specify a serviceAccountName, it uses the "default" service account. 
#### Note: Permissions given to the "default" service account are available to any pod in the namespace that does not specify a serviceAccountName. 
For example, grant read-only permission within "my-namespace" to the "default" service account: 
```
kubectl create rolebinding default-view \
  --clusterrole=view \
  --serviceaccount=my-namespace:default \
  --namespace=my-namespace

```
- 
Grant a role to all service accounts in a namespace 
If you want all applications in a namespace to have a role, no matter what service account they use, you can grant a role to the service account group for that namespace. 
For example, grant read-only permission within "my-namespace" to all service accounts in that namespace: 
```
kubectl create rolebinding serviceaccounts-view \
  --clusterrole=view \
  --group=system:serviceaccounts:my-namespace \
  --namespace=my-namespace

```
- 
Grant a limited role to all service accounts cluster-wide (discouraged) 
If you don't want to manage permissions per-namespace, you can grant a cluster-wide role to all service accounts. 
For example, grant read-only permission across all namespaces to all service accounts in the cluster: 
```
kubectl create clusterrolebinding serviceaccounts-view \
  --clusterrole=view \
 --group=system:serviceaccounts

```
- 
Grant super-user access to all service accounts cluster-wide (strongly discouraged) 
If you don't care about partitioning permissions at all, you can grant super-user access to all service accounts. 
#### Warning: This allows any application full access to your cluster, and also grants any user with read access to Secrets (or the ability to create any pod) full access to your cluster. 
```
kubectl create clusterrolebinding serviceaccounts-cluster-admin \
  --clusterrole=cluster-admin \
  --group=system:serviceaccounts

```

## Write access for EndpointSlices 
Kubernetes clusters created before Kubernetes v1.22 include write access to EndpointSlices (and the now-deprecated Endpoints API) in the aggregated "edit" and "admin" roles. As a mitigation for CVE-2021-25740 , this access is not part of the aggregated roles in clusters that you create using Kubernetes v1.22 or later. 
Existing clusters that have been upgraded to Kubernetes v1.22 will not be subject to this change. The CVE announcement includes guidance for restricting this access in existing clusters. 
If you want new clusters to retain this level of access in the aggregated roles, you can create the following ClusterRole: access/endpoints-aggregated.yaml
```
apiVersion:rbac.authorization.k8s.io/v1kind:ClusterRolemetadata:annotations:kubernetes.io/description:|-      Add endpoints write permissions to the edit and admin roles. This was
      removed by default in 1.22 because of CVE-2021-25740. See
      https://issue.k8s.io/103675. This can allow writers to direct LoadBalancer
      or Ingress implementations to expose backend IPs that would not otherwise
      be accessible, and can circumvent network policies or security controls
      intended to prevent/isolate access to those backends.
      EndpointSlices were never included in the edit or admin roles, so there
      is nothing to restore for the EndpointSlice API.labels:rbac.authorization.k8s.io/aggregate-to-edit:"true"name:custom:aggregate-to-edit:endpoints# you can change this if you wishrules:- apiGroups:[""]resources:["endpoints"]verbs:["create","delete","deletecollection","patch","update"]
```

## Upgrading from ABAC 
Clusters that originally ran older Kubernetes versions often used permissive ABAC policies, including granting full API access to all service accounts. 
Default RBAC policies grant scoped permissions to control-plane components, nodes, and controllers, but grant no permissions to service accounts outside the kube-systemnamespace (beyond the permissions given by API discovery roles ). 
While far more secure, this can be disruptive to existing workloads expecting to automatically receive API permissions. Here are two approaches for managing this transition: 
### Parallel authorizers 
Run both the RBAC and ABAC authorizers, and specify a policy file that contains the legacy ABAC policy : 
```
--authorization-mode=...,RBAC,ABAC --authorization-policy-file=mypolicy.json

```

To explain that first command line option in detail: if earlier authorizers, such as Node, deny a request, then the RBAC authorizer attempts to authorize the API request. If RBAC also denies that API request, the ABAC authorizer is then run. This means that any request allowed by either the RBAC or ABAC policies is allowed. 
When the kube-apiserver is run with a log level of 5 or higher for the RBAC component ( --vmodule=rbac*=5or --v=5), you can see RBAC denials in the API server log (prefixed with RBAC). You can use that information to determine which roles need to be granted to which users, groups, or service accounts. 
Once you have granted roles to service accounts and workloads are running with no RBAC denial messages in the server logs, you can remove the ABAC authorizer. 
### Permissive RBAC permissions 
You can replicate a permissive ABAC policy using RBAC role bindings. 
#### Warning: 
The following policy allows ALL service accounts to act as cluster administrators. Any application running in a container receives service account credentials automatically, and could perform any action against the API, including viewing secrets and modifying permissions. This is not a recommended policy. 
```
kubectl create clusterrolebinding permissive-binding \
  --clusterrole=cluster-admin \
  --user=admin \
  --user=kubelet \
  --group=system:serviceaccounts

```

After you have transitioned to use RBAC, you should adjust the access controls for your cluster to ensure that these meet your information security needs. 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified August 26, 2026 at 2:08 PM PST: Update for deprecation of kube-dns (#56933) (d96f81aa02) 
- - - - - - 

- - - - 

### 📄 Source: [https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-certs/](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-certs/)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - Português (Portuguese)   - বাংলা (Bengali)   - Français (French)   - Deutsch (German)   - हिन्दी (Hindi)   - Bahasa Indonesia (Indonesian)   - Italiano (Italian)   - 日本語 (Japanese)   - 한국어 (Korean)   - فارسی (Persian)   - Polski (Polish)   - Русский (Russian)   - Español (Spanish)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# kubeadm certs 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- - - - - - 
- - - - - 
# kubeadm certs 
kubeadm certsprovides utilities for managing certificates. For more details on how these commands can be used, see Certificate Management with kubeadm . 
## kubeadm certs 
A collection of operations for operating Kubernetes certificates. 
- overview 
### Synopsis 
Commands related to handling Kubernetes certificates 
```
kubeadm certs [flags]

```

### Options 
|  -h, --help  |
|   | 
help for certs  |
### Options inherited from parent commands 
|  --rootfs string  |
|   | 
The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path.  |
## kubeadm certs renew 
You can renew all Kubernetes certificates using the allsubcommand or renew them selectively. For more details see Manual certificate renewal . 
- renew - all - admin.conf - apiserver-etcd-client - apiserver-kubelet-client - apiserver - controller-manager.conf - etcd-healthcheck-client - etcd-peer - etcd-server - front-proxy-client - scheduler.conf - super-admin.conf 
### Synopsis 
Renew certificates for a Kubernetes cluster 
```
kubeadm certs renew [flags]

```

### Options 
|  -h, --help  |
|   | 
help for renew  |
### Options inherited from parent commands 
|  --rootfs string  |
|   | 
The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path.  |
Renew all available certificates 
### Synopsis 
Renew all known certificates necessary to run the control plane. Renewals are run unconditionally, regardless of expiration date. Renewals can also be run individually for more control. 
```
kubeadm certs renew all [flags]

```

### Options 
|  --cert-dir string Default: "/etc/kubernetes/pki"  |
|   | 
The path where to save the certificates  |
|  --config string  |
|   | 
Path to a kubeadm configuration file.  |
|  -h, --help  |
|   | 
help for all  |
|  --kubeconfig string Default: "/etc/kubernetes/admin.conf"  |
|   | 
The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file.  |
### Options inherited from parent commands 
|  --rootfs string  |
|   | 
The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path.  |
### Synopsis 
Renew the certificate embedded in the kubeconfig file for the admin to use and for kubeadm itself. 
Renewals run unconditionally, regardless of certificate expiration date; extra attributes such as SANs will be based on the existing file/certificates, there is no need to resupply them. 
Renewal by default tries to use the certificate authority in the local PKI managed by kubeadm; as alternative it is possible to use K8s certificate API for certificate renewal, or as a last option, to generate a CSR request. 
After renewal, in order to make changes effective, is required to restart control-plane components and eventually re-distribute the renewed certificate in case the file is used elsewhere. 
```
kubeadm certs renew admin.conf [flags]

```

### Options 
|  --cert-dir string Default: "/etc/kubernetes/pki"  |
|   | 
The path where to save the certificates  |
|  --config string  |
|   | 
Path to a kubeadm configuration file.  |
|  -h, --help  |
|   | 
help for admin.conf  |
|  --kubeconfig string Default: "/etc/kubernetes/admin.conf"  |
|   | 
The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file.  |
### Options inherited from parent commands 
|  --rootfs string  |
|   | 
The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path.  |
### Synopsis 
Renew the certificate the apiserver uses to access etcd. 
Renewals run unconditionally, regardless of certificate expiration date; extra attributes such as SANs will be based on the existing file/certificates, there is no need to resupply them. 
Renewal by default tries to use the certificate authority in the local PKI managed by kubeadm; as alternative it is possible to use K8s certificate API for certificate renewal, or as a last option, to generate a CSR request. 
After renewal, in order to make changes effective, is required to restart control-plane components and eventually re-distribute the renewed certificate in case the file is used elsewhere. 
```
kubeadm certs renew apiserver-etcd-client [flags]

```

### Options 
|  --cert-dir string Default: "/etc/kubernetes/pki"  |
|   | 
The path where to save the certificates  |
|  --config string  |
|   | 
Path to a kubeadm configuration file.  |
|  -h, --help  |
|   | 
help for apiserver-etcd-client  |
|  --kubeconfig string Default: "/etc/kubernetes/admin.conf"  |
|   | 
The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file.  |
### Options inherited from parent commands 
|  --rootfs string  |
|   | 
The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path.  |
### Synopsis 
Renew the certificate for the API server to connect to kubelet. 
Renewals run unconditionally, regardless of certificate expiration date; extra attributes such as SANs will be based on the existing file/certificates, there is no need to resupply them. 
Renewal by default tries to use the certificate authority in the local PKI managed by kubeadm; as alternative it is possible to use K8s certificate API for certificate renewal, or as a last option, to generate a CSR request. 
After renewal, in order to make changes effective, is required to restart control-plane components and eventually re-distribute the renewed certificate in case the file is used elsewhere. 
```
kubeadm certs renew apiserver-kubelet-client [flags]

```

### Options 
|  --cert-dir string Default: "/etc/kubernetes/pki"  |
|   | 
The path where to save the certificates  |
|  --config string  |
|   | 
Path to a kubeadm configuration file.  |
|  -h, --help  |
|   | 
help for apiserver-kubelet-client  |
|  --kubeconfig string Default: "/etc/kubernetes/admin.conf"  |
|   | 
The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file.  |
### Options inherited from parent commands 
|  --rootfs string  |
|   | 
The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path.  |
### Synopsis 
Renew the certificate for serving the Kubernetes API. 
Renewals run unconditionally, regardless of certificate expiration date; extra attributes such as SANs will be based on the existing file/certificates, there is no need to resupply them. 
Renewal by default tries to use the certificate authority in the local PKI managed by kubeadm; as alternative it is possible to use K8s certificate API for certificate renewal, or as a last option, to generate a CSR request. 
After renewal, in order to make changes effective, is required to restart control-plane components and eventually re-distribute the renewed certificate in case the file is used elsewhere. 
```
kubeadm certs renew apiserver [flags]

```

### Options 
|  --cert-dir string Default: "/etc/kubernetes/pki"  |
|   | 
The path where to save the certificates  |
|  --config string  |
|   | 
Path to a kubeadm configuration file.  |
|  -h, --help  |
|   | 
help for apiserver  |
|  --kubeconfig string Default: "/etc/kubernetes/admin.conf"  |
|   | 
The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file.  |
### Options inherited from parent commands 
|  --rootfs string  |
|   | 
The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path.  |
### Synopsis 
Renew the certificate embedded in the kubeconfig file for the controller manager to use. 
Renewals run unconditionally, regardless of certificate expiration date; extra attributes such as SANs will be based on the existing file/certificates, there is no need to resupply them. 
Renewal by default tries to use the certificate authority in the local PKI managed by kubeadm; as alternative it is possible to use K8s certificate API for certificate renewal, or as a last option, to generate a CSR request. 
After renewal, in order to make changes effective, is required to restart control-plane components and eventually re-distribute the renewed certificate in case the file is used elsewhere. 
```
kubeadm certs renew controller-manager.conf [flags]

```

### Options 
|  --cert-dir string Default: "/etc/kubernetes/pki"  |
|   | 
The path where to save the certificates  |
|  --config string  |
|   | 
Path to a kubeadm configuration file.  |
|  -h, --help  |
|   | 
help for controller-manager.conf  |
|  --kubeconfig string Default: "/etc/kubernetes/admin.conf"  |
|   | 
The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file.  |
### Options inherited from parent commands 
|  --rootfs string  |
|   | 
The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path.  |
### Synopsis 
Renew the certificate for liveness probes to healthcheck etcd. 
Renewals run unconditionally, regardless of certificate expiration date; extra attributes such as SANs will be based on the existing file/certificates, there is no need to resupply them. 
Renewal by default tries to use the certificate authority in the local PKI managed by kubeadm; as alternative it is possible to use K8s certificate API for certificate renewal, or as a last option, to generate a CSR request. 
After renewal, in order to make changes effective, is required to restart control-plane components and eventually re-distribute the renewed certificate in case the file is used elsewhere. 
```
kubeadm certs renew etcd-healthcheck-client [flags]

```

### Options 
|  --cert-dir string Default: "/etc/kubernetes/pki"  |
|   | 
The path where to save the certificates  |
|  --config string  |
|   | 
Path to a kubeadm configuration file.  |
|  -h, --help  |
|   | 
help for etcd-healthcheck-client  |
|  --kubeconfig string Default: "/etc/kubernetes/admin.conf"  |
|   | 
The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file.  |
### Options inherited from parent commands 
|  --rootfs string  |
|   | 
The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path.  |
### Synopsis 
Renew the certificate for etcd nodes to communicate with each other. 
Renewals run unconditionally, regardless of certificate expiration date; extra attributes such as SANs will be based on the existing file/certificates, there is no need to resupply them. 
Renewal by default tries to use the certificate authority in the local PKI managed by kubeadm; as alternative it is possible to use K8s certificate API for certificate renewal, or as a last option, to generate a CSR request. 
After renewal, in order to make changes effective, is required to restart control-plane components and eventually re-distribute the renewed certificate in case the file is used elsewhere. 
```
kubeadm certs renew etcd-peer [flags]

```

### Options 
|  --cert-dir string Default: "/etc/kubernetes/pki"  |
|   | 
The path where to save the certificates  |
|  --config string  |
|   | 
Path to a kubeadm configuration file.  |
|  -h, --help  |
|   | 
help for etcd-peer  |
|  --kubeconfig string Default: "/etc/kubernetes/admin.conf"  |
|   | 
The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file.  |
### Options inherited from parent commands 
|  --rootfs string  |
|   | 
The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path.  |
### Synopsis 
Renew the certificate for serving etcd. 
Renewals run unconditionally, regardless of certificate expiration date; extra attributes such as SANs will be based on the existing file/certificates, there is no need to resupply them. 
Renewal by default tries to use the certificate authority in the local PKI managed by kubeadm; as alternative it is possible to use K8s certificate API for certificate renewal, or as a last option, to generate a CSR request. 
After renewal, in order to make changes effective, is required to restart control-plane components and eventually re-distribute the renewed certificate in case the file is used elsewhere. 
```
kubeadm certs renew etcd-server [flags]

```

### Options 
|  --cert-dir string Default: "/etc/kubernetes/pki"  |
|   | 
The path where to save the certificates  |
|  --config string  |
|   | 
Path to a kubeadm configuration file.  |
|  -h, --help  |
|   | 
help for etcd-server  |
|  --kubeconfig string Default: "/etc/kubernetes/admin.conf"  |
|   | 
The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file.  |
### Options inherited from parent commands 
|  --rootfs string  |
|   | 
The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path.  |
### Synopsis 
Renew the certificate for the front proxy client. 
Renewals run unconditionally, regardless of certificate expiration date; extra attributes such as SANs will be based on the existing file/certificates, there is no need to resupply them. 
Renewal by default tries to use the certificate authority in the local PKI managed by kubeadm; as alternative it is possible to use K8s certificate API for certificate renewal, or as a last option, to generate a CSR request. 
After renewal, in order to make changes effective, is required to restart control-plane components and eventually re-distribute the renewed certificate in case the file is used elsewhere. 
```
kubeadm certs renew front-proxy-client [flags]

```

### Options 
|  --cert-dir string Default: "/etc/kubernetes/pki"  |
|   | 
The path where to save the certificates  |
|  --config string  |
|   | 
Path to a kubeadm configuration file.  |
|  -h, --help  |
|   | 
help for front-proxy-client  |
|  --kubeconfig string Default: "/etc/kubernetes/admin.conf"  |
|   | 
The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file.  |
### Options inherited from parent commands 
|  --rootfs string  |
|   | 
The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path.  |
### Synopsis 
Renew the certificate embedded in the kubeconfig file for the scheduler manager to use. 
Renewals run unconditionally, regardless of certificate expiration date; extra attributes such as SANs will be based on the existing file/certificates, there is no need to resupply them. 
Renewal by default tries to use the certificate authority in the local PKI managed by kubeadm; as alternative it is possible to use K8s certificate API for certificate renewal, or as a last option, to generate a CSR request. 
After renewal, in order to make changes effective, is required to restart control-plane components and eventually re-distribute the renewed certificate in case the file is used elsewhere. 
```
kubeadm certs renew scheduler.conf [flags]

```

### Options 
|  --cert-dir string Default: "/etc/kubernetes/pki"  |
|   | 
The path where to save the certificates  |
|  --config string  |
|   | 
Path to a kubeadm configuration file.  |
|  -h, --help  |
|   | 
help for scheduler.conf  |
|  --kubeconfig string Default: "/etc/kubernetes/admin.conf"  |
|   | 
The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file.  |
### Options inherited from parent commands 
|  --rootfs string  |
|   | 
The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path.  |
### Synopsis 
Renew the certificate embedded in the kubeconfig file for the super-admin. 
Renewals run unconditionally, regardless of certificate expiration date; extra attributes such as SANs will be based on the existing file/certificates, there is no need to resupply them. 
Renewal by default tries to use the certificate authority in the local PKI managed by kubeadm; as alternative it is possible to use K8s certificate API for certificate renewal, or as a last option, to generate a CSR request. 
After renewal, in order to make changes effective, is required to restart control-plane components and eventually re-distribute the renewed certificate in case the file is used elsewhere. 
```
kubeadm certs renew super-admin.conf [flags]

```

### Options 
|  --cert-dir string Default: "/etc/kubernetes/pki"  |
|   | 
The path where to save the certificates  |
|  --config string  |
|   | 
Path to a kubeadm configuration file.  |
|  -h, --help  |
|   | 
help for super-admin.conf  |
|  --kubeconfig string Default: "/etc/kubernetes/admin.conf"  |
|   | 
The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file.  |
### Options inherited from parent commands 
|  --rootfs string  |
|   | 
The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path.  |
## kubeadm certs certificate-key 
This command can be used to generate a new control-plane certificate key. The key can be passed as --certificate-keyto kubeadm initand kubeadm jointo enable the automatic copy of certificates when joining additional control-plane nodes. 
- certificate-key 
Generate certificate keys 
### Synopsis 
This command will print out a secure randomly-generated certificate key that can be used with the "init" command. 
You can also use "kubeadm init --upload-certs" without specifying a certificate key and it will generate and print one for you. 
```
kubeadm certs certificate-key [flags]

```

### Options 
|  -h, --help  |
|   | 
help for certificate-key  |
### Options inherited from parent commands 
|  --rootfs string  |
|   | 
The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path.  |
## kubeadm certs check-expiration 
This command checks expiration for the certificates in the local PKI managed by kubeadm. For more details see Check certificate expiration . 
- check-expiration 
Check certificates expiration for a Kubernetes cluster 
### Synopsis 
Checks expiration for the certificates in the local PKI managed by kubeadm. 
```
kubeadm certs check-expiration [flags]

```

### Options 
|  --allow-missing-template-keys Default: true  |
|   | 
If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.  |
|  --cert-dir string Default: "/etc/kubernetes/pki"  |
|   | 
The path where to save the certificates  |
|  --config string  |
|   | 
Path to a kubeadm configuration file.  |
|  -h, --help  |
|   | 
help for check-expiration  |
|  --kubeconfig string Default: "/etc/kubernetes/admin.conf"  |
|   | 
The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file.  |
|  -o, --output string Default: "text"  |
|   | 
Output format. One of: text|json|yaml|kyaml|go-template|go-template-file|template|templatefile|jsonpath|jsonpath-as-json|jsonpath-file.  |
|  --show-managed-fields  |
|   | 
If true, keep the managedFields when printing objects in JSON or YAML format.  |
### Options inherited from parent commands 
|  --rootfs string  |
|   | 
The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path.  |
## kubeadm certs generate-csr 
This command can be used to generate keys and CSRs for all control-plane certificates and kubeconfig files. The user can then sign the CSRs with a CA of their choice. To read more information on how to use the command see Signing certificate signing requests (CSR) generated by kubeadm . 
- generate-csr 
Generate keys and certificate signing requests 
### Synopsis 
Generates keys and certificate signing requests (CSRs) for all the certificates required to run the control plane. This command also generates partial kubeconfig files with private key data in the "users > user > client-key-data" field, and for each kubeconfig file an accompanying ".csr" file is created. 
This command is designed for use in Kubeadm External CA Mode . It generates CSRs which you can then submit to your external certificate authority for signing. 
The PEM encoded signed certificates should then be saved alongside the key files, using ".crt" as the file extension, or in the case of kubeconfig files, the PEM encoded signed certificate should be base64 encoded and added to the kubeconfig file in the "users > user > client-certificate-data" field. 
```
kubeadm certs generate-csr [flags]

```

### Examples 
```
  # The following command will generate keys and CSRs for all control-plane certificates and kubeconfig files:
  kubeadm certs generate-csr --kubeconfig-dir /tmp/etc-k8s --cert-dir /tmp/etc-k8s/pki

```

### Options 
|  --cert-dir string  |
|   | 
The path where to save the certificates  |
|  --config string  |
|   | 
Path to a kubeadm configuration file.  |
|  -h, --help  |
|   | 
help for generate-csr  |
|  --kubeconfig-dir string Default: "/etc/kubernetes"  |
|   | 
The path where to save the kubeconfig file.  |
### Options inherited from parent commands 
|  --rootfs string  |
|   | 
The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path.  |
## What's next 
- kubeadm init to bootstrap a Kubernetes control-plane node - kubeadm join to connect a node to the cluster - kubeadm reset to revert any changes made to this host by kubeadm initor kubeadm join
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified August 17, 2024 at 4:50 PM PST: Update references to generated pages (3b6f229424) 
- - - - - - 

- - - - 

### 📄 Source: [https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - 日本語 (Japanese)   - 한국어 (Korean)   - Español (Spanish)   - বাংলা (Bengali)   - Français (French)   - Deutsch (German)   - हिन्दी (Hindi)   - Bahasa Indonesia (Indonesian)   - Italiano (Italian)   - فارسی (Persian)   - Polski (Polish)   - Português (Portuguese)   - Русский (Russian)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# Upgrading kubeadm clusters 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- 
  -   - - - - 
  -   -   -   - - - - - 
- - - - - 
# Upgrading kubeadm clusters 
This page explains how to upgrade a Kubernetes cluster created with kubeadm from version 1.36.x to version 1.37.x, and from version 1.37.x to 1.37.y (where y > x). Skipping MINOR versions when upgrading is unsupported. For more details, please visit Version Skew Policy . 
To see information about upgrading clusters created using older versions of kubeadm, please refer to following pages instead: 
- Upgrading a kubeadm cluster from 1.35 to 1.36 - Upgrading a kubeadm cluster from 1.34 to 1.35 - Upgrading a kubeadm cluster from 1.33 to 1.34 - Upgrading a kubeadm cluster from 1.32 to 1.33 
The Kubernetes project recommends upgrading to the latest patch releases promptly, and to ensure that you are running a supported minor release of Kubernetes. Following this recommendation helps you to stay secure. 
The upgrade workflow at high level is the following: 
- Upgrade a primary control plane node. - Upgrade additional control plane nodes. - Upgrade worker nodes. 
## Before you begin 
- Make sure you read the release notes carefully. - The cluster should use a static control plane and etcd pods or external etcd. - Make sure to back up any important components, such as app-level state stored in a database. kubeadm upgradedoes not touch your workloads, only components internal to Kubernetes, but backups are always a best practice. - Swap must be disabled . 
### Additional information 
- The instructions below outline when to drain each node during the upgrade process. If you are performing a minor version upgrade for any kubelet, you must first drain the node (or nodes) that you are upgrading. In the case of control plane nodes, they could be running CoreDNS Pods or other critical workloads. For more information see Draining nodes . - The Kubernetes project recommends that you match your kubelet and kubeadm versions. You can instead use a version of kubelet that is older than kubeadm, provided it is within the range of supported versions. For more details, please visit kubeadm's skew against the kubelet . - All containers are restarted after upgrade, because the container spec hash value is changed. - To verify that the kubelet service has successfully restarted after the kubelet has been upgraded, you can execute systemctl status kubeletor view the service logs with journalctl -xeu kubelet. - kubeadm upgradesupports --configwith a UpgradeConfigurationAPI type which can be used to configure the upgrade process. - kubeadm upgradedoes not support reconfiguration of an existing cluster. Follow the steps in Reconfiguring a kubeadm cluster instead. 
### Considerations when upgrading etcd 
Because the kube-apiserverstatic pod is running at all times (even if you have drained the node), when you perform a kubeadm upgrade which includes an etcd upgrade, in-flight requests to the server will stall while the new etcd static pod is restarting. As a workaround, it is possible to actively stop the kube-apiserverprocess a few seconds before starting the kubeadm upgrade applycommand. This permits to complete in-flight requests and close existing connections, and minimizes the consequence of the etcd downtime. This can be done as follows on control plane nodes: 
```
killall -s SIGTERM kube-apiserver # trigger a graceful kube-apiserver shutdownsleep 20# wait a little bit to permit completing in-flight requestskubeadm upgrade ... # execute a kubeadm upgrade command
```

## Changing the package repository 
If you're using the community-owned package repositories ( pkgs.k8s.io), you need to enable the package repository for the desired Kubernetes minor release. This is explained in Changing the Kubernetes package repository document. Note: The legacy package repositories ( apt.kubernetes.ioand yum.kubernetes.io) have been deprecated and frozen starting from September 13, 2023 . Using the new package repositories hosted at pkgs.k8s.iois strongly recommended and required in order to install Kubernetes versions released after September 13, 2023. The deprecated legacy repositories, and their contents, might be removed at any time in the future and without a further notice period. The new package repositories provide downloads for Kubernetes versions starting with v1.24.0. 
## Determine which version to upgrade to 
Find the latest patch release for Kubernetes 1.37 using the OS package manager: 
- Ubuntu, Debian or HypriotOS - CentOS, RHEL or Fedora 
```
# Find the latest 1.37 version in the list.# It should look like 1.37.x-*, where x is the latest patch.sudo apt update
sudo apt-cache madison kubeadm

```

For systems with DNF: 
```
# Find the latest 1.37 version in the list.# It should look like 1.37.x-*, where x is the latest patch.sudo yum list --showduplicates kubeadm --disableexcludes=kubernetes

```

For systems with DNF5: 
```
# Find the latest 1.37 version in the list.# It should look like 1.37.x-*, where x is the latest patch.sudo yum list --showduplicates kubeadm --setopt=disable_excludes=kubernetes

```

If you don't see the version you expect to upgrade to, verify if the Kubernetes package repositories are used. 
## Upgrading control plane nodes 
The upgrade procedure on control plane nodes should be executed one node at a time. Pick a control plane node that you wish to upgrade first. It must have the /etc/kubernetes/admin.conffile. 
### Call "kubeadm upgrade" 
For the first control plane node 
- 
Upgrade kubeadm: 
  - Ubuntu, Debian or HypriotOS   - CentOS, RHEL or Fedora 
```
# replace x in 1.37.x-* with the latest patch versionsudo apt-mark unhold kubeadm &&\
sudo apt-get update && sudo apt-get install -y kubeadm='1.37.x-*'&&\
sudo apt-mark hold kubeadm

```

For systems with DNF: 
```
# replace x in 1.37.x-* with the latest patch versionsudo yum install -y kubeadm-'1.37.x-*' --disableexcludes=kubernetes

```

For systems with DNF5: 
```
# replace x in 1.37.x-* with the latest patch versionsudo yum install -y kubeadm-'1.37.x-*' --setopt=disable_excludes=kubernetes

```
- 
Verify that the download works and has the expected version: 
```
kubeadm version

```
- 
Verify the upgrade plan: 
```
sudo kubeadm upgrade plan

```

This command checks that your cluster can be upgraded, and fetches the versions you can upgrade to. It also shows a table with the component config version states. 
#### Note: kubeadm upgradealso automatically renews the certificates that it manages on this node. To opt-out of certificate renewal the flag --certificate-renewal=falsecan be used. For more information see the certificate management guide . - 
Choose a version to upgrade to, and run the appropriate command. For example: 
```
# replace x with the patch version you picked for this upgradesudo kubeadm upgrade apply v1.37.x

```

Once the command finishes you should see: 
```
[upgrade/successful] SUCCESS! Your cluster was upgraded to "v1.37.x". Enjoy!

[upgrade/kubelet] Now that your control plane is upgraded, please proceed with upgrading your kubelets if you haven't already done so.

```

#### Note: For versions earlier than v1.28, kubeadm defaulted to a mode that upgrades the addons (including CoreDNS and kube-proxy) immediately during kubeadm upgrade apply, regardless of whether there are other control plane instances that have not been upgraded. This may cause compatibility problems. Since v1.28, kubeadm defaults to a mode that checks whether all the control plane instances have been upgraded before starting to upgrade the addons. You must perform control plane instances upgrade sequentially or at least ensure that the last control plane instance upgrade is not started until all the other control plane instances have been upgraded completely, and the addons upgrade will be performed after the last control plane instance is upgraded. - 
Manually upgrade your CNI provider plugin. 
Your Container Network Interface (CNI) provider may have its own upgrade instructions to follow. Check the addons page to find your CNI provider and see whether additional upgrade steps are required. 
This step is not required on additional control plane nodes if the CNI provider runs as a DaemonSet. 
For the other control plane nodes 
Same as the first control plane node but use: 
```
sudo kubeadm upgrade node

```

instead of: 
```
sudo kubeadm upgrade apply

```

Also calling kubeadm upgrade planand upgrading the CNI provider plugin is no longer needed. 
### Drain the node 
Prepare the node for maintenance by marking it unschedulable and evicting the workloads: 
```
# replace <node-to-drain> with the name of your node you are drainingkubectl drain <node-to-drain> --ignore-daemonsets

```

### Upgrade kubelet and kubectl 
#### Note: 
On Linux nodes, the kubelet defaults to supporting only cgroups v2. For Kubernetes 1.37 the FailCgroupV1kubelet configuration option is set to trueby default. 
To learn more, refer to the Kubernetes cgroup v1 deprecation documentation . 
- 
Upgrade the kubelet and kubectl: 
  - Ubuntu, Debian or HypriotOS   - CentOS, RHEL or Fedora 
```
# replace x in 1.37.x-* with the latest patch versionsudo apt-mark unhold kubelet kubectl &&\
sudo apt-get update && sudo apt-get install -y kubelet='1.37.x-*'kubectl='1.37.x-*'&&\
sudo apt-mark hold kubelet kubectl

```

For systems with DNF: 
```
# replace x in 1.37.x-* with the latest patch versionsudo yum install -y kubelet-'1.37.x-*' kubectl-'1.37.x-*' --disableexcludes=kubernetes

```

For systems with DNF5: 
```
# replace x in 1.37.x-* with the latest patch versionsudo yum install -y kubelet-'1.37.x-*' kubectl-'1.37.x-*' --setopt=disable_excludes=kubernetes

```
- 
Restart the kubelet: 
```
sudo systemctl daemon-reload
sudo systemctl restart kubelet

```

### Uncordon the node 
Bring the node back online by marking it schedulable: 
```
# replace <node-to-uncordon> with the name of your nodekubectl uncordon <node-to-uncordon>

```

## Upgrade worker nodes 
The upgrade procedure on worker nodes should be executed one node at a time or few nodes at a time, without compromising the minimum required capacity for running your workloads. 
The following pages show how to upgrade Linux and Windows worker nodes: 
- Upgrade Linux nodes - Upgrade Windows nodes 
## Verify the status of the cluster 
After the kubelet is upgraded on all nodes verify that all nodes are available again by running the following command from anywhere kubectl can access the cluster: 
```
kubectl get nodes

```

The STATUScolumn should show Readyfor all your nodes, and the version number should be updated. 
## Recovering from a failure state 
If kubeadm upgradefails and does not roll back, for example because of an unexpected shutdown during execution, you can run kubeadm upgradeagain. This command is idempotent and eventually makes sure that the actual state is the desired state you declare. 
To recover from a bad state, you can also run sudo kubeadm upgrade apply --forcewithout changing the version that your cluster is running. 
During upgrade kubeadm writes the following backup folders under /etc/kubernetes/tmp: 
- kubeadm-backup-etcd-<date>-<time>- kubeadm-backup-manifests-<date>-<time>
kubeadm-backup-etcdcontains a backup of the local etcd member data for this control plane Node. In case of an etcd upgrade failure and if the automatic rollback does not work, the contents of this folder can be manually restored in /var/lib/etcd. In case external etcd is used this backup folder will be empty. 
kubeadm-backup-manifestscontains a backup of the static Pod manifest files for this control plane Node. In case of a upgrade failure and if the automatic rollback does not work, the contents of this folder can be manually restored in /etc/kubernetes/manifests. If for some reason there is no difference between a pre-upgrade and post-upgrade manifest file for a certain component, a backup file for it will not be written. 
#### Note: After the cluster upgrade using kubeadm, the backup directory /etc/kubernetes/tmpwill remain and these backup files will need to be cleared manually. 
## How it works 
kubeadm upgrade applydoes the following: 
- Checks that your cluster is in an upgradeable state: 
  - The API server is reachable   - All nodes are in the Readystate   - The control plane is healthy - Enforces the version skew policies. - Makes sure the control plane images are available or available to pull to the machine. - Generates replacements and/or uses user supplied overwrites if component configs require version upgrades. - Upgrades the control plane components or rollbacks if any of them fails to come up. - Applies the new CoreDNSand kube-proxymanifests and makes sure that all necessary RBAC rules are created. - Creates new certificate and key files of the API server and backs up old files if they're about to expire in 180 days. 
kubeadm upgrade nodedoes the following on additional control plane nodes: 
- Fetches the kubeadm ClusterConfigurationfrom the cluster. - Optionally backups the kube-apiserver certificate. - Upgrades the static Pod manifests for the control plane components. - Upgrades the kubelet configuration for this node. 
kubeadm upgrade nodedoes the following on worker nodes: 
- Fetches the kubeadm ClusterConfigurationfrom the cluster. - Upgrades the kubelet configuration for this node. 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified December 08, 2025 at 6:53 PM PST: Revise notes about cgroup v1 deprecation (b34a5979fd) 
- - - - - - 

- - - - 

### 📄 Source: [https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.37   - v1.36   - v1.35   - v1.34   - v1.33 - English 
  - 中文 (Chinese)   - Français (French)   - Bahasa Indonesia (Indonesian)   - 日本語 (Japanese)   - বাংলা (Bengali)   - Deutsch (German)   - हिन्दी (Hindi)   - Italiano (Italian)   - 한국어 (Korean)   - فارسی (Persian)   - Polski (Polish)   - Português (Portuguese)   - Русский (Russian)   - Español (Spanish)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# Configure Service Accounts for Pods 
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
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
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
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
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
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -     -     -   - 
- - 
  - - 
  - - 
  - - 
  -   - - 
  -   - - 
- - - - 
# Configure Service Accounts for Pods 
Kubernetes offers two distinct ways for clients that run within your cluster, or that otherwise have a relationship to your cluster's control plane to authenticate to the API server . 
A service account provides an identity for processes that run in a Pod, and maps to a ServiceAccount object. When you authenticate to the API server, you identify yourself as a particular user . Kubernetes recognises the concept of a user, however, Kubernetes itself does not have a User API. 
This task guide is about ServiceAccounts, which do exist in the Kubernetes API. The guide shows you some ways to configure ServiceAccounts for Pods. 
## Before you begin 
You need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a cluster, you can create one by using minikube or you can use one of these Kubernetes playgrounds: 
- iximiuz Labs - Killercoda - KodeKloud 
## Use the default service account to access the API server 
When Pods contact the API server, Pods authenticate as a particular ServiceAccount (for example, default). There is always at least one ServiceAccount in each namespace . 
Every Kubernetes namespace contains at least one ServiceAccount: the default ServiceAccount for that namespace, named default. If you do not specify a ServiceAccount when you create a Pod, Kubernetes automatically assigns the ServiceAccount named defaultin that namespace. 
You can fetch the details for a Pod you have created. For example: 
```
kubectl get pods/<podname> -o yaml

```

In the output, you see a field spec.serviceAccountName. Kubernetes automatically sets that value if you don't specify it when you create a Pod. 
An application running inside a Pod can access the Kubernetes API using automatically mounted service account credentials. See accessing the Cluster to learn more. 
When a Pod authenticates as a ServiceAccount, its level of access depends on the authorization plugin and policy in use. 
The API credentials are automatically revoked when the Pod is deleted, even if finalizers are in place. In particular, the API credentials are revoked 60 seconds beyond the .metadata.deletionTimestampset on the Pod (the deletion timestamp is typically the time that the delete request was accepted plus the Pod's termination grace period). 
### Opt out of API credential automounting 
If you don't want the kubelet to automatically mount a ServiceAccount's API credentials, you can opt out of the default behavior. You can opt out of automounting API credentials on /var/run/secrets/kubernetes.io/serviceaccount/tokenfor a service account by setting automountServiceAccountToken: falseon the ServiceAccount: 
For example: 
```
apiVersion:v1kind:ServiceAccountmetadata:name:build-robotautomountServiceAccountToken:false...
```

You can also opt out of automounting API credentials for a particular Pod: 
```
apiVersion:v1kind:Podmetadata:name:my-podspec:serviceAccountName:build-robotautomountServiceAccountToken:false...
```

If both the ServiceAccount and the Pod's .specspecify a value for automountServiceAccountToken, the Pod spec takes precedence. 
## Use more than one ServiceAccount 
Every namespace has at least one ServiceAccount: the default ServiceAccount resource, called default. You can list all ServiceAccount resources in your current namespace with: 
```
kubectl get serviceaccounts

```

The output is similar to this: 
```
NAME      SECRETS    AGE
default   1          1d

```

You can create additional ServiceAccount objects like this: 
```
kubectl apply -f - <<EOF
apiVersion: v1
kind: ServiceAccount
metadata:
  name: build-robot
EOF
```

The name of a ServiceAccount object must be a valid DNS subdomain name . 
If you get a complete dump of the service account object, like this: 
```
kubectl get serviceaccounts/build-robot -o yaml

```

The output is similar to this: 
```
apiVersion:v1kind:ServiceAccountmetadata:creationTimestamp:2019-06-16T00:12:34Zname:build-robotnamespace:defaultresourceVersion:"272500"uid:721ab723-13bc-11e5-aec2-42010af0021e
```

You can use authorization plugins to set permissions on service accounts . 
To use a non-default service account, set the spec.serviceAccountNamefield of a Pod to the name of the ServiceAccount you wish to use. 
You can only set the serviceAccountNamefield when creating a Pod, or in a template for a new Pod. You cannot update the .spec.serviceAccountNamefield of a Pod that already exists. 
#### Note: The .spec.serviceAccountfield is a deprecated alias for .spec.serviceAccountName. If you want to remove the fields from a workload resource, set both fields to empty explicitly on the pod template . 
### Cleanup 
If you tried creating build-robotServiceAccount from the example above, you can clean it up by running: 
```
kubectl delete serviceaccount/build-robot

```

## Manually create an API token for a ServiceAccount 
Suppose you have an existing service account named "build-robot" as mentioned earlier. 
You can get a time-limited API token for that ServiceAccount using kubectl: 
```
kubectl create token build-robot

```

The output from that command is a token that you can use to authenticate as that ServiceAccount. You can request a specific token duration using the --durationcommand line argument to kubectl create token(the actual duration of the issued token might be shorter, or could even be longer). Feature state: Stable since Kubernetes v1.33 More information about this feature 
This is a stable feature in Kubernetes, and has been since version v1.33. It was first available in the v1.29 release. You can no longer disable or opt out of this feature or behavior (it is locked); if you explicitly set a value for the associated feature gate ServiceAccountTokenNodeBinding , Kubernetes ignores it but does not report any error. 
Using kubectlv1.31 or later, it is possible to create a service account token that is directly bound to a Node: 
```
kubectl create token build-robot --bound-object-kind Node --bound-object-name node-001 --bound-object-uid 123...456

```

The token will be valid until it expires or either the associated Node or service account are deleted. 
#### Note: 
Versions of Kubernetes before v1.22 automatically created long term credentials for accessing the Kubernetes API. This older mechanism was based on creating token Secrets that could then be mounted into running Pods. In more recent versions, including Kubernetes v1.37, API credentials are obtained directly by using the TokenRequest API, and are mounted into Pods using a projected volume . The tokens obtained using this method have bounded lifetimes, and are automatically invalidated when the Pod they are mounted into is deleted. 
You can still manually create a service account token Secret; for example, if you need a token that never expires. However, using the TokenRequest subresource to obtain a token to access the API is recommended instead. 
### Manually create a long-lived API token for a ServiceAccount 
If you want to obtain an API token for a ServiceAccount, you create a new Secret with a special annotation, kubernetes.io/service-account.name. 
```
kubectl apply -f - <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: build-robot-secret
  annotations:
    kubernetes.io/service-account.name: build-robot
type: kubernetes.io/service-account-token
EOF
```

If you view the Secret using: 
```
kubectl get secret/build-robot-secret -o yaml

```

you can see that the Secret now contains an API token for the "build-robot" ServiceAccount. 
Because of the annotation you set, the control plane automatically generates a token for that ServiceAccounts, and stores them into the associated Secret. The control plane also cleans up tokens for deleted ServiceAccounts. 
```
kubectl describe secrets/build-robot-secret

```

The output is similar to this: 
```
Name:           build-robot-secret
Namespace:      default
Labels:         <none>
Annotations:    kubernetes.io/service-account.name: build-robot
                kubernetes.io/service-account.uid: da68f9c6-9d26-11e7-b84e-002dc52800da

Type:   kubernetes.io/service-account-token

Data
====
ca.crt:         1338 bytes
namespace:      7 bytes
token:          ...

```

#### Note: 
The content of tokenis omitted here. 
Take care not to display the contents of a kubernetes.io/service-account-tokenSecret somewhere that your terminal / computer screen could be seen by an onlooker. 
When you delete a ServiceAccount that has an associated Secret, the Kubernetes control plane automatically cleans up the long-lived token from that Secret. 
#### Note: 
If you view the ServiceAccount using: 
kubectl get serviceaccount build-robot -o yaml
You can't see the build-robot-secretSecret in the ServiceAccount API objects .secretsfield because that field is only populated with auto-generated Secrets. 
## Add ImagePullSecrets to a service account 
First, create an imagePullSecret . Next, verify it has been created. For example: 
- 
Create an imagePullSecret, as described in Specifying ImagePullSecrets on a Pod . 
```
kubectl create secret docker-registry myregistrykey --docker-server=<registry name> \
        --docker-username=DUMMY_USERNAME --docker-password=DUMMY_DOCKER_PASSWORD \
        --docker-email=DUMMY_DOCKER_EMAIL

```
- 
Verify it has been created. 
```
kubectl get secrets myregistrykey

```

The output is similar to this: 
```
NAME             TYPE                              DATA    AGE
myregistrykey    kubernetes.io/.dockerconfigjson   1       1d

```

### Add image pull secret to service account 
Next, modify the default service account for the namespace to use this Secret as an imagePullSecret. 
```
kubectl patch serviceaccount default -p '{"imagePullSecrets": [{"name": "myregistrykey"}]}'
```

You can achieve the same outcome by editing the object manually: 
```
kubectl edit serviceaccount/default

```

The output of the sa.yamlfile is similar to this: 
Your selected text editor will open with a configuration looking something like this: 
```
apiVersion:v1kind:ServiceAccountmetadata:creationTimestamp:2021-07-07T22:02:39Zname:defaultnamespace:defaultresourceVersion:"243024"uid:052fb0f4-3d50-11e5-b066-42010af0d7b6
```

Using your editor, delete the line with key resourceVersion, add lines for imagePullSecrets:and save it. Leave the uidvalue set the same as you found it. 
After you made those changes, the edited ServiceAccount looks something like this: 
```
apiVersion:v1kind:ServiceAccountmetadata:creationTimestamp:2021-07-07T22:02:39Zname:defaultnamespace:defaultuid:052fb0f4-3d50-11e5-b066-42010af0d7b6imagePullSecrets:- name:myregistrykey
```

### Verify that imagePullSecrets are set for new Pods 
Now, when a new Pod is created in the current namespace and using the default ServiceAccount, the new Pod has its spec.imagePullSecretsfield set automatically: 
```
kubectl run nginx --image=<registry name>/nginx --restart=Never
kubectl get pod nginx -o=jsonpath='{.spec.imagePullSecrets[0].name}{"\n"}'
```

The output is: 
```
myregistrykey

```

## ServiceAccount token volume projection Feature state: Stable since Kubernetes v1.20 
#### Note: 
To enable and use token request projection, you must specify each of the following command line arguments to kube-apiserver: --service-account-issuerdefines the Identifier of the service account token issuer. You can specify the --service-account-issuerargument multiple times, this can be useful to enable a non-disruptive change of the issuer. When this flag is specified multiple times, the first is used to generate tokens and all are used to determine which issuers are accepted. You must be running Kubernetes v1.22 or later to be able to specify --service-account-issuermultiple times. --service-account-key-filespecifies the path to a file containing PEM-encoded X.509 private or public keys (RSA or ECDSA), used to verify ServiceAccount tokens. The specified file can contain multiple keys, and the flag can be specified multiple times with different files. If specified multiple times, tokens signed by any of the specified keys are considered valid by the Kubernetes API server. --service-account-signing-key-filespecifies the path to a file that contains the current private key of the service account token issuer. The issuer signs issued ID tokens with this private key. --api-audiences(can be omitted) defines audiences for ServiceAccount tokens. The service account token authenticator validates that tokens used against the API are bound to at least one of these audiences. If api-audiencesis specified multiple times, tokens for any of the specified audiences are considered valid by the Kubernetes API server. If you specify the --service-account-issuercommand line argument but you don't set --api-audiences, the control plane defaults to a single element audience list that contains only the issuer URL. 
The kubelet can also project a ServiceAccount token into a Pod. You can specify desired properties of the token, such as the audience and the validity duration. These properties are not configurable on the default ServiceAccount token. The token will also become invalid against the API when either the Pod or the ServiceAccount is deleted. 
You can configure this behavior for the specof a Pod using a projected volume type called ServiceAccountToken. 
The token from this projected volume is a JSON Web Token (JWT). The JSON payload of this token follows a well defined schema - an example payload for a pod bound token: 
```
{"aud": [# matches the requested audiences, or the API server's default audiences when none are explicitly requested"https://kubernetes.default.svc"],"exp": 1731613413,"iat": 1700077413,"iss": "https://kubernetes.default.svc",# matches the first value passed to the --service-account-issuer flag"jti": "ea28ed49-2e11-4280-9ec5-bc3d1d84661a","kubernetes.io": {"namespace": "kube-system","node": {"name": "127.0.0.1","uid": "58456cb0-dd00-45ed-b797-5578fdceaced"},"pod": {"name": "coredns-69cbfb9798-jv9gn","uid": "778a530c-b3f4-47c0-9cd5-ab018fb64f33"},"serviceaccount": {"name": "coredns","uid": "a087d5a0-e1dd-43ec-93ac-f13d89cd13af"},"warnafter": 1700081020},"nbf": 1700077413,"sub": "system:serviceaccount:kube-system:coredns"}
```

### Launch a Pod using service account token projection 
To provide a Pod with a token with an audience of vaultand a validity duration of two hours, you could define a Pod manifest that is similar to: pods/pod-projected-svc-token.yaml
```
apiVersion:v1kind:Podmetadata:name:nginxspec:containers:- image:nginxname:nginxvolumeMounts:- mountPath:/var/run/secrets/tokensname:vault-tokenserviceAccountName:build-robotvolumes:- name:vault-tokenprojected:sources:- serviceAccountToken:path:vault-tokenexpirationSeconds:7200audience:vault
```

Create the Pod: 
```
kubectl create -f https://k8s.io/examples/pods/pod-projected-svc-token.yaml

```

The kubelet will: request and store the token on behalf of the Pod; make the token available to the Pod at a configurable file path; and refresh the token as it approaches expiration. The kubelet proactively requests rotation for the token if it is older than 80% of its total time-to-live (TTL), or if the token is older than 24 hours. 
The application is responsible for reloading the token when it rotates. It's often good enough for the application to load the token on a schedule (for example: once every 5 minutes), without tracking the actual expiry time. 
### Service account issuer discovery Feature state: Stable since Kubernetes v1.21 
If you have enabled token projection for ServiceAccounts in your cluster, then you can also make use of the discovery feature. Kubernetes provides a way for clients to federate as an identity provider , so that one or more external systems can act as a relying party . 
#### Note: 
The issuer URL must comply with the OIDC Discovery Spec . In practice, this means it must use the httpsscheme, and should serve an OpenID provider configuration at {service-account-issuer}/.well-known/openid-configuration. 
If the URL does not comply, ServiceAccount issuer discovery endpoints are not registered or accessible. 
When enabled, the Kubernetes API server publishes an OpenID Provider Configuration document via HTTP. The configuration document is published at /.well-known/openid-configuration. The OpenID Provider Configuration is sometimes referred to as the discovery document . The Kubernetes API server publishes the related JSON Web Key Set (JWKS), also via HTTP, at /openid/v1/jwks. 
#### Note: The responses served at /.well-known/openid-configurationand /openid/v1/jwksare designed to be OIDC compatible, but not strictly OIDC compliant. Those documents contain only the parameters necessary to perform validation of Kubernetes service account tokens. 
Clusters that use RBAC include a default ClusterRole called system:service-account-issuer-discovery. A default ClusterRoleBinding assigns this role to the system:serviceaccountsgroup, which all ServiceAccounts implicitly belong to. This allows pods running on the cluster to access the service account discovery document via their mounted service account token. Administrators may, additionally, choose to bind the role to system:authenticatedor system:unauthenticateddepending on their security requirements and which external systems they intend to federate with. 
The JWKS response contains public keys that a relying party can use to validate the Kubernetes service account tokens. Relying parties first query for the OpenID Provider Configuration, and use the jwks_urifield in the response to find the JWKS. 
In many cases, Kubernetes API servers are not available on the public internet, but public endpoints that serve cached responses from the API server can be made available by users or by service providers. In these cases, it is possible to override the jwks_uriin the OpenID Provider Configuration so that it points to the public endpoint, rather than the API server's address, by passing the --service-account-jwks-uriflag to the API server. Like the issuer URL, the JWKS URI is required to use the httpsscheme. 
## What's next 
See also: 
- Read the Cluster Admin Guide to Service Accounts - Read about Authorization in Kubernetes - Read about Secrets 
  - or learn to distribute credentials securely using Secrets   - but also bear in mind that using Secrets for authenticating as a ServiceAccount is deprecated. The recommended alternative is ServiceAccount token volume projection . - Read about projected volumes . - For background on OIDC discovery, read the ServiceAccount signing key retrieval Kubernetes Enhancement Proposal - Read the OIDC Discovery Spec 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified October 31, 2024 at 4:23 PM PST: Update ServiceAccountTokenJTI, ServiceAccountTokenPodNodeInfo, ServiceAccountTokenNodeBindingValidation to stable (2aca56ea10) 
- - - - - - 

- - - - 
