# Choose the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the image
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port 5000 to the outside world
EXPOSE 5000

# Run the application when the container starts
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
