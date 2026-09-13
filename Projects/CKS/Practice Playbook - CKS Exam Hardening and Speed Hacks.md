# CKS Exam Practice Playbook: Security Hardening & Speed Hacks

This playbook compiles practice questions, scenario requirements, diagnostic steps, CLI solutions, and YAML manifests for the **Certified Kubernetes Security Specialist (CKS)** exam track.

---

## ⚡ Section 0: CKS Speed Setup, Aliases & Time Management

The CKS exam provides 120 minutes to solve 15 to 16 complex security scenarios across multiple clusters and nodes. Rapid terminal execution and precision editing are critical.

### 0.1 Essential Terminal & Vim Configuration
Add the following to `~/.bashrc` and `~/.vimrc` immediately at the start of your exam session:

```bash
# Terminal Aliases & Autocompletion
alias k='kubectl'
alias kgp='kubectl get pods'
alias kgs='kubectl get svc'
alias kgn='kubectl get nodes'
alias kd='kubectl describe'
export do="--dry-run=client -o yaml"
export now="--force --grace-period=0"

# Quick Context & Node Switching
alias c="clear"

# Persistent Vim configuration
cat <<EOF > ~/.vimrc
set tabstop=2
set shiftwidth=2
set expandtab
set number
set autoindent
set smartindent
set paste
syntax on
EOF
```

### 0.2 Exam Safety Protocols
1. **Always Check Context & Node:** Every question specifies a cluster context (e.g. `kubectl config use-context cluster1`). Verify with `kubectl config current-context`.
2. **Back Up Static Pod Manifests:** Before editing `/etc/kubernetes/manifests/*.yaml`, **always copy the file outside the directory**:
   ```bash
   cp /etc/kubernetes/manifests/kube-apiserver.yaml /root/kube-apiserver.yaml.bak
   ```
   > [!IMPORTANT]
   > If you save a backup *inside* `/etc/kubernetes/manifests/`, the Kubelet will attempt to launch the backup as a static pod, causing port conflicts!
3. **Monitor Static Pod Restarts:** After editing a manifest, monitor the pod restart using `crictl`:
   ```bash
   crictl ps --name kube-apiserver
   # Check logs if container fails to restart:
   crictl logs $(crictl ps -a --name kube-apiserver -q | head -n1)
   ```

---

## 🛡️ Scenario 1: CIS Benchmark Auditing with `kube-bench`

### Problem Statement
You are tasked with auditing the master control plane node and worker node `node01` using `kube-bench`. Remediate all `[FAIL]` items for the API server and Kubelet configurations.

### Step-by-Step Implementation

1. **Run kube-bench on Master Node:**
   ```bash
   kube-bench run --targets master
   ```
   *Suppose the output reports:*
   * `[FAIL] 1.1.1 Ensure that the API server pod specification file permissions are set to 600 or more restrictive`
   * `[FAIL] 1.2.1 Ensure that the --anonymous-auth argument is set to false`
   * `[FAIL] 1.2.16 Ensure that the --profiling argument is set to false`

2. **Remediate Master Node Permissions & Flags:**
   ```bash
   # Fix file permissions:
   chmod 600 /etc/kubernetes/manifests/kube-apiserver.yaml

   # Edit API server manifest:
   vim /etc/kubernetes/manifests/kube-apiserver.yaml
   ```
   Ensure the following flags are present in `spec.containers[0].command`:
   ```yaml
   - --anonymous-auth=false
   - --profiling=false
   ```

3. **Run kube-bench on Worker Node (`node01`):**
   ```bash
   ssh node01
   kube-bench run --targets node
   ```
   *Suppose the output reports:*
   * `[FAIL] 4.1.1 Ensure that the kubelet service file permissions are set to 600 or more restrictive`
   * `[FAIL] 4.2.1 Ensure that the --anonymous-auth argument is set to false`

4. **Remediate Worker Node:**
   ```bash
   # Fix permissions:
   chmod 600 /lib/systemd/system/kubelet.service

   # Edit Kubelet config file:
   vim /var/lib/kubelet/config.yaml
   ```
   Modify `authentication.anonymous.enabled`:
   ```yaml
   authentication:
     anonymous:
       enabled: false
     webhook:
       enabled: true
   authorization:
     mode: Webhook
   ```
   Restart the Kubelet:
   ```bash
   systemctl daemon-reload
   systemctl restart kubelet
   systemctl status kubelet
   exit
   ```

5. **Verification:**
   Re-run `kube-bench run --targets master` and verify that the items now report `[PASS]`.

---

## 🔒 Scenario 2: Kubelet Security & NodeRestriction

### Problem Statement
Harden the Kubelet on `node01` by disabling the unauthenticated read-only port (`10255`) and enforcing Webhook authentication and authorization. Enable the `NodeRestriction` admission controller on the API server.

### Step-by-Step Implementation

1. **Enable NodeRestriction on Control Plane:**
   ```bash
   vim /etc/kubernetes/manifests/kube-apiserver.yaml
   ```
   Add `NodeRestriction` to `--enable-admission-plugins`:
   ```yaml
   - --enable-admission-plugins=NodeRestriction
   ```

