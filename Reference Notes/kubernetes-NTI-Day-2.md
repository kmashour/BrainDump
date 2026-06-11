---
tags:
  - kubernetes
Type: Reference Note
source: NTI-gerges
page: 
Date: 2025-04-19T09:57:00
deadline: 
status:
---
Default behavior 
application (container) = POD 

use cases where a POD will contain two-containers , the second container is called container helper or side car and it usually have one and only one purpose which is to take logs

if a POD crashes it will automatically restart like in docker compose 

