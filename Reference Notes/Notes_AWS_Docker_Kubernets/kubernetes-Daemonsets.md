
Through Daemon set we create a pod on each of the worker node of our cluster, it's mainly used to create a pod that do something on the node 
- It can be log aggregation on that node
- It may be mounted to the node filesystem to undergo some updates or downloads 

so its mainly used to do something related to the node but its not a must since in the it creates a node and Iam free to setup that node as I like, The thing is it will create a Pod on all the nodes so its like a linux Daemon so its best suited to do something on the Node 

We can also control on which node we want our daemon set to deployed but in that case we bypass or override the scheduler so in such cases the pods will be deployed without referring to the schedule






![[Pasted image 20250524164538.png]]