2. **Harden Kubelet on `node01`:**
   ```bash
   ssh node01
   vim /var/lib/kubelet/config.yaml
   ```
   Configure the following parameters:
   ```yaml
   readOnlyPort: 0
   authentication:
     anonymous:
       enabled: false
     webhook:
       enabled: true
   authorization:
     mode: Webhook
   ```
   Restart Kubelet:
   ```bash
   systemctl daemon-reload
   systemctl restart kubelet
   exit
   ```

3. **Verification:**
   Test connection to read-only port 10255 on `node01` from the master:
   ```bash
   curl -s -m 2 http://<NODE01_IP>:10255/pods
   # Expected: Connection refused (port is closed)
   ```

---

## 🌐 Scenario 3: Cloud Metadata Endpoint & Multi-Tenant NetworkPolicies

### Problem Statement
A web application pod named `frontend` in namespace `tenant-prod` must communicate with the database `db-service` on TCP port 5432 and perform DNS resolution via CoreDNS. To protect against SSRF, completely block access to the cloud metadata service IP (`169.254.169.254`). All other egress traffic must be denied.

### Step-by-Step Implementation

1. **Create Namespace and Labels:**
   Ensure the `kube-system` namespace has standard metadata labels for CoreDNS selection:
   ```bash
   kubectl label namespace kube-system kubernetes.io/metadata.name=kube-system --overwrite
   ```

2. **Author the NetworkPolicy (`/root/frontend-netpol.yaml`):**
   ```yaml
   apiVersion: networking.k8s.io/v1
   kind: NetworkPolicy
   metadata:
     name: frontend-egress-policy
     namespace: tenant-prod
   spec:
     podSelector:
       matchLabels:
         app: frontend
     policyTypes:
     - Egress
     egress:
     # 1. Allow DNS queries to CoreDNS in kube-system
     - to:
       - namespaceSelector:
           matchLabels:
             kubernetes.io/metadata.name: kube-system
       ports:
       - protocol: UDP
         port: 53
       - protocol: TCP
         port: 53
     # 2. Allow egress to internal database on port 5432
     - to:
       - podSelector:
           matchLabels:
             app: db-backend
       ports:
       - protocol: TCP
         port: 5432
     # 3. Allow egress to external APIs while explicitly excluding 169.254.169.254
     - to:
       - ipBlock:
           cidr: 0.0.0.0/0
           except:
           - 169.254.169.254/32
       ports:
       - protocol: TCP
         port: 443
   ```

3. **Apply & Verify:**
   ```bash
   kubectl apply -f /root/frontend-netpol.yaml
   # Verify that metadata address is blocked:
   kubectl exec -n tenant-prod frontend -- curl -s -m 2 http://169.254.169.254/latest/meta-data/
   # Expected Output: command times out / connection dropped
   ```

---

## ⚙️ Scenario 4: Host OS Hardening (Kernel Modules & Port Auditing)

### Problem Statement
Security audit flags unused legacy kernel modules `dccp` and `sctp` as high-risk vectors on `node01`. Blacklist and unload both modules. Furthermore, identify and terminate an unapproved listening process on port 8088.

### Step-by-Step Implementation

1. **Access Node & Blacklist Modules:**
   ```bash
   ssh node01
   # Unload modules currently in memory
   modprobe -r dccp sctp 2>/dev/null || true

   # Create blacklist file
   cat <<EOF > /etc/modprobe.d/blacklist-custom.conf
   blacklist dccp
   blacklist sctp
   install dccp /bin/true
   install sctp /bin/true
   EOF
   ```

2. **Identify and Kill Rogue Process:**
   ```bash
   # Find process listening on 8088:
   ss -tulpn | grep 8088
   # Or using lsof:
   lsof -i :8088

   # Identify PID (e.g. PID 48123) and terminate:
   kill -9 48123
   # If running as a systemd service, disable it:
   systemctl stop rogue-service 2>/dev/null || true
   systemctl disable rogue-service 2>/dev/null || true
   exit
   ```

---

## 🛡️ Scenario 5: AppArmor Profile Creation & Pod Enforcement

### Problem Statement
Load an AppArmor profile named `k8s-deny-write` on worker node `node01`. Deploy a pod named `secure-app` in the `default` namespace enforcing this profile so that write operations inside the container filesystem are denied.

### Step-by-Step Implementation

1. **Create and Load Profile on `node01`:**
   ```bash
   ssh node01
   cat <<'EOF' > /etc/apparmor.d/k8s-deny-write
   #include <tunables/global>

   profile k8s-deny-write flags=(attach_disconnected,mediate_deleted) {
     #include <abstractions/base>

     file,
     /** r,
     deny /** w,
   }
   EOF

   # Parse and load into the kernel:
   apparmor_parser -q /etc/apparmor.d/k8s-deny-write

   # Verify profile status:
   aa-status | grep k8s-deny-write
   exit
   ```

