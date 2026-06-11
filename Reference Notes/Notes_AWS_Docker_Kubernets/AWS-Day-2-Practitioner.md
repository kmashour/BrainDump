### Module 3:AWS Global Infrastructure Overview
#### Regions and AZs

![[Pasted image 20250719153509.png]]

![[Pasted image 20250719153531.png]]

![[Pasted image 20250719153624.png]]

![[Pasted image 20250719153735.png]]

--------------------------
#### CloudFront service 

The website shows AWS global infrastructure with all its AZs and regions 

cloudFront is inside the edge locations 

the internet routes is not predictable so it can use a route in the request and use a completely different one in the reply so it will cause delay 


![[Pasted image 20250719154304.png]]

![[Pasted image 20250719154322.png]]


Request goes to the nearest edge location if is wasn't there its considered a miss a cache the CDN use aws backbone network to retrieve the data from the source and reply the data to the requester and when other users request the same data its cache hit faster in replying 


![[Pasted image 20250719154504.png]]

![[Pasted image 20250719154825.png]]![[Pasted image 20250719154834.png]]

------------
#### Services from the slides 
 services 
  ![[Pasted image 20250721012623.png]]

  ![[Pasted image 20250721012637.png]]


  ![[Pasted image 20250721012645.png]]

  ![[Pasted image 20250721012655.png]]

  ![[Pasted image 20250721012726.png]]

![Pasted image 20221031004509](https://user-images.githubusercontent.com/109697567/200856868-6a73eec2-b1b4-4fe3-b9a2-51e7f8099f82.png)

Security Groups
	  have only permit rules. no deny rules. If no permits are found it is considered as an implied deny.
	- Can add up to 16 (5 default maximum) Security Groups per EC2 instance.
	- Security Groups are stateful, meaning that if the traffic is allowed either if its inbound or outbound, the opposite direction response is automatically allowed even if no permit rules were found.
	![Pasted image 20221031231048](https://user-images.githubusercontent.com/109697567/200858159-50800cf5-62a4-461b-a96e-eb1f2da305ca.png)

NACL
	- NACL functions at a subnet level, so it's applied to all EC2 instances inside the subnet.
	- It's applied at the implied router
	- NACLs are **Stateless** "one way only".
	- It includes permit & deny rules.
	- Each NACL rule has a sequence number, rules are elevated from lowest to highest sequence number.
	- Once a rule is found either permit or deny the process is stopped "no reading for rest of the rules", if none are found it ends with explicit deny.
	- Traffic going into Subnet is called inbound traffic, & traffic from the Subnet is called outbound traffic.


-----------

### Module 4: AWS Cloud Security
#### shared responsibility model 
![[Pasted image 20250508105843.png]]

![[Pasted image 20250721002936.png]]

![[Pasted image 20250721003315.png]]

![[Pasted image 20250721003928.png]]

![[Pasted image 20250721004105.png]]

![[Pasted image 20250721004124.png]]

![[Pasted image 20250721004223.png]]

![[Pasted image 20250721004235.png]]


![[Pasted image 20250721004038.png]]


#### Securing new AWS account 

Walk-through 
 
![[Pasted image 20250508134144.png]] 

![Pasted image 20221020232823](https://user-images.githubusercontent.com/109697567/200856466-5ba41a25-b03d-4a30-90b4-052604d218dc.png)

Cloud Trail
	 Any actions "APIs" taken by IAM users, roles or AWS services are recorded in CloudTrail.
	- Events can be viewed & downloaded.
	- It helps in governance & auditing the account.
	- Events history are maintained for 90 days.
	- Logs can be stored in a S3 Bucket for more than 90 days if desired, **this is encrypted by default.**
	- CloudTrail is integrated with SNS.
	- A trail created in the console is a multi-region trail, use the command interface to make a region trail.
	  so Console cloud trail is multi-region scope
	  And CLI if I want to make a single region trail 


#### AWS KMS

![[Pasted image 20250721011129.png]]

![[Pasted image 20250721011108.png]]

![[Pasted image 20250721011156.png]]





#### AWS Cognito
![[Pasted image 20250721010454.png]]


#### AWS Shield
![[Pasted image 20250721011337.png]]

![[Pasted image 20250721011429.png]]




#### AWS Artifact 
![[Pasted image 20250721011753.png]]

AWS Config
![[Pasted image 20250721012119.png]]