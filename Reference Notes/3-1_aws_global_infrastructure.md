---
domains:
  - "aws"
  - "infra"
class: reference-note
tier: reference-note
tags:
  - aws/infrastructure
  - aws/regions
  - aws/vpc
  - aws/well-architected
---

# Module 3-1: AWS Global Infrastructure & Network Architecture

This module details the physical footprint of Amazon Web Services (AWS), core cloud computing paradigms, structural design patterns of the **AWS Well-Architected Framework**, logical networking through **Virtual Private Cloud (VPC)**, and hybrid cloud connectivity.

---

## 🗺️ Cognitive Map: VPC Network Routing Topology

```mermaid
graph TD
    subgraph VPC["VPC (CIDR: 10.0.0.0/16)"]
        direction TB
        IGW["Internet Gateway"]
        
        subgraph PublicSubnet["Public Subnet (10.0.1.0/24)"]
            ALB["Elastic Load Balancer (ALB)"]
            NAT["NAT Gateway (EIP attached)"]
        end

        subgraph PrivateSubnet["Private Subnet (10.0.2.0/24)"]
            App["App Instance (Private IP only)"]
        end

        IGW <-->|"Route Table: 0.0.0.0/0 -> IGW"| PublicSubnet
        ALB --> App
        App -->|"Route Table: 0.0.0.0/0 -> NAT"| NAT
        NAT --> IGW
    end
```

---

## 1. Cloud Foundational Concepts & Virtualization

### A. Virtualization Foundations
Virtualization abstractions partition physical host resources into isolated logical environments:
*   **Physical Host:** Underlying bare-metal computing hardware.
*   **Hypervisor (Hardware Abstraction Layer - HAL):** Hypervisors split physical compute, memory, and network resources.
*   **Virtual Machine (VM):** The guest operating system running on simulated hardware, exposed in AWS as an **Amazon EC2 instance**.

---
title: Cloud-Benefits
tags: 
Date: 
DeeperDive:
---
Traditional computing model (CAPEX)
- **There are many problems with the traditional IT approach**
    - Covering the costs of data center rental.
    - Covering expenses for power supply, cooling, and maintenance.
    - Time required for hardware additions and replacements.
    - Cannot scale as flexibly as you would like…
    - Employing a 24/7 team for infrastructure monitoring.
    - Addressing disaster preparedness concerns such as earthquakes, power shutdowns, and fires.
    - Overall, inflexible and inconvenient for our rapidly changing world.
 ![[Pasted image 20250508105636.png]]

