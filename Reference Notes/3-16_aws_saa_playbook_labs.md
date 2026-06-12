---
domains:
  - "aws"
  - "labs"
---

# Module 3-16: AWS SAA Playbook & Labs

**Breadcrumbs:** [[3-Index - AWS|📐 AWS Index]] > **Module 3-16: AWS SAA Playbook & Labs**

This module provides step-by-step walkthroughs of practical AWS Solution Architect Associate (SAA) lab scenarios.

---

## 🧪 Lab Scenario 1: EC2 to S3 IAM Role Access (No Hardcoded Credentials)

### A. The Objective
An application running on an EC2 instance needs to list objects inside an S3 bucket without storing static Access Keys.

### B. Architecture Walkthrough
1. Create a custom IAM Role (e.g., `EC2S3ReadRole`) with trust policies allowing the EC2 service principal (`ec2.amazonaws.com`) to assume the role.
2. Attach a policy to the role allowing S3 listing:
    ```json
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": ["s3:ListBucket", "s3:GetObject"],
          "Resource": ["arn:aws:s3:::my-target-bucket", "arn:aws:s3:::my-target-bucket/*"]
        }
      ]
    }
    ```
3. Attach the role to an **EC2 Instance Profile** and bind the profile to the EC2 instance.
4. SSH into the instance and run:
    ```bash
    aws s3 ls s3://my-target-bucket
    ```
5. *Result:* The AWS CLI queries the local metadata service (IMDSv2), retrieves temporary STS credentials, and successfully lists S3 contents.

![[../Attachments/Pasted image 20250508152603.png]]
![[../Attachments/Pasted image 20250508152636.png]]
![[../Attachments/Pasted image 20250511001805.png]]
![[../Attachments/Pasted image 20250511002017.png]]

---

## 🧪 Lab Scenario 2: Decoupled Order Processing Pipeline

### A. The Objective
A web tier processes order requests. If database writes spike or fail, order requests must not be lost.

### B. Architecture Walkthrough
1. The frontend application publishes order details as JSON payloads to an **SQS Queue**.
2. An **AWS Lambda** function is triggered by SQS queue events:
    * It polls messages from the queue.
    * It processes the message and writes the transaction to an **RDS Database**.
3. If database connections are exhausted:
    * The Lambda function fails to process the order.
    * The message is returned to the SQS queue (due to visibility timeout).
    * If a message fails processing 5 times, it is shipped to a **Dead-Letter Queue (DLQ)** for inspection, preventing database loss.

![[../Attachments/Pasted image 20250509102913.png]]
![[../Attachments/Pasted image 20250509103328.png]]
![[../Attachments/Pasted image 20250512085552.png]]
![[../Attachments/Pasted image 20250512090125.png]]

---

## 🧪 Lab Scenario 3: Highly Available and Fault-Tolerant Web Tier

### A. The Objective
Design a multi-tier web application spanning multiple AZs that survives single instance failures and AZ outages.

### B. Architecture Walkthrough
1. Deploy a custom VPC with public and private subnets across 2 AZs.
2. Place an **Application Load Balancer (ALB)** in the public subnets.
3. Configure an **Auto Scaling Group (ASG)** to run EC2 targets inside private subnets:
    * Set Min Size to 2, Desired to 2, and Max to 4.
    * Associate the targets with the ALB target group.
4. Deploy a **NAT Gateway** in each public subnet so the private EC2 instances can download package updates.
5. Deploy a managed **RDS Database** in Multi-AZ mode inside dedicated private subnets.
6. *Result:* If an EC2 instance crashes, the ALB marks it unhealthy, and the ASG replaces it. If an AZ goes down, the database fails over to the standby AZ, and the ALB routes all traffic to the healthy AZ.

![[../Attachments/Pasted image 20250512101213.png]]
![[../Attachments/Pasted image 20250512102552.png]]
![[../Attachments/Pasted image 20250512104739.png]]

---

## 🧪 Lab Scenario 4: VPC Subnet Routing and NAT Configuration

### A. The Objective
Set up routing rules to isolate database tiers while allowing outbound internet access.

### B. Architecture Walkthrough
1. Set up a VPC with CIDR `10.0.0.0/16`.
2. Create subnets:
    * Public Subnet: `10.0.1.0/24` (AZ A)
    * Private Subnet: `10.0.2.0/24` (AZ A)
3. Deploy an **Internet Gateway (IGW)** and attach it to the VPC.
4. Deploy a **NAT Gateway** in the Public Subnet and allocate an Elastic IP (EIP).
5. Configure the Public Route Table:
    * Destination: `0.0.0.0/0` -> Target: `igw-xxxx`
    * Associate with the Public Subnet.
6. Configure the Private Route Table:
    * Destination: `0.0.0.0/0` -> Target: `nat-xxxx`
    * Associate with the Private Subnet.

![[../Attachments/Pasted image 20250516190254.png]]
![[../Attachments/Pasted image 20250516190953.png]]
![[../Attachments/Pasted image 20250516231854.png]]
![[../Attachments/Pasted image 20250516232519.png]]
![[../Attachments/Pasted image 20250529160044.png]]
![[../Attachments/Pasted image 20250626140433.png]]
![[../Attachments/Pasted image 20250626140557.png]]
![[../Attachments/Pasted image 20250626141215.png]]
![[../Attachments/Pasted image 20250626151341.png]]
![[../Attachments/Pasted image 20250626151400.png]]
![[../Attachments/Pasted image 20250626150847.png]]
![[../Attachments/Pasted image 20250626150926.png]]
![[../Attachments/Pasted image 20250626165425.png]]
![[../Attachments/Pasted image 20250626165815.png]]
