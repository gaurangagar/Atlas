from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def get_writer_chain(llm):

    writer_prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are an expert research writer. Write clear, structured and insightful reports."
        ),
        (
            "human",
            """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""
        ),
    ])

    return writer_prompt | llm | StrOutputParser()