import subprocess
import json
import os
import re

out_dir = "inflow/Terraform-Azure-PiyushSachdeva/metadata"
inflow_dir = "inflow/Terraform-Azure-PiyushSachdeva"
os.makedirs(out_dir, exist_ok=True)
os.makedirs(inflow_dir, exist_ok=True)

print("Fetching playlist video list...")
cmd = ['yt-dlp', '--flat-playlist', '--dump-json', 'https://www.youtube.com/playlist?list=PLl4APkPHzsUUHlbhuq9V02n9AMLPySoEQ']
res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
entries = []
for line in res.stdout.strip().splitlines():
    if line:
        data = json.loads(line)
        vid = data.get('id')
        title = data.get('title')
        entries.append({
            'id': vid,
            'title': title,
            'url': f'https://www.youtube.com/watch?v={vid}'
        })

print(f"Cataloged {len(entries)} videos.")
with open(os.path.join(inflow_dir, "catalog.json"), "w", encoding="utf-8") as f:
    json.dump(entries, f, indent=2)

def sanitize_filename(title):
    clean = re.sub(r'[\\/*?:"<>|]', "", title)
    clean = clean.replace(" ", "_")
    return clean[:80]

print("Now fetching detailed metadata for each video...")
for idx, item in enumerate(entries):
    vid = item['id']
    title = item['title']
    json_path = os.path.join(out_dir, f"{idx:02d}_{vid}.json")
    
    if os.path.exists(json_path):
        continue
        
    print(f"[{idx+1}/{len(entries)}] Fetching metadata for {title}...")
    cmd_meta = ["yt-dlp", "--dump-json", "--no-download", f"https://www.youtube.com/watch?v={vid}"]
    r = subprocess.run(cmd_meta, capture_output=True, text=True, encoding="utf-8")
    if r.returncode == 0:
        raw = json.loads(r.stdout)
        meta = {
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
            json.dump(meta, out_f, indent=2)
    else:
        print(f"Error fetching metadata for {vid}: {r.stderr[:200]}")

print("Metadata fetch complete!")
