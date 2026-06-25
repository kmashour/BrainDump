---
domains:
  - "aws"
class: reference-note
tier: reference-note
tags:
  - aws/management
  - aws/deployment
  - aws/billing
  - aws/governance
---

# Module 3-20: AWS Deployment, Management & Optimization Services

This module covers infrastructure deployment tools (CloudFormation, Amplify), hybrid cloud configurations (Outposts), batch operations (Batch), system management utilities (Systems Manager suite), marketing communications (SES, Pinpoint), billing tools, and the AWS Well-Architected Framework.

---

## 🗺️ Cognitive Map: Management & Observability Operations

To build a strong intuition for deployment and management operations, think of the services grouped by operational domains:

```mermaid
flowchart TD
    subgraph Provisioning ["Infrastructure Provisioning"]
        CFN["CloudFormation (IaC Engine)"]
        Amplify["Amplify (Web/Mobile App Fabric)"]
    end

    subgraph Management ["Fleet & Operations Management"]
        SSM_SM["SSM Session Manager (Secure SSH)"]
        SSM_RC["SSM Run Command (Remote Scripts)"]
        SSM_PM["SSM Patch Manager (OS Updates)"]
        SSM_Auto["SSM Automation (Runbooks)"]
    end

    subgraph Compute_Hybrid ["Hybrid & Batch Compute"]
        Outposts["Outposts (On-Premises AWS Racks)"]
        Batch["AWS Batch (Docker Jobs on EC2/Fargate)"]
    end

    subgraph Billing_Frameworks ["Cost & Architecture Governance"]
        CostExplorer["Cost Explorer / Anomaly Detection"]
        WATool["Well-Architected Tool"]
        TrustedAdvisor["Trusted Advisor"]
    end
```

---

## 1. Infrastructure Provisioning as Code

### AWS CloudFormation
*   **Purpose:** Declarative Infrastructure as Code (IaC) engine. Outlines infrastructure stacks in JSON or YAML templates.
*   **Change Sets:** Previews changes before they are applied. Displays whether resources will be added, modified, or replaced.
    *   *Replacement behavior:* Certain properties (like AvailabilityZone or DB engines) require recreating the resource (`Replacement: True`). This causes downtime and deletes ephemeral data.
*   **Tag Propagation:** Stack-level tags are automatically inherited and applied to all supported resources in the stack.
*   **CloudFormation Service Roles:** Dedicated IAM roles that delegate permissions to CloudFormation to create, update, and delete resources. This enforces the least-privilege model because users only need permissions to execute the stack, not direct access to resources (requires the user to have the `iam:PassRole` permission).

### AWS Amplify
*   **Purpose:** A development platform for building web and mobile applications (often compared to "Elastic Beanstalk for mobile/web apps").
*   **Architecture:** Automates provisioning backends (S3, Cognito, API Gateway, AppSync, Lambda, DynamoDB) via its CLI, connects them to frontend libraries (React, iOS, Android), and deploys host assets via CloudFront.

---

## 2. Fleet & Operations Management (AWS Systems Manager)

AWS Systems Manager (SSM) provides operational control over EC2 instances and on-premises servers via the **SSM Agent**.

### SSM Session Manager
*   **Purpose:** Starts secure terminal shells on EC2 instances or on-premises servers without opening inbound SSH port 22, managing SSH keys, or hosting bastion instances.
*   **Prerequisites:** The instance must run the SSM Agent and have an IAM instance profile with the `AmazonSSMManagedInstanceCore` policy attached. Fleet Manager monitors online agent status.
*   **Security:** Access is controlled via IAM. Terminal inputs/outputs are logged directly to S3 or CloudWatch Logs for audit compliance.

### SSM Run Command
*   **Purpose:** Executes shell commands or SSM Documents (scripts) on multiple instances simultaneously using Resource Groups.
*   **Features:** Operates without SSH. Command outputs are saved to S3/CloudWatch, updates route to SNS, and executions are audited via CloudTrail.

### SSM Patch Manager
*   **Purpose:** Automates patching operating systems, applications, and security updates on Linux, macOS, and Windows.
*   **Execution:** Scans or installs patches on-demand or on schedules defined by **Maintenance Windows** (which specify triggers, duration, targets, and tasks). Generates compliance reports of patch states.

### SSM Automation
*   **Purpose:** Simplifies common maintenance tasks (e.g., stopping/starting fleets, building AMIs, taking snapshots) using declarative SSM Documents called Runbooks.
*   **Triggers:** Executed manually, or automatically via EventBridge, Maintenance Windows, and AWS Config remediation rules.

---

## 3. Hybrid & Batch Compute

### AWS Outposts
*   **Purpose:** Extends AWS infrastructure, APIs, and tools directly to on-premises data centers by deploying physical, AWS-managed server racks in customer data centers.
*   **Supported Services:** EC2, EBS, S3, EKS, ECS, RDS, EMR.
*   **Shared Responsibility:** AWS manages the hardware, but **the customer is responsible for the physical security of the Outposts rack**.
*   **Benefits:** Sub-millisecond latency to local systems, local data processing, and compliance with data residency requirements.

### AWS Batch
*   **Purpose:** Managed batch processing service that runs containerized jobs at scale.
*   **Compute Tier:** Dynamically provisions EC2 or Spot Instances to process job queues, executing Docker images on ECS, EKS, or Fargate.
*   **Batch vs. Lambda:**
    *   **Lambda:** Serverless, strictly capped at a 15-minute timeout, limited runtime environments, and up to 10 GB ephemeral `/tmp` storage.
    *   **Batch:** No execution time limit, runs any runtime packaged as a Docker image, has access to EC2 storage (EBS/Instance Store), but requires managing container execution parameters.

