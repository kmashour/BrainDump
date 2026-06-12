---
domains:
  - "aws"
class: reference-note
tier: reference-note
tags:
  - aws/disaster-recovery
---

# Module 3-15: AWS Disaster Recovery (DR)

## Disaster Recovery - RPO & RTO
![[Pasted image 20250516105714.png]]

- #### RPO - Recovery Point Objective
RPO is the acceptable data to be lost after the restoration point "Backup point" due to a disaster. Measured in time (hours / minutes / seconds)
- #### RTO - Recovery Time Objective
RTO is the acceptable time taken after the disaster to get active again & go back to last restoration point taken.
- RPO & RTO determines the cost of Disaster Recovery, less RPO & RTO means more cost with more efficient Disaster Recovery.
![Pasted image 20221109072525](https://user-images.githubusercontent.com/109697567/200859792-7bc9d1b9-29e9-4bd4-885e-c7f6424986fe.png)
AWS Approach in Disaster Recovery could be explained as having a DR Site for disaster recovery, & it should be in a different region or away form the main production site. If the production went down, the cloud service is redirected to the DR Site, & it's advised to be automated redirection. 

The RTO and RPO is determined after making a business analysis to determine how much should we invest in a disaster recovery plans   

![[Pasted image 20250516110610.png]]

![[Pasted image 20250516110618.png]]
### Disaster Recovery Approaches
Graded from lower cost & recovery speed to the higher cost & fast recovery speed as follows : 
##### 1- Backup & Restore
- Copies AMIs & backup data & store it in a different region.
- no active DR sites until the disaster happens.
##### 2- Pilot Light
- Keep the minimal needs of the infrastructure only "**ex:** Databases".
- Continuous data replication between the two sites.
##### 3- Warm Standby
- Keep a scaled down version of the production environment.
- The second site can be scaled up after the disaster if needed.
##### 4- Multi Site
- Keep full running version of the production environment.
- Active/Active Sites.

![[Pasted image 20250516111402.png]]



---

---

## High Availability & Fault Tolerance
- **High availability** describes the **availability of the application**, **while Fault tolerance** describes how much the application **performance is affected by faults**.
- High availability is done by **Load Balancers.** through periodic health check the load balancer forward the traffic to healthy EC2 instances, The health check as threshold if it was exceeded the EC2 is marked out of service and unhealthy 

![[Pasted image 20250512091313.png]]

- Highly available but not fault tolarent 
![[Pasted image 20250512091336.png]]


---
