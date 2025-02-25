from phi.agent import Agent 
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.tavily import TavilyTools
import os
from dotenv import load_dotenv
load_dotenv()

## Websearch agent
web_search_agent = Agent(
    name="WebSearchAgent",
    role="Search the web for the latest information",
    model=Groq(id="llama-3.3-70b-versatile"),
    markdown=True,
    tools=[TavilyTools(api_key=os.getenv("TAVILY_API_KEY"))],
    instructions=["Always include sources"],
    show_tool_calls=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Gather financial data about the companies",
    model=Groq(id="llama-3.3-70b-versatile"),  # Fix: Use class instead of instance
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True),
    ],
    instructions=["Use tables to display financial data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    model= Groq(id="llama-3.3-70b-versatile"),
    instructions=["Always include sources", "Use tables to display financial data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news of Deepseek", stream=True)
multi_ai_agent.run("Summarize analyst recommendation and share the latest news of Deepseek", stream=True)

