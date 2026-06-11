---
tags:
  - kubernetes
Type: Reference Note
source: Elfakharny-Kubernetes-Udemy-Course
page: "-"
links: 
flogetzzel:
---
if we want to change default configuration of nginx for example we had to change the nginx.conf file to listen on port 8080 for example instead of 80 then we had to build a new image and run it, through config map we completely de-coupled the container configuration and implemented it through kubernetes 

![[Pasted image 20250426102514.png]]


Config is injected to the application by 3 ways 
- Config map are passed as environment variables
- mount config map to container, it becomes part of the application
- as command line arguments 
----


- Config map are passed as environment variables
 ![[Pasted image 20250426104057.png]]
 All the config map is read and the environment data are extracted and used in the container 

- As command line arguments 
 ![[Pasted image 20250426104349.png]]
 unlike the previous way here we need to map exactly the value that will be passed to the args we defined 

- mount config map to container, it becomes part of the application (mounting config map as a volume)

  ![[Pasted image 20250426104453.png]]
  data is a whole config file indentation rules should and must be very strict, so in yml to make a multi-line value we start with | and two spaces in the next line 

  ![[Pasted image 20250426104745.png]]
  mountPath --> we used the whole path till the nginx.conf
  subPath --> if we didn't use it, nginx.conf will be mounted as a directory not a file 