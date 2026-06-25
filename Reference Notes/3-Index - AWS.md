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

This index contains our Amazon Web Services (AWS) cloud architecture modules, decoupled for future certification studies and extensions.

- 🔑 **[Module 3-1: AWS Global Infrastructure](3-1_aws_global_infrastructure.md)**
  * Physical footprint, Regions, Availability Zones, Edge Locations, cloud benefits, TCO, Capex vs Opex, and support levels.
- 👤 **[Module 3-2: AWS IAM & Identity Management](3-2_aws_iam.md)**
  * STS, policies, groups, users, roles, SCPs, and Organizations governance.
- 🔐 **[Module 3-3: AWS KMS & Security Services](3-3_aws_kms_security.md)**
  * Envelope encryption, Customer Managed Keys (CMKs), Secrets Manager, Parameter Store, Cognito, WAF, and Shield.
- 🖥️ **[Module 3-4: AWS EC2 Compute](3-4_aws_ec2_compute.md)**
  * EC2 instance types, placement groups, AMI, User Data, instance lifecycle, IMDSv1/v2, purchasing models.
- 💾 **[Module 3-5: AWS EBS & EFS Storage](3-5_aws_ebs_efs_storage.md)**
  * gp3 vs io2 block performance, EFS network volumes, local Instance Store.
- 🪣 **[Module 3-6: AWS S3 Storage](3-6_aws_s3_storage.md)**
  * Storage classes, S3 bucket policies, versioning, replication, Transfer Acceleration, Athena queries.
- 🗄️ **[Module 3-7: AWS RDS & Aurora Databases](3-7_aws_rds_aurora_databases.md)**
  * RDS Multi-AZ, Read Replicas, Aurora architecture, endpoints, database migrations (DMS/SCT).
- ⚡ **[Module 3-8: AWS DynamoDB & NoSQL](3-8_aws_dynamodb_nosql.md)**
  * DynamoDB partition keys, DAX cache, provisioning RCU/WCU, ElastiCache, Redshift.
- 🕸️ **[Module 3-9: AWS VPC Networking](3-9_aws_vpc_networking.md)**
  * Subnets, routing tables, IGW, NAT Gateways vs Instances, Peering, Transit Gateway, Flow Logs.
- 🔌 **[Module 3-10: AWS Elastic Load Balancing (ELB)](3-10_aws_elb_load_balancing.md)**
  * ALB vs NLB, connection draining, SSL offloading, passthrough, SNI, cross-zone routing.
- 📈 **[Module 3-11: AWS Auto Scaling Groups (ASG)](3-11_aws_asg_auto_scaling.md)**
  * Target tracking, simple, step scaling policies, launch templates, lifecycle hooks.
- 🌐 **[Module 3-12: AWS Route 53 DNS](3-12_aws_route53_dns.md)**
  * DNS routing policies (geolocation, latency, failover), health checks, Hosted Zones.
- 🚀 **[Module 3-13: AWS CloudFront CDN](3-13_aws_cloudfront_cdn.md)**
  * CDN behaviors, origins, edge caching, OAC bucket protection, Signed URLs.
- ✉️ **[Module 3-14: AWS SQS & SNS Decoupling](3-14_aws_sqs_sns_decoupling.md)**
  * SQS standard vs FIFO, dead-letter queues, SNS fan-out patterns, EventBridge.
- 🛡️ **[Module 3-15: AWS Disaster Recovery (DR)](3-15_aws_disaster_recovery.md)**
  * Backup & Restore, Pilot Light, Warm Standby, Multi-Site active-active, RPO vs RTO.
- 🧪 **[Module 3-16: AWS SAA Playbook & Labs](3-16_aws_saa_playbook_labs.md)**
  * Hands-on walk-through scenarios, EC2 role access, SQS order processing, highly available tiers.
- 🐳 **[Module 3-17: AWS Containers (ECS, EKS & ECR)](3-17_containers_ecs_eks.md)**
  * Docker primitives, ECS clusters, Task/Execution roles, Fargate serverless, EKS nodes, and Auto Mode.
- ⚡ **[Module 3-18: AWS Serverless (Lambda, API Gateway, DynamoDB & Cognito)](3-18_serverless.md)**
  * Lambda pricing/concurrency/SnapStart, API Gateway endpoints, DynamoDB modes/DAX/streams, and Cognito identity flows.
- 📊 **[Module 3-19: AWS Databases, Analytics & Machine Learning Services](3-19_databases_analytics_ml.md)**
  * Redshift data warehouse, Neptune graphs, Timestream time-series, Keyspaces Cassandra, Athena SQL, Glue catalog, Lake Formation security, MSK Kafka, and AWS ML/SageMaker models.

---

## 🛠️ Verification Projects
- 🚀 **[Project: Secure Load-Balanced Web API](../Projects/Systems%20Design/Project%20-%20Secure%20Load-Balanced%20Web%20API.md)**
- ☸️ **[Project: ECS and EKS Cluster Deployments](../Projects/kubernetes/Project%20-%20ECS%20and%20EKS%20Cluster%20Deployments.md)**
- ⚡ **[Project: Serverless REST API with Lambda and API Gateway](../Projects/kubernetes/Project%20-%20Serverless%20REST%20API%20with%20Lambda%20and%20API%20Gateway.md)**
- 📊 **[Project: Athena S3 Access Log Analytics](../Projects/aws-cloudops/Project%20-%20Athena%20S3%20Access%20Log%20Analytics.md)**
