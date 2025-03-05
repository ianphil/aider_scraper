# Aider Documentation Scraper

This project is designed to scrape and convert the documentation pages from the Aider website into Markdown files. It fetches the sitemap, extracts URLs for documentation pages, scrapes the content of these pages, and converts the HTML content to Markdown format.

## What This Project Does

- Fetches the sitemap from `https://aider.chat/sitemap.xml`.
- Extracts URLs specifically for documentation pages (`https://aider.chat/docs/`).
- Scrapes the content of each documentation page using the CSS selector `main`.
- Converts the scraped HTML content to Markdown.
- Saves the Markdown files in the `aider_docs` directory.

## How to Run the Project

1. Ensure you have Python installed on your system.
2. Install the required libraries by running:
   ```
   pip install requests beautifulsoup4 html2text
   ```
3. Run the script:
   ```
   python main.py
   ```
4. The script will process the documentation pages and save them as Markdown files in the `aider_docs` directory.

After running the script, you will find all the processed documentation pages in Markdown format in the `aider_docs` directory.

## Development Environment

This project was created in Visual Studio Code using Aider and Grok.

- [Visual Studio Code](https://code.visualstudio.com/)
- [Aider](https://aider.chat/)
- [Grok](https://x.ai/)
