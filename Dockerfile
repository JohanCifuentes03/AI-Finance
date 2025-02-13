# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY app/ app/
COPY .env .

# Expose the port Gradio will run on
EXPOSE 7860

# Run the application
CMD ["python", "app/app.py"]