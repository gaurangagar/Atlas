from tools.web_search import web_search
from langchain.agents import create_agent

def build_search_agent(llm):
    return create_agent(
        model = llm,
        tools= [web_search]
    )