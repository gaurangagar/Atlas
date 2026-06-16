from langchain.tools import tool

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils.tavily_client import get_tavily_client
from rich import print

tavily=get_tavily_client()

@tool
def web_search(query:str)->str:
    """Performs a web search to find recent and credible information, returning result titles, URLs, and snippets."""
    results=tavily.search(query=query,max_results=5)
    
    final=[]

    for result in  results["results"]:
        final.append(f"Title: {result['title']}\nURL: {result['url']}\nSnippet: {result['content'][:300]}\n")

    return "\n----\n".join(final)

if __name__=='__main__':
    print(web_search.invoke("Who is Elon Musk?"))