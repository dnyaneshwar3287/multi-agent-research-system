import os
import re
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from tavily import TavilyClient
from langchain_core.tools import tool

load_dotenv()

# ✅ API KEY CHECK
api_key = os.getenv("TAVILY_API_KEY")
if not api_key:
    raise ValueError("TAVILY_API_KEY is missing in .env")

tavily = TavilyClient(api_key=api_key)

# 🔍 SEARCH TOOL
@tool
def web_search(query: str) -> str:
    """Search the web using Tavily and return formatted results."""
    results = tavily.search(query=query, max_results=5)

    out = []
    for r in results["results"]:
        out.append(
            f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
        )

    return "\n----\n".join(out)

# 📖 SCRAPER TOOL
@tool
def scrape_url(input_text: str) -> str:
    """Extract URL from text and scrape content."""
    try:
        urls = re.findall(r'https?://\S+', input_text)

        if not urls:
            return "No valid URL found to scrape."

        url = urls[0]

        resp = requests.get(
            url,
            timeout=8,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        soup = BeautifulSoup(resp.text, "html.parser")

        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()

        return soup.get_text(separator=" ", strip=True)[:3000]

    except Exception as e:
        return f"Could not scrape URL: {str(e)}"