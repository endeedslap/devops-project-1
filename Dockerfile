# Start with a small Python computer
FROM python:3.11-slim

# Create a folder inside the container to put our app
WORKDIR /app

# Copy the requirements file and install packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all our code into the container
COPY . .

# Tell Docker our app uses port 5000
EXPOSE 5000

# The command to run when the container starts
CMD ["python", "app.py"]