2. **Deploy Pod with AppArmor Profile:**

   *Kubernetes v1.30+ Native Syntax:*
   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: secure-app
     namespace: default
   spec:
     nodeName: node01 # Ensure pod schedules on the node where profile is loaded
     containers:
     - name: test-container
       image: busybox
       command: ["sh", "-c", "sleep 3600"]
       securityContext:
         appArmorProfile:
           type: Localhost
           localhostProfile: k8s-deny-write
   ```

   *(Legacy Kubernetes v1.29 syntax using annotation: `container.apparmor.security.beta.kubernetes.io/test-container: "localhost/k8s-deny-write"`)*

3. **Verify Enforcement:**
   ```bash
   kubectl apply -f pod-apparmor.yaml
   kubectl exec -it secure-app -- touch /tmp/testfile
   # Expected Output: touch: /tmp/testfile: Permission denied
   ```

---

## 🔒 Scenario 6: Seccomp Profile Deployment, Enforcement & Node Defaulting

### Problem Statement
1. On worker node `node01`, deploy a custom seccomp audit profile named `audit-syscalls.json` to the default Kubelet seccomp directory.
2. Deploy a pod named `audit-pod` scheduled on `node01` that enforces this custom local profile and verifies syscall logging in `/var/log/syslog`.
3. Create a production pod named `seccomp-pod` using the `RuntimeDefault` profile with `allowPrivilegeEscalation: false`.
4. Enable node-wide seccomp defaulting (`seccompDefault: true`) in `/var/lib/kubelet/config.yaml` on `node01` so all unconfigured pods automatically inherit `RuntimeDefault`.
5. Verify container seccomp enforcement directly at the container runtime level using `crictl`.

### Step-by-Step Implementation

1. **Deploy Custom Localhost Profile to Node:**
   ```bash
   ssh node01
   mkdir -p /var/lib/kubelet/seccomp/profiles
   cat <<'EOF' > /var/lib/kubelet/seccomp/profiles/audit-syscalls.json
   {
     "defaultAction": "SCMP_ACT_LOG"
   }
   EOF
   chmod 644 /var/lib/kubelet/seccomp/profiles/audit-syscalls.json
   exit
   ```

2. **Deploy Pod with `Localhost` Seccomp Profile:**
   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: audit-pod
     namespace: default
   spec:
     nodeName: node01
     securityContext:
       seccompProfile:
         type: Localhost
         localhostProfile: profiles/audit-syscalls.json
     containers:
     - name: test-container
       image: hashicorp/http-echo:1.0
       args: ["-text=exam-syscall-check"]
       securityContext:
         allowPrivilegeEscalation: false
   ```
   Apply and verify in syslog:
   ```bash
   kubectl apply -f audit-pod.yaml
   # Tail syslog on node01 to observe type=1326 seccomp audit records
   ssh node01 "tail -n 20 /var/log/syslog | grep 'http-echo'"
   ```

3. **Deploy Production Pod with `RuntimeDefault` Profile:**
   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: seccomp-pod
     namespace: default
   spec:
     securityContext:
       seccompProfile:
         type: RuntimeDefault
     containers:
     - name: nginx
       image: nginx:alpine
       securityContext:
         allowPrivilegeEscalation: false
   ```
   Apply manifest:
   ```bash
   kubectl apply -f seccomp-pod.yaml
   ```

4. **Enable Cluster-Wide Seccomp Defaulting on Node Kubelet:**
   ```bash
   ssh node01
   # Edit KubeletConfiguration to enable seccomp defaulting
   vi /var/lib/kubelet/config.yaml
   ```
   Add or update:
   ```yaml
   seccompDefault: true
   ```
   Restart the Kubelet service:
   ```bash
   systemctl daemon-reload
   systemctl restart kubelet
   systemctl status kubelet --no-pager
   exit
   ```

5. **Low-Level Verification with `crictl`:**
   Verify the seccomp profile applied by the runtime inside the worker node container:
   ```bash
   ssh node01
   # Obtain container ID
   CID=$(crictl ps --name=nginx -q)
   # Inspect Linux OCI seccomp specification
   crictl inspect $CID | jq .info.runtimeSpec.linux.seccomp
   # Expected Output: "defaultAction": "SCMP_ACT_ERRNO" or "SCMP_ACT_ALLOW" with restricted syscalls
   exit
   ```

> [!CAUTION]
> **Exam Pitfall:** If a container has `privileged: true`, Kubernetes will **ignore** any configured `seccompProfile` and the container will run as `Unconfined`. In the CKS exam, always ensure `privileged: false` (or omitted) and `allowPrivilegeEscalation: false` when hardening workloads with seccomp.

---

## 📦 Scenario 7: Sandboxed Workloads with gVisor (`runsc`)

### Problem Statement
Configure a `RuntimeClass` named `gvisor` mapped to handler `runsc`. Deploy an untrusted workload named `untrusted-worker` using this RuntimeClass.

### Step-by-Step Implementation

1. **Create the `RuntimeClass` Object:**
   ```yaml
   apiVersion: node.k8s.io/v1
   kind: RuntimeClass
   metadata:
     name: gvisor
   handler: runsc
   ```
   ```bash
   kubectl apply -f runtimeclass-gvisor.yaml
   ```

2. **Deploy Pod Specifying `runtimeClassName`:**
   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: untrusted-worker
     namespace: default
   spec:
     runtimeClassName: gvisor
     containers:
     - name: app
       image: python:3.11-alpine
       command: ["python", "-c", "import os; print('Kernel:', os.uname())"]
   ```
   ```bash
   kubectl apply -f pod-gvisor.yaml
   ```

3. **Verify gVisor Sentry Kernel:**
   ```bash
   kubectl logs untrusted-worker
   # Output should indicate gVisor user-space kernel (e.g., Linux ... gVisor ... x86_64)
   ```

