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
video_id: "HnUNi1RMMTA"
video_url: "https://www.youtube.com/watch?v=HnUNi1RMMTA"
title: "Azure OpenAI Deployment Types and Resiliency"
duration: "50m 24s"
upload_date: "20241028"
---

# 32: Azure OpenAI Deployment Types and Resiliency

**Source URL:** [https://www.youtube.com/watch?v=HnUNi1RMMTA](https://www.youtube.com/watch?v=HnUNi1RMMTA)  
**Author:** John Savill (Azure Master Class Deep Dives)  
**Duration:** 50m 24s  

---

## 📑 Curriculum Structure & Timestamps

### Video Chapters & Timeline Breakdown

- **`00:00`** — Introduction
- **`00:21`** — Generative API is stateless
- **`02:21`** — Regional Azure OpenAI resource
- **`04:54`** — Capacity pools
- **`08:27`** — Responsible AI
- **`09:27`** — Model deployment types
- **`11:21`** — Standard
- **`11:56`** — Global
- **`12:17`** — Network vs inference latency
- **`14:42`** — Intelligent routing
- **`17:47`** — Quota vs available capacity
- **`19:30`** — Data zone and data residency
- **`22:50`** — Availability benefits?
- **`23:52`** — Resource is regional
- **`24:31`** — Multiple regional resources
- **`25:53`** — Enabling in the application
- **`26:49`** — API Management
- **`29:08`** — Prompt caching impact
- **`31:25`** — Provisioned service
- **`32:15`** — PayGo features
- **`36:26`** — PTU features
- **`43:24`** — Azure reservations
- **`45:36`** — Batch service
- **`47:26`** — Summary
- **`49:54`** — Close

---

## 📝 Lecture Description & Architectural Resources

```text
A dive into how Azure OpenAI works, what different deployment types mean for your use and how to think about the high availability of your deployments.

🔎 Looking for content on a particular topic? Search the channel. If I have something it will be there!

🤔  Due to the channel growth and number of people wanting help I no longer can answer or even read questions, and they will just stay in the moderation queue never to be seen so please post questions to other sites like Reddit, Microsoft Community Hub etc.

▬▬▬▬▬▬  C H A P T E R S ⏰  ▬▬▬▬▬▬
00:00 - Introduction
00:21 - Generative API is stateless
02:21 - Regional Azure OpenAI resource
04:54 - Capacity pools
08:27 - Responsible AI
09:27 - Model deployment types
11:21 - Standard
11:56 - Global
12:17 - Network vs inference latency
14:42 - Intelligent routing
17:47 - Quota vs available capacity
19:30 - Data zone and data residency
22:50 - Availability benefits?
23:52 - Resource is regional
24:31 - Multiple regional resources
25:53 - Enabling in the application
26:49 - API Management
29:08 - Prompt caching impact
31:25 - Provisioned service
32:15 - PayGo features
36:26 - PTU features
43:24 - Azure reservations
45:36 - Batch service
47:26 - Summary
49:54 - Close

▬▬▬▬▬▬  K E Y   L I N K S 🔗 ▬▬▬▬▬▬
► Whiteboard:
🔗 https://github.com/johnthebrit/RandomStuff/raw/master/Whiteboards/AzureOpenAIDeployments.png
► Azure OpenAI Pricing:
🔗 https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/
► PTU Calculator:
🔗 https://oai.azure.com/portal/calculator
► Official resiliency documentation:
🔗 https://learn.microsoft.com/azure/ai-services/openai/how-to/business-continuity-disaster-recovery

▬▬▬▬▬▬  Want to learn more? 🚀  ▬▬▬▬▬▬ 
📖 Recommended Learning Path for Azure
🔗 https://learn.onboardtoazure.com
🥇 Certification Content Repository
🔗 https://github.com/johnthebrit/CertificationMaterials
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
🧠 Mentoring Content
🔗 https://youtube.com/playlist?list=PLlVtbbG169nGHxNkSWB0PjzZHwZ0BkXZZ
❔ Questions? Maybe I answered it in my FAQ
🔗 https://savilltech.com/faq
👕 Cure Childhood Cancer Charity T-Shirt Channel Store
🔗 https://johns-t-shirts-store.creator-spring.com/

👂  Enable the subtitles and from there you can translate to your native language via the auto-translate feature in settings! https://youtu.be/v5b53-PgEmI for a demo of using this feature.

SUBSCRIBE  ✅  https://www.youtube.com/channel/UCpIn7ox7j7bH_OFj7tYouOQ?sub_confirmation=1

#Azure #AI #openai
```
