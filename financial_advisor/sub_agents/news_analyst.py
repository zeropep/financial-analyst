import yfinance as yf
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


MODEL = LiteLlm(model="openai/gpt-4o")


def get_company_news(ticker: str):
    """
    Retrieves recent news articles for the given ticker using yfinance.

    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL', 'GOOGL').

    Returns:
        dict: A dictionary containing:
            - ticker (str): The input ticker symbol
            - success (bool): True if the operation was successful
            - news (list[dict]): A list of news items as returned by yfinance.Ticker.get_news()
    """
    stock = yf.Ticker(ticker)
    news_items = stock.get_news() or []
    return {
        "ticker": ticker,
        "success": True,
        "news": news_items,
    }


news_analyst = Agent(
    name="NewsAnalyst",
    model=MODEL,
    description="Fetches recent company news via yfinance for up-to-date market information.",
    instruction="""
    You are a News Analyst Specialist who uses web tools to find current information. Your job:
    
    1. **Company News**: Use get_company_news(ticker) to fetch recent news about a company.
    2. **Summarize Findings**: Explain what you found and its relevance
    
    **Your Web Tools:**
    - **get_company_news(ticker)**: Retrieve recent news via yfinance.Ticker.get_news()
    
    Use external APIs to search and scrape web content for current information.
    """,
    tools=[
        get_company_news,
    ],
)