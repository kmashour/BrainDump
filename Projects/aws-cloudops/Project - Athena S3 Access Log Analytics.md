---
obsidianUIMode: preview
class: project-note
tier: project
domains:
  - aws
concepts_referenced:
  - "[[Amazon S3]]"
  - "[[Amazon Athena]]"
difficulty: intermediate
status: completed
---

# Project: Athena S3 Access Log Analytics

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Projects > **Athena S3 Access Log Analytics**

---

## 🎯 Project Overview

This project implements a serverless log intelligence pipeline using **Amazon S3** and **Amazon Athena** to query, inspect, and audit S3 access logs. S3 Server Access Logs contain detailed records of requests made to buckets, which are critical for security audits, access troubleshooting, and usage billing analysis. Rather than downloading and parsing these logs manually, this project demonstrates how to set up an Athena external table using Regex serialization/deserialization (RegexSerDe) to map raw access log streams to structured SQL tables, enabling real-time analytics.

### Learning Objectives:
*   Configure Server Access Logging on a target Amazon S3 bucket to output logs to a dedicated logging bucket.
*   Configure Amazon Athena workspace parameters, including setting up an output location in S3 for query results.
*   Write and execute DDL (Data Definition Language) SQL statements using Apache Hive's `RegexSerDe` parser to define external tables mapping to S3 log files.
*   Perform analytics queries to count requests by HTTP status code, identify not-found (404) errors, and flag unauthorized access attempts (403 Access Denied) to audit bucket security.

---

## 🏛️ Target Architecture

The logging and query pipeline operates completely serverless, mapping host access events to SQL-queryable datasets:

```mermaid
flowchart TD
    subgraph ClientZone ["Client Traffic"]
        Client["Users & Applications"]
    end

    subgraph S3Service ["Amazon S3 Storage Infrastructure"]
        TargetBucket["Target S3 Bucket (e.g., source-data-bucket)"]
        LogBucket["Log Destination Bucket (e.g., access-logs-destination)"]
        ResultBucket["Athena Results Bucket (e.g., athena-query-results)"]
    end

    subgraph AnalyticsService ["Serverless Query Engine"]
        Athena["Amazon Athena Engine"]
        GlueCatalog["AWS Glue Data Catalog"]
    end

    Client -->|Access Requests| TargetBucket
    TargetBucket -->|S3 Server Access Logs (Near Real-Time)| LogBucket
    Athena -->|Leverages Schema Metadata| GlueCatalog
    Athena -->|Read and Parse Access Logs| LogBucket
    Athena -->|Write Query Outputs| ResultBucket
```

---

## 🛠️ Step-by-Step Implementation & Configuration

### 1. S3 Bucket Configuration
First, prepare three buckets (or two if using a single logging bucket with prefixes):
*   `source-data-bucket`: The bucket containing user data that will be audited.
*   `access-logs-destination`: The bucket that will receive access logs from the source bucket.
*   `athena-query-results`: The bucket used by Amazon Athena to store query outputs and metadata.

#### Enabling Access Logging via AWS CLI:
To enable logging on `source-data-bucket` pointing to `access-logs-destination` with the prefix `source-bucket-logs/`:
```bash
aws s3api put-bucket-logging \
  --bucket source-data-bucket \
  --bucket-logging-status '{
    "LoggingEnabled": {
      "TargetBucket": "access-logs-destination",
      "TargetPrefix": "source-bucket-logs/"
    }
  }'
```

---

### 2. Setting Up the Athena Query Environment
Before running SQL queries, configure the query result location in Athena settings to point to the query results bucket:
`s3://athena-query-results/`

---

### 3. Athena DDL: Creating the Access Logs External Table
Execute the following DDL statement in the Athena Query Editor to create the external table. This defines the schema for S3 access logs and configures the Apache Hive `RegexSerDe` regular expression to parse the log lines.

