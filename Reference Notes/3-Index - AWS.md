---
obsidianUIMode: preview
class: index-note
tier: reference-note
tags:
  - aws/reference-index
  - obsidian/moc
---

# 📐 AWS Reference MOC

**Breadcrumbs:** [[--Index--|🏠 Index]] > **AWS Reference MOC**

---

## 🏛️ Reference Modules & Frameworks

This index contains our Amazon Web Services (AWS) cloud architecture modules, ranging from foundational Practitioner rules to SAA-level VPC networking and storage designs.

- 🔑 **[Module 3-1: AWS Global Infrastructure & Network Architecture](3-1_aws_global_infrastructure.md)**
  * Physical footprint, Regions, Availability Zones, Edge Locations, CloudFront edge caching invalidations, cloud deployment & provisioning models, the 6 pillars of the Well-Architected Framework, and logical networking (VPC subnets, routing tables, Internet/NAT Gateways, SG/NACL ephemeral ports).
- 👤 **[Module 3-2: AWS IAM & Identity Management](3-2_aws_iam.md)**
  * Identity federation, AWS STS role assumptions, permanent vs temporary credentials, IAM policies, and multi-account governance (AWS Organizations & SCPs).
- 🔐 **[Module 3-3: AWS KMS & Security](3-3_aws_kms_security.md)**
  * KMS customer master keys (CMKs), envelope encryption mechanics, symmetric/asymmetric keys, Secrets Manager vs SSM Parameter Store, Cognito, WAF, and Shield.
- 🖥️ **[Module 3-4: AWS EC2 Compute](3-4_aws_ec2_compute.md)**
  * EC2 instance families, VM lifecycle, User Data bootstrapping, IMDSv1/v2 security, purchasing/launch models (on-demand/spot/savings), placement groups, Elastic Load Balancing (ALB/NLB), Auto Scaling Groups (ASG), and SQS/SNS app integration decoupling.
- 💾 **[Module 3-5: AWS EBS & EFS Storage](3-5_aws_ebs_efs_storage.md)**
  * EBS volume types (gp3 vs io2 Block Express), incremental snapshots, encryption sharing, local ephemeral Instance Store, and network POSIX EFS shared filesystem architectures.
- 🪣 **[Module 3-6: AWS S3 Storage](3-6_aws_s3_storage.md)**
  * S3 storage classes (Standard to Glacier Deep Archive), lifecycle policies, S3 bucket policies, versioning, replication, transfer acceleration, and Athena SQL queries.
- 🗄️ **[Module 3-7: AWS RDS & Aurora Databases](3-7_aws_rds_aurora_databases.md)**
  * RDS Multi-AZ deployments, Read Replicas, Aurora architecture, endpoints, database migrations (DMS), and schema conversion (SCT).
- ⚡ **[Module 3-8: AWS DynamoDB & NoSQL](3-8_aws_dynamodb_nosql.md)**
  * DynamoDB partition design, RCUs/WCUs, DynamoDB Accelerator (DAX) cache, ElastiCache (Redis vs Memcached), and Redshift data warehouse.

---

## 🛠️ Verification Projects
- 🚀 **[Project: Secure Load-Balanced Web API](../Projects/Systems%20Design/Project%20-%20Secure%20Load-Balanced%20Web%20API.md)**
