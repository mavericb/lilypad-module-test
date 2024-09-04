# Use NVIDIA CUDA base image
FROM nvidia/cuda:11.8.0-devel-ubuntu22.04 AS builder

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update -y && \
    apt-get install -y curl python3 python3-pip git libgl1-mesa-glx libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Download image at build time
RUN curl -o /app/image.jpg https://fastly.picsum.photos/id/866/200/300.jpg?hmac=rcadCENKh4rD6MAp6V_ma-AyWv641M4iiOpe1RyFHeI

# Copy application files
COPY Dockerfile /app/Dockerfile
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt
COPY start.sh /app/start.sh

RUN ls -la /app

# Make start.sh executable
RUN chmod +x /app/start.sh

# Set the entrypoint #
ENTRYPOINT ["/app/start.sh"]