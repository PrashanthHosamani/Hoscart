# Start from an official Python image (slim = smaller size)
FROM python:3.13-slim

# Set environment variables
# Prevents Python from writing .pyc files (not needed in containers)
ENV PYTHONDONTWRITEBYTECODE=1
# Prevents Python from buffering stdout/stderr (logs appear in real time)
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
# All commands below will run from /app
WORKDIR /app

# Install system dependencies (needed to compile some Python packages)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (Docker caches this layer, speeds up rebuilds)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose port 8000 (where Gunicorn will listen)
# NOTE: We do NOT run collectstatic here because env vars (SECRET_KEY etc.)
# are not available at build time. It runs in docker-compose.yml at startup instead.
EXPOSE 8000

# Start the app using Gunicorn (production-grade server)
# - 3 worker processes to handle multiple requests at once
# - Listens on 0.0.0.0:8000 (all network interfaces inside the container)
CMD ["gunicorn", "hoscart.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
