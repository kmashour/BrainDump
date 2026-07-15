---
obsidianUIMode: preview
class: project-note
tier: project
domains:
  - "aws"
  - "storage"
  - "networking"
  - "linux"
difficulty: advanced
status: in-progress
---

# Project: End-to-End Clustered Observability Stack

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Projects > [[Projects/PwC Interview Preparation/Plan - DevOps Interview Roadmap|DevOps Interview Roadmap]] > **E2E Observability Stack**

---

## 🎯 Project Overview
This project provides a complete, production-grade implementation of a containerized Python Flask application deployed on AWS via Terraform, built and scanned in GitHub Actions, and monitored continuously using Prometheus and Grafana.

---

## 🏛️ Target Architecture

```
                                  [ GitHub Actions CI/CD Pipeline ]
                                                │
                               (Check out, Trivy scan, Docker build)
                                                ▼
[ AWS Custom VPC ] ──> [ Public Subnet ] ─────────────────────────> [ Private Subnet ]
  ├── Internet Gateway   └── NAT Gateway                             └── EC2 Instance
  └── Route Tables                                                       ├── Flask Application (Port 5000)
                                                                         ├── Prometheus Server (Port 9090)
                                                                         └── Grafana Telemetry (Port 3000)
```

---

## 🛠️ Step-by-Step Implementation & Configuration

### Part 1: Instrumented Flask Application

This Flask application uses the `prometheus_client` library to expose HTTP request metrics (latency histogram and total count).

```python
# app/main.py
import time
from flask import Flask, request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Define Prometheus metrics
REQUEST_COUNT = Counter(
    'http_requests_total', 
    'Total HTTP Requests', 
    ['method', 'endpoint', 'http_status']
)
REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds', 
    'HTTP request latency in seconds', 
    ['method', 'endpoint']
)

@app.route('/')
def home():
    start_time = time.time()
    # Simulate work
    time.sleep(0.05)
    
    # Track request latency & count
    latency = time.time() - start_time
    REQUEST_LATENCY.labels(method='GET', endpoint='/').observe(latency)
    REQUEST_COUNT.labels(method='GET', endpoint='/', http_status=200).inc()
    
    return "ETIC DevOps Observability App is Running!"

@app.route('/metrics')
def metrics():
    # Expose Prometheus-compatible metrics endpoint
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Part 2: Secure Multi-Stage Dockerfile

This Dockerfile compiles dependencies in a build stage, uses a minimal runtime base, and runs under a non-root user account.

```dockerfile
# Dockerfile
# Stage 1: Build Environment
FROM python:3.11-alpine AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Minimal Runtime Environment
FROM python:3.11-alpine

WORKDIR /app

# Copy python packages from builder stage
COPY --from=builder /root/.local /root/.local
COPY app/main.py .

# Update path to include user-installed python modules
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

# Create non-root system user and assign directories
RUN addgroup -S appgroup && adduser -S appuser -G appgroup && \
    chown -R appuser:appgroup /app

USER appuser

EXPOSE 5000

CMD ["python", "main.py"]
```

*Requirements file:*
```text
# requirements.txt
Flask==3.0.3
prometheus-client==0.20.0
```

---

### Part 3: Infrastructure as Code (Terraform)

#### 1. Network Topology (VPC, Subnets, Routing)

```hcl
# main.tf
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  backend "s3" {
    bucket         = "karim-devops-tfstate"
    key            = "observability-stack/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}

provider "aws" {
  region = "us-east-1"
}

# 1. Custom VPC
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  tags = {
    Name = "devops-interview-vpc"
  }
}

# 2. Subnets
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true
  tags = { Name = "public-subnet-a" }
}

resource "aws_subnet" "private" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "us-east-1a"
  tags = { Name = "private-subnet-a" }
}

# 3. Gateways
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id
  tags   = { Name = "main-igw" }
}

resource "aws_eip" "nat" {
  domain = "vpc"
}

resource "aws_nat_gateway" "nat" {
  allocation_id = aws_eip.nat.id
  subnet_id     = aws_subnet.public.id
  tags          = { Name = "main-nat-gateway" }
}

# 4. Route Tables
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }
  tags = { Name = "public-route-table" }
}

resource "aws_route_table" "private" {
  vpc_id = aws_vpc.main.id
  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat.id
  }
  tags = { Name = "private-route-table" }
}

resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "private" {
  subnet_id      = aws_subnet.private.id
  route_table_id = aws_route_table.private.id
}
```

#### 2. Security Groups & ECR Repository

```hcl
# security.tf

# Security Group for Host EC2 Instance
resource "aws_security_group" "host" {
  name        = "observability-sg"
  description = "Allow inbound application and telemetry traffic"
  vpc_id      = aws_vpc.main.id

  # SSH
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Scope in production to your IP
  }

  # Flask App
  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/16"] # Restricted to VPC
  }

  # Prometheus
  ingress {
    from_port   = 9090
    to_port     = 9090
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/16"]
  }

  # Grafana Dashboard (Publicly Accessible)
  ingress {
    from_port   = 3000
    to_port     = 3000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Outbound All
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# ECR Image Registry
resource "aws_ecr_repository" "app" {
  name                 = "etic-observability-app"
  image_tag_mutability = "MUTABLE"
  image_scanning_configuration {
    scan_on_push = true
  }
}
```

#### 3. IAM Profiles & EC2 Instance Sizing

```hcl
# instances.tf

# IAM Role for EC2 Instance to Pull from ECR
resource "aws_iam_role" "ec2_role" {
  name = "ec2-ecr-read-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      }
    ]
  })
}

