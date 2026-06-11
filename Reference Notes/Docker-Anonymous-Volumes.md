---
tags:
  - Docker
Type: Reference Note
source: Elfakharny-Udemy-Course
page: "-"
Date: 2025-04-10T18:53:00
deadline: 
status:
---
volumes -> Anonymous volumes

both types of volumes are managed by the docker engine except that the name is managed by me in named volumes 

like named container anonymous volumes can be used by multiple container as long as its not used in the same time that's the main difference 

so before named volumes what happened is there were a container which is used to create a volume and another container which is the application and the volume was referenced to through the container.If you create multiple containers consecutively that each use anonymous volumes, each container creates its own volume. Anonymous volumes aren't reused or shared between containers automatically. To share an anonymous volume between two or more containers, you must mount the anonymous volume using the random volume ID.
To mount a volume with the `docker run` command, you can use either the `--mount` or `--volume` flag.
```console
$ docker run --mount type=volume,src=<volume-name>,dst=<mount-path> 
$ docker run --volume <volume-name>:<mount-path>
```


#docker_post_script
**docker manages the anonymous volumes,anonymous are only deleted when the container is deleted (-v), it doesn't have a name so we need to remove the container with -v** 
**named volumes offers everything anonymous offers in addition to complete decouple of volume from container hence deleting the volume wont affect the container and can be created with name as its only identifier it doesn't need to be tangled to a container**


90% named volumes will be used 
or bind mounts

docker run -it -v /myvol busybox sh 
exit
docker ps -> no traces of the container 
->p.s we need to stress that the container is there but stopped so it doesn't have a pid so ps doesn't show it that's why on just stopping the container the volume persist unlike deleting it the volume will also be deleted 
sudo ls -l /var/lib/docker/volumes --> esmo mor3b kda and that to guarantee uniqueness  

docker ps -a 
**docker rm -v container id ---> container is deleted** 
**-v must be used to delete the volume** 
**sudo ls -l /var/lib/docker/volumes** 