---

## 🔍 Scenario 8: Vulnerability Scanning with Trivy

### Problem Statement
Scan container image `nginx:1.14.2` using `trivy`. Identify all vulnerabilities with severity `CRITICAL`. If any CRITICAL vulnerabilities exist, delete the deployment `legacy-nginx` running that image.

### Step-by-Step Implementation

1. **Execute Trivy Image Scan:**
   ```bash
   trivy image --severity CRITICAL nginx:1.14.2
   ```

2. **Parse Specific CVEs or Check Exit Code:**
   ```bash
   # CI/CD check mode (fails if CRITICAL exists)
   trivy image --exit-code 1 --severity CRITICAL nginx:1.14.2
   echo $? # Returns 1 if vulnerabilities found
   ```

3. **Remediate Deployment:**
   ```bash
   kubectl get deployment legacy-nginx -o jsonpath='{.spec.template.spec.containers[*].image}'
   # If image is nginx:1.14.2:
   kubectl delete deployment legacy-nginx
   ```

---

## 🧬 Scenario 9: ImagePolicyWebhook Admission Configuration

### Problem Statement
Enable the `ImagePolicyWebhook` admission controller on the master node. Use the configuration file `/etc/kubernetes/admission/admission-config.yaml` which references the kubeconfig `/etc/kubernetes/admission/webhook-kubeconfig.yaml`. Set `defaultAllow: false` to enforce fail-close behavior.

### Step-by-Step Implementation

1. **Create Webhook Kubeconfig (`/etc/kubernetes/admission/webhook-kubeconfig.yaml`):**
   ```yaml
   apiVersion: v1
   kind: Config
   clusters:
   - cluster:
       certificate-authority: /etc/kubernetes/admission/external-ca.crt
       server: https://image-checker.default.svc:8443/image-policy
     name: image-checker
   contexts:
   - context:
       cluster: image-checker
       user: apiserver
     name: image-checker-ctx
   current-context: image-checker-ctx
   preferences: {}
   users:
   - name: apiserver
     user:
       client-certificate: /etc/kubernetes/admission/apiserver-client.crt
       client-key: /etc/kubernetes/admission/apiserver-client.key
   ```

2. **Create Admission Configuration (`/etc/kubernetes/admission/admission-config.yaml`):**
   ```yaml
   apiVersion: apiserver.config.k8s.io/v1
   kind: AdmissionConfiguration
   plugins:
   - name: ImagePolicyWebhook
     configuration:
       imagePolicy:
         kubeConfigFile: /etc/kubernetes/admission/webhook-kubeconfig.yaml
         allowTTL: 50
         denyTTL: 50
         retryBackOff: 500
         defaultAllow: false
   ```

3. **Update `kube-apiserver.yaml` Static Pod Manifest:**
   ```bash
   vim /etc/kubernetes/manifests/kube-apiserver.yaml
   ```
   Add the following flags:
   ```yaml
   - --enable-admission-plugins=NodeRestriction,ImagePolicyWebhook
   - --admission-control-config-file=/etc/kubernetes/admission/admission-config.yaml
   ```
   Add volume and volumeMount if `/etc/kubernetes/admission` is not already covered:
   ```yaml
   volumeMounts:
   - mountPath: /etc/kubernetes/admission
     name: admission-config
     readOnly: true
   volumes:
   - hostPath:
       path: /etc/kubernetes/admission
       type: DirectoryOrCreate
     name: admission-config
   ```

4. **Verify API Server Restart:**
   ```bash
   crictl ps --name kube-apiserver
   # Test rejected pod:
   kubectl run unapproved --image=docker.io/unverified/image:latest
   # Expected: Forbidden by ImagePolicyWebhook
   ```

---

## 🛡️ Scenario 10: Pod Security Admission (PSA) & SecurityContext Hardening

### Problem Statement
Enforce the `restricted` Pod Security Standard in namespace `finance-prod`. Modify deployment `finance-api` so that it satisfies all Restricted PSS requirements: non-root user, read-only root filesystem, drop ALL capabilities, and RuntimeDefault seccomp.

### Step-by-Step Implementation

1. **Label the Namespace:**
   ```bash
   kubectl label namespace finance-prod \
     pod-security.kubernetes.io/enforce=restricted \
     pod-security.kubernetes.io/enforce-version=latest \
     pod-security.kubernetes.io/warn=restricted \
     pod-security.kubernetes.io/audit=restricted --overwrite
   ```

