# Use an official Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the local directory to the container
COPY . .

# Upgrade pip and install required dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir streamlit

# Ensure Streamlit is in PATH
RUN echo "Checking Streamlit version..." && streamlit --version

# Expose the port used by Streamlit
EXPOSE 8501

# Run the Streamlit app
ENV PATH="/usr/local/bin:$PATH"
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]

