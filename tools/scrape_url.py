from bs4 import BeautifulSoup
from langchain.tools import tool
import requests
from rich import print

@tool
def scrape_url(url:str)->str:
    """Scrapes the content of a given URL, extract text and returns it."""

    try:
        headers={"User-Agent": "Mozilla/5.0"}

        response=requests.get(url,headers=headers,timeout=10)
        response.raise_for_status()

        soup=BeautifulSoup(response.content,"html.parser")

        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()

        text_content = soup.get_text()

        cleaned_text=text_content.strip()

        return cleaned_text

    except Exception as e:
        return f"Error scraping URL: {str(e)}" 

if __name__=='__main__':
    print(scrape_url.invoke("https://www.theguardian.com/world/2026/jun/15/brazil-rope-jump-bridge-woman-dies"))