What is the primary purpose of the `ImagePolicyWebhook` admission controller?

The `ImagePolicyWebhook` admission controller intercepts pod creation requests and consults an external webhook service to determine whether the container images specified in the pod spec should be allowed or denied.

In this lab, you will configure an `ImagePolicyWebhook` admission controller to work with a container image scanner.

A functional container image scanner is already deployed with the HTTPS endpoint:  
`https://image-checker-webhook.default.svc:1323/image_policy`

An incomplete configuration exists at `/etc/kubernetes/imgvalidation`.


controlplane /etc/kubernetes/imgvalidation ➜  cat admission-configuration.yaml 
apiVersion: apiserver.config.k8s.io/v1
kind: AdmissionConfiguration
plugins:
  - name: ImagePolicyWebhook
    path: /etc/kubernetes/imgvalidation/imagepolicy-conf.yaml


cat imagepolicy-conf.yaml 
imagePolicy:
  kubeConfigFile: /etc/kubernetes/imgvalidation/kubeconf.yaml
  allowTTL: 50
  denyTTL: 50
  retryBackoff: 500
  defaultAllow: true


at kubeconf.yaml 
apiVersion: v1
kind: Config
clusters:
- cluster:
    certificate-authority: /etc/kubernetes/imgvalidation/webhook.crt
    server: https://placeholder.example.com
  name: checker_webhook
contexts:
- context:
    cluster: checker_webhook
    user: api-server
  name: checker_validator
current-context: checker_validator
preferences: {}
users:
- name: api-server
  user:
    client-certificate: /etc/kubernetes/pki/front-proxy-client.crt
    client-key: /etc/kubernetes/pki/front-proxy-client.key


Reconfigure the API server to enable the `ImagePolicyWebhook` admission plugin and ensure it can access the configuration files.

  

ImagePolicyWebhook admission plugin enabled on kube-apiserver?

admission-control-config-file flag set on kube-apiserver?

imgvalidation volume mounted in kube-apiserver?


This link contains parameters passed in kube-apiserver container commands to use the admission controller

https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/#options