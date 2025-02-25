import io
import sys
import streamlit as st
from phi.agent import Agent 
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.tavily import TavilyTools
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define Web Search Agent
web_search_agent = Agent(
    name="WebSearchAgent",
    role="Search the web for the latest information",
    model=Groq(id="llama-3.3-70b-versatile"),
    markdown=True,
    tools=[TavilyTools(api_key=os.getenv("TAVILY_API_KEY"))],
    instructions=["Always include sources"],
    show_tool_calls=True,
)

# Define Finance Agent
finance_agent = Agent(
    name="FinanceAgent",
    role="Gather financial data about companies",
    model=Groq(id="llama-3.3-70b-versatile"),
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

# Define Multi-Agent System
multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Always include sources", "Use tables to display financial data"],
    show_tool_calls=True,
    markdown=True,
)

# Streamlit UI
st.title("Multi-Agent AI for Finance & Web Search")

# User input
user_query = st.text_area("Enter your query:")

if st.button("Get Response"):
    with st.spinner("Fetching data..."):
        response = multi_ai_agent.run(user_query)  # Returns a clean text response
        st.markdown(response, unsafe_allow_html=True)  # Display the response in Streamlit
