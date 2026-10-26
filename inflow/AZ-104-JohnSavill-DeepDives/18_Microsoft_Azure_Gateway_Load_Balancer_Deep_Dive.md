---
obsidianUIMode: preview
class: inflow-note
tier: inflow
domains:
  - "azure"
tags:
  - azure/deep-dive
  - azure/john-savill
  - status/inflow
video_id: "JLx7ZFzjdSs"
video_url: "https://www.youtube.com/watch?v=JLx7ZFzjdSs"
title: "Microsoft Azure Gateway Load Balancer Deep Dive"
duration: "32m 16s"
upload_date: "20211116"
---

# 18: Microsoft Azure Gateway Load Balancer Deep Dive

**Source URL:** [https://www.youtube.com/watch?v=JLx7ZFzjdSs](https://www.youtube.com/watch?v=JLx7ZFzjdSs)  
**Author:** John Savill (Azure Master Class Deep Dives)  
**Duration:** 32m 16s  

---

## 📑 Curriculum Structure & Timestamps

### Video Chapters & Timeline Breakdown

- **`00:00`** — Intro
- **`00:28`** — Offering public services
- **`01:42`** — Adding NVA in the flow
- **`04:00`** — Gateway load balancer
- **`06:23`** — Creating a gateway load balancer
- **`07:14`** — Chaining to a gateway load balancer
- **`10:40`** — Providers and consumers
- **`11:18`** — GW LB separation
- **`12:50`** — The flow of traffic
- **`15:20`** — Bump in the wire
- **`16:35`** — Enter VxLan
- **`19:38`** — Two tunnels
- **`24:14`** — My setup of the dummy NVA for testing
- **`27:00`** — Health probes and NSGs
- **`28:18`** — Looking at traffic through NVA
- **`29:40`** — Summary and next steps
- **`30:55`** — Me whining about a lack of autoexec.bat in Linux

---

## 📝 Lecture Description & Architectural Resources

```text
In this video we explore the Microsoft Azure Gateway Load Balancer to provider a seamless integration with Network Virtual Appliances and remove many of the previous NVA-associated pain points!

🔎 Looking for content on a particular topic? Search the channel. If I have something it will be there!

▬▬▬▬▬▬  C H A P T E R S ⏰  ▬▬▬▬▬▬
0:00 - Intro
0:28 - Offering public services
1:42 - Adding NVA in the flow
4:00 - Gateway load balancer
6:23 - Creating a gateway load balancer
7:14 - Chaining to a gateway load balancer
10:40 - Providers and consumers
11:18 - GW LB separation
12:50 - The flow of traffic
15:20 - Bump in the wire
16:35 - Enter VxLan
19:38 - Two tunnels
24:14 - My setup of the dummy NVA for testing
27:00 - Health probes and NSGs
28:18 - Looking at traffic through NVA
29:40 - Summary and next steps
30:55 - Me whining about a lack of autoexec.bat in Linux

▬▬▬▬▬▬  K E Y   L I N K S 🔗 ▬▬▬▬▬▬
► Whiteboard:
🔗 https://github.com/johnthebrit/RandomStuff/blob/master/Whiteboards/GWLBWhiteboard.png
► My setup file in GitHub:
🔗 https://github.com/johnthebrit/RandomStuff/blob/master/AzureNetworking/GWLB.sh
► Microsoft doc on creating a GW LB:
🔗 https://docs.microsoft.com/en-us/azure/load-balancer/tutorial-gateway-portal#create-gateway-load-balancer

▬▬▬▬▬▬  Want to learn more? 🚀  ▬▬▬▬▬▬ 
📖 Recommended Learning Path for Azure
🔗 https://learn.onboardtoazure.com
📅 Weekly Azure Update
🔗  https://youtube.com/playlist?list=PLlVtbbG169nEv7jSfOVmQGRp9wAoAM0Ks
☁ Azure Master Class
🔗  https://youtube.com/playlist?list=PLlVtbbG169nGccbp8VSpAozu3w9xSQJoY
⚙ DevOps Master Class
🔗  https://youtube.com/playlist?list=PLlVtbbG169nFr8RzQ4GIxUEznpNR53ERq
💻 PowerShell Master Class
🔗 https://youtube.com/playlist?list=PLlVtbbG169nFq_hR7FcMYg32xsSAObuq8
🎓 Certification Cram Videos
🔗  https://youtube.com/playlist?list=PLlVtbbG169nHz2qfLvPsAz9CnnXofhmcA
 ❔ Question about my setup?
🔗 https://youtube.com/playlist?list=PLlVtbbG169nHuSSHudxXDdn9Vz3T4-0mS

SUBSCRIBE  ✅  https://www.youtube.com/channel/UCpIn7ox7j7bH_OFj7tYouOQ?sub_confirmation=1

#microsoft #azure #johnsavillstechnicaltraining #onboardtoazure #cloud
```
