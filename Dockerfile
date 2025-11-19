FROM ubuntu:22.04

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    graphviz \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install PDPBioGen
RUN pip3 install -e .

# Test installation
RUN python3 -c "import pdpbiogen; print('PDPBioGen imported successfully')"

# Set entrypoint
ENTRYPOINT ["pdpbiogen"]
