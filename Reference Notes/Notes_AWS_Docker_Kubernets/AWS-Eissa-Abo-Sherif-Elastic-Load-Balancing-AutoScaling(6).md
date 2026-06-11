

EBS Snapshot its a best practice to always take snapshots of you EBS as backups 

Amazon S3 bucket will be on the same region, We can Copy the snapshot on another region its acceptable, The S3 will be automatically created by amazon no need for me to handle anything  
Snapshots is accessed in EC2 Dashboard i don't have an access to the S3 Bucket 

![[Pasted image 20250501132311.png]]

![[Pasted image 20250501132337.png]]


Through DLM or cloud watch events you can set expiration Date for the snapshots and according to the case scenario we set the expiration date...(THINK OF IT AS EBS ORCHESTERATOR)

cloud watch handles  1 ---> EBS 
DLM handles multiple ---> EBS 
![[Pasted image 20250501132138.png]]


-------------
===================================================================

Encryption Occurs on the EC2 Host so its Encrypted on Transit and sits Encrypted in the EBS Encrypted all the way ... 

The Decryption happens on the EC2 host only so the host can use the data 

EBS works with symmetric keys as from 2021 

![[Pasted image 20250501132728.png]]

KMS ---> Key management System

The CMK's never leaves the KMS, we give desired accounts or user access permissions to the KMS but we never share the CMK 

we use AWS manged keys ( default CMK ), every thing is handled by aws I can only see logs for auditing

unlike customer managed keys every thing is managed by me 
- Rotation
- policies for who can use it
- Change key periodically 
- Auditing on key usage 

-------------------
====================================================================

![[Pasted image 20250501133758.png]]


EBS is available For a specific AZ 
Snapshot is available across the region all AZ's under the same region 
Snapshot can be saved in other Regions under EC2 snapshot it will be found 

so snapshot can break all EC2 limits 

--------------------------------
====================================================================

The Best approach is to know if i want to create an Encrypted EBS volume or not before doing it, there are work around if I wanted to encrypt it after it was created but its a hassle..........

![[Pasted image 20250501134724.png]]


![[Pasted image 20250501135856.png]]


![[Pasted image 20250501135951.png]]



Encryption and Decryption of data stored in EBS happens on the EC2 instance !! so as we can see there no direct way or a work around to change the state of an encrypted volume to Unencrypted 

In such situations we Can do the following 
- Attach a new EBS unencrypted volume to the same EC2  
- Copy the Encrypted data to the new unencrypted volume 
- The data will be unencrypted on the host and will be saved in the new unencrypted volume without encryption 

----------------------
====================================================================

So Can I share the snapshot if i have multiple accounts in the organization 

by default a snapshot is available for the account created it only 

![[Pasted image 20250501140208.png]]

So we if we use amazon CMK the snapshot won't be shared, so we can do the copy and change CMK with something other than the default with the new snap shot to be shareable 

-------------------------
====================================================================

Any EBS or snapshot or copy will be encrypted within the scope of a region 


![[Pasted image 20250501143408.png]]
![[Pasted image 20250501143437.png]]![[Pasted image 20250501143449.png]]


-----------
===================================================================


Creating your Golden AMI -- hell yeah 
![[Pasted image 20250501161951.png]]

![[Pasted image 20250501170504.png]] 


---------------------------
====================================================================

![[Pasted image 20250501171718.png]]

![[Pasted image 20250501171731.png]] 


------------------
====================================================================

![[Pasted image 20250501172220.png]]


================================================================================================================================================================================================================================================================================

Elastic Load balancing 

Internet Facing Load Balancer 
Internal Load Balancer 



LB -- > Amazon recommend to deploy LB at 2 AZ in the same region...

LB between regions won't work LB is regional  **Many make this mistake thinking they can load balance an app between regions**



![[Pasted image 20250501174421.png]]


![[Pasted image 20250501174556.png]]


![[Pasted image 20250501174857.png]] 

Network load balancer offers the best performance performance we can use it as long as we don't need it to work on layer 7  

classic load balancer and application load balancer can a security groups configures, as of 2023 Network load balancer can have security groups configured 

![[Pasted image 20250501175443.png]]


![[Pasted image 20250501180443.png]]


![[Pasted image 20250501180459.png]]

If all Az's where unhealthy the LB just forward the traffic to all hopping it that traffic may reach a healthy target but it won't drop the traffic if 404 error of any kind came it will be a response from the failed EC2  


![[Pasted image 20250501180910.png]]

Its better for LB health checks to be on the same port thats running the application 

![[Pasted image 20250501181431.png]]

load balancer rules executed according to the order they are listed in so you need to put that in mind 

--------------------------------------------------------
====================================================================

Cross-Zone LB disabled The traffic is not divided according to EC2
every time a request is forwarded to an AZ... They have different number of EC2 

![[Pasted image 20250502101828.png]]

Cross zone lb The traffic is forwarded to all registered healthy EC2 instance by default enabled in Application load balancer and it charges in Network load balancer 

![[Pasted image 20250502102957.png]]



----------------
====================================================================

![[Pasted image 20250502103308.png]]

----------------------------------------
====================================================================

A load balancer node is defined in a public subnet if its a Internet facing load balancer 

We have one ENI-ELB per AZ with a public IP to connect with the public network and a private IP

Now to increase security measures we can place the interface of the application in a private subnet 


![[Pasted image 20250502103329.png]]

------------------------
====================================================================

![[Pasted image 20250502103846.png]]


**we can use gateway end-point for private subnets to connect to aws services** 
 
--------------------------------------------------------------------====================================================================

![[Pasted image 20250502120105.png]]


![[Pasted image 20250502120344.png]]


 ![[Pasted image 20250502120600.png]]


--------------------------------------------------------------------====================================================================

![[Pasted image 20250502122540.png]]
 
![[Pasted image 20250502122648.png]] 

![[Pasted image 20250502123036.png]]

 ![[Pasted image 20250502123257.png]]
![[Pasted image 20250502123408.png]]

![[Pasted image 20250502124046.png]]



![[Pasted image 20250502124150.png]]


![[Pasted image 20250502124835.png]]


--------------------------------------------------------------------====================================================================


![[Pasted image 20250502125222.png]]

Application load balancer 
Remember x-forwarded is the client public id found in the layer 7 header of the request 

Network load balancer 
Proxy protocol stores the ip of the client in the layer 4 message payload itself if we are not using target groups 

![[Pasted image 20250502125852.png]]