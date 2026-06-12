---
domains:
  - "aws"
class: reference-note
tier: reference-note
tags:
  - aws/s3
---

# Module 3-6: AWS S3 Storage

# Module 3-6: AWS S3 Storage

This module covers scalable object storage using **Amazon Simple Storage Service (S3)**, lifecycle policies, storage tiers, cross-region replication, and analytics querying via **Amazon Athena**.

---

---

## 🗺️ Cognitive Map: S3 Gateway Endpoints & Caching
```mermaid
graph TD
    Client["Client Browser"] -->|"1. Request"| CloudFront["CloudFront Edge Cache"]
    CloudFront -->|"2. Cache Miss / Fetch"| S3["S3 Bucket (Main source)"]
    
    subgraph PrivateNetwork["VPC Private Subnet"]
        EC2["EC2 Instance"] -->|"3. Read API via Gateway Endpoint"| S3
    end
```

---

---

## 1. Amazon S3 (Simple Storage Service) Core Concepts
Amazon S3 is object storage designed for 99.999999999% (11 9s) durability.

### A. Core Features & Architecture
![[Pasted image 20250509111142.png]]

---

## AWS S3 -Simple Storage Service / Object Storage
![[Pasted image 20250509113404.png]]
- It's Object Storage based, Data & Meta-Data stored as whole object & not divided into objects "as in Block Storage".
- Cheaper than Block Storage "as EBS Volumes"
- Better scalability & durability.
- **Cannot be mounted as a drive or a directory to an EC2 instance. it can only be accessed through API's** 
- Ideal for data growth storage as there is no limit on amount of data or metadata in an object, only the maximum size of a file is 5 Terabyte
- S3 Storages are called S3 Buckets, & the Buckets are confined to the Region & outside the VPC, **backing up it to another regions must be done manually**. since its outside the VPC NACL and security groups are not applied to it 
- The S3 Buckets' names are Globally Unique.
- There are no actual folders within a bucket, however this can be mimicked and attach a folder name to objects for work organization.
![Pasted image 20221101060601](https://user-images.githubusercontent.com/109697567/200858734-a6ce799d-7255-4082-a80d-2a4d0d7f4c13.png)

![[Pasted image 20250509114119.png]]



#AWS-S3-SCOPE
Regional scope 

---

---

## 3. S3 Gateway Endpoints & Private Networking
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



---

---

## 4. Athena Querying & Caching Tiers
*   **Amazon Athena:** An interactive query service allowing SQL queries directly against data sitting inside S3 buckets without needing database loading.
*   **Storage Tiers:** S3 Standard, Intelligent-Tiering, Standard-IA, One Zone-IA, Glacier Instant/Flexible/Deep Archive.

---
