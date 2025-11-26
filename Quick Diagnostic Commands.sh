# 1. Test everything locally first
pytest tests/ -v

# 2. Check requirements installation
pip install -r requirements.txt

# 3. Verify examples work
python examples/basic_usage.py

# 4. Check code quality
pip install black flake8
black --check .
flake8 .
