#!/usr/bin/env bash

# ==============================================================================
# Kubernetes Scheduling, Logging & Application Lifecycle Pattern Verification Script
# ==============================================================================
#
# Description:
#   This script automates the deployment, testing, and auditing of Kubernetes
#   scheduling policies (node selectors, node affinity, taints, tolerations),
#   and application lifecycle configuration sync (ConfigMaps, Secrets as volumes
#   and environment variables) on a local cluster (e.g., kind, minikube).
#
# Prerequisites:
#   - A running local cluster.
#   - kubectl configured to talk to your cluster.
#
# How to Run:
#   1. Make script executable:
#      - chmod +x "Reference Notes/scripts/verify_scheduling_lifecycle_poc.sh"
#   2. Execute:
#      - ./"Reference Notes/scripts/verify_scheduling_lifecycle_poc.sh"
#
# Options:
#   -n, --namespace <ns>  Target namespace (default: default)
#   -k, --keep            Do not clean up resources at the end of the run
#   -h, --help            Show this help message
#
# ==============================================================================

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
  log_fail "Cannot connect to Kubernetes cluster. Please ensure your cluster is running."
  exit 1
fi
log_ok "Connected to cluster successfully."

# Detect a target node (exclude control-plane/master if possible, fallback to first node)
log_info "Detecting cluster nodes..."
TARGET_NODE=$(kubectl get nodes -o jsonpath='{.items[*].metadata.name}' | tr ' ' '\n' | grep -v 'control-plane' | grep -v 'master' | head -n 1)
if [ -z "$TARGET_NODE" ]; then
  TARGET_NODE=$(kubectl get nodes -o jsonpath='{.items[0].metadata.name}')
fi

if [ -z "$TARGET_NODE" ]; then
  log_fail "No nodes found in the cluster. Exiting."
  exit 1
fi
log_ok "Target node selected: $TARGET_NODE"

# Helper function to get existing taints of target node and format as tolerations
get_existing_tolerations() {
  local node="$1"
  local indent="$2"
  local taints
  taints=$(kubectl get node "$node" -o jsonpath='{range .spec.taints[*]}{.key}:{.effect}{"\n"}{end}' 2>/dev/null)
  if [ -n "$taints" ]; then
    while IFS= read -r taint; do
      if [ -n "$taint" ]; then
        local key=$(echo "$taint" | cut -d: -f1)
        local effect=$(echo "$taint" | cut -d: -f2)
        echo "${indent}- key: \"$key\""
        echo "${indent}  operator: \"Exists\""
        if [ -n "$effect" ]; then
          echo "${indent}  effect: \"$effect\""
        fi
      fi
    done <<< "$taints"
  fi
}

# Define clean-up handler
cleanup() {
  if [ "$KEEP_RESOURCES" = true ]; then
    log_warn "Keeping resources on cluster as requested."
    return
  fi
  log_info "Cleaning up resources..."

  # Delete pods
  for pod in pod-nodeselector-test pod-nodeaffinity-test pod-notoleration-test pod-toleration-test pod-sync-test; do
    kubectl delete pod "$pod" -n "$NAMESPACE" --ignore-not-found=true --grace-period=0 --force=true &>/dev/null
  done

  # Delete configmap and secret
  kubectl delete configmap sync-config -n "$NAMESPACE" --ignore-not-found=true &>/dev/null
  kubectl delete secret sync-secret -n "$NAMESPACE" --ignore-not-found=true &>/dev/null

  # Remove node label and taint from TARGET_NODE (if TARGET_NODE is set)
  if [ -n "$TARGET_NODE" ]; then
    log_info "Removing label and taint from node $TARGET_NODE..."
    kubectl label node "$TARGET_NODE" zone- --ignore-not-found=true &>/dev/null
    kubectl taint node "$TARGET_NODE" tier- --ignore-not-found=true &>/dev/null
  fi

  log_ok "Clean-up completed."
}

# Setup exit trap to ensure cleanup on error or exit (unless KEEP_RESOURCES is true)
trap_cleanup() {
  local exit_code=$?
  if [ $exit_code -ne 0 ] && [ "$KEEP_RESOURCES" = false ]; then
    log_fail "Script exited with error code $exit_code. Cleaning up..."
    cleanup
  elif [ "$KEEP_RESOURCES" = false ]; then
    cleanup
  fi
}
trap trap_cleanup EXIT

# Ensure clean state on run
cleanup

# Ensure target namespace exists
if ! kubectl get namespace "$NAMESPACE" &>/dev/null; then
  log_info "Namespace '$NAMESPACE' does not exist. Creating it..."
  kubectl create namespace "$NAMESPACE"
