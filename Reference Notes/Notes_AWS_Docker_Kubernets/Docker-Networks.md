---
tags:
  - Docker
Type: Reference Note
source: Elfakharny-Udemy-Course
page: "-"
Date: 2025-04-10T18:42:00
deadline: 
status:
---
we agreed on that the container lives in an isolated namespace so needed to map the container ports to our host machine so we could access nginx container 

docker run -d nginx 

docker ps -> to retrieve container ID 
docker exec -it containerID sh 
ifconfig or ip addr (for modern versions of linux if docker container contains a package manager i can install it but once the container is closed everything is lost since i can't add anything to the image which is the container is based from) 
exit

**docker inspect containerID/container name ---> we can find our container ip** 

docker run -it alpine sh 
ping 172.07.02 -> nginx container 
apk add curl
curl 172.17.0.2 --> http request to nginx 
if it replies with html page that means that nginx is accessible through the containers network called bridge network 
and of type bridge its a virtual network used by docker as long as the container are on the same host they can communicate over that virtual network,docker install a virtual network interface (virtual network adapter)called docker_0 it has an ip address,its of type bridge which allows containers to communicate and assign ips to all  containers on the host machine which is part of a certain docker network

#docker_post_script 
ping container name ---> it will not work because we need some kind of mapping or resolving to workout the resolution of container name to its ip some kind of DNS like service,docker offer something called service discovery but its not a DNS only applied when we create our own network which is also of type bridge and add containers to it 

**docker network ls**  --> types of network that docker offer 

**docker network create my_bridge --driver bridge** 
**docker network** --> shows available options 
docker ps 
**docker network connect my_bridge containerID**  -> new network new ip so two different completely isolated so i can achieve segregation between multiple networks of container on the host machine another level and type of isolation docker networks 

**docker run -it --network my_bridge alpine sh** 

**ping containerID**
#docker_post_script 
**ping containerName** --> now it works what happened is when creating a new network docker gives you something called service discovery which something that maps the names and ips on that network so i can ping any container with its name directly as long as Iam on the network, Default bridge will not offer this service !!!!!!

##########################video-9##############################
Host network

Docker will make the container use the host machine network adapter(network interface) as its own, now the container is not isolated. The docker container is now the same as its running on the system so it can be used and accessed directly through local host without natting (mapping) of ports 

#Docker_Iam_your_mystery 
the story in windows/macos as main os is different since the host of docker is a lite vm which make docker operate, so we cant use docker engine directly since we don't have access to the kernel does that mean we cant access the containers from local host? 
No now the containers is viewed as just a service/process on the system that has a port that allows it to communicate with other process or services and all the container will share the same host machine private ip because they are all now treated as just a process on the host not an isolated one so these services are accessed through there dedicated ports 
(host-ip : port)?????

for security concerns don't use host network because we have now access to the host network and the isolation hugely affected of-course

mac-Vlan network 
container takes different ip from the range of my network interfaces 
and takes a mac-address 

**docker network create -d macvlan --subnet=192.168.2.0/24 \      --gateway=192.168.2.1 -o parent=ens18 pub_net** 
--> --subnet=192.168.2.0/24  (my private network name)  

this network is not isolated as bridge network

docker run -it -d --network pub_net httpd
docker inspect containerID
container is accessed through container ip and port from browser 

some application work in layer data-link layer like wireshark package sniffing app monitor packet in a network, so if we need to run such application we the mac-vlan type of network (security application solution)

mac-vlan and host can access the internet through the network since its dealt with as device on the network so it can access and be accessed 
---------------------------vs------------------------------
bridge also can access the network but can't be accessed from outside 

none full isolation to the container no communication at all 
docker run -it --network none alpine sh 
it is used to test malicious software testing for example
