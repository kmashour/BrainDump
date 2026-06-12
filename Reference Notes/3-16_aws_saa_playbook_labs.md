---
domains:
  - "aws"
class: reference-note
tier: reference-note
tags:
  - aws/labs
---

# Module 3-16: AWS SAA Playbook & Labs

## 8. Supplemental SAA Hands-on Projects & VPC Deep Dive
### A. Global Infrastructure / Architecture Initial Projects

---

# Introduction 


---

## project-1
![[Pasted image 20250508152603.png]]

![[Pasted image 20250508152636.png]]

---

## project-2 
![[Pasted image 20250509102913.png]]


![[Pasted image 20250509103328.png]]


### B. VPC Deep Dive Hands-on Topology

---

# VPC deep dive
![[Pasted image 20250516190254.png]]

With respect to only HA and fault tolerant creating two NAT gateways two bastion hosts that will do and of course the route table routes to the NAT in its AZ 

![[Pasted image 20250516190953.png]]

![[Pasted image 20250516231854.png]]

![[Pasted image 20250516232519.png]]




-----------

---

## 2. Hands-on Lab: EC2 to S3 IAM Role Authentication
This lab demonstrates creating an IAM role and assigning it to an EC2 instance to list and copy files from an S3 bucket without using hardcoded access keys.

### A. IAM Policy Definition
Create a JSON policy (e.g., `s3-read-policy.json`) restricting access to the target bucket:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket",
        "s3:GetObject"
      ],
      "Resource": [
        "arn:aws:s3:::my-secure-config-bucket",
        "arn:aws:s3:::my-secure-config-bucket/*"
      ]
    }
  ]
}
```

### B. Role Configuration
1. Create a trust policy allowing EC2 to assume the role (`ec2-trust-policy.json`):
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```
2. Create the IAM role using the CLI:
```bash
aws iam create-role --role-name EC2-S3-Read-Role --assume-role-policy-document file://ec2-trust-policy.json
```
3. Attach the S3 read policy to the role:
```bash
aws iam put-role-policy --role-name EC2-S3-Read-Role --policy-name S3ReadPolicy --policy-document file://s3-read-policy.json
```
4. Create an Instance Profile and associate it with the EC2 instance:
```bash
aws iam create-instance-profile --instance-profile-name EC2-S3-Profile
aws iam add-role-to-instance-profile --instance-profile-name EC2-S3-Profile --role-name EC2-S3-Read-Role
aws ec2 associate-iam-instance-profile --instance-id i-0123456789abcdef0 --iam-instance-profile Name=EC2-S3-Profile
```

### C. Validation from the EC2 Instance
Log into the EC2 instance and run verification commands:
```bash

---

## project 3
### Lab 
create a EC2 instance and list s3 buckets from the instance (policy)

``` AWS-CLI
aws s3 ls  
``` 

![[Pasted image 20250511001805.png]]

![[Pasted image 20250511002017.png]]

![[Pasted image 20250511004948.png]]
![[Pasted image 20250511005254.png]]



---

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

---

## project 1
working with health checks of load balancer groups 
![[Pasted image 20250529160044.png]]

---

## project 2
![[Pasted image 20250626140433.png]]

![[Pasted image 20250626140557.png]]

![[Pasted image 20250626141215.png]]

---

## project 3
![[Pasted image 20250626151341.png]]

![[Pasted image 20250626151400.png]]

---

## project 4
![[Pasted image 20250626150847.png]]

![[Pasted image 20250626150926.png]]

---

## Project 5
### C. Auto Scaling Group (ASG) Projects

---

# AutoScaling Group
![[Pasted image 20250626165425.png]]

![[Pasted image 20250626165815.png]]

---

---

## 5. Hands-on Configurations & Project Labs
This section documents how to setup load balancing and target group rules.

### A. Load Balancer Listener Rule Configurations
Create a listener rule for an ALB using path-based routing via the AWS CLI:
```bash
aws elbv2 create-rule \
    --listener-arn arn:aws:elasticloadbalancing:us-east-1:123456789012:listener/app/my-alb/50dc6c495c0c9188/f2f7dc8e1b3e839e \
    --conditions '[{"Field":"path-pattern","Values":["/images/*"]}]' \
    --priority 10 \
    --actions '[{"Type":"forward","TargetGroupArn":"arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/images-tg/73e2d6bc24d8a067"}]'
```

### B. Auto Scaling Lifecycle Hook Setup
Configure a lifecycle hook that pauses instance termination to back up logs to S3:
```bash
aws autoscaling put-lifecycle-hook \
    --lifecycle-hook-name BackupLogsHook \
    --auto-scaling-group-name my-web-asg \
    --lifecycle-transition autoscaling:EC2_INSTANCE_TERMINATING \
    --default-result CONTINUE \
    --heartbeat-timeout 3600
```

---

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

---

## project 1
working with health checks of load balancer groups 
![[Pasted image 20250529160044.png]]

---

## project 2
![[Pasted image 20250626140433.png]]

![[Pasted image 20250626140557.png]]

![[Pasted image 20250626141215.png]]

---

## project 3
![[Pasted image 20250626151341.png]]

![[Pasted image 20250626151400.png]]

---

## project 4
![[Pasted image 20250626150847.png]]

![[Pasted image 20250626150926.png]]

---

## Project 5
### C. Auto Scaling Group (ASG) Projects

---

# AutoScaling Group
![[Pasted image 20250626165425.png]]

![[Pasted image 20250626165815.png]]

---

---

## 5. Hands-on Lab: Configuring S3 Bucket Policies
Create a bucket policy restricting reads strictly to specific IAM Roles inside an organization:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowSpecificRole",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-secure-data-bucket/*",
      "Condition": {
        "ArnEquals": {
          "aws:PrincipalArn": "arn:aws:iam::123456789012:role/AppExecutionRole"
        }
      }
    }
  ]
}
```
