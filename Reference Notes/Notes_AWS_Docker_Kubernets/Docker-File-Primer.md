---
tags:
  - Docker
Type: Reference Note
source: Elfakharny-Udemy-Course
page: 
Date: 2025-04-11T18:25:00
deadline: 
status: true
DeeperDive: "[[Docker-Multi-stage-builds]]"
---
Docker file : docker offers a very simple to-do website to use as a playground for docker file its in java-script

#docker_post_script 
Docker file is useful so we can track what layers are added to the image and changes made for an image


1- clone the project from docker repository 
getting-started-app

cd getting-started-app
vim Dockerfile

**FROM node:18-alpine** --> constant updates and security patches, maintenance headache are not mine to worry about so if there is a base image with my needed runtime (in our case nodejs)  available please use it and reinvent the wheel, From is also used to determine the base image Iam going to build my image on

![[Screenshot from 2025-04-14 23-37-44 1.png]]

**WORKDIR /app** --> mdkir /app ; cd /app 

**COPY . .** --> copy files and directories from current working directory with respect to the image to /app in our case , we can use paths instead of . .
- `COPY <host-path> <image-path>` - this instruction tells the builder to copy files from the host and put them into the container image.
- we use .Dockerignore to add the files we don't want to copy it in the container ker-Networks￼￼
- ￼￼￼￼￼￼D

**ADD** --> can copy and download from URLs and decompress TAR archives, also can download and if the downloaded is compressed its decompressed and added to the image, if i want the file compressed then i must use COPY  

(we need some dependencies and the image we are using already handled the needed tools like **yarn** its there as a part of the node-18 image its used to install the dependencies thats why its recommended to use an image with a runtime environment because any application will need dependencies to run) 

**RUN** --> yarn install --production && yarn cache clean
cache cleans 
-> discard any extra module and files thats not needed to reduce image size and we tended to use && to reduce the layers because if each are used with RUN it will be extra layers with potential to multiple duplicates because the new layer might need file from lower layers so copies overhead will be added to the image size 

**ENTRYPOINT** ["node"] --> the parent process of the container as long as that process is running the container will run, ["node"] is the file i want the container start so when we hit the command docker run , that file (command node) will execute the scripts under src/index.js we can also take that approach 
[] means its a list so we can pass whatever scripts we want to the node command to run it ["node", "src/index.js"]
["node", "src/index.js"] ---> syntax here is very strict take care of space after comma and every "" take only one parameter with no spaces 
#Docker_best_practice 
["node", "src/index.js"] **--> its very annoying and can't be tracked by validation tools because we need to put space after the comma, alternatively.**
**ENTRYPOINT node or ENTRYPOINT node src/index.js , after every space its interpreted as a new parameter we can bypass that by using \ (escape chatacter)** 

**CMD** ["src/index.js"] --> CMD is used as a best practice because the command here will be considered as a sub process of the entry point so now that container could run any script its the same as passing it as argument to the container like we did it earlier with busybox the only difference is that it didn't have an entrypoint command that persists 

**EXPOSE 3000**  --> just an indication that the app listens on port 3000 but this line doesn't mean that we exposed that port 
so if i wanted to expose the app it will be through mapping port 3000 to an port on the host pc

#Docker_best_practice 
*we use one to three version behind when using a base image i want to be in the area where i didn't lose my support and having my stable version ---> when upgrading to a new version i always refer to the release note* 

#docker_post_script #Docker_best_practice 
**docker build** **-t getting-started:v1 .**--> expect a file named Dockerfile with the same case's(capitalization) in the current working directory , if it has another name we use **-f** , **-t** is the tag and the **.** means the docker file is in current working directory this is where i will build **(some distros require the docker file name explicitly even if its the default name)**, **DON'T neglect the tag El versioning ya karim !!!**


docker image ls 
docker run -d -p 3000:3000 getting-started

docker run getting-started -e "console.log('hello')"
-> we did over ride the CMD command that was used in the Dockerfile 




#docker_post_script 
The documentation states for `CMD`-
> The main purpose of a CMD is to provide defaults for an executing container.

