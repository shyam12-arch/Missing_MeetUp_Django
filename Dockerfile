FROM python:3.9  # Or use the Python version you're working with

WORKDIR /app  # Set the working directory

COPY requirements.txt .  # Copy requirements.txt into the container

RUN pip install --no-cache-dir -r requirements.txt  # Install dependencies

COPY . .  # Copy the rest of your Django project into the container

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]  # Start Django




# Use an official Python runtime as a parent image
#FROM python:3.9-slim

# Set the working directory in the container
#WORKDIR /app

# Copy the contents of the src directory into the container
#COPY . .

#RUN pip install --no-cache-dir -r requirments.txt  # Install dependencies

# Set the default command to execute the app
#CMD ["python", "manage.py", "runserver"]


