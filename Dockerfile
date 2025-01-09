FROM python:3.12.2-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8000

# Copy the whole project
COPY . .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install wheel
RUN pip install --no-cache-dir -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

# Create a script to initialize the media directory if it doesn't exist
RUN echo '#!/bin/sh\n\
if [ ! -d "/app/media" ]; then\n\
    mkdir -p /app/media/images\n\
    chmod -R 777 /app/media\n\
fi\n\
exec gunicorn Theranostics.wsgi:application --bind 0.0.0.0:$PORT' > /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

# Use the entrypoint script
CMD ["/app/entrypoint.sh"]