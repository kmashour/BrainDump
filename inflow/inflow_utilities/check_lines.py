with open('inflow/udemy_transcript_802576.txt', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

print("--- Sample around line 300 ---")
for i in range(295, 330):
    if i < len(lines):
        print(f"{i+1}: {lines[i].strip()}")

print("\n--- Sample around line 3000 ---")
for i in range(2995, 3030):
    if i < len(lines):
        print(f"{i+1}: {lines[i].strip()}")
