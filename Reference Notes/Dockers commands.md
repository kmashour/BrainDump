
docker info
# server component should reply the server component is docker daemon "the docker API which receive the docker commands to execute it"

client / server must reply 

 ==instead of using sudo add user acc. to group Docker==

 1st of we need to pull an image to local docker registry docker image + **action** any thing related to image will be the same  
 - docker image pull fedora
 - docker image ls 
 - docker container create -it (interactive, pseudo terminal) fedora bash 
 - docker container ls -a men 8er only running will be viewed
 - docker container start -i 90b id or name of container 
 - cat /etc/*hostname*
 -  id container == machine name       inside the container
 - cat /etc/*release*
 - keda ka2ny 3amlt vm so8yra inside a vm machine or a physical machine 
 - exit 5arg bara elcontainer fel 3ady by5rog men eluser we ro7 lel root we 3aml 
 - docker image pull python 
 - docker image ls 
 
 - docker container run == docker container create + docker container start + docker image pull 
 
 - docker container run -it python
 - exit() han5rog men elcontainer kolo

stop lel container once existed but why ?? 
Another very important concept 
the main target of a container is to run only 1 process once the process is terminated the container is considered obsolete its a bundle of packages and dependencies that run together live together terminate together 


the container = application 
exited container = exited application

vm != application 
vm machine runs normal = while ( exited application)

the fedora container was running the bash shell app if the bash exited the container is terminated 

container = command running which is bash 

container = command running was python 3 

container is not a standalone operating system 


can we run a container on another command ? 

docker contain ls -a

==docker container run -it python /bin/bash== 
run python container with the bash command not python 3

now python3 is sub process from parent process which is bash so by exiting we return to bash since we didn't exit the parent process 
bin
- docker container rm id1 id2 id3 or name
- docker  image rm python fedora  or id 
will delete all layers 

its better not to merge all layer because docker and reuse available layer in other images something like c++ shared libraries



---------------------------
Image deep dive : 

image name = repo:tag 

build time (build file,layer files) / runtime(running container) 

manifest list ---> manifest
manifest list: used when there are multiple os based images, the manifest list is used to 
choose the right manifest for the os running on the host machine (the machine which docker engine run on)


docker container run -it --name "hadoopc" -h hadoopc ==asami76/hadoop-pseudo==:v1.0 bash ==-c "/usr/local/bootstrap.sh; bash"==

--name "parameter" -> switch to change name of the container instead of the silly names generated name used as argument instead of sha256 id 

-h host container name host pc which inside the container 


-----------------------------
docker in vs code 

- docker image inspect id  (gives details on the image and replay in json file )
- docker container inspect id 

docker in vs code 

==docker image ls -q== -> gives images id

docker image rm $(docker image ls -q)


we need basic to intermediate commands skills in linux 

---------------------------------

Containers in Depth

already covered in Dockers intro 
-------------------------------------------
Networking and storage  

import os 
os.listdir()
os.listdir('/tmp')

due to limited resources and the absence of editors inside a python container we implement the script outside the container and copy the file from outside container to the container and execute inside the container

that's how to copy from outside to inside the container 
- docker container ==cp ./file.py 7e0:/tmp/file.py==

python container 
import os 
os.listdir()
os.listdir('/tmp')
exec(open('/tmp/file.py').read())

no problem so far but what if we want to modify the file will we repeat all the steps ? 
we need a way for containers to deal with volume and storage 



----------------------------------------------------------
Docker networking: 

example on port mapping 
docker container run -it -p 8000:80 nginx:latest

--

docker container run -d --name web nginx:latest

docker container run -d --name client centos:lates

curl http://web <- this will generate an error 
but 
ping 172.17.0.2 will work no problem<
now we need them to communicate with name not ips 

curl http://172.17.0.2
two containers communicated on same machine through ip 

this is temporary solution
docker container run -d --name client --add-host web:172.17.0.2 centos:latest

inside client 
ping web will work 
cat /etc/hosts -> we will find an entry for the ip 

---------------------
Docker networking 
in Virtual machine tool like hyper-v the tool itself has its networking stack like it creates virtual adapter on the host itself and the vm connects to the adapter through config of a virtual switch(Virtual switches are also used to establish connections between virtual and physical networks and to carry a VM's traffic to other VMs or a physical network). through we connect it to another vms or to the internet and so on 

in Docker b2a  
3 types on networks 
bridge default
host 
none 

ip link show 
* docker host *
loop back adapter (lo) dah mawgood 3latol
network interface () el3ady 
docker0 < bridge network> 

ip addr show
docker container run -dit --name alp1 alpine
### Summary:

| Option                            | Effect                                                                        |
| --------------------------------- | ----------------------------------------------------------------------------- |
| `-d` only                         | Runs in background but may exit immediately if no process is running.         |
| `-dit`                            | Runs in background with an interactive shell (useful for manual interaction). |
| `-d` + command (`sleep infinity`) | Keeps the container running indefinitely.                                     |
| docker exec -it alp1 shell        | to execute a command interactively in a background container                  |
| docker attach alp1                | to attach to the shell                                                        |
|                                   |                                                                               |

hover over bridge icon it shows alp1

docker container run -it --name alp2 alpine  ,,,

alp2 
ifconfig


host 
ip link show 
2 virtual adapter created for each container that deals with with container adapter 3shan ye3rf yekl m el3alm el5argy 



docker container run -it --name alp23 -- network non alpine

alp3
if config 
nothing it has no adapter like alp2 which was eth0 




docker container run -it --name alp4 --network host alpine
alp4 
hostname  replays 'apollo'
exposes the container on host and the container behave as its the host and claims all network adapter in the host


docker container run -d --name web --network host nginx
in browser http://web.com  works without port forwarding since the container is exposed

--------------------------------
drivers in dockers 

host machine has 3 types of drivers 
bridge driver 
mac v-lan layer 2 driver ??? not used much 
overlay driver in swarms 

docker network ls "shows drivers for each network"



create my own network 
docker network create mynet 


connect running container to another network:
docker network connect mynet alp1
docker network connect mynet alp2

creating network with default settings 
- docker network create mynet2

creating network with custom subnet  setting
- docker network create --subnet 10.0.0.0/16 mynet2 

container can be connected to multiple networks

- docker network connect mynet2 alp2

*inside apl2*
- if config
..===. we will see number of adapters = to number of connected networks bem3na 3ady go inside alp1 and run ifconfig===

we can disconnect containers from a network 

docker network disconnect mynet apl2

now pinging the other container will not work since they are on different networks although the network driver is the same 



docker network create --internal mynet3

docker network connect mynet3 alp1
docker network connect mynet3 alp2

they can only ping each other and any container on mynet3 can't ping google for example ,its the same bridge network but the switch --internal make it local only maybe it will be used in test environment 

---------------------------------------
The container network model (cnm)
-----------------------------------
==Docker storage bind mount== 

sudo cd /var/lib/docker/
ls

==overlay2 this is the storage driver and has nothing to do with the network driver overlay. ==
in containers the image layer are read only we add our custom layer that make a container this layer are r/w all the data has life time of the container once the container is deleted all the data will be deleted called ==non persistent data ==

docker image pull centos 
sudo cd /var/lib/docker/overlay2
ls
we will find the layer hash 
cd /var/lib/docker/overlay2/892ddf2
cd diff 
ls

the thing is when creating a file inside the container you will find it the overlay2 folder inside the container hash inside diff


bind mount ,, mount storage to the container ka2no flasha 3amlnlha mount 3la elcontainer

it can also be considered as the folder inside the host has a shortcut inside the container 

docker container run -it -v /home/sami/docker-work/code:/app/code python 

/app/code -> an app directory will be created in the root with the code directory shortcut from the host 

dlw2ty 7alna elmoshkla beta3t ezai ne3ml copy men host lel container we yeb2a el file mesm3 fel ne7yten + 7alna moshklt el non persistent data ya3ny lw 8ar fe dahya elcontainer el files mawgoda 



another way which is docker volume 


  docker volume create myvol
  inspect to see mountpoint 

docker container run -it -v myvol:/app/code python bash
myvol -> ma3rof maknha 3ala elhost
/app/code is created automatically 


/var/lib/docker/myvol/_data 
_data --> we add the desired file in this folder 

this way is create a consistency from the pov of where the files are stored...

*on host machine*
docker volume ls 

bind volumes and cloud ?? 

----------------------------------------

containerizing an application


since python image runs on outdated debian so we need to update in order to be able to connect to debain repository 

apt update 
apt upgrade -y 

containerizing 
docker commit pyflask 
asami76/pyflask:v1.0





---------------------------------
Dockerfile 

build context is the directory where the dockerfile is found and is considered home directory referred to with a .


any instruction change anything in file system add remove copy is considered a new layer 

docker build -t asami76/pyflask:v1.1 .

the difference between the commit approach and this is the commit considered all the changes is a R/W layer on its own unlike the build approach every modification in considered a layer 


inspect related stuff is runtime dependent as the exposed port 
the cmd in docker file


### **🚀 Summary**

|**Method**|**Effect**|
|---|---|
|`EXPOSE 80` (inside Dockerfile)|Only **documents** that the container listens on port 80. No actual exposure.|
|`-p 8000:80` (in `docker run`)|Maps container port 80 to **host port 8000**, making it accessible from your machine.|
 
 
 at 4:25:00