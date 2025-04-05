# 🧠 Multi-Agent AI System with Finance & Web Search

A Streamlit-powered app demonstrating a multi-agent AI system using the `phi` framework, integrating real-time **financial analysis** and **web search** with Groq's LLaMA 3 model.

## 🚀 Features

- 📈 **Finance Agent**  
  Fetches:
  - Stock prices
  - Analyst recommendations
  - Company fundamentals
  - Company news  
  → Displays results in structured tables

- 🌐 **Web Search Agent**  
  - Uses Tavily to search the latest web info
  - Includes verified source links

- 🤖 **Multi-Agent System**  
  - A top-level agent intelligently delegates to both Finance & Web agents
  - Unified, readable markdown output with tool traces

- 🖥️ **Streamlit Interface**  
  - Clean and interactive UI
  - Input any company name or stock symbol
  - Live output rendering with markdown and tables

---

## 🛠️ Tech Stack

- `phi` – Agent framework
- `Groq` – LLaMA 3.3 70B model
- `yfinance` – Financial data
- `Tavily` – Real-time web search
- `Streamlit` – UI/Frontend
- `dotenv` – Secret key management

---

## 📦 Installation

```bash
https://github.com/Nikhiliitg/agents_with_PHI_data
cd agents_with_PHI_data
pip install -r requirements.txt
```
-----

## You will need a Tavily Account(API KEY) for searching in websites .

TAVILY_API_KEY=your_tavily_api_key
-------

## Run the app :
**streamlit run app.py

----


### 👤 Author

Nikhil Deka
📍 IITG | 💻 Data Science | 🧠 Passionpreneur