Infrastructure as hardware
•  capital expenditure (Capital expenditure      (CAPEX)
• Have a long hardware procurement cycle
• Require you to provision capacity by
  guessing theoretical maximum peaks

Cloud computing model
• Infrastructure as software
• Software solutions:
	• Are flexible
	• Can change more quickly, easily, and
	  cost-effectively than hardware
	  solutions
	• Eliminate the undifferentiated heavy-
	  lifting tasks

Cloud Benefits 
- CAPEX & OPEX

- Benefits from massive economics of sale

- Stop guessing capacity !! --> One of the revolutionary benefits of cloud computing the hell of super (OVER) provisioning and under provisioning, because it was impossible to satisfy traffic demands because its not predictable it may be fine but there are some days with very high traffic so we design on that case which waste the resources provisioned only to survive the anomaly of high traffic event !! in cloud Resources are elastic it can expand and shrink on demand in addition to auto-scaling capabilities if I want it 

- Increased speed and agility --> fast deployment of infrastructure just few clicks daddy !!  

- Stop spending money running and maintaining data centers --> this is huge in disaster recovery scenarios so fail over can done very easily globally

- Go Global in minutes --> in trading sites for example we need very low latency so data centers  sites must be available in all of the globe and AWS is literally all over the globe so we can initiate our infrastructure in a near region if my application is latency dependent ....


### B. Cloud Deployment Models
*   **Public Cloud:** Computing resources owned and operated by a third-party Cloud Service Provider (CSP) (e.g., AWS, GCP, Azure) and delivered over the public internet.
*   **Private Cloud:** On-premises virtualization environments (e.g., OpenStack, VMware Cloud Foundation) managed internally.
*   **Hybrid Cloud:** Integrating on-premises infrastructure and public cloud environments via secure tunnels (VPN/Direct Connect) so they present as a single logical network.
*   **Multi-Cloud:** Combining multiple distinct public cloud vendors (AWS + GCP + Azure) to leverage best-of-breed services or avoid vendor lock-in.

---
title: Virtualization
tags: 
Date: 
DeeperDive:
---
physical machine 
hypervisor  (hardware abstraction layer)
virtual machine 

why virtualization in the first place ? 

In AWS when we create create an EC2 instance its the same as using a VM but the but now its on the cloud (AWS hardware is the host of our EC2) , a few clicks and minutes away 

 AWS 
- managed
- Power Up 
- maintenance 
- patching 
all are AWS responsibility 

After finishing I could terminate the EC2 instance and pay only for what i used 

---
title: Cloud-Deployment-Models-1
tags: 
Date: 
DeeperDive:
---
Public cloud 
AWS GCP AZURE 
**Infrastructure is 100% on cloud** 

**Public Cloud = cloud resources owned and operated by a third-party cloud service provider, accessible over the Internet.**
- Six Advantages of Cloud Computing: scalability, flexibility, cost-effectiveness, reliability, security, and global accessibility.


private cloud 
- (Open-stack) self service  كله منه فيه
  **Infrastructure is 100% on premise** but not like traditional legacy services it has services same as in public cloud but managed internally by cloud engineers..Billing is internal affairs and budgeting  depending on Infrastructure available 

Hybrid cloud
- Integrating on premise and cloud through VPN(virtual private network) AWS network becomes a part of your network
- Infrastructure **is a mix** between on Premise and cloud 

### C. Cloud Provisioning Models (Shared Responsibility Boundary)
*   **Infrastructure as a Service (IaaS):** AWS handles physical hardware and virtualization. The customer manages OS patching, runtimes, and application layers (e.g., EC2, EBS).
*   **Platform as a Service (PaaS):** AWS manages the OS, runtime, and infrastructure. The customer only manages code deployments and config (e.g., Elastic Beanstalk, RDS).
*   **Software as a Service (SaaS):** AWS manages the complete application stack. The customer only consumes the software interface (e.g., AWS Artifact).

---

## 2. Six Advantages of Cloud Computing & Economics
*   **Trade Capital Expense (CAPEX) for Variable Expense (OPEX):** Avoid massive upfront investments in data centers; pay only for consumed resources.
*   **Benefit from Massive Economies of Scale:** AWS's massive size allows them to procure hardware cheaper and pass savings to customers.
*   **Stop Guessing Capacity:** Avoid over-provisioning (paying for idle hardware) or under-provisioning (crashing during peak traffic) through cloud elasticity.
*   **Increase Speed & Agility:** Deploy resources in minutes with a few clicks.
*   **Stop Spending Money Running & Maintaining Data Centers:** Eliminate undifferentiated heavy lifting (cooling, security, hardware maintenance).
*   **Go Global in Minutes:** Deploy applications worldwide with ultra-low latency.

---
title: AWS-Design-Principles-of-cloud-architecture
tags: 
Date: 
DeeperDive:
---
AWS Expects 
- operational Excellence through 
	- use automation whenever possible --> 
	  speed , less human intervention = less human errors

	- Monitor and track everything --> track running metrics (CPU,NETWORK,BOTTLENECK,IO)
	
	- Continuous improvement

- Security 
	- Use "least-privilege" access --> each service/user has the least needed privileges to operate (المعرفه علي قدر الاحتياج)
	
	- Use Multifactor Authentication
	
	- Use IAM (Identity and Access Management) --> AWS expects us to use this service to set policies for users 
	
	- Protect data in-transit and at rest --> AWS expects us encrypt data in both states 
	
	- Monitor and Audit continuously
	  Audit : event logs for actions that happens on the system

- Reliability  موثوقيه 
	- Implement Disaster Recovery techniques --> 
	  Design for failure
	
	- Make use of Autoscaling 
	
	- Test and validate regulary --> Try fail over scenario in disaster recovery  

- Performance Efficiency 
	- choose the right tool for the job 
	  Lets we used EBS storage services for storage only while it is designed to able to work with EC2 instances so it was more appropriate to use S3 bucket, using EBS is money waste we didn't fully utilize its function
	
	- Optimize resource utilization and implement scaling --> start with average needed resources and scale when in demand, Cost effective approach.
	
	- user performance benchmarks --> Test the application on different traffic scenarios to have a sense of accurate Resource requirement according to demand and traffic on my app for better performance efficiency (creating a benchmark)

- Cost Optimization 
	- use the right instance type
	
	- use AWS cost saving plans(Reserved Instance , Spot instances)
	
	- monitor and track costs 

- Sustainability   استدامه 
	- Use environment friendly resources 
	- terminate any unused (idle) resources

bill of material !!!  
Waiting 5-6 month
racking and stacking 
tagging labeling 
virtualization 
add 3 month of waiting till we finish racking 
total of 9 month of waiting 
![[Pasted image 20250719123526.png]]

### Introduction to cloud computing (Slide-1)
 
 - Definition 
	 Cloud computing is the **on-demand** delivery of **compute power**,**database**,
	 **storage**,**applications**, and other IT resources **via** the **internet with pay-as-you go**
	 
	 🗣️ Cloud computing = on-demand delivery of compute power, database storage, applications, and other IT resources.

	- Pay as you go pricing
	- Provision computing resources precisely tailored to your needs.
	- Access virtually unlimited resources promptly.
	- Convenient access to servers, storage, databases, and various application services.
 - Advantages of cloud computing [[../2-Reference-Notes/AWS-Practitioner-2025-4-15|AWS-Practitioner-2025-4-15]] 
 - Cloud service models (IaaS) (PaaS)(SaaS)
	 - ![[iaas-paas-saas-comparison.jpg.optimal.jpg]]
	 
	 

	1️⃣ Infrastructure as a Service (IaaS)
	 - Offers virtualized computing resources over the internet.
	 - Allows flexible provisioning and management of infrastructure.
	 - Eliminates the need for physical hardware ownership.
	 - Examples include **Amazon EC2, Azure Virtual Machines, and Google Compute Engine.**

	2️⃣ Platform as a Service (PaaS)
	
	 - Cloud platform for developing, deploying, and managing applications.
	 - Simplifies application development and deployment - no need for you to manage deployment or underlying infrastructure.
	 - Examples include **AWS Elastic Beanstalk, Azure App Service, and Google App Engine**

    3️⃣ Software as a Service (SaaS)
	 - Cloud-based product that is run and managed by the service provider.
	 - Applications accessed over the internet.
	 - Examples include **Google Workspace, Microsoft Office 365, and Salesforce**.
 
 - Cloud Computing deployment models 
	 - Cloud, Hybrid, Private cloud  
	 - [[../2-Reference-Notes/AWS-Practitioner-2025-4-15-2|AWS-Practitioner-2025-4-15-2]]


  • Introduction to Amazon Web Services (AWS)
  
   - A web service is any piece of software that makes itself available over the internet and uses a standardized format (JSON,XML)
  
   - AWS is a secure cloud platform that offers a broad set of global cloud-based products.

   - AWS services work together like building blocks.

   - Example on categories of services compute database storage networking and content delivery 
    ![[Pasted image 20250718152014.png]]  


- How to Interact with AWS 
  - AWS management console 
  - aws CLI 
  - SDK

• AWS Cloud Adoption Framework (AWS CAF)
 - fast run through the slides 
 - ![[Pasted image 20250718154655.png]]



After completing this module, you should be able to: (Questions)

• Define different types of cloud computing models ? 
• Describe six advantages of cloud computing ?
• Recognize the main AWS service categories and core services ? 
• Review the AWS Cloud Adoption Framework (AWS CAF) ?


---------------------- 

### Introduction to cloud computing (Slide-2)

#### Fundamentals of pricing AWS Pricing Models

Three fundamental drivers of cost with AWS
![[Pasted image 20250718180933.png]]
1. **Pay as you go**
    - Pay **only for the resources you actually use**, without the need for significant upfront investments in hardware or infrastructure.
2. **Save when you reserve**
    - Minimizing risks, predictably managing budgets, and complying with long-term requirements by **providing cost savings and capacity reservation for extended periods.**
        - Reservations are available for EC2 Reserved Instances, DynamoDB Reserved Capacity, ElastiCache Reserved Nodes, RDS Reserved Instance, Redshift Reserved
3. **Pay less by using more**
    - Offering **lower prices for higher volumes of resource consumption or data transfer.**
4. **Pay less AWS grows**
    - As AWS's **scale and efficiency grow,** customers can benefit from reduced costs and improved services, allowing them to **pay less for the same or even enhanced cloud resources and capabilities.**

![[Pasted image 20250718181014.png]]

#### Total Cost of Ownership (TCO) 
Total Cost of Ownership (TCO) is the financial
estimate to help identify direct and indirect
costs of a system.
Why use TCO?
• To compare the costs of running an entire
infrastructure environment or specific
workload on-premises versus on AWS
• To budget and build the business case for
moving to the cloud

Slides 
#### Pricing Calculator

AWS Pricing Calculator = a free web-based planning tool that you can use to **create cost estimates for using AWS services.**

- **Model your solutions before building them**
- Explore AWS service price points
- Review the calculations behind your estimates
- **Plan your AWS spend**
- Find cost saving opportunities

#### Organizations 


IAM attached to the account 

![[Pasted image 20250719122004.png]]

![[Pasted image 20250719122036.png]]

All the account are under the same organization 

![[Pasted image 20250719122120.png]]

![[Pasted image 20250719122134.png]]

![[Pasted image 20250719122229.png]]

![[Pasted image 20250719122341.png]]

![[Pasted image 20250719122425.png]]

#### AWS Billing and cost management 
![[Pasted image 20250719134517.png]]

![[Pasted image 20250719134737.png]]

![[Pasted image 20250719135030.png]]


![[Pasted image 20250719135003.png]]






#### Support Plans

![[Pasted image 20250719134035.png]]
Trusted advisor consultant that gives reviews over my aws architecture if it follows the best practice 

![[Pasted image 20250719134054.png]]


![[Pasted image 20250719134107.png]]

![[Pasted image 20250719134204.png]]

![[Pasted image 20250719134240.png]]








---

## 3. AWS Physical footprint & Edge Caching
AWS operates a global infrastructure designed to achieve maximum resilience and lowest latency:
*   **AWS Regions:** Isolated geographic locations containing multiple physically separated **Availability Zones (AZs)**. Choosing regions depends on data compliance, latency, cost, and service availability.
*   **Availability Zones (AZs):** One or more data centers with redundant power, cooling, and physical security.
*   **Edge Locations:** Points of Presence (PoPs) used by **Amazon CloudFront** to cache content close to end users.
    *   *CloudFront Invalidation:* A process to purge cached assets from edge locations before their Time-To-Live (TTL) expires.

![[Pasted image 20250721180655.png]]

![[Pasted image 20250721180831.png]]

![[Pasted image 20250721180939.png]]

![[Pasted image 20250721181005.png]]

![[Pasted image 20250721181014.png]]


![[Pasted image 20250721181045.png]]

![[Pasted image 20250721181052.png]]

![[Pasted image 20250721181132.png]]

![[Pasted image 20250721181229.png]]

![[Pasted image 20250721181246.png]]

![[Pasted image 20250721181256.png]]


![[Pasted image 20250721181410.png]]

![[Pasted image 20250721181418.png]]

![[Pasted image 20250721181523.png]]

![[Pasted image 20250721181805.png]]

----------------

![[Pasted image 20250721184607.png]]


![[Pasted image 20250721182400.png]]





-----------

![[Pasted image 20250721181838.png]]

![[Pasted image 20250721181850.png]]

![[Pasted image 20250721181910.png]]

![[Pasted image 20250721181922.png]]

![[Pasted image 20250721182013.png]]


CloudFront invalidation is ==a process that removes cached content from Amazon CloudFront's edge locations before the content's Time-To-Live (TTL) expires==. This ensures that users accessing the content will receive the most up-to-date version, even if the cached copy hasn't expired yet.


![[Pasted image 20250721182023.png]]

---------


EC2 SLIDES

---

## 4. AWS Well-Architected Framework: The 6 Pillars
Architectural decisions should align with AWS's core design pillars:
1.  **Operational Excellence:** Automate with Infrastructure as Code (IaC), perform small, reversible changes, and anticipate failures.
2.  **Security:** Implement a strong identity foundation (least privilege), protect data at rest and in transit, and enable auditing (CloudTrail).
3.  **Reliability:** Design for failure, test disaster recovery, scale horizontally, and manage capacity dynamically.
4.  **Performance Efficiency:** Match resource types to workload demands, delegate heavy lifting, and use serverless.
5.  **Cost Optimization:** Implement Cloud Financial Management, pay only for consumed capacity, and analyze spending.
6.  **Sustainability:** Maximize utilization, minimize idle resources, and utilize energy-efficient services.

---
title: Cloud-Deployment-Models-2
tags:
Date:
DeeperDive:
---
### Cloud provisioning models 

SaaS --> Microsoft 365 suite is the biggest example of SaaS I don't care about neither Infrastructure nor the platform highest level of provisioning 

PaaS --> Elastic Beanstalk service the service will handle the run time environment for my application so the platform is ready for deployment which is my responsibility (Application , Database)  

IaaS --> The infrastructure Hardware is AWS responsibility the rest is on me setting the machine from scratch

![[Screenshot from 2025-04-15 21-17-29.png]]
### Module 3:AWS Global Infrastructure Overview
#### Regions and AZs

![[Pasted image 20250719153509.png]]

![[Pasted image 20250719153531.png]]

![[Pasted image 20250719153624.png]]

![[Pasted image 20250719153735.png]]

--------------------------
#### CloudFront service 

The website shows AWS global infrastructure with all its AZs and regions 

cloudFront is inside the edge locations 

the internet routes is not predictable so it can use a route in the request and use a completely different one in the reply so it will cause delay 


![[Pasted image 20250719154304.png]]

![[Pasted image 20250719154322.png]]


Request goes to the nearest edge location if is wasn't there its considered a miss a cache the CDN use aws backbone network to retrieve the data from the source and reply the data to the requester and when other users request the same data its cache hit faster in replying 


![[Pasted image 20250719154504.png]]

![[Pasted image 20250719154825.png]]![[Pasted image 20250719154834.png]]

------------
#### Services from the slides 
 services 
  ![[Pasted image 20250721012623.png]]

  ![[Pasted image 20250721012637.png]]


  ![[Pasted image 20250721012645.png]]

  ![[Pasted image 20250721012655.png]]

  ![[Pasted image 20250721012726.png]]

![Pasted image 20221031004509](https://user-images.githubusercontent.com/109697567/200856868-6a73eec2-b1b4-4fe3-b9a2-51e7f8099f82.png)

Security Groups
	  have only permit rules. no deny rules. If no permits are found it is considered as an implied deny.
	- Can add up to 16 (5 default maximum) Security Groups per EC2 instance.
	- Security Groups are stateful, meaning that if the traffic is allowed either if its inbound or outbound, the opposite direction response is automatically allowed even if no permit rules were found.
	![Pasted image 20221031231048](https://user-images.githubusercontent.com/109697567/200858159-50800cf5-62a4-461b-a96e-eb1f2da305ca.png)

NACL
	- NACL functions at a subnet level, so it's applied to all EC2 instances inside the subnet.
	- It's applied at the implied router
	- NACLs are **Stateless** "one way only".
	- It includes permit & deny rules.
	- Each NACL rule has a sequence number, rules are elevated from lowest to highest sequence number.
	- Once a rule is found either permit or deny the process is stopped "no reading for rest of the rules", if none are found it ends with explicit deny.
	- Traffic going into Subnet is called inbound traffic, & traffic from the Subnet is called outbound traffic.


-----------

### Module 4: AWS Cloud Security
#### shared responsibility model 
![[Pasted image 20250508105843.png]]

![[Pasted image 20250721002936.png]]

![[Pasted image 20250721003315.png]]

![[Pasted image 20250721003928.png]]

![[Pasted image 20250721004105.png]]

![[Pasted image 20250721004124.png]]

![[Pasted image 20250721004223.png]]

![[Pasted image 20250721004235.png]]


![[Pasted image 20250721004038.png]]


#### Securing new AWS account 

Walk-through 
 
![[Pasted image 20250508134144.png]] 

![Pasted image 20221020232823](https://user-images.githubusercontent.com/109697567/200856466-5ba41a25-b03d-4a30-90b4-052604d218dc.png)

Cloud Trail
	 Any actions "APIs" taken by IAM users, roles or AWS services are recorded in CloudTrail.
	- Events can be viewed & downloaded.
	- It helps in governance & auditing the account.
	- Events history are maintained for 90 days.
	- Logs can be stored in a S3 Bucket for more than 90 days if desired, **this is encrypted by default.**
	- CloudTrail is integrated with SNS.
	- A trail created in the console is a multi-region trail, use the command interface to make a region trail.
	  so Console cloud trail is multi-region scope
	  And CLI if I want to make a single region trail 


#### AWS KMS

![[Pasted image 20250721011129.png]]

![[Pasted image 20250721011108.png]]

![[Pasted image 20250721011156.png]]





#### AWS Cognito
![[Pasted image 20250721010454.png]]


#### AWS Shield
![[Pasted image 20250721011337.png]]

![[Pasted image 20250721011429.png]]




#### AWS Artifact 
![[Pasted image 20250721011753.png]]

AWS Config
![[Pasted image 20250721012119.png]]
Enterprise and Enterprise Ramp-On 
TAM --- Support Roles ,Proactive Approaches

![[Pasted image 20250722211238.png]]

AWS Expects 
 - operational Excellence through 
	- use automation whenever possible --> 
	  speed , less human intervention = less human errors

	- Monitor and track everything --> track running metrics (CPU,NETWORK,BOTTLENECK,IO)
	
	- Continuous improvement

 - Security 
	- Use "least-privilege" access --> each service/user has the least needed privileges to operate (المعرفه علي قدر الاحتياج)
	
	- Use Multifactor Authentication
	
	- Use IAM (Identity and Access Management) --> AWS expects us to use this service to set policies for users 
	
	- Protect data in-transit and at rest --> AWS expects us encrypt data in both states 
	
	- Monitor and Audit continuously
	  Audit : event logs for actions that happens on the system

 - Reliability  موثوقيه 
	- Implement Disaster Recovery techniques --> 
	  Design for failure
	
	- Make use of Autoscaling 
	
	- Test and validate regulary --> Try fail over scenario in disaster recovery  

 - Performance Efficiency 
	- choose the right tool for the job 
	  Lets we used EBS storage services for storage only while it is designed to able to work with EC2 instances so it was more appropriate to use S3 bucket, using EBS is money waste we didn't fully utilize its function
	
	- Optimize resource utilization and implement scaling --> start with average needed resources and scale when in demand, Cost effective approach.
	
	- user performance benchmarks --> Test the application on different traffic scenarios to have a sense of accurate Resource requirement according to demand and traffic on my app for better performance efficiency (creating a benchmark)

 - Cost Optimization 
	- use the right instance type
	
	- use AWS cost saving plans(Reserved Instance , Spot instances)
	
	- monitor and track costs 

 - Sustainability   استدامه 
	- Use environment friendly resources 
	- terminate any unused (idle) resources



Fault Tolerance 

 ![[Pasted image 20250722214026.png]]

  With the load balancer and the two EC2 instance we achieved high availability, Now suppose we added an Autoscaling group to guarantee the existence of two EC2 instance so if of one of the two EC2 terminated the AG will create another one in any of the two AZ either the same or another available its AG responsibility, so by adding two EC2 with LB we are highly available but the AG should be added and its always comes with a package when LB is mentioned  

 But are we 100% fault tolerant ?? 
 Absolutely not because when AG executes the Boot time may be minutes so the application behavior will be affected until its ready to receive traffic  

 In case of using container instead of VM the boot process will be faster and in scenarios like these we may be fault tolerant 

 To be fault tolerant 
 Suppose a third AZ and its in the AG and the three instance is up and they are the minimum to run my app , with threshold 60% cpu usage now we guaranteed 100% fault tolerance and elasticity  



Trusted Advisor 
  slides 


---

## 5. SAA Foundation & Global Infrastructure Details
---
tags:
  - AWS-EISSA-ABO-SHERIF
Type: Reference Note
source: DOLPHIN-ED-Video-1-3
page: 
links: 
flogetzzel:
---
# Introduction To what is Cloud
Key Architecture Pillars: To speak architecture language to a client...

Course approach:
![[Pasted image 20250508104234.png]]

Blue --> course services 
Green -->  Content delivery  

Never to skipping a section again without hands-on every day Reviewing Reviewing Reviewing Reviewing Reviewing Reviewing Reviewing Reviewing Reviewing Reviewing Reviewing Reviewing Reviewing Reviewing Reviewing Reviewing Reviewing Reviewing Reviewing Reviewing Reviewing Reviewing Reviewing Reviewing 

------------

![[Pasted image 20250508105636.png]]


![[Pasted image 20250508105843.png]]


-------------
# Part 1: Basics & Concepts

## Cloud types:
Using Cloud Servers provide much more efficiency than on-Premises data centers, regarding cost, reliability & time.
### - Public Cloud & Private Cloud
Public cloud is Publicly shared among customers, while Private cloud is for only one customer...
 
So Private cloud is also a CAPEX model like traditional data centers but it comes with the sense of automation and orchestration found in public cloud

cloud = Infrastructure + Automation  + Orchestration (Add and remove services )

![Pasted image 20221109155939](https://user-images.githubusercontent.com/109697567/200851078-db999f92-50f4-4754-b526-a30fc7a2152a.png)

### - Hybrid cloud
A mix between public cloud & on-premises Private Cloud, to provide privacy & security for specific services while the other services are on Public cloud.
- It's a more complex solution as the organization has to manage multiple plat forms.
- Suitable for effectiveness, backup, disaster recovery, development & testing.
### - Multi cloud
The use of multiple & different cloud computing & storage services in a single structure. Mostly because some services are better in each cloud provider than others for a specific use.
### - Hybrid Multi Cloud
Using Hybrid cloud concept but with multiple vendors and a On premise all of that is connected. 

## "Automation & Orchestration" Concept
- Automation concept is making the cloud processes automatic, like deployment, provisioning, upgrading, testing, etc.
- Orchestration concept is the idea of expanding your infrastructure.
## "Vendor lock-in" Concept
Using a specific cloud vendor in a major way & concentrating on its services makes it difficult to move to another vendor if required.
Vendor lock-in is using cloud formation EKS instead of terraform and kubernetes which can be used with any cloud provider 

## AWS Cloud Services
![Pasted image 20221016203143](https://user-images.githubusercontent.com/109697567/200851567-a14762b4-7de7-4781-a033-4b74541c12f2.png)



## AWS Global presence 
8th of May 2025 
![[Pasted image 20250508114815.png]]


## IAM - Identity & Access Management
IAM allows creating & managing multiple identities, authentication & authorization for AWS account.
So The same AWS account can have multiple users with different permissions, instead of only logging in as a ROOT User
### IAM Features:
- Shared access to AWS account
- Granular Permissions:
	Specific & strict permissions as desired.
- Secure access to AWS resources for applications that runs on AWS 
- Multi-factor authentication
- Identity Federation:
	The process of delegating a user authentication responsibility to a trusted external party. *ex:* Logging in by google authentication.
-  identity information logs
- PCI Compliance:
	Credit Card Compliance.
- Integrated with many AWS Services
- Eventually Consistent details & permissions 
	(IAM sticks with the user regardless his geolocation or the AWS  region he is operating in)
- Free to use
- AWS STS "AWS Secure Token Service":
	Temporary Sessions.



### IAM Identities
- Federated Users (outside AWS)
- IAM User
- IAM Group
- IAM Role:
	IAM Role is a set of permissions, acts as a badge for a determined temporary time "STS - Security Token Service".

![[Pasted image 20250508121336.png]]






### IAM Console
### *_USERS:*

### Creating IAM User :
![Pasted image 20221019205435](https://user-images.githubusercontent.com/109697567/200852774-85c5e4d5-eef3-4ce5-bd19-b214dd05be7e.png)

### Setting Permissions or adding the user to a Group :
![Pasted image 20221019224718](https://user-images.githubusercontent.com/109697567/200853212-ea5ee1db-edfe-4781-9b56-668829901943.png)
### User details
![ezgif com-gif-maker](https://user-images.githubusercontent.com/109697567/201072140-3fda1335-eda2-4cfa-bad3-67ec2ecbb131.gif)
### Access Key
- A secret key that is download as .csv file, to login using it instead of username & password.
- If the access key or the file is lost, the access can be denied from the console, by selecting status to inactive.
![Pasted image 20221020014900](https://user-images.githubusercontent.com/109697567/200855856-2b1660ce-ec28-4190-9f75-5929b43136b6.png)

### *_ACCOUNT SETTINGS:*

### Password Policy
Having restrictions over passwords in the system
![Pasted image 20221020015357](https://user-images.githubusercontent.com/109697567/200855949-dab439c2-4ea5-4429-aa60-c8d9bd49ad10.png)
![Pasted image 20221020015627](https://user-images.githubusercontent.com/109697567/200856160-2c05dff0-7e09-4c78-81a7-dfb8f0473af3.png)
*Note:* When applying a new password policy, only new users will be affected, & the old users will only be affected after password expiry "Enable passwords expiration".

![[Pasted image 20250508133827.png]]

### IAM Best Practice

![[Pasted image 20250508134144.png]]

![Pasted image 20221020232823](https://user-images.githubusercontent.com/109697567/200856466-5ba41a25-b03d-4a30-90b4-052604d218dc.png)
 
## Creating Billing Alarms
Using the Root User, limiting bills to as low as 1$ & setting Billing alarms can be done through the Budgets tab in the Billing Dashboard.
This can be set to be a continuous **"Recurring budget"** or an **"Expiring Budget"**.
This is very important step to avoid unexpected bills over the budget plan.

## VPC - Virtual Private Cloud
- The Virtual Private Cloud, is a virtual data center in the cloud, confined to an AWS region & isolated from other VPCs by default.
management- The client has full control over his VPC & is secured from other clients with other VPCs on the same AWS host server.
- A VPC is confined to a single AWS Region

#AWS-VPC-SCOPE
VPC is a regional service 
You don't get charged over VPC creation (igw,vgw,subnets)
### VPC Components  
- ##### CIDR Block
	- Each created VPC has  a main CIDR Block created with it & this main cannot be removed or changed, only the VPC can be totally deleted.
	- **VPC Address Pool can be expanded by adding up to 4 secondary CIDR Blocks, with some limitations.**                  secondary CIDR  == Expansion CIDR
	- When Connecting to another VPC subnets or on premise if the same CIDR range is used it creates a problem but it can be worked around it 

- ##### Subnets
	- Multiple subnets can be configured per VPC.
	- subnets can't be overlapping and that is a basic TCP/IP restriction subnets are confined in a *Availability Zone*, *meaning they cannot stretch between multiple AZs.* 
	- Subnets can only attach to one route table at a time 

	--if i tried stretching a subnet over two AZ is not recommended because it causes troubles like broadcast problems ??-- 

- ##### Implied Router
	- AWS provides an implied virtual router for the VPC, connecting all subnets to one another. This router is accessible or manageable  only by AWS not the client.

     We can Control Implied Router behavior but thats not in the associate level 

- ##### Route Tables
    - The client only edits the routing tables provided by the Implied Router
    - Route table can be used by more than one subnet 

	Routing inside a VPC is guaranteed by default and it can't be changed or removed 

#AWS-ROUTE-TABLE-SCOPE
Subnet level 

 - ##### Internet Gateway "IGW"
	 Default VPCs are automatically assigned with Internet Gateway, created new VPCs doesn't & must be assigned to an Internet Gateway Manually .
	 Internet Gateway is fully managed by AWS not the client, horizontally scaled, redundant & highly available, & supports IPv4 & IPv6.
	 **Only one IGW can be assigned to a VPC at a time.**
	- ##### Virtual Private Gateway "VGW"
	  An encrypted (VPN-IPsec) Gateway over the internet **(can be affected by network latency)** to establish connection to On-Premise with the cloud "For Hybrid Clouds".
	  Only one VGW can be assigned to a VPC at a time.
- ##### Security Groups
- ##### Network Access Control Lists "Network ACL"
![Pasted image 20221025014904](https://user-images.githubusercontent.com/109697567/200856677-0264d399-5873-4213-a96f-029d700de759.png)
### VPC Console
By default there will a VPC on each region, this can be viewed from the VPC dashboard. 
From the VPC Console You can manage & view the info of current VPCs or create new VPCs, & manage all the VPC components listed before.
![Pasted image 20221024230911](https://user-images.githubusercontent.com/109697567/200856768-a6fb0c84-0b09-42a5-a9b5-cddc7a060af1.png)

## Public Subnet vs Private Subnet
### Public Subnet 
Is a subnet created in a VPC with IGW attached and its associated routing table contains a default route pointing at the VPC's IGW, 
meaning it has internet access. 
Public Subnets is used for the applications & services that will need internet access
### private subnets 
doesn't have internet access. They can't access the internet directly and can't be accessed from outside the VPC,*Private Subnets is mainly for databases*, Private subnets is sometimes even used for application that need internet access for extra security so it will access the internet indirectly   


![Pasted image 20221031004509](https://user-images.githubusercontent.com/109697567/200856868-6a73eec2-b1b4-4fe3-b9a2-51e7f8099f82.png)

## Hybrid Cloud Connectivity Options in AWS
##### 1- VPN Connection
- Not reliable
- Over the internet connection
- Quick to deploy
- Secure
- Cost effective
##### 2- AWS Direct Connect Connection "DX"
- Long deployment times
- Reliable good performance
- Not secure by default as VPN Connection
*Note:* It's applicable to use "IPSec"/VPN on top of the DX to get the benefits of the DX with more reliable security.
Both Connections above are terminated on the "VGW" from the VPC end, & on the Customer Gateway from the On-Premises end.
![[Pasted image 20250508151826.png]]
## EC2 - Elastic Compute Cloud
EC2 is a service acting as Virtual Machines, with resizable computing capacity in the cloud, & fully manageable by the client with the root access.
EC2 can be provisioned on **shared hosts** (Between other AWS Client's EC2 instances) or **dedicated hosts**. There is a 20 EC2 instances soft limit per account. {{Soft limits is limits that can be changed, opposite of Hard Limits}}
EC2 is launched in a subnet in the availability zone.

### EC2 Instances Types:

#AWS-EBS-SCOPE
The availability zone 
Can only be used by one EC2 
##### 1- EBS Volumes - Elastic Block Store
- EBS volumes are volumes that keeps the data persistent & not lost after turning off the EC2.
- The EBS Volumes are always outside the EC2 instance but **in the same availability zone.**
- The EC2 EBS volume holding the data is reached through ENI (eth0) as its not on EC2 its a storage over the network in the AZ.
- EC2 instances with an EBS root volume are called **EBS-Backed EC2 Instances.**
##### 2- Instance-Store
- Also known as ephemeral Storage, these volumes are in the same physical server as the EC2, & are not persistent.
- Access to Instance-store volumes are much faster than EBS Volume.
- EC2 instances with an instance-store volume are called Instance-Store Backed EC2 Instances. sometime we want the high IO operations so we make distributed system for high availability will be covered later in the course  

### EC2 SSH Keys
- No Password needed for login, only 2 Keys Pairs
- Public key is stored in AWS, Private key is a key the client keeps.
- The Private key is downloaded only at instance creation, if not or lost the instance should be terminated & start a new one.
### Methods of Connection
##### 1- SSH - Secure Shell Login for EC2 instances
##### 2- EC2 Instance Connect "Browser Based SSH Connection"

###### EC2 connecting by SSH client steps are shown in the console after trying to connect:
![Pasted image 20221031012059](https://user-images.githubusercontent.com/109697567/200857121-427a5bf5-ea49-4a1c-a9c6-dc11dd727afd.png)
![Pasted image 20221031012400](https://user-images.githubusercontent.com/109697567/200857171-dc7050f2-83b0-498e-a5cb-21df72a4573a.png)
*Note:* instead of typing the SSH key in the command, use the option -K for storing it in memory & option -A for the agent forwarding. 
![Pasted image 20221111065442](https://user-images.githubusercontent.com/109697567/201266337-b006c88e-0e45-4632-b8db-4095ad3e4720.png)

### Private, Public & Elastic IP Addresses 
![Pasted image 20221031014312](https://user-images.githubusercontent.com/109697567/200857220-2cb7281b-5258-439a-97f0-d2ef243fde0b.png)


> [!NOTE] Title
> EIP has a soft limit of 5 per VPC "Can be changed by sending a ticket"



### NAT - Network Address Translation.
**No EC2 instance will launch without having a Private IP Address.** However it needs either Public IP Address or Elastic IP Address to simply be able to connect to it, as the EC2 is logged onto through the internet as every AWS service.
The EC2 Private IP Address is translated to its corresponding Public IP Address by NAT - Network Address Translation.
![Pasted image 20221031014808](https://user-images.githubusercontent.com/109697567/200857316-159c1a72-19ee-44a3-afb3-e9a5a1bbdd66.png)

### Elastic Ip Address
EIP is mostly used to hold a specific IP for firewalls, so it is referred to as **whitelisting**, The whitelisting term is used when we want to configure a firewall to IPs so we want fixed IPs so we don't reconfigure the firewall if the instances is restarted 
![[Pasted image 20250509093622.png]]
.

### Monolithic vs Multi Tier, & Microservices
Monolithic is using one instance for the whole application & the entire application is built as a single code project, making it harder to scale & troubleshoot. It's more advisable to use multi tier instances for multiple parts of the project or the application.
![Pasted image 20221103010515](https://user-images.githubusercontent.com/109697567/200857450-e74b170d-9773-4cea-a7f8-5d19f298b6d5.png)
Microservices approach is dividing the tiers even more to be able to launch it on containers instead of VMs, as it's has more efficiency & speed.
![Pasted image 20221103041823](https://user-images.githubusercontent.com/109697567/200857510-5c6185df-2b3a-4976-a22f-bdaf49a0d814.png)

![[Pasted image 20250512091001.png]]
## Security Groups
- Security Groups are virtual firewalls applied on the ENI "Elastic Network Interface" of the EC2 instance.
- Traffic going into the ENI is called inbound traffic, & traffic from the ENI is called outbound traffic. 
- Security Groups have only permit rules. no deny rules. If no permits are found it is considered as an implied deny.
- Can add up to 16 (5 default maximum) Security Groups per EC2 instance.
- Security Groups are stateful, meaning that if the traffic is allowed either if its inbound or outbound, the opposite direction response is automatically allowed even if no permit rules were found.
![Pasted image 20221031231048](https://user-images.githubusercontent.com/109697567/200858159-50800cf5-62a4-461b-a96e-eb1f2da305ca.png)

## Disaster Recovery - RPO & RTO

![[Pasted image 20250516105714.png]]

- #### RPO - Recovery Point Objective
RPO is the acceptable data to be lost after the restoration point "Backup point" due to a disaster. Measured in time (hours / minutes / seconds)
- #### RTO - Recovery Time Objective
RTO is the acceptable time taken after the disaster to get active again & go back to last restoration point taken.
- RPO & RTO determines the cost of Disaster Recovery, less RPO & RTO means more cost with more efficient Disaster Recovery.
![Pasted image 20221109072525](https://user-images.githubusercontent.com/109697567/200859792-7bc9d1b9-29e9-4bd4-885e-c7f6424986fe.png)
AWS Approach in Disaster Recovery could be explained as having a DR Site for disaster recovery, & it should be in a different region or away form the main production site. If the production went down, the cloud service is redirected to the DR Site, & it's advised to be automated redirection. 

The RTO and RPO is determined after making a business analysis to determine how much should we invest in a disaster recovery plans   

![[Pasted image 20250516110610.png]]

![[Pasted image 20250516110618.png]]
### Disaster Recovery Approaches
Graded from lower cost & recovery speed to the higher cost & fast recovery speed as follows : 
##### 1- Backup & Restore
- Copies AMIs & backup data & store it in a different region.
- no active DR sites until the disaster happens.
##### 2- Pilot Light
- Keep the minimal needs of the infrastructure only "**ex:** Databases".
- Continuous data replication between the two sites.
##### 3- Warm Standby
- Keep a scaled down version of the production environment.
- The second site can be scaled up after the disaster if needed.
##### 4- Multi Site
- Keep full running version of the production environment.
- Active/Active Sites.

![[Pasted image 20250516111402.png]]



---

## 6. VPC Deep Dive & Network Architecture
A **Virtual Private Cloud (VPC)** is a customer-defined private logical network inside an AWS Region.

### A. VPC Foundations
*   **CIDR Block:** Primary private IP range.
*   **Subnets:** Segmentations of the VPC CIDR confined to a single Availability Zone.
    *   *Public Subnets:* Have route entries to an **Internet Gateway (IGW)**.
    *   *Private Subnets:* Do not have direct routes to the internet.
*   **Route Tables:** Lists of paths directing network packages.
*   **Implied Router:** Managed routing fabric linking all subnets inside the VPC.

AWS --> HAS REGIONS 

Regions consist of availability zones --> Actual data centers

Edge locations --> **Edge locations are AWS data centers designed to deliver services with the lowest latency possible.** they are much more smaller than the Availability zones..

Ec2 instances which is a Vm on the cloud

vpc --> virtual private network it consist of a vpc cidr which is even divided into smaller subnet cidr all the EC2 instances is launched in the subnet, so vpc is like a virtual allocation of a large number of ips which is further divided into subnets 

The vpc can be on multiple AZs under the same region where they are divided into smaller number of subnets and can communicate directly with there private Ips 


In aws different subnet can communicate directly aslong as they share the same subnet 

up-till now every thing is within a virtual private network no one can access it from the outside and Ec2 instance can access the internet 

Public subnet --> all the Ec2 instances within that subnet can access the internet through the region public ips which is provided from aws to any instance within the public subnet 

private subnet --> any instance within that subnet will not be able to communicate with the outside world two ways inbound and outbound but its reachable from inside the VPC


IGW internet gateway --> Any VPC must and should have a IGW to accessible the from internet 

NAT --> Its activated in public subnet and is used as a tunnel to the private subnets to the internet by assigning a elastic public ip to the Ec2 instance within the private subnet 

Elastic public ip --> a ip assigned by NAT to private EC2 instances in a private subnet 

NACL NETWORK ACCESS LIST --> Its like a first layer firewall on the subnet, it allows all traffic by default 

SG security group --> Think of it as a 2nd layer firewall but on Ec2 instance and unique for every Ec2 

Route tables --> Define routing rules for a subnet so a public Ec2 instance can route to the IGW and a private EC2 instance can route to the NAT






### B. VPC Components & Deeper Details
# Part 2: VPC Deep Dive
----------
## My take on the 1st hour
#### VPC Recap

![[Pasted image 20250516113120.png]]

If i want to make a patch updates in the private network i need to download but the private subnet is completely isolated it can't even access s3 buckets since they are a accessed trough a public endpoint so a private subnet can't access it also even if its an aws resource 

I can't add a gateway route in the **route table** to the IGW since its a private subnet this will be out of sense 
#### Using a NAT instance:

So we used a NAT instance as a mediator a broker between public internet and private subnet 
![[Pasted image 20250516114836.png]]

- Remember any http communication the source chooses a port from the ephemeral range of ports 

![[Pasted image 20250516115220.png]]


#### NAT Gateway 

The NAT instance is not a fully managed service by aws and its a single point of failure.
We can apply multiple Instance for HA and to be redundant and start manually to configure route table of different private subnets on my NAT instances so its a bit of hassle on top of that  it will cost.

so why not just use a **NAT Gateway**

![[Pasted image 20250516120635.png]]


### High availability architecture 

Remember that the HA and redundancy is applied on the NAT gateway itself as a resource, but it can't be stretched on multiple AZ so we create on NAT Gate way in each AZ and it servers the private subnets under that AZ thats how the architecture it self is HA and redundant so is the NAT Gateway   

![[Pasted image 20250516121047.png]]



#### NAT Instance vs NAT Gateway 
![[Pasted image 20250516121547.png]]

----






---------------

## NAT Deep Dive & NAT services
Suppose a scenario of which the EC2 in a private instance & need to update its data from an S3 Bucket, the bucket is accessible by a public IP (it has public endpoint) on the internet, & same goes for all of AWS Services. As the EC2 is in a private subnet it won't be able to connect to the S3 to get the update unless changed to a public subnet, removing the purpose which the EC2 is in a private subnet in the first place.. so the solution is refused.
There are two NAT Services that can fix the issue proposed:
#### 1- NAT Instance
- Its an EC2 instance AMI (Amazon Machine Image), so it's fully managed & secured by the client.
- NAT instance is launched in a public subnet.
- The routing table of the private subnet requiring internet access should be given a default route pointing to the NAT Instance ID
- The NAT instance has a translation table, having the source/destination IP & port, as well as the mapping IP & port.
- All Ports in the translation table are from the ephemeral range.
- The instance is given private or elastic IP address.
- The Mapping IP is the translated public IP in the NAT translation table of the Private/Elastic IP Address in the public subnet.
![Pasted image 20221110134611](https://user-images.githubusercontent.com/109697567/204100897-a689250c-5232-4226-ba0c-8676bb81b2e9.png)
#### 2- NAT Gateway
- NAT Gateway is a fully managed highly available service, scaling by up to 45 Gbps per gateway.
- NAT Gateways work only with Elastic IP Addresses.
- It cannot be associated with a security group.
- More preferred than instances due to its high availability.
- Although it's highly available, but it exists only in one availability zone.
![Pasted image 20221110134611](https://user-images.githubusercontent.com/109697567/204100927-adc7e210-278b-4f18-9ee1-01c0f2cf8966.png)
#### AZ Independent Architecture For High Availability
Multiple NAT Gateways are deployed over multiple Availability Zones "one per each", & have the route table of the private subnets in each AZ to its NAT Gateway.
So if a NAT Gateway went down the routing table redirects the packet to the other NAT Gateway in another AZ in the same network, & if an AZ went down, the other NAT Gateways keep functioning.
![Pasted image 20221110144124](https://user-images.githubusercontent.com/109697567/204100940-24c8b5b4-fabf-4cd6-92f0-4e578c278c28.png)
#### How they work:
The packet goes from the private subnet to the NAT instance/NAT Gateway in the public subnet, which redirects it to the IGW with a new public IP from the translation table in the IGW, sending it over the internet.

![Pasted image 20221110144738](https://user-images.githubusercontent.com/109697567/204100950-926f1638-67f8-4e06-93b3-84bbee21b5ee.png)

#### Console Applications:
###### 1- Creating NAT Instance
- Create an ordinary EC2 instance, with a NAT instance image which can be found in **Community AMIs**. 
- Make sure to add HTTP & HTTPS ports to the security group if it will be needed.
- **A very important note** when creating a NAT instance is **disabling the Source/Destination Check**. This is because by default the EC2 instance can  work as a source or a distention but not as an intermediate stage, this is controlled by the Source/Destination Check.

![Pasted image 20221111063112](https://user-images.githubusercontent.com/109697567/204100954-f63dcd97-e914-42cd-8849-2316d47fc8fe.png)
###### 2- Logging in to a Private Subnet's EC2 Instance using NAT Instance
- A private Subnet doesn't have internet access, so you can't access it remotely.
- To log in to a private subnet, log in to a NAT public instance & log in to the private one from it.
- Remember to add the NAT ID to the private subnet route table, with destination 0.0.0.0/0
- Access the Public EC2 instance then the Private one
- Use command   to set if the instance will update or not, to test connectivity.
![Pasted image 20221111073339](https://user-images.githubusercontent.com/109697567/204100966-cdc8b13a-ae18-4f6e-a83f-7b9c486ae0c9.png)
###### 3- Creating NAT Gateway
- Created from the VPC Console
- Created with an Elastic IP Address
- No Source/Destination Check, No Security Groups, etc.. As it's an AWS fully managed service
###### 4- Logging in to a Private Subnet's EC2 Instance using NAT Gateway
- Same as before, but instead of adding NAT Instance ID in the target in the routing table, add NAT Gateway ID with destination 0.0.0.0/0

***Notice that*** using the NAT Instance or NAT Gateway for accessing the private subnet made us allow SSH Port for accessing it. Despite this technique working properly, its not preferred in a production environment as the NAT shouldn't get SSH requests to access it, meaning that we should remove the SSH Port from  NAT Instance, & you can't SSH request on a NAT Gateway anyways.
	*What is the alternative?* Bastion Host

gateway of last resort --> when we add an entry in a route table which is 0.0.0.0/24, as when you don't know where to route use this entry 
black hauling --> when i delete a instance or an endpoint that was used in a route table the route table entry becomes a black hauling

### Bastion Host
it's an EC2 instance with no applications, allowing SSH(22) "for Linux Bastion" or RDP(3389) "for Windows Bastion", & it has all required security applications. Bastion Host is the ONLY way to access the subnets from the internet.
Thus It's a regular EC2 Instance with Security Hardening "Strict & Heavy security" created & set by you. ***BASTION HOST IS NOT A SERVICE!***


- Bastion Hosts are launched in Public subnets
- You can set the Bastion Host to only allow SSH or RDP from the corporate IP Addresses range **instead of any remote access**, this is done from the **Bastion Host Security Group or NACL in case** the subnet **only contains bastion hosts**, if the subnet has other instances or a NAT gateway we will apply the security on just the bastion instance (security group) because the NACL will also block the NAT gateway and other instances traffic 
- **Remote accessing** can be done by using a remote desktop, so the **admins log in from home to the remote desktop in corporate**, & then **to the Bastion Host**.So its recommended for a **bastion host** to have **an elastic ip** so it doesn't change unless I manually release the IP
- Once Iam inside the VPC through Bastion I can even access private subnets since Iam using the private VPC network unless i deny it explicitly in security groups or the NACL  
- For high availability, multiple Bastion Hosts can be set across different subnets & apply auto-scaling between them.
- Bastion Hosts are used only for accessing the subnets, & not sending from inside a subnet to the internet. AWS recommends NAT Gateways for outgoing requests.
![Pasted image 20221124215306](https://user-images.githubusercontent.com/109697567/204100980-5b73c8c3-aa98-414f-acd9-3cfdb5316bcc.png)

## Proxy Server
- Proxy Servers are used for **URL Filtering**
- Created in Public Subnets
- It's created in the EC2 instance & works similar to NAT Instances
- If an EC2 in a private subnet required Proxy servers, the Proxy is initiated in a public subnet & the redirection happens similar to how NAT Instances did.
## Reverse Proxy Server
it is a service that is used for **caching**. When accessing the application/website linked with a Reverse Proxy, **the URL resolves to the R-proxy**, **filtering the traffic & then sending it to the application server**, & **it deals with the response from the application server** **the same way**, **caching the operation. So if the same request came again, it will respond automatically as it's cached.**

## Connecting VPCs together 
### VPC Peering
![[Pasted image 20250516193947.png]]

By default, VPCs cannot communicate directly with each other without using internet access(No Network between them). 
VPC Peering connection allows routing between two VPCs.
- Highly available & fully managed by AWS.
- The two VPCs can be from the same account or different account, & they can be in the same AWS region or not.
- The two VPCs cannot have overlapping CIDR ranges "not even in one subnet".
- Subnets routing tables must be edited & have the new VPC range added to it.
- The routing tables contain the CIDR Block Network Range.


![[Pasted image 20250516194210.png]]
- Transitive Peering is not allowed "No intermediate routing to VPCs".



![[Pasted image 20250516194416.png]]

![[Pasted image 20250516194453.png]]

- No Edge to Edge Routing "No intermediate routing to VPN/Direct connections".

![Pasted image 20221125215929](https://user-images.githubusercontent.com/109697567/204100991-2233a5dd-1cfc-49fa-a671-f32a635c4566.png)
*Note :* For any to any connection, the no. of required peering connections is N(N-1)/2

![[Pasted image 20250516194758.png]]

### AWS Transit Gateway
Upon increasing the no. of VPCs required to be connected together, more VPC Peering connections are required, & if on-premises is to be connected to the VPCs, no. of VPNs & DX will increase as will.
Here comes the use of Transit Gateway, as it can simplify communication requirements as the VPCs grow.


![[Pasted image 20250516195320.png]]
- **Regional resource.**
- Highly available & fully managed by AWS.
- Supports IPv4 & IPv6
- VPCs cannot have overlapping CIDR ranges "not even in one subnet".
- It allows intermediate routing through editable routing tables.
- If multiple regions is to be connected, a transit gateway peering can take place between the two AWS Transit Gateways.
- The routing tables contain the Subnets IP Addresses.


![Pasted image 20221125225925](https://user-images.githubusercontent.com/109697567/204101019-8cfadba7-6561-4fb0-a4b2-a294904e4089.png)
*Note:* Remember to edit the routing table either when using peering connection or Transit Gateway, setting each of them as the destination.

### VPC Peering & Transit Gateway in Console
##### 1- Peering Connection
![[Pasted image 20250516200245.png]]
- Check that the security groups & NACLs allow the connection & Ping Request.
- Upon creating Peering connection, the other VPC will get a pending request to accept or refuse.
- The peering connection request is accepted from the *Peering connection* table.
- After this step, if you tried to ping, time out will occur as the routing table is not set up yet.
- In the routing table, make sure to set the *Destination* as the other CIDR Network, & the *Target* as the peering connection.
- Edit both routing tables for both subnets containing EC2s you will use for the ping test.


##### 2- Transit Gateway

- For using Transit Gateway, first make sure to remove the peering connection from the routing tables to get rid of any black holes.
- When creating the Transit Gateway you will find the attachment type desired.
- After choosing the VPC, a new list will appear for you to choose which subnets to work with, as it's for subnet level.
- Edit the route tables after creating the Transit Gateway, make sure to set the *Destination* as the other CIDR Network, & the *Target* as the Transit Gateway.
 
## VPC Endpoints

### Why need them illustration

![[Pasted image 20250516215126.png]]

![[Pasted image 20250516215953.png]]

![[Pasted image 20250516220822.png]]

### Gateway endpoint & Interface endpoint

![Pasted image 20221125233953](https://user-images.githubusercontent.com/109697567/204101037-8f3f1291-85e8-4614-b00a-a6975358256a.png)
Used for making applications/instances on private subnets connect to AWS services "as S3 Buckets" without a public end point "no internet access".
*ie:* Traffic going from the private subnet to the service does not go through the internet.
- They are ``virtual devices, that are redundant, scalable, & highly available.
- They allow VPC workloads to connect to supported AWS services without leaving the AWS network, thus no need of NAT instances or gateways.
- It has two types : **Gateway or Interface Endpoints***. "usage of each is according to the service."
*Note:* Only S3 & DynamoDB uses Gateways Endpoints, while services inside the VPC use Interface Endpoints.



##### 1- Gateway Endpoints

![[Pasted image 20250516222112.png]]

![[Pasted image 20250516222112.png]]

- **Set as a target in the subnet's routing table**
- Redundant & highly available.
- Only one is required per VPC, but each gateway reaches a service
  so You can configure multiple gateways for different services.
- Region Specific.
- No Security Groups.


##### 2- Interface Endpoints
![[Pasted image 20250516223643.png]]

- It's an interface with a private IP Address in a subnet you choose.
- Services that use this endpoint are known to be *Powered by AWS Private Link*.
- Supports IPv4
- Regional Specific.
- **You can add Security Groups.**
- **No Routing is done**, instead it's **based on DNS** resolution to the service.
*Note:* Remember to **create an IAM Role** for the instance with the **permissions required for dealing with services**, otherwise the endpoint will ensure the connection but the commands won't work.

### Controlling Access to services with VPC Endpoint Policies

![[Pasted image 20250516223932.png]]

- By default, an endpoint allows full access to the designated service.
- *Endpoint Policies* can be used to control who access what in the designated service
- The Policies exists for both kinds of endpoints.
*Notice:* No NACLs or Security Groups, its done through permission policies.

### Accessing VPC Endpoints from Remote Networks using Proxy Server

![Pasted image 20221126164858](https://user-images.githubusercontent.com/109697567/204101045-925a738f-511c-4afc-bd05-df4422f2c897.png)

One of the uses of Proxy servers, is that if we created it in a private subnet & connect the subnet with VPN or DX connection to an on-premises site, the proxy can be used to redirect the traffic from the site to the VPC Endpoints, making AWS services reachable from the site without internet traffic.
## IPv6 Egress-only internet Gateway
All IPv6 addresses are public, thus any IPv6 address you need is allocated from AWS not you.
*What if you need a private instance allocated with IPv6?*
- Egress Only Gateway allows outbound IPv6 traffic, but prevents initiated inbound traffic from the internet to the VPC, so it was designed to satisfy private subnets requirements.
- It's attached to the VPC, & created under the VPC Console.
- It's stateful.
- cannot be associated by a security group. But notice that if this is required, the security groups & NACLs support IPv6, so you can add security roles as desired.
- It's assigned through the routing table as the target.
- A routing table can have both IPv4 & IPv6.

![Pasted image 20221127015503](https://user-images.githubusercontent.com/109697567/204120128-7754a9d3-9318-4c80-9c32-67d07a57d4fc.png)

## VPC Flow Logs
It's a feature allowing logging to the IP traffic going to & from the network interfaces in the VPC.
- It provides Source IP/Port, Destination IP/Port, and status (Accepted or Rejected).
- The logs doesn't contain the data or a description of it.
- You can create a flow log per VPC, per subnet, or per ENI "Elastic Network Interface".
- Flow logs can be published to Amazon CloudWatch logs, *or* Amazon S3 Buckets.
- To create a flow log for any of the 3 levels, it's created in the Console under the desired level as in picture.

![[Pasted image 20250522122808.png]]

![Pasted image 20221127023122](https://user-images.githubusercontent.com/109697567/204120138-8c6bbdae-6459-446f-85dd-53ae6017ad85.png)

## Hybrid Cloud Connectivity

![[Pasted image 20250522130140.png]]
### VPN
Connecting a corporate data center to an AWS private subnet is done via static or dynamic routing. This is done using a *Customer Gateway* for the corporate level, & *VGW* for the cloud level.
- It uses IPSec to establish a secure connection.
	Internet Protocol Security "IPSec" is a secure network layer protocol suite that can authenticate & encrypt data packets between host & gateway.responsiblity
- Internet-based connection, so quality & latency depends on the internet traffic.
- Route propagation between implied router and VGW, it makes implied router has knowledge of the available connection to remote site so if it need something from there it can use the VGW 
- Routing is either static or dynamic.
- VPN encryption scope is not end-to-end encryption. Its site to site from a gateway to gateway when the data is received its not the VPN responsibility any more  
- The VGW IP address the corporate will connect to is public IP address, & the customer gateway IP address is also public.
- The customer gateway is the side that initiates connection.
- After initiating, two public IP addresses are assigned to the VGW "Not highly available as the customer gateway still has one IP address".

![[Pasted image 20250522130620.png]]



![Pasted image 20221127041838](https://user-images.githubusercontent.com/109697567/204120149-88bccdbf-dec0-4aed-b6d3-344034a5dbac.png)

If customer gateway is behind NAT it must be NAT traversal 
![[Pasted image 20250522131147.png]]
#### VPN setup on Console
- Done under the VPC Console, VIRTUAL PRIVATE NETWORK (VPN) tab.
- You will notice that you have the option to create customer gateway, this is not a creation of course but it's defining the customer gateway that already exists on the corporate side.
![Pasted image 20221127042608](https://user-images.githubusercontent.com/109697567/204120154-aa970bbd-3956-46d5-bc99-08aba0b26601.png)
- Choose the option create virtual private gateway, to setup your VGW.
- The created VGW is detached, go to actions & attach it to a VPC.
![Pasted image 20221127042930](https://user-images.githubusercontent.com/109697567/204120171-02a3c6f5-0f1c-46f8-bf90-97b4d63d5992.png)
- Choose Site-to-Site VPN Connections, & create your VPN as desired.
- Download the configuration file & send it to the corporate to set up the customer gateway, as it is the one that initiates the connection not the VGW.

### AWS Direct Connect "DX"
- Requires an AWS Router, that is assigned to the internet provider in the customer country.
- the sub interfaces between the corporate & the ISP uses VLANs.
- Only Dynamic Routing is supported.
- Requires virtual interfaces "VIF"
- Private VIF is for VPC (VGW) connections, & public VIF is for AWS public endpoints "for services".
- Provides low latency & consistent performance.
- Supports link aggregation up to 4 "Using multiple links as one logical link for higher speed & bandwidth".
- Customer can request a dedicated connection of speed 1-10Gbps.
- Customer can request a hosted connection with starting speed 50Gbps.

![[Pasted image 20250522132919.png]]

##### DX High availability options
DX Connection is not cost efficient, so setting up multiple DX links for high availability might not be the best option.
- You can use VPN connection as your high availability solution, this is obviously is not fault tolerant.
For higher fault tolerance "no economic limitings":
- You can use multiple DX links.
- You can use multiple DX links & multiple customer gateway.
![Pasted image 20221127055212](https://user-images.githubusercontent.com/109697567/204120182-89f63cb9-af37-444f-8a23-d9f4b00132ea.png)
*Note:* Remember that all of the connections after the DX router in the ISP cage is managed by AWS & stated as redundant & highly available. Thus no editing in these connection shall be considered.
##### AWS Direct Connect Speeds & Link Aggregation Groups 
![[Pasted image 20250522134734.png]]
#### Direct Connect Gateway
DX is a link is bound to a specific region according to direct connect location, So I Want to connect to one of my VPC in another region I can't do that with the Private VIF provided in the current Region. Customer can use VPN connection after the DX router to reach the VGW assigned to the VPC in the other region makes an encrypted & secure connections again, As long as Iam using Public VIF because it provide access to all public aws endpoints without internet. So any public AWS endpoint can be reached without internet by **this work around until Direct connect gateway was made**

Direct Connect Gateway allows reaching any VGW in the account, using a single ***private VIF***.
It can associate either with VGWs in VPCs, or with a transit gateway that has multiple VPC attachments in one region.
*Note:* **DX Gateway won't establish any connection between the VPCs & each other.** 
*Note:* *Although DX is only used by a corporate but its not encrypted and its not private data is sent in plain text so we use DX over IpSec, so its not secured by default*
![[Pasted image 20250522135039.png]]

##### Multiple Region DX Connections
DX Gateway can be associated with a transit gateway, so no multiple DX links will be needed across different regions. A ***Transit VIF*** will be needed for Transit Gateways connections "after the ISP as the public & private VIF".
![Pasted image 20221127070202](https://user-images.githubusercontent.com/109697567/204120189-e399b014-7919-48f8-93fb-639a8350e238.png)
*Note:* All kinds of DX connections are not considered secure "although the data link is dedicated to the customer", as the data is not encrypted. This can be overcome by using IPSec upon the DX connection, as stated before in Part 1.



---

## 7. Deep-Intuition (AARF) Breakdowns

### AARF Breakdown: NAT Gateway vs. NAT Instance
1.  **The Answer (Core Pattern):** Deploy highly available, managed **NAT Gateways** within each Availability Zone where private subnets reside, configuring separate route tables per AZ pointing outbound traffic to the local NAT Gateway.
2.  **The Assumptions (Context):** A NAT Gateway requires an Elastic IP and must be launched in a public subnet with a route pointing to an Internet Gateway.
3.  **The Rationale (Why):** NAT Gateways are fully managed, scale up to 45 Gbps, and provide built-in redundancy. NAT Instances are single-node EC2 instances requiring manual security patching, source/destination check disabling, and custom failover scripts.
4.  **The Failure Loop (What if not):** Operating a single NAT Instance for multiple AZ private subnets creates a single point of failure. If that instance crashes, all outbound connections from private subnets fail, breaking database syncs and application API requests.
5.  **Alternative Case (When to use 'if not'):** In low-budget development/sandbox environments, use a single t3.micro NAT Instance to save costs.

### AARF Breakdown: SG and NACL Ephemeral Ports
1.  **The Answer (Core Pattern):** Layer security by applying restrictive instance-level Security Groups combined with subnet-level NACLs. When configuring custom NACLs, always ensure outbound rules permit return traffic to the client's ephemeral port range (typically TCP 1024-65535).
2.  **The Assumptions (Context):** TCP handshakes require two-way communication. Client browsers establish connections by selecting a random high-numbered port to receive responses.
3.  **The Rationale (Why):** SGs are stateful; they track connection state tables and allow return packets automatically. NACLs are stateless and evaluate every packet. Failing to configure outbound ephemeral port rules on a custom NACL blocks the return packet from leaving the subnet.
4.  **The Failure Loop (What if not):** If a custom NACL has inbound rules allowing port 80/443, but lacks an outbound rule allowing ports 1024-65535, a client attempting to load a website will experience connection timeouts. The packet enters the subnet, the server processes it, but the return packet is blocked at the subnet boundary by the stateless NACL.
5.  **Alternative Case (When to use 'if not'):** In development environments where network segmentation auditing is not required, use default Open NACLs (Allow All) and rely exclusively on Security Groups.

---

## 8. Supplemental SAA Hands-on Projects & VPC Deep Dive

### A. Global Infrastructure / Architecture Initial Projects
# Introduction 
## project-1

![[Pasted image 20250508152603.png]]

![[Pasted image 20250508152636.png]]

## project-2 
![[Pasted image 20250509102913.png]]


![[Pasted image 20250509103328.png]]


### B. VPC Deep Dive Hands-on Topology
# VPC deep dive

![[Pasted image 20250516190254.png]]

With respect to only HA and fault tolerant creating two NAT gateways two bastion hosts that will do and of course the route table routes to the NAT in its AZ 

![[Pasted image 20250516190953.png]]

![[Pasted image 20250516231854.png]]

![[Pasted image 20250516232519.png]]




-----------
