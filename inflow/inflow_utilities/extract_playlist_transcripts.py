import urllib.request
import re
import os
import glob
import time
import requests
import sys
from youtube_transcript_api import YouTubeTranscriptApi

# Target directories
OUTPUT_DIR = "inflow/linux_administration"
PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLy1Fx2HfcmWBpD_PI4AQpjeDK5-5q6TG7"
TEST_VIDEO_ID = "oD5Y4Gzr6vw"

# Patch requests Session to enforce a timeout
orig_request = requests.Session.request
def patched_request(self, *args, **kwargs):
    kwargs['timeout'] = 5
    return orig_request(self, *args, **kwargs)
requests.Session.request = patched_request

def get_proxies():
    print("[INFO] Fetching SOCKS5 proxies...")
    urls = [
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt"
    ]
    proxies = []
    for url in urls:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as response:
                text = response.read().decode('utf-8')
                p = [line.strip() for line in text.split('\n') if line.strip()]
                proxies.extend(p)
        except Exception as e:
            print(f"[WARN] Failed to fetch proxy list from {url}: {e}")
    proxies = list(set(proxies)) # Deduplicate
    print(f"[INFO] Found {len(proxies)} unique SOCKS5 proxies.")
    return proxies

def get_playlist_videos(playlist_url):
    print(f"[INFO] Fetching playlist metadata from: {playlist_url}")
    req = urllib.request.Request(
        playlist_url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            html = response.read().decode('utf-8')
    except Exception as e:
        print(f"[ERROR] Failed to fetch playlist page: {e}")
        sys.exit(1)

    videos = []
    # Try Regex extraction
    video_ids = re.findall(r'"videoId":"([^"]+)"', html)
    seen = set()
    dedup_ids = [x for x in video_ids if not (x in seen or seen.add(x))]
    for vid in dedup_ids:
        videos.append({'id': vid, 'title': f"Video_{vid}"})

    print(f"[INFO] Playlist parse completed. Found {len(videos)} videos.")
    return videos

def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>| ]', '_', name)

def format_transcript_with_timestamps(srt):
    lines = []
    for entry in srt:
        start_seconds = entry['start'] if isinstance(entry, dict) else entry.start
        text = entry['text'] if isinstance(entry, dict) else entry.text
        minutes = int(start_seconds // 60)
        seconds = int(start_seconds % 60)
        time_str = f"**{minutes:02d}:{seconds:02d}**"
        text = text.replace('\n', ' ')
        lines.append(f"{time_str} {text}")
    return "\n\n".join(lines)

class ProxyRotator:
    def __init__(self, proxies):
        self.proxies = proxies
        self.current_index = 0
        self.active_session = None

    def get_session(self):
        if self.active_session:
            return self.active_session
        return self.rotate()

    def rotate(self):
        while self.current_index < len(self.proxies):
            proxy = self.proxies[self.current_index]
            self.current_index += 1
            print(f"[ROTATOR] Testing SOCKS5 proxy {self.current_index}/{len(self.proxies)}: {proxy}")
            session = requests.Session()
            session.proxies = {
                "http": f"socks5://{proxy}",
                "https": f"socks5://{proxy}"
            }
            try:
                api = YouTubeTranscriptApi(http_client=session)
                api.fetch(TEST_VIDEO_ID, languages=['en'])
                print(f"[ROTATOR] Success! Active proxy: {proxy}")
                self.active_session = session
                return session
            except Exception:
                pass
        print("[ROTATOR] Exhausted all proxies!")
        return None

    def mark_dead(self):
        print("[ROTATOR] Current proxy died or got blocked. Rotating...")
        self.active_session = None

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    videos = get_playlist_videos(PLAYLIST_URL)
    if not videos:
        print("[ERROR] No videos found in playlist.")
        sys.exit(1)

    proxies = get_proxies()
    if not proxies:
        print("[ERROR] No proxies available.")
        sys.exit(1)

    rotator = ProxyRotator(proxies)

    for idx, video in enumerate(videos, 1):
        # Check if file starting with f"{idx:02d} - " already exists
        existing = glob.glob(os.path.join(OUTPUT_DIR, f"{idx:02d} - *"))
        if existing:
            print(f"[{idx}/{len(videos)}] Skipping (Already Exists): {os.path.basename(existing[0])}")
            continue

        print(f"[{idx}/{len(videos)}] Need to download: {video['title']} ({video['id']})")
        
        success = False
        attempts = 0
        while not success and attempts < 10:
            session = rotator.get_session()
            if not session:
                print("[ERROR] No working sessions. Exiting.")
                sys.exit(1)

            try:
                api = YouTubeTranscriptApi(http_client=session)
                try:
                    srt = api.fetch(video['id'], languages=['en'])
                except Exception:
                    transcript_list = api.list(video['id'])
                    try:
                        srt = transcript_list.find_transcript(['ar', 'en']).fetch()
                    except Exception:
                        first_transcript = next(iter(transcript_list))
                        srt = first_transcript.fetch()

                formatted_text = format_transcript_with_timestamps(srt)
                safe_title = sanitize_filename(video['title'])
                file_path = os.path.join(OUTPUT_DIR, f"{idx:02d} - {safe_title}.txt")

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(f"Source URL: https://www.youtube.com/watch?v={video['id']}\n\n")
                    f.write(formatted_text)

                print(f"  └─> Saved to {file_path}")
                success = True
                # Delay between downloads
                time.sleep(3)
            except Exception as e:
                print(f"  └─> Failed with current proxy: {e}")
                rotator.mark_dead()
                attempts += 1
                time.sleep(1)

if __name__ == "__main__":
    main()
