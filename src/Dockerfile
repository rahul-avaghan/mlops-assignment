# Use the official Python image
#FROM python:3.9

# Set the working directory in the container
#WORKDIR /app

# Copy the local code to the container
#COPY . .

# Install FastAPI and Uvicorn and joblib
#RUN pip install fastapi uvicorn joblib numpy scikit-learn flask gunicorn

# Expose the port the app runs on
#EXPOSE 8000

# Command to run the application
#CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]

#new code
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]

