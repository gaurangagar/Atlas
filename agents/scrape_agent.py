import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from tools.scrape_url import scrape_url
from utils.llm import get_llm
from langchain.agents import create_agent

def build_reader_agent():
    return create_agent(
        model = llm,
        tools = [scrape_url]
    )