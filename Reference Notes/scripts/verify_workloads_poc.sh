#!/usr/bin/env bash

# ==============================================================================
# Kubernetes Workload & Controller Pattern Verification Script
# ==============================================================================
#
# Description:
#   This script automates the deployment, testing, and auditing of core
#   Kubernetes workload patterns on a local cluster (e.g., kind, minikube).
#
# Validation Scenarios:
#   1. Shared Unix Socket emptyDir: Multi-container Pod communicating over UDS.
#   2. Localhost Port Sharing: Containers sharing local network loopback.
#   3. gRPC Probe Validation: Native gRPC probe using the agnhost test image.
#   4. StatefulSet Headless DNS Audit: Netshoot container auditing A/SRV records.
#
# Prerequisites:
#   - A running local cluster (e.g., kind, minikube).
#   - kubectl configured to talk to your cluster.
#   - Internet connection to pull required images (python:3.11-alpine,
#     nginx:alpine, curlimages/curl, registry.k8s.io/e2e-test-images/agnhost, nicolaka/netshoot).
#
# How to Run:
#   1. Start local cluster:
#      - kind:     kind create cluster
#      - minikube: minikube start
#   2. Verify access:
#      - kubectl cluster-info
#   3. Make script executable:
#      - chmod +x Reference\ Notes/scripts/verify_workloads_poc.sh
#   4. Execute:
#      - ./Reference\ Notes/scripts/verify_workloads_poc.sh
#
# Options:
#   -n, --namespace <ns>  Target namespace (default: default)
#   -k, --keep            Do not clean up resources at the end of the run
#   -h, --help            Show this help message
#
# ==============================================================================

# Exit immediately if a command fails during setup
set -o pipefail

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Helper output functions
log_info() { echo -e "${BLUE}[INFO] $(date +'%Y-%m-%dT%H:%M:%S') - $1${NC}"; }
log_ok() { echo -e "${GREEN}[OK] $(date +'%Y-%m-%dT%H:%M:%S') - $1${NC}"; }
log_warn() { echo -e "${YELLOW}[WARN] $(date +'%Y-%m-%dT%H:%M:%S') - $1${NC}"; }
log_fail() { echo -e "${RED}[FAIL] $(date +'%Y-%m-%dT%H:%M:%S') - $1${NC}"; }

# Default values
NAMESPACE="default"
KEEP_RESOURCES=false

# Parse arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    -n|--namespace)
      NAMESPACE="$2"
      shift 2
      ;;
    -k|--keep)
      KEEP_RESOURCES=true
      shift
      ;;
    -h|--help)
      echo "Usage: $0 [options]"
      echo "Options:"
      echo "  -n, --namespace <ns>  Target namespace (default: default)"
      echo "  -k, --keep            Do not clean up Kubernetes resources at the end"
      echo "  -h, --help            Show this help message"
      exit 0
      ;;
    *)
      log_fail "Unknown argument: $1"
      exit 1
      ;;
  esac
done

# Pre-flight Checks
log_info "Starting pre-flight checks..."
if ! command -v kubectl &> /dev/null; then
  log_fail "kubectl CLI is not installed. Exiting."
  exit 1
fi

if ! kubectl cluster-info &> /dev/null; then
  log_fail "Cannot connect to Kubernetes cluster. Please start kind/minikube."
  exit 1
fi
log_ok "Connected to cluster successfully."

# Ensure namespace exists
log_info "Configuring target namespace: '$NAMESPACE'..."
kubectl create namespace "$NAMESPACE" --dry-run=client -o yaml | kubectl apply -f - > /dev/null
log_ok "Namespace '$NAMESPACE' is ready."

# Initialize results
VAL1_STATUS="FAIL"
VAL2_STATUS="FAIL"
VAL3_STATUS="FAIL"
VAL4_STATUS="FAIL"

# ==============================================================================
# Validation 1: Shared Unix Socket emptyDir
# ==============================================================================
log_info "=================================================="
log_info "Validation 1: Shared Unix Socket emptyDir"
log_info "=================================================="

log_info "Deploying multi-container Pod (shared-unix-socket-poc)..."
cat <<EOF | kubectl apply -n "$NAMESPACE" -f -
apiVersion: v1
kind: Pod
metadata:
  name: shared-unix-socket-poc
  labels:
    poc: shared-unix-socket
