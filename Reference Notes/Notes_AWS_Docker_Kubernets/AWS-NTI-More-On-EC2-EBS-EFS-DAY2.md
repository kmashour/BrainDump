

EBS is zonal scope available over the same AZ to copy it across AZ we need to take snapshot and copy it to another zone or region 


We can create a EC2 based on EBS volume with all our configuration in an AMI as template for fast bring up 

EBS can be backed up manually or automatically 

EFS is available over the VPC so any AZ under the VPC can use the EFS its like NAT a Paas everything is handled by aws scaling and backups so aws ensures that my data on efs will always be availabe 

EFS is inside the VPC for security reasons so no one could access it 