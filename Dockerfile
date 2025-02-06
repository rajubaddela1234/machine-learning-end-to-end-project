<<<<<<< HEAD
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["python", "app.py"]
=======
FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python app.py
>>>>>>> 1184c8f6d16cf3aac3a98ee781687df5f9df9aaa
