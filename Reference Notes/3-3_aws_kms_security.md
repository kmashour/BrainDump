---
domains:
  - "aws"
  - "security"
class: reference-note
tier: reference-note
tags:
  - aws/kms
  - aws/encryption
  - aws/security
---

# Module 3-3: AWS KMS & Security

This module details cryptographic key management using **AWS Key Management Service (KMS)**, envelope encryption, secrets protection, user identity syncing via **AWS Cognito**, and edge-security layers utilizing **AWS WAF** and **AWS Shield**.

---

## 🗺️ Cognitive Map: KMS Envelope Encryption

```
+---------------------+
|  Your Application   |
+---------------------+
          |
          | 1. Request Data Key from KMS
          v
+---------------------+
|        AWS KMS      |
|  (with your CMK)    |
+---------------------+
          |
          | 2. Returns:
          |    - Plaintext Data Key
          |    - Encrypted Data Key (encrypted with CMK)
          v
+---------------------+
|  Your Application   |
+---------------------+
          |
          | 3. Uses Plaintext Data Key to Encrypt Data
          v
+---------------------+
| Encrypted Data File |
| + Encrypted Data Key|
+---------------------+
```

---

## 1. AWS Key Management Service (KMS) & Envelope Encryption
AWS KMS handles creation and management of customer master keys (CMKs) to encrypt data at rest.

### A. Envelope Encryption Mechanics
Envelope encryption uses a master key (CMK) to protect a data key, which encrypts the actual data:
1.  **Request:** The application requests a Data Key from KMS using a CMK.
2.  **Response:** KMS generates the Data Key and returns two copies: a **Plaintext Data Key** and an **Encrypted Data Key** (encrypted by the CMK).
3.  **Encryption:** The application encrypts the payload using the Plaintext Data Key, then immediately discards the Plaintext Data Key from memory.
4.  **Storage:** The application stores the encrypted payload alongside the Encrypted Data Key.
5.  **Decryption:** The application sends the Encrypted Data Key to KMS, which decrypts it using the CMK and returns the Plaintext Data Key. The application then decrypts the data.

Certainly! To help you visualize how AWS Key Management Service (KMS) and Customer Master Keys (CMKs) work, here's a simplified diagram illustrating the encryption process:

---

### 🔐 **AWS KMS Encryption Process Overview**

```
+---------------------+
|  Your Application   |
+---------------------+
          |
          | 1. Request Data Key from KMS
          v
+---------------------+
|        AWS KMS      |
|  (with your CMK)    |
+---------------------+
          |
          | 2. Returns:
          |    - Plaintext Data Key
          |    - Encrypted Data Key (encrypted with CMK)
          v
+---------------------+
|  Your Application   |
+---------------------+
          |
          | 3. Uses Plaintext Data Key to Encrypt Data
          v
+---------------------+
| Encrypted Data File |
| + Encrypted Data Key|
+---------------------+
```

---

### 📝 **Step-by-Step Explanation**

1. **Requesting a Data Key**: Your application requests a data key from AWS KMS to encrypt data.
    
2. **KMS Responds**: AWS KMS generates a data key and returns two versions:
    
    - **Plaintext Data Key**: Used immediately by your application to encrypt data.
        
    - **Encrypted Data Key**: The same data key encrypted with your CMK; stored securely for future decryption.
        
3. **Encrypting Data**: Your application uses the plaintext data key to encrypt your data and then discards the plaintext key from memory.
    
