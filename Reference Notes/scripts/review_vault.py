#!/usr/bin/env python3
import os
import re
import sys
from urllib.parse import unquote

# Define Paths
BASE_DIR = "/home/karim/Desktop/CKA"
INFLOW_DIR = os.path.join(BASE_DIR, "inflow")
MAIN_NOTES_DIR = os.path.join(BASE_DIR, "Main Notes")
REF_NOTES_DIR = os.path.join(BASE_DIR, "Reference Notes")
GARDEN_DIR = os.path.join(BASE_DIR, "Digital Garden")
PROJECTS_DIR = os.path.join(BASE_DIR, "Projects")
BACKLOG_PATH = os.path.join(BASE_DIR, "backlog.md")

# ANSI Colors
GREEN = "\033[0;32m"
RED = "\033[0;31m"
YELLOW = "\033[1;33m"
BLUE = "\033[0;34m"
NC = "\033[0m"

def log_info(msg):
    print(f"{BLUE}[INFO]{NC} {msg}")

def log_ok(msg):
    print(f"{GREEN}[PASS]{NC} {msg}")

def log_warn(msg):
    print(f"{YELLOW}[WARN]{NC} {msg}")

def log_error(msg):
    print(f"{RED}[FAIL]{NC} {msg}")

def parse_frontmatter(file_path):
    """Simple regex parser for frontmatter to avoid external dependencies (PyYAML)."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    frontmatter = {}
    # Find block between first two --- lines
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        return frontmatter, content
    
    yaml_text = match.group(1)
    body = content[match.end():]
    
    # Basic line parsing
    current_key = None
    for line in yaml_text.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        # Check if list item
        list_match = re.match(r"^\s*-\s*\"?([^\"]*)\"?$", line)
        if list_match and current_key:
            if not isinstance(frontmatter[current_key], list):
                frontmatter[current_key] = []
            frontmatter[current_key].append(list_match.group(1))
            continue
        
        # Check if key-value pair
        kv_match = re.match(r"^([^:]+):\s*(.*)$", line)
        if kv_match:
            key = kv_match.group(1).strip()
            val = kv_match.group(2).strip().strip('"').strip("'")
            current_key = key
            if val == "":
                frontmatter[key] = []
            else:
                frontmatter[key] = val
                
    return frontmatter, body

def check_inflow_coverage():
    """Checks if files in inflow/ are accounted for in backlog.md or reference notes."""
    log_info("Auditing inflow files coverage...")
    if not os.path.exists(INFLOW_DIR):
        log_warn("Inflow directory not found.")
        return 0, 0
    
    inflow_files = []
    for f in os.listdir(INFLOW_DIR):
        if os.path.isfile(os.path.join(INFLOW_DIR, f)) and f.endswith(".md"):
            inflow_files.append(f)
            
    if not inflow_files:
        log_ok("No files found in inflow/ directory.")
        return 0, 0
    
    # Read backlog
    backlog_content = ""
    if os.path.exists(BACKLOG_PATH):
        with open(BACKLOG_PATH, "r", encoding="utf-8") as b:
            backlog_content = b.read()
            
    # Read all reference notes contents to search for keywords
    ref_notes_content = ""
    for root, _, files in os.walk(REF_NOTES_DIR):
        for f in files:
            if f.endswith(".md"):
                with open(os.path.join(root, f), "r", encoding="utf-8") as rn:
                    ref_notes_content += rn.read() + "\n"
                    
    uncovered = 0
    for file_name in inflow_files:
        base_name = file_name.replace(".md", "")
        # Check if mentioned in backlog or reference notes
        if base_name in backlog_content or base_name in ref_notes_content or file_name in backlog_content:
            log_ok(f"Inflow file '{file_name}' is covered in the vault.")
        else:
            log_warn(f"Inflow file '{file_name}' appears to be UN-INGESTED (not mentioned in backlog or reference notes).")
            uncovered += 1
            
    return len(inflow_files), uncovered

def verify_links():
    """Verifies all internal WikiLinks and relative Markdown links in the vault."""
    log_info("Verifying all vault links...")
    broken_md_links = 0
    placeholder_wikilinks = 0
    total_checked = 0
    
    # Gather all valid note files in vault to map targets (skipping inflow)
    all_notes = {}
    for root, _, files in os.walk(BASE_DIR):
        if ".git" in root or ".obsidian" in root or "inflow" in root:
            continue
        for f in files:
            if f.endswith(".md"):
                rel_path = os.path.relpath(os.path.join(root, f), BASE_DIR)
                base_name_lower = f.replace(".md", "").lower()
                all_notes[base_name_lower] = rel_path
                all_notes[rel_path.lower()] = rel_path
                
    for root, _, files in os.walk(BASE_DIR):
        if ".git" in root or ".obsidian" in root or "inflow" in root:
            continue
        for f in files:
            if not f.endswith(".md") or f in ["instructions.md", "backlog.md"]:
                continue
            file_path = os.path.join(root, f)
            rel_src_path = os.path.relpath(file_path, BASE_DIR)
            
            with open(file_path, "r", encoding="utf-8") as file_obj:
                content = file_obj.read()
                
            # 1. Check [[WikiLinks]] (treated as warnings/placeholders if missing)
            wiki_links = re.findall(r"\[\[(.*?)\]\]", content)
            for link in wiki_links:
                total_checked += 1
                target = link.split("|")[0].strip()
                target = target.split("#")[0].strip()
                
                if not target:
                    continue
                
                target_lower = target.lower()
                found = False
                if target_lower in all_notes:
                    found = True
                else:
                    for ext in ["", ".md"]:
                        test_path = target_lower + ext
                        if test_path in all_notes:
                            found = True
                            break
                            
                if not found:
                    log_warn(f"Placeholder/Future WikiLink in '{rel_src_path}': [[{link}]]")
                    placeholder_wikilinks += 1
                    
            # 2. Check Standard Markdown Links [text](relative_path) - hard errors
            md_links = re.findall(r"\[[^\]]*\]\((.*?)\)", content)
            for path in md_links:
                path = unquote(path)
                if path.startswith("http") or path.startswith("mailto:") or path.startswith("#") or path.startswith("file:///"):
                    continue
                
                total_checked += 1
                target_file_path = os.path.normpath(os.path.join(root, path.split("#")[0]))
                
                if not os.path.exists(target_file_path):
                    log_error(f"Broken Relative Link in '{rel_src_path}': [{path}]")
                    broken_md_links += 1
                    
    return total_checked, broken_md_links, placeholder_wikilinks

def verify_frontmatter():
    """Checks YAML frontmatter properties against directory rules and templates."""
    log_info("Auditing YAML frontmatter properties...")
    failures = 0
    
    # 1. Main Notes Directory
    if os.path.exists(MAIN_NOTES_DIR):
        for f in os.listdir(MAIN_NOTES_DIR):
            if not f.endswith(".md") or f == "Index.md":
                continue
            path = os.path.join(MAIN_NOTES_DIR, f)
            fm, _ = parse_frontmatter(path)
            
            note_class = fm.get("class")
            if not note_class:
                log_warn(f"Main Note '{f}' is missing 'class' property in frontmatter.")
                failures += 1
                continue
                
            if note_class == "landing-note":
                required = ["tier", "role", "domains", "related_concepts", "against", "reference_guides"]
                for req in required:
                    if req not in fm:
                        log_warn(f"Landing Note '{f}' is missing required property '{req}' in frontmatter.")
                        failures += 1
            elif note_class == "deeper-dive":
                required = ["parent_concept", "sub_type", "source_type"]
                for req in required:
                    if req not in fm:
                        log_warn(f"Deeper Dive Note '{f}' is missing required property '{req}' in frontmatter.")
                        failures += 1
                        
    # 2. Digital Garden Directory
    if os.path.exists(GARDEN_DIR):
        for f in os.listdir(GARDEN_DIR):
            if not f.endswith(".md") or f == "Index.md":
                continue
            path = os.path.join(GARDEN_DIR, f)
            fm, _ = parse_frontmatter(path)
            
            note_class = fm.get("class")
            if note_class != "pattern-note":
                log_warn(f"Digital Garden Note '{f}' has incorrect or missing 'class: pattern-note' in frontmatter.")
                failures += 1
                continue
                
            required = ["domains", "components", "sources"]
            for req in required:
                if req not in fm:
                    log_warn(f"Pattern Note '{f}' is missing required property '{req}' in frontmatter.")
                    failures += 1
                    
    return failures

def main():
    print("=" * 60)
    print("      KUBERNETES SECOND BRAIN VAULT INTEGRITY AUDIT")
    print("=" * 60)
    
    total_inflow, uncovered_inflow = check_inflow_coverage()
    print("-" * 60)
    
    total_links, broken_md_links, placeholder_wikilinks = verify_links()
    print("-" * 60)
    
    fm_failures = verify_frontmatter()
    print("=" * 60)
    print("                        AUDIT SUMMARY")
    print("=" * 60)
    
    # Inflow Summary
    if uncovered_inflow == 0:
        print(f"Inflow Coverage:   {GREEN}100% OK{NC} ({total_inflow}/{total_inflow} files integrated)")
    else:
        print(f"Inflow Coverage:   {YELLOW}WARNING{NC} ({uncovered_inflow}/{total_inflow} files un-ingested)")
        
    # Links Summary
    if broken_md_links == 0:
        print(f"Link Integrity:    {GREEN}100% OK{NC} ({total_links} links validated, {placeholder_wikilinks} placeholders)")
    else:
        print(f"Link Integrity:    {RED}BROKEN{NC} ({broken_md_links} broken relative paths detected)")
        
    # Frontmatter Summary
    if fm_failures == 0:
        print(f"Frontmatter Audit: {GREEN}100% OK{NC} (All notes conform to templates)")
    else:
        print(f"Frontmatter Audit: {YELLOW}WARNING{NC} ({fm_failures} schema violations detected)")
        
    print("=" * 60)
    
    if broken_md_links > 0:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
