---
tags:
  - Docker
Type: Reference Note
source: Elfakharny-Udemy-Course
page: 
Date: 2025-04-11T18:24:00
deadline: 
status:
---
we were introduced to a docker file to build a nodejs image and the process is similar for any application whether its ruby .net it doesn't matter
now we need to publish our image so we can move it around so we need to move it a place where we can pull it from. 

To push a docker image we need docker registry 
public registry -> any one can pull it  
private registry -> need credentials to pull images from it  

the Dockerhub is an example of a docker registry 

docker login registry url or (just go with the steps docker is completely integrated with Dockerhub)

docker push getting-started --> **will fail** 

docker pull ubuntu --> ubuntu == `docker.io/library/ubuntu:latest`
docker.io --> registry
library --> username , namespace , organization name 
`library is a namespace used by google`
ubuntu:latest --> ubuntu = image(repo)name , latest = (tag)

when we use ubuntu directly docker implicitly uses the whole name as represented above and that is only applicable from docker official images since if the path is not explicitly used docker will use its namespace to search for the required image 

1- change the tag (name) 
2- docker.io is not mandatory aslong as we are pushing into    docker hub

docker tag getting-started:latest username/getting-started:latest 
--> **renamed using docker tag** or by simply rebuilding the image but it takes more time 

**docker push username/getting-started:latest**

docker pull username/getting-started:latest

run the image and test it 
docker run -d -p 3000:3000 image-name 

any other platform except for docker its like github we go and create a repo on the platform and create a repo and use it to push our image like in red-hat quay

docker login quay.io

**docker tag username/getting-started:latest**
**quay.io\/username/getting-started:latest**

**push quay.io\/username/getting-started:latest**

we may use another repositories in order for better integration when using tool like open shift so quay.io will offer better integration 
same as gitlab and github



https://docs.docker.com/get-started/docker-concepts/building-images/build-tag-and-publish-an-image/
