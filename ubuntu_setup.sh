#!/bin/bash

echo "🚀 Setting up PDPBioGen on Ubuntu..."

# Update system
echo "📦 Updating system packages..."
sudo apt update

# Install system dependencies
echo "📦 Installing system dependencies..."
sudo apt install -y python3 python3-pip python3-venv graphviz

# Create and activate virtual environment
echo "🐍 Creating Python virtual environment..."
python3 -m venv pdpbiogen-env
source pdpbiogen-env/bin/activate

# Upgrade pip
echo "📦 Upgrading pip..."
pip install --upgrade pip

# Install PDPBioGen
echo "📦 Installing PDPBioGen..."
pip install -e .

# Test installation
echo "🧪 Testing installation..."
python3 -c "
import pdpbiogen
print('✅ PDPBioGen imported successfully')
print('Version:', pdpbiogen.__version__)
"

# Test Graphviz
echo "🧪 Testing Graphviz..."
python3 -c "
import graphviz
d = graphviz.Digraph()
d.node('test')
d.render('/tmp/test_output', format='png', cleanup=True)
print('✅ Graphviz working correctly')
"

echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "To activate the environment:"
echo "  source pdpbiogen-env/bin/activate"
echo ""
echo "To test PDPBioGen:"
echo "  pdpbiogen --help"