fi

# Fetch existing tolerations to attach to test pods
EXISTING_TOLERATIONS=$(get_existing_tolerations "$TARGET_NODE" "  ")

# ==============================================================================
# Scenario 1: Node Label and NodeSelector/Affinity Validation
# ==============================================================================
log_info "======================================================================"
log_info "Scenario 1: Node Label and NodeSelector/Affinity Validation"
log_info "======================================================================"

# Apply custom label to TARGET_NODE
log_info "Applying label 'zone=frontend-secure' to node '$TARGET_NODE'..."
kubectl label node "$TARGET_NODE" zone=frontend-secure --overwrite
log_ok "Label applied successfully."

# Deploy Pod with nodeSelector
log_info "Deploying pod-nodeselector-test targeting label 'zone=frontend-secure'..."
cat <<EOF | kubectl apply -n "$NAMESPACE" -f -
apiVersion: v1
kind: Pod
metadata:
  name: pod-nodeselector-test
spec:
  nodeSelector:
    zone: frontend-secure
  containers:
  - name: test-container
    image: alpine
    command: ["sh", "-c", "sleep 3600"]
$(if [ -n "$EXISTING_TOLERATIONS" ]; then
    echo "  tolerations:"
    echo "$EXISTING_TOLERATIONS"
  fi)
EOF

log_info "Waiting for pod-nodeselector-test to schedule and run..."
if ! kubectl wait --for=condition=Ready pod/pod-nodeselector-test -n "$NAMESPACE" --timeout=60s; then
  log_fail "pod-nodeselector-test failed to become Ready."
  exit 1
fi

# Verify it gets scheduled on the correct node
SCHEDULED_NODE=$(kubectl get pod pod-nodeselector-test -n "$NAMESPACE" -o jsonpath='{.spec.nodeName}')
if [[ "$SCHEDULED_NODE" == "$TARGET_NODE" ]]; then
  log_ok "pod-nodeselector-test scheduled on the correct node: $SCHEDULED_NODE"
else
  log_fail "pod-nodeselector-test scheduled on '$SCHEDULED_NODE' instead of target node '$TARGET_NODE'"
  exit 1
fi

# Deploy Pod with Node Affinity
log_info "Deploying pod-nodeaffinity-test utilizing Node Affinity..."
cat <<EOF | kubectl apply -n "$NAMESPACE" -f -
apiVersion: v1
kind: Pod
metadata:
  name: pod-nodeaffinity-test
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: zone
            operator: In
            values:
            - frontend-secure
  containers:
  - name: test-container
    image: alpine
    command: ["sh", "-c", "sleep 3600"]
$(if [ -n "$EXISTING_TOLERATIONS" ]; then
    echo "  tolerations:"
    echo "$EXISTING_TOLERATIONS"
  fi)
EOF

log_info "Waiting for pod-nodeaffinity-test to schedule and run..."
if ! kubectl wait --for=condition=Ready pod/pod-nodeaffinity-test -n "$NAMESPACE" --timeout=60s; then
  log_fail "pod-nodeaffinity-test failed to become Ready."
  exit 1
fi

# Verify scheduling success
SCHEDULED_NODE_AFFINITY=$(kubectl get pod pod-nodeaffinity-test -n "$NAMESPACE" -o jsonpath='{.spec.nodeName}')
if [[ "$SCHEDULED_NODE_AFFINITY" == "$TARGET_NODE" ]]; then
  log_ok "pod-nodeaffinity-test scheduled on the correct node: $SCHEDULED_NODE_AFFINITY"
else
  log_fail "pod-nodeaffinity-test scheduled on '$SCHEDULED_NODE_AFFINITY' instead of target node '$TARGET_NODE'"
  exit 1
fi

# ==============================================================================
# Scenario 2: Taints and Tolerations Validation
# ==============================================================================
log_info "======================================================================"
log_info "Scenario 2: Taints and Tolerations Validation"
log_info "======================================================================"

# Apply taint to TARGET_NODE
log_info "Applying taint 'tier=backend:NoSchedule' to node '$TARGET_NODE'..."
kubectl taint node "$TARGET_NODE" tier=backend:NoSchedule --overwrite
log_ok "Taint applied successfully."

# Deploy Pod without matching toleration
log_info "Deploying pod-notoleration-test (nodeSelector applied but without tolerating the new taint)..."
cat <<EOF | kubectl apply -n "$NAMESPACE" -f -
apiVersion: v1
kind: Pod
metadata:
  name: pod-notoleration-test
spec:
  nodeSelector:
    zone: frontend-secure
  containers:
  - name: test-container
    image: alpine
    command: ["sh", "-c", "sleep 3600"]
