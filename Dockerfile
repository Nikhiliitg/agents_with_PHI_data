# Use an official Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the local directory to the container
COPY . .

# Install all required dependencies
RUN pip install --no-cache-dir \
    streamlit \
    phi \
    phi-agent \
    phi-model-groq \
    phi-tools-yfinance \
    phi-tools-tavily \
    python-dotenv \
    io \
    sys \
    os

# Expose the port used by Streamlit
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
