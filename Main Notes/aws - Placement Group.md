---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[aws - EC2 and Elastic Load Balancing]]"
sub_type: architecture
source_type: udemy
course_title: "AWS Certified Solutions Architect Associate"
tags:
  - aws/compute
  - aws/architecture
---

# aws - Placement Group

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - EC2 and Elastic Load Balancing]] > **Placement Group**

---

## 📑 EC2 Placement Group Topologies

An **EC2 Placement Group** is a logical configuration container that allows customers to influence how EC2 instances are placed on physical hypervisor racks to meet specific application latency or resilience requirements.

### 🏛️ Placement Strategies

```mermaid
flowchart TD
    subgraph Cluster ["Cluster (Single AZ)"]
        direction LR
        c1["Instance A"] <-->|"Low Latency <br> 10Gbps+ Network"| c2["Instance B"]
    end
    
    subgraph Spread ["Spread (Max 7 per AZ)"]
        direction TB
        subgraph Rack_A ["Rack 1"]
            s1["Instance A"]
        end
        subgraph Rack_B ["Rack 2"]
            s2["Instance B"]
        end
    end
    
    subgraph Partition ["Partition (Up to 7 Partitions per AZ)"]
        direction TB
        subgraph Part1 ["Partition 1 (Rack X)"]
            p1_1["Instance A"]
            p1_2["Instance B"]
        end
        subgraph Part2 ["Partition 2 (Rack Y)"]
            p2_1["Instance C"]
            p2_2["Instance D"]
        end
    end
```

#### 1. Cluster Placement Group
*   **Topology:** Packs instances closely together within a single Availability Zone (AZ).
*   **Benefits:** Enables low network latency and high throughput (10 Gbps+ using enhanced networking) for inter-instance communication.
*   **Risks:** High risk of concurrent failure if the underlying AZ encounters a physical hardware or power fault.
*   **Use Cases:** High-Performance Computing (HPC), high-speed big data analytics, low-latency node networks.

#### 2. Spread Placement Group
*   **Topology:** Distributes instances so that each is placed on a completely separate physical rack (separate power and network feeds).
*   **Constraints:** Strictly limited to a maximum of **7 instances per AZ** per placement group.
*   **Benefits:** Maximizes isolation between instances to prevent concurrent failure from a single rack fault.
*   **Use Cases:** Small fleets of critical workloads (e.g., control plane nodes, main database instances, security proxies).

#### 3. Partition Placement Group
*   **Topology:** Divides instance placement across logical partitions (up to 7 partitions per AZ). Each partition maps to an isolated set of physical hardware racks.
*   **Scale:** Can support hundreds of EC2 instances per group (unlike Spread).
*   **Benefits:** Ensures instances in Partition A do not share hardware with instances in Partition B. If Partition B fails, Partition A remains active.
*   **Use Cases:** Partition-aware distributed data stores (e.g., Apache Kafka, Cassandra, Hadoop HDFS, HBase).

*Read more in [[Reference Notes/3-4_aws_ec2_compute.md#5. EC2 Placement Groups]]*
