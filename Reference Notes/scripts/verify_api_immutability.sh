#!/usr/bin/env bash
# verify_api_immutability.sh
# Programmatic validation of Kubernetes Pod Immutability and Force-Replace workflows.

set -euo pipefail

# ANSI color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# 1. Check Pre-requisites
log_info "Verifying cluster access..."
if ! kubectl cluster-info >/dev/null 2>&1; then
    log_error "Kubernetes cluster is not accessible. Please ensure your kubeconfig is valid."
    exit 1
fi

TEMP_DIR=$(mktemp -d -t k8s-immutability-XXXXXX)
log_info "Using temporary directory: ${TEMP_DIR}"

cleanup() {
    log_info "Cleaning up resources..."
    kubectl delete pod po-demo --ignore-not-found=true >/dev/null 2>&1
    rm -rf "${TEMP_DIR}"
    log_info "Cleanup complete."
}
trap cleanup EXIT

# 2. Generate and Create Initial Pod Manifest
log_info "Generating initial Pod manifest (nginx:1.23.0)..."
cat <<EOF > "${TEMP_DIR}/pod-initial.yaml"
apiVersion: v1
kind: Pod
metadata:
  name: po-demo
  labels:
    app: demo
spec:
  containers:
  - name: web
    image: nginx:1.23.0
    ports:
    - containerPort: 80
EOF

log_info "Creating Pod imperatively using 'kubectl create'..."
kubectl create -f "${TEMP_DIR}/pod-initial.yaml"

log_info "Waiting for Pod to be ready..."
kubectl wait --for=condition=Ready pod/po-demo --timeout=60s

# 3. Check for last-applied-configuration annotation
log_info "Checking metadata annotations..."
ANNOTATIONS=$(kubectl get pod po-demo -o jsonpath='{.metadata.annotations}')
if [[ "$ANNOTATIONS" == *"last-applied-configuration"* ]]; then
    log_warn "Annotation exists. It was unexpectedly created."
else
    log_info "Success: 'last-applied-configuration' annotation is missing as expected (created imperatively)."
fi

# 4. Save configuration with apply to inject annotation
log_info "Injecting annotation via 'kubectl apply'..."
kubectl apply -f "${TEMP_DIR}/pod-initial.yaml"
ANNOTATIONS_UPDATED=$(kubectl get pod po-demo -o jsonpath='{.metadata.annotations}')
if [[ "$ANNOTATIONS_UPDATED" == *"last-applied-configuration"* ]]; then
    log_info "Success: 'last-applied-configuration' annotation is now present."
else
    log_error "Annotation was not injected by kubectl apply."
    exit 1
fi

# 5. Attempt to change an immutable field (containerPort 80 -> 8080)
log_info "Attempting to declaratively change containerPort (immutable field)..."
cat <<EOF > "${TEMP_DIR}/pod-immutable-change.yaml"
apiVersion: v1
kind: Pod
metadata:
  name: po-demo
  labels:
    app: demo
spec:
  containers:
  - name: web
    image: nginx:1.23.0
    ports:
    - containerPort: 8080
EOF

log_warn "Executing kubectl apply for immutable port change..."
if kubectl apply -f "${TEMP_DIR}/pod-immutable-change.yaml" 2> "${TEMP_DIR}/error.log"; then
    log_error "Error: Kubernetes allowed the modification of an immutable field!"
    exit 1
else
    log_info "Success: API server rejected the change as expected."
    echo -e "${YELLOW}API Server Rejection Message:${NC}"
    cat "${TEMP_DIR}/error.log"
fi

# 6. Execute Forceful Replacement
log_info "Executing forceful replacement using 'kubectl replace --force'..."
kubectl replace --force -f "${TEMP_DIR}/pod-immutable-change.yaml"

log_info "Waiting for recreated Pod to be ready..."
kubectl wait --for=condition=Ready pod/po-demo --timeout=60s

# Verify new port is applied
LIVE_PORT=$(kubectl get pod po-demo -o jsonpath='{.spec.containers[0].ports[0].containerPort}')
if [ "$LIVE_PORT" -eq 8080 ]; then
    log_info "Success: Pod replaced and containerPort updated to ${LIVE_PORT}."
else
    log_error "Failed: Port was not updated after replacement."
    exit 1
fi

# 7. Modify a Mutable Field (Image: nginx:1.23.0 -> nginx:1.24.0)
log_info "Modifying container image (mutable field) from nginx:1.23.0 to nginx:1.24.0..."
cat <<EOF > "${TEMP_DIR}/pod-mutable-change.yaml"
apiVersion: v1
kind: Pod
metadata:
  name: po-demo
  labels:
    app: demo
spec:
  containers:
  - name: web
    image: nginx:1.24.0
    ports:
    - containerPort: 8080
EOF

log_info "Applying mutable update..."
kubectl apply -f "${TEMP_DIR}/pod-mutable-change.yaml"

# Wait a brief moment for the container change to take effect
sleep 2

# Verify the image has been updated
LIVE_IMAGE=$(kubectl get pod po-demo -o jsonpath='{.spec.containers[0].image}')
if [ "$LIVE_IMAGE" == "nginx:1.24.0" ]; then
    log_info "Success: Pod image updated to ${LIVE_IMAGE} in-place."
else
    log_error "Failed: Image was not updated."
    exit 1
fi

log_info "--- ALL VERIFICATIONS PASSED SUCCESSFULLY ---"