spec:
  restartPolicy: Never
  volumes:
  - name: shared-socket-dir
    emptyDir: {}
  containers:
  - name: socket-server
    image: python:3.11-alpine
    env:
    - name: PYTHONUNBUFFERED
      value: "1"
    command:
    - python
    - -u
    - -c
    - |
      import socket, os, sys, time
      socket_path = "/tmp/shared/pod.sock"
      if os.path.exists(socket_path):
          os.remove(socket_path)
      server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
      server.bind(socket_path)
      server.listen(1)
      print("SOCKET_SERVER: Listening for connections on Unix socket...")
      sys.stdout.flush()
      conn, addr = server.accept()
      try:
          data = conn.recv(1024)
          print(f"SOCKET_SERVER: Received message: '{data.decode()}'")
          conn.sendall(b"Hello from socket-server!")
          print("SOCKET_SERVER: Response sent, closing connection.")
      finally:
          conn.close()
    volumeMounts:
    - name: shared-socket-dir
      mountPath: /tmp/shared
  - name: socket-client
    image: python:3.11-alpine
    env:
    - name: PYTHONUNBUFFERED
      value: "1"
    command:
    - python
    - -u
    - -c
    - |
      import socket, time, sys
      socket_path = "/tmp/shared/pod.sock"
      print("SOCKET_CLIENT: Waiting for socket-server to start...")
      time.sleep(3)
      client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
      try:
          client.connect(socket_path)
          print("SOCKET_CLIENT: Connected successfully to Unix socket!")
          client.sendall(b"Hello from socket-client sidecar!")
          response = client.recv(1024)
          print(f"SOCKET_CLIENT: Received response: '{response.decode()}'")
      except Exception as e:
          print(f"SOCKET_CLIENT: Connection failed: {e}")
          sys.exit(1)
    volumeMounts:
    - name: shared-socket-dir
      mountPath: /tmp/shared
EOF

log_info "Waiting for Pod shared-unix-socket-poc to complete..."
timeout=60
elapsed=0
pod_success=false
while true; do
  PHASE=$(kubectl get pod shared-unix-socket-poc -n "$NAMESPACE" -o jsonpath='{.status.phase}' 2>/dev/null)
  if [ "$PHASE" == "Succeeded" ]; then
    log_ok "Pod shared-unix-socket-poc completed with Succeeded phase."
    pod_success=true
    break
  elif [ "$PHASE" == "Failed" ]; then
    log_fail "Pod shared-unix-socket-poc failed."
    break
  elif [ $elapsed -gt $timeout ]; then
    log_fail "Timeout waiting for Pod shared-unix-socket-poc to complete."
    break
  fi
  sleep 2
  elapsed=$((elapsed+2))
done

if [ "$pod_success" = true ]; then
  SERVER_LOGS=$(kubectl logs shared-unix-socket-poc -c socket-server -n "$NAMESPACE" 2>/dev/null)
  CLIENT_LOGS=$(kubectl logs shared-unix-socket-poc -c socket-client -n "$NAMESPACE" 2>/dev/null)

  log_info "Server logs:"
  echo "$SERVER_LOGS"
  log_info "Client logs:"
  echo "$CLIENT_LOGS"

  if echo "$CLIENT_LOGS" | grep -q "Received response: 'Hello from socket-server!'" && \
     echo "$SERVER_LOGS" | grep -q "Received message: 'Hello from socket-client sidecar!'"; then
    log_ok "Unix Domain Socket communication validated successfully!"
    VAL1_STATUS="PASS"
  else
    log_fail "Logs do not verify successful Unix domain socket handshake."
  fi
else
  log_fail "Validation 1 Failed: Pod did not complete successfully."
fi


# ==============================================================================
# Validation 2: Localhost Port Sharing
# ==============================================================================
log_info "=================================================="
log_info "Validation 2: Localhost Port Sharing"
log_info "=================================================="

log_info "Deploying web/client sidecar Pod (localhost-port-sharing-poc)..."
cat <<EOF | kubectl apply -n "$NAMESPACE" -f -
apiVersion: v1
kind: Pod
metadata:
  name: localhost-port-sharing-poc
  labels:
    poc: localhost-port-sharing
spec:
  restartPolicy: Never
  containers:
  - name: web-server
    image: nginx:alpine
    ports:
    - containerPort: 80
  - name: curl-client
    image: curlimages/curl:8.2.1
    command:
    - sh
    - -c
    - |
      echo "CURL_CLIENT: Waiting for Nginx to boot..."
      for i in \$(seq 1 30); do
        if curl -s http://localhost:80 > /dev/null; then
          echo "CURL_CLIENT: Localhost webserver is reachable."
          break
        fi
        sleep 1
      done
      echo "CURL_CLIENT: Executing request to localhost..."
      curl -s http://localhost:80 | grep -o "Welcome to nginx!"
      if [ \$? -eq 0 ]; then
        echo "CURL_CLIENT: Connection succeeded and verified content."
        exit 0
      else
        echo "CURL_CLIENT: Content verification failed."
        exit 1
      fi
