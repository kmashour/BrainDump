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
video_id: "Zk7A9U39JeI"
video_url: "https://www.youtube.com/watch?v=Zk7A9U39JeI"
title: "Microsoft Azure AD Resiliency Deep Dive"
duration: "77m 32s"
upload_date: "20211207"
---

# 11: Microsoft Azure AD Resiliency Deep Dive

**Source URL:** [https://www.youtube.com/watch?v=Zk7A9U39JeI](https://www.youtube.com/watch?v=Zk7A9U39JeI)  
**Author:** John Savill (Azure Master Class Deep Dives)  
**Duration:** 77m 32s  

---

## 📑 Curriculum Structure & Timestamps

### Video Chapters & Timeline Breakdown

- **`00:00`** — Introduction
- **`00:43`** — Azure AD basics
- **`03:47`** — Azure AD resiliency SLA
- **`05:04`** — Change and Safe Deployment Platform
- **`07:37`** — Azure AD replication boundaries
- **`15:50`** — Fault domains
- **`16:50`** — The core store
- **`19:27`** — Types of replica
- **`26:44`** — B2C sharding
- **`28:06`** — Authentication service (ESTS)
- **`29:58`** — Scale units/cells
- **`31:48`** — Gateway
- **`34:47`** — User interactions cross geo
- **`37:55`** — Backup authentication
- **`43:37`** — What we can do
- **`44:14`** — Sync resiliency
- **`46:30`** — Tenant configurations
- **`52:43`** — Continuous Access Evaluation
- **`61:08`** — What can developers do
- **`64:04`** — Proactive token refresh
- **`66:20`** — Use managed identities
- **`73:07`** — Summary
- **`76:53`** — Close

---

## 📝 Lecture Description & Architectural Resources

```text
In this video I explore the different aspects of resiliency for Microsoft Azure Active Directory (AD). This includes what Microsoft does to ensure resiliency and then what we can do.

🔎 Looking for content on a particular topic? Search the channel. If I have something it will be there!

▬▬▬▬▬▬  C H A P T E R S ⏰  ▬▬▬▬▬▬
0:00 - Introduction
0:43 - Azure AD basics
3:47 - Azure AD resiliency SLA
5:04 - Change and Safe Deployment Platform
7:37 - Azure AD replication boundaries
15:50 - Fault domains
16:50 - The core store
19:27 - Types of replica
26:44 - B2C sharding
28:06 - Authentication service (ESTS)
29:58 - Scale units/cells
31:48 - Gateway
34:47 - User interactions cross geo
37:55 - Backup authentication
43:37 - What we can do
44:14 - Sync resiliency
46:30 - Tenant configurations
52:43 - Continuous Access Evaluation
1:01:08 - What can developers do
1:04:04 - Proactive token refresh
1:06:20 - Use managed identities
1:13:07 - Summary
1:16:53 - Close

▬▬▬▬▬▬  K E Y   L I N K S 🔗 ▬▬▬▬▬▬
► Whiteboard:
🔗 https://github.com/johnthebrit/RandomStuff/blob/master/Whiteboards/AADResiliency.svg
► AAD Resiliency Blog:
🔗 https://techcommunity.microsoft.com/t5/azure-active-directory-identity/identity-at-ignite-strengthen-resilience-with-identity/ba-p/2747271
► Where is my AAD data?:
🔗 http://aka.ms/aaddatamap
► AAD Resiliency Documentations:
🔗 https://docs.microsoft.com/azure/active-directory/fundamentals/resilience-in-infrastructure
► AAD Continuous Access Evaluation:
🔗 https://docs.microsoft.com/azure/active-directory/conditional-access/concept-continuous-access-evaluation

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
