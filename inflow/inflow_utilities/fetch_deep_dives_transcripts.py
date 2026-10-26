import os
import re
import json
from youtube_transcript_api import YouTubeTranscriptApi

with open("inflow/inflow_utilities/savill_deep_dives_catalog.json", "r", encoding="utf-8") as f:
    videos = json.load(f)

out_dir = "inflow/AZ-104-JohnSavill-DeepDives"
os.makedirs(out_dir, exist_ok=True)
master_path = "inflow/AZ-104-JohnSavill_DeepDives_Master_Transcript.md"

api = YouTubeTranscriptApi()

def sanitize_filename(title):
    clean = re.sub(r'[\\/*?:"<>|]', "", title)
    clean = clean.replace(" ", "_")
    return clean[:80]

master_lines = [
    "# John Savill - Azure Deep Dives Master Class - Consolidated Transcripts\n",
    "Source Playlist: https://www.youtube.com/playlist?list=PLlVtbbG169nGekKEV-l3TOXDLLEAj8jU2\n\n",
    "---\n\n"
]

success_count = 0
failed_videos = []

for idx, vid_id, title in videos:
    safe_title = sanitize_filename(title)
    file_name = f"{idx:02d}_{safe_title}.md"
    file_path = os.path.join(out_dir, file_name)
    url = f"https://www.youtube.com/watch?v={vid_id}"
    print(f"[{idx:02d}/33] Fetching transcript: {title} ({vid_id})...")
    
    try:
        t = api.fetch(vid_id)
        body_lines = []
        current_chunk = []
        last_minute = -1
        
        for item in t:
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
  - azure/deep-dive
  - azure/john-savill
  - status/inflow
video_id: "{vid_id}"
video_url: "{url}"
title: "{title}"
---

# {title}

**Source URL:** [{url}]({url})
**Author:** John Savill (Azure Master Class Deep Dives)

---

## Transcript

{full_transcript}
"""
        with open(file_path, "w", encoding="utf-8") as out_f:
            out_f.write(content)
            
        master_lines.append(f"## {idx:02d}. {title}\n\n**Video URL:** [{url}]({url})\n\n{full_transcript}\n\n---\n\n")
        success_count += 1
        print(f"  -> SUCCESS ({len(t)} entries)")
    except Exception as e:
        print(f"  -> FAILED/UNAVAILABLE: {e}")
        failed_videos.append((idx, vid_id, title, str(e)))

with open(master_path, "w", encoding="utf-8") as mf:
    mf.writelines(master_lines)

print(f"\nCompleted: {success_count}/{len(videos)} transcripts fetched.")
if failed_videos:
    print(f"Failed count: {len(failed_videos)}")
    for f in failed_videos:
        print(f" - {f[0]}: {f[2]} ({f[3]})")