EOF

log_info "Waiting for curl-client container in Pod localhost-port-sharing-poc to complete..."
timeout=60
elapsed=0
client_success=false
while true; do
  STATE=$(kubectl get pod localhost-port-sharing-poc -n "$NAMESPACE" -o jsonpath='{.status.containerStatuses[?(@.name=="curl-client")].state}' 2>/dev/null)
  if echo "$STATE" | grep -q "terminated"; then
    EXIT_CODE=$(kubectl get pod localhost-port-sharing-poc -n "$NAMESPACE" -o jsonpath='{.status.containerStatuses[?(@.name=="curl-client")].state.terminated.exitCode}' 2>/dev/null)
    if [ "$EXIT_CODE" == "0" ]; then
      log_ok "curl-client sidecar container completed successfully with exit code 0."
      client_success=true
      break
    else
      log_fail "curl-client sidecar container failed with exit code $EXIT_CODE."
      break
    fi
  elif [ $elapsed -gt $timeout ]; then
    log_fail "Timeout waiting for curl-client container to complete."
    break
  fi
  sleep 2
  elapsed=$((elapsed+2))
done

if [ "$client_success" = true ]; then
  CLIENT_LOGS=$(kubectl logs localhost-port-sharing-poc -c curl-client -n "$NAMESPACE" 2>/dev/null)
  log_info "Client logs:"
  echo "$CLIENT_LOGS"

  if echo "$CLIENT_LOGS" | grep -q "CURL_CLIENT: Connection succeeded and verified content."; then
    log_ok "Localhost port sharing validated successfully!"
    VAL2_STATUS="PASS"
  else
    log_fail "Logs do not verify successful localhost networking handshake."
  fi
else
  log_fail "Validation 2 Failed: Sidecar container exited with error or timed out."
fi


# ==============================================================================
# Validation 3: gRPC Probe Validation
# ==============================================================================
log_info "=================================================="
log_info "Validation 3: gRPC Probe Validation"
log_info "=================================================="

log_info "Deploying gRPC server Pod (grpc-probe-poc)..."
cat <<EOF | kubectl apply -n "$NAMESPACE" -f -
apiVersion: v1
kind: Pod
metadata:
  name: grpc-probe-poc
  labels:
    poc: grpc-probe
spec:
  restartPolicy: Never
  containers:
  - name: agnhost-grpc
    image: registry.k8s.io/e2e-test-images/agnhost:2.45
    command:
    - /agnhost
    - grpc-health-checking
    - --port
    - "5000"
    - --http-port
    - "8080"
    ports:
    - containerPort: 5000
    - containerPort: 8080
    readinessProbe:
      grpc:
        port: 5000
      initialDelaySeconds: 2
      periodSeconds: 2
EOF

log_info "Waiting for Pod grpc-probe-poc to become Ready..."
timeout=60
elapsed=0
grpc_ready=false
while true; do
  READY=$(kubectl get pod grpc-probe-poc -n "$NAMESPACE" -o jsonpath='{.status.containerStatuses[?(@.name=="agnhost-grpc")].ready}' 2>/dev/null)
  if [ "$READY" == "true" ]; then
    log_ok "Pod grpc-probe-poc marked Ready by Kubelet."
    grpc_ready=true
    break
  elif [ $elapsed -gt $timeout ]; then
    log_fail "Timeout waiting for Pod grpc-probe-poc to become Ready."
    break
  fi
  sleep 2
  elapsed=$((elapsed+2))
done

if [ "$grpc_ready" = true ]; then
  # Grab the describe/status events to print out probe success context
  EVENTS=$(kubectl get events -n "$NAMESPACE" --field-selector involvedObject.name=grpc-probe-poc -o custom-columns=LASTSEEN:.lastTimestamp,REASON:.reason,MESSAGE:.message | tail -n 5)
  log_info "Recent Events for Pod grpc-probe-poc:"
  echo "$EVENTS"
  log_ok "Native gRPC readiness probe validated successfully!"
  VAL3_STATUS="PASS"
else
  log_fail "Validation 3 Failed: Pod never transitioned to Ready state."
fi


# ==============================================================================
# Validation 4: StatefulSet Headless DNS Audit
# ==============================================================================
log_info "=================================================="
log_info "Validation 4: StatefulSet Headless DNS Audit"
log_info "=================================================="

