# 1. Check Python version
python3 --version

# 2. Check pip version
pip3 --version

# 3. Check Graphviz installation
which dot
dot -V

# 4. Check current directory structure
ls -la

# 5. Try installing in development mode
pip install -e . --verbose

# 6. Test basic Python functionality
python3 -c "import sys; print('Python path:', sys.path)"
