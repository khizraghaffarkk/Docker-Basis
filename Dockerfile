# Use the official Python image as the base image;python 3.8
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /toyota-data-feeder

# Copy only necessary files
COPY feeder.py requirements.txt ca.crt toyota_data.csv /toyota-data-feeder/

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Define the default running command to run your application
CMD ["python", "feeder.py"]