---

## 4. Marketing & Integration Services

### Amazon SES (Simple Email Service)
*   **Purpose:** Managed transactional and marketing email service.
*   **Features:** Sends bulk emails via SMTP or SES APIs. Supports SPF and DKIM security. Includes reputation dashboards to track deliverability, bounces, and spam feedback loops.

### Amazon Pinpoint
*   **Purpose:** Two-way multichannel marketing campaign communications manager (Email, SMS, Push, Voice, In-app messaging).
*   **Pinpoint vs. SES/SNS:**
    *   **SNS/SES:** The application must manage customer lists, scheduling, templates, and tracking metrics manually.
    *   **Pinpoint:** Natively manages user segmentation, scheduling, templates, and full campaigns, sending metrics back to S3/CloudWatch.

### Amazon AppFlow
*   **Purpose:** A managed integration service that transfers data between SaaS applications (e.g. Salesforce, SAP, Slack, Zendesk) and AWS destinations (S3, Redshift) privately using AWS PrivateLink.

---

## 5. Billing & Cost Management

### AWS Cost Explorer
*   **Purpose:** Visualizes and manages AWS cost and usage over time, forecasting future costs (up to 18 months) and recommending Savings Plans.

### AWS Cost Anomaly Detection
*   **Purpose:** Monitors cost usage data using machine learning to detect cost anomalies (one-time spikes or continuous increases) without defining manual thresholds. Alerting routes to SNS.

### AWS Instance Scheduler
*   **Purpose:** An AWS CloudFormation solution that schedules starting and stopping EC2, RDS, and Auto Scaling instances (e.g. stopping development servers outside of 9-to-5 business hours to save up to 70% in compute costs). Uses DynamoDB for schedules and Lambda for execution.

---

## 6. Architectural Governance & Whitepapers

### AWS Well-Architected Framework
Provides architectural best practices categorized into **six pillars**:
1.  **Operational Excellence:** Run and monitor systems, continually improving processes.
2.  **Security:** Protect data, systems, and assets.
3.  **Reliability:** Ensure workloads perform intended functions consistently and recover from failures.
4.  **Performance Efficiency:** Use compute resources efficiently as demand changes.
5.  **Cost Optimization:** Run systems to deliver business value at the lowest price point.
6.  **Sustainability:** Minimize the environmental impacts of running cloud workloads.

#### Core Design Guidelines:
*   Stop guessing capacity needs (use scaling).
*   Test systems at production scale.
*   Automate to make architectural experimentation easier.
*   Allow for evolutionary architectures.
*   Drive architectures using data.
*   Improve operations through game days (failure simulations).

### AWS Well-Architected Tool
*   **Purpose:** An assessment tool where users review workloads against the six pillars to generate risk identification reports (High/Medium risks) and improvement plans.

### AWS Trusted Advisor
*   **Purpose:** Scans the account to recommend optimizations across six categories: **Cost Optimization, Performance, Security, Fault Tolerance, Service Limits, and Operational Excellence**.
*   **Support Tiers:**
    *   *Basic/Developer Support:* Limited access to core security and service limit checks.
    *   *Business/Enterprise Support:* Unlocks full checks (over 100+) and Support API access.

---

## 7. Deep-Intuition Architectural Breakdowns (AARF)

### Systems Access: Session Manager vs. EC2 Instance Connect vs. SSH
*   **The Answer:** Use SSM Session Manager for secure, keyless CLI shell access with port 22 closed; use EC2 Instance Connect to push temporary SSH keys when SSH client tools are required; use traditional SSH only when SSM or IAM integrations are unavailable.
*   **The Assumptions:** Session Manager requires the SSM Agent and private network access to the SSM endpoint; EC2 Instance Connect requires port 22 to be open to the service's IP ranges and public IP access.
*   **The Rationale (Why):** Closing port 22 eliminates the threat of external brute-force port scans. Logging terminal actions directly to CloudWatch Logs provides audit trails that cannot be modified by local users.
*   **The Failure Loop (What if not):** If you configure EC2 Instance Connect but block port 22 in the instance's Security Group, the browser-based connect terminal will timeout and fail to connect.

### Marketing Operations: Amazon SES vs. Amazon Pinpoint
*   **The Answer:** Select SES to send transactional emails triggered by code (e.g., password reset emails); select Pinpoint to manage targeted marketing campaigns and SMS blasts.
*   **The Assumptions:** SES requires domain validation and handles raw message delivery; Pinpoint sits on top of SES/SMS channels, managing campaign schedules, user lists, and templates.
*   **The Rationale (Why):** Transactional emails are single, code-initiated notifications. Marketing campaigns require audience segmentation, A/B testing, and campaign scheduling.
*   **The Failure Loop (What if not):** If a marketing team attempts to run a newsletter campaign using raw SES API calls, developers must write custom database systems to handle user subscription preferences, tracking metrics, and email bounces, introducing code complexity.

---

## 8. Decoupled Verification Projects

Step-by-step configurations for declaring stacks as code, launching updates, and evaluating change set replacements are compiled in the following project:
*   *See complete implementation in [[Projects/aws-cloudops/Project - CloudFormation Stack Updates and Change Sets.md]]*
