Enterprise and Enterprise Ramp-On 
TAM --- Support Roles ,Proactive Approaches

![[Pasted image 20250722211238.png]]

AWS Expects 
 - operational Excellence through 
	- use automation whenever possible --> 
	  speed , less human intervention = less human errors

	- Monitor and track everything --> track running metrics (CPU,NETWORK,BOTTLENECK,IO)
	
	- Continuous improvement

 - Security 
	- Use "least-privilege" access --> each service/user has the least needed privileges to operate (المعرفه علي قدر الاحتياج)
	
	- Use Multifactor Authentication
	
	- Use IAM (Identity and Access Management) --> AWS expects us to use this service to set policies for users 
	
	- Protect data in-transit and at rest --> AWS expects us encrypt data in both states 
	
	- Monitor and Audit continuously
	  Audit : event logs for actions that happens on the system

 - Reliability  موثوقيه 
	- Implement Disaster Recovery techniques --> 
	  Design for failure
	
	- Make use of Autoscaling 
	
	- Test and validate regulary --> Try fail over scenario in disaster recovery  

 - Performance Efficiency 
	- choose the right tool for the job 
	  Lets we used EBS storage services for storage only while it is designed to able to work with EC2 instances so it was more appropriate to use S3 bucket, using EBS is money waste we didn't fully utilize its function
	
	- Optimize resource utilization and implement scaling --> start with average needed resources and scale when in demand, Cost effective approach.
	
	- user performance benchmarks --> Test the application on different traffic scenarios to have a sense of accurate Resource requirement according to demand and traffic on my app for better performance efficiency (creating a benchmark)

 - Cost Optimization 
	- use the right instance type
	
	- use AWS cost saving plans(Reserved Instance , Spot instances)
	
	- monitor and track costs 

 - Sustainability   استدامه 
	- Use environment friendly resources 
	- terminate any unused (idle) resources



Fault Tolerance 

 ![[Pasted image 20250722214026.png]]

  With the load balancer and the two EC2 instance we achieved high availability, Now suppose we added an Autoscaling group to guarantee the existence of two EC2 instance so if of one of the two EC2 terminated the AG will create another one in any of the two AZ either the same or another available its AG responsibility, so by adding two EC2 with LB we are highly available but the AG should be added and its always comes with a package when LB is mentioned  

 But are we 100% fault tolerant ?? 
 Absolutely not because when AG executes the Boot time may be minutes so the application behavior will be affected until its ready to receive traffic  

 In case of using container instead of VM the boot process will be faster and in scenarios like these we may be fault tolerant 

 To be fault tolerant 
 Suppose a third AZ and its in the AG and the three instance is up and they are the minimum to run my app , with threshold 60% cpu usage now we guaranteed 100% fault tolerance and elasticity  



Trusted Advisor 
  slides 