log_info "Deploying Headless Service and StatefulSet (statefulset-dns-audit)..."
cat <<EOF | kubectl apply -n "$NAMESPACE" -f -
apiVersion: v1
kind: Service
metadata:
  name: headless-dns-audit-svc
spec:
  clusterIP: None
  ports:
  - name: http
    port: 80
    targetPort: 80
  selector:
    app: statefulset-dns-audit
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: statefulset-dns-audit
spec:
  serviceName: headless-dns-audit-svc
  replicas: 2
  selector:
    matchLabels:
      app: statefulset-dns-audit
  template:
    metadata:
      labels:
        app: statefulset-dns-audit
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
        ports:
        - name: http
          containerPort: 80
EOF

log_info "Waiting for StatefulSet pods to roll out..."
if ! kubectl rollout status statefulset/statefulset-dns-audit -n "$NAMESPACE" --timeout=90s; then
  log_fail "StatefulSet rollout failed or timed out."
fi

log_info "Deploying temporary netshoot container for DNS queries..."
cat <<EOF | kubectl apply -n "$NAMESPACE" -f -
apiVersion: v1
kind: Pod
metadata:
  name: dns-audit-client
  labels:
    poc: dns-audit-client
spec:
  restartPolicy: Never
  containers:
  - name: netshoot
    image: nicolaka/netshoot:latest
    command: ["sleep", "3600"]
EOF

log_info "Waiting for dns-audit-client to run..."
if ! kubectl wait --for=condition=Ready pod/dns-audit-client -n "$NAMESPACE" --timeout=60s &>/dev/null; then
  log_fail "dns-audit-client Pod failed to become Ready."
fi

# Retrieve real Pod IPs
POD0_IP=$(kubectl get pod statefulset-dns-audit-0 -n "$NAMESPACE" -o jsonpath='{.status.podIP}' 2>/dev/null)
POD1_IP=$(kubectl get pod statefulset-dns-audit-1 -n "$NAMESPACE" -o jsonpath='{.status.podIP}' 2>/dev/null)

log_info "Expected Pod IPs: statefulset-dns-audit-0 = $POD0_IP, statefulset-dns-audit-1 = $POD1_IP"

# Determine cluster domain dynamically
CLUSTER_DOMAIN=$(kubectl exec dns-audit-client -n "$NAMESPACE" -c netshoot -- sh -c "grep search /etc/resolv.conf | awk '{print \$2}'" 2>/dev/null | sed -E 's/^[^.]+\.svc\.//' | head -n 1)
if [ -z "$CLUSTER_DOMAIN" ]; then
  CLUSTER_DOMAIN="cluster.local"
fi
log_info "Detected cluster DNS domain: $CLUSTER_DOMAIN"

# 1. Query A records for headless domain
A_QUERY="headless-dns-audit-svc.$NAMESPACE.svc.$CLUSTER_DOMAIN"
log_info "Auditing A records for Headless Domain: $A_QUERY"
A_RECORDS=$(kubectl exec dns-audit-client -n "$NAMESPACE" -c netshoot -- dig +short "$A_QUERY" 2>/dev/null)
log_info "A Records resolved:\n$A_RECORDS"

# 2. Query SRV records
SRV_QUERY="_http._tcp.headless-dns-audit-svc.$NAMESPACE.svc.$CLUSTER_DOMAIN"
log_info "Auditing SRV records for Headless Domain: $SRV_QUERY"
SRV_RECORDS=$(kubectl exec dns-audit-client -n "$NAMESPACE" -c netshoot -- dig +short SRV "$SRV_QUERY" 2>/dev/null)
log_info "SRV Records resolved:\n$SRV_RECORDS"

# 3. Query individual pod ordinals
POD0_QUERY="statefulset-dns-audit-0.headless-dns-audit-svc.$NAMESPACE.svc.$CLUSTER_DOMAIN"
POD1_QUERY="statefulset-dns-audit-1.headless-dns-audit-svc.$NAMESPACE.svc.$CLUSTER_DOMAIN"
log_info "Auditing ordinal pod A records..."
POD0_RESOLVED_IP=$(kubectl exec dns-audit-client -n "$NAMESPACE" -c netshoot -- dig +short "$POD0_QUERY" 2>/dev/null | tail -n 1)
POD1_RESOLVED_IP=$(kubectl exec dns-audit-client -n "$NAMESPACE" -c netshoot -- dig +short "$POD1_QUERY" 2>/dev/null | tail -n 1)

log_info "Ordinal 0 ($POD0_QUERY) resolves to: $POD0_RESOLVED_IP"
log_info "Ordinal 1 ($POD1_QUERY) resolves to: $POD1_RESOLVED_IP"

