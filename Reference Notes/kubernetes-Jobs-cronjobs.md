![[Pasted image 20250426090108.png]]


-------------



 ![[Pasted image 20250426090122.png]]

------------


 ![[Pasted image 20250426090511.png]]

-------------

 ![[Pasted image 20250426092030.png]]
 
 The pods operation must be coordinated and that is achieved through the app that is running in each container on the pods i.e developer problem to worry about 

--------------------

  ![[Pasted image 20250426091600.png]]

  ![[Pasted image 20250426092002.png]]
 no **completion** , we are running 10 pods as long as the data is running in queue and the pod terminate itself when there is no data to process so **the pod termination is left for the pod itself and the application it runs**, and there must be co-ordination in how the pod works so they don't intervene with other jobs but thats the developer problem to handle  
 Work Queue Pattern 
 Producer --> publish/generate the data, and i want to process this data in real time, on the moment it arrives..... this is done by adding the data in a message queuing system like RabbitQ , kafka, Aws SQS 
 Consumers --> responsible to take the data from the queue and process on it 

 SO the job runs as long as there are data running in that queue the pods will keep running until the data processing is finished and when it Finishes it throws it in data warehouse or whatever this application that are based on data analytics can work 24/7 as long as the data keeps flowing in the queue and the consumers  (pods) will keep working 

--------------------

  ![[Pasted image 20250426092759.png]]

----------------
  ![[Pasted image 20250426093148.png]]

----------------

 ![[Pasted image 20250426093653.png]]