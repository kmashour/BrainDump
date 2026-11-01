import re
import os

transcript_path = 'inflow/udemy_transcript_802576.txt'

with open(transcript_path, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

sections = []
current_sec = None

for idx, line in enumerate(lines):
    line_s = line.strip()
    if line_s.startswith('=== ') and line_s.endswith(' ==='):
        sec_title = line_s.strip('= ')
        current_sec = {'title': sec_title, 'line_start': idx + 1, 'lessons': []}
        sections.append(current_sec)
    elif line_s.startswith('--- ') and line_s.endswith(' ---'):
        lesson_title = line_s.strip('- ')
        if current_sec is not None:
            current_sec['lessons'].append({'title': lesson_title, 'line': idx + 1})
        else:
            # No section yet
            current_sec = {'title': 'Introduction', 'line_start': idx + 1, 'lessons': [{'title': lesson_title, 'line': idx + 1}]}
            sections.append(current_sec)

# calculate line ends
for i in range(len(sections)):
    if i < len(sections) - 1:
        sections[i]['line_end'] = sections[i+1]['line_start'] - 1
    else:
        sections[i]['line_end'] = len(lines)
    sections[i]['total_lines'] = sections[i]['line_end'] - sections[i]['line_start'] + 1

print(f"Total Sections identified: {len(sections)}\n")
for i, sec in enumerate(sections):
    print(f"Section {i+1:02d}: {sec['title']} (Lines {sec['line_start']} - {sec['line_end']}, Total lines: {sec['total_lines']}, Lessons: {len(sec['lessons'])})")
    for l in sec['lessons'][:3]:
        print(f"   - {l['title']}")
    if len(sec['lessons']) > 3:
        print(f"   ... and {len(sec['lessons']) - 3} more lessons")
