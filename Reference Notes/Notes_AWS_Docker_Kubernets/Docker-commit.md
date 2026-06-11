---
tags:
  - Docker
Type: Reference Note
source: Elfakharny-Udemy-Course
page: "-"
Date: 2025-04-10T18:40:00
deadline: 
status:
---
ocker containers data is ephemeral, all changes on file system is deleted after the container is deleted that's why we used volumes and Bind mounts so why that happens......

#docker_post_script 
image is designed to be for multiple users not one user only..
imagine if there is an image designed to use port 8000 but i changed the configuration to be 80 and other users used it it will create conflicts in our application and will need thorough inspection to see were the problem is....so the image is something like standard template that is being used as foundation to build on

#docker_post_script 
file-systems -> dictates how an OS should deal with the files on the disk (adding , modifying , deleted)

docker uses UFS -> union file-system 
UFS -> is consisted of layers unlike normal filesytems deals with the the file as its flat objects residing on a disk so it can be accessed directly, here in UFS the files are in layers that are read only, when we add files there are an additional layer (R/W) thats added on the top
(outer most layer) and its deleted when the container is deleted 

#docker_post_script 
what if we edited a file from the read-only layer the base layer of the image that's the container is based from it ?
**the UFS copy the read-only file and an outer most layer is created with our modification and that outer most layer shadowed the read-only layer same goes for deleting a layer(file) from the read-only layers it will be shadowed with a layer on top with the deletion record of that layer..... but that wont affect if we created a new container based on the same image changes wont be reflected** 

#docker_post_script 
in volumes and bind mount -> the files are handled in the same manner of the OS file system, UFS لا يعنيني في هذه الحاله 

docker run -it ubuntu bash 
touch test 
exit

**docker diff containerID** ---> shows the differences between the container and the image file (A:add , c:change , D:delete)

docker start containerID 
docker exec -it containerID bash
rm /etc/legal 

docker diff containerID

**docker exec -it containerID bash**
**apt update** 
**apt install -y curl**
**exit**

docker diff containerID ---> BOOM!! big number of files(layers) is added over the image 

**docker commit containerID  mod_ubuntu:1.0** 
-> will generate a sha256 for the image , there are a sha256 unique for every layer of the image. we only see the latest layer sha256 and it will refer to the image #themoreyoufuckaroundthemoreyouknow 
(outer most layer sha 256 = image sha256 )

**we should use another name** (Versioning 101)because we will be creating a new image so we take the top layers (our changes on the file-system) and union it with the original read-only layers and create a new image with new name so **we don't create conflicts with the ubuntu base image** because it may be used across multiple domains in the project  **(DOCKER IMAGES ARE IMMUTABLE)** 

#docker_post_script 
if the tag is not specified it will automatically choose latest 

docker run -it mod_ubuntu:1.0 bash 
curl ---> is installed 

docker image ls --> ubuntu mode is nearly twice the size 
1- Docker images are immutable 
2- A copy of the file will happen to exist in the top layer of the UFS and it will represent the recent updates 
3- this scenario will be repeated if we do any modification in the latest layer even if its the same files the only thing is our copy will be from the upper most layer 
4- Any file operation = new layer = n number of duplicate of the same file 
thats why we might end up with a huge image because of that replication behavior 


**we need tracking to that modification done on the image here the Docker file will play a crucial role** 