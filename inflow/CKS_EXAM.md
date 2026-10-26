https://www.youtube.com/playlist?list=PLyKswBedEWujChLpKK6zFj0S4MOUaxqR3  (Youtube playlist with exam Questions)


    1. Fix insecure kubelet and etcd  
    Ensure:  
    Kubelet:  
    /var/lib/kubelet/config.yaml  
    anonymous-auth=false  
    --authorization-mode=Webhook  
    Etcd:  
    - --client-cert-auth  
      
    2. TLS Secret  
    Create the TLS secret (it’s already referenced in the Deployment).  
    K create secret tls <name> -n <ns> —key <path> —cert <path>  
      
      
    3. Dockerfile security best practices  
    couchdb -> nobody  
    User root  
    Use USER nobody in the Dockerfile  
    In the Deployment:  
    runAsUser: 65535  
    readOnlyRootFilesystem: true  
    privileged: false  
      
      
    4. Pod accessing /dev/mem  
    Write a custom Falco rule to detect /dev/mem access  
    Identify the bad Pod  
    Scale its Deployment to 0 replicas  
      
    - rule: Detect /dev/mem Access  
    desc: Alert when any process opens /dev/mem  
    condition: container and open_read and fd.name = "/dev/mem"  
    output: "Suspicious /dev/mem access (pod=%k8s.pod.name ns=%k8s.ns.name user=%user.name cmd=%proc.cmdline file=%fd.name)"  
    priority: WARNING  
    tags: [filesystem, mitre_discovery]  
      
    5. Container security context  
    Ensure container immutability:  
    runAsUser: 30000  
    readOnlyRootFilesystem: true  
    allowPrivilegeEscalation: false  
      
      
    6. Audit logging  
    Reconfigure the API server:  
    Use a base audit policy  
    Configure log retention (e.g., max 2 log files for X days)  
    add logs at different levels (Metadata, Request) to ns, deploy (specific ns), secrets and configmaps and metadata catch all at the end  
      
    7. NetworkPolicy  
    Deny all ingress traffic  
    Allow ingress only from Pods within a specific namespace  
      
      
    8. Expose HTTPS via Ingress  
    Create an Ingress with TLS termination. Make sure to use/remember this annotation.  
    Cilium:  
    [ingress.cilium.io/force-https:](https://ingress.cilium.io/force-https:) “”enabled  
    nginx:  
    annotations:  
    [nginx.ingress.kubernetes.io/ssl-redirect:](https://nginx.ingress.kubernetes.io/ssl-redirect:) "true"  
      
      
    K create ingress <name> -n <ns> —class cilium —rule=kodekloud.com/*=web-svc:80,tls=web-secret  
      
      
    9. Disable API credential auto-mounting  
    Disable auto-mounting in the ServiceAccount  
    Mount the token manually via a projected volume (read-only)  
    [https://kubernetes.io/docs/concepts/storage/projected-volumes/#serviceaccounttoken](https://kubernetes.io/docs/concepts/storage/projected-volumes/#serviceaccounttoken)  
      
    10. Upgrade cluster node  
    Worker node was one patch version behind (straightforward upgrade).  
    1.35.2  
    kubectl drain node01 --ignore-daemonsets --delete-emptydir-data --force  
      
    ssh node01  
    sudo -i  
      
    apt update  
    apt-cache madison kubeadm | grep 1.32 # Replace with your control plane version  
    apt-mark unhold kubeadm  
    apt-get install -y kubeadm=1.32.1-1 # Use exact version from madison  
    apt-mark hold kubeadm  
      
    kubeadm upgrade node  
    apt-mark unhold kubelet kubectl  
    apt-get install -y kubelet=1.32.1-11 kubectl=1.32.1-11  
    apt-mark hold kubelet kubectl  
    Then:  
    systemctl daemon-reload  
    systemctl restart kubelet  
    exit (from node01)  
    kubectl uncordon node01  
      
      
    11. Generate SPDX document (bom tool)  
    Identify which Alpine image contains libcrypto3 —version 3-15-0  
    Remove that container from the Deployment  
    bom generate --image something/alpine:3.19.1 --output alpine.spdx  
      
      
    bom generate --image something/alpine:3.19.1 | gerp -i libcrypto3 | grep -i 3-15-0  
      
    12. Restricted Pod Security Standard  
    A namespace enforces restricted PSS  
    Fix the Deployment so Pods become compliant  
      
      
    K describe rs -n <ns>  
      
    13. Secure Docker daemon  
    Remove a user from the docker group  
    Ensure /var/run/docker.sock is owned by root  
      
      
    Gpasswd docker -d developer  
    Systemctl status docker.socket  
    Ll /var/run/docker.sock  
      
    14. Cilium Network Policy  
    Allow Pods in a namespace to access Deployment Pods  
    Require mutual authentication  
    Allow host access to specific Pods without mutual auth  
    istio mils in my case: label the ns and enable strict peer authentication  
      
      
    15. ImagePolicyWebhook  
    Configure API server admission plugins  
    Use provided AdmissionConfiguration  
    Set ImagePolicyWebhook to deny images when backend is unavailable  
      
    Kodekloud exams  
      
      
    16. API server authentication  
    Disable anonymous access —anonymous-auth=false  
    Use:  
    Node,RBAC authorization  
    Enable:  
    NodeRestriction admission controller  
      
    /etc/kubernetes/manifests/kube-apiserver.yaml