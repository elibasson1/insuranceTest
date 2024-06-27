FROM ubuntu:22.04
# Set the working directory in the container
WORKDIR /app

# Update package lists and install necessary packages
RUN apt-get update && apt-get install -y python3 python3-pip

# Copy requirements.txt and install dependencies
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt