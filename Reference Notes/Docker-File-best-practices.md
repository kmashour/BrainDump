---
tags:
  - Docker
Type: Reference Note
source: "[[Docker-File-Primer]]"
page: "-"
Date: 2025-04-14T18:34:00
deadline: 
status:
---
External sources citation Books articles Research papers blogs video-courses courses lectures External sources citation Books articles Research papers blogs video-courses courses lectures #followup  14-4-2025 Builtkit in Docker appears to be very important 


#### Essential practices.
- Use a Docker lintier  
  **a static code analysis tool used to flag programming errors, bugs, stylistic errors and suspicious constructs**.
- Check Docker language specific best practices
- [ ] Nana Devops  14/9/2025  --  #followup  14/9/2025

-  create a single application per container multiple process containers are a nightmare in development and operation 
- [ ] Research the case #Docker_Iam_your_mystery #followup  14/9/2025
  
- create configurable ephemeral containers twelve-factor app , set configuration defaults but don't store env relation configurations
- [ ] 12 factor app for more aptitude #followup 14/9/2025 #Docker_Iam_your_mystery https://12factor.net/  
#### Image Practices
- Understand how image operates 
  ![[Screenshot from 2025-04-14 23-37-44 3.png]]
- Use optimal image 
  ![[Screenshot from 2025-04-14 23-47-01.png]]
- pin versions everywhere
  
  |`2`|MAJOR → big changes, may break stuff|
  |`1`|MINOR → new features, backward compatible|
  |`3`|PATCH → bug fixes, backward compatible|
  image-name:MAJOR.MINOR.PATCH
  ![[Screenshot from 2025-04-14 23-50-40 4.png]]
- Create Image with optimal size 
  ![[Screenshot from 2025-04-15 00-05-00.png]]
  - use multi-stage whenever possible 
  ![[Screenshot from 2025-04-15 00-05-59.png]]

- Avoid any unnecessary files 
  ![[Screenshot from 2025-04-15 00-07-19 1.png]]

security Practices 
- ![[Screenshot from 2025-04-15 00-09-49.png]]
- ![[Screenshot from 2025-04-15 00-11-03.png]]
- ![[Pasted image 20250415001153.png]]
- ![[Pasted image 20250415001311.png]]
- [ ] 14/9/2025 #Docker_Iam_your_mystery #followup 

- ![[Screenshot from 2025-04-15 00-17-53 1.png]]
- ![[Screenshot from 2025-04-15 00-18-39.png]]

#### Misc Practices 
- ![[Screenshot from 2025-04-15 00-23-58.png]]
  ![[Screenshot from 2025-04-15 00-24-37.png]]
- ![[Screenshot from 2025-04-15 00-27-41.png]]  
  Package **metadata** includes:
    - The list of available packages
    - Their versions
    - Where to download them from   
    - Dependencies info
   It helps with:
    - Avoiding repeated downloads
    - Faster installs if you're installing again
     **p.s this are all great features but it doesn't align with the purpose of a container its as we said something that is just built once and packaged with dependencies all happens once when the image is built so no need for the extra load love !!**
  Containers should be:
     **Ephemeral, minimal, and reproducible**.
     Keeping package caches in them causes:
     -  **Bigger image size** (MBs of unnecessary stuff)
     -  **Outdated info** that might break reproducibility
     -  **Security issues** if old package data lingers

- ![[Pasted image 20250415004642.png]]
- ![[Pasted image 20250415005026.png]]





#followup 
![[Pasted image 20250415005414.png]]