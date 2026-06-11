https://www.youtube.com/watch?v=PrusdhS2lmo <- Big Data


We add the app with its dependencies in box in a lite way that can run anywhere 

containers are always compared to virtual machines and as long as we dig deeper to the difference between them the more we understand 

Virtualization appeared in the 60s 


virtualization
HW(server)|os|APP|APP

The problem appeared when the server spec fired up so all this resources will be wasted if only on one machine with only one OS and in the same concept will all the apps run on the same machine ?? 

so virtualization came into play 
HW(server)|HYPERVISOR LAYER|os(linux)|os(win)|os(macos)

virtual machine management software -> hypervisor
type 1 ring 0 
type 1 ring 1 
as software on already running OS
bare-metal 

It made the os behave as its the only hosted OS on the machine 
its even expanded into cluster where multiple physical servers connected together

dev -> create vm -> os -> Dependencies on OS
Ops -> move the vm -> start -> stop -> bckup -> restore -> snapshot


all of that has a respective equal in the containers 

------------------------------------------------------

Requirements increased ?? tab han3ml eh?

the resources acquired by the VM are all wasted for the app dependencies since most of them to run up the OS which our app runs in it but most of the resources are wasted by the VM , most of the times 
VM resources > app itself 

VM taxes kol mara a7tag app hat7tag 5artom dependencies

1) HW resources
2) licenses for OS and tools 
3) Configuration for each VM

still all of that better than the psychical servers but are there better solution ? 

name node make VM template out of it 

import(Provision) name node and run your VM + unique configuration if need 

but to make the VM template the dependency here is the tech expert to create the template and to setup the template 


my problem here it the various OS version on multiple VHW offered from the hypervisor 


os is -> kernel +++ user mode(GUI) fuck it i dont need it & kernel mode (el7ta elsoda elfel awl) i need it very important 

so **containers** main idea is tailor it self and dependencies on the kernel daemons which is constant across all the os versions in all VMs in that way we shared the kernel across multiple apps so the configuration and licenses is done 1 time 

that's applied by Virtual machine concept  which is 

base disks :

web template 
  
webapp 
layers 
layers 
layers 
.vhd -> virtual disk base disk(base image) has all custom configuration
Now we need tens of the that .vhd to make the load balancing cluster for our webapp ... 
1 -> full copy of the .vhd and paste it bera7tk but not efficient 

2 -> deal with base image as the template 
.AVHD -> Differancing disk which is the configuration unique on the clone VM lets say the new things is just 1GB so the .AVHD is 1GB worth of differences from the parent .VDH and the clone became the total of the parent (base image ) which is 100GB and 1 GB which is the .AVHD


base image - differencing disk - > differencing disk -> differencing disk

every diffrencing disk depends on his dady 



containers apply this concept by the idea of linux kernel is the same every where windows kernel is the same every where 


container 
App
requirements on top of os
requirements on top of os
OS kernel related specs (dependencies , commands , Daemons , services)



ka2n kda lma el container yenzl 3la os bybda2 yekml 3la elkernel el mawgoda le7ad ama yetl3 lel app 
ya3ny ka2nana gebna el app bel kernel beta3o we shelna el user mode we el7etat beta3t elkernel elhya sabta 3la kol el linux distro since in general all linux kernels is the same bec. 
linux kernel + specification -> Redhat
linux kernel + specification -> Ubuntu
linux kernel + specification -> SUSE


so in container we sticked to whats constant which is the kernel and add specification specific to our app 





how containers apply the concept of differencing is layers 



container image == vm template
app 
python config file - > layer
python   -> layer 
os specs -> layer (suse container)
starts with machine kernel

each layer is like a differencing disks in VMS and all layers can be merged same as in vms bas a7san en e7na man3mlsh merge 

vm template read only we copy and use the copy do our thing 

container (build)-> image
image <- (pull + create) container

running vm (export)-> vm template
vm template <- (import) running vm


cgroups |namespaces #themoreyoufuckaroundthemoreyouknow 

**cgroups** have a hierarchical structure with root and child, each with resource limits set by controllers — for example, a CPU controller for CPU time or a memory controller for memory.
We can use cgroups for various purposes, such as controlling resource usage in a multi-tenant environment, providing Quality of Service (QoS) guarantees, and running containers.

**Namespaces** are a Linux kernel feature that isolates various aspects of a process. **They provide a process with its own isolated view of the system, such as its own file system, network, hostname, and more.** Likewise, they allow us to create isolated environments for processes so that they can’t access or affect other processes or the host system.
There are several types of them available in Linux, such as:
- Mount: isolates a process’s view of the filesystem
- PID: isolates a process’s view of the process tree
- Network: isolates a process’s view of the network stack
- User: isolates a process’s view of user and group IDs
They are often combined with cgroups to provide container isolation and resource management.

cgroups and namespaces are crucial tools for managing resources in Linux systems with distinct functions and purposes. **cgroups limit and distribute resources like CPU, memory, I/O, and network bandwidth among groups of processes, using root and child cgroups and controllers for setting resource limits.** They are useful in multi-tenant environments, QoS, and container execution.

**Namespaces, in contrast, isolate various process elements, creating separate environments that prevent them from accessing or affecting other processes or the host system.** Different types, such as mount, PID, and network, isolate different process aspects. In addition, they are often combined with cgroups to provide isolation and resource management for containers

--------------------------------------

