from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def get_critic_chain(llm):

    writer_prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a sharp and constructive research critic. Be honest and specific."
        ),
        (
            "human",
            """Review the research report below and evaluate it strictly.

            Report:
            {report}

            Respond in this exact format:

            Score: X/10

            Strengths:
            - ...
            - ...

            Areas to Improve:
            - ...
            - ...

            One line verdict:
            ..."""
                    ),
                ])

    return writer_prompt | llm | StrOutputParser()