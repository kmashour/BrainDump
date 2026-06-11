# Introduction 
## project-1

![[Pasted image 20250508152603.png]]

![[Pasted image 20250508152636.png]]

## project-2 
![[Pasted image 20250509102913.png]]


![[Pasted image 20250509103328.png]]

## project 3
### Lab 
create a EC2 instance and list s3 buckets from the instance (policy)

``` AWS-CLI
aws s3 ls  
``` 

![[Pasted image 20250511001805.png]]

![[Pasted image 20250511002017.png]]

![[Pasted image 20250511004948.png]]
![[Pasted image 20250511005254.png]]


![[Pasted image 20250512085552.png]]

the Web/app programming will be modified to communicate with the SQS instead of the database 
**Lambda function is used in architectures like this to take the data in the SQS and write it in the RDS** 

![[Pasted image 20250512090125.png]]

Any Project that has Design requirements it is divided into functional requirements and non functional requirements 

we need to understand and study the platform in order to be able to design and implement according to the available services and its limitations 


![[Pasted image 20250512101213.png]]

![[Pasted image 20250512102552.png]]

----------


With the load balancer and the two EC2 instance we achieved high availability, Now suppose we added an Autoscaling group to guarantee the existence of two EC2 instance so if of one of the two EC2 terminated the AG will create another one in any of the two AZ either the same or another available its AG responsibility, so by adding two EC2 with LB we are highly available but the AG should be added and its always comes with a package when LB is mentioned  

But are we 100% fault tolerant ?? 
Absolutely not because when AG executes the Boot time may be minutes so the application behavior will be affected until its ready to receive traffic  

In case of using container instead of VM the boot process will be faster and in scenarios like these we may be fault tolerant 

To be fault tolerant 
Suppose a third AZ and its in the AG and the three instance is up and they are the minimum to run my app , with threshold 60% cpu usage now we guaranteed 100% fault tolerance and elasticity  


![[Pasted image 20250512104739.png]]










# VPC deep dive

![[Pasted image 20250516190254.png]]

With respect to only HA and fault tolerant creating two NAT gateways two bastion hosts that will do and of course the route table routes to the NAT in its AZ 

![[Pasted image 20250516190953.png]]

![[Pasted image 20250516231854.png]]

![[Pasted image 20250516232519.png]]




-----------
# AWS Elastic load balancer (ELB)
## project 1
working with health checks of load balancer groups 
![[Pasted image 20250529160044.png]]

## project 2
![[Pasted image 20250626140433.png]]

![[Pasted image 20250626140557.png]]

![[Pasted image 20250626141215.png]]




## project 3

![[Pasted image 20250626151341.png]]

![[Pasted image 20250626151400.png]]

## project 4

![[Pasted image 20250626150847.png]]

![[Pasted image 20250626150926.png]]




## Project 5

# AutoScaling Group
![[Pasted image 20250626165425.png]]

![[Pasted image 20250626165815.png]]