2. **Update Deployment SecurityContext:**
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: finance-api
     namespace: finance-prod
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: finance-api
     template:
       metadata:
         labels:
           app: finance-api
       spec:
         securityContext:
           runAsNonRoot: true
           runAsUser: 10001
           runAsGroup: 10001
           seccompProfile:
             type: RuntimeDefault
         containers:
         - name: api
           image: nginx:alpine
           securityContext:
             allowPrivilegeEscalation: false
             readOnlyRootFilesystem: true
             capabilities:
               drop:
               - ALL
           volumeMounts:
           - name: cache-vol
             mountPath: /var/cache/nginx
           - name: pid-vol
             mountPath: /var/run
         volumes:
         - name: cache-vol
           emptyDir: {}
         - name: pid-vol
           emptyDir: {}
   ```

3. **Verify Deployment Rollout:**
   ```bash
   kubectl rollout status deployment/finance-api -n finance-prod
   ```

---

## 🗝️ Scenario 11: Secret Encryption at Rest & etcd Verification

### Problem Statement
Configure AES-CBC encryption at rest for secrets in `etcd`. Verify directly via `etcdctl` that secret `db-creds` in `default` is encrypted with the `k8s:enc:aescbc:v1` prefix.

### Step-by-Step Implementation

1. **Generate 32-byte Base64 Key:**
   ```bash
   head -c 32 /dev/urandom | base64
   # Example output: c2VjdXJlZXhhbXBsZWtleWZvcmV4YW1wbGVjdXN0b20=
   ```

2. **Create Encryption Configuration (`/etc/kubernetes/enc/enc.yaml`):**
   ```yaml
   apiVersion: apiserver.config.k8s.io/v1
   kind: EncryptionConfiguration
   resources:
     - resources:
         - secrets
       providers:
         - aescbc:
             keys:
               - name: key1
                 secret: c2VjdXJlZXhhbXBsZWtleWZvcmV4YW1wbGVjdXN0b20=
         - identity: {}
   ```

3. **Update `kube-apiserver.yaml`:**
   ```yaml
   # Under command:
   - --encryption-provider-config=/etc/kubernetes/enc/enc.yaml
   # Under volumeMounts:
   - mountPath: /etc/kubernetes/enc
     name: enc-dir
     readOnly: true
   # Under volumes:
   - hostPath:
       path: /etc/kubernetes/enc
       type: DirectoryOrCreate
     name: enc-dir
   ```

4. **Verify API Server Health & Create Secret:**
   ```bash
   crictl ps --name kube-apiserver
   kubectl create secret generic db-creds --from-literal=password=SuperPass123
   ```

5. **Verify Encrypted Value in etcd:**
   ```bash
   ETCDCTL_API=3 etcdctl \
     --cacert=/etc/kubernetes/pki/etcd/ca.crt \
     --cert=/etc/kubernetes/pki/etcd/server.crt \
     --key=/etc/kubernetes/pki/etcd/server.key \
     get /registry/secrets/default/db-creds --raw | hexdump -C | head -n 4
   # Verify that output starts with: k8s:enc:aescbc:v1:key1:...
   ```

6. **Re-encrypt Existing Secrets:**
   ```bash
   kubectl get secrets -A -o json | kubectl replace -f -
   ```

---

## 📜 Scenario 12: Kubernetes API Server Auditing

### Problem Statement
Create an audit policy at `/etc/kubernetes/audit/policy.yaml` with the following rules:
* Log Pod changes at `Request` level.
* Log Secret changes at `Metadata` level only.
* Do not log health check queries (`None`).
* Configure `kube-apiserver` to log to `/var/log/kubernetes/audit.log` with maxage 7 days.

### Step-by-Step Implementation

1. **Create Policy (`/etc/kubernetes/audit/policy.yaml`):**
   ```yaml
   apiVersion: audit.k8s.io/v1
   kind: Policy
   omitStages:
     - "RequestReceived"
   rules:
     - level: None
       nonResourceURLs:
         - "/healthz*"
         - "/livez*"
         - "/readyz*"
     - level: Metadata
       resources:
         - group: ""
           resources: ["secrets"]
     - level: Request
       resources:
         - group: ""
           resources: ["pods"]
     - level: Metadata
   ```

2. **Update `kube-apiserver.yaml`:**
   ```yaml
   command:
   - --audit-policy-file=/etc/kubernetes/audit/policy.yaml
   - --audit-log-path=/var/log/kubernetes/audit.log
   - --audit-log-maxage=7
   - --audit-log-maxbackup=5
   - --audit-log-maxsize=100
   volumeMounts:
   - mountPath: /etc/kubernetes/audit
     name: audit-conf
     readOnly: true
   - mountPath: /var/log/kubernetes
     name: audit-log-dir
     readOnly: false
   volumes:
   - hostPath:
       path: /etc/kubernetes/audit
       type: DirectoryOrCreate
     name: audit-conf
   - hostPath:
       path: /var/log/kubernetes
       type: DirectoryOrCreate
     name: audit-log-dir
   ```

3. **Verify Audit Records:**
   ```bash
   tail -f /var/log/kubernetes/audit.log | grep -i "secrets"
   ```

---

## 🔍 Scenario 13: Runtime Threat Detection with Custom Falco Rules

### Problem Statement
Configure a custom Falco rule in `/etc/falco/falco_rules.local.yaml` named `Detect Shadow File Read` that triggers an `ALERT` priority alert whenever any process inside a container opens `/etc/shadow` for reading. Restart Falco and verify using an interactive pod.

### Step-by-Step Implementation

1. **Add Custom Rule to `/etc/falco/falco_rules.local.yaml`:**
   ```yaml
   - rule: Detect Shadow File Read
     desc: Detect any read access to /etc/shadow inside a container
     condition: >
       open_read and 
       container and 
       fd.name = "/etc/shadow"
     output: >
       Sensitive file read detected (user=%user.name file=%fd.name 
       proc=%proc.name cmdline=%proc.cmdline container_id=%container.id 
       container_name=%container.name)
     priority: ALERT
     tags: [filesystem, security]
   ```

2. **Validate and Restart Falco:**
   ```bash
   falco --validate /etc/falco/falco_rules.local.yaml
   systemctl restart falco
   systemctl status falco
   ```

3. **Simulate Attack & Verify Alert:**
   ```bash
   kubectl run attacker --image=busybox --rm -it -- cat /etc/shadow
   ```
   Inspect Falco alert:
   ```bash
   journalctl -u falco -n 20 --no-pager | grep "Sensitive file read detected"
   ```

---

## 📋 Scenario 14: Certificate Expiration Audits & Renewal

### Problem Statement
Inspect the control plane certificates. Identify the certificate expiration date for `apiserver.crt`. Renew all certificates using `kubeadm` and restart the static pods.

### Step-by-Step Implementation

1. **Check Expirations:**
   ```bash
   kubeadm certs check-expiration
   ```

2. **Inspect with OpenSSL:**
   ```bash
   openssl x509 -in /etc/kubernetes/pki/apiserver.crt -text -noout | grep -A 2 "Validity"
   ```

3. **Renew All Certificates:**
   ```bash
   kubeadm certs renew all
   ```

4. **Restart Static Pods:**
   ```bash
   # Move and replace manifests or kill containers via crictl:
   crictl rmp -f $(crictl pods --name kube-apiserver -q)
   ```

---

## 🔒 Scenario 15: Docker Daemon Hardening & Unix Socket Isolation

### Problem Statement
1. Security auditing identifies that worker node `node01` has the Docker daemon exposed over an unencrypted, unauthenticated TCP port (`tcp://0.0.0.0:2375`). Reconfigure `/etc/docker/daemon.json` so the daemon listens exclusively on the local Unix socket `unix:///var/run/docker.sock` and a secure TLS endpoint on `tcp://192.168.1.11:2376`.
2. Enforce mutual client certificate authentication (`tlsverify: true`) using CA `/var/docker/cacert.pem`, server cert `/var/docker/server.pem`, and server key `/var/docker/serverkey.pem`.
3. Resolve any systemd service flag conflicts and restart the Docker service.
4. Audit namespace `dev` for any pod mounting `/var/run/docker.sock` (or CRI socket) via `hostPath`. Remediate the pod manifest to prevent container breakout to the host root.

