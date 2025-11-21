# 1. Clone and setup (2 minutes)
git clone https://github.com/tlcagford/PDPBioGen
cd PDPBioGen
pip install poetry
poetry install

# 2. Verify installation
poetry run python -m pdpbiogen --help
# Output: CLI help with available commands