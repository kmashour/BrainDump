---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "aws"
  - "database"
related_concepts:
  - "[[Amazon S3]]"
  - "[[AWS Glue]]"
against:
  - "[[Amazon Athena]]"
reference_guides:
  - "[[Reference Notes/3-19_databases_analytics_ml.md]]"
tags:
  - aws/emr
  - database/big-data
  - status/completed
---

# Amazon EMR

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Infrastructure > **Amazon EMR**

---

## 🎯 Purpose (Why it is used)
Amazon EMR (Elastic MapReduce) is a managed cluster platform that simplifies running open-source big data frameworks (such as Apache Spark, Hadoop, HBase, Flink, and Hive) on AWS. It enables processing and analyzing petabyte-scale datasets for machine learning, financial modeling, bioinformatics, and data transformation.

---

## ⚙️ Functionality (What it is doing)
*   **Big Data Cluster Orchestration:** Automatically provisions and configures EC2 clusters running distributed data processing frameworks.
*   **Purchasing Optimization:** Integrates Master, Core, and Task nodes with Reserved and Spot Instances to scale processing capacity while minimizing costs.
*   **Transient Cluster Deployment:** Boots up clusters to run specific analytics jobs and terminates them immediately upon completion.
*   **Glue Integration:** Interfaces with the AWS Glue Data Catalog to query metadata schemas directly.

---

## 🏛️ Architectural Context (How it fits in the architecture)
EMR sits as the heavy compute processing layer in big data pipelines. It extracts data from S3, processes it in parallel across compute nodes, and writes the output back to S3 or a data warehouse (like Redshift).

---

## 🧩 Problem Solver (What problem it solves)
Setting up, configuring, and tuning open-source distributed frameworks (like Spark or Hadoop clusters) on bare metal or raw VMs requires significant administration and systems engineering expertise. EMR solves this by providing automated provisioning, scaling, and integration out of the box.

---

## 🟢 Operational Impact (What will happen with it operating)
Operational data processing scales dynamically, and Spot Instances on Task nodes reduce processing costs by up to 90%. Analytics teams can launch transient clusters to run periodic batch processing without maintaining continuous compute resources.

---

## 🔴 Failure Impact (What will happen without it)
Without EMR, companies must manually spin up, configure, network, and maintain clusters of VMs running Hadoop or Spark, which involves complex capacity planning and high operational overhead.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Amazon EMR**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
