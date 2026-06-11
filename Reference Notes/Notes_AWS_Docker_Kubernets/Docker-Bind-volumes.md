---
tags:
  - Docker
Type: Reference Note
source: Elfakharny-Udemy-Course
page: "-"
Date: 
deadline: 
status: true
---
bind mount 

When you use a bind mount, a file or directory on the host machine is mounted from the host into a container. 
**By contrast,**
when you use a volume, a new directory is created within Docker's storage directory on the host machine, and Docker manages that directory's contents.

If you bind mount file or directory into a directory in the container in which files or directories exist, the pre-existing files are obscured by the mount.(the host volume is always checked when we mount a volume). 

This is similar to if you were to save files into `/mnt` on a Linux host, and then mounted a USB drive into `/mnt`. The contents of `/mnt` would be obscured by the contents of the USB drive until the USB drive was unmounted.
**With containers, there's no straightforward way of removing a mount to reveal the obscured files again. Your best option is to recreate the container without the mount**.

#Docker_Iam_your_mystery 
when using bind mount only in the first image build and volume mapping the local host directory is checked and the data in it is mapped to the container after that all the contents of the container will be mapped from the inside the container to the local host !! 

syntax of a bind mount:

docker run --name static-site -v 
\<path-on-Host\>:\<path-on-container\>

docker run --name static-site -v $(pwd):**/usr/share/nginx/html:ro** -p 8080:80 -d nginx 

we mounted our directory which contains the static website to the nginx html directory that is used by nginx container to source from it (/usr/share/nginx/html) the website it will host (serve)

#docker_post_script 
- **ro -----> read only if i want to make the container read-only only the host machine can edit the files, if the file is already created the ro is useless** 
- **/usr/share/nginx/html --> default path where nginx goes to see if there is an html file to serve** 
#docker_post_script
- **docker run -v mywebdata:/usr/share/nginx/html:ro -P -d nginx** 
  **mywebdata --> volume will be created automatically** 
  **-P --> will automatically open a port on my host pc**

**bind mount and volume how are they different** 
--->If you bind mount file or directory into a directory in the 
container in which files or directories exist, the pre-existing 
files are obscured by the mount, unlike in named volumes it create some sort of open door from the container to the volume is nothing is obscured **(فتحوا القطرين علي بعض )**  

