#!/usr/bin/env bash

# ==============================================================================
# Kubernetes Storage Mechanics & CSI Pattern Verification Script
# ==============================================================================
#
# Description:
#   This script automates the deployment, testing, and auditing of core
#   Kubernetes storage patterns (emptyDir, hostPath/local, WaitForFirstConsumer,
#   and PVC Protection finalizers) on a local cluster (e.g., kind, minikube).
#
# Prerequisites:
#   - A running local cluster.
#   - kubectl configured to talk to your cluster.
#
# How to Run:
#   1. Make script executable:
#      - chmod +x "Reference Notes/scripts/verify_storage_poc.sh"
#   2. Execute:
#      - ./"Reference Notes/scripts/verify_storage_poc.sh"
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

# Define clean-up handler
cleanup() {
  if [ "$KEEP_RESOURCES" = true ]; then
    log_warn "Keeping resources on cluster as requested."
    return
  fi
  log_info "Cleaning up resources..."
  kubectl delete pod shared-emptydir-pod -n "$NAMESPACE" --ignore-not-found=true --grace-period=0 --force=true &>/dev/null
  kubectl delete pod storage-consumer-pod -n "$NAMESPACE" --ignore-not-found=true --grace-period=0 --force=true &>/dev/null
  kubectl delete pvc delayed-pvc-poc -n "$NAMESPACE" --ignore-not-found=true &>/dev/null
  kubectl delete pv delayed-pv-poc --ignore-not-found=true &>/dev/null
  kubectl delete storageclass delayed-sc-poc --ignore-not-found=true &>/dev/null
  log_ok "Clean-up completed."
}

# Ensure clean state on run
cleanup

# ==============================================================================
# Scenario 1: Shared emptyDir Volume
# ==============================================================================
log_info "======================================================================"
log_info "Scenario 1: Shared emptyDir Volume Mount"
log_info "======================================================================"

# Apply Pod manifest with two containers sharing an emptyDir volume
log_info "Deploying shared-emptydir-pod..."
cat <<EOF | kubectl apply -n "$NAMESPACE" -f -
apiVersion: v1
kind: Pod
metadata:
  name: shared-emptydir-pod
spec:
  containers:
  - name: writer-container
    image: alpine
    command: ["sh", "-c", "echo 'Random_Shared_Secret' > /shared-data/secret.txt && sleep 3600"]
    volumeMounts:
    - name: shared-vol
      mountPath: /shared-data
  - name: reader-container
    image: alpine
    command: ["sh", "-c", "sleep 5 && tail -f /shared-data/secret.txt"]
    volumeMounts:
    - name: shared-vol
      mountPath: /shared-data
  volumes:
  - name: shared-vol
    emptyDir: {}
EOF

log_info "Waiting for shared-emptydir-pod to run..."
kubectl wait --for=condition=Ready pod/shared-emptydir-pod -n "$NAMESPACE" --timeout=30s

# Verify writer successfully shared file with reader
log_info "Checking reader logs for shared secret..."
READER_LOGS=$(kubectl logs shared-emptydir-pod -c reader-container -n "$NAMESPACE" --tail=1)
if [[ "$READER_LOGS" == "Random_Shared_Secret" ]]; then
  log_ok "emptyDir Shared Volume verification passed! Value read: '$READER_LOGS'."
else
  log_fail "emptyDir Shared Volume verification failed! Expected 'Random_Shared_Secret', got '$READER_LOGS'."
  cleanup
  exit 1
fi

# ==============================================================================
# Scenario 2: WaitForFirstConsumer and hostPath PV/PVC
# ==============================================================================
log_info "======================================================================"
log_info "Scenario 2: WaitForFirstConsumer Binding Mechanics"
log_info "======================================================================"

# 1. Create StorageClass
log_info "Creating StorageClass with volumeBindingMode=WaitForFirstConsumer..."
cat <<EOF | kubectl apply -f -
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: delayed-sc-poc
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: WaitForFirstConsumer
EOF

# 2. Create PV
log_info "Creating hostPath PV referencing the delayed StorageClass..."
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: PersistentVolume
metadata:
  name: delayed-pv-poc
spec:
  capacity:
    storage: 100Mi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: delayed-sc-poc
  hostPath:
    path: /tmp/verify-storage-poc-data
    type: DirectoryOrCreate
EOF

