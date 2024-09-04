#!/bin/bash

# This script is used to build all of the modules in SDXL Pipeline.
# It requires *quite a lot* of disk space - be warned!

# Change to the directory that this script is in.
cd "$(dirname "$0")"

# Load the configuration
source CONFIG.env

# Check if Docker username and password are provided as arguments
if [ $# -eq 2 ]; then
    DOCKER_USERNAME=$1
    DOCKER_PASSWORD=$2
fi

# Check that the required variables are set
if [[ -z $DOCKER_USERNAME || -z $DOCKER_PASSWORD || -z $IMAGE_NAME || -z $IMAGE_TAG ]]; then
    echo "Usage: $0 <DOCKER_USERNAME> <DOCKER_PASSWORD>"
    echo "Or set DOCKER_USERNAME, DOCKER_PASSWORD, IMAGE_NAME, and IMAGE_TAG in CONFIG.env before building."
    exit 1
fi

# Build the Docker containers for each model
echo "Building Docker containers..."

# Turn on Docker BuildKit and cd to the docker directory
cd ../docker/
export DOCKER_BUILDKIT=1

# Login to Docker Hub
echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin

# Generate a new tag
NEW_TAG=$(date +v%Y%m%d%H%M%S)

# Build the Docker image
docker build -f Dockerfile -t $DOCKER_USERNAME/$IMAGE_NAME:$IMAGE_TAG-$NEW_TAG .

# Publish the Docker containers
echo "Publishing Docker containers..."
docker push $DOCKER_USERNAME/$IMAGE_NAME:$IMAGE_TAG-$NEW_TAG

echo "Done!"