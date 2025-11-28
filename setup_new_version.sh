#!/bin/bash

echo "Setting up PDPBioGen 2025 Dual-Licensed Version"
echo "Copyright (c) 2025 Tony Eugene Ford"
echo "================================================"

# Create directory structure
mkdir -p PDPBioGen/{scripts,docs,examples,bin,tests/test_data,.github}

# Copy all the file contents I provided above into their respective files
# (You'll need to manually create each file with the content I provided)

echo "Directory structure created."
echo "Now manually create each file with the provided content."
echo "Then run:"
echo "cd PDPBioGen"
echo "chmod +x scripts/*.py bin/*.sh"
echo "conda env create -f environment.yml"
echo "nextflow run pdpbiogen.nf --help"
