---
domains:
  - "aws"
class: reference-note
tier: reference-note
tags:
  - aws/loadbalancing
---

# Module 3-10: AWS Elastic Load Balancing (ELB)

## 2. Elastic Load Balancing (ELB) Topologies
Elastic Load Balancing automatically distributes incoming application traffic across multiple targets.

### A. Core Topologies & Features

---

## Target Groups, Listeners, & Health Checks
Load Balancer is a REGIONAL construct, cannot create load balancers for applications across multiple regions.

##### How it works ?
ELB Load Balancer is an EC2 instance with the load balancing software, launched in an AWS-Created VPC called VPC ELB.
It reaches the instances in customer VPC with an AWS-Created ENI called ENI-ELB in customer VPC. This means that the customer subnet must have available IP addresses in range for the ENI-ELB. 
It deals with the private IP address given too the ENI-ELB.
![Pasted image 20221206024324](https://user-images.githubusercontent.com/109697567/206048344-82b16614-2089-4f7c-8fd8-e6b82c587080.png)

### Load Balancer Types
##### 1- Classic Load Balancer (CLB)
- Backend EC2 Instances
- Applicable on all layers, but old & not recommended by AWS anymore
##### 2- Application Load Balancer (ALB)
- Applicable upon Layer 7 "Applications layer" 
- Targets can be EC2 Instances, IP addresses, Lambda Function
##### 3- Network Load Balancer (NLB)
- Applicable upon Layer 4 "Network layer" 
- Targets can be EC2 Instances, IP addresses, Lambda Function
- Highest Performance for load balancers "only for layer 4".
*Note:*  Load balancers applicable on IP Addresses allow the ability to apply load balancing for on-premises sites as well, by using their IP address.

### Target Groups
![[Pasted image 20250529151249.png]]
It's a logical grouping of targets, targets can be EC2 Instances, IP addresses, or ECS microservice.
- A target is an endpoint registered with the ***ALB/NLB*** as part of a target group.
- IP addresses can be used to add targets that are instances in a peered VPC, on- premises servers, and AWS resources that can be addressed by IP and port. 
- ALB/NLB can route traffic to multiple target groups.
- A target can be registered with a target group multiple times using different ports.

### ELB Listeners
A listener is the process that checks for connection requests to the ELB nodes, Multiple listeners can be configured on the ELB.
- On the CLB, listeners are configured frontend towards the clients, and backend towards backend instances.
- On ALB/NLB, frontend is the same as CLB, but backend is configured at the target group.
![[Pasted image 20250529151422.png]]

### ELB Health Checks
![[Pasted image 20250529151634.png]]
A load balancer decouples the application layer by concealing the failure in one tier from other tiers.
- Health checks are used by the elastic load balancer to track the health and responsiveness of the backend compute.
- Health check ports and thresholds are configurable.
- This way, ELB increases the availability of the application.
- If no healthy backend computes were found, the traffic won't be dropped, but will be sent to all computes instead "in hope of a response".

### Target Groups & Listeners Rules
A rule can be given to each listener to specify a specific job "*ex:* specific Port".
- Any listener has a default rule.
- The default rule is sending any traffic to the target group port.
- Customer can define different rules.
- Rules are applied from top to bottom in the console.
- If no rule were to be satisfied the traffic is sent to the default rule.
![[Pasted image 20250529152226.png]]
![Pasted image 20221206035943](https://user-images.githubusercontent.com/109697567/206048412-46195733-e291-4b71-ae3c-e43ba570e8fb.png)

---

## ELB is on the EC2 Dashboard in Console:
![Pasted image 20221206035509](https://user-images.githubusercontent.com/109697567/206048439-b7790ab2-1d37-4055-ab68-262a01aec959.png)

---

## Cross-Zone Load Balancing
Applying the traffic equally upon instance level, instead of node level.
*ie:* Applies distribution of traffic among different AZs instead of among EC2 instances in the same EZ only.
- Ensures higher availability & fault tolerance.
- Enabled by default in CLB.
- Enabled by default in ALB.
- Disabled by default & Chargeable in NLB.
![Pasted image 20221207153739](https://user-images.githubusercontent.com/109697567/220480136-fb69acfa-8240-4dfd-b39c-882e06f426f5.png)

---

## Connection Draining
Suppose some EC2 instances is required to be deregistered from the ELB for troubleshooting, what happens to the sessions on these instances.
When a backend instance or a target from a target group attached to an ELB is deregistered from the ELB:
- ELB stops sending any further traffic to this instance/target.
- ELB waits for a deregistration (or connection draining) delay, during which in-flight sessions through that instance/ELB are given time to finish.
- Deregistration delay is 300 seconds by default.
- If the deregistration delay is met & the instance still didn't end current sessions, Traffic/Sessions will be dropped.

---

## ELB High Availability Design For Subnets
- AWS Recommends using ELB across minimum of 2 AZ.
- If the ELB is an internet-facing ELB, the enabled subnets have to be public subnets "subnets with routes accessing the internet" for the ENI.
- Backend or targets can be in public or private subnets.
- *Note:* NAT Gateways can be used in HA Design for private subnets accessing the internet.
![[Pasted image 20250529154850.png]]

---

## ELB - Security Groups
![[Pasted image 20250529155342.png]]

![Pasted image 20221207162035](https://user-images.githubusercontent.com/109697567/220480187-a0c60fbb-ddad-4436-ae9d-b9718e6bcd43.png)

- Applying security Groups to the ELB can be done.
- Security Groups are not applicable on NLB.
- The concept is setting the security groups as source instead of using IP addresses.
- Security groups are stateful.
- Make sure that the NACLs allow subnets communications
- AS the NLB cannot have security groups, it only have the NACL of the subnet. Instead of setting the security group as source, the NLB Nodes IP/Subnet range is set.
- Notice the security groups of each of the ELBs & the instances:
![Pasted image 20221207162035](https://user-images.githubusercontent.com/109697567/220480215-800168e1-dab4-4158-bdfe-84cc761f1d38.png)

---

## ELB & Digital Certificates
X.509/TLS/SSL or Digital Certificates is a digital file that is used to certify the ownership/binding between a public cryptographic key to an entity that must be named in the subject field. 
- The entity can be a person, organization, web entity, or a software distribution.
- The certificate includes the public key and information about who issued it (the Certificate Authority).
- Certificate Authority (CA) ensure that people cannot claim others' IDs by issuing fake digital certificates.
![[Pasted image 20250529161234.png]]
![Pasted image 20221207170045](https://user-images.githubusercontent.com/109697567/220480254-e113fc46-874d-41d2-ab36-8dccb3e4963f.png)

![[Pasted image 20250529161310.png]]
### Digital Certificates on ELB
ELB deals with the traffic, so it must have the certificate the clients will require for connection.
![[Pasted image 20250529161459.png]]
##### CLB
- Can do both SSL & HTTPS "Layer 4 & Layer 7".
- Can have one certificate.
##### ALB
-  Can do HTTPS only "Layer 7".
-  Can have multiple certificates.
##### NLB.
- Can do only SSL "Layer 4"
-  Can have multiple certificates.

#### SSL Offloading
SSL offloading is when the ELB will terminate TLS/HTTPS sessions from clients then establish clear or unencrypted sessions to the backend.
- Encryption is done on the Client to ELB side.
- Backend instances/targets do not have to process TLS/HTTPS handshake and the associated secure sessions overhead.
- Meaning that the backend won't need encrypted traffic.
- Termination is done on the ELB.
![Pasted image 20221207172807](https://user-images.githubusercontent.com/109697567/220480291-df051a21-8a4f-4f4b-ab12-a86beb29dc32.png)

#### TCP Passthrough
TCP Passthrough is when the backend is responsible for termination of TLS/HTTPS sessions from clients.
- End-to-end in-transit (in-flight) encryption is required between the client and EC2 backend instances or targets.
- ELB should not be involved in any SSL negotiation (decrypting and re-encrypting traffic).
- Meaning no encryption is done on the client to ELB or the ELB to backend sides. 
- Termination is done on the backend.
![Pasted image 20221207173455](https://user-images.githubusercontent.com/109697567/220480326-ced7262c-6114-4ca0-ae1d-07118ea62a8c.png)

#### Server Name Indication "SNI"
SNI or Server Name Indication is an extension to TLS.
- Clients that support SNI can indicate which domain they are trying to connect to during the handshake.
- Servers supporting SNI can read this HTTP header and respond with the correct domain certificate.
- It's not a DNS service, it only provides the correct certificate from multiple certificate.
- Supported by ALB, NLB "as they can hold multiple certificates".
![Pasted image 20221207174224](https://user-images.githubusercontent.com/109697567/220480351-83371145-e99f-4824-8b54-cdbf71821f78.png)

---

## ELB & Client IP Address
Normally, ELB nodes will send their own IPv4 address as source IP address in the packets forwarded. Suppose it's required for the applications to be able to know the actual client IP addresses, not that of the ELB Node.

The following ways used to provide the client IP address to the backend:
##### X-Forwarded
- For at layer 7 listeners.
- CLB & ALB.
- Client IP is in put in Header.
##### Proxy Protocol
- At layer 4 listeners.
- CLB & NLB.
- Client IP is put in the proxy data not the Header.
- If the Instance IDs were used in the target groups, NLB automatically preserves client IP addresses when the instances are registered to their target groups using instance IDs.
*ie.* Proxy Protocol is not needed in NBL if the instances were defined using instance ID, but is used in case of IP addresses or Lambda functions defining of instances in the target group.
![Pasted image 20221207182608](https://user-images.githubusercontent.com/109697567/220480394-9beb1df5-2274-4fbd-80af-b3d76d7d14b3.png)

---

## ELB Monitoring & Logging
Monitoring ELB in AWS can be achieved by:
- ###### CloudWatch:
	- By default ELB service will send ***metrics*** to CloudWatch every minute if there is traffic flowing through the ELB nodes
- ##### CloudTrail:
	- CloudTrail logs all ***API Calls*** made to ELB APIs.
 - ##### Access Logs:
	 - Provides logs about ***actual traffic, Client IP, Protocol, Port,*** basically about the actual session information. Disabled by default.

---

## Session Affinity (Sticky Sessions)
![[Pasted image 20250626145343.png]]
Session stickiness refers to a configuration whereby the ELB will bind a client to a specific backend instance/target.
- This is supported by all ELBs. 
- Session stickiness is not fault tolerant. 
- Used with stateful applications, or applications that can not maintain session state.
- Applied on the target group not the ELB.
*Note:* Stateful applications are applications that stores cache & cookies on the instant, so faulting of the instance means losing of data access.

---

## Perfect Forward Secrecy
Perfect Forward Secrecy (PFS) helps prevent the decoding of captured encrypted data by unauthorized third parties, even if the private key gets compromised.
- Concept is allowing using changing encryption keys.
- It does that by using session keys that are ephemeral and not stored anywhere.
- Uses Elliptic Curve Diffie-Hellman Ephemeral (ECDHE) Protocol.

---

## Application Load Balancer (ALB)
-  supports: HTTP, HTTPS, HTTP/2 
- Supports Web Application Firewall (WAF): You can use AWS WAF with Application Load Balancer (ALB) to allow or block requests based on the rules in a web access control list (web ACL). 
- Internet-facing ALB supports IPv4 and DualStack. 
- ALB supports WebSockets by default "Server Initiating messages to client".
- ALB supports round robin (default), and least outstanding requests load balancing algorithms
	- Round Robin: Distributes work among targets equally.
	- Least Outstanding Requests: Sends traffic to less stressed instances.

### Path-Based & Host-Based Routing
Supported ONLY for ALB.
An Application Load Balancer supports specific content routing traffic to a specific target group based on:
- The HTTP path header of the URL.
	``www.example.com/images``
	``www.example.com/videos``
- The HTTP hostname header of the URL.
	``offers.example.com``
	``sales.example.com``
- This is also possible for HTTPS traffic.
![Pasted image 20221207190102](https://user-images.githubusercontent.com/109697567/220480515-964acd6b-9953-4fbc-a84b-b57fb3ca3128.png)

### Slow Start Mode
Supported ONLY for ALB.
By default, a registered target starts receiving its full share of requests as soon as it becomes healthy.
- This is a target group level configuration.
- Slow-start mode gives a target time to warm up before receiving the full share of requests.
- During this period, the ALB increases the requests sent to this target gradually towards full share, which happens when the slow-start time ends.

---

## Network Load Balancer (NLB)
- NLB provides the highest connections speed and lowest latency among all ELBs.
- Supports TCP & UDP load balancing.
- NLB can be assigned an Elastic IP per enabled AZ if desired.
- Access logs, cross-zone load balancing, and delete protection are disabled by default, & chargeable.
- Supports client connections over VPC peering, AWS VPNs and 3rd party VPNs.

### AWS PrivateLink & VPC Endpoints
![[Pasted image 20250626153447.png]]
- Used with Interface VPC Endpoints.
- AWS PrivateLink-powered services are created in a VPC, also called ***VPC Endpoint Services***.
- Requirement is to have a NLB in the provider VPC and an Interface VPC Endpoint in the consumer VPC. Together, they constitute the Private Link to this service.
- Provider VPC can control via permissions which principals can connect via interface endpoints.

#### AWS PrivateLink & VPC Endpoints High Availability
- High Availability is applied by configuring the NLB and interface endpoints in each AZ in that AWS region.
- Consumers use DNS names for the endpoints to connect to the services. 
- It's advised to enable cross-zone load balancing on the NLB to ensure each NLB node can route to all EC2 instances, but it's chargeable.
![Pasted image 20221207220244](https://user-images.githubusercontent.com/109697567/220480562-f13bed65-3e13-4fcb-ab44-3336f64c8118.png)

### Gateway Load Balancer
It is a service that makes it easy and cost-effective to deploy, scale and manage the availability of third-party virtual applications such as Firewalls, Intrusion detection and prevention systems, and deep packet inspection systems in the cloud.
- Internet traffic goes from the IGW to the Gateway Load Balancer, & the Gateway Load Balancer redirects it to a NLB attached to a target group with the third-party virtual appliances, then after the application ends its work, the Gateway Load Balancer gets the traffic back & sends it to the original destination EC2 Instances.
- Traffic from the instance to internet "response" works the same way.
This is done via routing tables of the subnets.
- Subnet level service & has its own subnet.
![Pasted image 20221207221721](https://user-images.githubusercontent.com/109697567/220480598-c441e1c6-99f9-4134-b7d0-bb840062db54.png)

---

## Load Balancers are under the EC2 Dashboard in Console
![Pasted image 20221210202912](https://user-images.githubusercontent.com/109697567/220480632-75dfe0f2-30e4-4cbf-9fd2-5b00f332b4e7.png)




![[Pasted image 20250501135856.png]]


![[Pasted image 20250501135951.png]]



Encryption and Decryption of data stored in EBS happens on the EC2 instance !! so as we can see there no direct way or a work around to change the state of an encrypted volume to Unencrypted 

In such situations we Can do the following 
- Attach a new EBS unencrypted volume to the same EC2  
- Copy the Encrypted data to the new unencrypted volume 
- The data will be unencrypted on the host and will be saved in the new unencrypted volume without encryption 

----------------------
====================================================================

So Can I share the snapshot if i have multiple accounts in the organization 

by default a snapshot is available for the account created it only 

![[Pasted image 20250501140208.png]]

So we if we use amazon CMK the snapshot won't be shared, so we can do the copy and change CMK with something other than the default with the new snap shot to be shareable 

-------------------------
====================================================================

Any EBS or snapshot or copy will be encrypted within the scope of a region 


![[Pasted image 20250501143408.png]]
![[Pasted image 20250501143437.png]]![[Pasted image 20250501143449.png]]


-----------
===================================================================


Creating your Golden AMI -- hell yeah 
![[Pasted image 20250501161951.png]]

![[Pasted image 20250501170504.png]] 


---------------------------
====================================================================

![[Pasted image 20250501171718.png]]

![[Pasted image 20250501171731.png]] 


------------------
====================================================================

![[Pasted image 20250501172220.png]]


================================================================================================================================================================================================================================================================================

Elastic Load balancing 

Internet Facing Load Balancer 
Internal Load Balancer 



LB -- > Amazon recommend to deploy LB at 2 AZ in the same region...

LB between regions won't work LB is regional  **Many make this mistake thinking they can load balance an app between regions**



![[Pasted image 20250501174421.png]]


![[Pasted image 20250501174556.png]]


![[Pasted image 20250501174857.png]] 

Network load balancer offers the best performance performance we can use it as long as we don't need it to work on layer 7  

classic load balancer and application load balancer can a security groups configures, as of 2023 Network load balancer can have security groups configured 

![[Pasted image 20250501175443.png]]


![[Pasted image 20250501180443.png]]


![[Pasted image 20250501180459.png]]

If all Az's where unhealthy the LB just forward the traffic to all hopping it that traffic may reach a healthy target but it won't drop the traffic if 404 error of any kind came it will be a response from the failed EC2  


![[Pasted image 20250501180910.png]]

Its better for LB health checks to be on the same port thats running the application 

![[Pasted image 20250501181431.png]]

load balancer rules executed according to the order they are listed in so you need to put that in mind 

--------------------------------------------------------
====================================================================

Cross-Zone LB disabled The traffic is not divided according to EC2
every time a request is forwarded to an AZ... They have different number of EC2 

![[Pasted image 20250502101828.png]]

Cross zone lb The traffic is forwarded to all registered healthy EC2 instance by default enabled in Application load balancer and it charges in Network load balancer 

![[Pasted image 20250502102957.png]]



----------------
====================================================================

![[Pasted image 20250502103308.png]]

----------------------------------------
====================================================================

A load balancer node is defined in a public subnet if its a Internet facing load balancer 

We have one ENI-ELB per AZ with a public IP to connect with the public network and a private IP

Now to increase security measures we can place the interface of the application in a private subnet 


![[Pasted image 20250502103329.png]]

------------------------
====================================================================

![[Pasted image 20250502103846.png]]


**we can use gateway end-point for private subnets to connect to aws services** 
 
--------------------------------------------------------------------====================================================================

![[Pasted image 20250502120105.png]]


![[Pasted image 20250502120344.png]]


 ![[Pasted image 20250502120600.png]]


--------------------------------------------------------------------====================================================================

![[Pasted image 20250502122540.png]]
 
![[Pasted image 20250502122648.png]] 

![[Pasted image 20250502123036.png]]

 ![[Pasted image 20250502123257.png]]
![[Pasted image 20250502123408.png]]

![[Pasted image 20250502124046.png]]



![[Pasted image 20250502124150.png]]


![[Pasted image 20250502124835.png]]


--------------------------------------------------------------------====================================================================


![[Pasted image 20250502125222.png]]

Application load balancer 
Remember x-forwarded is the client public id found in the layer 7 header of the request 

Network load balancer 
Proxy protocol stores the ip of the client in the layer 4 message payload itself if we are not using target groups 

![[Pasted image 20250502125852.png]]

---

---

## Deep-Intuition (AARF) Breakdowns

### AARF Breakdown: SSL Offloading vs. TCP Passthrough
1.  **The Answer (Core Pattern):** Terminate TLS sessions at the load balancer (SSL Offloading) using certificates managed by AWS Certificate Manager (ACM). Transition to TCP Passthrough only when end-to-end encryption to the host is required for compliance (e.g., PCI-DSS, HIPAA).
2.  **The Assumptions (Context):** The client to ELB path is encrypted. In SSL Offloading, the ELB to backend instance path is unencrypted HTTP over the private network.
3.  **The Rationale (Why):** SSL Offloading offloads the compute-intensive TLS handshake and decryption CPU cycles from backend application servers, simplifying certificate rotation. TCP Passthrough (utilizing NLB) forwards encrypted packets directly to the EC2 instances, requiring each instance to manage its own certificate and perform decryption.
4.  **The Failure Loop (What if not):** Implementing TCP Passthrough on web applications with large numbers of short-lived connections causes high CPU utilization on EC2 instances due to constant TLS negotiations, necessitating larger instance sizes and increasing overall compute costs.
5.  **Alternative Case (When to use 'if not'):** For regulated workloads requiring zero plaintext data transmission over any network segment, implement TCP Passthrough with backend TLS termination.
