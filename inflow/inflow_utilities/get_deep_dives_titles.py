import urllib.request
import re
import json

url = 'https://www.youtube.com/playlist?list=PLlVtbbG169nGekKEV-l3TOXDLLEAj8jU2'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
html = urllib.request.urlopen(req).read().decode('utf-8')

# The video IDs appear in playlist order
# In youtube playlist html, there are often entries like:
# "url":"/watch?v=...&list=PLlVtbbG169nGekKEV-l3TOXDLLEAj8jU2&index=..."
matches = re.findall(r'/watch\?v=([a-zA-Z0-9_-]{11})(?:&amp;|&)list=PLlVtbbG169nGekKEV-l3TOXDLLEAj8jU2(?:&amp;|&)index=(\d+)', html)
indexed_vids = {}
for vid, idx in matches:
    indexed_vids[int(idx)] = vid

print(f"Found {len(indexed_vids)} indexed videos.")
if not indexed_vids:
    vids = re.findall(r'watch\?v=([a-zA-Z0-9_-]{11})', html)
    seen = set()
    order = []
    for v in vids:
        if v not in seen:
            seen.add(v)
            order.append(v)
    for i, v in enumerate(order, 1):
        indexed_vids[i] = v

# Let's get title for each video
results = []
for idx in sorted(indexed_vids.keys()):
    vid = indexed_vids[idx]
    # Fetch oembed or video page title
    try:
        oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
        o_req = urllib.request.Request(oembed_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(o_req, timeout=5) as o_resp:
            meta = json.loads(o_resp.read().decode('utf-8'))
            title = meta.get("title")
    except Exception as e:
        title = "Unknown"
    print(f"{idx:02d}. [{vid}] {title}")
    results.append((idx, vid, title))

with open("inflow/inflow_utilities/savill_deep_dives_catalog.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)
