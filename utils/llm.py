import os
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI

def get_groq_llm():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")

    return ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=api_key,
        temperature=0
    )

def get_google_llm():
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables")

    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        api_key=api_key,
        temperature=0
    )