$(if [ -n "$EXISTING_TOLERATIONS" ]; then
    echo "  tolerations:"
    echo "$EXISTING_TOLERATIONS"
  fi)
EOF

log_info "Waiting for pod-notoleration-test scheduling decision (sleeping 5s)..."
sleep 5

# Verify it remains Pending
POD_STATUS=$(kubectl get pod pod-notoleration-test -n "$NAMESPACE" -o jsonpath='{.status.phase}')
if [[ "$POD_STATUS" == "Pending" ]]; then
  log_ok "pod-notoleration-test remains in Pending state as expected."
  # Print event message for diagnostic clarity
  SCHED_EVENT=$(kubectl get events -n "$NAMESPACE" --field-selector involvedObject.name=pod-notoleration-test --sort-by='.metadata.creationTimestamp' -o jsonpath='{.items[-1:].message}' 2>/dev/null)
  if [ -n "$SCHED_EVENT" ]; then
    log_info "Scheduling decision event: '$SCHED_EVENT'"
  fi
else
  log_fail "pod-notoleration-test is not in Pending state! Phase is: $POD_STATUS"
  exit 1
fi

# Deploy Pod with matching toleration
log_info "Deploying pod-toleration-test (with matching toleration for 'tier=backend:NoSchedule')..."
cat <<EOF | kubectl apply -n "$NAMESPACE" -f -
apiVersion: v1
kind: Pod
metadata:
  name: pod-toleration-test
spec:
  nodeSelector:
    zone: frontend-secure
  tolerations:
  - key: "tier"
    operator: "Equal"
    value: "backend"
    effect: "NoSchedule"
$(if [ -n "$EXISTING_TOLERATIONS" ]; then
    echo "$EXISTING_TOLERATIONS"
  fi)
  containers:
  - name: test-container
    image: alpine
    command: ["sh", "-c", "sleep 3600"]
EOF

log_info "Waiting for pod-toleration-test to schedule and run..."
if ! kubectl wait --for=condition=Ready pod/pod-toleration-test -n "$NAMESPACE" --timeout=60s; then
  log_fail "pod-toleration-test failed to become Ready."
  exit 1
fi

# Verify scheduling success
SCHEDULED_NODE_TOLERATION=$(kubectl get pod pod-toleration-test -n "$NAMESPACE" -o jsonpath='{.spec.nodeName}')
if [[ "$SCHEDULED_NODE_TOLERATION" == "$TARGET_NODE" ]]; then
  log_ok "pod-toleration-test scheduled on tainted node successfully: $SCHEDULED_NODE_TOLERATION"
else
  log_fail "pod-toleration-test scheduled on '$SCHEDULED_NODE_TOLERATION' instead of target node '$TARGET_NODE'"
  exit 1
fi

# Remove the taint
log_info "Removing taint 'tier=backend:NoSchedule' from node '$TARGET_NODE'..."
kubectl taint node "$TARGET_NODE" tier- --ignore-not-found=true &>/dev/null
log_ok "Taint removed successfully."

# ==============================================================================
# Scenario 3: ConfigMap and Secret Volume Mount Sync Validation
# ==============================================================================
log_info "======================================================================"
log_info "Scenario 3: ConfigMap and Secret Volume Mount Sync Validation"
log_info "======================================================================"

# Create ConfigMap
log_info "Creating ConfigMap 'sync-config'..."
kubectl create configmap sync-config -n "$NAMESPACE" \
  --from-literal=config-key="config-value-from-volume" \
  --from-literal=env-config-key="config-value-from-env" \
  --dry-run=client -o yaml | kubectl apply -f -

# Create Secret
log_info "Creating Secret 'sync-secret'..."
kubectl create secret generic sync-secret -n "$NAMESPACE" \
  --from-literal=secret-key="secret-value-from-volume" \
  --from-literal=env-secret-key="secret-value-from-env" \
  --dry-run=client -o yaml | kubectl apply -f -

# Deploy test Pod mounting both as volumes and as environment variables
log_info "Deploying pod-sync-test..."
cat <<EOF | kubectl apply -n "$NAMESPACE" -f -
apiVersion: v1
kind: Pod
metadata:
  name: pod-sync-test
spec:
  nodeSelector:
    zone: frontend-secure
  containers:
  - name: test-container
    image: alpine
    command: ["sh", "-c", "sleep 3600"]
    env:
    - name: ENV_CONFIG_VAL
      valueFrom:
        configMapKeyRef:
          name: sync-config
          key: env-config-key
    - name: ENV_SECRET_VAL
      valueFrom:
        secretKeyRef:
          name: sync-secret
          key: env-secret-key
    volumeMounts:
    - name: config-volume
      mountPath: /etc/config
    - name: secret-volume
      mountPath: /etc/secret
  volumes:
  - name: config-volume
    configMap:
      name: sync-config
  - name: secret-volume
    secret:
      secretName: sync-secret
