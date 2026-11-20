import os
import re
import json
import time
from youtube_transcript_api import YouTubeTranscriptApi

CATALOG_PATH = "inflow/inflow_utilities/savill_deep_dives_catalog.json"
OUT_DIR = "inflow/AZ-104-JohnSavill-DeepDives"
CACHE_DIR = "inflow/inflow_utilities/transcripts_cache"
MASTER_PATH = "inflow/AZ-104-JohnSavill_DeepDives_Master_Transcript.md"

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    videos = json.load(f)

api = YouTubeTranscriptApi()

def sanitize_filename(title):
    clean = re.sub(r'[\\/*?:"<>|]', "", title)
    clean = clean.replace(" ", "_")
    return clean[:80]

def format_transcript_blocks(snippets):
    chunks_by_block = {}
    for item in snippets:
        start = item.get("start") if isinstance(item, dict) else item.start
        text = item.get("text") if isinstance(item, dict) else item.text
        text = text.replace("\n", " ").strip()
        if not text:
            continue
        block = int(start // 120)
        chunks_by_block.setdefault(block, []).append(text)
        
    output_blocks = []
    for block in sorted(chunks_by_block.keys()):
        mins = block * 2
        block_text = " ".join(chunks_by_block[block])
        output_blocks.append(f"**[{mins:02d}:00]** {block_text}")
        
    return "\n\n".join(output_blocks)

def main():
    dir_files = os.listdir(OUT_DIR)
    success_count = 0
    failed_videos = []
    
    # Store transcript text per index for master file
    video_transcripts = {}
    
    for idx, vid_id, title in videos:
        safe_title = sanitize_filename(title)
        prefix = f"{idx:02d}_"
        matches = [f for f in dir_files if f.startswith(prefix) and f.endswith(".md")]
        if matches:
            file_name = matches[0]
        else:
            file_name = f"{idx:02d}_{safe_title}.md"
            
        file_path = os.path.join(OUT_DIR, file_name)
        cache_path = os.path.join(CACHE_DIR, f"{vid_id}.json")
        url = f"https://www.youtube.com/watch?v={vid_id}"
        
        # Read existing file content if present
        current_content = ""
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                current_content = f.read()
                
        # Check if transcript already present in the markdown
        if "## 🎙️ Full Spoken Transcript" in current_content:
            parts = current_content.split("## 🎙️ Full Spoken Transcript")
            transcript_part = parts[1].strip()
            video_transcripts[idx] = transcript_part
            success_count += 1
            print(f"[{idx:02d}/33] ALREADY PRESENT in {file_name}")
            continue
            
        # Check if cached on disk
        snippets = None
        if os.path.exists(cache_path):
            try:
                with open(cache_path, "r", encoding="utf-8") as cf:
                    snippets = json.load(cf)
                print(f"[{idx:02d}/33] Loaded from cache: {title} ({len(snippets)} snippets)")
            except Exception as e:
                print(f"[{idx:02d}/33] Cache read error: {e}")
                
        # If not cached, attempt fetch
        if snippets is None:
            print(f"[{idx:02d}/33] Fetching transcript from YouTube: {title} ({vid_id})...")
            try:
                raw_snippets = api.fetch(vid_id)
                snippets = [{"start": s.start, "duration": s.duration, "text": s.text} for s in raw_snippets]
                with open(cache_path, "w", encoding="utf-8") as cf:
                    json.dump(snippets, cf)
                print(f"  -> SUCCESS ({len(snippets)} snippets fetched and cached)")
                time.sleep(3) # Polite delay to protect rate limits
            except Exception as e:
                print(f"  -> WARNING: Transcript unavailable for {vid_id} ({title}): {e}")
                failed_videos.append((idx, vid_id, title, str(e)))
                
        if snippets:
            formatted = format_transcript_blocks(snippets)
            video_transcripts[idx] = formatted
            success_count += 1
            
            # Append to file
            if current_content:
                # Ensure separation
                clean_base = current_content.rstrip()
                updated_content = f"{clean_base}\n\n---\n\n## 🎙️ Full Spoken Transcript\n\n{formatted}\n"
            else:
                updated_content = f"# {idx:02d}: {title}\n\n**Source URL:** [{url}]({url})\n\n---\n\n## 🎙️ Full Spoken Transcript\n\n{formatted}\n"
                
            with open(file_path, "w", encoding="utf-8") as out_f:
                out_f.write(updated_content)
        else:
            print(f"  -> File preserved as-is: {file_name}")

    # Now update consolidated master file
    print("\nUpdating consolidated master file...")
    master_lines = [
        "# John Savill - Azure Technical Training Deep Dives Master Index & Syllabus\n",
        "Source Playlist: https://www.youtube.com/playlist?list=PLlVtbbG169nGekKEV-l3TOXDLLEAj8jU2\n\n",
        "This master archive catalogues all 33 architectural deep-dive lectures from John Savill's Deep Dives series, providing full chapter breakdowns, whiteboard links, and complete spoken transcripts.\n\n",
        "---\n\n"
    ]
    
    for idx, vid_id, title in videos:
        url = f"https://www.youtube.com/watch?v={vid_id}"
        prefix = f"{idx:02d}_"
        matches = [f for f in dir_files if f.startswith(prefix) and f.endswith(".md")]
        file_name = matches[0] if matches else f"{idx:02d}_{sanitize_filename(title)}.md"
        file_path = os.path.join(OUT_DIR, file_name)
        
        # Read chapters if available from metadata
        meta_path = os.path.join(OUT_DIR, "metadata", f"{idx:02d}_{vid_id}.json")
        chapter_text = "*No chapter markers provided.*"
        dur_str = "N/A"
        if os.path.exists(meta_path):
            try:
                with open(meta_path, "r", encoding="utf-8") as mf:
                    mdata = json.load(mf)
                dur = mdata.get("duration", 0)
                dur_str = f"{dur // 60}m {dur % 60}s"
                chapters = mdata.get("chapters") or []
                if chapters:
                    ch_lines = ["### Video Chapters & Timeline Breakdown\n"]
                    for ch in chapters:
                        st = ch.get("start_time", 0)
                        ch_lines.append(f"- **`{int(st//60):02d}:{int(st%60):02d}`** — {ch.get('title', '')}")
                    chapter_text = "\n".join(ch_lines)
            except Exception:
                pass
                
        master_lines.append(f"## {idx:02d}. {title}\n")
        master_lines.append(f"- **Video Link:** [{url}]({url})\n")
        master_lines.append(f"- **Duration:** {dur_str}\n")
        master_lines.append(f"- **Key Chapters:**\n{chapter_text}\n\n")
        
        if idx in video_transcripts and video_transcripts[idx]:
            master_lines.append(f"### 🎙️ Full Spoken Transcript\n\n{video_transcripts[idx]}\n\n")
        else:
            master_lines.append("*Spoken transcript unavailable at time of ingestion due to YouTube upstream rate-limiting.*\n\n")
            
        master_lines.append("---\n\n")
        
    with open(MASTER_PATH, "w", encoding="utf-8") as out_m:
        out_m.writelines(master_lines)
        
    print(f"Master file updated: {MASTER_PATH}")
    print(f"\nSummary:")
    print(f"  Successfully processed transcripts: {success_count}/{len(videos)}")
    print(f"  Failed / rate-limited videos: {len(failed_videos)}/{len(videos)}")
    if failed_videos:
        for fv in failed_videos:
            print(f"    - [{fv[0]:02d}] {fv[2]} ({fv[1]}): {fv[3][:100]}")

if __name__ == "__main__":
    main()