# 3. Create PVC
log_info "Submitting PVC..."
cat <<EOF | kubectl apply -n "$NAMESPACE" -f -
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: delayed-pvc-poc
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: delayed-sc-poc
  resources:
    requests:
      storage: 50Mi
EOF

# 4. Verify PVC remains Pending
log_info "Verifying PVC status remains 'Pending' initially..."
sleep 3
PVC_STATUS=$(kubectl get pvc delayed-pvc-poc -n "$NAMESPACE" -o jsonpath='{.status.phase}')
if [[ "$PVC_STATUS" == "Pending" ]]; then
  log_ok "PVC is in 'Pending' state as expected (waiting for consumer)."
else
  log_fail "PVC was not Pending! Status was: '$PVC_STATUS'."
  cleanup
  exit 1
fi

# 5. Start Pod using PVC to trigger binding
log_info "Deploying consumer Pod to trigger binding..."
cat <<EOF | kubectl apply -n "$NAMESPACE" -f -
apiVersion: v1
kind: Pod
metadata:
  name: storage-consumer-pod
spec:
  containers:
  - name: app-writer
    image: alpine
    command: ["sh", "-c", "echo 'Host_Persistence_Data' > /mnt/storage/check.txt && sleep 3600"]
    volumeMounts:
    - name: data-volume
      mountPath: /mnt/storage
  volumes:
  - name: data-volume
    persistentVolumeClaim:
      claimName: delayed-pvc-poc
EOF

log_info "Waiting for storage-consumer-pod to schedule and run..."
kubectl wait --for=condition=Ready pod/storage-consumer-pod -n "$NAMESPACE" --timeout=45s

# 6. Verify PVC is now Bound
log_info "Verifying PVC has transitioned to 'Bound'..."
PVC_STATUS=$(kubectl get pvc delayed-pvc-poc -n "$NAMESPACE" -o jsonpath='{.status.phase}')
if [[ "$PVC_STATUS" == "Bound" ]]; then
  log_ok "PVC transitioned to 'Bound' successfully!"
else
  log_fail "PVC is not Bound! Status was: '$PVC_STATUS'."
  cleanup
  exit 1
fi

# ==============================================================================
# Scenario 3: PVC Protection Finalizers
# ==============================================================================
log_info "======================================================================"
log_info "Scenario 3: PVC Protection Finalizer Auditing"
log_info "======================================================================"

# Try to delete the PVC while the Pod is running (uses --wait=false to not block script)
log_info "Attempting to delete PVC while Pod is actively using it..."
kubectl delete pvc delayed-pvc-poc -n "$NAMESPACE" --wait=false

log_info "Checking PVC status and finalizers..."
sleep 2
PVC_DELETION_TIMESTAMP=$(kubectl get pvc delayed-pvc-poc -n "$NAMESPACE" -o jsonpath='{.metadata.deletionTimestamp}')
PVC_FINALIZERS=$(kubectl get pvc delayed-pvc-poc -n "$NAMESPACE" -o jsonpath='{.metadata.finalizers}')

if [[ -n "$PVC_DELETION_TIMESTAMP" && "$PVC_FINALIZERS" == *"kubernetes.io/pvc-protection"* ]]; then
  log_ok "PVC Deletion Protection active! PVC marked with deletionTimestamp but blocked by finalizer: '$PVC_FINALIZERS'."
else
  log_fail "PVC Deletion Protection failed! deletionTimestamp: '$PVC_DELETION_TIMESTAMP', finalizers: '$PVC_FINALIZERS'."
  cleanup
  exit 1
fi

# Delete the Pod to release finalizer block
log_info "Deleting consumer Pod to release the volume..."
kubectl delete pod storage-consumer-pod -n "$NAMESPACE" --grace-period=0 --force=true

log_info "Verifying PVC is now fully deleted..."
sleep 3
PVC_CHECK=$(kubectl get pvc delayed-pvc-poc -n "$NAMESPACE" 2>&1)
if [[ "$PVC_CHECK" == *"NotFound"* ]]; then
  log_ok "PVC was successfully and fully removed after Pod was deleted."
else
  log_fail "PVC still exists in the cluster! Output: '$PVC_CHECK'."
  cleanup
  exit 1
fi

log_info "======================================================================"
log_ok "ALL STORAGE MECHANICAL VALIDATIONS PASSED SUCCESSFULLY!"
log_info "======================================================================"

cleanup
exit 0
