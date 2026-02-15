# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Install system dependencies for D-Bus and notifications
RUN apt-get update && apt-get install -y \
    libglib2.0-bin \
    dbus \
    libnotify-bin \
    && rm -rf /var/lib/apt/lists/*

# Generate a machine-id (required for D-Bus)
# This is often needed for D-Bus based libraries like plyer to function in a container
RUN dbus-uuidgen > /etc/machine-id

# Set the working directory in the container
WORKDIR /app

RUN pip install plyer

# Copy the current directory contents into the container at /app
COPY . .

# Run app.py when the container launches
CMD ["python", "app.py"]
