import requests
from bs4 import BeautifulSoup
import html2text
import os
import time
from xml.etree import ElementTree as ET

# Configuration
output_dir = "aider_docs"  # Directory to save Markdown files
os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}  # Mimic a browser

content_selector = "main"  # CSS selector for main content (adjust if needed)

# Step 1: Fetch the sitemap
sitemap_url = "https://aider.chat/sitemap.xml"
response = requests.get(sitemap_url, headers=headers)
response.raise_for_status()  # Raise an error if the request fails

# Step 2: Parse the XML and extract URLs
root = ET.fromstring(response.content)
urls = [loc.text for loc in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]

# Step 3: Filter for documentation URLs
doc_urls = [url for url in urls if url.startswith("https://aider.chat/docs/")]

# Step 4: Set up html2text converter
h = html2text.HTML2Text()
h.ignore_links = False  # Preserve links in Markdown
h.ignore_images = False
h.ignore_tables = False

# Step 5: Scrape and convert each page
for url in doc_urls:
    try:
        # Fetch the page
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract main content
        content = soup.select_one(content_selector)
        if not content:
            print(f"Warning: No content found for {url} with selector '{content_selector}'")
            continue

        # Convert to Markdown
        markdown = h.handle(str(content))

        # Generate filename
        relative_path = url.replace("https://aider.chat/docs/", "")
        if relative_path.endswith(".html"):
            relative_path = relative_path[:-5]  # Remove .html
        filename = relative_path.replace("/", "_") + ".md"
        output_path = os.path.join(output_dir, filename)

        # Save to file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown)
        print(f"Saved {url} to {output_path}")

        # Delay to be polite
        time.sleep(1)

    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
    except Exception as e:
        print(f"Error processing {url}: {e}")

print("Scraping complete! All documentation pages have been processed.")