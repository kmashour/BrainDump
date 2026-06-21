#!/usr/bin/env python3
import os
import re
import sys
import ssl
import urllib.request
import urllib.parse
from html.parser import HTMLParser

# Disable SSL verification to prevent issues on various docs pages
try:
    ssl_context = ssl._create_unverified_context()
except AttributeError:
    ssl_context = None

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

# Re-use URL matching logic from review_vault.py
def is_doc_url(url):
    url_lower = url.lower()
    # Exclude images, binary files, social media, shorteners, playgrounds, code repositories
    exclude_patterns = [
        "twitter.com", "facebook.com", "instagram.com", "youtube.com", "youtu.be",
        "linkedin.com", "img-c.udemycdn.com", "bit.ly", "kode.wiki", "placeholder.example.com",
        "image-checker-webhook", ".png", ".jpg", ".jpeg", ".gif", ".svg", 
        "github.com/kubernetes/website/commit", "github.com/aws/secrets-store-csi-driver-provider-aws",
        "github.com/kubernetes/autoscaler", "github.com/kubernetes-sigs", "github.com/aws/secrets-store-csi-driver",
        "killercoda.com", "kodekloud.com", "labs.iximiuz.com", "minikube.sigs.k8s.io", "vaultproject.io",
        "kubernetes.io/docs/reference/generated", "kubernetes.io/docs/reference/kubernetes-api"
    ]
    for pattern in exclude_patterns:
        if pattern in url_lower:
            return False
            
    # Include doc sites
    doc_domains = ["kubernetes.io/docs", "secrets-store-csi-driver.sigs.k8s.io"]
    for domain in doc_domains:
        if domain in url_lower:
            return True
            
    return False

class SimpleHTMLToMarkdown(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.markdown = []
        self.links = []
        self.in_body = False
        self.current_tag = None
        self.skip_content = False
        self.list_depth = 0
        self.in_code = False
        
    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        if tag == 'body':
            self.in_body = True
        if tag in ['script', 'style', 'nav', 'footer', 'header', 'aside']:
            self.skip_content = True
        if tag in ['pre', 'code']:
            self.in_code = True
            if tag == 'pre':
                self.markdown.append("\n```\n")
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.markdown.append("\n" + "#" * int(tag[1]) + " ")
        if tag == 'p':
            self.markdown.append("\n")
        if tag in ['ul', 'ol']:
            self.list_depth += 1
            self.markdown.append("\n")
        if tag == 'li':
            self.markdown.append("  " * (self.list_depth - 1) + "- ")
        if tag == 'tr':
            self.markdown.append("\n| ")
        if tag in ['td', 'th']:
            self.markdown.append(" ")
            
        # Collect links for sublink crawling
        if tag == 'a':
            for attr, val in attrs:
                if attr == 'href':
                    # Resolve relative link to absolute link
                    abs_url = urllib.parse.urljoin(self.base_url, val)
                    self.links.append(abs_url)
                    
    def handle_endtag(self, tag):
        if tag == 'body':
            self.in_body = False
        if tag in ['script', 'style', 'nav', 'footer', 'header', 'aside']:
            self.skip_content = False
        if tag in ['pre', 'code']:
            self.in_code = False
            if tag == 'pre':
                self.markdown.append("\n```\n")
        if tag in ['ul', 'ol']:
            self.list_depth = max(0, self.list_depth - 1)
        if tag in ['td', 'th']:
            self.markdown.append(" |")
        self.current_tag = None
        
    def handle_data(self, data):
        if self.in_body and not self.skip_content:
            clean_data = data.strip()
            if clean_data:
                if self.in_code:
                    self.markdown.append(data) # Preserve whitespaces for code
                else:
                    # Remove multiple consecutive spaces/newlines
                    clean_data = re.sub(r'\s+', ' ', clean_data)
                    self.markdown.append(clean_data + " ")

def fetch_url_html(url):
    log_info(f"Fetching URL: {url}")
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    )
    try:
        kwargs = {}
        if ssl_context:
            kwargs['context'] = ssl_context
        with urllib.request.urlopen(req, timeout=15, **kwargs) as response:
            html = response.read()
            # Try decoding with utf-8, fallback to latin-1
            try:
                return html.decode('utf-8')
            except UnicodeDecodeError:
                return html.decode('latin-1')
    except Exception as e:
        log_error(f"Failed to fetch {url}: {e}")
        return None

