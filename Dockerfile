# Use the official Python 3.12 image as base
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application code into the container
COPY . /app/

# Expose the port the application runs on
EXPOSE 8080

# Run the FastAPI application with uvicorn server
CMD ["uvicorn", "polls.app:app", "--host", "0.0.0.0", "--port", "8080"]
