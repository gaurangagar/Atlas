import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from tools.web_search import web_search
from utils.llm import get_llm
from langchain.agents import create_agent

def build_search_agent():
    return create_agent(
        model = llm,
        tools= [web_search]
    )