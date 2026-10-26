import os
import re
import json
import glob

meta_dir = 'inflow/Terraform-Azure-PiyushSachdeva/metadata'
trans_dir = 'inflow/Terraform-Azure-PiyushSachdeva/transcripts'
inflow_dir = 'inflow/Terraform-Azure-PiyushSachdeva'

def clean_vtt(vtt_path):
    if not os.path.exists(vtt_path):
        return ''
    with open(vtt_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    clean_lines = []
    seen = set()
    for line in lines:
        line = line.strip()
        if not line or '-->' in line or line.startswith('WEBVTT') or line.startswith('Kind:') or line.startswith('Language:'):
            continue
        line = re.sub(r'<[^>]+>', '', line).strip()
        if line and line not in seen:
            seen.add(line)
            clean_lines.append(line)
    return ' '.join(clean_lines)

with open(os.path.join(inflow_dir, 'catalog.json'), 'r', encoding='utf-8') as f:
    catalog = json.load(f)

print(f'Generating inflow files for {len(catalog)} videos...')
for idx, item in enumerate(catalog):
    vid = item['id']
    title = item['title']
    meta_file = os.path.join(meta_dir, f'{idx:02d}_{vid}.json')
    meta = {}
    if os.path.exists(meta_file):
        with open(meta_file, 'r', encoding='utf-8') as mf:
            meta = json.load(mf)
            
    vtt_file = os.path.join(trans_dir, f'{idx:02d}_{vid}.en.vtt')
    transcript = clean_vtt(vtt_file)
    
    clean_title = re.sub(r'[\\/*?:\"<>|]', '', title).replace(' ', '_')[:70]
    out_md = os.path.join(inflow_dir, f'{idx:02d}_{clean_title}.md')
    
    chapters = meta.get('chapters') or []
    chapter_text = ''
    if chapters:
        chapter_text = '### Video Chapters & Timeline Breakdown\n\n'
        for ch in chapters:
            st = int(ch.get('start_time', 0))
            m, s = divmod(st, 60)
            chapter_text += f"- **`{m:02d}:{s:02d}`** — {ch.get('title', '')}\n"
            
    desc = meta.get('description', '')
    dur = meta.get('duration', 0)
    dur_m, dur_s = divmod(dur, 60)
    
    content = f"""---
obsidianUIMode: preview
class: inflow-note
tier: inflow
domains:
  - terraform
  - azure
source: https://www.youtube.com/watch?v={vid}
duration: "{dur_m:02d}:{dur_s:02d}"
tags:
  - terraform/azure
  - status/raw
---

# {title}

**Source URL:** [YouTube: {title}](https://www.youtube.com/watch?v={vid})  
**Duration:** `{dur_m:02d}:{dur_s:02d}` minutes

---

## 📋 Video Overview & Description

{desc}

---

{chapter_text}

---

## 📝 Full Video Transcript

{transcript if transcript else "*No transcript available.*"}
"""
    with open(out_md, 'w', encoding='utf-8') as out_f:
        out_f.write(content)

inflow_files = [f for f in os.listdir(inflow_dir) if f.endswith('.md')]
print(f'Successfully generated {len(inflow_files)} inflow markdown files.')
