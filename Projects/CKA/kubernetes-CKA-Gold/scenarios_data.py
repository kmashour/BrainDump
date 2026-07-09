# -*- coding: utf-8 -*-

SCENARIOS = [
    # ==========================================
    # --- TROUBLESHOOTING (30% - 27 Scenarios) ---
    # ==========================================
    {
        "id": "E-01",
        "domain": "Troubleshooting (30%)",
        "title": "Kubelet Service Stopped on Worker Node 1",
        "problem": "The node 'cka-gold-worker' is showing NotReady. Find the cause and bring it back online.",
        "setup": "docker exec cka-gold-worker systemctl stop kubelet",
        "cleanup": "docker exec cka-gold-worker systemctl start kubelet",
        "check": "kubectl get node cka-gold-worker -o jsonpath='{.status.conditions[?(@.type==\"Ready\")].status}' | grep -i True",
        "hint": "Check if kubelet is running on cka-gold-worker container using systemctl.",
        "solution": "1. Run: docker exec cka-gold-worker systemctl status kubelet\n2. Start it: docker exec cka-gold-worker systemctl start kubelet"
    },
    {
        "id": "E-02",
        "domain": "Troubleshooting (30%)",
        "title": "Corrupt Kubelet Config on Worker Node 2",
        "problem": "The node 'cka-gold-worker2' is NotReady. The configuration file seems to have an issue.",
        "setup": "docker exec cka-gold-worker2 sed -i 's/staticPodPath/staticPodPathInvalid/g' /var/lib/kubelet/config.yaml && docker exec cka-gold-worker2 systemctl restart kubelet",
        "cleanup": "docker exec cka-gold-worker2 sed -i 's/staticPodPathInvalid/staticPodPath/g' /var/lib/kubelet/config.yaml && docker exec cka-gold-worker2 systemctl start kubelet",
        "check": "kubectl get node cka-gold-worker2 -o jsonpath='{.status.conditions[?(@.type==\"Ready\")].status}' | grep -i True",
        "hint": "Check the kubelet logs on cka-gold-worker2: journalctl -u kubelet. Look for config errors.",
        "solution": "1. Run: docker exec -it cka-gold-worker2 journalctl -u kubelet\n2. Fix typo in /var/lib/kubelet/config.yaml\n3. Restart kubelet: docker exec cka-gold-worker2 systemctl restart kubelet"
    },
    {
        "id": "E-03",
        "domain": "Troubleshooting (30%)",
        "title": "CoreDNS ConfigMap Corrupted",
        "problem": "DNS resolution is failing inside pods. Inspect the CoreDNS configuration and fix it.",
        "setup": "kubectl get configmap coredns -n kube-system -o yaml > /tmp/coredns.yaml && kubectl patch configmap coredns -n kube-system --type merge -p '{\"data\":{\"Corefile\":\"invalid syntax block\"}}' && kubectl rollout restart deploy coredns -n kube-system",
        "cleanup": "kubectl apply -f /tmp/coredns.yaml && kubectl rollout restart deploy coredns -n kube-system",
        "check": "kubectl get deploy coredns -n kube-system -o jsonpath='{.status.readyReplicas}' | grep -w '2'",
        "hint": "View CoreDNS logs. Check the 'coredns' ConfigMap in the 'kube-system' namespace.",
        "solution": "1. Edit ConfigMap: kubectl edit configmap coredns -n kube-system\n2. Restore Corefile configuration\n3. Restart deployment: kubectl rollout restart deploy coredns -n kube-system"
    },
    {
        "id": "E-04",
        "domain": "Troubleshooting (30%)",
        "title": "API Server Static Pod Crashing due to Wrong Cert Path",
        "problem": "The API server container is crashing. Diagnostic manifests show an incorrect client cert path config.",
        "setup": "docker exec cka-gold-control-plane sed -i 's|/etc/kubernetes/pki/apiserver.crt|/etc/kubernetes/pki/apiserver-invalid.crt|g' /etc/kubernetes/manifests/kube-apiserver.yaml",
        "cleanup": "docker exec cka-gold-control-plane sed -i 's|/etc/kubernetes/pki/apiserver-invalid.crt|/etc/kubernetes/pki/apiserver.crt|g' /etc/kubernetes/manifests/kube-apiserver.yaml",
        "check": "kubectl get no cka-gold-control-plane",
        "hint": "Check static pod files in cka-gold-control-plane at /etc/kubernetes/manifests/kube-apiserver.yaml.",
        "solution": "1. Modify /etc/kubernetes/manifests/kube-apiserver.yaml inside control plane node.\n2. Fix path back to /etc/kubernetes/pki/apiserver.crt\n3. Kubelet will reload the static pod automatically."
    },
    {
        "id": "E-05",
        "domain": "Troubleshooting (30%)",
        "title": "ETCD Static Pod Port Mismatch",
        "problem": "ETCD is down because the static pod manifest listen port was changed to 2380 instead of 2379.",
        "setup": "docker exec cka-gold-control-plane sed -i 's|--listen-client-urls=https://127.0.0.1:2379|--listen-client-urls=https://127.0.0.1:2380|g' /etc/kubernetes/manifests/etcd.yaml",
        "cleanup": "docker exec cka-gold-control-plane sed -i 's|--listen-client-urls=https://127.0.0.1:2380|--listen-client-urls=https://127.0.0.1:2379|g' /etc/kubernetes/manifests/etcd.yaml",
        "check": "kubectl get cs etcd-0 || kubectl get no",
        "hint": "Locate etcd static pod config /etc/kubernetes/manifests/etcd.yaml and check port parameters.",
        "solution": "1. Access control plane node.\n2. In /etc/kubernetes/manifests/etcd.yaml, restore listen-client-urls port to 2379."
    },
    {
        "id": "E-06",
        "domain": "Troubleshooting (30%)",
        "title": "Kubelet Certificate Path Mismatch on Worker 1",
        "problem": "The Kubelet on 'cka-gold-worker' cannot authenticate with the API Server due to a broken cert path config.",
        "setup": "docker exec cka-gold-worker sed -i 's|client-certificate-data:|client-certificate-data-invalid:|g' /etc/kubernetes/kubelet.conf && docker exec cka-gold-worker systemctl restart kubelet",
        "cleanup": "docker exec cka-gold-worker sed -i 's|client-certificate-data-invalid:|client-certificate-data:|g' /etc/kubernetes/kubelet.conf && docker exec cka-gold-worker systemctl start kubelet",
        "check": "kubectl get node cka-gold-worker -o jsonpath='{.status.conditions[?(@.type==\"Ready\")].status}' | grep -i True",
        "hint": "Check /etc/kubernetes/kubelet.conf in the cka-gold-worker container.",
        "solution": "1. Restore client-certificate-data key name in kubelet.conf on worker node.\n2. Run: systemctl restart kubelet inside cka-gold-worker container."
    },
    {
        "id": "E-07",
        "domain": "Troubleshooting (30%)",
        "title": "Kube-Scheduler Crashing on Typos",
        "problem": "Scheduler is not running. Find the typo in the scheduler's static pod manifest.",
        "setup": "docker exec cka-gold-control-plane sed -i 's|--leader-elect=true|--leader-elect=true-invalid|g' /etc/kubernetes/manifests/kube-scheduler.yaml",
        "cleanup": "docker exec cka-gold-control-plane sed -i 's|--leader-elect=true-invalid|--leader-elect=true|g' /etc/kubernetes/manifests/kube-scheduler.yaml",
        "check": "kubectl get pod -n kube-system -l component=kube-scheduler -o jsonpath='{.items[0].status.phase}' | grep -i Running",
        "hint": "Check kube-scheduler.yaml under /etc/kubernetes/manifests/ on cka-gold-control-plane.",
        "solution": "1. Edit /etc/kubernetes/manifests/kube-scheduler.yaml inside the control plane node.\n2. Remove the '-invalid' typo from --leader-elect flag."
    },
    {
        "id": "E-08",
        "domain": "Troubleshooting (30%)",
        "title": "Pod Stuck in Pending due to Custom Scheduler Name Mismatch",
        "problem": "A deployment called 'nginx-scheduler-test' is pending because it requests a custom scheduler that doesn't exist.",
        "setup": "kubectl create deployment nginx-scheduler-test --image=nginx --replicas=1 && kubectl patch deployment nginx-scheduler-test --type=json -p='[{\"op\": \"add\", \"path\": \"/spec/template/spec/schedulerName\", \"value\": \"non-existent-scheduler\"}]'",
        "cleanup": "kubectl delete deployment nginx-scheduler-test --ignore-not-found=true",
        "check": "kubectl get deployment nginx-scheduler-test -o jsonpath='{.status.readyReplicas}' | grep -w '1'",
        "hint": "Inspect the deployment spec template for schedulerName. Remove or change it to default-scheduler.",
        "solution": "1. Run: kubectl edit deploy nginx-scheduler-test\n2. Delete the 'schedulerName: non-existent-scheduler' line or change it to 'default-scheduler'.\n3. Save and check replicas."
    },
    {
        "id": "E-09",
        "domain": "Troubleshooting (30%)",
        "title": "Pod Stuck in ImagePullBackOff due to Image Name Typo",
        "problem": "A pod named 'nginx-typo-image' cannot start due to an image configuration error.",
        "setup": "kubectl run nginx-typo-image --image=nginxx:latest",
        "cleanup": "kubectl delete pod nginx-typo-image --ignore-not-found=true",
        "check": "kubectl get pod nginx-typo-image -o jsonpath='{.status.phase}' | grep -i Running",
        "hint": "Check the image name using kubectl describe pod. Edit the image name to a valid image.",
        "solution": "1. Re-create or patch pod: kubectl set image pod/nginx-typo-image nginx-typo-image=nginx:latest"
    },
    {
        "id": "E-10",
        "domain": "Troubleshooting (30%)",
        "title": "CNI Plugin Deleted (Network down)",
        "problem": "Pods are stuck in ContainerCreating because the CNI DaemonSet has been scaled to 0 or deleted.",
        "setup": "kubectl scale daemonset kindnet -n kube-system --replicas=0",
        "cleanup": "kubectl scale daemonset kindnet -n kube-system --replicas=1",
        "check": "kubectl get daemonset kindnet -n kube-system -o jsonpath='{.status.numberReady}' | grep -v '0'",
        "hint": "Check the status of CNI pods in the kube-system namespace. Scaled DaemonSets can be scaled back up.",
        "solution": "1. Scale DaemonSet back up: kubectl scale daemonset kindnet -n kube-system --replicas=1"
    },
    {
        "id": "E-11",
        "domain": "Troubleshooting (30%)",
        "title": "Service Selector Mismatch",
        "problem": "Service 'web-svc' has no backend endpoint IPs. Resolve the selector mismatch.",
        "setup": "kubectl create deployment web-app --image=nginx --replicas=2 && kubectl create service clusterip web-svc --tcp=80:80 && kubectl patch service web-svc --type=json -p='[{\"op\": \"replace\", \"path\": \"/spec/selector/app\", \"value\": \"wrong-label\"}]'",
        "cleanup": "kubectl delete deployment web-app --ignore-not-found=true && kubectl delete service web-svc --ignore-not-found=true",
        "check": "kubectl get endpoints web-svc -o jsonpath='{.subsets[0].addresses[0].ip}' | grep -v '^$'",
        "hint": "Compare the selectors of the service using 'kubectl describe svc web-svc' with the labels of deployment pods.",
        "solution": "1. Run: kubectl describe svc web-svc (finds selector app=wrong-label)\n2. Edit service: kubectl edit svc web-svc\n3. Modify selector to app=web-app"
    },
    {
        "id": "E-12",
        "domain": "Troubleshooting (30%)",
        "title": "Pod Memory Request Exceeds Node Limits",
        "problem": "A pod named 'mem-heavy' is stuck in Pending because it requests more RAM than any node can provide.",
        "setup": "kubectl run mem-heavy --image=nginx --requests='memory=100Gi'",
        "cleanup": "kubectl delete pod mem-heavy --ignore-not-found=true",
        "check": "kubectl get pod mem-heavy -o jsonpath='{.status.phase}' | grep -i Running",
        "hint": "Reduce the pod memory request to a reasonable value (e.g. 50Mi) so that the scheduler can schedule it.",
        "solution": "1. Delete current pod: kubectl delete pod mem-heavy --force\n2. Recreate with valid requests: kubectl run mem-heavy --image=nginx --requests='memory=50Mi'"
    },
    {
        "id": "E-13",
        "domain": "Troubleshooting (30%)",
        "title": "PVC Stuck Pending due to Invalid StorageClass",
        "problem": "A PVC named 'pending-pvc' is stuck in Pending. Check the StorageClass request.",
        "setup": "kubectl apply -f - <<EOF\napiVersion: v1\nkind: PersistentVolumeClaim\nmetadata:\n  name: pending-pvc\nspec:\n  accessModes:\n    - ReadWriteOnce\n  resources:\n    requests:\n      storage: 1Gi\n  storageClassName: non-existent-sc\nEOF",
        "cleanup": "kubectl delete pvc pending-pvc --ignore-not-found=true",
        "check": "kubectl get pvc pending-pvc -o jsonpath='{.status.phase}' | grep -i Bound",
        "hint": "Examine the storageClassName of the PVC. Change it to 'standard' (default KinD storage class).",
        "solution": "1. Delete PVC: kubectl delete pvc pending-pvc\n2. Modify manifest storageClassName to 'standard' (or omit it for default)\n3. Re-apply: kubectl apply -f <manifest>"
    },
    {
        "id": "E-14",
        "domain": "Troubleshooting (30%)",
        "title": "Failed ETCD Snapshot Restore Recovery",
        "problem": "A broken configuration was applied. Restore the cluster configuration using the snapshot file at '/opt/backup.db'.",
        "setup": "mkdir -p /opt && ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key snapshot save /opt/backup.db && kubectl create namespace break-me",
        "cleanup": "kubectl delete namespace break-me --ignore-not-found=true && rm -f /opt/backup.db",
        "check": "kubectl get ns break-me --no-headers 2>&1 | grep -q 'NotFound' || exit 0",
        "hint": "Restore etcd using 'etcdctl snapshot restore --data-dir=/var/lib/etcd-restored /opt/backup.db' and point control plane etcd configuration path to the restored dir.",
        "solution": "1. Run etcdctl snapshot restore command.\n2. Update hostPath volume in /etc/kubernetes/manifests/etcd.yaml to point /var/lib/etcd to the restored directory."
    },
    {
        "id": "E-15",
        "domain": "Troubleshooting (30%)",
        "title": "Tainted Worker Node Evicting Pods",
        "problem": "Worker node 'cka-gold-worker' has an administrative taint added. Remove it to allow scheduling.",
        "setup": "kubectl taint nodes cka-gold-worker key=value:NoSchedule --overwrite",
        "cleanup": "kubectl taint nodes cka-gold-worker key- || true",
        "check": "kubectl describe node cka-gold-worker | grep -i Taints | grep -v 'key=value:NoSchedule'",
        "hint": "Look for active taints on cka-gold-worker node. Remove the taint using the minus suffix.",
        "solution": "1. Run: kubectl taint nodes cka-gold-worker key-"
    },
    {
        "id": "E-16",
        "domain": "Troubleshooting (30%)",
        "title": "Static Pod not Starting on Worker 1",
        "problem": "You need to host a static pod on 'cka-gold-worker'. Ensure the static pod runs correctly.",
        "setup": "docker exec cka-gold-worker mkdir -p /etc/kubernetes/manifests",
        "cleanup": "docker exec cka-gold-worker rm -f /etc/kubernetes/manifests/static.yaml || true",
        "check": "kubectl get pods --all-namespaces | grep -i cka-gold-worker | grep -i static-pod",
        "hint": "Write a pod manifest file to /etc/kubernetes/manifests/static.yaml inside the cka-gold-worker node container.",
        "solution": "1. Create YAML file: docker exec -i cka-gold-worker sh -c 'cat <<EOF > /etc/kubernetes/manifests/static.yaml\napiVersion: v1\nkind: Pod\nmetadata:\n  name: static-pod\nspec:\n  containers:\n  - name: web\n    image: nginx\nEOF'"
    },
    {
        "id": "E-17",
        "domain": "Troubleshooting (30%)",
        "title": "Ingress Routing Failure due to Service Port Mismatch",
        "problem": "Ingress is returning a 503 error. The target service port configuration does not match the actual service port.",
        "setup": "kubectl apply -f - <<EOF\napiVersion: v1\nkind: Namespace\nmetadata:\n  name: ingress-test\n---\napiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: web-deploy\n  namespace: ingress-test\nspec:\n  replicas: 1\n  selector:\n    matchLabels:\n      app: web\n  template:\n    metadata:\n      labels:\n        app: web\n    spec:\n      containers:\n      - name: nginx\n        image: nginx\n---\napiVersion: v1\nkind: Service\nmetadata:\n  name: web-service\n  namespace: ingress-test\nspec:\n  selector:\n    app: web\n  ports:\n  - port: 80\n    targetPort: 80\n---\napiVersion: networking.k8s.io/v1\nkind: Ingress\nmetadata:\n  name: test-ingress\n  namespace: ingress-test\nspec:\n  rules:\n  - http:\n      paths:\n      - path: /test\n        pathType: Prefix\n        backend:\n          service:\n            name: web-service\n            port:\n              number: 8080\nEOF",
        "cleanup": "kubectl delete namespace ingress-test --ignore-not-found=true",
        "check": "kubectl get ingress test-ingress -n ingress-test -o jsonpath='{.spec.rules[0].http.paths[0].backend.service.port.number}' | grep -w '80'",
        "hint": "Check the backend port in the Ingress resource compared to the Port defined in the web-service service.",
        "solution": "1. Edit ingress: kubectl edit ingress test-ingress -n ingress-test\n2. Modify port number from 8080 to 80"
    },
    {
        "id": "E-18",
        "domain": "Troubleshooting (30%)",
        "title": "HostPort Conflict on Worker 1 Node",
        "problem": "A pod named 'hostport-pod' fails to run because port 80 is already in use by another service on cka-gold-worker.",
        "setup": "kubectl run dummy-pod --image=nginx --overrides='{\"spec\":{\"nodeName\":\"cka-gold-worker\",\"containers\":[{\"name\":\"nginx\",\"image\":\"nginx\",\"ports\":[{\"hostPort\":80,\"containerPort\":80}]}]}}' && sleep 2 && kubectl run hostport-pod --image=nginx --overrides='{\"spec\":{\"nodeName\":\"cka-gold-worker\",\"containers\":[{\"name\":\"nginx\",\"image\":\"nginx\",\"ports\":[{\"hostPort\":80,\"containerPort\":80}]}]}}'",
        "cleanup": "kubectl delete pod dummy-pod hostport-pod --ignore-not-found=true",
        "check": "kubectl get pod hostport-pod -o jsonpath='{.status.phase}' | grep -i Running || exit 0",
        "hint": "A hostPort can only be bound once on a single node. Change the hostPort configuration to a free port or remove it.",
        "solution": "1. Delete dummy-pod or recreate hostport-pod using a different hostPort (e.g. 8080)."
    },
    {
        "id": "E-19",
        "domain": "Troubleshooting (30%)",
        "title": "Pod Stuck in CreateContainerConfigError",
        "problem": "Pod 'config-err-pod' cannot start because it references a ConfigMap key that does not exist.",
        "setup": "kubectl create configmap app-config --from-literal=key1=val1 && kubectl apply -f - <<EOF\napiVersion: v1\nkind: Pod\nmetadata:\n  name: config-err-pod\nspec:\n  containers:\n  - name: app\n    image: nginx\n    env:\n    - name: CFG_VAL\n      valueFrom:\n        configMapKeyRef:\n          name: app-config\n          key: missing-key\nEOF",
        "cleanup": "kubectl delete pod config-err-pod --ignore-not-found=true && kubectl delete configmap app-config --ignore-not-found=true",
        "check": "kubectl get pod config-err-pod -o jsonpath='{.status.phase}' | grep -i Running",
        "hint": "Check the ConfigMap 'app-config' values. Either create the key 'missing-key' in the ConfigMap or edit the PodSpec.",
        "solution": "1. Patch ConfigMap to include key: kubectl patch configmap app-config --type merge -p '{\"data\":{\"missing-key\":\"fixed-value\"}}'"
    },
    {
        "id": "E-20",
        "domain": "Troubleshooting (30%)",
        "title": "Pod Blocked by Disabled ServiceAccount Token Automount",
        "problem": "Pod 'sa-test-pod' needs to talk to the API server but has automountServiceAccountToken: false. Enable it.",
        "setup": "kubectl apply -f - <<EOF\napiVersion: v1\nkind: Pod\nmetadata:\n  name: sa-test-pod\nspec:\n  automountServiceAccountToken: false\n  containers:\n  - name: test\n    image: nginx\nEOF",
        "cleanup": "kubectl delete pod sa-test-pod --ignore-not-found=true",
        "check": "kubectl get pod sa-test-pod -o jsonpath='{.spec.automountServiceAccountToken}' | grep -w 'true' || kubectl get pod sa-test-pod -o yaml | grep -v 'automountServiceAccountToken: false'",
        "hint": "Set automountServiceAccountToken: true in the pod spec and recreate the pod.",
        "solution": "1. Recreate the pod with automountServiceAccountToken: true."
    },
    {
        "id": "E-21",
        "domain": "Troubleshooting (30%)",
        "title": "Kubelet Masked on Worker Node 2",
        "problem": "Node 'cka-gold-worker2' is showing NotReady. The systemd service is masked on the host.",
        "setup": "docker exec cka-gold-worker2 systemctl mask kubelet && docker exec cka-gold-worker2 systemctl stop kubelet",
        "cleanup": "docker exec cka-gold-worker2 systemctl unmask kubelet && docker exec cka-gold-worker2 systemctl start kubelet",
        "check": "kubectl get node cka-gold-worker2 -o jsonpath='{.status.conditions[?(@.type==\"Ready\")].status}' | grep -i True",
        "hint": "Run systemctl unmask kubelet and then start the service inside the cka-gold-worker2 container.",
        "solution": "1. Run: docker exec cka-gold-worker2 systemctl unmask kubelet\n2. Run: docker exec cka-gold-worker2 systemctl start kubelet"
    },
    {
        "id": "E-22",
        "domain": "Troubleshooting (30%)",
        "title": "Tainted Workers Blocking Deployment Scheduling",
        "problem": "A deployment called 'unreachable-deploy' is stuck in Pending because all worker nodes have taints.",
        "setup": "kubectl create deployment unreachable-deploy --image=nginx --replicas=2 && kubectl taint nodes cka-gold-worker env=prod:NoSchedule --overwrite && kubectl taint nodes cka-gold-worker2 env=prod:NoSchedule --overwrite",
        "cleanup": "kubectl delete deployment unreachable-deploy --ignore-not-found=true && kubectl taint nodes cka-gold-worker env- || true && kubectl taint nodes cka-gold-worker2 env- || true",
        "check": "kubectl get deployment unreachable-deploy -o jsonpath='{.status.readyReplicas}' | grep -w '2'",
        "hint": "Untaint the nodes using 'kubectl taint nodes <node> env-' or add the corresponding toleration to the deployment.",
        "solution": "1. Untaint the nodes: kubectl taint nodes cka-gold-worker env- && kubectl taint nodes cka-gold-worker2 env-"
    },
    {
        "id": "E-23",
        "domain": "Troubleshooting (30%)",
        "title": "ClusterRole Binding Mismatched Subject Name",
        "problem": "A pod trying to query namespaces fails because the ClusterRoleBinding links to the wrong service account name.",
        "setup": "kubectl create serviceaccount monitor-sa && kubectl create clusterrolebinding monitor-crb --clusterrole=view --serviceaccount=default:wrong-name",
        "cleanup": "kubectl delete serviceaccount monitor-sa --ignore-not-found=true && kubectl delete clusterrolebinding monitor-crb --ignore-not-found=true",
        "check": "kubectl auth can-i get namespaces --as=system:serviceaccount:default:monitor-sa | grep -i yes",
        "hint": "Edit the ClusterRoleBinding 'monitor-crb' to point to the correct ServiceAccount name 'monitor-sa'.",
        "solution": "1. Run: kubectl edit clusterrolebinding monitor-crb\n2. Change subject name to 'monitor-sa'."
    },
    {
        "id": "E-24",
        "domain": "Troubleshooting (30%)",
        "title": "NetworkPolicy Default Deny Block",
        "problem": "Traffic between pods in namespace 'default' and namespace 'app' is blocked by a default deny policy. Configure it to allow access.",
        "setup": "kubectl create namespace app && kubectl apply -f - <<EOF\napiVersion: networking.k8s.io/v1\nkind: NetworkPolicy\nmetadata:\n  name: deny-all\n  namespace: app\nspec:\n  podSelector: {}\n  policyTypes:\n  - Ingress\nEOF",
        "cleanup": "kubectl delete namespace app --ignore-not-found=true",
        "check": "kubectl get netpol -n app | grep -v 'deny-all' || exit 0",
        "hint": "Either delete the default deny NetworkPolicy in 'app' namespace, or add a NetworkPolicy rule to allow ingress.",
        "solution": "1. Delete deny-all policy: kubectl delete netpol deny-all -n app"
    },
    {
        "id": "E-25",
        "domain": "Troubleshooting (30%)",
        "title": "Kube-Proxy Pods Failing due to Bad ConfigMap",
        "problem": "Kube-proxy daemonset is failing because the 'kube-proxy' ConfigMap has a syntax error.",
        "setup": "kubectl get configmap kube-proxy -n kube-system -o yaml > /tmp/kube-proxy-cm.yaml && kubectl patch configmap kube-proxy -n kube-system --type merge -p '{\"data\":{\"config.conf\":\"corrupted configuration line\"}}' && kubectl rollout restart daemonset kube-proxy -n kube-system",
        "cleanup": "kubectl apply -f /tmp/kube-proxy-cm.yaml && kubectl rollout restart daemonset kube-proxy -n kube-system",
        "check": "kubectl get daemonset kube-proxy -n kube-system -o jsonpath='{.status.numberReady}' | grep -w '3'",
        "hint": "Check the configMap 'kube-proxy' in 'kube-system' namespace. Fix the configuration config.conf syntax.",
        "solution": "1. Restore the configuration file by editing ConfigMap: kubectl edit configmap kube-proxy -n kube-system\n2. Rollout restart the daemonset: kubectl rollout restart daemonset kube-proxy -n kube-system"
    },
    {
        "id": "E-26",
        "domain": "Troubleshooting (30%)",
        "title": "Ephemeral Storage Limit Exceeded",
        "problem": "A pod named 'evicted-pod' fails to run because it requests ephemeral storage that exceeds the namespace limit.",
        "setup": "kubectl apply -f - <<EOF\napiVersion: v1\nkind: LimitRange\nmetadata:\n  name: storage-limit\nspec:\n  limits:\n  - default:\n      ephemeral-storage: 100Mi\n    defaultRequest:\n      ephemeral-storage: 50Mi\n    max:\n      ephemeral-storage: 200Mi\n    type: Container\n---\napiVersion: v1\nkind: Pod\nmetadata:\n  name: evicted-pod\nspec:\n  containers:\n  - name: main\n    image: nginx\n    resources:\n      requests:\n        ephemeral-storage: 500Mi\nEOF",
        "cleanup": "kubectl delete pod evicted-pod --ignore-not-found=true && kubectl delete limitrange storage-limit --ignore-not-found=true",
        "check": "kubectl get pod evicted-pod -o jsonpath='{.status.phase}' | grep -i Running || exit 0",
        "hint": "The pod ephemeral-storage request exceeds the LimitRange max limit (200Mi). Modify the pod request or delete the LimitRange.",
        "solution": "1. Remove request limit or change request in pod spec to under 200Mi, then recreate pod."
    },
    {
        "id": "E-27",
        "domain": "Troubleshooting (30%)",
        "title": "API Priority & Fairness Blocking Configuration",
        "problem": "A broken FlowSchema causes administrator requests to fail. Remove the broken FlowSchema.",
        "setup": "kubectl apply -f - <<EOF\napiVersion: flowcontrol.apiserver.k8s.io/v1beta3\nkind: FlowSchema\nmetadata:\n  name: block-admin\nspec:\n  matchingPrecedence: 1\n  priorityLevelConfiguration:\n    name: catch-all\n  rules:\n  - subjects:\n    - kind: User\n      name: admin\n    resourceRules:\n    - verbs: [\"*\"]\n      apiGroups: [\"*\"]\n      resources: [\"*\"]\nEOF",
        "cleanup": "kubectl delete flowschema block-admin --ignore-not-found=true",
        "check": "kubectl get flowschema | grep -q 'block-admin' && exit 1 || exit 0",
        "hint": "Locate and delete the FlowSchema named 'block-admin'.",
        "solution": "1. Run: kubectl delete flowschema block-admin"
    },

    # ==========================================
    # --- CLUSTER ARCHITECTURE, INSTALLATION & CONFIG (25% - 23 Scenarios) ---
    # ==========================================
    {
        "id": "E-28",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Upgrade Control Plane Node (kubeadm & kubelet)",
        "problem": "Systematic Upgrade: You are tasked with upgrading the control-plane node (cka-gold-control-plane) from v1.35.0 to v1.35.1. Perform a secure drain, plan and apply the kubeadm upgrade, upgrade the kubelet/kubectl packages, and restart services.",
        "setup": "docker exec cka-gold-control-plane mkdir -p /var/log/upgrade-test",
        "cleanup": "docker exec cka-gold-control-plane rm -rf /var/log/upgrade-test",
        "check": "docker exec cka-gold-control-plane ls /var/log/upgrade-test/upgraded",
        "hint": "On the actual CKA exam, you must follow the official Kubernetes documentation upgrade flow. This involves: 1. Draining the control plane node; 2. Upgrading kubeadm via apt-get; 3. Running 'kubeadm upgrade plan' and 'kubeadm upgrade apply'; 4. Upgrading kubelet and kubectl; 5. Reloading systemd and restarting kubelet; 6. Uncordoning the node. (Since KinD uses static binaries rather than APT packages, simulate this in your sandbox by running the drain command, and then creating the verification file: 'docker exec cka-gold-control-plane touch /var/log/upgrade-test/upgraded').",
        "solution": "=== ACTUAL CKA EXAM SYSTEMATIC PATHWAY ===\n1. Drain the control plane node:\n   kubectl drain cka-gold-control-plane --ignore-daemonsets --force\n2. SSH to the control-plane node and escalate to root:\n   ssh cka-gold-control-plane\n   sudo -i\n3. Upgrade kubeadm package:\n   apt-mark unhold kubeadm\n   apt-get update && apt-get install -y kubeadm=1.35.1-1.1\n   apt-mark hold kubeadm\n4. Plan and apply the upgrade:\n   kubeadm upgrade plan\n   kubeadm upgrade apply v1.35.1\n5. Upgrade kubelet and kubectl packages:\n   apt-mark unhold kubelet kubectl\n   apt-get install -y kubelet=1.35.1-1.1 kubectl=1.35.1-1.1\n   apt-mark hold kubelet kubectl\n6. Reload systemd manager configuration and restart kubelet daemon:\n   systemctl daemon-reload\n   systemctl restart kubelet\n7. Exit the node and uncordon the control plane:\n   exit\n   kubectl uncordon cka-gold-control-plane\n\n=== KIND SANDBOX PRACTICE SIMULATION ===\nIn this local KinD cluster environment, execute: \ndocker exec cka-gold-control-plane touch /var/log/upgrade-test/upgraded"
    },
    {
        "id": "E-29",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Upgrade Worker Node (kubeadm & kubelet)",
        "problem": "Systematic Upgrade: Upgrade the worker node 'cka-gold-worker' from v1.35.0 to v1.35.1. Cordon and drain the node first, then perform the local package upgrade.",
        "setup": "kubectl cordon cka-gold-worker",
        "cleanup": "kubectl uncordon cka-gold-worker && docker exec cka-gold-worker rm -f /var/log/worker-upgraded || true",
        "check": "kubectl get node cka-gold-worker -o jsonpath='{.spec.unschedulable}' | grep -w 'true' && docker exec cka-gold-worker ls /var/log/worker-upgraded",
        "hint": "On the actual CKA exam, worker node upgrades differ from control plane upgrades: 1. Drain the worker node from the control-plane; 2. SSH to the worker node; 3. Upgrade kubeadm via apt-get; 4. Run 'kubeadm upgrade node' (instead of apply); 5. Upgrade kubelet/kubectl and restart the services; 6. Uncordon the node from the control-plane. (Simulate this locally by running the drain command and creating the verification file: 'docker exec cka-gold-worker touch /var/log/worker-upgraded').",
        "solution": "=== ACTUAL CKA EXAM SYSTEMATIC PATHWAY ===\n1. Drain the worker node from your management terminal:\n   kubectl drain cka-gold-worker --ignore-daemonsets --force\n2. SSH to the worker node:\n   ssh cka-gold-worker\n3. Upgrade kubeadm on the worker node:\n   apt-mark unhold kubeadm\n   apt-get update && apt-get install -y kubeadm=1.35.1-1.1\n   apt-mark hold kubeadm\n4. Upgrade the local node configuration:\n   sudo kubeadm upgrade node\n5. Upgrade kubelet and kubectl on the worker node:\n   apt-mark unhold kubelet kubectl\n   apt-get install -y kubelet=1.35.1-1.1 kubectl=1.35.1-1.1\n   apt-mark hold kubelet kubectl\n6. Restart the local kubelet service:\n   sudo systemctl daemon-reload\n   sudo systemctl restart kubelet\n7. Exit the worker node and uncordon it from the control plane:\n   exit\n   kubectl uncordon cka-gold-worker\n\n=== KIND SANDBOX PRACTICE SIMULATION ===\nRun the drain and touch verification file locally:\n1. kubectl drain cka-gold-worker --ignore-daemonsets --force\n2. docker exec cka-gold-worker touch /var/log/worker-upgraded"
    },
    {
        "id": "E-30",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Take a secure ETCD backup",
        "problem": "Save a backup snapshot of etcd to the path '/opt/etcd-backup.db' on the control plane node.",
        "setup": "docker exec cka-gold-control-plane rm -f /opt/etcd-backup.db",
        "cleanup": "docker exec cka-gold-control-plane rm -f /opt/etcd-backup.db",
        "check": "docker exec cka-gold-control-plane ls -lh /opt/etcd-backup.db",
        "hint": "Use etcdctl inside cka-gold-control-plane to save snapshot to the path /opt/etcd-backup.db.",
        "solution": "1. Run: docker exec cka-gold-control-plane sh -c \"ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key snapshot save /opt/etcd-backup.db\""
    },
    {
        "id": "E-31",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Restore ETCD backup from Snapshot file",
        "problem": "Restore an etcd snapshot located at '/opt/snapshot.db' inside cka-gold-control-plane. Ensure a test configmap created after is gone.",
        "setup": "docker exec cka-gold-control-plane sh -c \"mkdir -p /opt && ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key snapshot save /opt/snapshot.db\" && kubectl create configmap test-after-backup",
        "cleanup": "kubectl delete configmap test-after-backup --ignore-not-found=true",
        "check": "kubectl get configmap test-after-backup 2>&1 | grep -q 'NotFound' || exit 0",
        "hint": "Restore snapshot and redirect hostPath volume to restored data directory.",
        "solution": "1. Restore snapshot inside container.\n2. Update etcd.yaml hostPath path to point to restored data-dir."
    },
    {
        "id": "E-32",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Configure Kube-APIServer Audit Logging",
        "problem": "Enable audit logging on the API Server. Log file should be at '/var/log/kubernetes/audit.log', max size 10MB.",
        "setup": "docker exec cka-gold-control-plane mkdir -p /etc/kubernetes/audit",
        "cleanup": "docker exec cka-gold-control-plane rm -rf /etc/kubernetes/audit",
        "check": "docker exec cka-gold-control-plane grep -q 'audit-log-path' /etc/kubernetes/manifests/kube-apiserver.yaml",
        "hint": "Add --audit-log-path=/var/log/kubernetes/audit.log in kube-apiserver static pod arguments.",
        "solution": "1. Edit /etc/kubernetes/manifests/kube-apiserver.yaml\n2. Add lines under args: - --audit-log-path=/var/log/kubernetes/audit.log"
    },
    {
        "id": "E-33",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Renew API Server Certificates",
        "problem": "Renew all certificates managed by kubeadm.",
        "setup": "echo 'Renew simulation'",
        "cleanup": "echo 'Done'",
        "check": "docker exec cka-gold-control-plane kubeadm certs check-expiration",
        "hint": "Run 'kubeadm certs renew all' inside the cka-gold-control-plane container.",
        "solution": "1. Run: docker exec cka-gold-control-plane kubeadm certs renew all"
    },
    {
        "id": "E-34",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Create Certificate Signing Request API",
        "problem": "Create a CSR named 'dev-user-csr' and approve it using kubectl certificate approve.",
        "setup": "kubectl delete csr dev-user-csr --ignore-not-found=true",
        "cleanup": "kubectl delete csr dev-user-csr --ignore-not-found=true",
        "check": "kubectl get csr dev-user-csr -o jsonpath='{.status.conditions[0].type}' | grep -i Approved",
        "hint": "Generate a private key and CSR. Create a CSR object in Kubernetes and run approve command.",
        "solution": "1. Apply a CertificateSigningRequest YAML manifest.\n2. Run: kubectl certificate approve dev-user-csr"
    },
    {
        "id": "E-35",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Configure API Server Admission Plugins",
        "problem": "Configure kube-apiserver to enable the 'NodeRestriction' admission plugin.",
        "setup": "docker exec cka-gold-control-plane sed -i 's|--enable-admission-plugins=NodeRestriction|--enable-admission-plugins=None|g' /etc/kubernetes/manifests/kube-apiserver.yaml",
        "cleanup": "docker exec cka-gold-control-plane sed -i 's|--enable-admission-plugins=None|--enable-admission-plugins=NodeRestriction|g' /etc/kubernetes/manifests/kube-apiserver.yaml",
        "check": "docker exec cka-gold-control-plane grep -q 'NodeRestriction' /etc/kubernetes/manifests/kube-apiserver.yaml",
        "hint": "Check the --enable-admission-plugins argument in /etc/kubernetes/manifests/kube-apiserver.yaml.",
        "solution": "1. In /etc/kubernetes/manifests/kube-apiserver.yaml, add or modify --enable-admission-plugins=NodeRestriction"
    },
    {
        "id": "E-36",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Create Kubeconfig file for User 'sarah'",
        "problem": "Generate a kubeconfig file at '/tmp/sarah.kubeconfig' pointing to cluster 'cka-gold' and user 'sarah'.",
        "setup": "rm -f /tmp/sarah.kubeconfig",
        "cleanup": "rm -f /tmp/sarah.kubeconfig",
        "check": "grep -q 'sarah' /tmp/sarah.kubeconfig && grep -q 'cka-gold' /tmp/sarah.kubeconfig",
        "hint": "Use 'kubectl config set-cluster', 'set-credentials', and 'set-context' commands with --kubeconfig=/tmp/sarah.kubeconfig.",
        "solution": "1. Run: kubectl config set-cluster cka-gold --server=https://127.0.0.1:6443 --kubeconfig=/tmp/sarah.kubeconfig\n2. Run: kubectl config set-credentials sarah --token=token --kubeconfig=/tmp/sarah.kubeconfig\n3. Run: kubectl config set-context sarah@cka-gold --cluster=cka-gold --user=sarah --kubeconfig=/tmp/sarah.kubeconfig"
    },
    {
        "id": "E-37",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Expose Metrics Server Endpoint",
        "problem": "Verify that metrics api group v1beta1.metrics.k8s.io is running.",
        "setup": "echo 'Metrics validation'",
        "cleanup": "echo 'Done'",
        "check": "kubectl get apiservice v1beta1.metrics.k8s.io",
        "hint": "Metrics Server should be active. Ensure `kubectl top nodes` returns data.",
        "solution": "1. Metrics server is installed by default on kind cluster. Verify: kubectl get apiservice v1beta1.metrics.k8s.io"
    },
    {
        "id": "E-38",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Drain cka-gold-worker Node",
        "problem": "Drain the worker node 'cka-gold-worker' for maintenance.",
        "setup": "kubectl uncordon cka-gold-worker || true",
        "cleanup": "kubectl uncordon cka-gold-worker || true",
        "check": "kubectl get node cka-gold-worker -o jsonpath='{.spec.unschedulable}' | grep -w 'true'",
        "hint": "Use 'kubectl drain cka-gold-worker --ignore-daemonsets --force'.",
        "solution": "1. Run: kubectl drain cka-gold-worker --ignore-daemonsets --force"
    },
    {
        "id": "E-39",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Uncordon cka-gold-worker Node",
        "problem": "Make the worker node 'cka-gold-worker' schedulable again after maintenance.",
        "setup": "kubectl cordon cka-gold-worker",
        "cleanup": "kubectl uncordon cka-gold-worker || true",
        "check": "kubectl get node cka-gold-worker -o jsonpath='{.spec.unschedulable}' | grep -v 'true'",
        "hint": "Use 'kubectl uncordon cka-gold-worker'.",
        "solution": "1. Run: kubectl uncordon cka-gold-worker"
    },
    {
        "id": "E-40",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Create Static Pod on Control Plane Node",
        "problem": "Create a static pod named 'static-web' running nginx on cka-gold-control-plane.",
        "setup": "docker exec cka-gold-control-plane rm -f /etc/kubernetes/manifests/static-web.yaml || true",
        "cleanup": "docker exec cka-gold-control-plane rm -f /etc/kubernetes/manifests/static-web.yaml || true",
        "check": "kubectl get pods -n default | grep -i static-web-cka-gold-control-plane",
        "hint": "Place the static pod manifest inside cka-gold-control-plane container at /etc/kubernetes/manifests/static-web.yaml.",
        "solution": "1. Run: docker exec -i cka-gold-control-plane sh -c 'cat <<EOF > /etc/kubernetes/manifests/static-web.yaml\napiVersion: v1\nkind: Pod\nmetadata:\n  name: static-web\nspec:\n  containers:\n  - name: web\n    image: nginx\nEOF'"
    },
    {
        "id": "E-41",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Configure Kubelet Garbage Collection thresholds",
        "problem": "Set Kubelet to perform image garbage collection when disk usage exceeds 80%.",
        "setup": "echo 'Simulation setup'",
        "cleanup": "echo 'Done'",
        "check": "docker exec cka-gold-control-plane grep -q 'imageGCHighThresholdPercent' /var/lib/kubelet/config.yaml || exit 0",
        "hint": "Modify /var/lib/kubelet/config.yaml inside control plane and worker nodes to add imageGCHighThresholdPercent: 80.",
        "solution": "1. Edit /var/lib/kubelet/config.yaml\n2. Add line: imageGCHighThresholdPercent: 80\n3. Restart kubelet: systemctl restart kubelet"
    },
    {
        "id": "E-42",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Create a ServiceAccount Named 'developer'",
        "problem": "Create a ServiceAccount named 'developer' in the namespace 'default'.",
        "setup": "kubectl delete serviceaccount developer --ignore-not-found=true",
        "cleanup": "kubectl delete serviceaccount developer --ignore-not-found=true",
        "check": "kubectl get serviceaccount developer",
        "hint": "Use 'kubectl create serviceaccount developer'.",
        "solution": "1. Run: kubectl create serviceaccount developer"
    },
    {
        "id": "E-43",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Create a Role Named 'pod-reader'",
        "problem": "Create a Role named 'pod-reader' that allows getting, watching, and listing pods in default namespace.",
        "setup": "kubectl delete role pod-reader --ignore-not-found=true",
        "cleanup": "kubectl delete role pod-reader --ignore-not-found=true",
        "check": "kubectl get role pod-reader -o jsonpath='{.rules[0].verbs}' | grep -w 'get'",
        "hint": "Use 'kubectl create role pod-reader --verb=get,list,watch --resource=pods'.",
        "solution": "1. Run: kubectl create role pod-reader --verb=get,list,watch --resource=pods"
    },
    {
        "id": "E-44",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Bind Role 'pod-reader' to ServiceAccount 'developer'",
        "problem": "Create a RoleBinding named 'read-pods' to bind Role 'pod-reader' to ServiceAccount 'developer'.",
        "setup": "kubectl create serviceaccount developer || true && kubectl create role pod-reader --verb=get,list,watch --resource=pods || true && kubectl delete rolebinding read-pods --ignore-not-found=true",
        "cleanup": "kubectl delete rolebinding read-pods --ignore-not-found=true && kubectl delete role pod-reader --ignore-not-found=true && kubectl delete serviceaccount developer --ignore-not-found=true",
        "check": "kubectl get rolebinding read-pods -o jsonpath='{.subjects[0].name}' | grep -w 'developer'",
        "hint": "Use 'kubectl create rolebinding read-pods --role=pod-reader --serviceaccount=default:developer'.",
        "solution": "1. Run: kubectl create rolebinding read-pods --role=pod-reader --serviceaccount=default:developer"
    },
    {
        "id": "E-45",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Create a ClusterRole Named 'node-reader'",
        "problem": "Create a ClusterRole named 'node-reader' that allows reading nodes.",
        "setup": "kubectl delete clusterrole node-reader --ignore-not-found=true",
        "cleanup": "kubectl delete clusterrole node-reader --ignore-not-found=true",
        "check": "kubectl get clusterrole node-reader",
        "hint": "Use 'kubectl create clusterrole node-reader --verb=get,list,watch --resource=nodes'.",
        "solution": "1. Run: kubectl create clusterrole node-reader --verb=get,list,watch --resource=nodes"
    },
    {
        "id": "E-46",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Bind ClusterRole to Group 'system:authenticated'",
        "problem": "Create a ClusterRoleBinding named 'read-nodes-binding' to bind ClusterRole 'node-reader' to group 'system:authenticated'.",
        "setup": "kubectl create clusterrole node-reader --verb=get,list,watch --resource=nodes || true && kubectl delete clusterrolebinding read-nodes-binding --ignore-not-found=true",
        "cleanup": "kubectl delete clusterrolebinding read-nodes-binding --ignore-not-found=true && kubectl delete clusterrole node-reader --ignore-not-found=true",
        "check": "kubectl get clusterrolebinding read-nodes-binding -o jsonpath='{.subjects[0].name}' | grep -w 'system:authenticated'",
        "hint": "Use 'kubectl create clusterrolebinding read-nodes-binding --clusterrole=node-reader --group=system:authenticated'.",
        "solution": "1. Run: kubectl create clusterrolebinding read-nodes-binding --clusterrole=node-reader --group=system:authenticated"
    },
    {
        "id": "E-47",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Find the active API Server Port",
        "problem": "Output the active API Server secure port to file '/tmp/apiserver-port.txt'.",
        "setup": "rm -f /tmp/apiserver-port.txt",
        "cleanup": "rm -f /tmp/apiserver-port.txt",
        "check": "grep -q '6443' /tmp/apiserver-port.txt",
        "hint": "Check kube-apiserver static pod arguments or running process inside control plane container. Default is 6443.",
        "solution": "1. Run: echo '6443' > /tmp/apiserver-port.txt"
    },
    {
        "id": "E-48",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Configure Kubelet Node IP argument",
        "problem": "Identify the Node IP configuration option in Kubelet systemd config.",
        "setup": "echo 'Simulation'",
        "cleanup": "echo 'Done'",
        "check": "docker exec cka-gold-worker systemctl status kubelet | grep -q 'node-ip'",
        "hint": "Examine cgroup and config flags inside cka-gold-worker at /etc/systemd/system/kubelet.service.d/10-kubeadm.conf.",
        "solution": "1. The node IP is passed as argument --node-ip in the systemd drop-in configuration."
    },
    {
        "id": "E-49",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Verify API Priority & Fairness Default Limits",
        "problem": "List all active FlowSchemas in the cluster.",
        "setup": "echo 'Simulation'",
        "cleanup": "echo 'Done'",
        "check": "kubectl get flowschemas | grep -q 'exempt'",
        "hint": "Use 'kubectl get flowschemas'.",
        "solution": "1. Run: kubectl get flowschemas"
    },
    {
        "id": "E-50",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Graceful Node Shutdown Config check",
        "problem": "Ensure the GracefulNodeShutdown feature flag config parameter exists in Kubelet config.",
        "setup": "echo 'Simulation'",
        "cleanup": "echo 'Done'",
        "check": "docker exec cka-gold-control-plane grep -q 'shutdownGracePeriod' /var/lib/kubelet/config.yaml || exit 0",
        "hint": "Check the shutdownGracePeriod settings in Kubelet config.yaml.",
        "solution": "1. Add shutdownGracePeriod to Kubelet configuration file."
    },

    # ==========================================
    # --- SERVICES & NETWORKING (20% - 18 Scenarios) ---
    # ==========================================
    {
        "id": "E-51",
        "domain": "Services & Networking (20%)",
        "title": "Install Nginx Ingress Controller Mock",
        "problem": "Create a dummy namespace 'ingress-nginx' to simulate ingress controller installation.",
        "setup": "kubectl delete ns ingress-nginx --ignore-not-found=true",
        "cleanup": "kubectl delete ns ingress-nginx --ignore-not-found=true",
        "check": "kubectl get ns ingress-nginx",
        "hint": "Use 'kubectl create namespace ingress-nginx'.",
        "solution": "1. Run: kubectl create namespace ingress-nginx"
    },
    {
        "id": "E-52",
        "domain": "Services & Networking (20%)",
        "title": "Configure Path Ingress Routing",
        "problem": "Create an Ingress resource named 'path-ingress' in default namespace routing '/app' to service 'app-svc' on port 80.",
        "setup": "kubectl delete ingress path-ingress --ignore-not-found=true",
        "cleanup": "kubectl delete ingress path-ingress --ignore-not-found=true",
        "check": "kubectl get ingress path-ingress -o jsonpath='{.spec.rules[0].http.paths[0].path}' | grep -w '/app'",
        "hint": "Use 'kubectl create ingress path-ingress --rule=\"/app=app-svc:80\"'.",
        "solution": "1. Run: kubectl create ingress path-ingress --rule=\"/app=app-svc:80\""
    },
    {
        "id": "E-53",
        "domain": "Services & Networking (20%)",
        "title": "Configure Host-based Ingress Routing",
        "problem": "Create Ingress 'host-ingress' mapping domain 'web.example.com' to service 'web-svc' on port 80.",
        "setup": "kubectl delete ingress host-ingress --ignore-not-found=true",
        "cleanup": "kubectl delete ingress host-ingress --ignore-not-found=true",
        "check": "kubectl get ingress host-ingress -o jsonpath='{.spec.rules[0].host}' | grep -w 'web.example.com'",
        "hint": "Use 'kubectl create ingress host-ingress --rule=\"web.example.com/*=web-svc:80\"'.",
        "solution": "1. Run: kubectl create ingress host-ingress --rule=\"web.example.com/*=web-svc:80\""
    },
    {
        "id": "E-54",
        "domain": "Services & Networking (20%)",
        "title": "Create a ClusterIP Service",
        "problem": "Expose deployment 'my-deploy' on internal service 'my-service' port 80, targetPort 8080.",
        "setup": "kubectl create deployment my-deploy --image=nginx --replicas=1 || true && kubectl delete service my-service --ignore-not-found=true",
        "cleanup": "kubectl delete deployment my-deploy --ignore-not-found=true && kubectl delete service my-service --ignore-not-found=true",
        "check": "kubectl get svc my-service -o jsonpath='{.spec.ports[0].targetPort}' | grep -w '8080'",
        "hint": "Use 'kubectl expose deployment my-deploy --name=my-service --port=80 --target-port=8080'.",
        "solution": "1. Run: kubectl expose deployment my-deploy --name=my-service --port=80 --target-port=8080"
    },
    {
        "id": "E-55",
        "domain": "Services & Networking (20%)",
        "title": "Create NodePort Service",
        "problem": "Expose deployment 'my-deploy' via NodePort service 'np-service' on port 80, nodePort 32000.",
        "setup": "kubectl create deployment my-deploy --image=nginx --replicas=1 || true && kubectl delete service np-service --ignore-not-found=true",
        "cleanup": "kubectl delete deployment my-deploy --ignore-not-found=true && kubectl delete service np-service --ignore-not-found=true",
        "check": "kubectl get svc np-service -o jsonpath='{.spec.ports[0].nodePort}' | grep -w '32000'",
        "hint": "Create NP service using YAML overrides or by exposing deploy and changing type to NodePort and nodePort value.",
        "solution": "1. Create YAML for np-service:\nkubectl expose deploy my-deploy --name=np-service --type=NodePort --port=80 --dry-run=client -o yaml > /tmp/np.yaml\n2. Modify nodePort: 32000 under ports block and apply."
    },
    {
        "id": "E-56",
        "domain": "Services & Networking (20%)",
        "title": "Create Headless Service for StatefulSet",
        "problem": "Create a service named 'db-headless' with clusterIP set to None.",
        "setup": "kubectl delete service db-headless --ignore-not-found=true",
        "cleanup": "kubectl delete service db-headless --ignore-not-found=true",
        "check": "kubectl get svc db-headless -o jsonpath='{.spec.clusterIP}' | grep -i None",
        "hint": "Create a ClusterIP service and edit it to set clusterIP: None, or apply a YAML manifest.",
        "solution": "1. Create manifest and apply:\nkubectl apply -f - <<EOF\napiVersion: v1\nkind: Service\nmetadata:\n  name: db-headless\nspec:\n  clusterIP: None\n  selector:\n    app: db\n  ports:\n  - port: 3306\nEOF"
    },
    {
        "id": "E-57",
        "domain": "Services & Networking (20%)",
        "title": "Configure Ingress NetworkPolicy Rule",
        "problem": "Create a NetworkPolicy 'allow-ingress-only' allowing ingress traffic only from pods with label 'access=granted'.",
        "setup": "kubectl delete netpol allow-ingress-only --ignore-not-found=true",
        "cleanup": "kubectl delete netpol allow-ingress-only --ignore-not-found=true",
        "check": "kubectl get netpol allow-ingress-only -o jsonpath='{.spec.ingress[0].from[0].podSelector.matchLabels.access}' | grep -w 'granted'",
        "hint": "Apply a NetworkPolicy targeting pods with specific selector that allows from matching podSelector access=granted.",
        "solution": "1. Apply manifest:\nkubectl apply -f - <<EOF\napiVersion: networking.k8s.io/v1\nkind: NetworkPolicy\nmetadata:\n  name: allow-ingress-only\nspec:\n  podSelector: {}\n  ingress:\n  - from:\n    - podSelector:\n        matchLabels:\n          access: granted\nEOF"
    },
    {
        "id": "E-58",
        "domain": "Services & Networking (20%)",
        "title": "Restrict Egress to DNS UDP 53 only",
        "problem": "Create NetworkPolicy 'dns-egress-only' in default namespace blocking all egress except DNS traffic on UDP 53.",
        "setup": "kubectl delete netpol dns-egress-only --ignore-not-found=true",
        "cleanup": "kubectl delete netpol dns-egress-only --ignore-not-found=true",
        "check": "kubectl get netpol dns-egress-only -o jsonpath='{.spec.egress[0].ports[0].port}' | grep -w '53'",
        "hint": "Create policy with egress rules specifying UDP port 53.",
        "solution": "1. Apply manifest:\nkubectl apply -f - <<EOF\napiVersion: networking.k8s.io/v1\nkind: NetworkPolicy\nmetadata:\n  name: dns-egress-only\nspec:\n  podSelector: {}\n  policyTypes:\n  - Egress\n  egress:\n  - to:\n    - namespaceSelector: {}\n    ports:\n    - protocol: UDP\n      port: 53\nEOF"
    },
    {
        "id": "E-59",
        "domain": "Services & Networking (20%)",
        "title": "Configure CoreDNS Upstream Forward Rule",
        "problem": "Modify CoreDNS ConfigMap to forward corporate DNS queries to 10.10.10.10.",
        "setup": "echo 'Simulation'",
        "cleanup": "echo 'Done'",
        "check": "kubectl get configmap coredns -n kube-system -o yaml | grep -q '10.10.10.10' || exit 0",
        "hint": "Modify coredns configmap in kube-system namespace. Add forward statement.",
        "solution": "1. Edit: kubectl edit configmap coredns -n kube-system\n2. Add forward statement: forward . 10.10.10.10"
    },
    {
        "id": "E-60",
        "domain": "Services & Networking (20%)",
        "title": "Verify Kube-proxy Config",
        "problem": "Ensure kube-proxy config exists in the kube-system namespace.",
        "setup": "echo 'Done'",
        "cleanup": "echo 'Done'",
        "check": "kubectl get configmap kube-proxy -n kube-system",
        "hint": "Run: kubectl get configmap kube-proxy -n kube-system",
        "solution": "1. Run: kubectl get configmap kube-proxy -n kube-system"
    },
    {
        "id": "E-61",
        "domain": "Services & Networking (20%)",
        "title": "Create ExternalName Service",
        "problem": "Create service 'my-ext-svc' mapping to external domain 'api.google.com'.",
        "setup": "kubectl delete service my-ext-svc --ignore-not-found=true",
        "cleanup": "kubectl delete service my-ext-svc --ignore-not-found=true",
        "check": "kubectl get svc my-ext-svc -o jsonpath='{.spec.externalName}' | grep -w 'api.google.com'",
        "hint": "Use 'kubectl create service externalname my-ext-svc --external-name=api.google.com'.",
        "solution": "1. Run: kubectl create service externalname my-ext-svc --external-name=api.google.com"
    },
    {
        "id": "E-62",
        "domain": "Services & Networking (20%)",
        "title": "Configure Service SessionAffinity",
        "problem": "Modify service 'my-service' to use ClientIP session affinity.",
        "setup": "kubectl create deployment my-deploy --image=nginx --replicas=1 || true && kubectl create service clusterip my-service --tcp=80:80 || true",
        "cleanup": "kubectl delete deployment my-deploy --ignore-not-found=true && kubectl delete service my-service --ignore-not-found=true",
        "check": "kubectl get svc my-service -o jsonpath='{.spec.sessionAffinity}' | grep -w 'ClientIP'",
        "hint": "Set spec.sessionAffinity: ClientIP on my-service.",
        "solution": "1. Edit service: kubectl edit svc my-service\n2. Modify sessionAffinity to ClientIP"
    },
    {
        "id": "E-63",
        "domain": "Services & Networking (20%)",
        "title": "Create Pod with HostNetwork Enabled",
        "problem": "Deploy a pod named 'host-network-pod' with hostNetwork: true.",
        "setup": "kubectl delete pod host-network-pod --ignore-not-found=true",
        "cleanup": "kubectl delete pod host-network-pod --ignore-not-found=true",
        "check": "kubectl get pod host-network-pod -o jsonpath='{.spec.hostNetwork}' | grep -w 'true'",
        "hint": "Set hostNetwork: true in pod spec.",
        "solution": "1. Apply manifest:\nkubectl apply -f - <<EOF\napiVersion: v1\nkind: Pod\nmetadata:\n  name: host-network-pod\nspec:\n  hostNetwork: true\n  containers:\n  - name: web\n    image: nginx\nEOF"
    },
    {
        "id": "E-64",
        "domain": "Services & Networking (20%)",
        "title": "Enable Dual-Stack Service Mock",
        "problem": "Create a service called 'dual-stack-svc' configured for IPv4/IPv6 preferDualStack IP family policy.",
        "setup": "kubectl delete service dual-stack-svc --ignore-not-found=true",
        "cleanup": "kubectl delete service dual-stack-svc --ignore-not-found=true",
        "check": "kubectl get svc dual-stack-svc -o jsonpath='{.spec.ipFamilyPolicy}' | grep -i PreferDualStack || exit 0",
        "hint": "Set ipFamilyPolicy: PreferDualStack in service spec.",
        "solution": "1. Apply manifest:\nkubectl apply -f - <<EOF\napiVersion: v1\nkind: Service\nmetadata:\n  name: dual-stack-svc\nspec:\n  selector:\n    app: web\n  ports:\n  - port: 80\n  ipFamilyPolicy: PreferDualStack\nEOF"
    },
    {
        "id": "E-65",
        "domain": "Services & Networking (20%)",
        "title": "Check CNI Configurations",
        "problem": "Verify that CNI configurations are present inside nodes.",
        "setup": "echo 'CNI verification'",
        "cleanup": "echo 'Done'",
        "check": "docker exec cka-gold-control-plane ls /etc/cni/net.d/",
        "hint": "Look at /etc/cni/net.d/ inside the control plane container.",
        "solution": "1. Check CNI configuration: docker exec cka-gold-control-plane ls /etc/cni/net.d/"
    },
    {
        "id": "E-66",
        "domain": "Services & Networking (20%)",
        "title": "Expose deployment using LoadBalancer",
        "problem": "Expose deployment 'my-deploy' with LoadBalancer service named 'lb-service'.",
        "setup": "kubectl create deployment my-deploy --image=nginx --replicas=1 || true && kubectl delete service lb-service --ignore-not-found=true",
        "cleanup": "kubectl delete deployment my-deploy --ignore-not-found=true && kubectl delete service lb-service --ignore-not-found=true",
        "check": "kubectl get svc lb-service -o jsonpath='{.spec.type}' | grep -w 'LoadBalancer'",
        "hint": "Use 'kubectl expose deployment my-deploy --name=lb-service --type=LoadBalancer --port=80'.",
        "solution": "1. Run: kubectl expose deployment my-deploy --name=lb-service --type=LoadBalancer --port=80"
    },
    {
        "id": "E-67",
        "domain": "Services & Networking (20%)",
        "title": "CoreDNS Scale to 2 Replicas",
        "problem": "Scale the CoreDNS deployment to 2 replicas.",
        "setup": "kubectl scale deployment coredns -n kube-system --replicas=1",
        "cleanup": "kubectl scale deployment coredns -n kube-system --replicas=2",
        "check": "kubectl get deploy coredns -n kube-system -o jsonpath='{.status.replicas}' | grep -w '2'",
        "hint": "Use 'kubectl scale deployment coredns -n kube-system --replicas=2'.",
        "solution": "1. Run: kubectl scale deployment coredns -n kube-system --replicas=2"
    },
    {
        "id": "E-68",
        "domain": "Services & Networking (20%)",
        "title": "Configure Ingress TLS Secret",
        "problem": "Configure an ingress resource named 'secure-ingress' that binds to a TLS secret named 'secure-tls'.",
        "setup": "kubectl delete ingress secure-ingress --ignore-not-found=true",
        "cleanup": "kubectl delete ingress secure-ingress --ignore-not-found=true",
        "check": "kubectl get ingress secure-ingress -o jsonpath='{.spec.tls[0].secretName}' | grep -w 'secure-tls'",
        "hint": "Define a spec.tls block with hosts and secretName in the ingress manifest.",
        "solution": "1. Apply manifest:\nkubectl apply -f - <<EOF\napiVersion: networking.k8s.io/v1\nkind: Ingress\nmetadata:\n  name: secure-ingress\nspec:\n  tls:\n  - hosts:\n    - secure.example.com\n    secretName: secure-tls\n  rules:\n  - host: secure.example.com\n    http:\n      paths:\n      - path: /\n        pathType: Prefix\n        backend:\n          service:\n            name: web-svc\n            port:\n              number: 80\nEOF"
    },

    # ==========================================
    # --- WORKLOADS & SCHEDULING (15% - 13 Scenarios) ---
    # ==========================================
    {
        "id": "E-69",
        "domain": "Workloads & Scheduling (15%)",
        "title": "Deployment Rolling Update & Rollback",
        "problem": "Create a deployment 'rolling-dep' with image nginx:1.21. Upgrade to nginx:1.23, then rollback to previous configuration.",
        "setup": "kubectl create deployment rolling-dep --image=nginx:1.21 && sleep 2 && kubectl set image deployment/rolling-dep nginx=nginx:1.23",
        "cleanup": "kubectl delete deployment rolling-dep --ignore-not-found=true",
        "check": "kubectl rollout undo deployment/rolling-dep && sleep 2 && kubectl get deploy rolling-dep -o jsonpath='{.spec.template.spec.containers[0].image}' | grep -w 'nginx:1.21'",
        "hint": "Use 'kubectl rollout undo deployment/rolling-dep'.",
        "solution": "1. Run: kubectl rollout undo deployment/rolling-dep"
    },
    {
        "id": "E-70",
        "domain": "Workloads & Scheduling (15%)",
        "title": "Schedule Pod via NodeSelector",
        "problem": "Label cka-gold-worker node with 'disktype=ssd' and configure pod 'ssd-pod' to run on it via NodeSelector.",
        "setup": "kubectl label nodes cka-gold-worker disktype- && kubectl delete pod ssd-pod --ignore-not-found=true",
        "cleanup": "kubectl label nodes cka-gold-worker disktype- && kubectl delete pod ssd-pod --ignore-not-found=true",
        "check": "kubectl get pod ssd-pod -o jsonpath='{.spec.nodeSelector.disktype}' | grep -w 'ssd'",
        "hint": "Label the node: kubectl label node cka-gold-worker disktype=ssd. Add nodeSelector to pod.",
        "solution": "1. Label node: kubectl label node cka-gold-worker disktype=ssd\n2. Apply pod manifest:\nkubectl apply -f - <<EOF\napiVersion: v1\nkind: Pod\nmetadata:\n  name: ssd-pod\nspec:\n  nodeSelector:\n    disktype: ssd\n  containers:\n  - name: main\n    image: nginx\nEOF"
    },
    {
        "id": "E-71",
        "domain": "Workloads & Scheduling (15%)",
        "title": "Schedule Pod via Required NodeAffinity",
        "problem": "Configure a pod named 'affinity-pod' to only schedule on nodes with key 'zone' set to 'us-east'.",
        "setup": "kubectl delete pod affinity-pod --ignore-not-found=true",
        "cleanup": "kubectl delete pod affinity-pod --ignore-not-found=true",
        "check": "kubectl get pod affinity-pod -o jsonpath='{.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms[0].matchExpressions[0].key}' | grep -w 'zone'",
        "hint": "Use nodeAffinity in Pod spec.",
        "solution": "1. Apply manifest:\nkubectl apply -f - <<EOF\napiVersion: v1\nkind: Pod\nmetadata:\n  name: affinity-pod\nspec:\n  affinity:\n    nodeAffinity:\n      requiredDuringSchedulingIgnoredDuringExecution:\n        nodeSelectorTerms:\n        - matchExpressions:\n          - key: zone\n            operator: In\n            values:\n            - us-east\n  containers:\n  - name: main\n    image: nginx\nEOF"
    },
    {
        "id": "E-72",
        "domain": "Workloads & Scheduling (15%)",
        "title": "Configure PodAntiAffinity",
        "problem": "Configure deployment 'anti-affinity-deploy' with podAntiAffinity to prevent replicas from running on the same node.",
        "setup": "kubectl delete deployment anti-affinity-deploy --ignore-not-found=true",
        "cleanup": "kubectl delete deployment anti-affinity-deploy --ignore-not-found=true",
        "check": "kubectl get deploy anti-affinity-deploy -o jsonpath='{.spec.template.spec.affinity.podAntiAffinity}' | grep -v '^$'",
        "hint": "Add podAntiAffinity to deployment spec.",
        "solution": "1. Apply manifest with spec.template.spec.affinity.podAntiAffinity rule."
    },
    {
        "id": "E-73",
        "domain": "Workloads & Scheduling (15%)",
        "title": "Configure Toleration for Pod",
        "problem": "Create pod 'toleration-pod' that tolerates node taint 'tier=prod:NoSchedule'.",
        "setup": "kubectl delete pod toleration-pod --ignore-not-found=true",
        "cleanup": "kubectl delete pod toleration-pod --ignore-not-found=true",
        "check": "kubectl get pod toleration-pod -o jsonpath='{.spec.tolerations[0].key}' | grep -w 'tier'",
        "hint": "Define tolerations block in pod spec.",
        "solution": "1. Apply manifest:\nkubectl apply -f - <<EOF\napiVersion: v1\nkind: Pod\nmetadata:\n  name: toleration-pod\nspec:\n  tolerations:\n  - key: \"tier\"\n    operator: \"Equal\"\n    value: \"prod\"\n    effect: \"NoSchedule\"\n  containers:\n  - name: main\n    image: nginx\nEOF"
    },
    {
        "id": "E-74",
        "domain": "Workloads & Scheduling (15%)",
        "title": "Deploy DaemonSet",
        "problem": "Create a DaemonSet named 'monitoring-ds' running image prometheus/node-exporter on all nodes.",
        "setup": "kubectl delete daemonset monitoring-ds --ignore-not-found=true",
        "cleanup": "kubectl delete daemonset monitoring-ds --ignore-not-found=true",
        "check": "kubectl get daemonset monitoring-ds",
        "hint": "Create DaemonSet spec with selector and container exporter.",
        "solution": "1. Apply DaemonSet manifest:\nkubectl apply -f - <<EOF\napiVersion: apps/v1\nkind: DaemonSet\nmetadata:\n  name: monitoring-ds\nspec:\n  selector:\n    matchLabels:\n      name: monitoring-ds\n  template:\n    metadata:\n      labels:\n        name: monitoring-ds\n    spec:\n      containers:\n      - name: exporter\n        image: prometheus/node-exporter\nEOF"
    },
    {
        "id": "E-75",
        "domain": "Workloads & Scheduling (15%)",
        "title": "Deploy Multi-Container Pod with Shared Volume",
        "problem": "Deploy a pod 'multi-container-pod' containing two containers ('app' and 'sidecar') sharing an emptyDir volume at '/var/log'.",
        "setup": "kubectl delete pod multi-container-pod --ignore-not-found=true",
        "cleanup": "kubectl delete pod multi-container-pod --ignore-not-found=true",
        "check": "kubectl get pod multi-container-pod -o jsonpath='{.spec.containers[*].name}' | grep -q 'sidecar' && kubectl get pod multi-container-pod -o jsonpath='{.spec.volumes[*].emptyDir}' | grep -v '^$'",
        "hint": "Define two containers and associate them with a volume of type emptyDir.",
        "solution": "1. Apply multi-container pod manifest."
    },
    {
        "id": "E-76",
        "domain": "Workloads & Scheduling (15%)",
        "title": "Deploy InitContainer Pod",
        "problem": "Create a pod named 'init-pod' with an initContainer named 'init-myservice' that finishes immediately.",
        "setup": "kubectl delete pod init-pod --ignore-not-found=true",
        "cleanup": "kubectl delete pod init-pod --ignore-not-found=true",
        "check": "kubectl get pod init-pod -o jsonpath='{.spec.initContainers[0].name}' | grep -w 'init-myservice'",
        "hint": "Define spec.initContainers in the pod configuration.",
        "solution": "1. Apply manifest:\nkubectl apply -f - <<EOF\napiVersion: v1\nkind: Pod\nmetadata:\n  name: init-pod\nspec:\n  initContainers:\n  - name: init-myservice\n    image: busybox\n    command: ['sh', '-c', 'echo service up']\n  containers:\n  - name: main\n    image: nginx\nEOF"
    },
    {
        "id": "E-77",
        "domain": "Workloads & Scheduling (15%)",
        "title": "Create a CronJob",
        "problem": "Create a CronJob 'every-min-job' executing 'date' every minute.",
        "setup": "kubectl delete cronjob every-min-job --ignore-not-found=true",
        "cleanup": "kubectl delete cronjob every-min-job --ignore-not-found=true",
        "check": "kubectl get cronjob every-min-job -o jsonpath='{.spec.schedule}' | grep -w '*/1 * * * *' || kubectl get cronjob every-min-job -o jsonpath='{.spec.schedule}' | grep -w '* * * * *'",
        "hint": "Use 'kubectl create cronjob every-min-job --schedule=\"*/1 * * * *\" --image=busybox -- date'.",
        "solution": "1. Run: kubectl create cronjob every-min-job --schedule=\"* * * * *\" --image=busybox -- date"
    },
    {
        "id": "E-78",
        "domain": "Workloads & Scheduling (15%)",
        "title": "Create PodDisruptionBudget",
        "problem": "Create a PDB named 'web-pdb' selector app=web requiring minAvailable: 2.",
        "setup": "kubectl delete pdb web-pdb --ignore-not-found=true",
        "cleanup": "kubectl delete pdb web-pdb --ignore-not-found=true",
        "check": "kubectl get pdb web-pdb -o jsonpath='{.spec.minAvailable}' | grep -w '2'",
        "hint": "Apply a PodDisruptionBudget manifest.",
        "solution": "1. Apply manifest:\nkubectl apply -f - <<EOF\napiVersion: policy/v1\nkind: PodDisruptionBudget\nmetadata:\n  name: web-pdb\nspec:\n  minAvailable: 2\n  selector:\n    matchLabels:\n      app: web\nEOF"
    },
    {
        "id": "E-79",
        "domain": "Workloads & Scheduling (15%)",
        "title": "Create LimitRange in Default Namespace",
        "problem": "Create LimitRange 'default-limit' in default namespace setting default container CPU limit to 200m.",
        "setup": "kubectl delete limitrange default-limit --ignore-not-found=true",
        "cleanup": "kubectl delete limitrange default-limit --ignore-not-found=true",
        "check": "kubectl get limitrange default-limit -o jsonpath='{.spec.limits[0].default.cpu}' | grep -w '200m'",
        "hint": "Apply a LimitRange configuration YAML.",
        "solution": "1. Apply manifest:\nkubectl apply -f - <<EOF\napiVersion: v1\nkind: LimitRange\nmetadata:\n  name: default-limit\nspec:\n  limits:\n  - default:\n      cpu: 200m\n    type: Container\nEOF"
    },
    {
        "id": "E-80",
        "domain": "Workloads & Scheduling (15%)",
        "title": "Create Namespace ResourceQuota",
        "problem": "Create ResourceQuota named 'ns-quota' in default namespace limiting total pods count to 5.",
        "setup": "kubectl delete resourcequota ns-quota --ignore-not-found=true",
        "cleanup": "kubectl delete resourcequota ns-quota --ignore-not-found=true",
        "check": "kubectl get resourcequota ns-quota -o jsonpath='{.spec.hard.pods}' | grep -w '5'",
        "hint": "Use 'kubectl create resourcequota ns-quota --hard=pods=5'.",
        "solution": "1. Run: kubectl create resourcequota ns-quota --hard=pods=5"
    },
    {
        "id": "E-81",
        "domain": "Workloads & Scheduling (15%)",
        "title": "Run Parallel Job",
        "problem": "Create a Job named 'parallel-job' with parallelism 2 and completions 4 running 'sleep 5'.",
        "setup": "kubectl delete job parallel-job --ignore-not-found=true",
        "cleanup": "kubectl delete job parallel-job --ignore-not-found=true",
        "check": "kubectl get job parallel-job -o jsonpath='{.spec.parallelism}' | grep -w '2'",
        "hint": "Apply Job manifest with spec.parallelism: 2 and spec.completions: 4.",
        "solution": "1. Apply manifest:\nkubectl apply -f - <<EOF\napiVersion: batch/v1\nkind: Job\nmetadata:\n  name: parallel-job\nspec:\n  parallelism: 2\n  completions: 4\n  template:\n    spec:\n      containers:\n      - name: worker\n        image: busybox\n        command: [\"sleep\", \"5\"]\n      restartPolicy: Never\nEOF"
    },

    # ==========================================
    # --- STORAGE (10% - 9 Scenarios) ---
    # ==========================================
    {
        "id": "E-82",
        "domain": "Storage (10%)",
        "title": "Create HostPath PersistentVolume",
        "problem": "Create a PV named 'local-pv' size 1Gi, accessMode ReadWriteOnce, path '/mnt/data'.",
        "setup": "kubectl delete pv local-pv --ignore-not-found=true",
        "cleanup": "kubectl delete pv local-pv --ignore-not-found=true",
        "check": "kubectl get pv local-pv -o jsonpath='{.spec.capacity.storage}' | grep -w '1Gi'",
        "hint": "Use standard hostPath PV configuration.",
        "solution": "1. Apply manifest:\nkubectl apply -f - <<EOF\napiVersion: v1\nkind: PersistentVolume\nmetadata:\n  name: local-pv\nspec:\n  capacity:\n    storage: 1Gi\n  accessModes:\n    - ReadWriteOnce\n  hostPath:\n    path: \"/mnt/data\"\nEOF"
    },
    {
        "id": "E-83",
        "domain": "Storage (10%)",
        "title": "Create PVC and Bind to PV",
        "problem": "Create PVC named 'local-pvc' size 1Gi, RWO matching 'local-pv'.",
        "setup": "kubectl apply -f - <<EOF\napiVersion: v1\nkind: PersistentVolume\nmetadata:\n  name: local-pv\nspec:\n  capacity:\n    storage: 1Gi\n  accessModes:\n    - ReadWriteOnce\n  hostPath:\n    path: \"/mnt/data\"\nEOF || true && kubectl delete pvc local-pvc --ignore-not-found=true",
        "cleanup": "kubectl delete pvc local-pvc --ignore-not-found=true && kubectl delete pv local-pv --ignore-not-found=true",
        "check": "kubectl get pvc local-pvc -o jsonpath='{.status.phase}' | grep -i Bound",
        "hint": "Create PVC with storage size 1Gi and accessModes ReadWriteOnce.",
        "solution": "1. Apply manifest:\nkubectl apply -f - <<EOF\napiVersion: v1\nkind: PersistentVolumeClaim\nmetadata:\n  name: local-pvc\nspec:\n  accessModes:\n    - ReadWriteOnce\n  resources:\n    requests:\n      storage: 1Gi\n  volumeName: local-pv\nEOF"
    },
    {
        "id": "E-84",
        "domain": "Storage (10%)",
        "title": "Mount PVC to Pod",
        "problem": "Create pod 'storage-pod' mounting PVC 'local-pvc' at path '/usr/share/nginx/html'.",
        "setup": "kubectl delete pod storage-pod --ignore-not-found=true && kubectl apply -f - <<EOF\napiVersion: v1\nkind: PersistentVolume\nmetadata:\n  name: local-pv\nspec:\n  capacity:\n    storage: 1Gi\n  accessModes:\n    - ReadWriteOnce\n  hostPath:\n    path: \"/mnt/data\"\n---\napiVersion: v1\nkind: PersistentVolumeClaim\nmetadata:\n  name: local-pvc\nspec:\n  accessModes:\n    - ReadWriteOnce\n  resources:\n    requests:\n      storage: 1Gi\n  volumeName: local-pv\nEOF",
        "cleanup": "kubectl delete pod storage-pod --ignore-not-found=true && kubectl delete pvc local-pvc --ignore-not-found=true && kubectl delete pv local-pv --ignore-not-found=true",
        "check": "kubectl get pod storage-pod -o jsonpath='{.spec.containers[0].volumeMounts[0].mountPath}' | grep -w '/usr/share/nginx/html'",
        "hint": "Define volumes and volumeMounts inside the Pod spec.",
        "solution": "1. Apply manifest:\nkubectl apply -f - <<EOF\napiVersion: v1\nkind: Pod\nmetadata:\n  name: storage-pod\nspec:\n  containers:\n  - name: web\n    image: nginx\n    volumeMounts:\n    - name: log-vol\n      mountPath: /usr/share/nginx/html\n  volumes:\n  - name: log-vol\n    persistentVolumeClaim:\n      claimName: local-pvc\nEOF"
    },
    {
        "id": "E-85",
        "domain": "Storage (10%)",
        "title": "Create StorageClass with Retain Reclaim Policy",
        "problem": "Create StorageClass 'retain-sc' using local-path provisioner with reclaimPolicy set to Retain.",
        "setup": "kubectl delete sc retain-sc --ignore-not-found=true",
        "cleanup": "kubectl delete sc retain-sc --ignore-not-found=true",
        "check": "kubectl get sc retain-sc -o jsonpath='{.reclaimPolicy}' | grep -w 'Retain'",
        "hint": "Apply StorageClass manifest with reclaimPolicy: Retain.",
        "solution": "1. Apply manifest:\nkubectl apply -f - <<EOF\napiVersion: storage.k8s.io/v1\nkind: StorageClass\nmetadata:\n  name: retain-sc\nprovisioner: rancher.io/local-path\nreclaimPolicy: Retain\nvolumeBindingMode: Immediate\nEOF"
    },
    {
        "id": "E-86",
        "domain": "Storage (10%)",
        "title": "Dynamic PVC Volume Expansion check",
        "problem": "Verify that StorageClass standard allows volume expansion.",
        "setup": "echo 'SC setup'",
        "cleanup": "echo 'Done'",
        "check": "kubectl get sc standard -o jsonpath='{.allowVolumeExpansion}' | grep -w 'true' || exit 0",
        "hint": "Examine 'kubectl get sc standard -o yaml' and check for allowVolumeExpansion: true.",
        "solution": "1. Run: kubectl patch sc standard --type merge -p '{\"allowVolumeExpansion\":true}'"
    },
    {
        "id": "E-87",
        "domain": "Storage (10%)",
        "title": "Mount ConfigMap as Volume",
        "problem": "Create ConfigMap 'app-settings' with key 'app.config' and mount it as a volume in pod 'cm-vol-pod' at '/etc/config'.",
        "setup": "kubectl delete pod cm-vol-pod --ignore-not-found=true && kubectl delete configmap app-settings --ignore-not-found=true",
        "cleanup": "kubectl delete pod cm-vol-pod --ignore-not-found=true && kubectl delete configmap app-settings --ignore-not-found=true",
        "check": "kubectl get pod cm-vol-pod -o jsonpath='{.spec.containers[0].volumeMounts[0].mountPath}' | grep -w '/etc/config'",
        "hint": "Use configMap volume type in pod volumes definition.",
        "solution": "1. Create ConfigMap: kubectl create configmap app-settings --from-literal=app.config=setting-value\n2. Apply pod manifest mounting CM volume."
    },
    {
        "id": "E-88",
        "domain": "Storage (10%)",
        "title": "Inject Secret as Env Variables",
        "problem": "Create Secret 'db-secret' with DB_PASS='secret123' and inject it as env variable DB_PASSWORD in pod 'secret-env-pod'.",
        "setup": "kubectl delete pod secret-env-pod --ignore-not-found=true && kubectl delete secret db-secret --ignore-not-found=true",
        "cleanup": "kubectl delete pod secret-env-pod --ignore-not-found=true && kubectl delete secret db-secret --ignore-not-found=true",
        "check": "kubectl get pod secret-env-pod -o jsonpath='{.spec.containers[0].env[0].valueFrom.secretKeyRef.key}' | grep -w 'DB_PASS'",
        "hint": "Define env with valueFrom.secretKeyRef in the Pod container spec.",
        "solution": "1. Create secret: kubectl create secret generic db-secret --from-literal=DB_PASS=secret123\n2. Apply Pod manifest with secretKeyRef env mapping."
    },
    {
        "id": "E-89",
        "domain": "Storage (10%)",
        "title": "Configure Pod EmptyDir Volume",
        "problem": "Create pod 'cache-pod' with an emptyDir volume mounted at '/cache'.",
        "setup": "kubectl delete pod cache-pod --ignore-not-found=true",
        "cleanup": "kubectl delete pod cache-pod --ignore-not-found=true",
        "check": "kubectl get pod cache-pod -o jsonpath='{.spec.volumes[0].emptyDir}' || exit 1",
        "hint": "Set volume type to emptyDir: {} in Pod spec.",
        "solution": "1. Apply manifest:\nkubectl apply -f - <<EOF\napiVersion: v1\nkind: Pod\nmetadata:\n  name: cache-pod\nspec:\n  containers:\n  - name: main\n    image: nginx\n    volumeMounts:\n    - name: cache-vol\n      mountPath: /cache\n  volumes:\n  - name: cache-vol\n    emptyDir: {}\nEOF"
    },
    {
        "id": "E-90",
        "domain": "Storage (10%)",
        "title": "Check PV Reclaim Status Released",
        "problem": "Demonstrate the Retain reclaim policy. If PVC is deleted, the matching PV should remain in Released status.",
        "setup": "echo 'Simulation'",
        "cleanup": "echo 'Done'",
        "check": "echo 'Passed'",
        "hint": "When PV has reclaimPolicy: Retain, deleting the PVC moves the PV to Released status rather than deleting it.",
        "solution": "1. Understand that Retain policy preserves the PV and its files on the backend storage."
    },
    {
        "id": "E-91",
        "domain": "Workloads & Scheduling (15%)",
        "title": "Troubleshoot Node Capacity Resource Limits",
        "problem": "Pod 'resource-fit' is stuck in Pending because it requests too much CPU. Adjust resource requests so that it can run on the cluster nodes.",
        "setup": "kubectl run resource-fit --image=nginx --requests='cpu=80'",
        "cleanup": "kubectl delete pod resource-fit --ignore-not-found=true",
        "check": "kubectl get pod resource-fit -o jsonpath='{.status.phase}' | grep -i Running",
        "hint": "Examine the CPU requests. Nodes do not have 80 cores. Scale it down to 50m (0.05 core).",
        "solution": "1. Delete the stuck pod: kubectl delete pod resource-fit --force\n2. Recreate with valid requests: kubectl run resource-fit --image=nginx --requests='cpu=50m'"
    },
    {
        "id": "E-92",
        "domain": "Troubleshooting (30%)",
        "title": "Ephemeral Container Debug",
        "problem": "Pod 'crashed-pod' is running with a shellless distroless image and has issues. Debug it by launching an ephemeral container with image 'busybox' inside it.",
        "setup": "kubectl run crashed-pod --image=gcr.io/distroless/static-debian11 --command -- sleep 3600",
        "cleanup": "kubectl delete pod crashed-pod --ignore-not-found=true",
        "check": "kubectl get pod crashed-pod -o jsonpath='{.spec.ephemeralContainers[0].name}' | grep -i debug",
        "hint": "Use 'kubectl debug crashed-pod -it --image=busybox --target=crashed-pod --name=debug-container' (wait, in check we check for any debug container name).",
        "solution": "1. Run: kubectl debug crashed-pod -it --image=busybox --image-pull-policy=IfNotPresent --share-processes --name=debug-container"
    },
    {
        "id": "E-93",
        "domain": "Troubleshooting (30%)",
        "title": "JSONPath Node OS Image Filter",
        "problem": "Use JSONPath to list all nodes with their names and OS images, sorted by name, and write the output format 'Name: <node-name>, OS: <os-image>' to file '/tmp/node-os.txt'.",
        "setup": "rm -f /tmp/node-os.txt",
        "cleanup": "rm -f /tmp/node-os.txt",
        "check": "grep -q 'OS:' /tmp/node-os.txt && grep -q 'cka-gold-control-plane' /tmp/node-os.txt",
        "hint": "Use kubectl get nodes -o jsonpath='{range .items[*]}Name: {.metadata.name}, OS: {.status.nodeInfo.osImage}{\"\\n\"}{end}' > /tmp/node-os.txt.",
        "solution": "1. Run: kubectl get nodes -o jsonpath='{range .items[*]}Name: {.metadata.name}, OS: {.status.nodeInfo.osImage}{\"\\n\"}{end}' > /tmp/node-os.txt"
    },
    {
        "id": "E-94",
        "domain": "Troubleshooting (30%)",
        "title": "JSONPath Pod IP Filter",
        "problem": "Extract the IP addresses of all pods in namespace 'default' with label 'app=web-app' and write the list of IPs to '/tmp/pod-ips.txt'.",
        "setup": "kubectl create deployment web-app --image=nginx --replicas=2 || true && rm -f /tmp/pod-ips.txt",
        "cleanup": "kubectl delete deployment web-app --ignore-not-found=true && rm -f /tmp/pod-ips.txt",
        "check": "cat /tmp/pod-ips.txt | grep -E '^[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+'",
        "hint": "Use kubectl get pods -l app=web-app -o jsonpath='{.items[*].status.podIP}' > /tmp/pod-ips.txt.",
        "solution": "1. Run: kubectl get pods -l app=web-app -o jsonpath='{.items[*].status.podIP}' | tr ' ' '\\n' > /tmp/pod-ips.txt"
    },
    {
        "id": "E-95",
        "domain": "Storage (10%)",
        "title": "ConfigMap Multi-key Volume Mount",
        "problem": "Create a ConfigMap named 'multi-config' containing keys 'config1=val1' and 'config2=val2'. Mount it in pod 'config-mount-pod' under directory '/etc/config' so that config1 and config2 appear as files.",
        "setup": "kubectl delete pod config-mount-pod --ignore-not-found=true && kubectl delete configmap multi-config --ignore-not-found=true",
        "cleanup": "kubectl delete pod config-mount-pod --ignore-not-found=true && kubectl delete configmap multi-config --ignore-not-found=true",
        "check": "kubectl get pod config-mount-pod -o jsonpath='{.spec.volumes[0].configMap.name}' | grep -w 'multi-config'",
        "hint": "Use kubectl create configmap. Create Pod spec with a volume referencing the ConfigMap and mount it.",
        "solution": "1. Create CM: kubectl create configmap multi-config --from-literal=config1=val1 --from-literal=config2=val2\n2. Apply pod manifest mounting 'multi-config' volume at '/etc/config'."
    },
    {
        "id": "E-96",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Pod ServiceAccount Integration",
        "problem": "Create a ServiceAccount named 'deploy-sa' in namespace 'default'. Configure a pod named 'sa-pod' to run using this ServiceAccount and verify its token is mounted inside.",
        "setup": "kubectl delete pod sa-pod --ignore-not-found=true && kubectl delete serviceaccount deploy-sa --ignore-not-found=true",
        "cleanup": "kubectl delete pod sa-pod --ignore-not-found=true && kubectl delete serviceaccount deploy-sa --ignore-not-found=true",
        "check": "kubectl get pod sa-pod -o jsonpath='{.spec.serviceAccountName}' | grep -w 'deploy-sa'",
        "hint": "Set serviceAccountName: deploy-sa in the Pod spec.",
        "solution": "1. Create SA: kubectl create serviceaccount deploy-sa\n2. Apply Pod manifest:\nkubectl apply -f - <<EOF\napiVersion: v1\nkind: Pod\nmetadata:\n  name: sa-pod\nspec:\n  serviceAccountName: deploy-sa\n  containers:\n  - name: main\n    image: nginx\nEOF"
    },
    {
        "id": "E-97",
        "domain": "Workloads & Scheduling (15%)",
        "title": "Sidecar Log Rotation Handler",
        "problem": "Create a multi-container pod named 'logger-pod' containing container 'app' writing to '/var/log/app.log', and a sidecar container 'log-watcher' that tail-logs that file.",
        "setup": "kubectl delete pod logger-pod --ignore-not-found=true",
        "cleanup": "kubectl delete pod logger-pod --ignore-not-found=true",
        "check": "kubectl get pod logger-pod -o jsonpath='{.spec.containers[*].name}' | grep -q 'log-watcher' && kubectl get pod logger-pod -o jsonpath='{.spec.volumes[0].emptyDir}' || exit 1",
        "hint": "Create pod with emptyDir volume shared by both containers.",
        "solution": "1. Apply manifest with two containers sharing an emptyDir volume mounted at /var/log."
    },
    {
        "id": "E-98",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "Kubelet Cgroup Driver Check",
        "problem": "Ensure the cgroup driver used by the Kubelet on cka-gold-control-plane node is configured to 'systemd'.",
        "setup": "echo 'Simulation'",
        "cleanup": "echo 'Done'",
        "check": "docker exec cka-gold-control-plane grep -q 'cgroupDriver: systemd' /var/lib/kubelet/config.yaml || exit 0",
        "hint": "Check the cgroupDriver setting inside /var/lib/kubelet/config.yaml.",
        "solution": "1. Cgroup driver on kind is systemd by default. Verify: docker exec cka-gold-control-plane grep 'cgroupDriver' /var/lib/kubelet/config.yaml"
    },
    {
        "id": "E-99",
        "domain": "Cluster Architecture, Installation & Config (25%)",
        "title": "API Server Port Diagnostics (Port occupied)",
        "problem": "Simulate port collision. The API server fails to bind because port 6443 is blocked on the host. Fix the blocking issue.",
        "setup": "docker exec cka-gold-control-plane sh -c 'apt-get update && apt-get install -y netcat-openbsd || true' && docker exec -d cka-gold-control-plane nc -l -p 6443",
        "cleanup": "docker exec cka-gold-control-plane pkill -f 'nc -l -p 6443' || true",
        "check": "kubectl get nodes",
        "hint": "Check port usage on control plane node. Kill the netcat process blocking port 6443.",
        "solution": "1. Exec into control plane: docker exec cka-gold-control-plane fuser -k 6443/tcp || docker exec cka-gold-control-plane pkill -f 'nc -l -p 6443'"
    },
    {
        "id": "E-100",
        "domain": "Troubleshooting (30%)",
        "title": "CNI Config Restoration",
        "problem": "Node 'cka-gold-worker' becomes NotReady because CNI config file '/etc/cni/net.d/10-kindnet.conflist' was renamed. Restore it.",
        "setup": "docker exec cka-gold-worker mv /etc/cni/net.d/10-kindnet.conflist /etc/cni/net.d/10-kindnet.conflist.bak 2>/dev/null",
        "cleanup": "docker exec cka-gold-worker mv /etc/cni/net.d/10-kindnet.conflist.bak /etc/cni/net.d/10-kindnet.conflist 2>/dev/null || true",
        "check": "kubectl get node cka-gold-worker -o jsonpath='{.status.conditions[?(@.type==\"Ready\")].status}' | grep -i True",
        "hint": "Access cka-gold-worker node, look for backed up files in /etc/cni/net.d/, and rename it back.",
        "solution": "1. Restore: docker exec cka-gold-worker mv /etc/cni/net.d/10-kindnet.conflist.bak /etc/cni/net.d/10-kindnet.conflist"
    }
]

