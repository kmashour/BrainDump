import subprocess
import json
import os
import re

with open("inflow/inflow_utilities/savill_deep_dives_catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

meta_dir = "inflow/AZ-104-JohnSavill-DeepDives/metadata"
inflow_dir = "inflow/AZ-104-JohnSavill-DeepDives"
os.makedirs(meta_dir, exist_ok=True)
os.makedirs(inflow_dir, exist_ok=True)

master_file = "inflow/AZ-104-JohnSavill_DeepDives_Master_Transcript.md"

def sanitize_filename(title):
    clean = re.sub(r'[\\/*?:"<>|]', "", title)
    clean = clean.replace(" ", "_")
    return clean[:80]

master_entries = [
    "# John Savill - Azure Technical Training Deep Dives Master Index & Syllabus\n",
    "Source Playlist: https://www.youtube.com/playlist?list=PLlVtbbG169nGekKEV-l3TOXDLLEAj8jU2\n\n",
    "This master archive catalogues all 33 architectural deep-dive lectures from John Savill's Deep Dives series, providing full chapter breakdowns, whiteboard links, and architectural notes.\n\n",
    "---\n\n"
]

for idx, vid, title in catalog:
    json_path = os.path.join(meta_dir, f"{idx:02d}_{vid}.json")
    safe_title = sanitize_filename(title)
    md_path = os.path.join(inflow_dir, f"{idx:02d}_{safe_title}.md")
    
    # Check if cached
    data = None
    if os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            pass
            
    if not data:
        print(f"[{idx:02d}/33] Fetching: {title} ({vid})...")
        cmd = ["yt-dlp", "--dump-json", "--no-download", f"https://www.youtube.com/watch?v={vid}"]
        res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        if res.returncode == 0:
            raw = json.loads(res.stdout)
            data = {
                "id": vid,
                "title": raw.get("title") or title,
                "duration": raw.get("duration"),
                "chapters": raw.get("chapters"),
                "description": raw.get("description"),
                "webpage_url": raw.get("webpage_url") or f"https://www.youtube.com/watch?v={vid}",
                "upload_date": raw.get("upload_date"),
                "tags": raw.get("tags")
            }
            with open(json_path, "w", encoding="utf-8") as out_f:
                json.dump(data, out_f, indent=2)
        else:
            print(f"  -> ERROR fetching {vid}: {res.stderr[:200]}")
            data = {
                "id": vid,
                "title": title,
                "duration": 0,
                "chapters": [],
                "description": "Metadata extraction unavailable.",
                "webpage_url": f"https://www.youtube.com/watch?v={vid}",
                "upload_date": "",
                "tags": []
            }
            
    # Format markdown
    dur_mins = (data.get("duration") or 0) // 60
    dur_secs = (data.get("duration") or 0) % 60
    
    chapter_lines = []
    chapters = data.get("chapters") or []
    if chapters:
        chapter_lines.append("### Video Chapters & Timeline Breakdown\n")
        for ch in chapters:
            start = ch.get("start_time", 0)
            c_mins = int(start // 60)
            c_secs = int(start % 60)
            c_title = ch.get("title", "")
            chapter_lines.append(f"- **`{c_mins:02d}:{c_secs:02d}`** — {c_title}")
    else:
        chapter_lines.append("*No chapter markers provided by author.*")
        
    chapter_text = "\n".join(chapter_lines)
    desc_text = data.get("description") or "No description provided."
    
    md_content = f"""---
obsidianUIMode: preview
class: inflow-note
tier: inflow
domains:
  - "azure"
tags:
  - azure/deep-dive
  - azure/john-savill
  - status/inflow
video_id: "{vid}"
video_url: "{data.get('webpage_url')}"
title: "{data.get('title')}"
duration: "{dur_mins}m {dur_secs}s"
upload_date: "{data.get('upload_date')}"
---

# {idx:02d}: {data.get('title')}

**Source URL:** [{data.get('webpage_url')}]({data.get('webpage_url')})  
**Author:** John Savill (Azure Master Class Deep Dives)  
**Duration:** {dur_mins}m {dur_secs}s  

---

## 📑 Curriculum Structure & Timestamps

{chapter_text}

---

## 📝 Lecture Description & Architectural Resources

```text
{desc_text}
```
"""
    with open(md_path, "w", encoding="utf-8") as out_md:
        out_md.write(md_content)
        
    master_entries.append(f"""## {idx:02d}. {data.get('title')}
- **Video Link:** [{data.get('webpage_url')}]({data.get('webpage_url')})
- **Duration:** {dur_mins}m {dur_secs}s
- **Key Chapters:**
{chapter_text}

---

""")

with open(master_file, "w", encoding="utf-8") as mf:
    mf.writelines(master_entries)

print("Finished processing all 33 deep dives!")
