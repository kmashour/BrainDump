---
tags:
  - Docker
Type: Reference Note
source: Elfakharny-Udemy-Course
page: "-"
Date: 2025-04-09T19:02:00
deadline: 
status:
---
1st example of docker container was the busy box is that the only use, is our approach only revolves around using a container that has commands which i need to use that's not available on my system ?? 

we can create a server a daemon, web server most used example we want web server just to host a static website an ad or something very very simple  

I don't want to install the web server on my machine i want to sandbox it to run it in an isolated environment 

**nginx is many things but now lets look at it as a web-server** 

now we will run nginx through a docker container 

**docker run -d nginx** (p.s unlike busybox which is not configured to run any command its a container with a diagnostics and networking tool kit for debugging so the commands are for us to be executed so if no commands were directed to the container it just turn down in nginx container it is configured to run the nginx service so it continue on running upon the container run command)

**docker ps** --> will list port its listens on 

the nginx container is a web-server so it listens on a port, the problem is that it listens on the port but the container itself is part of internal virtual network created for a docker container so the host machine will not be able to access the web-server because its on a different network

docker run -d -P nginx
-P -> random port is opened on the host system and is mapped to the container port this is called port mapping or port forwarding (NAT) the traffic now 8080 is dealt with as its the port of the container hence the word mapping or even forwarding it forward the traffic to the container so it could listen to any request from any where (0.0.0.0:8080->80) and reply to the request 0.0.0.0 means any where(any ip)

docker run -d -p 8080:80
-p -> to decide which port to open on host system 
host port:container port

--name mywebserver --> to name the container 
-h --> changes host name 

docker run -d -p 8080:80 --name mywebserver nginx 

docker ps

#Docker_best_practice 
*port mapping is done in production is always used as good security practice* 
*take care not re-map a port by mistake*

