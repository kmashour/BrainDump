AWS --> HAS REGIONS 

Regions consist of availability zones --> Actual data centers

Edge locations --> **Edge locations are AWS data centers designed to deliver services with the lowest latency possible.** they are much more smaller than the Availability zones..

Ec2 instances which is a Vm on the cloud

vpc --> virtual private network it consist of a vpc cidr which is even divided into smaller subnet cidr all the EC2 instances is launched in the subnet, so vpc is like a virtual allocation of a large number of ips which is further divided into subnets 

The vpc can be on multiple AZs under the same region where they are divided into smaller number of subnets and can communicate directly with there private Ips 


In aws different subnet can communicate directly aslong as they share the same subnet 

up-till now every thing is within a virtual private network no one can access it from the outside and Ec2 instance can access the internet 

Public subnet --> all the Ec2 instances within that subnet can access the internet through the region public ips which is provided from aws to any instance within the public subnet 

private subnet --> any instance within that subnet will not be able to communicate with the outside world two ways inbound and outbound but its reachable from inside the VPC


IGW internet gateway --> Any VPC must and should have a IGW to accessible the from internet 

NAT --> Its activated in public subnet and is used as a tunnel to the private subnets to the internet by assigning a elastic public ip to the Ec2 instance within the private subnet 

Elastic public ip --> a ip assigned by NAT to private EC2 instances in a private subnet 

NACL NETWORK ACCESS LIST --> Its like a first layer firewall on the subnet, it allows all traffic by default 

SG security group --> Think of it as a 2nd layer firewall but on Ec2 instance and unique for every Ec2 

Route tables --> Define routing rules for a subnet so a public Ec2 instance can route to the IGW and a private EC2 instance can route to the NAT