### Step-by-Step Implementation

1. **Access Node and Audit Listening Ports:**
   ```bash
   ssh node01
   # Confirm insecure 2375 listener
   ss -tulpn | grep 2375
   ```

2. **Configure `/etc/docker/daemon.json`:**
   ```bash
   cat <<EOF > /etc/docker/daemon.json
   {
     "hosts": [
       "unix:///var/run/docker.sock",
       "tcp://192.168.1.11:2376"
     ],
     "tls": true,
     "tlscert": "/var/docker/server.pem",
     "tlskey": "/var/docker/serverkey.pem",
     "tlsverify": true,
     "tlscacert": "/var/docker/cacert.pem"
   }
   EOF
   ```

3. **Check for Flag Conflicts in Systemd:**
   ```bash
   # If systemd passes -H flags to dockerd, remove them to avoid fatal startup conflict:
   grep -E 'ExecStart.*-H' /lib/systemd/system/docker.service
   # If present, create a systemd drop-in override:
   mkdir -p /etc/systemd/system/docker.service.d/
   cat <<EOF > /etc/systemd/system/docker.service.d/override.conf
   [Service]
   ExecStart=
   ExecStart=/usr/bin/dockerd --containerd=/run/containerd/containerd.sock
   EOF
   ```

4. **Reload Systemd and Restart Docker Daemon:**
   ```bash
   systemctl daemon-reload
   systemctl restart docker
   systemctl status docker
   # Verify port 2376 is listening with TLS, and 2375 is closed
   ss -tulpn | grep -E '2375|2376'
   ```

5. **Verify Secure Client Authentication:**
   ```bash
   export DOCKER_HOST="tcp://192.168.1.11:2376"
   export DOCKER_TLS_VERIFY=true
   docker --tlscert=/var/docker/client.pem --tlskey=/var/docker/client-key.pem --tlscacert=/var/docker/cacert.pem ps
   exit
   ```

6. **Audit and Remediate HostPath Socket Breakout in Kubernetes:**
   ```bash
   # Find pods mounting host docker.sock or containerd.sock
   kubectl get pods -n dev -o json | jq -r '.items[] | select(.spec.volumes[]?.hostPath.path | test(".*\\.sock$")) | .metadata.name'
   
   # Inspect untrusted-builder pod
   kubectl get pod untrusted-builder -n dev -o yaml > /tmp/builder.yaml
   
   # Remove hostPath volume and volumeMount pointing to /var/run/docker.sock
   # Re-apply hardened workload
   kubectl delete pod untrusted-builder -n dev --force --grace-period=0
   kubectl apply -f /tmp/builder.yaml
   ```

---

## 🛡️ Scenario 16: Manifest Security Linting with KubeLinter & Immutability

### Problem Statement
A developer committed a deployment manifest `/root/staging/web-deploy.yaml` that fails organizational security baselines.
1. Run `kubelinter` against `/root/staging/web-deploy.yaml` to identify security violations.
2. Remediate the manifest:
   * Enforce a read-only root filesystem (`readOnlyRootFilesystem: true`).
   * Add an ephemeral `emptyDir` volume mounted at `/var/cache/nginx` and `/var/run` to allow Nginx to start without rootfs write access.
   * Run the container as non-root user UID `10001` with privilege escalation disabled.
