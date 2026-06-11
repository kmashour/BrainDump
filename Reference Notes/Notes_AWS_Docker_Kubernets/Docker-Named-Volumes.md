---
tags:
  - Docker
Type: Reference Note
source: Elfakharny-Udemy-Course
page: "-"
Date: 2025-04-09T18:54:00
deadline: 
status:
---

volume : a combination of files that resides somewhere on the disk (بالعربي معنها مجلد والترجمه مش هتقرب الموضوع هنا)

Files in the container are not persistent if the container deleted any data on the container is also deleted 
**is there any difference between stopped and deleted ??** 
The data is lost when the container is removed, not when it's stopped or restarted. 
Basically, if you do `docker ps`, **if the containers keeps the same id (the big ugly hexadecimal id)**, the data is not lost.

It gets complicated when somehow your docker containers are not managed by you, but by some kind of automated-managing method. **Tools like these usually start new containers if there is failure. In that case you should mount a volume to store your data on the host.**

docker run  -it busybox sh

vim hello.txt

exit or terminate the sh shell the container in our case the busybox container will seize to exist since the container entry point command is killed which was the sh shell (parent process of the container)..... take care by passing a cmd we are actually configuring a new entry point a process that acts as an entry point to the container will be covered later

**file created in a layer called ephemeral layer a volatile layer that lives as long as the container lives** 

docker run  -it busybox sh
now lets do the opposite lets delete something very critical in our container such as 
rm /bin/env 
exit 

docker run  -it busybox sh 
ls -l --> the /bin/env --> booom!!  its there 

that's why its a very strong concept its a very safe environment (sand boxed environment)for experimenting if that happened on the host machine its impossible to retrieve and its a headache to retrieve if there are backups 

I want my files persistent because sometimes its a database container so the files must be persistent !! so if the container is closed and the image is removed the files are still persistent 
In addition to that it can be way of doing something similar to virtual machine shared folders or allowing copying and pasting between the host and the VM just using these as analogy of bridging the isolated environments if we need to pass something 

*for that we use* 
volumes ---> 
named volumes , 
anonymous volumes , 
bind mount volumes 

volumes -> named volumes (the volume who has name or the defined volumes)

docker manages this files 
/var/lib/docker/volumes --> only accesses by root user , contains docker volumes so it can have multiple volumes for multiple containers  

**A volume can be used by multiple containers, A container also can be connected to multiple volumes**

#Docker_Iam_your_mystery 
multiple  t may create locking issues


*volumes cant be added while container is running, so go to old school way which is just copying the files from within its original path if a volume is not created* 

docker volume create mydata 
sudo -l /var/lib/docker/volumes 
now the files is accessed by host through that path and through the container internally 

docker run -it -v mydata:/opt busybox sh  
-->
-->
-->
vi /opt/hello.txt 
exit 
docker ps --> why use this line ? 

docker run -it -v mydata:/tmp alpine sh
ls -l /tmp/hello/txt
cat /tmp/hello.txt 
exit 

cat /var/lib/docker/volumes/mydata/\_data/hello.txt
--> \_data is created by the docker engine inside the volume and stores files in it

docker run -d -it -v mydata:/tmp alpine sleep infinity 
docker run -d -it -v mydata:/opt busybox sleep infinity 
docker ps

docker exec -it ID_1 sh 
vi /opt/hello.txt
exit ---> (the container will still be working since the entry point is still running the sleep inifinity)


docker exec -it ID_2 sh 
cat /tmp/hello.txt
exit

docker run -it -v dbdata:/data busybox sh
--> docker will create everything the volume , the directory that's inside the container if its not there by default everything u want it will be there thanks to the docker engine 
ls -ld /data/
exit

#Docker_best_practice 
docker volume ls 
--> **a good practice in sense of house keeping** of my system is to delete unused systems, it can consume disk space out of thin air  
--> you need to make sure for safety measures that the volume is not used by any container 
for i in 'docker ps -a | awk {'print $1'}
for>do 
for>docker rm -f $i
for>do 
or
docker volume rm mydata
docker volume dbdata 


Alternative options to copying
that's how to copy from outside to inside the container 
- docker container ==cp ./file.py 7e0:/tmp/file.py==













