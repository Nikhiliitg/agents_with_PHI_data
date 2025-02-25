import phi.api
from phi.model.groq import Groq
from phi.agent import Agent
from phi.tools.yfinance import YFinanceTools
from phi.tools.tavily import TavilyTools
import os
from phi.playground import Playground, serve_playground_app
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set API key
phi.api.key = os.getenv('PHI_API')

# Define Web Search Agent
web_search_agent = Agent(
    name="WebSearchAgent",
    role="Search the web for the latest information",
    model=Groq(id="llama-3.3-70b-versatile"),  # Fix: Use Groq("id") instead of Groq(id="id")
    markdown=True,
    tools=[TavilyTools(api_key=os.getenv("TAVILY_API_KEY"))],
    instructions=["Always include sources"],
    show_tool_calls=True,
)

# Define Finance Agent
finance_agent = Agent(
    name="Finance Agent",
    role="Gather financial data about companies",
    model=Groq(id="llama-3.3-70b-versatile"),  # Fix: Use Groq("id") instead of Groq(id="id")
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True
        ),
    ],
    instructions=["Use tables to display financial data"],
    show_tool_calls=True,
    markdown=True,
)

# Initialize Playground
app = Playground(agents=[web_search_agent, finance_agent]).get_app()

if __name__ == '__main__':
    serve_playground_app("exp:app" , reload=True)  # Fix: Pass the app object directly, not a string