$(if [ -n "$EXISTING_TOLERATIONS" ]; then
    echo "  tolerations:"
    echo "$EXISTING_TOLERATIONS"
  fi)
EOF

log_info "Waiting for pod-sync-test to schedule and become Ready..."
if ! kubectl wait --for=condition=Ready pod/pod-sync-test -n "$NAMESPACE" --timeout=60s; then
  log_fail "pod-sync-test failed to become Ready."
  exit 1
fi

# Verify volume mount content
log_info "Verifying mounted ConfigMap file content..."
CONFIG_VAL_FILE=$(kubectl exec pod-sync-test -n "$NAMESPACE" -c test-container -- cat /etc/config/config-key 2>/dev/null)
if [[ "$CONFIG_VAL_FILE" == "config-value-from-volume" ]]; then
  log_ok "ConfigMap volume file content matches: '$CONFIG_VAL_FILE'"
else
  log_fail "ConfigMap volume file content mismatch! Expected 'config-value-from-volume', got '$CONFIG_VAL_FILE'"
  exit 1
fi

log_info "Verifying mounted Secret file content..."
SECRET_VAL_FILE=$(kubectl exec pod-sync-test -n "$NAMESPACE" -c test-container -- cat /etc/secret/secret-key 2>/dev/null)
if [[ "$SECRET_VAL_FILE" == "secret-value-from-volume" ]]; then
  log_ok "Secret volume file content matches: '$SECRET_VAL_FILE'"
else
  log_fail "Secret volume file content mismatch! Expected 'secret-value-from-volume', got '$SECRET_VAL_FILE'"
  exit 1
fi

# Verify environment variables
log_info "Verifying ConfigMap environment variable..."
CONFIG_VAL_ENV=$(kubectl exec pod-sync-test -n "$NAMESPACE" -c test-container -- sh -c 'echo "$ENV_CONFIG_VAL"' 2>/dev/null)
if [[ "$CONFIG_VAL_ENV" == "config-value-from-env" ]]; then
  log_ok "ConfigMap env var injection matches: '$CONFIG_VAL_ENV'"
else
  log_fail "ConfigMap env var injection mismatch! Expected 'config-value-from-env', got '$CONFIG_VAL_ENV'"
  exit 1
fi

log_info "Verifying Secret environment variable..."
SECRET_VAL_ENV=$(kubectl exec pod-sync-test -n "$NAMESPACE" -c test-container -- sh -c 'echo "$ENV_SECRET_VAL"' 2>/dev/null)
if [[ "$SECRET_VAL_ENV" == "secret-value-from-env" ]]; then
  log_ok "Secret env var injection matches: '$SECRET_VAL_ENV'"
else
  log_fail "Secret env var injection mismatch! Expected 'secret-value-from-env', got '$SECRET_VAL_ENV'"
  exit 1
fi

# ==============================================================================
# Scenario 4: Logging & Monitoring Diagnostics
# ==============================================================================
log_info "======================================================================"
log_info "Scenario 4: Logging & Monitoring Diagnostics"
log_info "======================================================================"

# Fetch logs from active verification pods
log_info "Fetching logs from active verification pods..."
for pod in pod-nodeselector-test pod-nodeaffinity-test pod-toleration-test pod-sync-test; do
  log_info "--- Logs for pod $pod ---"
  POD_LOGS=$(kubectl logs "$pod" -n "$NAMESPACE" --tail=5 2>/dev/null)
  if [ -n "$POD_LOGS" ]; then
    echo "$POD_LOGS"
  else
    log_info "(No logs generated by alpine sleep container)"
  fi
done

# Check if metrics-server is available
log_info "Checking metrics-server availability..."
if kubectl top nodes &>/dev/null; then
  log_ok "metrics-server is available."
  log_info "Node CPU/Memory usage:"
  kubectl top nodes
  log_info "Pod CPU/Memory usage in namespace '$NAMESPACE':"
  kubectl top pods -n "$NAMESPACE"
else
  log_warn "metrics-server is not available (kubectl top failed). Skipping metrics diagnostic."
fi

# ==============================================================================
# Scenario 5: Success & Cleanup
# ==============================================================================
log_info "======================================================================"
log_ok "ALL SCHEDULING & LIFECYCLE POC VALIDATIONS COMPLETED SUCCESSFULLY!"
log_info "======================================================================"

exit 0
