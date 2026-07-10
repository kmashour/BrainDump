A Note on Secrets

Remember that secrets encode data in base64 format. Anyone with the base64 encoded secret can easily decode it. As such the secrets can be considered as not very safe.

The concept of safety of the Secrets is a bit confusing in Kubernetes. The [kubernetes documentation](https://kubernetes.io/docs/concepts/configuration/secret) page and a lot of blogs out there refer to secrets as a "safer option" to store sensitive data. They are safer than storing in plain text as they reduce the risk of accidentally exposing passwords and other sensitive data. In my opinion it's not the secret itself that is safe, it is the practices around it. 

Secrets are not encrypted, so it is not safer in that sense. However, some best practices around using secrets make it safer. As in best practices like:

- Not checking-in secret object definition files to source code repositories.
    
- [Enabling Encryption at Rest](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/) for Secrets so they are stored encrypted in ETCD. 
    

  

Also the way kubernetes handles secrets. Such as:

- A secret is only sent to a node if a pod on that node requires it.
    
- Kubelet stores the secret into a tmpfs so that the secret is not written to disk storage.
    
- Once the Pod that depends on the secret is deleted, kubelet will delete its local copy of the secret data as well.
    

Read about the [protections](https://kubernetes.io/docs/concepts/configuration/secret/#protections) and [risks](https://kubernetes.io/docs/concepts/configuration/secret/#risks) of using secrets [here](https://kubernetes.io/docs/concepts/configuration/secret/#risks)

  

Having said that, there are other better ways of handling sensitive data like passwords in Kubernetes, such as using tools like Helm Secrets, [HashiCorp Vault](https://www.vaultproject.io/). I hope to make a lecture on these in the future.

---

## 🌐 Scraped Reference Content

> [!NOTE]
> The content below has been automatically scraped from official documentation and related sub-links for deeper context.

### 📄 Source: [https://kubernetes.io/docs/concepts/configuration/secret](https://kubernetes.io/docs/concepts/configuration/secret)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.36   - v1.35   - v1.34   - v1.33   - v1.32 - English 
  - 中文 (Chinese)   - Français (French)   - Deutsch (German)   - Bahasa Indonesia (Indonesian)   - 日本語 (Japanese)   - 한국어 (Korean)   - Português (Portuguese)   - Español (Spanish)   - Tiếng Việt (Vietnamese)   - বাংলা (Bengali)   - हिन्दी (Hindi)   - Italiano (Italian)   - فارسی (Persian)   - Polski (Polish)   - Русский (Russian)   - Українська (Ukrainian) - 
  - Light   - Dark   - Auto 
# Secrets 
- - - - - - - - - - - - - - - - 
- 
  - 
    -   - 
    -     - 
      -       - 
        - 
          -           -           -           -           -           -           -           -           -       -     - 
      -       -       -       -       -   - 
    - 
      -       - 
        -         -         -         -         -         -         -         -         -         -       -       -     - 
      -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -     - 
      - 
        -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -         -         -       - 
        -         -         -         -         -         -         -         -       - 
        -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -     - 
      - 
        -         -       - 
        -         -       -   - 
    - 
      -       -       -     - 
      - 
        -         -         -         -         -         -         -         -         -       -       - 
        -         -         -         -         -       -       - 
        -         -         -         -         -         -       - 
        -         -         -         -         -         -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       - 
        -         -         -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       - 
        -         -         -         -         -         -         -       - 
        -         -         -         -         -         -         -         -         -         -     - 
      -       -       -       -       -       -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -     - 
      -       - 
        -         -       -       -       -       -       -     - 
      -       -       -       -     - 
      -       -       -       -     - 
      -       -       -       -     -     -     -   - 
    -     - 
      - 
        -       - 
        -       - 
        -       - 
        -       - 
        -       - 
        -     - 
      -       -       -       -     - 
      -       -       -       -     - 
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -     - 
      -       - 
        -         -         -         -         -         -       - 
        -       - 
        -       - 
        -       - 
        -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -       - 
        -         -       - 
        -       - 
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
        -         -         -         -         -         -       - 
        -     - 
      -       -       -       -       -       -       -     - 
      -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -     - 
      - 
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -     - 
      -       -       - 
        -         -         -         -         - 
          -           -           -         -         - 
          -           -           -         -         - 
          -           -         - 
          -         -         - 
          -           -           -           -           -           -           -           -           -           -           -           -           -           -           -         -         -         - 
          -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -         -         -         -         -         -         -         -         -         -         -         -         - 
          -           -         -         -         -         -         -         - 
          -         -         -         -         - 
          -           -           -           -           -           -         -         -         - 
          -           -           -           -           -           -         -         - 
          -           -         -         -         -       -       -       -       -       -       -     - 
      -     - 
      -       -       -       -       -       -       -     - 
      -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -     -     -   - 
- 
  -   -   - - 
  -   -   -   -   -   -   - - 
  -   -   -   -   -   -   - - 
  - - 
  - - 
- - - - 
# Secrets 
A Secret is an object that contains a small amount of sensitive data such as a password, a token, or a key. Such information might otherwise be put in a Pod specification or in a container image . Using a Secret means that you don't need to include confidential data in your application code. 
Because Secrets can be created independently of the Pods that use them, there is less risk of the Secret (and its data) being exposed during the workflow of creating, viewing, and editing Pods. Kubernetes, and applications that run in your cluster, can also take additional precautions with Secrets, such as avoiding writing sensitive data to nonvolatile storage. 
Secrets are similar to ConfigMaps but are specifically intended to hold confidential data. 
#### Caution: 
Kubernetes Secrets are, by default, stored unencrypted in the API server's underlying data store (etcd). Anyone with API access can retrieve or modify a Secret, and so can anyone with access to etcd. Additionally, anyone who is authorized to create a Pod in a namespace can use that access to read any Secret in that namespace; this includes indirect access such as the ability to create a Deployment. 
In order to safely use Secrets, take at least the following steps: 
- Enable Encryption at Rest for Secrets. - Enable or configure RBAC rules with least-privilege access to Secrets. - Restrict Secret access to specific containers. - Consider using external Secret store providers . 
For more guidelines to manage and improve the security of your Secrets, refer to Good practices for Kubernetes Secrets . 
See Information security for Secrets for more details. 
## Uses for Secrets 
You can use Secrets for purposes such as the following: 
- Set environment variables for a container . - Provide credentials such as SSH keys or passwords to Pods . - Allow the kubelet to pull container images from private registries . 
The Kubernetes control plane also uses Secrets; for example, bootstrap token Secrets are a mechanism to help automate node registration. 
### Use case: dotfiles in a secret volume 
You can make your data "hidden" by defining a key that begins with a dot. This key represents a dotfile or "hidden" file. For example, when the following Secret is mounted into a volume, secret-volume, the volume will contain a single file, called .secret-file, and the dotfile-test-containerwill have this file present at the path /etc/secret-volume/.secret-file. 
#### Note: Files beginning with dot characters are hidden from the output of ls -l; you must use ls -lato see them when listing directory contents. secret/dotfile-secret.yaml
```
apiVersion:v1kind:Secretmetadata:name:dotfile-secretdata:.secret-file:dmFsdWUtMg0KDQo=---apiVersion:v1kind:Podmetadata:name:secret-dotfiles-podspec:volumes:- name:secret-volumesecret:secretName:dotfile-secretcontainers:- name:dotfile-test-containerimage:registry.k8s.io/busyboxcommand:- ls- "-l"- "/etc/secret-volume"volumeMounts:- name:secret-volumereadOnly:truemountPath:"/etc/secret-volume"
```

### Use case: Secret visible to one container in a Pod 
Consider a program that needs to handle HTTP requests, do some complex business logic, and then sign some messages with an HMAC. Because it has complex application logic, there might be an unnoticed remote file reading exploit in the server, which could expose the private key to an attacker. 
This could be divided into two processes in two containers: a frontend container which handles user interaction and business logic, but which cannot see the private key; and a signer container that can see the private key, and responds to simple signing requests from the frontend (for example, over localhost networking). 
With this partitioned approach, an attacker now has to trick the application server into doing something rather arbitrary, which may be harder than getting it to read a file. 
### Alternatives to Secrets 
Rather than using a Secret to protect confidential data, you can pick from alternatives. 
Here are some of your options: 
- If your cloud-native component needs to authenticate to another application that you know is running within the same Kubernetes cluster, you can use a ServiceAccount and its tokens to identify your client. - There are third-party tools that you can run, either within or outside your cluster, that manage sensitive data. For example, a service that Pods access over HTTPS, that reveals a Secret if the client correctly authenticates (for example, with a ServiceAccount token). - For authentication, you can implement a custom signer for X.509 certificates, and use CertificateSigningRequests to let that custom signer issue certificates to Pods that need them. - You can use a device plugin to expose node-local encryption hardware to a specific Pod. For example, you can schedule trusted Pods onto nodes that provide a Trusted Platform Module, configured out-of-band. 
You can also combine two or more of those options, including the option to use Secret objects themselves. 
For example: implement (or deploy) an operator that fetches short-lived session tokens from an external service, and then creates Secrets based on those short-lived session tokens. Pods running in your cluster can make use of the session tokens, and operator ensures they are valid. This separation means that you can run Pods that are unaware of the exact mechanisms for issuing and refreshing those session tokens. 
## Types of Secret 
When creating a Secret, you can specify its type using the typefield of the Secret resource, or certain equivalent kubectlcommand line flags (if available). The Secret type is used to facilitate programmatic handling of the Secret data. 
Kubernetes provides several built-in types for some common usage scenarios. These types vary in terms of the validations performed and the constraints Kubernetes imposes on them. 
|  Built-in Type  | Usage  |
|  Opaque | arbitrary user-defined data  |
|  kubernetes.io/service-account-token | ServiceAccount token  |
|  kubernetes.io/dockercfg | serialized ~/.dockercfgfile  |
|  kubernetes.io/dockerconfigjson | serialized ~/.docker/config.jsonfile  |
|  kubernetes.io/basic-auth | credentials for basic authentication  |
|  kubernetes.io/ssh-auth | credentials for SSH authentication  |
|  kubernetes.io/tls | data for a TLS client or server  |
|  bootstrap.kubernetes.io/token | bootstrap token data  |
You can define and use your own Secret type by assigning a non-empty string as the typevalue for a Secret object (an empty string is treated as an Opaquetype). 
Kubernetes doesn't impose any constraints on the type name. However, if you are using one of the built-in types, you must meet all the requirements defined for that type. 
If you are defining a type of Secret that's for public use, follow the convention and structure the Secret type to have your domain name before the name, separated by a /. For example: cloud-hosting.example.net/cloud-api-credentials. 
### Opaque Secrets 
Opaqueis the default Secret type if you don't explicitly specify a type in a Secret manifest. When you create a Secret using kubectl, you must use the genericsubcommand to indicate an OpaqueSecret type. For example, the following command creates an empty Secret of type Opaque: 
```
kubectl create secret generic empty-secret
kubectl get secret empty-secret

```

The output looks like: 
```
NAME           TYPE     DATA   AGE
empty-secret   Opaque   0      2m6s

```

The DATAcolumn shows the number of data items stored in the Secret. In this case, 0means you have created an empty Secret. 
### ServiceAccount token Secrets 
A kubernetes.io/service-account-tokentype of Secret is used to store a token credential that identifies a ServiceAccount . This is a legacy mechanism that provides long-lived ServiceAccount credentials to Pods. 
In Kubernetes v1.22 and later, the recommended approach is to obtain a short-lived, automatically rotating ServiceAccount token by using the TokenRequestAPI instead. You can get these short-lived tokens using the following methods: 
- Call the TokenRequestAPI either directly or by using an API client like kubectl. For example, you can use the kubectl create tokencommand. - Request a mounted token in a projected volume in your Pod manifest. Kubernetes creates the token and mounts it in the Pod. The token is automatically invalidated when the Pod that it's mounted in is deleted. For details, see Launch a Pod using service account token projection . 
#### Note: You should only create a ServiceAccount token Secret if you can't use the TokenRequestAPI to obtain a token, and the security exposure of persisting a non-expiring token credential in a readable API object is acceptable to you. For instructions, see Manually create a long-lived API token for a ServiceAccount . 
When using this Secret type, you need to ensure that the kubernetes.io/service-account.nameannotation is set to an existing ServiceAccount name. If you are creating both the ServiceAccount and the Secret objects, you should create the ServiceAccount object first. 
After the Secret is created, a Kubernetes controller fills in some other fields such as the kubernetes.io/service-account.uidannotation, and the tokenkey in the datafield, which is populated with an authentication token. 
The following example configuration declares a ServiceAccount token Secret: secret/serviceaccount-token-secret.yaml
```
apiVersion:v1kind:Secretmetadata:name:secret-sa-sampleannotations:kubernetes.io/service-account.name:"sa-name"type:kubernetes.io/service-account-tokendata:extra:YmFyCg==
```

After creating the Secret, wait for Kubernetes to populate the tokenkey in the datafield. 
See the ServiceAccount documentation for more information on how ServiceAccounts work. You can also check the automountServiceAccountTokenfield and the serviceAccountNamefield of the Podfor information on referencing ServiceAccount credentials from within Pods. 
### Docker config Secrets 
If you are creating a Secret to store credentials for accessing a container image registry, you must use one of the following typevalues for that Secret: 
- kubernetes.io/dockercfg: store a serialized ~/.dockercfgwhich is the legacy format for configuring Docker command line. The Secret datafield contains a .dockercfgkey whose value is the content of a base64 encoded ~/.dockercfgfile. - kubernetes.io/dockerconfigjson: store a serialized JSON that follows the same format rules as the ~/.docker/config.jsonfile, which is a new format for ~/.dockercfg. The Secret datafield must contain a .dockerconfigjsonkey for which the value is the content of a base64 encoded ~/.docker/config.jsonfile. 
Below is an example for a kubernetes.io/dockercfgtype of Secret: secret/dockercfg-secret.yaml
```
apiVersion:v1kind:Secretmetadata:name:secret-dockercfgtype:kubernetes.io/dockercfgdata:.dockercfg:|    eyJhdXRocyI6eyJodHRwczovL2V4YW1wbGUvdjEvIjp7ImF1dGgiOiJvcGVuc2VzYW1lIn19fQo=
```

#### Note: If you do not want to perform the base64 encoding, you can choose to use the stringDatafield instead. 
When you create Docker config Secrets using a manifest, the API server checks whether the expected key exists in the datafield, and it verifies if the value provided can be parsed as a valid JSON. The API server doesn't validate if the JSON actually is a Docker config file. 
You can also use kubectlto create a Secret for accessing a container registry, such as when you don't have a Docker configuration file: 
```
kubectl create secret docker-registry secret-tiger-docker \
  --docker-email=tiger@acme.example \
  --docker-username=tiger \
  --docker-password=pass1234 \
  --docker-server=my-registry.example:5000

```

This command creates a Secret of type kubernetes.io/dockerconfigjson. 
Retrieve the .data.dockerconfigjsonfield from that new Secret and decode the data: 
```
kubectl get secret secret-tiger-docker -o jsonpath='{.data.*}'| base64 -d

```

The output is equivalent to the following JSON document (which is also a valid Docker configuration file): 
```
{"auths":{"my-registry.example:5000":{"username":"tiger","password":"pass1234","email":"tiger@acme.example","auth":"dGlnZXI6cGFzczEyMzQ="}}}
```

#### Caution: 
The authvalue there is base64 encoded; it is obscured but not secret. Anyone who can read that Secret can learn the registry access bearer token. 
It is suggested to use credential providers to dynamically and securely provide pull secrets on-demand. 
### Basic authentication Secret 
The kubernetes.io/basic-authtype is provided for storing credentials needed for basic authentication. When using this Secret type, the datafield of the Secret must contain one of the following two keys: 
- username: the user name for authentication - password: the password or token for authentication 
Both values for the above two keys are base64 encoded strings. You can alternatively provide the clear text content using the stringDatafield in the Secret manifest. 
The following manifest is an example of a basic authentication Secret: secret/basicauth-secret.yaml
```
apiVersion:v1kind:Secretmetadata:name:secret-basic-authtype:kubernetes.io/basic-authstringData:username:admin# required field for kubernetes.io/basic-authpassword:t0p-Secret# required field for kubernetes.io/basic-auth
```

#### Note: The stringDatafield for a Secret does not work well with server-side apply. 
The basic authentication Secret type is provided only for convenience. You can create an Opaquetype for credentials used for basic authentication. However, using the defined and public Secret type ( kubernetes.io/basic-auth) helps other people to understand the purpose of your Secret, and sets a convention for what key names to expect. 
### SSH authentication Secrets 
The builtin type kubernetes.io/ssh-authis provided for storing data used in SSH authentication. When using this Secret type, you will have to specify a ssh-privatekeykey-value pair in the data(or stringData) field as the SSH credential to use. 
The following manifest is an example of a Secret used for SSH public/private key authentication: secret/ssh-auth-secret.yaml
```
apiVersion:v1kind:Secretmetadata:name:secret-ssh-authtype:kubernetes.io/ssh-authdata:# the data is abbreviated in this examplessh-privatekey:|    UG91cmluZzYlRW1vdGljb24lU2N1YmE=
```

The SSH authentication Secret type is provided only for convenience. You can create an Opaquetype for credentials used for SSH authentication. However, using the defined and public Secret type ( kubernetes.io/ssh-auth) helps other people to understand the purpose of your Secret, and sets a convention for what key names to expect. The Kubernetes API verifies that the required keys are set for a Secret of this type. 
#### Caution: SSH private keys do not establish trusted communication between an SSH client and host server on their own. A secondary means of establishing trust is needed to mitigate "man in the middle" attacks, such as a known_hostsfile added to a ConfigMap. 
### TLS Secrets 
The kubernetes.io/tlsSecret type is for storing a certificate and its associated key that are typically used for TLS. 
One common use for TLS Secrets is to configure encryption in transit for an Ingress , but you can also use it with other resources or directly in your workload. When using this type of Secret, the tls.keyand the tls.crtkey must be provided in the data(or stringData) field of the Secret configuration, although the API server doesn't actually validate the values for each key. 
As an alternative to using stringData, you can use the datafield to provide the base64 encoded certificate and private key. For details, see Constraints on Secret names and data . 
The following YAML contains an example config for a TLS Secret: secret/tls-auth-secret.yaml
```
apiVersion:v1kind:Secretmetadata:name:secret-tlstype:kubernetes.io/tlsdata:# values are base64 encoded, which obscures them but does NOT provide# any useful level of confidentiality# Replace the following values with your own base64-encoded certificate and key.tls.crt:"REPLACE_WITH_BASE64_CERT"tls.key:"REPLACE_WITH_BASE64_KEY"
```

The TLS Secret type is provided only for convenience. You can create an Opaquetype for credentials used for TLS authentication. However, using the defined and public Secret type ( kubernetes.io/tls) helps ensure the consistency of Secret format in your project. The API server verifies if the required keys are set for a Secret of this type. 
To create a TLS Secret using kubectl, use the tlssubcommand: 
```
kubectl create secret tls my-tls-secret \
  --cert=path/to/cert/file \
  --key=path/to/key/file

```

The public/private key pair must exist before hand. The public key certificate for --certmust be .PEM encoded and must match the given private key for --key. 
### Bootstrap token Secrets 
The bootstrap.kubernetes.io/tokenSecret type is for tokens used during the node bootstrap process. It stores tokens used to sign well-known ConfigMaps. 
A bootstrap token Secret is usually created in the kube-systemnamespace and named in the form bootstrap-token-<token-id>where <token-id>is a 6 character string of the token ID. 
As a Kubernetes manifest, a bootstrap token Secret might look like the following: secret/bootstrap-token-secret-base64.yaml
```
apiVersion:v1kind:Secretmetadata:name:bootstrap-token-5emitjnamespace:kube-systemtype:bootstrap.kubernetes.io/tokendata:auth-extra-groups:c3lzdGVtOmJvb3RzdHJhcHBlcnM6a3ViZWFkbTpkZWZhdWx0LW5vZGUtdG9rZW4=expiration:MjAyMC0wOS0xM1QwNDozOToxMFo=token-id:NWVtaXRqtoken-secret:a3E0Z2lodnN6emduMXAwcg==usage-bootstrap-authentication:dHJ1ZQ==usage-bootstrap-signing:dHJ1ZQ==
```

A bootstrap token Secret has the following keys specified under data: 
- token-id: A random 6 character string as the token identifier. Required. - token-secret: A random 16 character string as the actual token Secret. Required. - description: A human-readable string that describes what the token is used for. Optional. - expiration: An absolute UTC time using RFC3339 specifying when the token should be expired. Optional. - usage-bootstrap-<usage>: A boolean flag indicating additional usage for the bootstrap token. - auth-extra-groups: A comma-separated list of group names that will be authenticated as in addition to the system:bootstrappersgroup. 
You can alternatively provide the values in the stringDatafield of the Secret without base64 encoding them: secret/bootstrap-token-secret-literal.yaml
```
apiVersion:v1kind:Secretmetadata:# Note how the Secret is namedname:bootstrap-token-5emitj# A bootstrap token Secret usually resides in the kube-system namespacenamespace:kube-systemtype:bootstrap.kubernetes.io/tokenstringData:auth-extra-groups:"system:bootstrappers:kubeadm:default-node-token"expiration:"2020-09-13T04:39:10Z"# This token ID is used in the nametoken-id:"5emitj"token-secret:"kq4gihvszzgn1p0r"# This token can be used for authenticationusage-bootstrap-authentication:"true"# and it can be used for signingusage-bootstrap-signing:"true"
```

#### Note: The stringDatafield for a Secret does not work well with server-side apply. 
## Working with Secrets 
### Creating a Secret 
There are several options to create a Secret: 
- Use kubectl- Use a configuration file - Use the Kustomize tool 
#### Constraints on Secret names and data 
The name of a Secret object must be a valid DNS subdomain name . 
You can specify the dataand/or the stringDatafield when creating a configuration file for a Secret. The dataand the stringDatafields are optional. The values for all keys in the datafield have to be base64-encoded strings. If the conversion to base64 string is not desirable, you can choose to specify the stringDatafield instead, which accepts arbitrary strings as values. 
The keys of dataand stringDatamust consist of alphanumeric characters, -, _or .. All key-value pairs in the stringDatafield are internally merged into the datafield. If a key appears in both the dataand the stringDatafield, the value specified in the stringDatafield takes precedence. 
#### Size limit 
Individual Secrets are limited to 1MiB in size. This is to discourage creation of very large Secrets that could exhaust the API server and kubelet memory. However, creation of many smaller Secrets could also exhaust memory. You can use a resource quota to limit the number of Secrets (or other resources) in a namespace. 
### Editing a Secret 
You can edit an existing Secret unless it is immutable . To edit a Secret, use one of the following methods: 
- Use kubectl- Use a configuration file 
You can also edit the data in a Secret using the Kustomize tool . However, this method creates a new Secretobject with the edited data. 
Depending on how you created the Secret, as well as how the Secret is used in your Pods, updates to existing Secretobjects are propagated automatically to Pods that use the data. For more information, refer to Using Secrets as files from a Pod section. 
### Using a Secret 
Secrets can be mounted as data volumes or exposed as environment variables to be used by a container in a Pod. Secrets can also be used by other parts of the system, without being directly exposed to the Pod. For example, Secrets can hold credentials that other parts of the system should use to interact with external systems on your behalf. 
Secret volume sources are validated to ensure that the specified object reference actually points to an object of type Secret. Therefore, a Secret needs to be created before any Pods that depend on it. 
If the Secret cannot be fetched (perhaps because it does not exist, or due to a temporary lack of connection to the API server) the kubelet periodically retries running that Pod. The kubelet also reports an Event for that Pod, including details of the problem fetching the Secret. 
#### Optional Secrets 
When you reference a Secret in a Pod, you can mark the Secret as optional , such as in the following example. If an optional Secret doesn't exist, Kubernetes ignores it. secret/optional-secret.yaml
```
apiVersion:v1kind:Podmetadata:name:mypodspec:containers:- name:mypodimage:redisvolumeMounts:- name:foomountPath:"/etc/foo"readOnly:truevolumes:- name:foosecret:secretName:mysecretoptional:true
```

By default, Secrets are required. None of a Pod's containers will start until all non-optional Secrets are available. 
If a Pod references a specific key in a non-optional Secret and that Secret does exist, but is missing the named key, the Pod fails during startup. 
### Using Secrets as files from a Pod 
If you want to access data from a Secret in a Pod, one way to do that is to have Kubernetes make the value of that Secret be available as a file inside the filesystem of one or more of the Pod's containers. 
For instructions, refer to Create a Pod that has access to the secret data through a Volume . 
When a volume contains data from a Secret, and that Secret is updated, Kubernetes tracks this and updates the data in the volume, using an eventually-consistent approach. 
#### Note: A container using a Secret as a subPath volume mount does not receive automated Secret updates. 
The kubelet keeps a cache of the current keys and values for the Secrets that are used in volumes for pods on that node. You can configure the way that the kubelet detects changes from the cached values. The configMapAndSecretChangeDetectionStrategyfield in the kubelet configuration controls which strategy the kubelet uses. The default strategy is Watch. 
Updates to Secrets can be either propagated by an API watch mechanism (the default), based on a cache with a defined time-to-live, or polled from the cluster API server on each kubelet synchronisation loop. 
As a result, the total delay from the moment when the Secret is updated to the moment when new keys are projected to the Pod can be as long as the kubelet sync period + cache propagation delay, where the cache propagation delay depends on the chosen cache type (following the same order listed in the previous paragraph, these are: watch propagation delay, the configured cache TTL, or zero for direct polling). 
### Using Secrets as environment variables 
To use a Secret in an environment variable in a Pod: 
- For each container in your Pod specification, add an environment variable for each Secret key that you want to use to the env[].valueFrom.secretKeyReffield. - Modify your image and/or command line so that the program looks for values in the specified environment variables. 
For instructions, refer to Define container environment variables using Secret data . 
It's important to note that the range of characters allowed for environment variable names in pods is restricted . If any keys do not meet the rules, those keys are not made available to your container, though the Pod is allowed to start. 
### Container image pull Secrets 
If you want to fetch container images from a private repository, you need a way for the kubelet on each node to authenticate to that repository. You can configure image pull Secrets to make this possible. These Secrets are configured at the Pod level. 
#### Using imagePullSecrets 
The imagePullSecretsfield is a list of references to Secrets in the same namespace. You can use an imagePullSecretsto pass a Secret that contains a Docker (or other) image registry password to the kubelet. The kubelet uses this information to pull a private image on behalf of your Pod. See the PodSpec API for more information about the imagePullSecretsfield. 
##### Manually specifying an imagePullSecret 
You can learn how to specify imagePullSecretsfrom the container images documentation. 
##### Arranging for imagePullSecrets to be automatically attached 
You can manually create imagePullSecrets, and reference these from a ServiceAccount. Any Pods created with that ServiceAccount or created with that ServiceAccount by default, will get their imagePullSecretsfield set to that of the service account. See Add ImagePullSecrets to a service account for a detailed explanation of that process. 
### Using Secrets with static Pods 
You cannot use ConfigMaps or Secrets with static Pods . 
## Immutable Secrets FEATURE STATE: Kubernetes v1.21 [stable]
Kubernetes lets you mark specific Secrets (and ConfigMaps) as immutable . Preventing changes to the data of an existing Secret has the following benefits: 
- protects you from accidental (or unwanted) updates that could cause applications outages - (for clusters that extensively use Secrets - at least tens of thousands of unique Secret to Pod mounts), switching to immutable Secrets improves the performance of your cluster by significantly reducing load on kube-apiserver. The kubelet does not need to maintain a [watch] on any Secrets that are marked as immutable. 
### Marking a Secret as immutable 
You can create an immutable Secret by setting the immutablefield to true. For example, 
```
apiVersion:v1kind:Secretmetadata:...data:...immutable:true
```

You can also update any existing mutable Secret to make it immutable. 
#### Note: Once a Secret or ConfigMap is marked as immutable, it is not possible to revert this change nor to mutate the contents of the datafield. You can only delete and recreate the Secret. Existing Pods maintain a mount point to the deleted Secret - it is recommended to recreate these pods. 
## Information security for Secrets 
Although ConfigMap and Secret work similarly, Kubernetes applies some additional protection for Secret objects. 
Secrets often hold values that span a spectrum of importance, many of which can cause escalations within Kubernetes (e.g. service account tokens) and to external systems. Even if an individual app can reason about the power of the Secrets it expects to interact with, other apps within the same namespace can render those assumptions invalid. 
Authorization configuration affects how Secret data can be accessed within a namespace. For example, granting list or watch permissions on Secrets allows a subject to read all Secret data in that namespace, not only the Secrets explicitly referenced by its Pods. Restrict access to the minimum set of permissions required for a workload to function, and avoid granting broad roles such as cluster-adminunless required for administrative purposes. 
Also see the Authorization documentation . 
A Secret is only sent to a node if a Pod on that node requires it. For mounting Secrets into Pods, the kubelet stores a copy of the data into a tmpfsso that the confidential data is not written to durable storage. Once the Pod that depends on the Secret is deleted, the kubelet deletes its local copy of the confidential data from the Secret. 
There may be several containers in a Pod. By default, containers you define only have access to the default ServiceAccount and its related Secret. You must explicitly define environment variables or map a volume into a container in order to provide access to any other Secret. 
There may be Secrets for several Pods on the same node. However, only the Secrets that a Pod requests are potentially visible within its containers. Therefore, one Pod does not have access to the Secrets of another Pod. 
### Configure least-privilege access to Secrets 
To enhance the security measures around Secrets, use separate namespaces to isolate access to mounted secrets. 
#### Warning: Any containers that run with privileged: trueon a node can access all Secrets used on that node. 
## What's next 
- For guidelines to manage and improve the security of your Secrets, refer to Good practices for Kubernetes Secrets . - Learn how to manage Secrets using kubectl- Learn how to manage Secrets using config file - Learn how to manage Secrets using kustomize - Read the API reference for Secret
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified March 17, 2026 at 1:33 AM PST: Improve security clarification for Kubernetes Secrets (#54644) (8af7916eb8) 
- - - - - - 

- - - - 

### 📄 Source: [https://kubernetes.io/docs/concepts/configuration/secret/#protections](https://kubernetes.io/docs/concepts/configuration/secret/#protections)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.36   - v1.35   - v1.34   - v1.33   - v1.32 - English 
  - 中文 (Chinese)   - Français (French)   - Deutsch (German)   - Bahasa Indonesia (Indonesian)   - 日本語 (Japanese)   - 한국어 (Korean)   - Português (Portuguese)   - Español (Spanish)   - Tiếng Việt (Vietnamese)   - বাংলা (Bengali)   - हिन्दी (Hindi)   - Italiano (Italian)   - فارسی (Persian)   - Polski (Polish)   - Русский (Russian)   - Українська (Ukrainian) - 
  - Light   - Dark   - Auto 
# Secrets 
- - - - - - - - - - - - - - - - 
- 
  - 
    -   - 
    -     - 
      -       - 
        - 
          -           -           -           -           -           -           -           -           -       -     - 
      -       -       -       -       -   - 
    - 
      -       - 
        -         -         -         -         -         -         -         -         -         -       -       -     - 
      -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -     - 
      - 
        -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -         -         -       - 
        -         -         -         -         -         -         -         -       - 
        -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -     - 
      - 
        -         -       - 
        -         -       -   - 
    - 
      -       -       -     - 
      - 
        -         -         -         -         -         -         -         -         -       -       - 
        -         -         -         -         -       -       - 
        -         -         -         -         -         -       - 
        -         -         -         -         -         -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       - 
        -         -         -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       - 
        -         -         -         -         -         -         -       - 
        -         -         -         -         -         -         -         -         -         -     - 
      -       -       -       -       -       -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -     - 
      -       - 
        -         -       -       -       -       -       -     - 
      -       -       -       -     - 
      -       -       -       -     - 
      -       -       -       -     -     -     -   - 
    -     - 
      - 
        -       - 
        -       - 
        -       - 
        -       - 
        -       - 
        -     - 
      -       -       -       -     - 
      -       -       -       -     - 
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -     - 
      -       - 
        -         -         -         -         -         -       - 
        -       - 
        -       - 
        -       - 
        -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -       - 
        -         -       - 
        -       - 
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
        -         -         -         -         -         -       - 
        -     - 
      -       -       -       -       -       -       -     - 
      -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -     - 
      - 
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -     - 
      -       -       - 
        -         -         -         -         - 
          -           -           -         -         - 
          -           -           -         -         - 
          -           -         - 
          -         -         - 
          -           -           -           -           -           -           -           -           -           -           -           -           -           -           -         -         -         - 
          -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -         -         -         -         -         -         -         -         -         -         -         -         - 
          -           -         -         -         -         -         -         - 
          -         -         -         -         - 
          -           -           -           -           -           -         -         -         - 
          -           -           -           -           -           -         -         - 
          -           -         -         -         -       -       -       -       -       -       -     - 
      -     - 
      -       -       -       -       -       -       -     - 
      -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -     -     -   - 
- 
  -   -   - - 
  -   -   -   -   -   -   - - 
  -   -   -   -   -   -   - - 
  - - 
  - - 
- - - - 
# Secrets 
A Secret is an object that contains a small amount of sensitive data such as a password, a token, or a key. Such information might otherwise be put in a Pod specification or in a container image . Using a Secret means that you don't need to include confidential data in your application code. 
Because Secrets can be created independently of the Pods that use them, there is less risk of the Secret (and its data) being exposed during the workflow of creating, viewing, and editing Pods. Kubernetes, and applications that run in your cluster, can also take additional precautions with Secrets, such as avoiding writing sensitive data to nonvolatile storage. 
Secrets are similar to ConfigMaps but are specifically intended to hold confidential data. 
#### Caution: 
Kubernetes Secrets are, by default, stored unencrypted in the API server's underlying data store (etcd). Anyone with API access can retrieve or modify a Secret, and so can anyone with access to etcd. Additionally, anyone who is authorized to create a Pod in a namespace can use that access to read any Secret in that namespace; this includes indirect access such as the ability to create a Deployment. 
In order to safely use Secrets, take at least the following steps: 
- Enable Encryption at Rest for Secrets. - Enable or configure RBAC rules with least-privilege access to Secrets. - Restrict Secret access to specific containers. - Consider using external Secret store providers . 
For more guidelines to manage and improve the security of your Secrets, refer to Good practices for Kubernetes Secrets . 
See Information security for Secrets for more details. 
## Uses for Secrets 
You can use Secrets for purposes such as the following: 
- Set environment variables for a container . - Provide credentials such as SSH keys or passwords to Pods . - Allow the kubelet to pull container images from private registries . 
The Kubernetes control plane also uses Secrets; for example, bootstrap token Secrets are a mechanism to help automate node registration. 
### Use case: dotfiles in a secret volume 
You can make your data "hidden" by defining a key that begins with a dot. This key represents a dotfile or "hidden" file. For example, when the following Secret is mounted into a volume, secret-volume, the volume will contain a single file, called .secret-file, and the dotfile-test-containerwill have this file present at the path /etc/secret-volume/.secret-file. 
#### Note: Files beginning with dot characters are hidden from the output of ls -l; you must use ls -lato see them when listing directory contents. secret/dotfile-secret.yaml
```
apiVersion:v1kind:Secretmetadata:name:dotfile-secretdata:.secret-file:dmFsdWUtMg0KDQo=---apiVersion:v1kind:Podmetadata:name:secret-dotfiles-podspec:volumes:- name:secret-volumesecret:secretName:dotfile-secretcontainers:- name:dotfile-test-containerimage:registry.k8s.io/busyboxcommand:- ls- "-l"- "/etc/secret-volume"volumeMounts:- name:secret-volumereadOnly:truemountPath:"/etc/secret-volume"
```

### Use case: Secret visible to one container in a Pod 
Consider a program that needs to handle HTTP requests, do some complex business logic, and then sign some messages with an HMAC. Because it has complex application logic, there might be an unnoticed remote file reading exploit in the server, which could expose the private key to an attacker. 
This could be divided into two processes in two containers: a frontend container which handles user interaction and business logic, but which cannot see the private key; and a signer container that can see the private key, and responds to simple signing requests from the frontend (for example, over localhost networking). 
With this partitioned approach, an attacker now has to trick the application server into doing something rather arbitrary, which may be harder than getting it to read a file. 
### Alternatives to Secrets 
Rather than using a Secret to protect confidential data, you can pick from alternatives. 
Here are some of your options: 
- If your cloud-native component needs to authenticate to another application that you know is running within the same Kubernetes cluster, you can use a ServiceAccount and its tokens to identify your client. - There are third-party tools that you can run, either within or outside your cluster, that manage sensitive data. For example, a service that Pods access over HTTPS, that reveals a Secret if the client correctly authenticates (for example, with a ServiceAccount token). - For authentication, you can implement a custom signer for X.509 certificates, and use CertificateSigningRequests to let that custom signer issue certificates to Pods that need them. - You can use a device plugin to expose node-local encryption hardware to a specific Pod. For example, you can schedule trusted Pods onto nodes that provide a Trusted Platform Module, configured out-of-band. 
You can also combine two or more of those options, including the option to use Secret objects themselves. 
For example: implement (or deploy) an operator that fetches short-lived session tokens from an external service, and then creates Secrets based on those short-lived session tokens. Pods running in your cluster can make use of the session tokens, and operator ensures they are valid. This separation means that you can run Pods that are unaware of the exact mechanisms for issuing and refreshing those session tokens. 
## Types of Secret 
When creating a Secret, you can specify its type using the typefield of the Secret resource, or certain equivalent kubectlcommand line flags (if available). The Secret type is used to facilitate programmatic handling of the Secret data. 
Kubernetes provides several built-in types for some common usage scenarios. These types vary in terms of the validations performed and the constraints Kubernetes imposes on them. 
|  Built-in Type  | Usage  |
|  Opaque | arbitrary user-defined data  |
|  kubernetes.io/service-account-token | ServiceAccount token  |
|  kubernetes.io/dockercfg | serialized ~/.dockercfgfile  |
|  kubernetes.io/dockerconfigjson | serialized ~/.docker/config.jsonfile  |
|  kubernetes.io/basic-auth | credentials for basic authentication  |
|  kubernetes.io/ssh-auth | credentials for SSH authentication  |
|  kubernetes.io/tls | data for a TLS client or server  |
|  bootstrap.kubernetes.io/token | bootstrap token data  |
You can define and use your own Secret type by assigning a non-empty string as the typevalue for a Secret object (an empty string is treated as an Opaquetype). 
Kubernetes doesn't impose any constraints on the type name. However, if you are using one of the built-in types, you must meet all the requirements defined for that type. 
If you are defining a type of Secret that's for public use, follow the convention and structure the Secret type to have your domain name before the name, separated by a /. For example: cloud-hosting.example.net/cloud-api-credentials. 
### Opaque Secrets 
Opaqueis the default Secret type if you don't explicitly specify a type in a Secret manifest. When you create a Secret using kubectl, you must use the genericsubcommand to indicate an OpaqueSecret type. For example, the following command creates an empty Secret of type Opaque: 
```
kubectl create secret generic empty-secret
kubectl get secret empty-secret

```

The output looks like: 
```
NAME           TYPE     DATA   AGE
empty-secret   Opaque   0      2m6s

```

The DATAcolumn shows the number of data items stored in the Secret. In this case, 0means you have created an empty Secret. 
### ServiceAccount token Secrets 
A kubernetes.io/service-account-tokentype of Secret is used to store a token credential that identifies a ServiceAccount . This is a legacy mechanism that provides long-lived ServiceAccount credentials to Pods. 
In Kubernetes v1.22 and later, the recommended approach is to obtain a short-lived, automatically rotating ServiceAccount token by using the TokenRequestAPI instead. You can get these short-lived tokens using the following methods: 
- Call the TokenRequestAPI either directly or by using an API client like kubectl. For example, you can use the kubectl create tokencommand. - Request a mounted token in a projected volume in your Pod manifest. Kubernetes creates the token and mounts it in the Pod. The token is automatically invalidated when the Pod that it's mounted in is deleted. For details, see Launch a Pod using service account token projection . 
#### Note: You should only create a ServiceAccount token Secret if you can't use the TokenRequestAPI to obtain a token, and the security exposure of persisting a non-expiring token credential in a readable API object is acceptable to you. For instructions, see Manually create a long-lived API token for a ServiceAccount . 
When using this Secret type, you need to ensure that the kubernetes.io/service-account.nameannotation is set to an existing ServiceAccount name. If you are creating both the ServiceAccount and the Secret objects, you should create the ServiceAccount object first. 
After the Secret is created, a Kubernetes controller fills in some other fields such as the kubernetes.io/service-account.uidannotation, and the tokenkey in the datafield, which is populated with an authentication token. 
The following example configuration declares a ServiceAccount token Secret: secret/serviceaccount-token-secret.yaml
```
apiVersion:v1kind:Secretmetadata:name:secret-sa-sampleannotations:kubernetes.io/service-account.name:"sa-name"type:kubernetes.io/service-account-tokendata:extra:YmFyCg==
```

After creating the Secret, wait for Kubernetes to populate the tokenkey in the datafield. 
See the ServiceAccount documentation for more information on how ServiceAccounts work. You can also check the automountServiceAccountTokenfield and the serviceAccountNamefield of the Podfor information on referencing ServiceAccount credentials from within Pods. 
### Docker config Secrets 
If you are creating a Secret to store credentials for accessing a container image registry, you must use one of the following typevalues for that Secret: 
- kubernetes.io/dockercfg: store a serialized ~/.dockercfgwhich is the legacy format for configuring Docker command line. The Secret datafield contains a .dockercfgkey whose value is the content of a base64 encoded ~/.dockercfgfile. - kubernetes.io/dockerconfigjson: store a serialized JSON that follows the same format rules as the ~/.docker/config.jsonfile, which is a new format for ~/.dockercfg. The Secret datafield must contain a .dockerconfigjsonkey for which the value is the content of a base64 encoded ~/.docker/config.jsonfile. 
Below is an example for a kubernetes.io/dockercfgtype of Secret: secret/dockercfg-secret.yaml
```
apiVersion:v1kind:Secretmetadata:name:secret-dockercfgtype:kubernetes.io/dockercfgdata:.dockercfg:|    eyJhdXRocyI6eyJodHRwczovL2V4YW1wbGUvdjEvIjp7ImF1dGgiOiJvcGVuc2VzYW1lIn19fQo=
```

#### Note: If you do not want to perform the base64 encoding, you can choose to use the stringDatafield instead. 
When you create Docker config Secrets using a manifest, the API server checks whether the expected key exists in the datafield, and it verifies if the value provided can be parsed as a valid JSON. The API server doesn't validate if the JSON actually is a Docker config file. 
You can also use kubectlto create a Secret for accessing a container registry, such as when you don't have a Docker configuration file: 
```
kubectl create secret docker-registry secret-tiger-docker \
  --docker-email=tiger@acme.example \
  --docker-username=tiger \
  --docker-password=pass1234 \
  --docker-server=my-registry.example:5000

```

This command creates a Secret of type kubernetes.io/dockerconfigjson. 
Retrieve the .data.dockerconfigjsonfield from that new Secret and decode the data: 
```
kubectl get secret secret-tiger-docker -o jsonpath='{.data.*}'| base64 -d

```

The output is equivalent to the following JSON document (which is also a valid Docker configuration file): 
```
{"auths":{"my-registry.example:5000":{"username":"tiger","password":"pass1234","email":"tiger@acme.example","auth":"dGlnZXI6cGFzczEyMzQ="}}}
```

#### Caution: 
The authvalue there is base64 encoded; it is obscured but not secret. Anyone who can read that Secret can learn the registry access bearer token. 
It is suggested to use credential providers to dynamically and securely provide pull secrets on-demand. 
### Basic authentication Secret 
The kubernetes.io/basic-authtype is provided for storing credentials needed for basic authentication. When using this Secret type, the datafield of the Secret must contain one of the following two keys: 
- username: the user name for authentication - password: the password or token for authentication 
Both values for the above two keys are base64 encoded strings. You can alternatively provide the clear text content using the stringDatafield in the Secret manifest. 
The following manifest is an example of a basic authentication Secret: secret/basicauth-secret.yaml
```
apiVersion:v1kind:Secretmetadata:name:secret-basic-authtype:kubernetes.io/basic-authstringData:username:admin# required field for kubernetes.io/basic-authpassword:t0p-Secret# required field for kubernetes.io/basic-auth
```

#### Note: The stringDatafield for a Secret does not work well with server-side apply. 
The basic authentication Secret type is provided only for convenience. You can create an Opaquetype for credentials used for basic authentication. However, using the defined and public Secret type ( kubernetes.io/basic-auth) helps other people to understand the purpose of your Secret, and sets a convention for what key names to expect. 
### SSH authentication Secrets 
The builtin type kubernetes.io/ssh-authis provided for storing data used in SSH authentication. When using this Secret type, you will have to specify a ssh-privatekeykey-value pair in the data(or stringData) field as the SSH credential to use. 
The following manifest is an example of a Secret used for SSH public/private key authentication: secret/ssh-auth-secret.yaml
```
apiVersion:v1kind:Secretmetadata:name:secret-ssh-authtype:kubernetes.io/ssh-authdata:# the data is abbreviated in this examplessh-privatekey:|    UG91cmluZzYlRW1vdGljb24lU2N1YmE=
```

The SSH authentication Secret type is provided only for convenience. You can create an Opaquetype for credentials used for SSH authentication. However, using the defined and public Secret type ( kubernetes.io/ssh-auth) helps other people to understand the purpose of your Secret, and sets a convention for what key names to expect. The Kubernetes API verifies that the required keys are set for a Secret of this type. 
#### Caution: SSH private keys do not establish trusted communication between an SSH client and host server on their own. A secondary means of establishing trust is needed to mitigate "man in the middle" attacks, such as a known_hostsfile added to a ConfigMap. 
### TLS Secrets 
The kubernetes.io/tlsSecret type is for storing a certificate and its associated key that are typically used for TLS. 
One common use for TLS Secrets is to configure encryption in transit for an Ingress , but you can also use it with other resources or directly in your workload. When using this type of Secret, the tls.keyand the tls.crtkey must be provided in the data(or stringData) field of the Secret configuration, although the API server doesn't actually validate the values for each key. 
As an alternative to using stringData, you can use the datafield to provide the base64 encoded certificate and private key. For details, see Constraints on Secret names and data . 
The following YAML contains an example config for a TLS Secret: secret/tls-auth-secret.yaml
```
apiVersion:v1kind:Secretmetadata:name:secret-tlstype:kubernetes.io/tlsdata:# values are base64 encoded, which obscures them but does NOT provide# any useful level of confidentiality# Replace the following values with your own base64-encoded certificate and key.tls.crt:"REPLACE_WITH_BASE64_CERT"tls.key:"REPLACE_WITH_BASE64_KEY"
```

The TLS Secret type is provided only for convenience. You can create an Opaquetype for credentials used for TLS authentication. However, using the defined and public Secret type ( kubernetes.io/tls) helps ensure the consistency of Secret format in your project. The API server verifies if the required keys are set for a Secret of this type. 
To create a TLS Secret using kubectl, use the tlssubcommand: 
```
kubectl create secret tls my-tls-secret \
  --cert=path/to/cert/file \
  --key=path/to/key/file

```

The public/private key pair must exist before hand. The public key certificate for --certmust be .PEM encoded and must match the given private key for --key. 
### Bootstrap token Secrets 
The bootstrap.kubernetes.io/tokenSecret type is for tokens used during the node bootstrap process. It stores tokens used to sign well-known ConfigMaps. 
A bootstrap token Secret is usually created in the kube-systemnamespace and named in the form bootstrap-token-<token-id>where <token-id>is a 6 character string of the token ID. 
As a Kubernetes manifest, a bootstrap token Secret might look like the following: secret/bootstrap-token-secret-base64.yaml
```
apiVersion:v1kind:Secretmetadata:name:bootstrap-token-5emitjnamespace:kube-systemtype:bootstrap.kubernetes.io/tokendata:auth-extra-groups:c3lzdGVtOmJvb3RzdHJhcHBlcnM6a3ViZWFkbTpkZWZhdWx0LW5vZGUtdG9rZW4=expiration:MjAyMC0wOS0xM1QwNDozOToxMFo=token-id:NWVtaXRqtoken-secret:a3E0Z2lodnN6emduMXAwcg==usage-bootstrap-authentication:dHJ1ZQ==usage-bootstrap-signing:dHJ1ZQ==
```

A bootstrap token Secret has the following keys specified under data: 
- token-id: A random 6 character string as the token identifier. Required. - token-secret: A random 16 character string as the actual token Secret. Required. - description: A human-readable string that describes what the token is used for. Optional. - expiration: An absolute UTC time using RFC3339 specifying when the token should be expired. Optional. - usage-bootstrap-<usage>: A boolean flag indicating additional usage for the bootstrap token. - auth-extra-groups: A comma-separated list of group names that will be authenticated as in addition to the system:bootstrappersgroup. 
You can alternatively provide the values in the stringDatafield of the Secret without base64 encoding them: secret/bootstrap-token-secret-literal.yaml
```
apiVersion:v1kind:Secretmetadata:# Note how the Secret is namedname:bootstrap-token-5emitj# A bootstrap token Secret usually resides in the kube-system namespacenamespace:kube-systemtype:bootstrap.kubernetes.io/tokenstringData:auth-extra-groups:"system:bootstrappers:kubeadm:default-node-token"expiration:"2020-09-13T04:39:10Z"# This token ID is used in the nametoken-id:"5emitj"token-secret:"kq4gihvszzgn1p0r"# This token can be used for authenticationusage-bootstrap-authentication:"true"# and it can be used for signingusage-bootstrap-signing:"true"
```

#### Note: The stringDatafield for a Secret does not work well with server-side apply. 
## Working with Secrets 
### Creating a Secret 
There are several options to create a Secret: 
- Use kubectl- Use a configuration file - Use the Kustomize tool 
#### Constraints on Secret names and data 
The name of a Secret object must be a valid DNS subdomain name . 
You can specify the dataand/or the stringDatafield when creating a configuration file for a Secret. The dataand the stringDatafields are optional. The values for all keys in the datafield have to be base64-encoded strings. If the conversion to base64 string is not desirable, you can choose to specify the stringDatafield instead, which accepts arbitrary strings as values. 
The keys of dataand stringDatamust consist of alphanumeric characters, -, _or .. All key-value pairs in the stringDatafield are internally merged into the datafield. If a key appears in both the dataand the stringDatafield, the value specified in the stringDatafield takes precedence. 
#### Size limit 
Individual Secrets are limited to 1MiB in size. This is to discourage creation of very large Secrets that could exhaust the API server and kubelet memory. However, creation of many smaller Secrets could also exhaust memory. You can use a resource quota to limit the number of Secrets (or other resources) in a namespace. 
### Editing a Secret 
You can edit an existing Secret unless it is immutable . To edit a Secret, use one of the following methods: 
- Use kubectl- Use a configuration file 
You can also edit the data in a Secret using the Kustomize tool . However, this method creates a new Secretobject with the edited data. 
Depending on how you created the Secret, as well as how the Secret is used in your Pods, updates to existing Secretobjects are propagated automatically to Pods that use the data. For more information, refer to Using Secrets as files from a Pod section. 
### Using a Secret 
Secrets can be mounted as data volumes or exposed as environment variables to be used by a container in a Pod. Secrets can also be used by other parts of the system, without being directly exposed to the Pod. For example, Secrets can hold credentials that other parts of the system should use to interact with external systems on your behalf. 
Secret volume sources are validated to ensure that the specified object reference actually points to an object of type Secret. Therefore, a Secret needs to be created before any Pods that depend on it. 
If the Secret cannot be fetched (perhaps because it does not exist, or due to a temporary lack of connection to the API server) the kubelet periodically retries running that Pod. The kubelet also reports an Event for that Pod, including details of the problem fetching the Secret. 
#### Optional Secrets 
When you reference a Secret in a Pod, you can mark the Secret as optional , such as in the following example. If an optional Secret doesn't exist, Kubernetes ignores it. secret/optional-secret.yaml
```
apiVersion:v1kind:Podmetadata:name:mypodspec:containers:- name:mypodimage:redisvolumeMounts:- name:foomountPath:"/etc/foo"readOnly:truevolumes:- name:foosecret:secretName:mysecretoptional:true
```

By default, Secrets are required. None of a Pod's containers will start until all non-optional Secrets are available. 
If a Pod references a specific key in a non-optional Secret and that Secret does exist, but is missing the named key, the Pod fails during startup. 
### Using Secrets as files from a Pod 
If you want to access data from a Secret in a Pod, one way to do that is to have Kubernetes make the value of that Secret be available as a file inside the filesystem of one or more of the Pod's containers. 
For instructions, refer to Create a Pod that has access to the secret data through a Volume . 
When a volume contains data from a Secret, and that Secret is updated, Kubernetes tracks this and updates the data in the volume, using an eventually-consistent approach. 
#### Note: A container using a Secret as a subPath volume mount does not receive automated Secret updates. 
The kubelet keeps a cache of the current keys and values for the Secrets that are used in volumes for pods on that node. You can configure the way that the kubelet detects changes from the cached values. The configMapAndSecretChangeDetectionStrategyfield in the kubelet configuration controls which strategy the kubelet uses. The default strategy is Watch. 
Updates to Secrets can be either propagated by an API watch mechanism (the default), based on a cache with a defined time-to-live, or polled from the cluster API server on each kubelet synchronisation loop. 
As a result, the total delay from the moment when the Secret is updated to the moment when new keys are projected to the Pod can be as long as the kubelet sync period + cache propagation delay, where the cache propagation delay depends on the chosen cache type (following the same order listed in the previous paragraph, these are: watch propagation delay, the configured cache TTL, or zero for direct polling). 
### Using Secrets as environment variables 
To use a Secret in an environment variable in a Pod: 
- For each container in your Pod specification, add an environment variable for each Secret key that you want to use to the env[].valueFrom.secretKeyReffield. - Modify your image and/or command line so that the program looks for values in the specified environment variables. 
For instructions, refer to Define container environment variables using Secret data . 
It's important to note that the range of characters allowed for environment variable names in pods is restricted . If any keys do not meet the rules, those keys are not made available to your container, though the Pod is allowed to start. 
### Container image pull Secrets 
If you want to fetch container images from a private repository, you need a way for the kubelet on each node to authenticate to that repository. You can configure image pull Secrets to make this possible. These Secrets are configured at the Pod level. 
#### Using imagePullSecrets 
The imagePullSecretsfield is a list of references to Secrets in the same namespace. You can use an imagePullSecretsto pass a Secret that contains a Docker (or other) image registry password to the kubelet. The kubelet uses this information to pull a private image on behalf of your Pod. See the PodSpec API for more information about the imagePullSecretsfield. 
##### Manually specifying an imagePullSecret 
You can learn how to specify imagePullSecretsfrom the container images documentation. 
##### Arranging for imagePullSecrets to be automatically attached 
You can manually create imagePullSecrets, and reference these from a ServiceAccount. Any Pods created with that ServiceAccount or created with that ServiceAccount by default, will get their imagePullSecretsfield set to that of the service account. See Add ImagePullSecrets to a service account for a detailed explanation of that process. 
### Using Secrets with static Pods 
You cannot use ConfigMaps or Secrets with static Pods . 
## Immutable Secrets FEATURE STATE: Kubernetes v1.21 [stable]
Kubernetes lets you mark specific Secrets (and ConfigMaps) as immutable . Preventing changes to the data of an existing Secret has the following benefits: 
- protects you from accidental (or unwanted) updates that could cause applications outages - (for clusters that extensively use Secrets - at least tens of thousands of unique Secret to Pod mounts), switching to immutable Secrets improves the performance of your cluster by significantly reducing load on kube-apiserver. The kubelet does not need to maintain a [watch] on any Secrets that are marked as immutable. 
### Marking a Secret as immutable 
You can create an immutable Secret by setting the immutablefield to true. For example, 
```
apiVersion:v1kind:Secretmetadata:...data:...immutable:true
```

You can also update any existing mutable Secret to make it immutable. 
#### Note: Once a Secret or ConfigMap is marked as immutable, it is not possible to revert this change nor to mutate the contents of the datafield. You can only delete and recreate the Secret. Existing Pods maintain a mount point to the deleted Secret - it is recommended to recreate these pods. 
## Information security for Secrets 
Although ConfigMap and Secret work similarly, Kubernetes applies some additional protection for Secret objects. 
Secrets often hold values that span a spectrum of importance, many of which can cause escalations within Kubernetes (e.g. service account tokens) and to external systems. Even if an individual app can reason about the power of the Secrets it expects to interact with, other apps within the same namespace can render those assumptions invalid. 
Authorization configuration affects how Secret data can be accessed within a namespace. For example, granting list or watch permissions on Secrets allows a subject to read all Secret data in that namespace, not only the Secrets explicitly referenced by its Pods. Restrict access to the minimum set of permissions required for a workload to function, and avoid granting broad roles such as cluster-adminunless required for administrative purposes. 
Also see the Authorization documentation . 
A Secret is only sent to a node if a Pod on that node requires it. For mounting Secrets into Pods, the kubelet stores a copy of the data into a tmpfsso that the confidential data is not written to durable storage. Once the Pod that depends on the Secret is deleted, the kubelet deletes its local copy of the confidential data from the Secret. 
There may be several containers in a Pod. By default, containers you define only have access to the default ServiceAccount and its related Secret. You must explicitly define environment variables or map a volume into a container in order to provide access to any other Secret. 
There may be Secrets for several Pods on the same node. However, only the Secrets that a Pod requests are potentially visible within its containers. Therefore, one Pod does not have access to the Secrets of another Pod. 
### Configure least-privilege access to Secrets 
To enhance the security measures around Secrets, use separate namespaces to isolate access to mounted secrets. 
#### Warning: Any containers that run with privileged: trueon a node can access all Secrets used on that node. 
## What's next 
- For guidelines to manage and improve the security of your Secrets, refer to Good practices for Kubernetes Secrets . - Learn how to manage Secrets using kubectl- Learn how to manage Secrets using config file - Learn how to manage Secrets using kustomize - Read the API reference for Secret
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified March 17, 2026 at 1:33 AM PST: Improve security clarification for Kubernetes Secrets (#54644) (8af7916eb8) 
- - - - - - 

- - - - 

### 📄 Source: [https://kubernetes.io/docs/concepts/configuration/secret/#risks](https://kubernetes.io/docs/concepts/configuration/secret/#risks)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.36   - v1.35   - v1.34   - v1.33   - v1.32 - English 
  - 中文 (Chinese)   - Français (French)   - Deutsch (German)   - Bahasa Indonesia (Indonesian)   - 日本語 (Japanese)   - 한국어 (Korean)   - Português (Portuguese)   - Español (Spanish)   - Tiếng Việt (Vietnamese)   - বাংলা (Bengali)   - हिन्दी (Hindi)   - Italiano (Italian)   - فارسی (Persian)   - Polski (Polish)   - Русский (Russian)   - Українська (Ukrainian) - 
  - Light   - Dark   - Auto 
# Secrets 
- - - - - - - - - - - - - - - - 
- 
  - 
    -   - 
    -     - 
      -       - 
        - 
          -           -           -           -           -           -           -           -           -       -     - 
      -       -       -       -       -   - 
    - 
      -       - 
        -         -         -         -         -         -         -         -         -         -       -       -     - 
      -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -     - 
      - 
        -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -         -         -       - 
        -         -         -         -         -         -         -         -       - 
        -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -     - 
      - 
        -         -       - 
        -         -       -   - 
    - 
      -       -       -     - 
      - 
        -         -         -         -         -         -         -         -         -       -       - 
        -         -         -         -         -       -       - 
        -         -         -         -         -         -       - 
        -         -         -         -         -         -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       - 
        -         -         -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       - 
        -         -         -         -         -         -         -       - 
        -         -         -         -         -         -         -         -         -         -     - 
      -       -       -       -       -       -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -     - 
      -       - 
        -         -       -       -       -       -       -     - 
      -       -       -       -     - 
      -       -       -       -     - 
      -       -       -       -     -     -     -   - 
    -     - 
      - 
        -       - 
        -       - 
        -       - 
        -       - 
        -       - 
        -     - 
      -       -       -       -     - 
      -       -       -       -     - 
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -     - 
      -       - 
        -         -         -         -         -         -       - 
        -       - 
        -       - 
        -       - 
        -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -       - 
        -         -       - 
        -       - 
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
        -         -         -         -         -         -       - 
        -     - 
      -       -       -       -       -       -       -     - 
      -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -     - 
      - 
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -     - 
      -       -       - 
        -         -         -         -         - 
          -           -           -         -         - 
          -           -           -         -         - 
          -           -         - 
          -         -         - 
          -           -           -           -           -           -           -           -           -           -           -           -           -           -           -         -         -         - 
          -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -         -         -         -         -         -         -         -         -         -         -         -         - 
          -           -         -         -         -         -         -         - 
          -         -         -         -         - 
          -           -           -           -           -           -         -         -         - 
          -           -           -           -           -           -         -         - 
          -           -         -         -         -       -       -       -       -       -       -     - 
      -     - 
      -       -       -       -       -       -       -     - 
      -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -     -     -   - 
- 
  -   -   - - 
  -   -   -   -   -   -   - - 
  -   -   -   -   -   -   - - 
  - - 
  - - 
- - - - 
# Secrets 
A Secret is an object that contains a small amount of sensitive data such as a password, a token, or a key. Such information might otherwise be put in a Pod specification or in a container image . Using a Secret means that you don't need to include confidential data in your application code. 
Because Secrets can be created independently of the Pods that use them, there is less risk of the Secret (and its data) being exposed during the workflow of creating, viewing, and editing Pods. Kubernetes, and applications that run in your cluster, can also take additional precautions with Secrets, such as avoiding writing sensitive data to nonvolatile storage. 
Secrets are similar to ConfigMaps but are specifically intended to hold confidential data. 
#### Caution: 
Kubernetes Secrets are, by default, stored unencrypted in the API server's underlying data store (etcd). Anyone with API access can retrieve or modify a Secret, and so can anyone with access to etcd. Additionally, anyone who is authorized to create a Pod in a namespace can use that access to read any Secret in that namespace; this includes indirect access such as the ability to create a Deployment. 
In order to safely use Secrets, take at least the following steps: 
- Enable Encryption at Rest for Secrets. - Enable or configure RBAC rules with least-privilege access to Secrets. - Restrict Secret access to specific containers. - Consider using external Secret store providers . 
For more guidelines to manage and improve the security of your Secrets, refer to Good practices for Kubernetes Secrets . 
See Information security for Secrets for more details. 
## Uses for Secrets 
You can use Secrets for purposes such as the following: 
- Set environment variables for a container . - Provide credentials such as SSH keys or passwords to Pods . - Allow the kubelet to pull container images from private registries . 
The Kubernetes control plane also uses Secrets; for example, bootstrap token Secrets are a mechanism to help automate node registration. 
### Use case: dotfiles in a secret volume 
You can make your data "hidden" by defining a key that begins with a dot. This key represents a dotfile or "hidden" file. For example, when the following Secret is mounted into a volume, secret-volume, the volume will contain a single file, called .secret-file, and the dotfile-test-containerwill have this file present at the path /etc/secret-volume/.secret-file. 
#### Note: Files beginning with dot characters are hidden from the output of ls -l; you must use ls -lato see them when listing directory contents. secret/dotfile-secret.yaml
```
apiVersion:v1kind:Secretmetadata:name:dotfile-secretdata:.secret-file:dmFsdWUtMg0KDQo=---apiVersion:v1kind:Podmetadata:name:secret-dotfiles-podspec:volumes:- name:secret-volumesecret:secretName:dotfile-secretcontainers:- name:dotfile-test-containerimage:registry.k8s.io/busyboxcommand:- ls- "-l"- "/etc/secret-volume"volumeMounts:- name:secret-volumereadOnly:truemountPath:"/etc/secret-volume"
```

### Use case: Secret visible to one container in a Pod 
Consider a program that needs to handle HTTP requests, do some complex business logic, and then sign some messages with an HMAC. Because it has complex application logic, there might be an unnoticed remote file reading exploit in the server, which could expose the private key to an attacker. 
This could be divided into two processes in two containers: a frontend container which handles user interaction and business logic, but which cannot see the private key; and a signer container that can see the private key, and responds to simple signing requests from the frontend (for example, over localhost networking). 
With this partitioned approach, an attacker now has to trick the application server into doing something rather arbitrary, which may be harder than getting it to read a file. 
### Alternatives to Secrets 
Rather than using a Secret to protect confidential data, you can pick from alternatives. 
Here are some of your options: 
- If your cloud-native component needs to authenticate to another application that you know is running within the same Kubernetes cluster, you can use a ServiceAccount and its tokens to identify your client. - There are third-party tools that you can run, either within or outside your cluster, that manage sensitive data. For example, a service that Pods access over HTTPS, that reveals a Secret if the client correctly authenticates (for example, with a ServiceAccount token). - For authentication, you can implement a custom signer for X.509 certificates, and use CertificateSigningRequests to let that custom signer issue certificates to Pods that need them. - You can use a device plugin to expose node-local encryption hardware to a specific Pod. For example, you can schedule trusted Pods onto nodes that provide a Trusted Platform Module, configured out-of-band. 
You can also combine two or more of those options, including the option to use Secret objects themselves. 
For example: implement (or deploy) an operator that fetches short-lived session tokens from an external service, and then creates Secrets based on those short-lived session tokens. Pods running in your cluster can make use of the session tokens, and operator ensures they are valid. This separation means that you can run Pods that are unaware of the exact mechanisms for issuing and refreshing those session tokens. 
## Types of Secret 
When creating a Secret, you can specify its type using the typefield of the Secret resource, or certain equivalent kubectlcommand line flags (if available). The Secret type is used to facilitate programmatic handling of the Secret data. 
Kubernetes provides several built-in types for some common usage scenarios. These types vary in terms of the validations performed and the constraints Kubernetes imposes on them. 
|  Built-in Type  | Usage  |
|  Opaque | arbitrary user-defined data  |
|  kubernetes.io/service-account-token | ServiceAccount token  |
|  kubernetes.io/dockercfg | serialized ~/.dockercfgfile  |
|  kubernetes.io/dockerconfigjson | serialized ~/.docker/config.jsonfile  |
|  kubernetes.io/basic-auth | credentials for basic authentication  |
|  kubernetes.io/ssh-auth | credentials for SSH authentication  |
|  kubernetes.io/tls | data for a TLS client or server  |
|  bootstrap.kubernetes.io/token | bootstrap token data  |
You can define and use your own Secret type by assigning a non-empty string as the typevalue for a Secret object (an empty string is treated as an Opaquetype). 
Kubernetes doesn't impose any constraints on the type name. However, if you are using one of the built-in types, you must meet all the requirements defined for that type. 
If you are defining a type of Secret that's for public use, follow the convention and structure the Secret type to have your domain name before the name, separated by a /. For example: cloud-hosting.example.net/cloud-api-credentials. 
### Opaque Secrets 
Opaqueis the default Secret type if you don't explicitly specify a type in a Secret manifest. When you create a Secret using kubectl, you must use the genericsubcommand to indicate an OpaqueSecret type. For example, the following command creates an empty Secret of type Opaque: 
```
kubectl create secret generic empty-secret
kubectl get secret empty-secret

```

The output looks like: 
```
NAME           TYPE     DATA   AGE
empty-secret   Opaque   0      2m6s

```

The DATAcolumn shows the number of data items stored in the Secret. In this case, 0means you have created an empty Secret. 
### ServiceAccount token Secrets 
A kubernetes.io/service-account-tokentype of Secret is used to store a token credential that identifies a ServiceAccount . This is a legacy mechanism that provides long-lived ServiceAccount credentials to Pods. 
In Kubernetes v1.22 and later, the recommended approach is to obtain a short-lived, automatically rotating ServiceAccount token by using the TokenRequestAPI instead. You can get these short-lived tokens using the following methods: 
- Call the TokenRequestAPI either directly or by using an API client like kubectl. For example, you can use the kubectl create tokencommand. - Request a mounted token in a projected volume in your Pod manifest. Kubernetes creates the token and mounts it in the Pod. The token is automatically invalidated when the Pod that it's mounted in is deleted. For details, see Launch a Pod using service account token projection . 
#### Note: You should only create a ServiceAccount token Secret if you can't use the TokenRequestAPI to obtain a token, and the security exposure of persisting a non-expiring token credential in a readable API object is acceptable to you. For instructions, see Manually create a long-lived API token for a ServiceAccount . 
When using this Secret type, you need to ensure that the kubernetes.io/service-account.nameannotation is set to an existing ServiceAccount name. If you are creating both the ServiceAccount and the Secret objects, you should create the ServiceAccount object first. 
After the Secret is created, a Kubernetes controller fills in some other fields such as the kubernetes.io/service-account.uidannotation, and the tokenkey in the datafield, which is populated with an authentication token. 
The following example configuration declares a ServiceAccount token Secret: secret/serviceaccount-token-secret.yaml
```
apiVersion:v1kind:Secretmetadata:name:secret-sa-sampleannotations:kubernetes.io/service-account.name:"sa-name"type:kubernetes.io/service-account-tokendata:extra:YmFyCg==
```

After creating the Secret, wait for Kubernetes to populate the tokenkey in the datafield. 
See the ServiceAccount documentation for more information on how ServiceAccounts work. You can also check the automountServiceAccountTokenfield and the serviceAccountNamefield of the Podfor information on referencing ServiceAccount credentials from within Pods. 
### Docker config Secrets 
If you are creating a Secret to store credentials for accessing a container image registry, you must use one of the following typevalues for that Secret: 
- kubernetes.io/dockercfg: store a serialized ~/.dockercfgwhich is the legacy format for configuring Docker command line. The Secret datafield contains a .dockercfgkey whose value is the content of a base64 encoded ~/.dockercfgfile. - kubernetes.io/dockerconfigjson: store a serialized JSON that follows the same format rules as the ~/.docker/config.jsonfile, which is a new format for ~/.dockercfg. The Secret datafield must contain a .dockerconfigjsonkey for which the value is the content of a base64 encoded ~/.docker/config.jsonfile. 
Below is an example for a kubernetes.io/dockercfgtype of Secret: secret/dockercfg-secret.yaml
```
apiVersion:v1kind:Secretmetadata:name:secret-dockercfgtype:kubernetes.io/dockercfgdata:.dockercfg:|    eyJhdXRocyI6eyJodHRwczovL2V4YW1wbGUvdjEvIjp7ImF1dGgiOiJvcGVuc2VzYW1lIn19fQo=
```

#### Note: If you do not want to perform the base64 encoding, you can choose to use the stringDatafield instead. 
When you create Docker config Secrets using a manifest, the API server checks whether the expected key exists in the datafield, and it verifies if the value provided can be parsed as a valid JSON. The API server doesn't validate if the JSON actually is a Docker config file. 
You can also use kubectlto create a Secret for accessing a container registry, such as when you don't have a Docker configuration file: 
```
kubectl create secret docker-registry secret-tiger-docker \
  --docker-email=tiger@acme.example \
  --docker-username=tiger \
  --docker-password=pass1234 \
  --docker-server=my-registry.example:5000

```

This command creates a Secret of type kubernetes.io/dockerconfigjson. 
Retrieve the .data.dockerconfigjsonfield from that new Secret and decode the data: 
```
kubectl get secret secret-tiger-docker -o jsonpath='{.data.*}'| base64 -d

```

The output is equivalent to the following JSON document (which is also a valid Docker configuration file): 
```
{"auths":{"my-registry.example:5000":{"username":"tiger","password":"pass1234","email":"tiger@acme.example","auth":"dGlnZXI6cGFzczEyMzQ="}}}
```

#### Caution: 
The authvalue there is base64 encoded; it is obscured but not secret. Anyone who can read that Secret can learn the registry access bearer token. 
It is suggested to use credential providers to dynamically and securely provide pull secrets on-demand. 
### Basic authentication Secret 
The kubernetes.io/basic-authtype is provided for storing credentials needed for basic authentication. When using this Secret type, the datafield of the Secret must contain one of the following two keys: 
- username: the user name for authentication - password: the password or token for authentication 
Both values for the above two keys are base64 encoded strings. You can alternatively provide the clear text content using the stringDatafield in the Secret manifest. 
The following manifest is an example of a basic authentication Secret: secret/basicauth-secret.yaml
```
apiVersion:v1kind:Secretmetadata:name:secret-basic-authtype:kubernetes.io/basic-authstringData:username:admin# required field for kubernetes.io/basic-authpassword:t0p-Secret# required field for kubernetes.io/basic-auth
```

#### Note: The stringDatafield for a Secret does not work well with server-side apply. 
The basic authentication Secret type is provided only for convenience. You can create an Opaquetype for credentials used for basic authentication. However, using the defined and public Secret type ( kubernetes.io/basic-auth) helps other people to understand the purpose of your Secret, and sets a convention for what key names to expect. 
### SSH authentication Secrets 
The builtin type kubernetes.io/ssh-authis provided for storing data used in SSH authentication. When using this Secret type, you will have to specify a ssh-privatekeykey-value pair in the data(or stringData) field as the SSH credential to use. 
The following manifest is an example of a Secret used for SSH public/private key authentication: secret/ssh-auth-secret.yaml
```
apiVersion:v1kind:Secretmetadata:name:secret-ssh-authtype:kubernetes.io/ssh-authdata:# the data is abbreviated in this examplessh-privatekey:|    UG91cmluZzYlRW1vdGljb24lU2N1YmE=
```

The SSH authentication Secret type is provided only for convenience. You can create an Opaquetype for credentials used for SSH authentication. However, using the defined and public Secret type ( kubernetes.io/ssh-auth) helps other people to understand the purpose of your Secret, and sets a convention for what key names to expect. The Kubernetes API verifies that the required keys are set for a Secret of this type. 
#### Caution: SSH private keys do not establish trusted communication between an SSH client and host server on their own. A secondary means of establishing trust is needed to mitigate "man in the middle" attacks, such as a known_hostsfile added to a ConfigMap. 
### TLS Secrets 
The kubernetes.io/tlsSecret type is for storing a certificate and its associated key that are typically used for TLS. 
One common use for TLS Secrets is to configure encryption in transit for an Ingress , but you can also use it with other resources or directly in your workload. When using this type of Secret, the tls.keyand the tls.crtkey must be provided in the data(or stringData) field of the Secret configuration, although the API server doesn't actually validate the values for each key. 
As an alternative to using stringData, you can use the datafield to provide the base64 encoded certificate and private key. For details, see Constraints on Secret names and data . 
The following YAML contains an example config for a TLS Secret: secret/tls-auth-secret.yaml
```
apiVersion:v1kind:Secretmetadata:name:secret-tlstype:kubernetes.io/tlsdata:# values are base64 encoded, which obscures them but does NOT provide# any useful level of confidentiality# Replace the following values with your own base64-encoded certificate and key.tls.crt:"REPLACE_WITH_BASE64_CERT"tls.key:"REPLACE_WITH_BASE64_KEY"
```

The TLS Secret type is provided only for convenience. You can create an Opaquetype for credentials used for TLS authentication. However, using the defined and public Secret type ( kubernetes.io/tls) helps ensure the consistency of Secret format in your project. The API server verifies if the required keys are set for a Secret of this type. 
To create a TLS Secret using kubectl, use the tlssubcommand: 
```
kubectl create secret tls my-tls-secret \
  --cert=path/to/cert/file \
  --key=path/to/key/file

```

The public/private key pair must exist before hand. The public key certificate for --certmust be .PEM encoded and must match the given private key for --key. 
### Bootstrap token Secrets 
The bootstrap.kubernetes.io/tokenSecret type is for tokens used during the node bootstrap process. It stores tokens used to sign well-known ConfigMaps. 
A bootstrap token Secret is usually created in the kube-systemnamespace and named in the form bootstrap-token-<token-id>where <token-id>is a 6 character string of the token ID. 
As a Kubernetes manifest, a bootstrap token Secret might look like the following: secret/bootstrap-token-secret-base64.yaml
```
apiVersion:v1kind:Secretmetadata:name:bootstrap-token-5emitjnamespace:kube-systemtype:bootstrap.kubernetes.io/tokendata:auth-extra-groups:c3lzdGVtOmJvb3RzdHJhcHBlcnM6a3ViZWFkbTpkZWZhdWx0LW5vZGUtdG9rZW4=expiration:MjAyMC0wOS0xM1QwNDozOToxMFo=token-id:NWVtaXRqtoken-secret:a3E0Z2lodnN6emduMXAwcg==usage-bootstrap-authentication:dHJ1ZQ==usage-bootstrap-signing:dHJ1ZQ==
```

A bootstrap token Secret has the following keys specified under data: 
- token-id: A random 6 character string as the token identifier. Required. - token-secret: A random 16 character string as the actual token Secret. Required. - description: A human-readable string that describes what the token is used for. Optional. - expiration: An absolute UTC time using RFC3339 specifying when the token should be expired. Optional. - usage-bootstrap-<usage>: A boolean flag indicating additional usage for the bootstrap token. - auth-extra-groups: A comma-separated list of group names that will be authenticated as in addition to the system:bootstrappersgroup. 
You can alternatively provide the values in the stringDatafield of the Secret without base64 encoding them: secret/bootstrap-token-secret-literal.yaml
```
apiVersion:v1kind:Secretmetadata:# Note how the Secret is namedname:bootstrap-token-5emitj# A bootstrap token Secret usually resides in the kube-system namespacenamespace:kube-systemtype:bootstrap.kubernetes.io/tokenstringData:auth-extra-groups:"system:bootstrappers:kubeadm:default-node-token"expiration:"2020-09-13T04:39:10Z"# This token ID is used in the nametoken-id:"5emitj"token-secret:"kq4gihvszzgn1p0r"# This token can be used for authenticationusage-bootstrap-authentication:"true"# and it can be used for signingusage-bootstrap-signing:"true"
```

#### Note: The stringDatafield for a Secret does not work well with server-side apply. 
## Working with Secrets 
### Creating a Secret 
There are several options to create a Secret: 
- Use kubectl- Use a configuration file - Use the Kustomize tool 
#### Constraints on Secret names and data 
The name of a Secret object must be a valid DNS subdomain name . 
You can specify the dataand/or the stringDatafield when creating a configuration file for a Secret. The dataand the stringDatafields are optional. The values for all keys in the datafield have to be base64-encoded strings. If the conversion to base64 string is not desirable, you can choose to specify the stringDatafield instead, which accepts arbitrary strings as values. 
The keys of dataand stringDatamust consist of alphanumeric characters, -, _or .. All key-value pairs in the stringDatafield are internally merged into the datafield. If a key appears in both the dataand the stringDatafield, the value specified in the stringDatafield takes precedence. 
#### Size limit 
Individual Secrets are limited to 1MiB in size. This is to discourage creation of very large Secrets that could exhaust the API server and kubelet memory. However, creation of many smaller Secrets could also exhaust memory. You can use a resource quota to limit the number of Secrets (or other resources) in a namespace. 
### Editing a Secret 
You can edit an existing Secret unless it is immutable . To edit a Secret, use one of the following methods: 
- Use kubectl- Use a configuration file 
You can also edit the data in a Secret using the Kustomize tool . However, this method creates a new Secretobject with the edited data. 
Depending on how you created the Secret, as well as how the Secret is used in your Pods, updates to existing Secretobjects are propagated automatically to Pods that use the data. For more information, refer to Using Secrets as files from a Pod section. 
### Using a Secret 
Secrets can be mounted as data volumes or exposed as environment variables to be used by a container in a Pod. Secrets can also be used by other parts of the system, without being directly exposed to the Pod. For example, Secrets can hold credentials that other parts of the system should use to interact with external systems on your behalf. 
Secret volume sources are validated to ensure that the specified object reference actually points to an object of type Secret. Therefore, a Secret needs to be created before any Pods that depend on it. 
If the Secret cannot be fetched (perhaps because it does not exist, or due to a temporary lack of connection to the API server) the kubelet periodically retries running that Pod. The kubelet also reports an Event for that Pod, including details of the problem fetching the Secret. 
#### Optional Secrets 
When you reference a Secret in a Pod, you can mark the Secret as optional , such as in the following example. If an optional Secret doesn't exist, Kubernetes ignores it. secret/optional-secret.yaml
```
apiVersion:v1kind:Podmetadata:name:mypodspec:containers:- name:mypodimage:redisvolumeMounts:- name:foomountPath:"/etc/foo"readOnly:truevolumes:- name:foosecret:secretName:mysecretoptional:true
```

By default, Secrets are required. None of a Pod's containers will start until all non-optional Secrets are available. 
If a Pod references a specific key in a non-optional Secret and that Secret does exist, but is missing the named key, the Pod fails during startup. 
### Using Secrets as files from a Pod 
If you want to access data from a Secret in a Pod, one way to do that is to have Kubernetes make the value of that Secret be available as a file inside the filesystem of one or more of the Pod's containers. 
For instructions, refer to Create a Pod that has access to the secret data through a Volume . 
When a volume contains data from a Secret, and that Secret is updated, Kubernetes tracks this and updates the data in the volume, using an eventually-consistent approach. 
#### Note: A container using a Secret as a subPath volume mount does not receive automated Secret updates. 
The kubelet keeps a cache of the current keys and values for the Secrets that are used in volumes for pods on that node. You can configure the way that the kubelet detects changes from the cached values. The configMapAndSecretChangeDetectionStrategyfield in the kubelet configuration controls which strategy the kubelet uses. The default strategy is Watch. 
Updates to Secrets can be either propagated by an API watch mechanism (the default), based on a cache with a defined time-to-live, or polled from the cluster API server on each kubelet synchronisation loop. 
As a result, the total delay from the moment when the Secret is updated to the moment when new keys are projected to the Pod can be as long as the kubelet sync period + cache propagation delay, where the cache propagation delay depends on the chosen cache type (following the same order listed in the previous paragraph, these are: watch propagation delay, the configured cache TTL, or zero for direct polling). 
### Using Secrets as environment variables 
To use a Secret in an environment variable in a Pod: 
- For each container in your Pod specification, add an environment variable for each Secret key that you want to use to the env[].valueFrom.secretKeyReffield. - Modify your image and/or command line so that the program looks for values in the specified environment variables. 
For instructions, refer to Define container environment variables using Secret data . 
It's important to note that the range of characters allowed for environment variable names in pods is restricted . If any keys do not meet the rules, those keys are not made available to your container, though the Pod is allowed to start. 
### Container image pull Secrets 
If you want to fetch container images from a private repository, you need a way for the kubelet on each node to authenticate to that repository. You can configure image pull Secrets to make this possible. These Secrets are configured at the Pod level. 
#### Using imagePullSecrets 
The imagePullSecretsfield is a list of references to Secrets in the same namespace. You can use an imagePullSecretsto pass a Secret that contains a Docker (or other) image registry password to the kubelet. The kubelet uses this information to pull a private image on behalf of your Pod. See the PodSpec API for more information about the imagePullSecretsfield. 
##### Manually specifying an imagePullSecret 
You can learn how to specify imagePullSecretsfrom the container images documentation. 
##### Arranging for imagePullSecrets to be automatically attached 
You can manually create imagePullSecrets, and reference these from a ServiceAccount. Any Pods created with that ServiceAccount or created with that ServiceAccount by default, will get their imagePullSecretsfield set to that of the service account. See Add ImagePullSecrets to a service account for a detailed explanation of that process. 
### Using Secrets with static Pods 
You cannot use ConfigMaps or Secrets with static Pods . 
## Immutable Secrets FEATURE STATE: Kubernetes v1.21 [stable]
Kubernetes lets you mark specific Secrets (and ConfigMaps) as immutable . Preventing changes to the data of an existing Secret has the following benefits: 
- protects you from accidental (or unwanted) updates that could cause applications outages - (for clusters that extensively use Secrets - at least tens of thousands of unique Secret to Pod mounts), switching to immutable Secrets improves the performance of your cluster by significantly reducing load on kube-apiserver. The kubelet does not need to maintain a [watch] on any Secrets that are marked as immutable. 
### Marking a Secret as immutable 
You can create an immutable Secret by setting the immutablefield to true. For example, 
```
apiVersion:v1kind:Secretmetadata:...data:...immutable:true
```

You can also update any existing mutable Secret to make it immutable. 
#### Note: Once a Secret or ConfigMap is marked as immutable, it is not possible to revert this change nor to mutate the contents of the datafield. You can only delete and recreate the Secret. Existing Pods maintain a mount point to the deleted Secret - it is recommended to recreate these pods. 
## Information security for Secrets 
Although ConfigMap and Secret work similarly, Kubernetes applies some additional protection for Secret objects. 
Secrets often hold values that span a spectrum of importance, many of which can cause escalations within Kubernetes (e.g. service account tokens) and to external systems. Even if an individual app can reason about the power of the Secrets it expects to interact with, other apps within the same namespace can render those assumptions invalid. 
Authorization configuration affects how Secret data can be accessed within a namespace. For example, granting list or watch permissions on Secrets allows a subject to read all Secret data in that namespace, not only the Secrets explicitly referenced by its Pods. Restrict access to the minimum set of permissions required for a workload to function, and avoid granting broad roles such as cluster-adminunless required for administrative purposes. 
Also see the Authorization documentation . 
A Secret is only sent to a node if a Pod on that node requires it. For mounting Secrets into Pods, the kubelet stores a copy of the data into a tmpfsso that the confidential data is not written to durable storage. Once the Pod that depends on the Secret is deleted, the kubelet deletes its local copy of the confidential data from the Secret. 
There may be several containers in a Pod. By default, containers you define only have access to the default ServiceAccount and its related Secret. You must explicitly define environment variables or map a volume into a container in order to provide access to any other Secret. 
There may be Secrets for several Pods on the same node. However, only the Secrets that a Pod requests are potentially visible within its containers. Therefore, one Pod does not have access to the Secrets of another Pod. 
### Configure least-privilege access to Secrets 
To enhance the security measures around Secrets, use separate namespaces to isolate access to mounted secrets. 
#### Warning: Any containers that run with privileged: trueon a node can access all Secrets used on that node. 
## What's next 
- For guidelines to manage and improve the security of your Secrets, refer to Good practices for Kubernetes Secrets . - Learn how to manage Secrets using kubectl- Learn how to manage Secrets using config file - Learn how to manage Secrets using kustomize - Read the API reference for Secret
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified March 17, 2026 at 1:33 AM PST: Improve security clarification for Kubernetes Secrets (#54644) (8af7916eb8) 
- - - - - - 

- - - - 

### 📄 Source: [https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/)

Kubernetes 
- Documentation - Kubernetes Blog - Training - Careers - Partners - Community - Versions 
  - Release Information   - v1.36   - v1.35   - v1.34   - v1.33   - v1.32 - English 
  - 中文 (Chinese)   - বাংলা (Bengali)   - Français (French)   - Deutsch (German)   - हिन्दी (Hindi)   - Bahasa Indonesia (Indonesian)   - Italiano (Italian)   - 日本語 (Japanese)   - 한국어 (Korean)   - فارسی (Persian)   - Polski (Polish)   - Português (Portuguese)   - Русский (Russian)   - Español (Spanish)   - Українська (Ukrainian)   - Tiếng Việt (Vietnamese) - 
  - Light   - Dark   - Auto 
# Encrypting Confidential Data at Rest 
- - - - - - - - - - - - - - - - 
- 
  - 
    -   - 
    -     - 
      -       - 
        - 
          -           -           -           -           -           -           -           -           -       -     - 
      -       -       -       -       -   - 
    - 
      -       - 
        -         -         -         -         -         -         -         -         -         -       -       -     - 
      -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -     - 
      - 
        -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -         -         -       - 
        -         -         -         -         -         -         -         -       - 
        -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -     - 
      - 
        -         -       - 
        -         -       -   - 
    - 
      -       -       -     - 
      - 
        -         -         -         -         -         -         -         -         -       -       - 
        -         -         -         -         -       -       - 
        -         -         -         -         -         -       - 
        -         -         -         -         -         -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       - 
        -         -         -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       - 
        -         -         -         -         -         -         -       - 
        -         -         -         -         -         -         -         -         -         -     - 
      -       -       -       -       -       -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -     - 
      -       - 
        -         -       -       -       -       -       -     - 
      -       -       -       -     - 
      -       -       -       -     - 
      -       -       -       -     -     -     -   - 
    -     - 
      - 
        -       - 
        -       - 
        -       - 
        -       - 
        -       - 
        -     - 
      -       -       -       -     - 
      -       -       -       -     - 
      -       -     - 
      -       -       -       -     - 
      -       -       -       -       -     - 
      -       -       -   - 
    -     - 
      -       -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -     - 
      -       - 
        -         -         -         -         -         -       - 
        -       - 
        -       - 
        -       - 
        -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -       - 
        -         -       - 
        -       - 
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -         -       - 
        -       - 
        -         -       - 
        -         -         -         -         -       - 
        -       - 
        -       - 
        -         -         -         -       - 
        -         -         -         -         -         -       - 
        -         -         -       - 
        -         -         -         -         -         -       - 
        -     - 
      -       -       -       -       -       -       -     - 
      -       -       -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -     - 
      - 
        -         -         -         -         -         -         -         -         -         -         -         -         -         -         -     - 
      -       -       - 
        -         -         -         -         - 
          -           -           -         -         - 
          -           -           -         -         - 
          -           -         - 
          -         -         - 
          -           -           -           -           -           -           -           -           -           -           -           -           -           -           -         -         -         - 
          -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -           -         -         -         -         -         -         -         -         -         -         -         -         - 
          -           -         -         -         -         -         -         - 
          -         -         -         -         - 
          -           -           -           -           -           -         -         -         - 
          -           -           -           -           -           -         -         - 
          -           -         -         -         -       -       -       -       -       -       -     - 
      -     - 
      -       -       -       -       -       -       -     - 
      -     - 
      -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -       -     - 
      -       -       -     - 
      -       -     -   - 
    -     - 
      -       -       -       -       -     -     - 
      -       -       -       -     - 
      -       -     -     - 
      -       -       -     - 
      -       -       -       -       -       -       -     - 
      -       -       -       -       -       -       -     -     -   - 
- - - 
  -   -   - - 
  -   -   -   -   -   -   - - - - - - 
- - - - 
# Encrypting Confidential Data at Rest 
All of the APIs in Kubernetes that let you write persistent API resource data support at-rest encryption. For example, you can enable at-rest encryption for Secrets . This at-rest encryption is additional to any system-level encryption for the etcd cluster or for the filesystem(s) on hosts where you are running the kube-apiserver. 
This page shows how to enable and configure encryption of API data at rest. 
#### Note: 
This task covers encryption for resource data stored using the Kubernetes API . For example, you can encrypt Secret objects, including the key-value data they contain. 
If you want to encrypt data in filesystems that are mounted into containers, you instead need to either: 
- use a storage integration that provides encrypted volumes - encrypt the data within your own application 
## Before you begin 
- 
You need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a cluster, you can create one by using minikube or you can use one of these Kubernetes playgrounds: 
  - iximiuz Labs   - Killercoda   - KodeKloud - 
This task assumes that you are running the Kubernetes API server as a static pod on each control plane node. - 
Your cluster's control plane must use etcd v3.x (major version 3, any minor version). - 
To encrypt a custom resource, your cluster must be running Kubernetes v1.26 or newer. - 
To use a wildcard to match resources, your cluster must be running Kubernetes v1.27 or newer. 
To check the version, enter kubectl version. 
## Determine whether encryption at rest is already enabled 
By default, the API server stores plain-text representations of resources into etcd, with no at-rest encryption. 
The kube-apiserverprocess accepts an argument --encryption-provider-configthat specifies a path to a configuration file. The contents of that file, if you specify one, control how Kubernetes API data is encrypted in etcd. If you are running the kube-apiserver without the --encryption-provider-configcommand line argument, you do not have encryption at rest enabled. If you are running the kube-apiserver with the --encryption-provider-configcommand line argument, and the file that it references specifies the identityprovider as the first encryption provider in the list, then you do not have at-rest encryption enabled ( the default identityprovider does not provide any confidentiality protection. ) 
If you are running the kube-apiserver with the --encryption-provider-configcommand line argument, and the file that it references specifies a provider other than identityas the first encryption provider in the list, then you already have at-rest encryption enabled. However, that check does not tell you whether a previous migration to encrypted storage has succeeded. If you are not sure, see ensure all relevant data are encrypted . 
## Understanding the encryption at rest configuration 
```
---## CAUTION: this is an example configuration.#          Do not use this for your own cluster!#apiVersion:apiserver.config.k8s.io/v1kind:EncryptionConfigurationresources:- resources:- secrets- configmaps- pandas.awesome.bears.example# a custom resource APIproviders:# This configuration does not provide data confidentiality. The first# configured provider is specifying the "identity" mechanism, which# stores resources as plain text.#- identity:{}# plain text, in other words NO encryption- aesgcm:keys:- name:key1secret:c2VjcmV0IGlzIHNlY3VyZQ==- name:key2secret:dGhpcyBpcyBwYXNzd29yZA==- aescbc:keys:- name:key1secret:c2VjcmV0IGlzIHNlY3VyZQ==- name:key2secret:dGhpcyBpcyBwYXNzd29yZA==- secretbox:keys:- name:key1secret:YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXoxMjM0NTY=- resources:- eventsproviders:- identity:{}# do not encrypt Events even though *.* is specified below- resources:- '*.apps'# wildcard match requires Kubernetes 1.27 or laterproviders:- aescbc:keys:- name:key2secret:c2VjcmV0IGlzIHNlY3VyZSwgb3IgaXMgaXQ/Cg==- resources:- '*.*'# wildcard match requires Kubernetes 1.27 or laterproviders:- aescbc:keys:- name:key3secret:c2VjcmV0IGlzIHNlY3VyZSwgSSB0aGluaw==
```

Each resourcesarray item is a separate config and contains a complete configuration. The resources.resourcesfield is an array of Kubernetes resource names ( resourceor resource.group) that should be encrypted like Secrets, ConfigMaps, or other resources. 
If custom resources are added to EncryptionConfigurationand the cluster version is 1.26 or newer, any newly created custom resources mentioned in the EncryptionConfigurationwill be encrypted. Any custom resources that existed in etcd prior to that version and configuration will be unencrypted until they are next written to storage. This is the same behavior as built-in resources. See the Ensure all secrets are encrypted section. 
The providersarray is an ordered list of the possible encryption providers to use for the APIs that you listed. Each provider supports multiple keys - the keys are tried in order for decryption, and if the provider is the first provider, the first key is used for encryption. 
Only one provider type may be specified per entry ( identityor aescbcmay be provided, but not both in the same item). The first provider in the list is used to encrypt resources written into the storage. When reading resources from storage, each provider that matches the stored data attempts in order to decrypt the data. If no provider can read the stored data due to a mismatch in format or secret key, an error is returned which prevents clients from accessing that resource. 
EncryptionConfigurationsupports the use of wildcards to specify the resources that should be encrypted. Use ' *.<group>' to encrypt all resources within a group (for eg ' *.apps' in above example) or ' *.*' to encrypt all resources. ' *.' can be used to encrypt all resource in the core group. ' *.*' will encrypt all resources, even custom resources that are added after API server start. 
#### Note: Use of wildcards that overlap within the same resource list or across multiple entries are not allowed since part of the configuration would be ineffective. The resourceslist's processing order and precedence are determined by the order it's listed in the configuration. 
If you have a wildcard covering resources and want to opt out of at-rest encryption for a particular kind of resource, you achieve that by adding a separate resourcesarray item with the name of the resource that you want to exempt, followed by a providersarray item where you specify the identityprovider. You add this item to the list so that it appears earlier than the configuration where you do specify encryption (a provider that is not identity). 
For example, if ' *.*' is enabled and you want to opt out of encryption for Events and ConfigMaps, add a new earlier item to the resources, followed by the providers array item with identityas the provider. The more specific entry must come before the wildcard entry. 
The new item would look similar to: 
```
...- resources:- configmaps.# specifically from the core API group,# because of trailing "."- eventsproviders:- identity:{}# and then other entries in resources
```

Ensure that the exemption is listed before the wildcard ' *.*' item in the resources array to give it precedence. 
For more detailed information about the EncryptionConfigurationstruct, please refer to the encryption configuration API . 
#### Caution: 
If any resource is not readable via the encryption configuration (because keys were changed), and you cannot restore a working configuration, your only recourse is to delete that entry from the underlying etcd directly. 
Any calls to the Kubernetes API that attempt to read that resource will fail until it is deleted or a valid decryption key is provided. 
### Available providers 
Before you configure encryption-at-rest for data in your cluster's Kubernetes API, you need to select which provider(s) you will use. 
The following table describes each available provider. Providers for Kubernetes encryption at rest 
|  Name  | Encryption  | Strength  | Speed  | Key length  |
|  identity  | None  | N/A  | N/A  | N/A  |
|  Resources written as-is without encryption. When set as the first provider, the resource will be decrypted as new values are written. Existing encrypted resources are not automatically overwritten with the plaintext data. The identity provider is the default if you do not specify otherwise.  |
|  aescbc  | AES-CBC with PKCS#7 padding  | Weak  | Fast  | 16, 24, or 32-byte  |
|  Not recommended due to CBC's vulnerability to padding oracle attacks. Key material accessible from control plane host.  |
|  aesgcm  | AES-GCM with random nonce  | Must be rotated every 200,000 writes  | Fastest  | 16, 24, or 32-byte  |
|  Not recommended for use except when an automated key rotation scheme is implemented. Key material accessible from control plane host.  |
|  kms v1 (deprecated since Kubernetes v1.28)  | Uses envelope encryption scheme with DEK per resource.  | Strongest  | Slow ( compared to kms version 2 )  | 32-bytes  |
|  Data is encrypted by data encryption keys (DEKs) using AES-GCM; DEKs are encrypted by key encryption keys (KEKs) according to configuration in Key Management Service (KMS). Simple key rotation, with a new DEK generated for each encryption, and KEK rotation controlled by the user. Read how to configure the KMS V1 provider .  |
|  kms v2  | Uses envelope encryption scheme with DEK per API server.  | Strongest  | Fast  | 32-bytes  |
|  Data is encrypted by data encryption keys (DEKs) using AES-GCM; DEKs are encrypted by key encryption keys (KEKs) according to configuration in Key Management Service (KMS). Kubernetes generates a new DEK per encryption from a secret seed. The seed is rotated whenever the KEK is rotated. A good choice if using a third party tool for key management. Available as stable from Kubernetes v1.29. Read how to configure the KMS V2 provider .  |
|  secretbox  | XSalsa20 and Poly1305  | Strong  | Faster  | 32-byte  |
|  Uses relatively new encryption technologies that may not be considered acceptable in environments that require high levels of review. Key material accessible from control plane host.  |
The identityprovider is the default if you do not specify otherwise. The identityprovider does not encrypt stored data and provides no additional confidentiality protection. 
### Key storage 
#### Local key storage 
Encrypting secret data with a locally managed key protects against an etcd compromise, but it fails to protect against a host compromise. Since the encryption keys are stored on the host in the EncryptionConfiguration YAML file, a skilled attacker can access that file and extract the encryption keys. 
#### Managed (KMS) key storage 
The KMS provider uses envelope encryption : Kubernetes encrypts resources using a data key, and then encrypts that data key using the managed encryption service. Kubernetes generates a unique data key for each resource. The API server stores an encrypted version of the data key in etcd alongside the ciphertext; when reading the resource, the API server calls the managed encryption service and provides both the ciphertext and the (encrypted) data key. Within the managed encryption service, the provider use a key encryption key to decipher the data key, deciphers the data key, and finally recovers the plain text. Communication between the control plane and the KMS requires in-transit protection, such as TLS. 
Using envelope encryption creates dependence on the key encryption key, which is not stored in Kubernetes. In the KMS case, an attacker who intends to get unauthorised access to the plaintext values would need to compromise etcd and the third-party KMS provider. 
### Protection for encryption keys 
You should take appropriate measures to protect the confidential information that allows decryption, whether that is a local encryption key, or an authentication token that allows the API server to call KMS. 
Even when you rely on a provider to manage the use and lifecycle of the main encryption key (or keys), you are still responsible for making sure that access controls and other security measures for the managed encryption service are appropriate for your security needs. 
## Encrypt your data 
### Generate the encryption key 
The following steps assume that you are not using KMS, and therefore the steps also assume that you need to generate an encryption key. If you already have an encryption key, skip to Write an encryption configuration file . 
#### Caution: 
Storing the raw encryption key in the EncryptionConfig only moderately improves your security posture, compared to no encryption. 
For additional secrecy, consider using the kmsprovider as this relies on keys held outside your Kubernetes cluster. Implementations of kmscan work with hardware security modules or with encryption services managed by your cloud provider. 
To learn about setting up encryption at rest using KMS, see Using a KMS provider for data encryption . The KMS provider plugin that you use may also come with additional specific documentation. 
Start by generating a new encryption key, and then encode it using base64: 
- Linux - macOS - Windows 
Generate a 32-byte random key and base64 encode it. You can use this command: 
```
head -c 32 /dev/urandom | base64

```

You can use /dev/hwrnginstead of /dev/urandomif you want to use your PC's built-in hardware entropy source. Not all Linux devices provide a hardware random generator. 
Generate a 32-byte random key and base64 encode it. You can use this command: 
```
head -c 32 /dev/urandom | base64

```

Generate a 32-byte random key and base64 encode it. You can use this command: 
```
# Do not run this in a session where you have set a random number# generator seed.[Convert]::ToBase64String((1..32|%{[byte](Get-Random-Max256)}))
```

#### Note: Keep the encryption key confidential, including while you generate it and ideally even after you are no longer actively using it. 
### Replicate the encryption key 
Using a secure mechanism for file transfer, make a copy of that encryption key available to every other control plane host. 
At a minimum, use encryption in transit - for example, secure shell (SSH). For more security, use asymmetric encryption between hosts, or change the approach you are using so that you're relying on KMS encryption. 
### Write an encryption configuration file 
#### Caution: The encryption configuration file may contain keys that can decrypt content in etcd. If the configuration file contains any key material, you must properly restrict permissions on all your control plane hosts so only the user who runs the kube-apiserver can read this configuration. 
Create a new encryption configuration file. The contents should be similar to: 
```
---apiVersion:apiserver.config.k8s.io/v1kind:EncryptionConfigurationresources:- resources:- secrets- configmaps- pandas.awesome.bears.exampleproviders:- aescbc:keys:- name:key1# See the following text for more details about the secret valuesecret:<BASE 64 ENCODED SECRET>- identity:{}# this fallback allows reading unencrypted secrets;# for example, during initial migration
```

To create a new encryption key (that does not use KMS), see Generate the encryption key . 
### Use the new encryption configuration file 
You will need to mount the new encryption config file to the kube-apiserverstatic pod. Here is an example on how to do that: 
- 
Save the new encryption config file to /etc/kubernetes/enc/enc.yamlon the control-plane node. - 
Edit the manifest for the kube-apiserverstatic pod: /etc/kubernetes/manifests/kube-apiserver.yamlso that it is similar to: 
```
---## This is a fragment of a manifest for a static Pod.# Check whether this is correct for your cluster and for your API server.#apiVersion:v1kind:Podmetadata:annotations:kubeadm.kubernetes.io/kube-apiserver.advertise-address.endpoint:10.20.30.40:443creationTimestamp:nulllabels:app.kubernetes.io/component:kube-apiservertier:control-planename:kube-apiservernamespace:kube-systemspec:containers:- command:- kube-apiserver...- --encryption-provider-config=/etc/kubernetes/enc/enc.yaml # add this linevolumeMounts:...- name:enc                          # add this linemountPath:/etc/kubernetes/enc     # add this linereadOnly:true# add this line...volumes:...- name:enc                            # add this linehostPath:# add this linepath:/etc/kubernetes/enc          # add this linetype:DirectoryOrCreate            # add this line...
```
- 
Restart your API server. 
#### Caution: Your config file contains keys that can decrypt the contents in etcd, so you must properly restrict permissions on your control-plane nodes so only the user who runs the kube-apiservercan read it. 
You now have encryption in place for one control plane host. A typical Kubernetes cluster has multiple control plane hosts, so there is more to do. 
### Reconfigure other control plane hosts 
If you have multiple API servers in your cluster, you should deploy the changes in turn to each API server. 
#### Caution: 
For cluster configurations with two or more control plane nodes, the encryption configuration should be identical across each control plane node. 
If there is a difference in the encryption provider configuration between control plane nodes, this difference may mean that the kube-apiserver can't decrypt data. 
When you are planning to update the encryption configuration of your cluster, plan this so that the API servers in your control plane can always decrypt the stored data (even part way through rolling out the change). 
Make sure that you use the same encryption configuration on each control plane host. 
### Verify that newly written data is encrypted 
Data is encrypted when written to etcd. After restarting your kube-apiserver, any newly created or updated Secret (or other resource kinds configured in EncryptionConfiguration) should be encrypted when stored. 
To check this, you can use the etcdctlcommand line program to retrieve the contents of your secret data. 
This example shows how to check this for encrypting the Secret API. 
- 
Create a new Secret called secret1in the defaultnamespace: 
```
kubectl create secret generic secret1 -n default --from-literal=mykey=mydata

```
- 
Using the etcdctlcommand line tool, read that Secret out of etcd: 
```
ETCDCTL_API=3 etcdctl get /registry/secrets/default/secret1 [...] | hexdump -C

```

where [...]must be the additional arguments for connecting to the etcd server. 
For example: 
```
ETCDCTL_API=3 etcdctl \
   --cacert=/etc/kubernetes/pki/etcd/ca.crt   \
   --cert=/etc/kubernetes/pki/etcd/server.crt \
   --key=/etc/kubernetes/pki/etcd/server.key  \
   get /registry/secrets/default/secret1 | hexdump -C

```

The output is similar to this (abbreviated): 
```
000000002f72656769737472792f736563726574|/registry/secret|00000010732f64656661756c742f736563726574|s/default/secret|00000020310a6b38733a656e633a616573636263|1.k8s:enc:aescbc|000000303a76313a6b6579313ac76ce7d309bc06|:v1:key1:.l.....|00000040255191e4e06ce5b14d7a8b3db9c27c6e|%Q...l..Mz.=..|n|00000050b479df0528ae0d8e5f35132cc018993e|.y..(..._5.,...>|[...]00000110233a0dfc28ca482d6b2d46cc720b704c|#:..(.H-k-F.r.pL|00000120a5fc3543124e60efbf6ffecfdf0bad1f|..5C.N`..o......|0000013082c4885302da3e66ff0a|...S..>f..|0000013a
```
- 
Verify the stored Secret is prefixed with k8s:enc:aescbc:v1:which indicates the aescbcprovider has encrypted the resulting data. Confirm that the key name shown in etcdmatches the key name specified in the EncryptionConfigurationmentioned above. In this example, you can see that the encryption key named key1is used in etcdand in EncryptionConfiguration. - 
Verify the Secret is correctly decrypted when retrieved via the API: 
```
kubectl get secret secret1 -n default -o yaml

```

The output should contain mykey: bXlkYXRh, with contents of mydataencoded using base64; read decoding a Secret to learn how to completely decode the Secret. 
### Ensure all relevant data are encrypted 
It's often not enough to make sure that new objects get encrypted: you also want that encryption to apply to the objects that are already stored. 
For this example, you have configured your cluster so that Secrets are encrypted on write. Performing a replace operation for each Secret will encrypt that content at rest, where the objects are unchanged. 
You can make this change across all Secrets in your cluster: 
```
# Run this as an administrator that can read and write all Secretskubectl get secrets --all-namespaces -o json | kubectl replace -f -

```

The command above reads all Secrets and then updates them with the same data, in order to apply server side encryption. 
#### Note: 
If an error occurs due to a conflicting write, retry the command. It is safe to run that command more than once. 
For larger clusters, you may wish to subdivide the Secrets by namespace, or script an update. 
## Prevent plain text retrieval 
If you want to make sure that the only access to a particular API kind is done using encryption, you can remove the API server's ability to read that API's backing data as plaintext. 
#### Warning: 
Making this change prevents the API server from retrieving resources that are marked as encrypted at rest, but are actually stored in the clear. 
When you have configured encryption at rest for an API (for example: the API kind Secret, representing secretsresources in the core API group), you must ensure that all those resources in this cluster really are encrypted at rest. Check this before you carry on with the next steps. 
Once all Secrets in your cluster are encrypted, you can remove the identitypart of the encryption configuration. For example: 
```
---apiVersion:apiserver.config.k8s.io/v1kind:EncryptionConfigurationresources:- resources:- secretsproviders:- aescbc:keys:- name:key1secret:<BASE 64 ENCODED SECRET>- identity:{}# REMOVE THIS LINE
```

…and then restart each API server in turn. This change prevents the API server from accessing a plain-text Secret, even by accident. 
## Rotate a decryption key 
Changing an encryption key for Kubernetes without incurring downtime requires a multi-step operation, especially in the presence of a highly-available deployment where multiple kube-apiserverprocesses are running. 
- Generate a new key and add it as the second key entry for the current provider on all control plane nodes. - Restart all kube-apiserverprocesses, to ensure each server can decrypt any data that are encrypted with the new key. - Make a secure backup of the new encryption key. If you lose all copies of this key you would need to delete all the resources were encrypted under the lost key, and workloads may not operate as expected during the time that at-rest encryption is broken. - Make the new key the first entry in the keysarray so that it is used for encryption-at-rest for new writes - Restart all kube-apiserverprocesses to ensure each control plane host now encrypts using the new key - As a privileged user, run kubectl get secrets --all-namespaces -o json | kubectl replace -f -to encrypt all existing Secrets with the new key - After you have updated all existing Secrets to use the new key and have made a secure backup of the new key, remove the old decryption key from the configuration. 
## Decrypt all data 
This example shows how to stop encrypting the Secret API at rest. If you are encrypting other API kinds, adjust the steps to match. 
To disable encryption at rest, place the identityprovider as the first entry in your encryption configuration file: 
```
---apiVersion:apiserver.config.k8s.io/v1kind:EncryptionConfigurationresources:- resources:- secrets# list any other resources here that you previously were# encrypting at restproviders:- identity:{}# add this line- aescbc:keys:- name:key1secret:<BASE 64 ENCODED SECRET># keep this in place# make sure it comes after "identity"
```

Then run the following command to force decryption of all Secrets: 
```
kubectl get secrets --all-namespaces -o json | kubectl replace -f -

```

Once you have replaced all existing encrypted resources with backing data that don't use encryption, you can remove the encryption settings from the kube-apiserver. 
## Configure automatic reloading 
You can configure automatic reloading of encryption provider configuration. That setting determines whether the API server should load the file you specify for --encryption-provider-configonly once at startup, or automatically whenever you change that file. Enabling this option allows you to change the keys for encryption at rest without restarting the API server. 
To allow automatic reloading, configure the API server to run with: --encryption-provider-config-automatic-reload=true. When enabled, file changes are polled every minute to observe the modifications. The apiserver_encryption_config_controller_automatic_reload_last_timestamp_secondsmetric identifies when the new config becomes effective. This allows encryption keys to be rotated without restarting the API server. 
## What's next 
- Read about decrypting data that are already stored at rest - Learn more about the EncryptionConfiguration configuration API (v1) . 
## Feedback 
Was this page helpful? Yes No 
Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on Stack Overflow . Open an issue in the GitHub Repository if you want to report a problem or suggest an improvement . Last modified May 09, 2025 at 12:28 PM PST: Sync encryption docs reviewers with kubernetes sig-auth-encryption-at-rest-reviewers (4e42436cf9) 
- - - - - - 

- - - - 