and for `ENTRYPOINT`:
> An ENTRYPOINT helps you to configure a container that you can run as an executable.

So, what's the difference between those two commands?

Docker has a default entrypoint which is `/bin/sh -c` but does not have a default command.
When you run docker like this: `docker run -i -t ubuntu bash` the entrypoint is the default `/bin/sh -c`, the image is `ubuntu` and the command is `bash`.
**The command is run via the entrypoint. i.e., the actual thing that gets executed is `/bin/sh -c bash`. This allowed Docker to implement `RUN` quickly by relying on the shell's parser.**
take care !!! when building an image if an entry point is not provided it takes the base image entry point as default 

Later on, people asked to be able to customize this, so `ENTRYPOINT` and `--entrypoint` were introduced.

Everything after the image name->(**`ubuntu`) in the example above, is the command and is passed to the entrypoint.** **When using the `CMD` instruction, it is exactly as if you were executing**  
**`docker run -i -t ubuntu <cmd>`**  
The parameter of the entrypoint is `<cmd>`.

You will also get the same result if you instead type this command `docker run -i -t ubuntu`: a bash shell will start in the container because in the [ubuntu Dockerfile](https://github.com/dockerfile/ubuntu/blob/master/Dockerfile) a default `CMD` is specified:  `CMD ["bash"]`.

**Example ..........**
As everything is passed to the entrypoint, you can have a very nice behavior from your images. this is a good, it shows how to use an image as a "binary"(حرفيا هشغلها علي انها أمر حقير). When using `["/bin/cat"]` as entrypoint and then doing `docker run img /etc/passwd`, you get it, `/etc/passwd` is the command and is passed to the entrypoint so the end result execution is simply `/bin/cat /etc/passwd`.

Another example would be to have any cli as entrypoint. For instance, if you have a redis image, instead of running `docker run redisimg redis -H something -u toto get key`, you can simply have `ENTRYPOINT ["redis", "-H", "something", "-u", "toto"]` and then run like this for the same result: `docker run redisimg get key`.

it all goes back to basic linux and shell commands 
```
docker run -d ubuntu:14.04 /bin/bash -c "while true; do echo hello  world;done"
```

> bash interprets the following options when it is invoked:
> -c string
> If the -c option is present, then commands are read from string. If there are arguments after the string, they are assigned to the positional parameters, starting with $0.

Without the `-c`, the `"while true..."` string is taken to be a filename for `bash` to open.

Resources:
https://docs.docker.com/reference/dockerfile/#entrypoint
https://docs.docker.com/build/building/best-practices/
https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/

External sources citation Books articles Research papers blogs video-courses courses lectures 

-------


▪ FROM: Initializes a new build stage and sets the Base Image
▪ RUN: Will execute any commands in a new layer
▪ CMD: Provides a default for an executing container. There can only be
one CMD instruction in a Dockerfile
▪ LABEL: Adds metadata to an image
▪ EXPOSE: Informs Docker that the container listens on the specified
network ports at runtime
▪ ENV: Sets the environment variable <key> to the value <value>
▪ ADD: Copies new files, directories or remote file URLs from <src> and
adds them to the filesystem of the image at the path <dest>.
▪ COPY: Copies new files or directories from <src> and adds them to
the filesystem of the container at the path <dest>.Dockerfile instructions
▪ ENTRYPOINT: Allows for configuring a container that will run as an executable
▪ VOLUME: Creates a mount point with the specified name and marks it as holding
externally mounted volumes from native host or other containers
▪ USER: Sets the user name (or UID) and optionally the user group (or GID) to use
when running the image and for any RUN, CMD,
▪ WORKDIR: Sets the working directory for any RUN, CMD, ENTRYPOINT, COPY, and
ADD instructions that follow it in the Dockerfile
▪ ARG: Defines a variable that users can pass at build-time to the builder with the
docker build command, using the --build-arg <varname>=<value> flag
▪ ONBUILD: Adds a trigger instruction to the image that will be executed at a later
time, when the image is used as the base for another build
▪ HEALTHCHECK: Tells Docker how to test a container to check that it is still
working
▪ SHELL: Allows the default shell used for the shell form of commands to be
overridden