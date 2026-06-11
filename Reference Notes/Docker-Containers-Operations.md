---
tags:
  - Docker
Type: Reference Note
source: Elfakharny-Udemy-Course
page: 
Date: 2025-04-11T19:07:00
deadline: 
status: 
links-to: "[[Docker-Image-Operation(Build-time)]]"
---

----

docker run busybox echo "hello word"   <- CLI arguments  
it will execute it then stops !!
container has more usages this is just a trivial example

docker run busybox ls -l ---> **will list the container file-system its like chroot that created a private file-system replica but now it on a container** 

**container will never continue running as long as the command it executes finish** 

RULE--> container lifetime is command run time execution it doesn't matter if the command exits successfully or failed the container will seize to run 
(container lifetime = command runtime)

docker ps ->  list all running container process 
-a -> all container regardless there state 
containers have unique ids



docker run busybox sleep 5 
docker run busybox sleep infinity -> sleeps until its manually terminated 

docker run --detach busybox sleep infinity -> detach from my current bash process(entry point bare in mind that ps also shows the entry point command to the container) , detaches from current terminal (-d) 

#Docker_tool_Dicovery_NetworkCategory :nc 
docker exec container_ID nc -zv  google.com 80 (**nc:net-cat** is like Swiss knife of networking , here nc checks if port 80 is open in host google.com), i can use containers that has nc with a little bit older version 

docker exec -it container ID sh (attach a shell to the container, as long as this shell type is available )
it-> stands for interactive terminal

**docker attach containerID puts the container in foreground**


docker exec with -i , -it , without

| Option                            | Effect                                                                        |
| --------------------------------- | ----------------------------------------------------------------------------- |
| `-d` only                         | Runs in background but may exit immediately if no process is running.         |
| `-dit`                            | Runs in background with an interactive shell (useful for manual interaction). |
| `-d` + command (`sleep infinity`) | Keeps the container running indefinitely.                                     |
| docker exec -it alp1 shell        | to execute a command interactively in a background container                  |
| docker attach alp1                | to attach to the shell                                                        |

#Docker_Iam_your_mystery
**I would like to start a stopped Docker container with a different command, as the default command crashes - meaning I can't start the container and then use `docker exec` command ?**
**or a container that Entry Point = Null ???**  


Find your stopped container id
```
docker ps -a
```
Commit the stopped container:
This command saves modified container state into a new image named `user/test_image`:
```
docker commit $CONTAINER_ID user/test_image
```
 Start/run with a different entry point:
```
docker run -ti --entrypoint=sh user/test_image
```

Entry-point argument description:
https://docs.docker.com/engine/reference/run/#/entrypoint-default-command-to-execute-at-runtime](https://docs.docker.com/engine/reference/run/#/entrypoint-default-command-to-execute-at-runtime)
Note:
**Steps above just start a stopped container with the same file-system state. That is great for a quick investigation; but environment variables, network configuration, attached volumes and other stuff is not inherited. You should specify all these arguments explicitly.**






--------------------- container operations --------------------
#Docker_best_practice 
**use containerID because its unique can't be repeated** 

docker stop  ID --> its stopped but not removed its on my system

docker start ID--> start the container directly without needing to detach or pass sleep infinity again

#Docker_best_practice 
**Its not recommended to use -f at all we are not carpenter** 
**when we use -f on a running container it we will kill all running processes within the container unlike stop it will wait for the process to finish an then stops** 

docker stop ID
---------------> docker rm -f ID (combines both stop and rm)
docker rm   ID
after removing the we will need to us run command if we want the container it is completely removed


