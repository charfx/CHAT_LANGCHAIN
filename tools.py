import os
from typing import Any, Dict

from dotenv import load_dotenv
from langchain.tools import tool
from tavily import TavilyClient

load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")
if not api_key:
    raise ValueError("TAVILY_API_KEY is not set. Add it to your .env file.")

client = TavilyClient(api_key=api_key)


@tool
def web_search(query: str) -> Dict[str, Any]:
    """Search the web for information related to the query."""
    print(f"We are doing a search for: {query}")
    return client.search(query=query, max_results=5)


if __name__ == "__main__":
    result = web_search.invoke({"query": "latest bitcoin news today and resume it into one sentence "})
    print(result)