# Assertions
VAL4_STATUS="PASS"

if ! echo "$A_RECORDS" | grep -q "$POD0_IP"; then
  log_fail "Headless A-records do not contain statefulset-dns-audit-0 IP ($POD0_IP)"
  VAL4_STATUS="FAIL"
fi

if ! echo "$A_RECORDS" | grep -q "$POD1_IP"; then
  log_fail "Headless A-records do not contain statefulset-dns-audit-1 IP ($POD1_IP)"
  VAL4_STATUS="FAIL"
fi

if ! echo "$SRV_RECORDS" | grep -q "statefulset-dns-audit-0.headless-dns-audit-svc.$NAMESPACE.svc.$CLUSTER_DOMAIN"; then
  log_fail "Headless SRV-records do not map to statefulset-dns-audit-0 ordinal domain"
  VAL4_STATUS="FAIL"
fi

if ! echo "$SRV_RECORDS" | grep -q "statefulset-dns-audit-1.headless-dns-audit-svc.$NAMESPACE.svc.$CLUSTER_DOMAIN"; then
  log_fail "Headless SRV-records do not map to statefulset-dns-audit-1 ordinal domain"
  VAL4_STATUS="FAIL"
fi

if [ "$POD0_RESOLVED_IP" != "$POD0_IP" ]; then
  log_fail "Ordinal 0 DNS resolution mismatch. Expected $POD0_IP, got '$POD0_RESOLVED_IP'"
  VAL4_STATUS="FAIL"
fi

if [ "$POD1_RESOLVED_IP" != "$POD1_IP" ]; then
  log_fail "Ordinal 1 DNS resolution mismatch. Expected $POD1_IP, got '$POD1_RESOLVED_IP'"
  VAL4_STATUS="FAIL"
fi

if [ "$VAL4_STATUS" == "PASS" ]; then
  log_ok "StatefulSet Headless DNS architecture validated successfully!"
fi


# ==============================================================================
# Cleanup & Summary
# ==============================================================================
log_info "=================================================="
log_info "Audit Execution Summary"
log_info "=================================================="

if [ "$KEEP_RESOURCES" = true ]; then
  log_warn "Keeping resources in namespace '$NAMESPACE' as requested by --keep / -k."
else
  log_info "Cleaning up deployed Kubernetes resources..."
  kubectl delete pod shared-unix-socket-poc localhost-port-sharing-poc grpc-probe-poc dns-audit-client -n "$NAMESPACE" --ignore-not-found --grace-period=0 --force &>/dev/null
  kubectl delete statefulset statefulset-dns-audit -n "$NAMESPACE" --ignore-not-found --grace-period=0 --force &>/dev/null
  kubectl delete service headless-dns-audit-svc -n "$NAMESPACE" --ignore-not-found --grace-period=0 --force &>/dev/null
  log_ok "Cleaned up all resources."
fi

# Print tabular summary
echo -e "\n=================================================="
echo -e "          AUDIT & VERIFICATION RESULTS            "
echo -e "=================================================="
if [ "$VAL1_STATUS" == "PASS" ]; then
  echo -e "1. Shared Unix Socket emptyDir:   ${GREEN}PASSED${NC}"
else
  echo -e "1. Shared Unix Socket emptyDir:   ${RED}FAILED${NC}"
fi

if [ "$VAL2_STATUS" == "PASS" ]; then
  echo -e "2. Localhost Port Sharing:        ${GREEN}PASSED${NC}"
else
  echo -e "2. Localhost Port Sharing:        ${RED}FAILED${NC}"
fi

if [ "$VAL3_STATUS" == "PASS" ]; then
  echo -e "3. gRPC Probe Validation:         ${GREEN}PASSED${NC}"
else
  echo -e "3. gRPC Probe Validation:         ${RED}FAILED${NC}"
fi

if [ "$VAL4_STATUS" == "PASS" ]; then
  echo -e "4. StatefulSet Headless DNS Audit:${GREEN}PASSED${NC}"
else
  echo -e "4. StatefulSet Headless DNS Audit:${RED}FAILED${NC}"
fi
echo -e "=================================================="

# Exit codes
if [ "$VAL1_STATUS" != "PASS" ] || [ "$VAL2_STATUS" != "PASS" ] || [ "$VAL3_STATUS" != "PASS" ] || [ "$VAL4_STATUS" != "PASS" ]; then
  log_fail "One or more validations FAILED."
  exit 1
else
  log_ok "All validations PASSED successfully."
  exit 0
fi
