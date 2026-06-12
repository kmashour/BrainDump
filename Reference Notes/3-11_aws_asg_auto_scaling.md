---
domains:
  - "aws"
  - "compute"
---

# Module 3-11: AWS ASG Auto Scaling Groups

**Breadcrumbs:** [[3-Index - AWS|📐 AWS Index]] > **Module 3-11: AWS ASG Auto Scaling Groups**

This module covers EC2 Auto Scaling Group (ASG) capacity management, scaling policies, lifecycle transitions, and load balancer integrations.

---

## 📈 Auto Scaling Group Mechanics

An Auto Scaling Group (ASG) maintains a fleet of EC2 instances based on defined boundaries:
* **Min Size:** The absolute minimum number of instances that must be active.
* **Max Size:** The limit of scale-out capacity.
* **Desired Capacity:** The target running capacity. If not specified, it defaults to the Min Size.

---

## ⚙️ Launch Templates & Health Checks

* **Launch Templates:** Defines the VM configuration: AMI ID, instance type, key pair, security groups, and User Data script. Version control enabled.
* **ASG Health Checks:**
  * *EC2 Status Checks (Default):* Monitors host hardware and guest OS hypervisor status.
  * *ELB Health Checks:* Monitors application-level status codes (e.g., HTTP 200). If a target fails the ELB check, the ASG terminates and replaces the instance.

---

## 🚦 Scaling Policies

* **Target Tracking Scaling:** Adjusts capacity to maintain a metric at a target value (e.g., keep average CPU utilization at 70%).
* **Simple Scaling:** Increases/decreases instances by a fixed amount when a CloudWatch alarm triggers (e.g., if CPU > 80%, add 2 instances).
* **Step Scaling:** Adjusts capacity based on the size of the alarm breach (e.g., if CPU > 80%, add 2; if CPU > 90%, add 4).

---

## ⏳ Cooldown and Warm-up Periods

* **Cooldown Period:** A safety buffer time (default 300 seconds) after a scaling action completes. During this window, the ASG ignores other alarms to prevent rapid over-provisioning before new servers can spin up and distribute the load.
* **Instance Warm-up:** The time required for a newly launched instance to initialize and start reporting metrics.

---

## 🔗 Lifecycle Hooks

Lifecycle Hooks pause the ASG state transitions (e.g., `EC2_INSTANCE_LAUNCHING` or `EC2_INSTANCE_TERMINATING`) to execute custom scripts (e.g., installing software, backing up log directories to S3) before the instance is marked active or deleted.

```
Instance Terminating -> Lifecycle Hook (Terminating:Wait) -> Run Script -> Complete -> Instance Deleted
```

---

## 🧠 Deep-Intuition (AARF) Breakdown: ASG Scaling Policies and Lifecycle Hooks

1. **The Answer (Core Pattern):** Configure an Auto Scaling Group with Target Tracking scaling based on `ASGAverageCPUUtilization` (target 70%) combined with a termination Lifecycle Hook to upload log files to S3 before host termination.
2. **The Assumptions (Context):** The EC2 instances must have an IAM Instance Profile with S3 write permissions, and the cooldown period must be set to allow host initialization.
3. **The Rationale (Why):** Target tracking simplifies management by adjusting capacity to match real-time load. When scaling in occurs, instances are terminated. The lifecycle hook pauses the deletion process, providing time for backup agents to parse local logs and ship them to S3 before the block device is recycled.
4. **The Failure Loop (What if not):** Without a termination lifecycle hook, scaling in immediately deletes the EBS volume. If an application crash caused the scale-in event, the audit trails and logs are lost forever, preventing post-incident forensics.
5. **Alternative Case (When to use 'if not'):** For containerized workloads managed by orchestrators like Kubernetes (EKS), use Cluster Autoscaler to handle scaling at the container level, bypassing ASG lifecycle hooks.

![[../Attachments/Pasted image 20250626165425.png]]
![[../Attachments/Pasted image 20250626165815.png]]
