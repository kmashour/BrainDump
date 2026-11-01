with open('inflow/udemy_transcript_802576.txt', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

lessons_after_3005 = []
for idx in range(3004, len(lines)):
    line_s = lines[idx].strip()
    if line_s.startswith('--- ') and line_s.endswith(' ---'):
        lessons_after_3005.append((idx + 1, line_s.strip('- ')))

print(f"Total lessons after line 3005: {len(lessons_after_3005)}\n")
for line_num, title in lessons_after_3005:
    print(f"Line {line_num}: {title}")
