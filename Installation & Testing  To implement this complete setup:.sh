# 1. Create the new directory structure
mkdir -p pdpbiogen tests docs

# 2. Install in development mode
pip install -e .[dev]

# 3. Run tests
pytest tests/ -v

# 4. Check code quality
black pdpbiogen/ tests/
flake8 pdpbiogen/ tests/
mypy pdpbiogen/

# 5. Test the CLI
pdpbiogen --help
pdpbiogen example.yaml test_output
