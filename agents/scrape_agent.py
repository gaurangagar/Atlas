from tools.scrape_url import scrape_url
from langchain.agents import create_agent

def build_reader_agent(llm):
    return create_agent(
        model = llm,
        tools = [scrape_url]
    )