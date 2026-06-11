---
tags:
  - kubernetes
Type: Reference Note
source: Elfakharny-Kubernetes-Udemy-Course
page: "-"
links: 
flogetzzel:
---
when a cluster is made the first user created is the cluster admin and privilege level to do anything on the cluster he modify any abject or delete any object. The most dangerous account on the cluster 

The normal approach is to create to do my daily tasks on the cluster, because if the cluster credentials got leaked an unknown user will have full access to my cluster, so its by conviction when the cluster is created and running normal the first thing we do is create an account that has privileges just enough to preform the tasks assigned to the individual in my team 


to understand RBAC in the process

General security concept 
Authentication --> is to define a user to the system
SSO -> a single sign on with it a user can access multiple systems in the organization ليك حق الدخول ولا لأ

authorization --> the things that Iam allowed to do on the system once Iam authenticated 

in kubernetes its very restricted by default you have zero authorizations 

 Authorization are assigned is through RBAC so its an authorization system 

RBAC:

ROLE ---------------------------------------------------- SUBJECT 
![[Pasted image 20250427112916.png]]

- The subject can be a user that has Role 
- The subject can a group of user that all share the same Role 
- The subject can be a ServiceAccount that is used by an object such like a bot or a pod that perform certain actions on the cluster (refer to the jobs section)


![[Pasted image 20250524212213.png]]


The role manifest defines the authorization given to a user Group or service account, when we want a resource such as a daemon set or a Job or a normal pod to create another resource on the cluster it must have authentication and authorization to contact the 
Api-server so we use a service account with the least possible privileges to execute the tasks needed  

role bind is a kubernetes object to attach the Role object to the subject 

![[Pasted image 20250524212851.png]]

apiVersion ---> rbac.authorization.k8s.io this is a kubernetes resource group and we use v1 of that group
its just a logical organization of resources related to each other 
remember in Deployment and replica-set the apiVersion was app/v1 
the logical group was app 





![[Pasted image 20250524213500.png]]

Role-bind to attach the role to a subject 





