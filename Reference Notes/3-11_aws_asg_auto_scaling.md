---
domains:
  - "aws"
class: reference-note
tier: reference-note
tags:
  - aws/autoscaling
---

# Module 3-11: AWS Auto Scaling Groups (ASG)

## Scalability & Elasticity
### Scalability 
- Scalability refers to system's ability to handle the growth of load by adding resources.
- This scaling can be vertical scaling (up/down) or horizontal scaling(out/in).
 ![Pasted image 20221103043119](https://user-images.githubusercontent.com/109697567/200859709-cc84e90c-9afd-4851-90fa-87e2878137ac.png)
### Elasticity 
  
- Elasticity describes the system ability to provision &  deprovision resources **automatically** to ensure that resources matches the need. 
- **Auto scaling groups can be configured for EC2 instances**, There  are another auto scaling type called Application Autoscaling will be covered later 
- **Autoscaling is always accompanied with load balancer** in design to ensure high availability  

> [!NOTE]
> - Remember we need to take in consideration the time need for horizontal scaling to start executing it needs triggers from cloud watch and autoscaling groups health checks then start in creating the EC2 instances and EC2 instance may need Minutes to initialize so if it was a 1 min spike in traffic, The application has failed to be fault tolerant we tackle more of this in later videos  

![[Pasted image 20250512092901.png]]

---

## 3. Auto Scaling Groups (ASG) Deep Dive
ASGs dynamically scale EC2 fleets based on CPU, network, or custom CloudWatch metrics.

### A. Lifecycle & Metrics

---

## Application Auto Scaling
Application Auto Scaling is a web service for automatically scaling resources for services beyond Amazon EC2. 
- It can be used with Auto Scaling and EC2 Auto Scaling to scale resources across multiple services including:
	- ECS services 
	- Spot Fleet requests
	- EMR Clusters 
	- AppStream 2.0 fleets
	- Aurora Replicas DynamoDB Read and Write Capacity units
	- SageMaker endpoints
	- Amazon Comprehend

---

## EC2 Auto Scaling
- It's a Regional service
- It can span multiple Availability Zones in the same AWS Region.
- It integrates with ELB, CloudWatch, and Cloud Trail.
- It is free to use, but customers pay only for EC2 and EBS resources used. 
- ASG will try to balance resources across Availability Zones.
- The EC2 Auto Scaling configuration components are:
	 - ##### An Auto Scaling Group 
		- Is the logical grouping of managed instances.
		- Desired no. is the starting no. of instances to launch.
	- ##### A Launch Configuration (or A Template)
		- The template for instance configurations. 
	- ##### A Scaling Policy (Plan) 
		- Defines the when and how to scale out or in.
![Pasted image 20221207224003](https://user-images.githubusercontent.com/109697567/220480680-0209af7f-cc18-4f14-9ac8-22739d398533.png)
*Note:* Launch Templates are preferred over Launch Configurations by AWS, as future updates are concerning Launch Templates.

### EC2 Auto Scaling: Launch Templates
Launch Templates serves the same purpose as launch configuration, where it defines the EC2 instance configuration. AWS recommends using it over launch configuration.
However it has the following advantages over launch configurations:
- It can have different versions.
- It allows the use of multiple instance types and can use On-Demand and Spot instances in the same Auto Scaling group.
- We can define a placement group in the template such that instances will be launched in that placement group "Check placement groups in Part3".
This would help achieve the desired scale, cost, and performance.

### EC2 Auto Scaling: Health Checks
![[Pasted image 20250626164334.png]]
By default the EC2 Auto Scaling service determines if the instance is running or not via EC2 status check, even with ELB applied.
- This can be changed when creating Auto Scaling Group in the console to wait for EC2 status check ***AND*** the ELB health checks.
- If either of the two checks states a negative response, the instance is terminated.
![Pasted image 20221207230640](https://user-images.githubusercontent.com/109697567/220480719-52273ba7-8493-4fcf-afef-cbcd4b9f92d8.png)

### EC2 Auto Scaling: Types
![[Pasted image 20250626164350.png]]
Auto Scaling policy types: 
- ##### 1- Manual
	- This is to maintain a current number of Instances at all times.
	- Manually change the Min/Desired/Max & Attach/Detach instances.
- ##### 2- Cyclic or Schedule Scaling
	- Used with predictable load change to add Instances and remove them after the desired duration (daily, weekly, monthly).
- ##### 3- On-Demand or Dynamic Scaling
	 ![[Pasted image 20250626164613.png]]
	- Scaling in response to an alarm/event.
	- CloudWatch monitors metrics and generates alarms for auto scaling to scale out/in.
	- Has 3 types:
		![[Pasted image 20250626164832.png]]
		- **Simple Scaling:** A single adjustment up or down in response to the alarm.
		- **Step Scaling:** Multiple Steps/Adjustments depending on different Alarms.
		- **Target Tracking Scaling:** Scale out or in based on a target value for a specific metric.
- ##### 4- Predictive Scaling
	- Combines proactive and reactive scaling.

### EC2 Auto Scaling: Lifecycle Hooks
- Lifecycle hooks enables performing custom actions "such as checking logs" by pausing instances as an auto scaling group launches or terminates these instances.
- When an instance is paused, it remains in a wait state either until the lifecycle action is completed or until the timeout period ends (one hour by default).
![Pasted image 20221208001552](https://user-images.githubusercontent.com/109697567/220480740-5be069f5-566e-4da8-9eba-7cbb2ce8bb87.png)

### EC2 Auto Scaling: Cooldown & Warm-up Periods
##### Cooldown Period
- After a scale-out or scale-in activity.
- Is the amount of time Auto Scaling waits after a scale-out or scale-in activity before another scale activity can start. 
- This help ensure that the impact of the scaling activity becomes visible.
##### Instance Warm-up Period
- After a scale out activity.
- Is the amount of time that elapses before a newly launched instance (due to a scale-out activity) begins contributing to CloudWatch metrics.
- Basically to allow new launched instances to start giving impact after fully launching.

### EC2 Auto Scaling: Scale-in Termination Protection
Instances can be protected from being automatically terminated during a scale-in event using Scale-in instance protection.
This setting can be changed at the Auto Scaling Group level.

However, this does not protect the instance from:
- Manual termination. 
- Replacement if it becomes unhealthy.
- Spot instance interruption.

### EC2 Auto Scaling: Termination Policy
Which Instance is to be terminated??

- The AZ with the larger number of EC2 instances is selected first for termination.
- If there is a mix of launch configuration and Launch Template instances, ones with launch configuration are selected first for termination.
- AS terminates the instance with the oldest launch configuration first.
- If they are all the same, AS terminates the one that is closest to billing hour.
![Pasted image 20221208003255](https://user-images.githubusercontent.com/109697567/220480864-e59cfb4c-1324-4fe9-9446-bded240ec9f6.png)



---