3. Re-run `kubelinter` to confirm zero violations.

### Step-by-Step Implementation

1. **Lint Manifest:**
   ```bash
   kubelinter lint /root/staging/web-deploy.yaml
   # Output flags: no-read-only-root-fs, run-as-non-root, privilege-escalation
   ```

2. **Remediate `/root/staging/web-deploy.yaml`:**
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: secure-web
     namespace: staging
   spec:
     replicas: 2
     selector:
       matchLabels:
         app: secure-web
     template:
       metadata:
         labels:
           app: secure-web
       spec:
         securityContext:
           runAsNonRoot: true
           runAsUser: 10001
         containers:
           - name: nginx
             image: nginx:alpine
             securityContext:
               readOnlyRootFilesystem: true
               allowPrivilegeEscalation: false
             volumeMounts:
               - name: cache-vol
                 mountPath: /var/cache/nginx
               - name: run-vol
                 mountPath: /var/run
         volumes:
           - name: cache-vol
             emptyDir: {}
           - name: run-vol
             emptyDir: {}
   ```

3. **Verify Linting Passes:**
   ```bash
   kubelinter lint /root/staging/web-deploy.yaml
   # Output: No lint errors found
   kubectl apply -f /root/staging/web-deploy.yaml
   ```

---

## 🧬 Scenario 17: OPA Gatekeeper Policy Enforcement

### Problem Statement
Enforce governance using OPA Gatekeeper. All newly created Namespaces must have an `owner` label.
1. Create a `ConstraintTemplate` named `k8srequiredlabels` using Rego to check for missing labels in `input.parameters.labels`.
2. Instantiate a `Constraint` named `ns-must-have-owner` enforcing the `owner` label on `Namespace` objects.
3. Verify that creating an unlabelled namespace is blocked with an informative error message.

### Step-by-Step Implementation

1. **Deploy ConstraintTemplate:**
   ```yaml
   apiVersion: templates.gatekeeper.sh/v1
   kind: ConstraintTemplate
   metadata:
     name: k8srequiredlabels
   spec:
     crd:
       spec:
         names:
           kind: K8sRequiredLabels
         validation:
           openAPIV3Schema:
             properties:
               labels:
                 type: array
                 items:
                   type: string
     targets:
       - target: admission.k8s.gatekeeper.sh
         rego: |
           package k8srequiredlabels
           violation[{"msg": msg}] {
             provided := {label | input.review.object.metadata.labels[label]}
             required := {label | label := input.parameters.labels[_]}
             missing := required - provided
             count(missing) > 0
             msg := sprintf("Resource missing mandatory labels: %v", [missing])
           }
   ```
   Save and apply: `kubectl apply -f template.yaml`

2. **Deploy Constraint:**
   ```yaml
   apiVersion: constraints.gatekeeper.sh/v1beta1
   kind: K8sRequiredLabels
   metadata:
     name: ns-must-have-owner
   spec:
     match:
       kinds:
         - apiGroups: [""]
           kinds: ["Namespace"]
     parameters:
       labels: ["owner"]
   ```
   Save and apply: `kubectl apply -f constraint.yaml`

3. **Verify Enforcement:**
   ```bash
   # Test unlabelled namespace (must fail):
   kubectl create namespace test-fail
   # Expected Error: Error from server (Forbidden): admission webhook "validation.gatekeeper.sh" denied the request: Resource missing mandatory labels: {"owner"}

   # Test compliant namespace (must succeed):
   kubectl create namespace test-pass --dry-run=client -o yaml | kubectl label --local -f - owner=devops -o yaml | kubectl apply -f -
   ```

---

## ⚙️ Scenario 18: Security-Conscious Cluster Upgrade with `kubeadm`

### Problem Statement
Upgrade master node `controlplane` from version `1.29.0` to `1.29.2`.
1. Plan the upgrade and update `kubeadm`.
2. Apply the upgrade using `kubeadm upgrade apply v1.29.2`.
3. Safely drain `controlplane`, upgrade `kubelet` and `kubectl`, and restart services.
4. Verify cluster status and confirm etcd/API security flags persist.

### Step-by-Step Implementation

1. **Upgrade kubeadm:**
   ```bash
   apt-mark unhold kubeadm
   apt-get update && apt-get install -y kubeadm=1.29.2-1.1
   apt-mark hold kubeadm
   kubeadm version
   ```

2. **Plan & Apply Control Plane Upgrade:**
   ```bash
   kubeadm upgrade plan
   kubeadm upgrade apply v1.29.2 -y
   ```

3. **Drain Control Plane Node:**
   ```bash
   kubectl drain controlplane --ignore-daemonsets
   ```

4. **Upgrade Kubelet and Kubectl:**
   ```bash
   apt-mark unhold kubelet kubectl
   apt-get install -y kubelet=1.29.2-1.1 kubectl=1.29.2-1.1
   apt-mark hold kubelet kubectl
   systemctl daemon-reload
   systemctl restart kubelet
   kubectl uncordon controlplane
   ```

5. **Post-Upgrade Security Verification:**
   ```bash
   kubectl get nodes
   kubeadm certs check-expiration
   kube-bench run --targets master
   ```

---

## 🔒 Scenario 19: Linux Capabilities Stripping & Least Privilege Verification

### Problem Statement
A microservice pod named `production-proxy` running in the `security-demo` namespace is currently executing with standard container default capabilities. An audit flagged this as a high risk because unnecessary capabilities (such as `CAP_NET_RAW`, `CAP_SYS_CHROOT`, and `CAP_SYS_TIME`) remain accessible.
1. Reconfigure the pod manifest so that **all default capabilities are dropped**.
2. Grant only **`NET_BIND_SERVICE`** to allow the container to bind to port 80.
3. Enforce **`allowPrivilegeEscalation: false`** to enable the kernel's `no_new_privs` bit.
4. Verify that privileged syscalls like changing the system clock (`date -s`) fail with `Operation not permitted`.
5. On the host node, inspect the running container process using `crictl` and `getpcaps` to confirm the stripped capability set.

### Step-by-Step Implementation

1. **Craft the Hardened Pod Manifest (`hardened-proxy.yaml`):**
   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: production-proxy
     namespace: security-demo
   spec:
     containers:
     - name: proxy
       image: nginx:alpine
       securityContext:
         allowPrivilegeEscalation: false
         capabilities:
           drop:
           - ALL
           add:
           - NET_BIND_SERVICE
   ```

