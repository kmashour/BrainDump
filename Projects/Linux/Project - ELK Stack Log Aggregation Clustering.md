---
obsidianUIMode: preview
class: project-playbook
tier: project-playbook
tags:
  - project
  - linux/services
  - linux/elk
  - linux/observability
---

# Project: ELK Stack Log Aggregation Clustering

**Breadcrumbs:** [[8-Index - Linux and OS|🏠 Linux and OS Index]] > **Projects** > **ELK Stack Log Aggregation Clustering**

---

## 🎯 Project Objective
This playbook covers establishing a centralized log collection and analysis environment using the Elasticsearch, Logstash, and Kibana (ELK) stack on a RHEL platform. It details node installation, Logstash Grok filter mapping, and Kibana dashboard configuration.

---

## 💻 Scenario
1.  **Observability Host:** `192.168.12.10` hosting the Elasticsearch storage node, Logstash parser engine, and Kibana portal.
2.  **Log Client:** Remote client shipping syslog files over port 5044 to the central log aggregator.

---

## 🛠️ Step-by-Step Implementation

### Step 1: Install Java Prerequisites and ELK Repos
Run these commands on the observability host:
```bash
# 1. Install Java Development Kit
yum install -y java-11-openjdk-devel

# 2. Add Elastic official repository signature
rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch

# 3. Add Elasticsearch repository definition
cat <<EOF > /etc/yum.repos.d/elasticsearch.repo
[elasticsearch]
name=Elasticsearch repository for 7.x packages
baseurl=https://artifacts.elastic.co/packages/7.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
EOF
```

### Step 2: Install and Configure Elasticsearch Node
```bash
# 1. Install Elasticsearch package
yum install -y elasticsearch

# 2. Override default elasticsearch configurations
cat <<EOF > /etc/elasticsearch/elasticsearch.yml
cluster.name: corp-logging
node.name: lognode-1
path.data: /var/lib/elasticsearch
path.logs: /var/log/elasticsearch
network.host: 192.168.12.10
http.port: 9200
discovery.seed_hosts: ["192.168.12.10"]
cluster.initial_master_nodes: ["lognode-1"]
EOF

# 3. Enable and start Elasticsearch service
systemctl enable --now elasticsearch
```

### Step 3: Install and Configure Logstash Parsing Pipeline
```bash
# 1. Install Logstash package
yum install -y logstash

# 2. Write Logstash Syslog/Beats input and grok parser configuration
cat <<EOF > /etc/logstash/conf.d/syslog-pipeline.conf
input {
  beats {
    port => 5044
  }
}

filter {
  if [fields][log_type] == "syslog" {
    grok {
      match => { "message" => "%{SYSLOGTIMESTAMP:syslog_timestamp} %{SYSLOGHOST:syslog_hostname} %{DATA:syslog_program}(?:\[%{POSINT:syslog_pid}\])?: %{GREEDYDATA:syslog_message}" }
    }
    date {
      match => [ "syslog_timestamp", "MMM  d HH:mm:ss", "MMM dd HH:mm:ss" ]
    }
  }
}

output {
  elasticsearch {
    hosts => ["http://192.168.12.10:9200"]
    index => "syslog-records-%{+YYYY.MM.dd}"
  }
}
EOF

# 3. Start Logstash service
systemctl enable --now logstash
```

### Step 4: Install and Configure Kibana Interface
```bash
# 1. Install Kibana package
yum install -y kibana

# 2. Override Kibana configs
cat <<EOF > /etc/kibana/kibana.yml
server.port: 5601
server.host: "192.168.12.10"
elasticsearch.hosts: ["http://192.168.12.10:9200"]
EOF

# 3. Start Kibana service
systemctl enable --now kibana
```

### Step 5: Configure Portals Security Controls (Firewall)
```bash
# Open elasticsearch, logstash, and kibana ports in firewall
firewall-cmd --permanent --add-port=9200/tcp
firewall-cmd --permanent --add-port=5044/tcp
firewall-cmd --permanent --add-port=5601/tcp
firewall-cmd --reload
```

---

## 🔬 Verification & Diagnostics

### Test Elasticsearch Node Response
Verify that the storage backend is active and responding:
```bash
curl -X GET http://192.168.12.10:9200/
```
*Expected Output snippet:*
```json
{
  "name" : "lognode-1",
  "cluster_name" : "corp-logging",
  "cluster_uuid" : "a1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5d6",
  "version" : {
    "number" : "7.10.0"
  },
  "tagline" : "You Know, for Search"
}
```

### Test Logstash Pipeline Syntax
Verify pipeline configuration syntaxes before launching:
```bash
/usr/share/logstash/bin/logstash --config.test_and_exit -f /etc/logstash/conf.d/syslog-pipeline.conf
```
*Expected Output snippet:*
```
Configuration OK
```
---
> [!NOTE]
> Ensure the Kibana portal `http://192.168.12.10:5601` is accessible via a web browser and create an index pattern matching `syslog-records-*` to view aggregated logs.
