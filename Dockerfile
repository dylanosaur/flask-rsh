# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app files into the container
COPY app.py .

# Expose the desired port
EXPOSE 5000

# Set the entry point command to run the Flask app
CMD ["python3", "app.py"]