4. **Storing Encrypted Data**: You store the encrypted data along with the encrypted data key.([Medium](https://crishantha.medium.com/aws-kms-4cb9bb80c89?utm_source=chatgpt.com "AWS KMS - Crishantha Nanayakkara - Medium"))
    
5. **Decrypting Data**: When you need to decrypt the data, your application sends the encrypted data key to AWS KMS, which decrypts it using your CMK and returns the plaintext data key. Your application then uses this key to decrypt the data.
    

---

### 📺 **Visual Learning**

For a more in-depth visual explanation, you might find this video helpful:

[AWS Key Management Service | Fully Visualized](https://www.youtube.com/watch?pp=ygUOI2JlbmVmaXRzb2ZrbXM%3D&v=z7bzr0AZDsE&utm_source=chatgpt.com)


---

## 2. Key Types & Management
*   **Symmetric Keys:** A single 256-bit AES key used for encryption/decryption. The CMK never leaves the secure boundaries of KMS.
*   **Asymmetric Keys:** Public/Private key pairs used for signing/verification or encryption/decryption.
*   **AWS-Managed Keys:** Free, automatically created on your behalf by AWS (e.g., `aws/s3`). Rotated every 3 years. Cannot be shared across accounts.
*   **Customer-Managed Keys:** Managed by you. Cost $1/month. Allow granular key policies, optional 1-year rotation, and cross-account sharing.

---

## 3. Secrets Manager & Parameter Store
AWS provides two options for managing configurations and secrets:
*   **AWS Systems Manager Parameter Store:** A secure, serverless store for hierarchical configuration data. Free for standard parameters. Does not support automatic rotation natively.
*   **AWS Secrets Manager:** A paid service ($0.40/secret/month) specifically designed for sensitive credentials. Supports auto-rotation (e.g., RDS passwords via Lambda integration) and cross-account access.

---

## 4. Encryption on EC2 and EBS (Eissa Notes)


EBS Snapshot its a best practice to always take snapshots of you EBS as backups 

Amazon S3 bucket will be on the same region, We can Copy the snapshot on another region its acceptable, The S3 will be automatically created by amazon no need for me to handle anything  
Snapshots is accessed in EC2 Dashboard i don't have an access to the S3 Bucket 

![[Pasted image 20250501132311.png]]

![[Pasted image 20250501132337.png]]


Through DLM or cloud watch events you can set expiration Date for the snapshots and according to the case scenario we set the expiration date...(THINK OF IT AS EBS ORCHESTERATOR)

cloud watch handles  1 ---> EBS 
DLM handles multiple ---> EBS 
![[Pasted image 20250501132138.png]]


-------------
===================================================================

Encryption Occurs on the EC2 Host so its Encrypted on Transit and sits Encrypted in the EBS Encrypted all the way ... 

The Decryption happens on the EC2 host only so the host can use the data 

EBS works with symmetric keys as from 2021 

![[Pasted image 20250501132728.png]]

KMS ---> Key management System

The CMK's never leaves the KMS, we give desired accounts or user access permissions to the KMS but we never share the CMK 

we use AWS manged keys ( default CMK ), every thing is handled by aws I can only see logs for auditing

unlike customer managed keys every thing is managed by me 
- Rotation
- policies for who can use it
- Change key periodically 
- Auditing on key usage 

-------------------
====================================================================

![[Pasted image 20250501133758.png]]


EBS is available For a specific AZ 
Snapshot is available across the region all AZ's under the same region 
Snapshot can be saved in other Regions under EC2 snapshot it will be found 

so snapshot can break all EC2 limits 

--------------------------------
====================================================================

The Best approach is to know if i want to create an Encrypted EBS volume or not before doing it, there are work around if I wanted to encrypt it after it was created but its a hassle..........

![[Pasted image 20250501134724.png]]

---

## 5. Audit & Monitoring Services
- **Higher Fault tolerance** means higher cost, due to increase of resources. If the application didn't react in real time in fault scenarios the application will not be considered fault tolerance 
![Pasted image 20221103042616](https://user-images.githubusercontent.com/109697567/200859632-0ad6166f-a411-4e40-9088-8b4c2930742d.png)

## Scalability & Elasticity
### Scalability 
- Scalability refers to system's ability to handle the growth of load by adding resources.
- This scaling can be vertical scaling (up/down) or horizontal scaling(out/in).
 ![Pasted image 20221103043119](https://user-images.githubusercontent.com/109697567/200859709-cc84e90c-9afd-4851-90fa-87e2878137ac.png)
### Elasticity 
  
- Elasticity describes the system ability to provision &  deprovision resources **automatically** to ensure that resources matches the need. 
- **Auto scaling groups can be configured for EC2 instances**, There  are another auto scaling type called Application Autoscaling will be covered later 
- **Autoscaling is always accompanied with load balancer** in design to ensure high availability  

> [!NOTE]
> - Remember we need to take in consideration the time need for horizontal scaling to start executing it needs triggers from cloud watch and autoscaling groups health checks then start in creating the EC2 instances and EC2 instance may need Minutes to initialize so if it was a 1 min spike in traffic, The application has failed to be fault tolerant we tackle more of this in later videos  

![[Pasted image 20250512092901.png]]

## CloudWatch
- CloudWatch is the center of real time monitoring & visibility in AWS.
- It's a metric data repository "per resource".
- Has the ability to add a custom metric.
- Provides statistics & logs.
- Monitors alarms can be set & can trigger actions
![[Pasted image 20250512103020.png]]
## CloudTrail
- Any actions "APIs" taken by IAM users, roles or AWS services are recorded in CloudTrail.
- Events can be viewed & downloaded.
- It helps in governance & auditing the account.
- Events history are maintained for 90 days.
- Logs can be stored in a S3 Bucket for more than 90 days if desired, **this is encrypted by default.**
- CloudTrail is integrated with SNS.
- A trail created in the console is a multi-region trail, use the command interface to make a region trail.
  so Console cloud trail is multi-region scope
  And CLI if I want to make a single region trail 
![[Pasted image 20250512103915.png]]
### Logs Events types
#### 1- Management event
- Provide visibility into management & operations on resources.
- Free of charge.
- Enabled  by default.
#### 2- Data event 
- Provide visibility into resource level operations "objects in a bucket".
- Chargeable.
- Disabled by default.
#### 3- Insights Events
- Logs events for unusual API write activates in the account.
- Chargeable.
- Disabled by default.

### Log File Integrity Validation
- The ability of CloudTrail to determine whether a log file was modified, changed or deleted after delivering the logs to an S3 Bucket.
- This is beneficial in forensics investigations.
- Using a validation log file, you can accurately determine whether a log file was changed or not, & **if so shows the user credentials involved in this activity.**
- **This is done by creating a hash for every log file delivered.**


---

## 6. Supplemental Hands-on SAA Labs & HA Design

### A. SQS, RDS, and High Availability / Fault Tolerance Lab
![[Pasted image 20250512085552.png]]

the Web/app programming will be modified to communicate with the SQS instead of the database 
**Lambda function is used in architectures like this to take the data in the SQS and write it in the RDS** 

![[Pasted image 20250512090125.png]]

Any Project that has Design requirements it is divided into functional requirements and non functional requirements 

we need to understand and study the platform in order to be able to design and implement according to the available services and its limitations 


![[Pasted image 20250512101213.png]]

![[Pasted image 20250512102552.png]]

----------


With the load balancer and the two EC2 instance we achieved high availability, Now suppose we added an Autoscaling group to guarantee the existence of two EC2 instance so if of one of the two EC2 terminated the AG will create another one in any of the two AZ either the same or another available its AG responsibility, so by adding two EC2 with LB we are highly available but the AG should be added and its always comes with a package when LB is mentioned  

But are we 100% fault tolerant ?? 
Absolutely not because when AG executes the Boot time may be minutes so the application behavior will be affected until its ready to receive traffic  

In case of using container instead of VM the boot process will be faster and in scenarios like these we may be fault tolerant 

To be fault tolerant 
Suppose a third AZ and its in the AG and the three instance is up and they are the minimum to run my app , with threshold 60% cpu usage now we guaranteed 100% fault tolerance and elasticity  


![[Pasted image 20250512104739.png]]











### B. Elastic Load Balancer (ELB) Projects
# AWS Elastic load balancer (ELB)
## project 1
working with health checks of load balancer groups 
![[Pasted image 20250529160044.png]]

## project 2
![[Pasted image 20250626140433.png]]

![[Pasted image 20250626140557.png]]

![[Pasted image 20250626141215.png]]




## project 3

![[Pasted image 20250626151341.png]]

![[Pasted image 20250626151400.png]]

## project 4

![[Pasted image 20250626150847.png]]

![[Pasted image 20250626150926.png]]




## Project 5


### C. Auto Scaling Group (ASG) Projects
# AutoScaling Group
![[Pasted image 20250626165425.png]]

![[Pasted image 20250626165815.png]]

---

## 7. Deep-Intuition (AARF) Breakdowns

### AARF Breakdown: KMS Customer Managed Keys (CMK)
1.  **The Answer (Core Pattern):** Utilize KMS Customer Managed Keys (CMKs) with explicit IAM Key Policies restricting access to authorized execution roles:
    ```json
    {
      "Sid": "AllowUseOfTheKey",
      "Effect": "Allow",
      "Principal": {"AWS": "arn:aws:iam::123456789012:role/AppExecutionRole"},
      "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey*"
      ],
      "Resource": "*"
    }
    ```
2.  **The Assumptions (Context):** The calling application role must have permission to access both the target storage resource (e.g., S3 bucket, EBS volume) *and* the KMS key used for envelope encryption.
3.  **The Rationale (Why):** Implements separation of duties. Restricting key permissions ensures that even if a user bypasses S3 bucket policies, they cannot read data without decrypting it, providing a double-barrier security topology and complete CloudTrail auditing.
4.  **The Failure Loop (What if not):** If IAM roles have S3 access but lack KMS Decrypt permissions on the custom CMK, application read API requests fail with `Access Denied` or `KMS.AccessDeniedException`, causing application crashes during startup or retrieval.
5.  **Alternative Case (When to use 'if not'):** For non-sensitive, high-volume workloads where API call costs are a major concern, use S3 Managed Keys (SSE-S3) to completely bypass KMS transaction charges.

