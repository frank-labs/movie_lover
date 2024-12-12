# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install system dependencies and PostgreSQL client libraries
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && apt-get clean

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Collect static files (output will be shared via volume mount)
RUN python manage.py collectstatic --noinput

# Expose the port your app will run on
EXPOSE 8000

# Command to start the Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "movie_lover.wsgi:application"]
