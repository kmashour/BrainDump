---
tags:
  - Docker
Type: Reference Note
source: Elfakharny-Udemy-Course
page: "-"
Date: 2025-04-09T19:09:00
deadline: 
status:
---

Linux refers to the kernel not the os 
kernel is between hardware and the os 
drivers are on the kernel 

Microsoft windows os and kernel is one package

unix the kernel is package with whatever os depending on the owner company

macos darwin based which is a unix-like system also packaged with os and hardware, apple offers a bigger package

#########################video-2###############################
histrionically there where no pc only servers there were only unix 


----------->they need isolation , multi-host environment  
server ----> chroot(root jail),
----------->to distribute system resources

chroot is beyond permission its literally isolated each user will have his dedicated file-system replica that can be used by a specific user 

ulimit can set limits on server resources but doesn't apply to cpu resources because its shared  

nice/renice they are the best cpu resources management but they are not limiters 
40 year old tools boom !!

1998 ---> vmware

complete isolation , hypervisor made complete isolation between every machine each will have his cpu resources memory networking ......
----------------------> vm1
pc on steroids -------> vm2
----------------------> vm2

hardware virtualization  (bare-metal) 
machine (with installed hyper-visor i.e vmware ) 
can host multiple Virtual machine is built on it with complete resource isolation 

os virtualization (chroot)
Linux/unix in base , they give access to make  isolated spaces for multi-users so each user work is not mixed or corrupted by other users. 
if not linux unix it will be as software (vmware) on an already running OS (windows/macos).



from 2002
on Linux level
Control Groups (cgroups)
Linux Namespaces 

2008
Linux containers (lxc)
self contained environment on the kernel level that's why it need someone who knows code who knows kernel interfaces since it was low level interaction with kernel every thing was on Linux(kernel)

That's were dockers emerged 
this is a boooom ! 
Docker made the concept of containers accessible to a larger audience, Now any application or tool can run with complete isolation any container will save its file-system completely 
decoupled from the machine they operate on kernel level which made any container portable to any linux kernel whatever the distribution was, any container only sees (it-self) from POV of resoucres they are allowed certain memory , disk spaces with a cpu resources to run and they accommodate to that, in short they did every thing lxc could provide in term of accessibility 

so in container we sticked to whats constant which is the kernel and add specification specific to our app 
`ka2n kda lma el container yenzl 3la os bybda2 yekml 3la elkernel el mawgoda le7ad ama yetl3 lel app ya3ny ka2nana gebna el app bel kernel beta3o we shelna el user mode we el7etat beta3t elkernel elhya sabta 3la kol el linux distro since in general all linux kernels is the same bec`
linux kernel + specification -> Redhat
linux kernel + specification -> Ubuntu
linux kernel + specification -> SUSE

so **containers** main idea is tailor it self and dependencies on the kernel daemons which is constant across all the os linux versions.

container vs vm --> in term of OS (interview question)

for what purpose do you need do we need a GUI do we need full os capabilities (GUI and terminal) **vm all the way**, because sometimes we need to run a GUI program .
if we need optimized utilization of resources we use docker all the way.

also containers crashes commonly unlike virtual machines the most important thing is when a containerized applications crash the data is decoupled from the container itself 

###########################video 3############################

docker client: tool which I interact with 
docker server: interpret the commands forwarded from the client and handles the cgroups and namespaces the lxc to create the container #themoreyoufuckaroundthemoreyouknow Docker architecture refer to [[../5-sources/books/Docker-Deep-Dive.pdf|Docker Deep Dive Zero to Docker in a single book (Nigel Poulton) (z-lib.org)]]



installation guide : 
docker desktop : lite weight linux vm is installed so the docker engine(docker back-end server) could be hosted since docker installed on kernel it communicates with the kernel level so it need the vm and a docker client as an interface to give commands to the docker.
docker desktop used in windows and Macos the desktop as said will be a lite weight linux vm that runs the docker engine and the docker client will be on the system

if we already have linux as our OS we only just need the engine 
no need for linux desktop except if we need a layer of isolation if want the docker environment to run as if it is sand-boxed since the docker engine will not run directly on our kernel but on the docker desktop lite weight kernel (which is a lite weight linux virtual machine ) 
