---
tags:
  - kubernetes
Type: Reference Note
source: Elfakharny-Udemy-Course
page: "-"
Date: 2025-04-20T13:24:00
deadline: 
status:
---
Annotation can't be used to filter data its used to save metadata on pod or resources to be generic it doesn't have those strict rules in labels 

as best practice if i want key value database its better to use redis instead of using api-server as general purpose database because annotations are data saved in the pods (resource)

real-life example to why we use annotations to can be used to instruct Prometheus how to scrap  

![[Screenshot from 2025-04-20 13-37-13.png]]