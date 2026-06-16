import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

def get_tavily_client():
    try:
        tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        return tavily_client
    except ImportError as e:
        raise ImportError(
            "tavily-python is not installed. Run: pip install tavily-python"
        ) from e
    except Exception as e:
        raise RuntimeError(f"Failed to initialize Tavily client: {e}") from e