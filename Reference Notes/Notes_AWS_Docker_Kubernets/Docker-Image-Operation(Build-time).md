---
tags:
  - Docker
Type: Reference Note
source: Elfakharny-Udemy-Course
page: "-"
Date: 2025-04-10T19:03:00
deadline: 
status:
---

docker image ---> Consider it as the template for the docker container  


docker pull busybox -> it contains some commands and diagnostic tools for troubleshooting linux

docker images -> list all available images

docker images are pulled from docker registry(docker-hub)

docker run busybox -> if busybox is not on the system it will automatically pull and run the container, container in that sense will run as a process in the background completely isolated with its allocated resources and gives a big  
hola bitch !!!  

image has two types 

1- predefined to run a certain command on container run command

2- containers that can run multiple commands they are designed     to run as per given input (CLI argument), so the container      just start and exit at the same instant if not given a          command (msh hay2om ya3ny)

**the main target of a container is to run only 1 process once the process is terminated the container is considered obsolete its a bundle of packages and dependencies that run together live together terminate together** 
the container = application 
exited container = exited application
container status up = Running container  




-------------------- operations on image level ------------

#Docker_best_practice 
good practice remove all non used images because it occupies space
docker images 
docker rmi image id 

**if container uses an image there will be an error in removing the image, we can use -f but its not a good practice since it forcefully remove the image** 
 

docker containers runs in an instant very very fast unlike a virtual machine a whole os will startup

docker container ---> The running container which is based on a docker image 

**using rmi nginx --> i have two nginx the latest and another old version so by default it will delete the default version bye bye** 
**--> so we ether use and specify the tag** 
**--> or use the image ID**

#Docker_best_practice
best practice in docker image, is to get rid of the tag latest to escape conflicts because somewhere in time what will happen is there will more than one under label latest 








where is docker images stored on a linux machine: 
	The contents of the `/var/lib/docker` directory vary depending on the [driver Docker is using for storage](https://github.com/docker/docker/blob/990a3e30fa66e7bd3df3c78c873c97c5b1310486/daemon/graphdriver/driver.go#L37-L43).
    By default this will be `aufs` but can fall back to `overlay`, `overlay2`, `btrfs`, `devicemapper` or `zfs` depending on your kernel support. In most places this will be `aufs` but the [RedHats went with `devicemapper`](http://developerblog.redhat.com/2014/09/30/overview-storage-scalability-docker/).
    You can manually set the storage driver with the [`-s` or `--storage-driver=`](https://docs.docker.com/engine/reference/commandline/dockerd/#/daemon-storage-driver-option) option to the [Docker daemon](https://docs.docker.com/engine/reference/commandline/dockerd/).

- `/var/lib/docker/{driver-name}` will contain the driver specific storage for contents of the images.

- `/var/lib/docker/graph/<id>` now only contains metadata about the image, in the `json` and `layersize` files.
  In the case of `aufs`:
 
- `/var/lib/docker/aufs/diff/<id>` has the file contents of the images.

	External sources citation Books articles Research papers blogs video-courses courses lectures - `/var/lib/docker/repositories-aufs` is a JSON file containing local image information. This can be viewed with the command `docker images`.

In the case of `devicemapper`:

- `/var/lib/docker/devicemapper/devicemapper/data` stores the images
- `/var/lib/docker/devicemapper/devicemapper/metadata` the metadata
- Note these files are thin provisioned "sparse" files so aren't as big as they seem.
