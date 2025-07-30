#Dockerfile
# Official python runtime (using a slim version)
FROM python:3.12-slim-bookworm 

# Set env variables (stops pythng from write .pyc files and prevents python stdout/stderr buffering)
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1

# Create and set image working directory
WORKDIR /app


# install system deps 
RUN apt-get update && apt-get install -y --no-install-recommends postgresql-client && rm -rf /var/lib/apt/lists/*

# install python deps
# upgrade pip
RUN pip install --upgrade pip
# copy only requirements to leverage docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy project code into image directory
COPY . .

# makee wait-for-it.sh executable
RUN chmod +x wait-for-it.sh

# Expose port for app run
EXPOSE 8000

# Define the command to run app using gunicorn
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]