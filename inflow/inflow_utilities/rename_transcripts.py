#!/usr/bin/env python3
import os
import re
import json
import urllib.request
import time

DIRECTORY = "inflow/linux_administration"

def get_video_title(video_id):
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
    req = urllib.request.Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data['title']
    except Exception as e:
        print(f"  [ERROR] oEmbed failed for {video_id}: {e}")
        return None

def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>| ]', '_', name)

def main():
    if not os.path.exists(DIRECTORY):
        print(f"[ERROR] Directory {DIRECTORY} not found.")
        return

    files = sorted([f for f in os.listdir(DIRECTORY) if f.endswith(".txt")])
    print(f"[INFO] Scanning {len(files)} files in {DIRECTORY}...")

    for f in files:
        # Match pattern: e.g. "01 - Video_oD5Y4Gzr6vw.txt"
        match = re.match(r"^(\d+)\s*-\s*Video_([a-zA-Z0-9_-]+)\.txt$", f)
        if not match:
            # Check if it has a Video ID but different format
            match = re.search(r"Video_([a-zA-Z0-9_-]+)\.txt$", f)
            if not match:
                continue
            video_id = match.group(1)
            num_prefix = f.split(" - ")[0] if " - " in f else "00"
        else:
            num_prefix = match.group(1)
            video_id = match.group(2)

        file_path = os.path.join(DIRECTORY, f)
        print(f"Resolving title for {video_id} (Prefix: {num_prefix})...")
        
        # Read the file to ensure we get the source URL if needed
        try:
            with open(file_path, "r", encoding="utf-8") as file_obj:
                first_line = file_obj.readline()
                url_match = re.search(r"watch\?v=([a-zA-Z0-9_-]+)", first_line)
                if url_match:
                    video_id = url_match.group(1)
        except Exception:
            pass

        title = get_video_title(video_id)
        if title:
            safe_title = sanitize_filename(title)
            new_filename = f"{num_prefix} - {safe_title}.txt"
            new_path = os.path.join(DIRECTORY, new_filename)
            
            if file_path != new_path:
                os.rename(file_path, new_path)
                print(f"  └─> Renamed to: {new_filename}")
        else:
            print(f"  └─> Skipping rename due to resolution error.")
        
        # Sleep for a bit to avoid hammering the oEmbed API
        time.sleep(1)

if __name__ == "__main__":
    main()