# Attach AWS Managed Policy for ECR Read-Only access
resource "aws_iam_role_policy_attachment" "ecr_read" {
  role       = aws_iam_role.ec2_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
}

# Instance Profile
resource "aws_iam_instance_profile" "ec2_profile" {
  name = "ec2-instance-profile"
  role = aws_iam_role.ec2_role.name
}

# EC2 Instance Sizing & Deployment
resource "aws_instance" "server" {
  ami                  = "ami-04b70fa74e45c3917" # Ubuntu Server 24.04 LTS
  instance_type        = "t3.medium"            # Meets memory requirements for Prometheus/Grafana
  subnet_id            = aws_subnet.public.id   # Set in public subnet for direct access in lab
  security_groups      = [aws_security_group.host.id]
  iam_instance_profile = aws_iam_instance_profile.ec2_profile.name
  key_name             = "karim-ssh-key"

  user_data = <<-EOF
              #!/bin/bash
              apt-get update -y
              apt-get install -y docker.io docker-compose
              systemctl enable --now docker
              EOF

  tags = {
    Name = "observability-server"
  }
}
```

---

### Part 4: DevSecOps GitHub Actions Pipeline

This pipeline checks out the repository, configures credentials, builds the Docker image, runs a security vulnerability scan (Trivy), and pushes to ECR on successful verification.

```yaml
# .github/workflows/deploy.yml
name: Build, Scan & Push Observability Stack

on:
  push:
    branches:
      - main

permissions:
  id-token: write # Required for assuming AWS IAM Roles via OIDC
  contents: read

jobs:
  ci-cd-pipeline:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1

      - name: Log in to Amazon ECR
        id: login-ecr
        uses: aws-actions/amazon-ecr-login@v2

      - name: Build Docker Image
        run: |
          docker build -t ${{ steps.login-ecr.outputs.registry }}/etic-observability-app:latest .

      - name: Run Trivy Vulnerability Scan
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: ${{ steps.login-ecr.outputs.registry }}/etic-observability-app:latest
          format: 'table'
          exit-code: '1' # Force build failure if vulnerabilities are found
          ignore-unfixed: true
          vuln-type: 'os,library'
          severity: 'HIGH,CRITICAL'

      - name: Push Image to Amazon ECR
        run: |
          docker push ${{ steps.login-ecr.outputs.registry }}/etic-observability-app:latest
```

---

### Part 5: Docker Compose Observability Stack (EC2 Deployment Target)

Once deployed on the EC2 host, run this configuration to spawn the application and telemetry stacks.

```yaml
# docker-compose.yml
version: '3.8'

services:
  flask-app:
    image: <aws-account-id>.dkr.ecr.us-east-1.amazonaws.com/etic-observability-app:latest
    ports:
      - "5000:5000"
    restart: always

  prometheus:
    image: prom/prometheus:v2.52.0
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - prometheus-data:/prometheus
    ports:
      - "9090:9090"
    restart: always

  grafana:
    image: grafana/grafana:11.0.0
    volumes:
      - ./grafana/datasources:/etc/grafana/provisioning/datasources:ro
      - ./grafana/dashboards:/etc/grafana/provisioning/dashboards:ro
      - grafana-data:/var/lib/grafana
    ports:
      - "3000:3000"
    depends_on:
      - prometheus
    restart: always

volumes:
  prometheus-data:
  grafana-data:
```

#### 1. Prometheus Configuration

Configure the scraping engine to harvest metrics from the Flask container.

```yaml
# prometheus.yml
global:
  scrape_interval: 15s # Default scrape frequency

scrape_configs:
  - job_name: 'flask-application'
    static_configs:
      - targets: ['flask-app:5000']
```

#### 2. Grafana Provisioning Config

Pre-configure the Prometheus data source.

```yaml
# grafana/datasources/prometheus.yml
apiVersion: 1

datasources:
  - name: Prometheus
    type: prometheus
    access: proxy
    url: http://prometheus:9090
    isDefault: true
```

---

## 🔍 Verification & Diagnostics (Interview Talking Points)

During the PwC interview, walk through these commands to show how you troubleshoot application, routing, and metric scraper issues:

### 1. Verify ECR Credentials & Docker Engine Run
```bash
# Log in to ECR from EC2 using Instance Profile credentials
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <aws-account-id>.dkr.ecr.us-east-1.amazonaws.com

# Deploy the stack
docker-compose up -d

# Verify all containers are healthy
docker-compose ps
```

### 2. Verify Metric Exposition
```bash
# Query the local Flask metrics output
curl http://localhost:5000/metrics
```
*Expected Output:*
```plaintext
# HELP http_requests_total Total HTTP Requests
# TYPE http_requests_total counter
http_requests_total{endpoint="/",http_status="200",method="GET"} 12.0
# HELP http_request_duration_seconds HTTP request latency in seconds
# TYPE http_request_duration_seconds histogram
http_request_duration_seconds_bucket{le="0.005",method="GET"} 0.0
http_request_duration_seconds_bucket{le="0.1",method="GET"} 12.0
http_request_duration_seconds_sum{method="GET"} 0.601
http_request_duration_seconds_count{method="GET"} 12.0
```

### 3. Basic PromQL Metrics Troubleshooting
*   **Verify Scraper Health:** Query `up{job="flask-application"}` inside Prometheus. If it returns `1`, the target is healthy. If `0`, check routing/Docker network resolution.
*   **Calculate Request Rate:**
    `sum(rate(http_requests_total[5m])) by (endpoint)`
*   **Calculate Latency Quantiles (95th Percentile):**
    `histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))`
