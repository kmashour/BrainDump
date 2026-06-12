---
domains:
  - "aws"
class: reference-note
tier: reference-note
tags:
  - aws/infrastructure
---

# Module 3-1: AWS Global Infrastructure

# Module 3-1: AWS Global Infrastructure & Network Architecture

This module details the physical footprint of Amazon Web Services (AWS), core cloud computing paradigms, structural design patterns of the **AWS Well-Architected Framework**, logical networking through **Virtual Private Cloud (VPC)**, and hybrid cloud connectivity.

---

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

---

# Part 1: Basics & Concepts


---

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

---

## "Automation & Orchestration" Concept
- Automation concept is making the cloud processes automatic, like deployment, provisioning, upgrading, testing, etc.
- Orchestration concept is the idea of expanding your infrastructure.

---

## "Vendor lock-in" Concept
Using a specific cloud vendor in a major way & concentrating on its services makes it difficult to move to another vendor if required.
Vendor lock-in is using cloud formation EKS instead of terraform and kubernetes which can be used with any cloud provider

---

## AWS Cloud Services
![Pasted image 20221016203143](https://user-images.githubusercontent.com/109697567/200851567-a14762b4-7de7-4781-a033-4b74541c12f2.png)

---

## AWS Global presence 
8th of May 2025 
![[Pasted image 20250508114815.png]]

---

## Creating Billing Alarms
Using the Root User, limiting bills to as low as 1$ & setting Billing alarms can be done through the Budgets tab in the Billing Dashboard.
This can be set to be a continuous **"Recurring budget"** or an **"Expiring Budget"**.
This is very important step to avoid unexpected bills over the budget plan.

---

# Part 2: VPC Deep Dive
----------
