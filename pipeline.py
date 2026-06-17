from chain.writer_chain import get_writer_chain
from chain.critic_chain import get_critic_chain
from agents.search_agent import build_search_agent
from agents.scrape_agent import build_reader_agent

from utils.llm import get_google_llm
from rich import print

def run_research_pipeline(topic:str)->dict:

    print("\nStarting research pipeline")
    print(f"Topic: {topic}\n")

    llm =get_google_llm()
    state={}

    print("Step 1: Building search agent")
    search_agent=build_search_agent(llm)

    print("Step 2: Searching web")
    search_result = search_agent.invoke({
        "messages" : [("user", f"Find recent, reliable and detailed information about: {topic}")]
    })

    state["search_results"] = search_result['messages'][-1].content

    print("Search completed")
    print("\n search result ",state['search_results'])
    print(f"Search results length: {len(state['search_results'])}")

    print("Step 3: Building reader agent")
    reader_agent = build_reader_agent(llm)

    print("Step 4: Scraping detailed content")
    reader_result = reader_agent.invoke({
        "messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_results'][:800]}"
        )]
    })

    state['scraped_content'] = reader_result['messages'][-1].content

    print("Scraping completed")
    print("\nscraped content: \n", state['scraped_content'])
    print(f"Scraped content length: {len(state['scraped_content'])}")

    print("Step 5: Combining research")

    research_combined = (
        f"SEARCH RESULTS : \n {state['search_results']} \n\n"
        f"DETAILED SCRAPED CONTENT : \n {state['scraped_content']}"
    )

    print("Step 6: Generating report")

    state["report"] = get_writer_chain(llm).invoke({
        "topic" : topic,
        "research" : research_combined
    })

    print("Report generated")
    print("\n Final Report\n",state['report'])
    print(f"Report length: {len(state['report'])}")

    print("Step 7: Reviewing report")

    state["feedback"] = get_critic_chain(llm).invoke({
        "report":state['report']
    })

    print("Review completed")
    print(f"Feedback length: {len(state['feedback'])}")

    print("\n critic report \n", state['feedback'])

    print("Pipeline completed successfully")

    return state


if __name__=='__main__' :
    topic = input("\n Enter a research topic : ")
    run_research_pipeline(topic)
