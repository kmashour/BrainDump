# CKA Practice Playbook - Lightning Labs & Mock Exams

This playbook compiles practice questions, scenario requirements, diagnostic steps, CLI solutions, and YAML manifests from the Lightning Labs, Mock Exams, Ultimate Mocks, and Network Policy Testing tips and tricks.


# Section 1: Lightning Labs

## Introduction

  #### Welcome to the KodeKloud CKA Lightning Labs!
   
  - This section has been created to give you hands-on practice in solving questions of mixed difficulty in a short period of time.
   
  - This environment is only valid for 35 minutes. You have 5-8 questions to complete within this time.
   
  - You can toggle between the questions but make sure that that you click on `END EXAM` before the 35 minute mark. To pass, you need to secure 80%.
   
   Good Luck!!!
   
   Note: Answers for most questions should be available under the `/var/answers` directory on the master node.
   
   
  #### Disclaimer:
   
  - Please note that this exam is not a replica of the actual exam
  - Please note that the questions in these exams are not the same as in the actual exam
  - Please note that the interface is not the same as in the actual exam
  - Please note that the scoring system may not be the same as in the actual exam
  - Please note that the difficulty level may not be the same as in the actual exam
   
   
  - I want to understand what Lightning Lab is, [Let's Explore](https://kodekloud.com/topic/lightning-lab-introduction/)

---

## Lightning Lab 1 Solutions

  - I am ready! [Take me to Lightning Lab 1](https://kodekloud.com/topic/lightning-lab-1-2/)

## Solution to LL-1

1.  Upgrade the current version of kubernetes from 1.28.0 to 1.29.0 exactly using the kubeadm utility.

    Make sure that the upgrade is carried out one node at a time starting with the controlplane node. To minimize downtime, the deployment `gold-nginx` should be rescheduled on an alternate node before upgrading each node.


    Upgrade `controlplane` node first and drain node `node01` before upgrading it. Pods for `gold-nginx` should run on the controlplane node subsequently.

    **Upgrade `controlplane`**

    1.  Update package repo

        ```bash
        apt update
        ```

    1.  Check madison to see what kubernetes packages are available

        ```bash
        apt-cache madison kubeadm
        ```

        Note that only 1.28 versions are present, meaning you have to grab the 1.29 repos

    1.  Grab kubernetes 1.29 repos

        For this, we need to edit the apt source file which you should find is `/etc/apt/sources.list.d/kubernetes.list`

        ```bash
        vi /etc/apt/sources.list.d/kubernetes.list
        ```

        FInd any occurrence of `1.28` in this file and change it to `1.29`, then save and exit from vi.

    1.  Now run madison again to find out the package version for 1.29

        ```bash
        apt-cache madison kubeadm
        ```

        You should see the following in the list

        > `kubeadm | 1.29.0-1.1 | https://pkgs.k8s.io/core:/stable:/v1.29/deb  Packages`

        Now we know the package version is `1.29.0-1.1` we can proceed with the upgrade

    1. Drain node

        ```bash
        kubectl drain controlplane --ignore-daemonsets
        ```

    1. Upgrade kubeadm

        ```bash
        apt-mark unhold kubeadm
        apt install -y kubeadm=1.29.0-1.1
        ```

    1. Plan and apply upgrade

        ```bash
        kubeadm upgrade plan
        kubeadm upgrade apply v1.29.0
        ```

    1. Upgrade the kubelet

        ```bash
        apt-mark unhold kubelet
        apt install -y kubelet=1.29.0-1.1
        systemctl daemon-reload
        systemctl restart kubelet
        ```

    1. Reinstate controlplane node

        ```bash
        kubectl uncordon controlplane
        ```

    1. Upgrade kubectl

        ```bash
        apt-mark unhold kubectl
        apt install -y kubectl=1.29.0-1.1
        ```

    1. Re-hold packages

        ```bash
        apt-mark hold kubeadm kubelet kubectl
        ```

    **Upgrade `node01`**

    1. Drain the worker node

        ```bash
        kubectl drain node01 --ignore-daemonsets
        ```

    1. Go to worker node

        ```bash
        ssh node01
        ```

    1. As before, you will need to update the package caches for v1.29

        Follow the same steps as you did on `controlplane`

    1. Upgrade kubeadm

        ```bash
        apt-mark unhold kubeadm
        apt install -y kubeadm=1.29.0-1.1
        ```

    1. Upgrade node

        ```bash
        kubeadm upgrade node
        ```

    1. Upgrade the kubelet

        ```bash
        apt-mark unhold kubelet
        apt install kubelet=1.29.0-1.1
        systemctl daemon-reload
        systemctl restart kubelet
        ```

    1. Re-hold packages

        ```bash
        apt-mark hold kubeadm kubelet
        ```

    1. Return to controlplane

        ```bash
        exit
        ```

    1. Reinstate worker node

        ```bash
        kubectl uncordon node01
        ```

    1. Verify `gold-nginx` is scheduled on controlplane node

        ```bash
        kubectl get pods -o wide | grep gold-nginx
        ```

    **TIP**

    To do cluster upgrades faster and save at least 3 minutes, you can work on both nodes at the same time.

    While `kubeadm upgrade apply` is running on `controlplane`, which takes some minutes, open a second terminal and perform steps `ii`, `iii` and `iv` of "Upgrade `node01`", so that it is ready for `kubeadm upgrade node` as soon as you have drained it.




2.  Print the names of all deployments in the admin2406 namespace in the following format...

    This is a job for `custom-columns` output of kubectl

    ```bash
    kubectl -n admin2406 get deployment -o custom-columns=DEPLOYMENT:.metadata.name,CONTAINER_IMAGE:.spec.template.spec.containers[].image,READY_REPLICAS:.status.readyReplicas,NAMESPACE:.metadata.namespace --sort-by=.metadata.name > /opt/admin2406_data
    ```
    

3.  <details>
    <summary>A kubeconfig file called admin.kubeconfig has been created in /root/CKA. There is something wrong with the configuration. Troubleshoot and fix it.</summary>

    First, test this kubeconfig file to observe the connection error:

    ```bash
    kubectl get pods --kubeconfig /root/CKA/admin.kubeconfig
    ```

    *Diagnostic Output:* Typically shows a connection failure to an incorrect port (e.g., `4380`).

    Compare it with the default working configuration to verify the correct control plane API server port:

    ```bash
    cat ~/.kube/config
    ```

    Modify the port in `admin.kubeconfig` from `4380` to `6443` (the default API server port):

    ```bash
    vi /root/CKA/admin.kubeconfig
    # Under clusters -> cluster -> server:
    # Change port from 4380 to 6443:
    # server: https://controlplane:6443
    ```

    Test the connectivity again to verify it is resolved:

    ```bash
    kubectl get pods --kubeconfig /root/CKA/admin.kubeconfig
    ```
    
    </details>


4.  <details>
    <summary>Create a new deployment called nginx-deploy, with image nginx:1.16 and 1 replica. Next upgrade the deployment to version 1.17 using rolling update.</summary>

    ```bash
    kubectl create deployment nginx-deploy --image=nginx:1.16
    kubectl set image deployment/nginx-deploy nginx=nginx:1.17 --record
    ```

    You may ignore the deprecation warning.

    </details>

5.  <details>
    <summary>A new deployment called alpha-mysql has been deployed in the alpha namespace. However, the pods are not running. Troubleshoot and fix the issue.</summary>

    The deployment should make use of the persistent volume alpha-pv to be mounted at /var/lib/mysql and should use the environment variable MYSQL_ALLOW_EMPTY_PASSWORD=1 to make use of an empty root password.

    Important: Do not alter the persistent volume.

    Inspect the deployment to check the environment variable is set. Here I'm using `yq` which is like `jq` but for YAML to not have to view the _entire_ deployment YAML, just the section beneath `containers` in the deployment spec.

    ```bash
    kubectl get deployment -n alpha alpha-mysql  -o yaml | yq e .spec.template.spec.containers -
    ```

    Find out why the deployment does not have minimum availability. We'll have to find out the name of the deployment's pod first, then describe the pod to see the error.

    ```bash
    kubectl get pods -n alpha
    kubectl describe pod -n alpha alpha-mysql-xxxxxxxx-xxxxx
    ```

    We find that the requested PVC isn't present, so create it. First, examine the Persistent Volume to find the values for access modes, capacity (storage), and storage class name

    ```bash
    kubectl get pv alpha-pv
    ```

    Now use `vi` to create a PVC manifest

    ```yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: mysql-alpha-pvc
      namespace: alpha
    spec:
      accessModes:
      - ReadWriteOnce
      resources:
        requests:
          storage: 1Gi
      storageClassName: slow
    ```
    
  </details>

6.  <details>
    <summary>Take the backup of ETCD at the location /opt/etcd-backup.db on the controlplane node.</summary>

    This question is a bit poorly worded. It requires us to make a backup of etcd and store the backup at the given location.

    Know that the certificates we need for authentication of `etcdctl` are located in `/etc/kubernetes/pki/etcd`

    ```bash
    ETCDCTL_API='3' etcdctl snapshot save \
      --cacert=/etc/kubernetes/pki/etcd/ca.crt \
      --cert=/etc/kubernetes/pki/etcd/server.crt \
      --key=/etc/kubernetes/pki/etcd/server.key \
      /opt/etcd-backup.db
    ```

    Whilst we _could_ also use the argument `--endpoints=127.0.0.1:2379`, it is not necessary here as we are on the controlplane node, same as `etcd` itself. The default endpoint is the local host.
    
    </details>

7.  <details>
    <summary>Create a pod called secret-1401 in the admin1401 namespace using the busybox image....</summary>

    The container within the pod should be called `secret-admin` and should sleep for 4800 seconds.

    The container should mount a read-only secret volume called secret-volume at the path `/etc/secret-volume`. The secret being mounted has already been created for you and is called `dotfile-secret`.

    1. Use imperative command to get a starter manifest

        ```bash
        kubectl run secret-1401 -n admin1401 --image busybox --dry-run=client -o yaml --command -- sleep 4800 > admin.yaml
        ```

    1. Edit this manifest to add in the details for mounting the secret

        ```bash
        vi admin.yaml
        ```

        Add in the volume and volume mount sections seen below

        ```yaml
        apiVersion: v1
        kind: Pod
        metadata:
          creationTimestamp: null
          labels:
            run: secret-1401
          name: secret-1401
          namespace: admin1401
        spec:
          volumes:
          - name: secret-volume
            secret:
              secretName: dotfile-secret
          containers:
          - command:
            - sleep
            - "4800"
            image: busybox
            name: secret-admin
            volumeMounts:
            - name: secret-volume
              readOnly: true
              mountPath: /etc/secret-volume
        ```

    1. And create the pod

        ```bash
        kubectl create -f admin.yaml
        ```

  </details>

---


# Section 2: Mock Exams 1-3

## Introduction

  - Take me to [Introduction of Mock Exams](https://kodekloud.com/topic/mock-exam-introduction-4/)

---

## Mock Exam 1 Solutions

  Test My Knowledge, Take me to [Mock Exam 1](https://kodekloud.com/topic/mock-exam-1-3/)

  #### Solution to the Mock Exam 1

  1. Apply below manifests:

     <details>
     <summary>Reveal Solution</summary>
     
     ```yaml
     apiVersion: v1
     kind: Pod
     metadata:
       creationTimestamp: null
       labels:
         run: nginx-pod
       name: nginx-pod
     spec:
       containers:
       - image: nginx:alpine
         name: nginx-pod
         resources: {}
       dnsPolicy: ClusterFirst
       restartPolicy: Always
     status: {}
     ```
     
     </details>

  2. Run below command which create a pod with labels:

     <details>
     <summary>Reveal Solution</summary>
     
     ```bash
     kubectl run messaging --image=redis:alpine --labels=tier=msg
     ```
     
     </details>

 
  3. Run below command to create a namespace:
     
     <details>
     <summary>Reveal Solution</summary>

     ```bash
     kubectl create namespace apx-x9984574
     ```
     
     </details>

  4. Use the below command which will redirect the o/p:

     <details>
     <summary>Reveal Solution</summary>

     ```bash
     kubectl get nodes -o json > /opt/outputs/nodes-z3444kd9.json
     ```
     
     </details>

  5. Execute below command which will expose the pod on port 6379:

     <details>
     <summary>Reveal Solution</summary>

     ```bash
     kubectl expose pod messaging --port=6379 --name messaging-service
     ```
     
     </details>

  6. Apply below manifests:

     <details>
     <summary>Reveal Solution</summary>

      ```yaml
      apiVersion: apps/v1
      kind: Deployment
      metadata:
        creationTimestamp: null
        labels:
          app: hr-web-app
        name: hr-web-app
      spec:
        replicas: 2
        selector:
          matchLabels:
            app: hr-web-app
        strategy: {}
        template:
          metadata:
            creationTimestamp: null
            labels:
              app: hr-web-app
          spec:
            containers:
            - image: kodekloud/webapp-color
              name: webapp-color
              resources: {}
      status: {}
      ```
      
      In v1.19, we can add `--replicas` flag with `kubectl create deployment` command:
      ```bash
      kubectl create deployment hr-web-app --image=kodekloud/webapp-color --replicas=2
      ```
      
     </details>

  7. To Create a static pod, copy it to the static pods directory. In this case, it is `/etc/kubernetes/manifests`. Apply below manifests:

     <details>
     <summary>Reveal Solution</summary>

     ```yaml
     apiVersion: v1
     kind: Pod
     metadata:
       creationTimestamp: null
       labels:
         run: static-busybox
       name: static-busybox
     spec:
       containers:
       - command:
         - sleep
         - "1000"
         image: busybox
         name: static-busybox
         resources: {}
       dnsPolicy: ClusterFirst
       restartPolicy: Always
     status: {}
     ```
     
     </details>

  8. Run below command to create a pod in namespace `finance`:

     <details>
     <summary>Reveal Solution</summary>

     ```bash
     kubectl run temp-bus --image=redis:alpine -n finance
     ```
     
     </details>

  9. Run below command and troubleshoot step by step:

     <details>
     <summary>Reveal Solution</summary>

     ```bash
     kubectl describe pod orange
     ```

     Export the running pod using below command and correct the spelling of the command **`sleeeep`** to **`sleep`** 

     ```bash
     kubectl get pod orange -o yaml > orange.yaml
     ```
   
     Delete the running Orange pod and recreate the pod using command.
     
     ```bash
     kubectl delete pod orange
     kubectl create -f orange.yaml
     ```
     
     </details>

  10. Apply below manifests:

      <details>
      <summary>Reveal Solution</summary>

      ```yaml
      apiVersion: v1
      kind: Service
      metadata:
        creationTimestamp: null
        labels:
          app: hr-web-app
        name: hr-web-app-service
      spec:
        ports:
        - port: 8080
          protocol: TCP
          targetPort: 8080
          nodePort: 30082
        selector:
          app: hr-web-app
        type: NodePort
      status:
        loadBalancer: {}
      ```
      
      </details>

  11. Run the below command to redirect the o/p:

      <details>
      <summary>Reveal Solution</summary>

      ```bash
      kubectl get nodes -o jsonpath='{.items[*].status.nodeInfo.osImage}' > /opt/outputs/nodes_os_x43kj56.txt
      ```
      
      </details>

  12. Apply the below manifest to create a PV:

      <details>
      <summary>Reveal Solution</summary>
     
       ```yaml
       apiVersion: v1
       kind: PersistentVolume
       metadata:
         name: pv-analytics
       spec:
         capacity:
           storage: 100Mi
         volumeMode: Filesystem
         accessModes:
           - ReadWriteMany
         hostPath:
             path: /pv/data-analytics
       ```
       
       </details>

---

## Mock Exam 2 Solutions

  1. Run the below command for solution:

     <details>
     <summary>Reveal Solution</summary>

     ```bash
     ETCDCTL_API=3 etcdctl snapshot save --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key --endpoints=127.0.0.1:2379 /opt/etcd-backup.db
     ```
     
     </details>

  2. Run the below command for solution:

     <details>
     <summary>Reveal Solution</summary>
 
     ```yaml
     apiVersion: v1
     kind: Pod
     metadata:
        creationTimestamp: null
        labels:
          run: redis-storage
        name: redis-storage
     spec:
      volumes:
      - name: redis-storage
        emptyDir: {}
      
      containers:
      - image: redis:alpine
        name: redis-storage
        resources: {}
        volumeMounts:
        - name: redis-storage
          mountPath: /data/redis
      dnsPolicy: ClusterFirst
      restartPolicy: Always
     status: {}
     ```
     
     </details>
 
  3. Run the below command for solution:

     <details>
     <summary>Reveal Solution</summary>

     ```yaml
     apiVersion: v1
     kind: Pod
     metadata:
       creationTimestamp: null
       name: super-user-pod
     spec:
       containers:
       - image: busybox:1.28
         name: super-user-pod
         command: ["sleep", "4800"]
         securityContext:
           capabilities:
             add: ["SYS_TIME"]
     ```
     
     </details>

  4. Run the below command for solution:

     <details>
     <summary>Reveal Solution</summary>
     
     ```yaml
     apiVersion: v1
     kind: PersistentVolumeClaim
     metadata:
       name: my-pvc
     spec:
       accessModes:
         - ReadWriteOnce
       resources:
         requests:
           storage: 10Mi      
     ```
    
     ```yaml
     apiVersion: v1
     kind: Pod
     metadata:
       creationTimestamp: null
       labels:
         run: use-pv
       name: use-pv
     spec:
       containers:
       - image: nginx
         name: use-pv
         volumeMounts:
         - mountPath: "/data"
           name: mypod
       volumes:
       - name: mypod
         persistentVolumeClaim:
           claimName: my-pvc
     ```
     
     </details>

  5. Run the below command for solution:

     <details>
     <summary>Reveal Solution</summary>
 
     For Kubernetes Version <=1.17
 
     ```bash
     kubectl run nginx-deploy --image=nginx:1.16 --replicas=1 --record
     kubectl rollout history deployment nginx-deploy
     kubectl set image deployment/nginx-deploy nginx=nginx:1.17 --record
     kubectl rollout history deployment nginx-deploy
     ```
 
     For Kubernetes Version >1.17
 
     ```yaml
     kubectl create deployment nginx-deploy --image=nginx:1.16 --dry-run=client -o yaml > deploy.yaml
   
     apiVersion: apps/v1
     kind: Deployment
     metadata:
       name: nginx-deploy
     spec:
       replicas: 1
       selector:
         matchLabels:
           app: nginx-deploy
       strategy: {}
       template:
         metadata:
           creationTimestamp: null
           labels:
             app: nginx-deploy
         spec:
           containers:
           - image: nginx:1.16
             name: nginx
     ```
     
     ```bash
     kubectl create -f deploy.yaml --record
     kubectl rollout history deployment nginx-deploy
     kubectl set image deployment/nginx-deploy nginx=nginx:1.17 --record
     kubectl rollout history deployment nginx-deploy
     ```
     
     </details>
  
  6. Run the below command for solution:

     <details>
     <summary>Reveal Solution</summary>
 
     ```yaml
      apiVersion: certificates.k8s.io/v1
      kind: CertificateSigningRequest
      metadata:
        name: john-developer
      spec:
        signerName: kubernetes.io/kube-apiserver-client
        request: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0KTUlJQ1ZEQ0NBVHdDQVFBd0R6RU5NQXNHQTFVRUF3d0VhbTlvYmpDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRApnZ0VQQURDQ0FRb0NnZ0VCQUt2Um1tQ0h2ZjBrTHNldlF3aWVKSzcrVVdRck04ZGtkdzkyYUJTdG1uUVNhMGFPCjV3c3cwbVZyNkNjcEJFRmVreHk5NUVydkgyTHhqQTNiSHVsTVVub2ZkUU9rbjYra1NNY2o3TzdWYlBld2k2OEIKa3JoM2prRFNuZGFvV1NPWXBKOFg1WUZ5c2ZvNUpxby82YU92czFGcEc3bm5SMG1JYWpySTlNVVFEdTVncGw4bgpjakY0TG4vQ3NEb3o3QXNadEgwcVpwc0dXYVpURTBKOWNrQmswZWhiV2tMeDJUK3pEYzlmaDVIMjZsSE4zbHM4CktiSlRuSnY3WDFsNndCeTN5WUFUSXRNclpUR28wZ2c1QS9uREZ4SXdHcXNlMTdLZDRaa1k3RDJIZ3R4UytkMEMKMTNBeHNVdzQyWVZ6ZzhkYXJzVGRMZzcxQ2NaanRxdS9YSmlyQmxVQ0F3RUFBYUFBTUEwR0NTcUdTSWIzRFFFQgpDd1VBQTRJQkFRQ1VKTnNMelBKczB2czlGTTVpUzJ0akMyaVYvdXptcmwxTGNUTStsbXpSODNsS09uL0NoMTZlClNLNHplRlFtbGF0c0hCOGZBU2ZhQnRaOUJ2UnVlMUZnbHk1b2VuTk5LaW9FMnc3TUx1a0oyODBWRWFxUjN2SSsKNzRiNnduNkhYclJsYVhaM25VMTFQVTlsT3RBSGxQeDNYVWpCVk5QaGhlUlBmR3p3TTRselZuQW5mNm96bEtxSgpvT3RORStlZ2FYWDdvc3BvZmdWZWVqc25Yd0RjZ05pSFFTbDgzSkljUCtjOVBHMDJtNyt0NmpJU3VoRllTVjZtCmlqblNucHBKZWhFUGxPMkFNcmJzU0VpaFB1N294Wm9iZDFtdWF4bWtVa0NoSzZLeGV0RjVEdWhRMi80NEMvSDIKOWk1bnpMMlRST3RndGRJZjAveUF5N05COHlOY3FPR0QKLS0tLS1FTkQgQ0VSVElGSUNBVEUgUkVRVUVTVC0tLS0tCg==
        usages:
        - digital signature
        - key encipherment
        - client auth
        groups:
        - system:authenticated
       ```
 
      ```bash
      kubectl certificate approve john-developer
      kubectl create role developer --resource=pods --verb=create,list,get,update,delete --namespace=development
      kubectl create rolebinding developer-role-binding --role=developer --user=john --namespace=development
      kubectl auth can-i update pods --as=john --namespace=development
      ```
  
     </details>
 
  7. Run the below command for solution:

     <details>
     <summary>Reveal Solution</summary>
 
     ```bash
     kubectl run nginx-resolver --image=nginx
     kubectl expose pod nginx-resolver --name=nginx-resolver-service --port=80 --target-port=80 --type=ClusterIP
     kubectl run test-nslookup --image=busybox:1.28 --rm -it --restart=Never -- nslookup nginx-resolver-service
     kubectl run test-nslookup --image=busybox:1.28 --rm -it --restart=Never -- nslookup nginx-resolver-service > /root/CKA/nginx.svc
 
     Get the IP of the nginx-resolver pod and replace the dots(.) with hyphon(-) which will be used below.
 
     kubectl get pod nginx-resolver -o wide
     kubectl run test-nslookup --image=busybox:1.28 --rm -it --restart=Never -- nslookup <P-O-D-I-P.default.pod> > /root/CKA/nginx.pod
 
     ```
 
     </details>

  8. Run the below command for solution:

     <details>
     <summary>Reveal Solution</summary>
 
     ```bash
     kubectl run nginx-critical --image=nginx --dry-run=client -o yaml > static.yaml
     
     cat static.yaml - Copy the contents of this file.
 
     kubectl get nodes -o wide
     ssh node01 
     OR
     ssh <IP of node01>
 
     Check if static-pod directory is present which is /etc/kubernetes/manifests if not then create it.
     mkdir -p /etc/kubernetes/manifests
 
     Paste the contents of the file(static.yaml) copied in the first step to file nginx-critical.yaml.
 
     Move/copy the nginx-critical.yaml to path /etc/kubernetes/manifests/
 
     cp nginx-critical.yaml /etc/kubernetes/manifests
 
     Go back to master node
 
     kubectl get pods 
     ```
 
     </details>

---

## Mock Exam 3 Solutions

1. Run the below command for solution: 

     <details>
     <summary>Reveal Solution</summary>

     ```bash
     kubectl create serviceaccount pvviewer
     kubectl create clusterrole pvviewer-role --resource=persistentvolumes --verb=list
     kubectl create clusterrolebinding pvviewer-role-binding --clusterrole=pvviewer-role --serviceaccount=default:pvviewer
     ```

     ```yaml
     apiVersion: v1
     kind: Pod
     metadata:
       creationTimestamp: null
       labels:
         run: pvviewer
       name: pvviewer
     spec:
       containers:
       - image: redis
         name: pvviewer
         resources: {}
       serviceAccountName: pvviewer
     ```
     
     </details>

2. Run the below command for solution: 

     <details>
     <summary>Reveal Solution</summary>
 
     ```bash
     kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type=="InternalIP")].address}' > /root/CKA/node_ips
     ```
     
     </details>
 
3. Run the below command for solution:  
 
     <details>
     <summary>Reveal Solution</summary>
 
     ```yaml
     apiVersion: v1
     kind: Pod
     metadata:
       name: multi-pod
     spec:
       containers:
       - image: nginx
         name: alpha
         env:
         - name: name
           value: alpha
       - image: busybox
         name: beta
         command: ["sleep", "4800"]
         env:
         - name: name
           value: beta
     status: {}
     ```
     
     </details>
 
4. Run the below command for solution:
 
     <details>
     <summary>Reveal Solution</summary>
     
     ```yaml
     apiVersion: v1
     kind: Pod
     metadata:
       name: non-root-pod
     spec:
       securityContext:
         runAsUser: 1000
         fsGroup: 2000
       containers:
       - name: non-root-pod
         image: redis:alpine
     ```
     
     </details>
 
5. Run the below command for solution:  
 
     <details>
     <summary>Reveal Solution</summary>
 
     ```yaml
     apiVersion: networking.k8s.io/v1
     kind: NetworkPolicy
     metadata:
       name: ingress-to-nptest
       namespace: default
     spec:
       podSelector:
         matchLabels:
           run: np-test-1
       policyTypes:
       - Ingress
       ingress:
       - ports:
         - protocol: TCP
           port: 80
     ```
     
     </details>
   
6. Run the below command for solution: 
 
     <details>
     <summary>Reveal Solution</summary>
 
     ```bash
     kubectl taint node node01 env_type=production:NoSchedule
     ```

     Deploy `dev-redis` pod and to ensure that workloads are not scheduled to this `node01` worker node.
     ```bash
     kubectl run dev-redis --image=redis:alpine

     kubectl get pods -owide
     ```

     Deploy new pod `prod-redis` with toleration to be scheduled on `node01` worker node.
     ```yaml
     apiVersion: v1
     kind: Pod
     metadata:
       name: prod-redis
     spec:
       containers:
       - name: prod-redis
         image: redis:alpine
       tolerations:
       - effect: NoSchedule
         key: env_type
         operator: Equal
         value: production     
     ```

     View the pods with short details: 
     ```bash
     kubectl get pods -owide | grep prod-redis
     ```
     
     </details>
 
7. Run the below command for solution: 
 
     <details>
     <summary>Reveal Solution</summary>
 
     ```bash
     kubectl create namespace hr
     kubectl run hr-pod --image=redis:alpine --namespace=hr --labels=environment=production,tier=frontend
     ```
     
     </details>

8. Run the below command for solution:

     <details>
     <summary>Reveal Solution</summary>

     ```bash
     vi /root/CKA/super.kubeconfig

     Change the 2379 port to 6443 and run the below command to verify
     
     kubectl cluster-info --kubeconfig=/root/CKA/super.kubeconfig     
     ```
     
     </details>

9. Run the below command for solution:
   
     <details>
     <summary>Reveal Solution</summary>
     
     ```bash
     sed -i 's/kube-contro1ler-manager/kube-controller-manager/g' kube-controller-manager.yaml
     ```
     
     </details>

---





#  Section 3: Ultimate Mocks

##  Introduction

NOTE: CKA Ultimate Mocks is a separate course from the main CKA course, and as such requires a separate payment or is included in Pro subscription.

In this section, we will go through some of the most troublesome questions - these being the ones that get the most requests for help on our various forums.


* [Troubleshooting](#cluster-1-orange-pvc-binding-troubleshooting)
* [Storage](#cluster-1-olive-pvc-storage)
* [Services/Networking](#cluster-3-external-webserver-services-networking)
* [General](#cluster-state-jsonpath-questions)

---

## Cluster State & JSONPath Questions

This comes up in both CKA and CKAD tests and is about questions that ask you to write for instance the pods consuming most CPU or most memory to a file, or some other kinds of question such as listing Pod IPs normally using jsonpath or custom columns. These questions are often marked incorrect at the end of the exam and cause much consternation amongst students.

Now the more attentive students may realize why this is the case. If you get such a question near the start of the mock, and then you have questions further on that require you to make deployments into the same cluster, then this is going to change things! The pod that was consuming the most CPU when you answered that question may no longer be the top consumer by the end of the exam, as some newly deployed pod may have a higher CPU usage.

This type of question is about cluster state, and the state of the cluster changes whenever you deploy or delete resources. The marking script can only consider the cluster state after you press `End Exam`. The trick here is to defer answering such questions until you are about to end the exam. Ideally (though this is not always feasible), create a script to answer the question and test it while you are still on the question. Then, when you are about to press the `End Exam` button, run the script again and it will update the file with what the current state is. This should now get the question to pass. In the real exam, you should not have to do this as it is likely that one of the exam clusters is dedicated to such questions so its state won't change by the end of the exam.

## Examples

### Example 1

Store the `pod names` and their `ip addresses` from all namespaces at `/root/pod_ips_ckad02_svcn` where the output is sorted by their IPs.

Please ensure the format as shown below:
```text
POD_NAME        IP_ADDR
pod-1           ip-1
pod-3           ip-2
pod-2           ip-3
...
```
---
From the required output, this clearly requires Custom Columns

1. Work out the custom columns command to get the required output

    Note the use of the `--context` argument here. This ensures the command is run on the correct cluster, irrespective of whether you ran `kubectl config use-context`

    ```bash
    kubectl --context=cluster3 get pods -A -o custom-columns="POD_NAME:.metadata.name,IP_ADDR:.status.podIP" --sort-by=".status.podIP"
    ```

1.  Adjust this to write to the output file and check the output

    ```bash
    kubectl --context=cluster3 get pods -A -o custom-columns="POD_NAME:.metadata.name,IP_ADDR:.status.podIP" --sort-by=".status.podIP" > /root/pod_ips_ckad02_svcn
    ```

    Check it
    ```bash
    cat /root/pod_ips_ckad02_svcn
    ```

1.  Now use `vi` to create a file `run-at-end.sh`

    ```bash
    vi run-at-end.sh
    ```

    Paste the entire kubectl command from above (step 2) into this file. If you have already created this script for a previous similar question, then simply add this line to the file, so the script will answer all such questions when you run it.

1.  Test it

    ```bash
    rm -f /root/pod_ips_ckad02_svcn
    source run-at-end.sh
    cat /root/pod_ips_ckad02_svcn
    ```

    The output should be the same

1.  Finally when you are finished and before pressing `End Exam`, re-run your script

    ```bash
    source run-at-end.sh
    ```

### Example 2

Find the pod that consumes the most CPU and store the result to the file `/opt/high_cpu_pod` in the following format<br/>`cluster_name,namespace,pod_name`.

The pod could be in any namespace in any of the clusters that are currently configured on the student-node.

---

Since it says "in any of the clusters", this will really test your skills of bash scripting, plus `kubectl top` has no JSON output option making it even more difficult to script. Having said that, the best way to solve this question is to write the requirements down on your notepad then answer the question manually at the end before you press `End Exam`. Note that you do not need to navigate back to the question to provide the answer - just do it from your notes.

Use a similar approach whether the stat is CPU or memory, or the resource is Pods or Nodes.

* Manual version
    1. Get all the cluster names

        ```bash
        kubectl config get-contexts -o name
        ```

    1.  Examine the pod usage on each cluster. Run this command with each value for `--context`

        ```bash
        kubectl --context=cluster1 top pods -A --sort-by=cpu
        ```

    1. When you have determined the top pod across all clusters, then you can create the output file in vi and manually add the information in the requested format.

* Scripted version

    Note - To do it this way would probably take longer than you want to spend unless you're already a shell scripting guru!

    ```bash
    for ctx in $(kubectl config get-contexts -o name)
    do
        kubectl --context=$ctx top pod --no-headers -A --sort-by=cpu | head -1 | awk -v ctx=$ctx '{printf "%s,%s,%s,%s\n", ctx, $1, $2, $3}'
    done | sort -t ',' -k4 -h | tail -1 | sed -E 's/,[0-9]+[a-z]*$//i' > /opt/high_cpu_pod
    ```

    There is a lot going on here, isn't there?

    As a working DevOps engineer, this is the sort of thing you would be expected to be able to come up with in your day-to-day job - indeed the lab engineer who developed the marking script for this lab would have to use something like the above! Hence it is important to know how to *use* Linux as well as Kubernetes to be successful in a Kubernetes job. You don't need to know it to Sys Admin level (e.g RHCSA, LFCS).<br/>The following courses are recommended:
    * [Linux Basics](https://kodekloud.com/courses/the-linux-basics-course/)
    * [Shell Scripts for Beginners](https://kodekloud.com/courses/shell-scripts-for-beginners/)
    * [Advanced Bash Scripting](https://kodekloud.com/courses/advanced-bash-scripting/)

    So, what is actually going on?

    1. The `for` loop lists the cluster contexts one by one storing the cluster name in the variable `ctx`
    1. With each context, the `kubectl top pods` command is executed with `-A` for all namespaces...
        1. `--no-headers` removes the column headers from the output.
        1. `--sort-by=cpu` ensures the pod we need from this cluster is the first pod listed. In `kubectl top`, sort order is descending.
        1. Then we pipe the output to `head -1` to get only the first line of results (the top pod for this cluster).
        1. Then we pipe it to `awk` to format the output close to what we need, passing in the cluster name so we can include it in the output. The output will look like this
            ```text
            cluster1,default,frontend-stable-cka05-arch,396m
            ```
    1. After `done` there will be one line like above for each of the clusters. It would look like this, and note they are in cluster order, not CPU usage order:
        ```text
        cluster1,default,frontend-stable-cka05-arch,396m
        cluster2,kube-system,kube-apiserver-cluster2-controlplane,43m
        cluster3,kube-system,metrics-server-7b67f64457-9cqrd,5m
        cluster4,kube-system,kube-apiserver-cluster4-controlplane,32m
        ```
    1. Pipe to `sort` so we get the highest CPU pod *across all clusters* to the end of the list. `sort` works in ascending order.
        1. `-t ','` sets the field separator to be comma.
        1. `-k4` means sort by the fourth field (the one containing the CPU value).
        1. `-h` means "human" sort, taking into account any SI unit (i.e. the `m` for milli-cpu`). The output will now look like this:
            ```text
            cluster3,kube-system,metrics-server-7b67f64457-9cqrd,5m
            cluster4,kube-system,kube-apiserver-cluster4-controlplane,32m
            cluster2,kube-system,kube-apiserver-cluster2-controlplane,43m
            cluster1,default,frontend-stable-cka05-arch,396m
            ```

    1. Pipe to `tail -1` to get the last entry in the sorted list which is the one we need, which will yield
        ```text
        cluster1,default,frontend-stable-cka05-arch,396m
        ```
    1. Finally pipe to `sed` to remove the CPU value and only output the first 3 fields as required by the question. The `sed` expression matches comma, followed by one or more digits, followed by zero or more letters, followed by end of line using extended regex (`-E`) and replaces it with an empty string, thus deleting the matched text. This yields the required output:
        ```text
        cluster1,default,frontend-stable-cka05-arch
        ```
        Then redirect the output to the requested file.

---

## Cluster 3: External Webserver (Services & Networking)

NOTE: This question is also present in the Ultimate CKAD Mocks. The service name is `external-webserver-ckad01-svcn`, however the solution is exactly the same. If you are doing the CKAD version of this question, put instead `external-webserver-ckad01-svcn` everywhere you see `external-webserver-cka03-svcn`.

For this question, please set the context to cluster3 by running:

```bash
kubectl config use-context cluster3
```


We have an **external** webserver running on `student-node` which is exposed at port `9999`. We have created a service called `external-webserver-cka03-svcn` that can connect to our local webserver from within the kubernetes cluster3 but at the moment it is not working as expected.

Fix the issue so that other pods within cluster3 can use `external-webserver-cka03-svcn` service to access the webserver.

---

For this we are told that we need to wire up the service to a web server that's running on `student-node` at port `9999`. Let's verify this. On student node run the following

```bash
curl localhost:9999
```

> Output

```html
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

Yup, it's there!

The important thing to note is that this web server is *outside* of the cluster, therefore the service is going to need to talk to an IP which is not inside the cluster, it is in fact the primary IP address of `student-node`. Let's find that by running the following on `student-node`:

```bash
ifconfig
```

> Output (note that the values you get for each interface will almost certainly be different)

```text
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1450
        inet 192.37.66.3  netmask 255.255.255.0  broadcast 192.37.66.255
        ether 02:42:c0:25:42:03  txqueuelen 0  (Ethernet)
        RX packets 2179  bytes 713082 (713.0 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2361  bytes 391620 (391.6 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.25.0.103  netmask 255.255.255.0  broadcast 172.25.0.255
        ether 02:42:ac:19:00:67  txqueuelen 0  (Ethernet)
        RX packets 36  bytes 8457 (8.4 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 14  bytes 1593 (1.5 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 161  bytes 14395 (14.3 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 161  bytes 14395 (14.3 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

The primary interface is `eth0`. Note down the `inet` value for this interface which in this example is `192.37.66.3`. This is the IP address that our service needs to talk to.

If we now do a `kubectl get service` on `external-webserver-cka03-svcn`, we see there's no pod selector and therefore no endpoints. So isn't "working as expected" since it doesn't have any endpoints.

To wire up the service to the external IP, we must explicitly create an endpoint for the service. Note that the name of the endpoint (`metadata.name`) *must exactly match* the name of the service that you want to associate it to. Here's the endpoint with comments indicating what's what.

```yaml
apiVersion: v1
kind: Endpoints
metadata:
  name: external-webserver-cka03-svcn  # <- Must be same name as the service to associate with
  namespace: default
subsets:
  - addresses:
      - ip: 192.37.66.3  # <- We got this from ifconfig
    ports:
      - port: 9999       # <- Given in the question
```

Create this in a file and `kubectl apply` it.

Now let's test it using a `wbitt/network-multitool` pod that will contain curl so that we can call the service.<br/> TIP - remember this image! It contains many common networking and DNS tools that can be useful in troubleshooting - and yes it can be used in the real exam.

```bash
k run test-pod --image wbitt/network-multitool --restart Never -it -- curl external-webserver-cka03-svcn.default.svc
```

> Output

```html
The directory /usr/share/nginx/html is not mounted.
Therefore, over-writing the default index.html file with some useful information:
WBITT Network MultiTool (with NGINX) - test-pod - 10.42.0.13 - HTTP: 80 , HTTPS: 443 . (Formerly praqma/network-multitool)
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

We got a response - RESULT!

So what we have achieved here is to configure a ClusterIP service that allows pods *inside* the cluster to talk to a service that is *outside* the cluster by way of an explicit endpoint that points to an external IP address. `kube-proxy` takes care of the routing for us.

---

## Cluster 1: olive-pvc (Storage)

For this question, please set the context to `cluster1` by running:


```bash
kubectl config use-context cluster1
```

We want to deploy a python based application on the cluster using a template located at `/root/olive-app-cka10-str`.yaml on `student-node`. However, before you proceed we need to make some modifications to the YAML file as per details given below:


* The YAML should also contain a persistent volume claim with name `olive-pvc-cka10-str` to claim a `100Mi` of storage from `olive-pv-cka10-str PV`.
* Update the deployment to add a sidecar container, which can use `busybox` image (you might need to add a sleep command for this container to keep it running.)
* Share the `python-data` volume with this container and mount the same at path `/usr/src`. Make sure this container only has `read` permissions on this volume.
* Finally, create a pod using this YAML and make sure the POD is in `Running` state.

### Missing from the question, but required to pass

* Create a nodeport service for this deployment with the following specification
    * Node port: `32006`
    * Name: `olive-svc-cka10-str`


---

### Solution

1.  Examine what we have...

    ```bash
    cat /root/olive-app-cka10-str
    ```

    The PVC volume claim is already present. Look for the PVC

    ```bash
    kubectl get pvc
    ```

    It is not present, therefore it will have to be created first.

    ```bash
    kubectl get pv
    ```

    The PV exists. Note the `ACCESS MODES` and `STORAGECLASS`, which are required in the PVC manifest, along with the storage request given in the question.

1.  Prepare manfiest for the new PVC

    ```yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: olive-pvc-cka10-str
    spec:
      accessModes:
      - ReadWriteMany
      resources:
        requests:
          storage: 100Mi
      storageClassName: olive-stc-cka10-str
    ```

    Then create it. It will not bind yet until the pod is created.

1.  Adjust the pod as directed, and add the service to the end.

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: olive-app-cka10-str
    spec:
      replicas: 1
      template:
        metadata:
          labels:
            app: olive-app-cka10-str
        spec:
          affinity:
            nodeAffinity:
              requiredDuringSchedulingIgnoredDuringExecution:
                nodeSelectorTerms:
                - matchExpressions:
                  - key: kubernetes.io/hostname
                    operator: In
                    values:
                      - cluster1-node01
          containers:
          - name: busybox
            image: busybox
            command:        # <- Any variation of sleep command should work.
            - bin/sh        # Needs to sleep long enough to get to end of test.
            - -c
            - sleep 10000
            volumeMounts:
            - mountPath: /usr/src
              name: python-data
              readOnly: true
          - name: python
            image: poroko/flask-demo-app
            ports:
            - containerPort: 5000
            volumeMounts:
            - name: python-data
              mountPath: /usr/share/
          volumes:
          - name: python-data
            persistentVolumeClaim:
              claimName: olive-pvc-cka10-str
      selector:
        matchLabels:
          app: olive-app-cka10-str

    ---

    apiVersion: v1
    kind: Service
    metadata:
      name: olive-svc-cka10-str
      namespace: default
    spec:
      ports:
      - nodePort: 32006
        port: 5000
        protocol: TCP
        targetPort: 5000
      selector:
        app: olive-app-cka10-str
      type: NodePort
    ```

1.  Create the resources

    ```bash
    kubectl apply -f /root/olive-app-cka10-str
    ```

---

## Cluster 1: orange-pvc Binding (Troubleshooting)

For this question, please set the context to cluster1 by running:

```bash
kubectl config use-context cluster1
```

There is an existing persistent volume called orange-pv-cka13-trb. A persistent volume claim called orange-pvc-cka13-trb is created to claim storage from orange-pv-cka13-trb.

However, this PVC is stuck in a Pending state. As of now, there is no data in the volume.

Troubleshoot and fix this issue, making sure that orange-pvc-cka13-trb PVC is in Bound state.

---

### Solution

1. Describe the PVC and determine the issue

    ```bash
    kubectl describe pvc orange-pvc-cka13-trb
    ```

    Note the message "requested PV is too small". We must adjust the PVC to fit

2.  Describe the PV and determine its properties. Note that PVC properties must be adjusted to match

    ```bash
    kubectl describe pv orange-pv-cka13-trb
    ```

3.  Adjust the PVC. Note that you cannot directly edit a PVC size to be smaller, so we have to replace it.

    ```bash
    kubectl get pvc orange-pvc-cka13-trb -o yaml  > pvc.yaml
    vi pvc.yaml
    ```

    Change the requested size to match the size of the PV. Save and exit vi, then replace the PVC with the edited manifest:

    ```bash
    kubectl replace --force -f pvc.yaml
    ```

---

## Cluster 1: NetPol cyan-pod (Troubleshooting)

For this question, please set the context to cluster1 by running:

```bash
kubectl config use-context cluster1
```

One of the nginx based pod called `cyan-pod-cka28-trb` is running under `cyan-ns-cka28-trb` namespace and it is exposed within the cluster using `cyan-svc-cka28-trb` service.

This is a restricted pod so a network policy called `cyan-np-cka28-trb` has been created in the same namespace to apply some restrictions on this pod.

Two other pods called `cyan-white-cka28-trb1` and `cyan-black-cka28-trb` are also running in the default namespace.

The nginx based app running on the `cyan-pod-cka28-trb` pod is exposed internally on the default nginx port (80).

**Expectation**: This app should only be accessible from the `cyan-white-cka28-trb` pod.

**Problem**: This app is not accessible from anywhere.

Troubleshoot this issue and fix the connectivity as per the requirement listed above.

Note: You can exec into `cyan-white-cka28-trb` and `cyan-black-cka28-trb` pods and test connectivity using the curl utility.

You may update the network policy, but make sure it is not deleted from the `cyan-ns-cka28-trb` namespace.

---

### Update - Intermittent lab bug!

The solution given below is correct, however in some instances it doesn't work due to an intermittent bug in the installation of Weave to the lab environment found by a very astute community member in [this thread](https://kodekloud.com/community/t/network-policy-blocking-all-the-ingress-traffic/300501/15?u=alistair_kodekloud) on the community forum.

TL;DR - To detect the presence of this bug, run the following two commands. Bonus - see if you can understand how they work! Note that the first one is split across multiple lines with `\` for legibility. This is a valid construct in shell script.

```bash
kubectl exec -n kube-system \
   $(kubectl get po -n kube-system --selector name=weave-net -o jsonpath='{.items[0].metadata.name}') \
   -c weave -- printenv | grep IPALLOC

kubectl get configmap -n kube-system kube-proxy -o jsonpath={'.data.config\.conf}' | yq e .clusterCIDR -
```

Both should report the same CIDR range, e.g. `10.244.0.0/16`. If they are not both the same (doesn't matter what they actually are, but must be the same), then the lab has the bug. Should you encounter this (netpol not working even though you have followed the solution below), then practice your skills of [manual pod scheduling](../../Reference%20Notes/0-13_scheduling_logging_and_lifecycle.md#a-manual-scheduling-bypassing-the-scheduler), and get all three concerned pods to restart on the same worker node (choose either node). Then the netpol should take effect.




### Solution

First, let's examine the policy we have

```bash
k get netpol -n cyan-ns-cka28-trb cyan-np-cka28-trb -o yaml
```

> Output. (The additional metadata is omitted as it is different every time)

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: cyan-np-cka28-trb
  namespace: cyan-ns-cka28-trb
spec:
  egress:
  - ports:
    - port: 8080
      protocol: TCP
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: default
    ports:
    - port: 8080
      protocol: TCP
  podSelector:
    matchLabels:
      app: cyan-app-cka28-trb
  policyTypes:
  - Ingress
  - Egress
status: {}
```

The egress policy you find here is a [red herring](https://dictionary.cambridge.org/dictionary/english/red-herring). Since we are not concerned with egress from the nginx pod, only ingress to it from the other pods, then it does not feature in the solution to this problem so you can ignore it.

There are two issues that need fixing here. You can modify the policy and make both these changes with a single invocation of:

```bash
kubectl edit netpol -n cyan-ns-cka28-trb cyan-np-cka28-trb
```

1. The reason nothing can connect at the start is that the ingress port 8080 in the netpol is wrong. It should be 80. Why? We are told in the question that the nginx app in the pod to which the policy applies is listening on the default port `80`. Therefore the *ingress* port needs to be `80` and not `8080`. Fix this.
1. Now that’s fixed, everything in default namespace now has access to the pod on port 80, and curl will return the nginx default message. Thus we need to add to the rule a podSelector to ensure the incoming traffic can only come from the nominated pod in the default namespace, so it’s an AND rule.

The finished product is this. Again I have omitted the additional metadata but you can leave it in. Save and exit `vi` so the changes are applied.

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: cyan-np-cka28-trb
  namespace: cyan-ns-cka28-trb
spec:
  egress:
  - ports:
    - port: 8080
      protocol: TCP
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: default
      podSelector:      # <- This was added. No dash before podSelector!
        matchLabels:
          app: cyan-white-cka28-trb
    ports:
    - port: 80          # <- This was edited
      protocol: TCP
  podSelector:
    matchLabels:
      app: cyan-app-cka28-trb
  policyTypes:
  - Ingress
  - Egress
```

Note the fact that there must be no `-` before the podSelector that we added. If we put a `-` then the rule would operate as follows

> **ALLOW** any pod in namespace `default` **OR** any pod in any namespace with label `app=cyan-white-cka28-trb`

That would also permit `cyan-black-cka28-trb` to access, which is incorrect! Without the `-`, the rule operates correctly as follows

> **ALLOW** any pod in namespace `default` **THAT HAS** label `app=cyan-white-cka28-trb`

Which basically means pods in namespace `default` **AND** with correct labels.

Let's test this. We will use the `--connect-timeout` argument for `curl` so as not to wait too long for the expected failed connection from the black pod.

```bash
k exec -n default cyan-white-cka28-trb -it -- curl --connect-timeout 10 cyan-svc-cka28-trb.cyan-ns-cka28-trb.svc
```

> Output

```html
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

```bash
k exec -n default cyan-black-cka28-trb -it -- curl --connect-timeout 10 cyan-svc-cka28-trb.cyan-ns-cka28-trb.svc
```

> Output

```text
curl: (28) Connection timeout after 10000 ms
command terminated with exit code 28
```

White pod connects, black pod does not - RESULT!

---


# Section 4: Network Policy Testing Tips

## Introduction

In this bonus section we will discuss some useful tips that can be used preparation for the exam

- [01-Server for testing network policies](#servers-for-testing-network-policies)
- [02-Client-for-testing-network-things](#clients-for-testing-network-dns)

---

## Servers for Testing Network Policies

Sometimes you may have a question that asks you to block ingress to a pod on all but some specific port. If a pod that meets the port requirement is not already present in the given namespace, then the issue here is "How do I create a pod onto which to attach the netpol that listens on the given port so I can test the policy?". You can't just run an nginx pod as that always listens on port 80. You could configure it otherwise, but that would require you to mount a configmap into the nginx pod containing an alternate config for nginx with the new port number. That's far too much hassle under exam conditions!

## Simple server

Fortunately, the default Python distribution contains a simple server that can have its port number configured from the command line, meaning you can run it imperatively. Let's say the network policy requires blocking all but port 9000. We can start a server test pod to listen on 9000 like so. If it's a different port, just put that port number instead of 9000.

```bash
kubectl run server --image python --command -- python -m http.server 9000
```

Get the pod's IP address. Using the IP for curl test is quicker than typing out the DNS name.

```bash
controlplane $ k get pod server -o wide
NAME     READY   STATUS    RESTARTS   AGE   IP             NODE     NOMINATED NODE   READINESS GATES
server   1/1     Running   0          16s   192.168.1.12   node01   <none>           <none>
```

Now run a pod with `curl` in and test connection to the server

```bash
curl 192.168.1.12:9000
```

You should get a response.

Now apply your network policy and test again.

## Slightly more advanced server

Perhaps you want to set up several pods and have each serve a specific message on a configurable port so you can tell them apart by their reponses. We can do that with a pod and a config map for each. The pod is the same each time - except for giving it a unique name and mounting the appropriate config map.

The following simulates a pod found in one of the Killer.sh network policy questions.

1. Create a config map which contains a shell script to run the server on a given port with a given message

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
    name: db1-configmap
    data:
    entrypoint.sh: |
      #!/bin/sh
      echo "database one" > index.htm  #<- Message
      port=1111                        #<- Server Port
      # Run server...
      while true
      do
          { echo -ne "HTTP/1.0 200 OK\r\nContent-Length: $(wc -c <index.htm)\r\n\r\n"; cat index.htm; } | nc -l -p $port
      done
    ```
1. Create a pod that mounts the configmap and runs the script it contains

    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
    name: db-1
    spec:
    containers:
    - name: server
        image: alpine:3.19
        command:
        - /opt/server/entrypoint.sh
        volumeMounts:
        - name: script
        mountPath: /opt/server
    volumes:
    - name: script
        configMap:
        name: db1-configmap
        defaultMode: 0755
    ```
1. Get the pod's IP address. Using the IP for curl test is quicker than typing out the DNS name.

    ```bash
    controlplane $ k get pod server -o wide
    NAME     READY   STATUS    RESTARTS   AGE   IP             NODE     NOMINATED NODE   READINESS GATES
    db-1     1/1     Running   0          16s   192.168.1.12   node01   <none>           <none>
    ```

1. Now run a pod with `curl` in and test connection to the server

    ```bash
    curl 192.168.1.12:1111
    ```


## See also

See also [client for testing](#clients-for-testing-network-dns)

---

## Clients for Testing Network & DNS

Often you will get questions that require you to test network polices, or look something up in the Kubernetes DNS. There is a one size fits all pod that you can deploy that has all the network testing tools you could possibly want, including

* curl
* nslookup
* netstat
* dig
* telnet
* nc

and many more.

You run it like so. Commit the image name to memory - this image is a lifesaver! There is nothing to stop you using it in the exam.

```bash
kubectl run tester --image wbitt/network-multitool
```

When the pod is running, you can exec into it and run the commands

```bash
$ kubectl exec tester -it -- bash

/# curl something
/# nslookup something-else
/# exit
```

Or run the commands directly if you need to send the results to a file

```bash
$ kubectl exec tester -it -- nslookup my-service.default.svc > /opt/some-file.txt
```

---

# Section 5: Ultimate Mock Exams & High-Density Exam Scenarios

This section focuses on advanced scenarios encountered in the Ultimate Mock Exam series, simulating complex multi-cluster context transitions, container runtime bootstrapping, autoscaler optimization, modern routing interfaces (Gateway API), and Helm lifecycle operations.

---

## 1. Multi-Cluster Context Navigation & Boundary Traversal
In high-density exam environments, operations are performed across multiple distinct clusters. You must explicitly verify and set context boundaries before executing tasks.

### A. Context Mapping & Auditing Commands
* **Retrieve All Available Clusters:**
  ```bash
  kubectl config get-clusters
  ```
* **Retrieve All Configured Contexts:**
  ```bash
  kubectl config get-contexts
  ```
* **Switch Active Context:**
  ```bash
  kubectl config use-context cluster3
  ```

### B. Node SSH & Privilege Escalation
In multiple cluster topologies, the main terminal runs on a central client node (`student-node`). Direct host access requires traversing the network boundary:
1. **SSH to Target Node:**
   ```bash
   ssh Bob@node01
   ```
2. **Escalate to root Privileges:**
   ```bash
   sudo -i
   # Or switch shell user:
   sudo su
   ```

---

## 2. Advanced Autoscaling & Traffic Routing Manifests

### A. Horizontal Pod Autoscaler (HPA) with Stabilization Window
Scale down rules can cause rapid fluctuations ("thrashing" or "flapping") when traffic drops briefly. To cautiously scale down pods, implement a `behavior` block specifying a stabilization window:

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: webapp-hpa
  namespace: default
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: kkapp-deploy
  minReplicas: 1
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 50
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300 # Wait 5 minutes before reclaiming replicas
```

### B. Vertical Pod Autoscaler (VPA) with Auto-recreate
Unlike HPA (which adds replicas), VPA adjusts the resource limits (CPU/Memory) of existing containers. When set to `Auto` mode, VPA is permitted to evict and recreate pods to apply the new resources:

```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: analytics-vpa
  namespace: default
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: analytics-deployment
  updatePolicy:
    updateMode: Auto # Automatically evicts and redeploys pods with resized specifications
```

### C. Gateway API Resource (Modern Ingress Alternative)
The Gateway API separates configuration responsibilities between cluster operators (provisioning infrastructure Gateways) and application developers (defining routing paths via HTTPRoutes).

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: web-gateway
  namespace: nginx-gateway
spec:
  gatewayClassName: nginx # Maps to the ingress controller GatewayClass implementation
  listeners:
  - name: http
    protocol: HTTP
    port: 80
    allowedRoutes:
      namespaces:
        from: Same
```

---

## 3. Helm Client-Side Release Lifecycle
During local application audits, you must fetch remote chart modifications and apply upgrades using the `helm` client:

1. **List Active Releases in a Specific Namespace:**
   ```bash
   helm list -n kk-ns
   ```
2. **Update Remote Repositories:** Fetch the latest chart version definitions:
   ```bash
   helm repo update
   ```
3. **Search for All Available Versions of a Chart:**
   ```bash
   helm search repo nginx --versions
   ```
4. **Upgrade an Existing Release to a Mapped Version:**
   ```bash
   helm upgrade kk-mock1 kk-mock1/nginx --version 18.1.5 -n kk-ns
   ```

---

## 4. Quick-Fire Hands-On Diagnostic Playbooks

### Scenario A: Secret Metadata Retrieval & Base64 Decoding
* **Goal:** Extract an encrypted database password from a secret in namespace `prod` and write the decrypted text to `/root/db-password.txt` on the student node.
* **CLI Command:**
  ```bash
  kubectl get secret beta-sec-cka14-arch -n prod -o jsonpath='{.data.password}' | base64 -d > /root/db-password.txt
  ```

### Scenario B: Bare-Metal Container Runtime (cri-dockerd) Bootstrapping
* **Goal:** Install and enable a container runtime package (`cri-docker`) on a worker node.
* **Playbook:**
  1. SSH to the target worker node and escalate to root:
     ```bash
     ssh Bob@node01
     sudo -i
     ```
  2. Install the local Debian package using `dpkg`:
     ```bash
     dpkg -i /root/cri-dockerd_*.deb
     ```
  3. Start the systemd service and configure it to run persistently on system boot:
     ```bash
     systemctl start cri-docker
     systemctl enable cri-docker
     ```
  4. Verify the active status:
     ```bash
     systemctl is-enabled cri-docker && systemctl status cri-docker
     ```

### Scenario C: Init Container Command Typo Crash-Loops
* **Goal:** Resolve a pod stuck in `Init:CrashLoopBackOff` or `Init:Error`.
* **Playbook:**
  1. Fetch the logs of the crashing init container:
     ```bash
     kubectl logs orange -c init-my-service
     # Resulting error: "sleeeep: command not found" (typo in sleep binary)
     ```
  2. Export the pod manifest:
     ```bash
     kubectl get pod orange -o yaml > orange.yaml
     ```
  3. Edit `orange.yaml` using `vi`/`sed` to change `sleeeep` to `sleep`.
  4. Force replace the immutable pod:
     ```bash
     kubectl replace --force -f orange.yaml
     ```

### Scenario D: Service NodePort Custom Port Assignment
* **Goal:** Expose the `hr-web-app` deployment on a static NodePort `30082`.
* **Playbook:**
  1. Imperatively generate the service template manifest:
     ```bash
     kubectl expose deployment hr-web-app --type=NodePort --port=8080 --name=hr-web-app-service --dry-run=client -o yaml > svc.yaml
     ```
  2. Add `nodePort: 30082` under the service ports spec inside `svc.yaml`:
     ```yaml
     spec:
       ports:
       - port: 8080
         protocol: TCP
         targetPort: 8080
         nodePort: 30082 # <-- Add this static port mapping
     ```
  3. Apply the resource:
     ```bash
     kubectl apply -f svc.yaml
     ```

### Scenario E: HostPath Persistent Volume Setup
* **Goal:** Provision a local-host persistent volume `pv-analytics` mapping to directory `/pv/data-analytics`.
* **PV Manifest (`pv.yaml`):**
  ```yaml
  apiVersion: v1
  kind: PersistentVolume
  metadata:
    name: pv-analytics
  spec:
    capacity:
      storage: 100Mi
    volumeMode: Filesystem
    accessModes:
      - ReadWriteMany
    hostPath:
      path: /pv/data-analytics
  ```
* **Apply Command:**
  ```bash
  kubectl apply -f pv.yaml
  ```

### Scenario F: Custom Resource Definition (CRD) Metadata Auditing
* **Goal:** Save the names of all Vertical Pod Autoscaler CRDs present in the cluster to `/root/vpa-crds.txt`.
* **CLI Command:**
  ```bash
  kubectl get crd | grep -i vertical | awk '{print $1}' > /root/vpa-crds.txt
  ```

---


