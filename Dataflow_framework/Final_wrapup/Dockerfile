# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app/main.py", "--watch"]

# Use Python 3.9 as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Expose the port FastAPI will run on
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000"]

#Build Docker image: docker build -t file-processing-system .

#Run container: docker run -d -p 8000:8000 file-processing-system