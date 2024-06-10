# Use the official Ubuntu image from the Docker Hub
FROM ubuntu:20.04

# Set the working directory in the container
WORKDIR /app

# Install dependencies and Python 3.12
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.12 python3.12-distutils python3.12-venv wget && \
    wget https://bootstrap.pypa.io/get-pip.py -O get-pip.py && \
    python3.12 get-pip.py && \
    rm get-pip.py

# Create a symlink for python3 and pip3
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 1 && \
    update-alternatives --install /usr/bin/pip3 pip3 /usr/local/bin/pip3.12 1

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip3 install -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run the application
CMD ["python3", "app.py"]
