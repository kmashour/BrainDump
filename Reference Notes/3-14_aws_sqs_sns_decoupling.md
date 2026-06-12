---
domains:
  - "aws"
class: reference-note
tier: reference-note
tags:
  - aws/decoupling
---

# Module 3-14: AWS SQS & SNS Decoupling

## 4. Application Integration & Decoupling (SQS & SNS)


---

## SQS - Amazon Simple Queue Service (Message Queue Concept)
- Message Queues provide asynchronous communication & coordination for the application components.
- Messages are stored in queue reliably until they re processed, then get deleted.
- this allows scaling different parts of the project (Producer queue and consumer queue) because they are independent of each other  & increase its reliability.
- Message sending Tiers is called **Message** **Producers**, while message receiving Tiers is called **Message Consumers**.
- Using SQS is referred to as Decoupling process, as it decouples different tiers. 
![[Pasted image 20250510235011.png]]

---

## SNS - Amazon Simple Notification Service
- SNS is a fast & fully managed notification service.
- **Publisher is the sender "Producer" & Subscriber is the receiver "Consumer".**
- Publishers publish messages to a SNS Topic, Subscribers receive messages from the SNS Topics they are subscribed to.
- **Publisher must have the permissions to be in the SNS Topic "IAM Policies".**
- Subscribers can be users, emails, SMS, services & many other formats.
- SNS is reliable & stores multiple data copies across multiple AZs.
- SNS supports HTTPS in-transit. Its also encrypted at rest 
![Pasted image 20221103014434](https://user-images.githubusercontent.com/109697567/200859449-f4fb80d3-3c56-4e0f-8234-26952278915b.png)
**Note:** Message size in SQS & SNS shouldn't exceed 256 Kbytes, indicating that the messages either in queue "SQS" or instant "SNS" won't include the data or the object itself, only a message about the data.


---
