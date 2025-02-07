# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the contents of the src directory into the container
COPY . .

# Set the default command to execute the app
CMD ["python", "manage.py", "runserver"]