2. **Apply Workload:**
   ```bash
   kubectl create namespace security-demo --dry-run=client -o yaml | kubectl apply -f -
   kubectl apply -f hardened-proxy.yaml
   kubectl get pod -n security-demo production-proxy
   ```

3. **Verify Capability Stripping via Container Execution:**
   Attempt to execute a system-time change (which requires `CAP_SYS_TIME`):
   ```bash
   kubectl exec -n security-demo production-proxy -- date -s "2030-01-01 12:00:00"
   # Expected Output: date: can't set date: Operation not permitted
   ```

4. **Audit Capabilities on the Worker Node:**
   ```bash
   # SSH to the node hosting the pod (e.g. node01)
   ssh node01

   # Identify the container PID via crictl:
   CONTAINER_ID=$(crictl ps --name=proxy -q | head -n1)
   PID=$(crictl inspect $CONTAINER_ID | jq .info.pid)

   # Inspect active capabilities of the container process:
   getpcaps $PID
   # Expected Output: <PID>: cap_net_bind_service=ep

   # Alternatively, decode directly from /proc:
   grep CapEff /proc/$PID/status
   # Decode hexadecimal mask:
   capsh --decode=$(grep CapEff /proc/$PID/status | awk '{print $2}')
   # Expected Output: 0x0000000000000400=cap_net_bind_service
   exit
   ```

---

## 💡 CKS Exam Checklist & Quick Reference

| Exam Objective | High-Frequency File / Command | Key Flag or Resource |
| :--- | :--- | :--- |
| **API Server Audit** | `/etc/kubernetes/manifests/kube-apiserver.yaml` | `--audit-policy-file`, `--audit-log-path` |
| **Secret Encryption** | `/etc/kubernetes/manifests/kube-apiserver.yaml` | `--encryption-provider-config` (`aescbc`) |
| **Kubelet Security** | `/var/lib/kubelet/config.yaml` | `readOnlyPort: 0`, `anonymous.enabled: false` |
| **AppArmor** | `/etc/apparmor.d/*` | `apparmor_parser -q <file>`, `securityContext.appArmorProfile` |
| **Seccomp** | `/var/lib/kubelet/seccomp/*` | `securityContext.seccompProfile.type: RuntimeDefault` |
| **Falco** | `/etc/falco/falco_rules.local.yaml` | `systemctl restart falco`, `journalctl -u falco -f` |
| **Trivy** | `trivy image --severity HIGH,CRITICAL <image>` | `--ignore-unfixed`, `--exit-code 1` |
| **NetworkPolicy** | `kind: NetworkPolicy` | `policyTypes: [Ingress, Egress]`, `except: [169.254.169.254/32]` |
| **CIS Benchmark** | `kube-bench run --targets master,node` | File permission `chmod 600`, ownership `root:root` |
| **Docker API / Daemon** | `/etc/docker/daemon.json` | `"tlsverify": true`, `"hosts": ["...:2376"]`, audit `docker.sock` mounts |
| **KubeLinter / Immutability** | `kubelinter lint <file.yaml>` | `readOnlyRootFilesystem: true`, `emptyDir: {}` mount |
| **OPA Gatekeeper** | `ConstraintTemplate` & `Constraint` | `rego: | ...`, `kinds: [Namespace]` |
| **Cluster Upgrade** | `kubeadm upgrade apply v1.XX.Y` | `kubectl drain --ignore-daemonsets`, `apt-mark hold` |
| **Linux Capabilities** | `securityContext.capabilities` | `drop: [ALL]`, `add: [NET_BIND_SERVICE]`, `capsh --decode` |
| **Syscall Tracing / strace** | `strace -c <cmd>`, `strace -p <PID>` | Discover required syscalls for Seccomp profile |
| **Host Service Masking** | `systemctl mask <service>` | Symlinks unit to `/dev/null`, prevents start |


