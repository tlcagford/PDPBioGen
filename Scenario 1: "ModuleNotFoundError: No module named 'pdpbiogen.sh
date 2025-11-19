# Make sure you're in the right directory
ls -la setup.py

# Install in development mode
pip install -e .

# Or add current directory to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
