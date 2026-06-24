---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[aws - EBS and EFS Storage]]"
sub_type: core-concept
source_type: udemy
course_title: "AWS Certified Solutions Architect Associate"
tags:
  - aws/snow-family
  - aws/storage
  - aws/deep-dive
---

# aws - AWS Snow Family

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - EBS and EFS Storage]] > **AWS Snow Family**

---

## 📑 AWS Snow Family Foundations

The **AWS Snow Family** is a collection of physical, highly secure, and ruggedized devices designed to migrate large volumes of data (up to petabytes/exabytes) in and out of AWS and run local edge computing workloads under harsh, disconnected conditions.

### ⚙️ Physical Devices & Performance Specs
*   **AWS Snowcone:** 
    *   *Form Factor:* Compact, portable (4.5 lbs), ruggedized.
    *   *Storage:* 8 TB usable storage.
    *   *Integration:* Comes with a pre-installed **AWS DataSync agent** to seamlessly migrate data over the network once configured.
*   **AWS Snowball Edge Storage Optimized:**
    *   *Use Cases:* High-capacity data migration and storage-intensive local processing.
    *   *Storage:* **210 TB** (as of newer models, or 80 TB standard).
    *   *Compute:* Provides storage-focused edge computing.
*   **AWS Snowball Edge Compute Optimized:**
    *   *Use Cases:* Low-latency edge computing and local machine learning inference in remote environments (e.g., ships, trucks, military/mining outposts) with limited/no internet access.
    *   *Storage:* **28 TB** usable capacity.
    *   *Compute:* Built-in massive vCPU and GPU capability to run **Amazon EC2 instances** or **AWS Lambda functions** directly on the device.
*   **AWS Snowmobile:** A 45-foot container pulled by a semi-truck. Designed to migrate up to **100 PB** of data for exabyte-scale migrations.

### 🔄 Architectural Pipeline: S3 Glacier Imports
*   **Limitation:** Snowball devices *cannot* import data directly into the Amazon S3 Glacier or Glacier Deep Archive storage classes.
*   **Resolution Pathway:**
    1.  Import the data from the Snowball Edge device directly into a standard **Amazon S3** bucket.
    2.  Set up an **S3 Lifecycle Policy** on the destination bucket to transition the objects into Glacier/Glacier Deep Archive automatically.

*Read more in [[Reference Notes/3-5_aws_ebs_efs_storage.md#7-aws-snow-family|Module 3-5: AWS Snow Family]]*
