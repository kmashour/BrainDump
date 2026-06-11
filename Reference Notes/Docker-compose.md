---
tags:
  - Docker
Type: Reference Note
source: Elfakharny-Udemy-Course
page: 
Date: 2025-04-12T18:19:00
deadline: 
status: true
---
docker compose used to host docker containers without the need for docker run or port forwarding just as we did in AWS beanstalk 

We will do something similar to PaaS we will host multiple docker container locally without needing to connect them or even use docker run through whats called docker compose 

Its (docker compose) a pool written in python to deal with micro-service application i.e multiple containers 

docker-compose handles any container that shuts down automatically, so all containers within the docker compose up and running , the problem is how will the containers communicate internally for micro-services based applications like database and **how and which containers will be able to communicate with the outside world,** Docker compose can handle all of that through making networks for all containers defined within the docker-compose, volumes all is configured through yml file and docker compose will run it, its not exactly a Paas like beanstalk but very similar to it so we can do all of the above without writing even one docker command.... 

we can use **service label** in docker-compose more convenient and readable its the same as the hosts file in linux based systems

In Case using just Docker run any container that crashes will make the application collapse just like a circuit and its more of hassle to implement it 

We will work on a Microservice weather application 
Authentication service (GO) --> so the user needs login  
Database used (MySQL) --> we can use any SQL Database 
UI service --> html and CSS 
weather service --> retrieve the weather data using 
OPEN-weather API

Imagine making a VM for each service total shit show !! .

Multi-stage build is used in Go docker file and the reason for that is to minimize my image size and that what makes me Batman of Docker 

#Docker_best_practice 
Multi-stage docker: Best practices 
**from is what defines the base image** 
we use **from** twice, Go is a compiled language so we take the binary which is the output of the build from the first container and **just add the output of the build to the **2nd image** so the 1st image is just a buffer for building so we were able to discard all the build tools that would have been only used once,
**thats the 1st catch and the 2nd is security wise is better since less tools less vulnerabilities**  


docker compose is a python application so can use 
pip 
apt 
yum 
brew 

In the application directory
vim docker-compose.yml --> default name use by docker compose

docker compose will deal with the container as a service .. 

==yml file is used for docker compose==

![[Docker+compose.html]]

```html
Clone the weather app from GitLab:

git clone https://gitlab.com/abohmeed/moderndevops-weatherapp.git

Install docker-compose:

brew install docker-compose

Create the `docker-compose.yaml` file as follows:
version: '3'code
services:

  auth:

    restart: always  --> optional, here it states on undefined action  
     do an automatic restart		

    build: ./auth    ---> we either tell docker compose to pull an          image or use build a docker file

    depends_on:

      - db

    environment: 

      DB_HOST: db

      DB_USER: root

      DB_PASSWORD: my-secret-pw

      DB_NAME: authdb

    networks:

      - app-net -> bridge network so container could commincate by name         which is the service name 

  ui:

    restart: always

    build: ./UI

    depends_on:

      - auth

      - weather

    environment:

      AUTH_HOST: auth

      AUTH_PORT: 8080

      WEATHER_HOST: weather

      WEATHER_PORT: 5000

    ports:

      - "3000:3000"

    networks:

      - app-net

  weather:

    restart: always

    build: ./weather

    environment:

      APIKEY: 6d92c50bdamsh81137f3b87ace1fp1d53eejsnfe818b9dbc83

    networks:

      - app-net

  db:

    restart: always

    image: mysql:8.0.25

    environment:

      MYSQL_ROOT_PASSWORD: my-secret-pw --> when database starts for          the first time it must be configured with a password

      MYSQL_DATABASE: authdb

    networks:

      - app-net

    volumes:

      - ./db-data:/var/lib/mysql

networks:
   
  app-net:

    driver: bridge

volumes:

  db-data:     -> its not necessary in bind mounts but in named volume                    it is, for now just stick with writing it till we                       know for sure btw the way used above is bind mount 

```

Remember to add version 3 at the start of yml file
Run the file:
**docker-compose up -d**  --> -d in detach mode if its in foreground the terminal will be flooded with logs of the yml command execution by default as we said the docker-compase looks for a file called 
------- docker-compose.yml ---------- in the project working directory
running this command more than once is completely fine if a service is already up its just passes to the next step in the build

**docker logs** --> to print the logs if there is a problem or if a container fails sometime port mapping could cause a problem when conflicts happens to multiple containers listening on the same mapped port

**docker-compose ps** --> Show the status

Bring the application down:
docker-compose down --> delete and removes everything the docker-compose created

#Docker_best_practice 
**security best practice in docker compose** 
**is to put the authentication which user names and passwords and api keys in environment variables instead of plain text so instead of exporting every environment variable we can create**


#Docker_best_practice 
vim .env --> docker compose recognize this file when created within the the project directory this file is added to .gitignore 

![[Screenshot from 2025-04-13 00-37-38.png]]

![[Screenshot from 2025-04-13 00-38-19.png]]


#Docker_Iam_your_mystery 
```
volumes:

  db-data:     -> its not necessary in bind mounts but in named volume                    it is, for now just stick with writing it till we                       know for sure btw the way used above is bind mount 
```
Do you **need** to define the volume at the end?
- **For bind mounts** (like `./db-data:/var/lib/mysql`) → **No**, you **do NOT** need to define it at the bottom under `volumes:`.
    Docker knows that `./db-data` is a path on your host, so it doesn't treat it as a Docker-managed volume.


```
networks:
   front-end: --> optional 
   back-end: -->  optional
  app-net:

    driver: bridge
```
we can add multiple network to cluster containers....


#Docker_Iam_your_mystery  Answered
how does docker compose build the yml file is it sequential i don't think so why is that ??? 
because we used and stated the network and volumes that where defined at the end of the file so it must have another approach ??????????
version 1 -- > sequential service build and link is a must 
version 2 -- > sequential services is not a must depends on solves this problem , links was still used 
version 3 -- > networks: made me completely substitute links : 
As of now version 1 and 2 are deprecated 3

In - Details - Answer
links: service-label 
to connect micro services instead of hard coding the connection credentials like with 
UI service --> DB 
Authentication --> DB 
Depending on system architecture 

version 1 -- > sequential service build and link is a must 

version 2 -- > sequential services is not a must depends on solves this problem , links was still used 

version 3 -- > networks: made me completely substitute links : 

As of now version 1 and 2 are deprecated 
