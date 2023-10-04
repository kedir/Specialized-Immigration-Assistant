# Use the official Python 3.10 image as the base image
FROM python:3.10.12

# Expose port 8501 for the Streamlit application
EXPOSE 8501

# Set the working directory inside the container
WORKDIR /app

# Update package information and install necessary packages
RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version
RUN pip install --no-cache-dir -U pip

# Copy the requirements.txt file to the container
COPY app/requirements.txt /app/

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -U -r requirements.txt

# Copy the contents of the app/ directory to the container
COPY app/ /app/

# Define the entry point for the Docker container (Streamlit)
ENTRYPOINT ["streamlit", "run"]

# Set the default command to run the Streamlit app with specified options
CMD ["main.py", "--browser.gatherUsageStats=false", "--global.disableWatchdogWarning=true"]
