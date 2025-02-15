import requests
from bs4 import BeautifulSoup
import markdownify

# Base URL
BASE_URL = "https://www.quantconnect.com/docs/v2"

# List of main documentation categories
doc_sections = [
    "cloud-platform",
    "local-platform",
    "writing-algorithms",
    "research",
    "lean-cli",
    "lean-engine"
]

# Generate full URLs for each section
doc_links = [f"{BASE_URL}/{section}" for section in doc_sections]

def extract_page_content(url):
    """Fetch page content and convert it to Markdown format"""
    res = requests.get(url)
    if res.status_code != 200:
        print(f"Failed to fetch {url}")
        return None

    page_soup = BeautifulSoup(res.text, 'html.parser')

    # Try different divs where content might be stored
    content_div = (page_soup.find("div", {"class": "docs-content"}) or 
                   page_soup.find("div", {"class": "container"}) or
                   page_soup.find("div", {"class": "content"}))

    if content_div:
        markdown_content = markdownify.markdownify(str(content_div), heading_style="ATX")
        return markdown_content.strip()  # Remove empty spaces
    else:
        print(f"Warning: No content found for {url}")
    
    return None

# Extract and save documentation content
all_docs = {}
for link in doc_links:
    content = extract_page_content(link)
    if content:
        all_docs[link] = content

# Save to a Markdown file
with open("QuantConnect_All_Docs.md", "w", encoding="utf-8") as f:
    for link, content in all_docs.items():
        f.write(f"# {link}\n\n{content}\n\n")

print("✅ Saved extracted documentation to QuantConnect_All_Docs.md")
