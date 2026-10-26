# CKS Exam Notes

## 1. Docker Secure
* `gpasswd -d developer docker`
* `group develope`
* `vi /usr/lib/systemd/system/docker.sock`
* `group make it root`
* `systemctl daemon_reload`
* `restart docker`
* `ls -la /var/run/docker.sock`
* `vi /usr/lib/systemd/system/docker.service`
* `remove tcp`
* `daemon reload + restart docker`
* `netstat -tulpn | grep 2375`

## 2. Cilium ingress
* 1 - tls ingress from documentation
* 2 - annotations: 
  * `ingress.cilium.io/force-https: "enabled"`
* 3 - `ingressClassName: cilium`
* 4 - change `host_secretname_service`
* `curl -k https://web.k8s.local:32001`

## 3. Update kubelet configs and etcd
* `vi /var/lib/kubelet/config.yaml`
  * `authentication:`
    * `enabled: false` 
  * `webhook:`
    * `enabled: true`
  * `authorization:`
    * `mode: Webhook`
* `vi /etc/kubernetes/manifests/etcd`
  * `--client-cert-auth=true`
* `systemctl daemon_reload`
* `restart kubelet`
* `k get nodes`

## 4. Istio
* 1 -> `k label ns ----- istio-injection=enabled --overwrite`
* 3 -> `vi mtls.yaml -> From configs`
* 4 -> `k apply -f -----`
* 2 -> `k rollout restart deployment -n ---- deployname`
* `k get po -n -----`

## 5. ImagePolicy Webhook
* `vi /etc/kubernetes/webhook/image-policy.yaml`
  * `defaultAllow: false`
* `vi /etc/kubernetes/webhook/kubeconfig`
  * `server -> from Exam`
* `vi /etc/kubernetes/manifests/kube-apiserver`
  * `--enable-admission-plugins=ImagePolicyWebhook`
  * `admission-control-config-file=-------`

## 6. Privileged / restricted pod
* `k describe rs -n ------` -> Ready: 0, error: 109
* `securityContext:`
  * `allowPrivilegeEscalation: false`
  * `capabilities:`
    * `drop:`
      * `- ALL`
  * `runAsNonRoot: true`
  * `seccompProfile:`
    * `type: RuntimeDefault`
  * `runAsUser: 1000`

## 7. Falco
* we will check falco pod or service
* `falco --version` or `k get po -n falco`
* `vi /etc/falco/falco_rules.local.yaml`
  * `rule: container access /dev/mem`
  * `desc: "-----------"`
  * `condition: open_read and fd.name="/dev/mem" and container`
  * `output: pod_name=%container.id`
  * `Priority: warning`
* `sudo falco -r /etc/falco/falco_rules.local.yaml`

## 8. TLS secret
* `k scale deploy -n ------ deploy --replicas=0`
* `k get rs -n ------`
* `k get po -n ------`
* `k create secret tls secret-tls -n ----- --cert=------- --key=-------`

## 9. Dockerfile and yaml file security
* Dockerfile -> `USER nobody`
* Yaml file -> 
  * `runAsUser=-----`
  * `readOnlyRootFilesystem: true`
  * `privileged: false`

## 10. Ensure immutability for 2 containers
* `runAsUser: ------`
* `readOnlyRootFilesystem: true`
* `allowPrivilegeEscalation: false`

## 11. Generate spdx document
* `k exec -n ----- exec Podname -c ----- -- apk list libcrypto` (For 3 containers)
* remove bugged container
* bom generate required image -o required output

## 12. Upgrade cluster(node)
* `k drain specificnode --ignore-daemonsets --delete-emptydir --force`
* `k get nodes`
* `ssh node02`
* `sudo -i`
* Do as Documentation to upgrade kubeadm kubelet kubectl
* to make sure `kubelet version = kubectl version`
* `exit`
* `kubectl uncordon node02`
* `k get nodes`

## 13. Disable automount serviceaccount
* `k create sa bot-sa`
* `k edit sa bot-sa`
  * and add `automountServiceAccountToken: false`
* `k edit deploy -n -----`
  * `ServiceAccountName: -----`
  * `autoMountServiceAccountToken: false`
* add Projected Volume as documentation

## 14. Network Policy
* Deny all ingress traffic
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: -----
  namespace: -----
spec:
  podSelector: {}
  policyTypes:
  - Ingress
```
* Allow ingress only from pods within a specific namespace
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: -----
  namespace: -----
spec:
  podSelector: {}
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          ---: ---
    ports:
    - protocol: TCP
      port: ---
```

## 15. Auditing
* `vi policy.yaml` -> update policy as request
* `vi /etc/kubernetes/manifests/kube-apiserver`
  * `--audit-log-path`
  * `--audit-policy-file`
  * `--audit-maxage`
  * `--audit-maxbackup`
* make sure volume and volume mount exist or not [from Documentation]
* For investigating:
  * `crictl ps -a | grep "kube-apiserver"`
  * `crictl logs container-id`

## 16. API server authentication
* `vi /etc/kubernetes/manifests/kube-apiserver`
* add `--anonymous-auth=false`
* `--authorization-mode=Node,RBAC`
* `--enable-admission-plugins=AlwaysAdmit,NodeRestriction` (This was already present)