def extract_sublinks(parent_url, discovered_links):
    """Filters discovered links to find sublinks on the same base domain and path."""
    parsed_parent = urllib.parse.urlparse(parent_url)
    parent_path = parsed_parent.path.rstrip('/')
    # Get directory path of the parent
    parent_dir = os.path.dirname(parent_path) if '.' in os.path.basename(parent_path) else parent_path
    
    sublinks = set()
    for link in discovered_links:
        # Strip anchors and query params
        link = link.split('#')[0].split('?')[0].rstrip('/')
        parsed_link = urllib.parse.urlparse(link)
        
        if parsed_link.netloc == parsed_parent.netloc:
            # Check if it starts with the same directory prefix and is not the parent itself
            if parsed_link.path.startswith(parent_dir) and parsed_link.path != parent_path:
                sublinks.add(link)
                
    return sorted(list(sublinks))

def scrape_and_format(url, visited_urls):
    if url in visited_urls:
        return "", []
    visited_urls.add(url)
    
    html = fetch_url_html(url)
    if not html:
        return "", []
        
    parser = SimpleHTMLToMarkdown(url)
    try:
        parser.feed(html)
    except Exception as e:
        log_error(f"Error parsing HTML of {url}: {e}")
        return "", []
        
    markdown_content = "".join(parser.markdown)
    # Clean up empty lines and formatting artifacts
    markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)
    
    return markdown_content, parser.links

def main():
    if len(sys.argv) < 2:
        print("Usage: scrape_docs.py <path_to_inflow_file>")
        sys.exit(1)
        
    inflow_file = sys.argv[1]
    if not os.path.exists(inflow_file):
        log_error(f"Inflow file not found: {inflow_file}")
        sys.exit(1)
        
    log_info(f"Processing inflow file: {inflow_file}")
    with open(inflow_file, "r", encoding="utf-8") as f:
        file_content = f.read()
        
    # Check if this file has already been scraped to avoid infinite loops
    if "## 🌐 Scraped Reference Content" in file_content:
        log_ok("File already contains scraped reference content. Skipping.")
        sys.exit(0)
        
    # Find all HTTP/HTTPS links
    urls = re.findall(r'https?://[^\s\)\>\]]+', file_content)
    # Clean trailing punctuation from URLs and deduplicate
    urls = sorted(list(set([u.rstrip('.,;:!?') for u in urls])))
    
    doc_urls = [u for u in urls if is_doc_url(u)]
    if not doc_urls:
        log_ok("No documentation URLs found to scrape.")
        sys.exit(0)
        
    log_info(f"Found {len(doc_urls)} documentation URL(s) to scrape: {doc_urls}")
    
    visited_urls = set()
    scraped_sections = []
    
    for main_url in doc_urls:
        log_info(f"Scraping main URL: {main_url}")
        content, discovered_links = scrape_and_format(main_url, visited_urls)
        
        if content:
            scraped_sections.append(f"### 📄 Source: [{main_url}]({main_url})\n\n{content}\n")
            
            # Find sublinks to traverse
            sublinks = extract_sublinks(main_url, discovered_links)
            # Filter out excluded/non-doc sublinks
            sublinks = [s for s in sublinks if is_doc_url(s)]
            
            if sublinks:
                # Limit sublink scraping to max 10 to avoid scraping too many pages
                max_sublinks = min(10, len(sublinks))
                log_info(f"Found {len(sublinks)} potential sublink(s). Scraping top {max_sublinks}...")
                
                for sublink in sublinks[:max_sublinks]:
                    log_info(f"Scraping sub-link: {sublink}")
                    sub_content, _ = scrape_and_format(sublink, visited_urls)
                    if sub_content:
                        scraped_sections.append(f"#### 📄 Sub-topic: [{sublink}]({sublink})\n\n{sub_content}\n")
                        
    if scraped_sections:
        divider = "\n\n---\n\n## 🌐 Scraped Reference Content\n\n"
        divider += "> [!NOTE]\n"
        divider += "> The content below has been automatically scraped from official documentation and related sub-links for deeper context.\n\n"
        
        appended_content = file_content + divider + "\n".join(scraped_sections)
        
        with open(inflow_file, "w", encoding="utf-8") as f:
            f.write(appended_content)
            
        log_ok(f"Successfully scraped content and appended it to {inflow_file}")
    else:
        log_warn("No content could be scraped from the documentation URLs.")

if __name__ == "__main__":
    main()
