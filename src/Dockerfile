# Use the official Python image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the local code to the container
COPY . .

# Install FastAPI and Uvicorn and joblib
RUN pip install fastapi uvicorn joblib numpy scikit-learn flask gunicorn

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
