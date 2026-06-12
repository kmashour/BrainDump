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

- 🔑 **[Module 3-1: AWS Global Infrastructure](3-1_aws_global_infrastructure.md)**
  * Physical footprint, Regions, Availability Zones, Edge Locations, cloud deployment & service models, and the 6 pillars of the Well-Architected Framework.
- 👤 **[Module 3-2: AWS IAM & Governance](3-2_aws_iam.md)**
  * IAM Users, Groups, Roles, Policies, programmatic access, and temporary security credentials via AWS STS. AWS Organizations structure, consolidated billing, and Service Control Policies (SCPs).
- 🔐 **[Module 3-3: AWS KMS & Cryptographic Encryption](3-3_aws_kms_security.md)**
  * AWS KMS Customer Master Keys (CMKs), envelope encryption mechanics, Symmetric/Asymmetric keys, IAM Key Policies, and AWS Secrets Manager.
- 🖥️ **[Module 3-4: AWS Compute & EC2 Architecture](3-4_aws_ec2_compute.md)**
  * EC2 instance families, VM lifecycle states, stop-hibernate mechanics, User Data bootstrapping, IMDSv2 security, purchasing/launch types, and placement groups.
- 💾 **[Module 3-5: AWS EBS & EFS Storage](3-5_aws_ebs_efs_storage.md)**
  * EBS volume types, snapshots, encryption, instance store (ephemeral), and EFS shared filesystem architectures.
- 🪣 **[Module 3-6: AWS S3 Object Storage](3-6_aws_s3_storage.md)**
  * S3 storage classes, bucket policies, access control lists (ACLs), versioning, replication, lifecycle management, and Athena integration.
- 🗄️ **[Module 3-7: AWS Relational Databases (RDS & Aurora)](3-7_aws_rds_aurora_databases.md)**
  * Managed relational databases (RDS), backups/snapshots, Multi-AZ deployments, Read Replicas, Aurora cloud-native storage, and Database Migration Service (DMS/SCT).
- ⚡ **[Module 3-8: AWS NoSQL (DynamoDB), Caching & Redshift](3-8_aws_dynamodb_nosql.md)**
  * DynamoDB partition design, RCUs/WCUs, DynamoDB Accelerator (DAX), ElastiCache (Redis vs Memcached), and Redshift data warehouse.
- 🌐 **[Module 3-9: AWS VPC Networking](3-9_aws_vpc_networking.md)**
  * VPC CIDR blocks, public/private subnets, Route Tables, Internet Gateways (IGW), NAT Gateways vs NAT Instances, VPC Peering, Transit Gateway, VPC Flow Logs, and Endpoint interfaces/gateways.
- ⚖️ **[Module 3-10: AWS ELB Elastic Load Balancing](3-10_aws_elb_load_balancing.md)**
  * ALB vs NLB vs CLB, target groups, listener rules, health checks, cross-zone load balancing, connection draining, SSL offloading vs TCP passthrough, and SNI.
- 📈 **[Module 3-11: AWS ASG Auto Scaling Groups](3-11_aws_asg_auto_scaling.md)**
  * ASG scaling policies (target tracking, simple, step), launch templates, cooldown/warm-up periods, and lifecycle hooks.
- 🗺️ **[Module 3-12: AWS Route 53 DNS](3-12_aws_route53_dns.md)**
  * Route 53 Hosted Zones, and routing policies: simple, weighted, latency, failover, geolocation, geoproximity, and multivalue.
- 🚀 **[Module 3-13: AWS CloudFront CDN](3-13_aws_cloudfront_cdn.md)**
  * CloudFront CDN distributions, origins, behaviors, edge caching, OAI/OAC, and Signed URLs/Cookies.
- 🔄 **[Module 3-14: AWS SQS & SNS Decoupling](3-14_aws_sqs_sns_decoupling.md)**
  * SQS Standard vs FIFO queues, dead-letter queues, SNS fan-out architectures, EventBridge event routing, and Lambda integrations.
- 🛡️ **[Module 3-15: AWS Disaster Recovery](3-15_aws_disaster_recovery.md)**
  * Backup & Restore, Pilot Light, Warm Standby, Multi-Site active-active disaster recovery patterns, and RPO vs RTO SLA metrics.
- 🧪 **[Module 3-16: AWS SAA Playbook & Labs](3-16_aws_saa_playbook_labs.md)**
  * SAA hands-on lab scenario walkthroughs: EC2 IAM role access, SQS decoupled order flows, and high availability web tier.

---

## 🛠️ Verification Projects
- 🚀 **[Project: Secure Load-Balanced Web API](../Projects/Systems%20Design/Project%20-%20Secure%20Load-Balanced%20Web%20API.md)**
