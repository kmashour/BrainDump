---
tags:
  - kubernetes
Type: Reference Note
source: Elfakharny-Kubernetes-Udemy-Course
page: "-"
links: 
flogetzzel:
---
Some data can't be just added to config maps because its confidential it needs to kept secret !! 

Most used :
opaque
image registry 
tls 

The secret is like config map in everything it can even be mounted as a volume as in ssh authentication, think of a secret as config map for credentials 

-------------------

 ![[Pasted image 20250426112349.png]]



 ![[Pasted image 20250426112223.png]]

 **Kubernetes in Opaque secret leaves the security to the kubernetes admin to add this secret to a namespace with controlled access over it, not anyone can just access that namespace and expose the secrets because in this type its not actually encrypted its just encoded so its very easy to just decode it, so the security here is that the secrets is placed in a namespace that has access bases on roles (RBAC)**

 There a 3rd party tools integrated with kubernetes to encrypt the secrets on  cloud or on premise, but either way when the secret is used inside kubernetes it must be in plain text so kubernetes could use it, so when the secret is used inside a kubernetes cluster the tool will decrypt it so kubernetes could use it, **THE TOOLS JUST ENCRYPT THE SECRET MANIFEST UNTIL ITS INSIDE THE CLUSTER**

 **kubectl exec -it POD_NAME -- env ---> the variable will be in plain text for sure in order for the containers to use it** , this command is running inside a container !!!


------------------

 ![[Pasted image 20250426113556.png]]
 The only difference between it and opaque is that the keys are defined tls.crt and tls.key 
 we can't use other keys because the application that uses this type of secrets will be searching for those values 



------------------------

 ![[Pasted image 20250426113913.png]]

  In this type of secrets we define our remote registry credentials to pull images from private registries this type of secretes is used with pods, the manifest of this type of secret is a bit complicated to implement. 
  **the imperative way of using this type of secret is much more convenient**.. Kubernetes convert the imperative commands and convert into a file and use the base64 encode
 ![[Pasted image 20250426113957.png]]
   of course if Iam using a parent component 
   (replica-set , daemoset , deployment , jobs) can implement it in the pod section   

---------------------
 service account, This account on any system refers to a service thats not used by humans its used by a pod , Api its just used by anything but a human  

 **In some scenarios a pod may need to construct a job so it will need an account on the cluster to perform this action** 

 The service account credentials is known to whole the team, and the pod should use it not a human in the same sense we did a service account so the pod wouldn't use a human account credentials 


 ![[Pasted image 20250426115107.png]]
 through this command a service account secret is created in the background, kubernetes handles it without the need of any intervention from me this credentials can used by API server for authentication but till now its useless because its only authenticated it won't be Authorized to do anything until we configure the RBAC ...
 So till now we only authenticated the service account but its crippled it can't do anything 
 ![[Pasted image 20250426115334.png]]


-------------------

 Basic authentication is one of oldest types of authentications in http servers like nginx and apache. when a user open a certain web page or the website itself it will prompt a username and password 
 
 ![[Pasted image 20250426115805.png]]
 this secret manifest must have the two keys 
 username: 
 password :

 This secret can be used in nginx manifest to implement the basic authentication and of course nginx must be configured for that (look into it just covered as a concept)

 ![[Pasted image 20250426115941.png]]

--------------

 ssh authentication secrets, least used of all secret types...
 we have two ways 
 username - password 
 public-private keys 

  When using the private key authentication we use volume mounting, the mount path is inside the container and automatically is sources from where the secret of type ssh-authentication is kept 

  ![[Pasted image 20250426120759.png]]
  ![[Pasted image 20250426120843.png]]
  A good practice when using mount only is to use readOnly so data won't be modified 
  