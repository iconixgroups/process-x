# Use the official Python image from Docker Hub as the base image
FROM python:3.8-slim

# Set environment variables to reduce output verbosity and prevent Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY backend/requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the Django project into the container
COPY backend /app

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Start the application server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.wsgi:application"]