#!/usr/bin/env python3
import os
import re
import json
import sys
import urllib.request

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    print("[ERROR] 'youtube-transcript-api' is not installed.")
    print("Please install it by running: pip install youtube-transcript-api")
    sys.exit(1)

def get_playlist_videos(playlist_url):
    """Fetches the playlist HTML page and extracts all video IDs and titles."""
    print(f"[INFO] Fetching playlist metadata from: {playlist_url}")
    req = urllib.request.Request(
        playlist_url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    )
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
    except Exception as e:
        print(f"[ERROR] Failed to fetch playlist page: {e}")
        sys.exit(1)

    # Locate the script block containing ytInitialData JSON
    match = re.search(r'var ytInitialData = ({.*?});', html)
    videos = []
    
    if match:
        try:
            data = json.loads(match.group(1))
            # Drill down the nested YouTube JSON structure
            tabs = data['contents']['twoColumnBrowseResultsRenderer']['tabs']
            tab_content = tabs[0]['tabRenderer']['content']
            section_list = tab_content['sectionListRenderer']['contents']
            item_section = section_list[0]['itemSectionRenderer']['contents']
            playlist_renderer = item_section[0]['playlistVideoListRenderer']['contents']
            
            for item in playlist_renderer:
                if 'playlistVideoRenderer' in item:
                    renderer = item['playlistVideoRenderer']
                    video_id = renderer['videoId']
                    title = renderer['title']['runs'][0]['text']
                    videos.append({'id': video_id, 'title': title})
        except KeyError:
            pass

    # Fallback to regex extraction if JSON parsing fails due to UI changes
    if not videos:
        print("[WARN] JSON parsing failed, falling back to regular expression parsing...")
        video_ids = re.findall(r'"videoId":"([^"]+)"', html)
        seen = set()
        dedup_ids = [x for x in video_ids if not (x in seen or seen.add(x))]
        for vid in dedup_ids:
            videos.append({'id': vid, 'title': f"Video_{vid}"})

    return videos

def sanitize_filename(name):
    """Sanitizes names for save paths."""
    return re.sub(r'[\\/*?:"<>| ]', '_', name)

def format_transcript_with_timestamps(srt):
    """Formats raw transcript segments with bold timestamp prefixes."""
    lines = []
    for entry in srt:
        start_seconds = entry['start']
        minutes = int(start_seconds // 60)
        seconds = int(start_seconds % 60)
        time_str = f"**{minutes:02d}:{seconds:02d}**"
        text = entry['text'].replace('\n', ' ')
        lines.append(f"{time_str} {text}")
    return "\n\n".join(lines)

def download_transcripts(playlist_url, output_dir="transcripts"):
    os.makedirs(output_dir, exist_ok=True)
    videos = get_playlist_videos(playlist_url)
    
    if not videos:
        print("[ERROR] No videos found. Check if the playlist is public or unlisted.")
        return

    print(f"[INFO] Found {len(videos)} videos in playlist. Starting transcript extraction...")
    
    for idx, video in enumerate(videos, 1):
        safe_title = sanitize_filename(video['title'])
        file_path = os.path.join(output_dir, f"{idx:02d} - {safe_title}.txt")
        
        print(f"[{idx}/{len(videos)}] Extracting: {video['title']} ({video['id']})")
        
        try:
            # Fetch raw transcript, prioritize English, fallback to auto-translated/first available
            try:
                srt = YouTubeTranscriptApi.get_transcript(video['id'], languages=['en'])
            except Exception:
                # If English isn't direct, list available transcripts and fetch the first one
                transcript_list = YouTubeTranscriptApi.list_transcripts(video['id'])
                srt = transcript_list.find_transcript(['en']).fetch()
            
            # Format transcript with custom timestamps
            formatted_text = format_transcript_with_timestamps(srt)
            
            # Save the formatted text
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"Source URL: https://www.youtube.com/watch?v={video['id']}\n\n")
                f.write(formatted_text)
                
            print(f"  └─> Saved to {file_path}")
        except Exception as e:
            print(f"  └─> [FAILED] {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 extract_playlist_transcripts.py <PLAYLIST_URL> [output_directory]")
        sys.exit(1)
        
    url = sys.argv[1]
    out_dir = sys.argv[2] if len(sys.argv) > 2 else "inflow"
    
    download_transcripts(url, out_dir)