```sql
CREATE DATABASE IF NOT EXISTS s3_access_logs_db;

CREATE EXTERNAL TABLE IF NOT EXISTS s3_access_logs_db.mybucket_logs(
  BucketOwner STRING,
  Bucket STRING,
  RequestDateTime STRING,
  RemoteIP STRING,
  Requester STRING,
  RequestID STRING,
  Operation STRING,
  Key STRING,
  RequestURI_operation STRING,
  HTTPStatus INT,
  Error_code STRING,
  BytesSent BIGINT,
  ObjectSize BIGINT,
  TotalTime INT,
  TurnAroundTime INT,
  Referrer STRING,
  UserAgent STRING,
  VersionId STRING,
  HostId STRING,
  SignatureVersion STRING,
  CipherSuite STRING,
  AuthenticationType STRING,
  RequesterChargedSTRING STRING,
  MinimumTLSVersion STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = '1',
  'input.regex' = '([^ ]*) ([^ ]*) \\[(.*?)\\] ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) \\\"([^\\\"]*)\\\" ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) \\\"([^\\\"]*)\\\" \\\"([^\\\"]*)\\\" ([^ ]*)(?: ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*))?'
)
LOCATION 's3://access-logs-destination/source-bucket-logs/';
```
> [!IMPORTANT]
> The `LOCATION` parameter must point to the destination S3 path containing the log files, and it **must end with a trailing slash** (`/`). Athena reads all objects in the specified directory recursively.

---

## 🔍 Verification & Diagnostics

Once logs are delivered (S3 server access logs are delivered on a best-effort basis, typically arriving within a few hours), run the following queries to verify and analyze data:

### 1. Preview the Logs (Sanity Check)
Confirm that the schema correctly aligns with the logs by querying the first 10 rows:
```sql
SELECT 
  Bucket, 
  RequestDateTime, 
  RemoteIP, 
  Requester, 
  Operation, 
  Key, 
  HTTPStatus 
FROM s3_access_logs_db.mybucket_logs 
LIMIT 10;
```

### 2. Count Requests by HTTP Status and Operation
Run an aggregation query to summarize total HTTP status codes by Request URI operation to see successful requests, client errors, and backend issues:
```sql
SELECT 
  HTTPStatus, 
  RequestURI_operation, 
  COUNT(*) AS RequestCount
FROM s3_access_logs_db.mybucket_logs
GROUP BY HTTPStatus, RequestURI_operation
ORDER BY RequestCount DESC;
```

### 3. Detect and Audit Security Denials (403 Access Denied)
Audit access denial events to identify configuration mistakes or potential brute-force/unauthorized scans:
```sql
SELECT 
  RequestDateTime, 
  RemoteIP, 
  Requester, 
  Operation, 
  Key, 
  HTTPStatus, 
  Error_code
FROM s3_access_logs_db.mybucket_logs
WHERE HTTPStatus = 403
ORDER BY RequestDateTime DESC;
```

### 4. Locate Missing Resources (404 Not Found)
Identify dead links or application misconfigurations returning missing object errors:
```sql
SELECT 
  Key, 
  RequestURI_operation, 
  Referrer, 
  COUNT(*) AS NotFoundCount
FROM s3_access_logs_db.mybucket_logs
WHERE HTTPStatus = 404
GROUP BY Key, RequestURI_operation, Referrer
ORDER BY NotFoundCount DESC;
```

---

## 💡 Key Architectural Takeaways

- **Design Trade-off (Eventual Consistency & Processing Delay):** S3 server access logging is decoupled from the direct request path to avoid impacts on storage performance. Logs are delivered asynchronously (often taking 1–4 hours). For real-time, low-latency log auditing, engineers must use **CloudTrail Data Events** routed to CloudWatch Logs, though it costs significantly more.
- **Cost Optimization:** Athena charges based on the volume of data scanned (typically $5 per TB). To minimize query costs and optimize performance:
  1. **Partitioning:** Implement partition projections (e.g., partitioning by year, month, day) in the table DDL to query only specific date ranges.
  2. **Columnar Data Formats:** Use ETL tools like AWS Glue to convert raw text logs (CSV/TSV) into columnar formats (Parquet/ORC). This allows Athena to query only specific columns, reducing data scanned by up to 99%.
- **Regex SerDe Resilience:** The `RegexSerDe` deserializer uses Java-style regular expressions. If a log line fails to match the regular expression, the row is returned as all `NULL` values. Care must be taken to match custom headers and newer fields (like TLS version fields appended in modern S3 access log schemas).
