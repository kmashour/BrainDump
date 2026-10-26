import os
import re
import sys
from youtube_transcript_api import YouTubeTranscriptApi

videos = [
    ("01", "usvlTo0TDoA", "Learn Azure in 2026"),
    ("02", "_x1V2ny8FWM", "What IS Microsoft Azure?"),
    ("03", "afzzawldfFk", "Azure Master Class v3 - Introduction"),
    ("04", "BqNbzeuxTaE", "Azure Master Class v3 - Part 1 - Cloud and Microsoft Azure 101"),
    ("05", "rMKmbZ1SYQg", "Master the Azure Pricing Calculator"),
    ("06", "megA6BPpYqo", "Azure Master Class v3 - Part 2 - Identity"),
    ("07", "uts0oy8NlUs", "The Line Between AD and Azure AD!"),
    ("08", "9P10hgPDRZg", "What are Azure AD External Identities?"),
    ("09", "1-x86jJuK7c", "Azure AD Administrative Units Overview"),
    ("10", "rC1TV0_sIrM", "Microsoft Azure Managed Identity Deep Dive"),
    ("11", "t-i4XrygWCc", "Azure Master Class v3 - Part 3 - Governance"),
    ("12", "qFoHDTxkQII", "Azure Role-Based Access Control Deep Dive"),
    ("13", "tGr1KqnuxeM", "Azure Master Class v3 - Part 4 - Resiliency"),
    ("14", "4nDRvZR2EjU", "Understanding Microsoft Azure Availability Zones!"),
    ("15", "8fvO3WArG-Y", "Disaster Recovery in Microsoft Azure"),
    ("16", "YnFkgLxqrKQ", "Azure Master Class v3 - Part 5 - Storage"),
    ("17", "nDtCSQyG_I8", "Azure Master Class v3 - Part 6 - Networking"),
    ("18", "nVZYDhB_M64", "AZ-700 Designing and Implement Azure Networking Study SUPER Guide!"),
    ("19", "KRBFVqgxyo4", "Azure Master Class v3 - Part 7 - VMs and VMSS"),
    ("20", "_UuO52KgwGk", "Creating your first Azure VM!"),
    ("21", "bMlkYLX4ZfQ", "Azure Master Class v2 - Module 8 - App Services"),
    ("22", "r6YIlPEC4y4", "DevOps Master Class - Part 7 - Containers & Friends"),
    ("23", "kmmuCapzX8I", "Azure Master Class v2 - Module 9 - Database & A.I."),
    ("24", "0gtpasITVnk", "DP-900 Data Fundamentals Study Cram v2"),
    ("25", "gzBXFnfvoXo", "Azure Master Class v2 - Module 10 - Monitoring & Security"),
    ("26", "rE-qgIgDCq8", "Defender for Cloud (Azure Security Center) and Azure Sentinel Overview (AZ-500)"),
    ("27", "9GXKjDJNB9s", "Azure Master Class v2 - Module 11 - IaC & DevOps"),
    ("28", "OcygSUFppsI", "Azure Master Class v2 - Closing Thoughts"),
    ("29", "sVq7qjU9LNE", "Azure AD Renamed! Enter Microsoft Entra ID"),
    ("30", "0Knf9nub4-k", "AZ-104 Administrator Associate Study Cram v2"),
]

def sanitize_filename(title):
    clean = re.sub(r'[\\/*?:"<>|]', "", title)
    clean = clean.replace(" ", "_")
    return clean[:80]

out_dir = "inflow/AZ-104-JohnSavill"
os.makedirs(out_dir, exist_ok=True)
master_path = "inflow/AZ-104-JohnSavill_Master_Transcript.md"

api = YouTubeTranscriptApi()

master_lines = [
    "# John Savill - AZ-104 Azure Administrator Master Class Study Playlist - Master Transcript\n",
    "Source Playlist: https://www.youtube.com/playlist?list=PLlVtbbG169nGlGPWs9xaLKT1KfwqREHbs\n\n",
    "---\n\n"
]

for idx, vid_id, title in videos:
    safe_title = sanitize_filename(title)
    file_name = f"{idx}_{safe_title}.md"
    file_path = os.path.join(out_dir, file_name)
    url = f"https://www.youtube.com/watch?v={vid_id}"
    print(f"[{idx}/30] Fetching transcript for: {title} ({vid_id})...")
    
    try:
        t = api.fetch(vid_id)
        # Format text with timestamps every minute or so
        body_lines = []
        current_chunk = []
        last_minute = -1
        
        for item in t:
            # item has 'start', 'duration', 'text'
            minute = int(item.start // 60)
            if minute != last_minute and minute % 2 == 0:
                if current_chunk:
                    body_lines.append(" ".join(current_chunk) + "\n\n")
                    current_chunk = []
                mins = int(item.start // 60)
                secs = int(item.start % 60)
                body_lines.append(f"**[{mins:02d}:{secs:02d}]** ")
                last_minute = minute
            current_chunk.append(item.text)
            
        if current_chunk:
            body_lines.append(" ".join(current_chunk) + "\n\n")
            
        full_transcript = "".join(body_lines)
        
        content = f"""---
obsidianUIMode: preview
class: inflow-note
tier: inflow
domains:
  - "azure"
tags:
  - azure/az-104
  - azure/john-savill
  - status/inflow
video_id: "{vid_id}"
video_url: "{url}"
title: "{title}"
---

# {idx}: {title}

**Source Video:** [{title}]({url})
**Instructor:** John Savill (Azure Master Class)

---

## 📝 Video Transcript & Key Concepts

{full_transcript}
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
            
        master_lines.append(f"## Lesson {idx}: {title}\n**URL:** {url}\n\n{full_transcript}\n\n---\n\n")
        print(f"  -> Saved {file_name} ({len(full_transcript)} chars)")
    except Exception as e:
        print(f"  -> Error fetching {vid_id}: {e}")

with open(master_path, "w", encoding="utf-8") as f:
    f.writelines(master_lines)

print(f"\nCompleted! Master transcript saved to {master_path}")
