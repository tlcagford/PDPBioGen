# 1. Clone
git clone https://github.com/tlcagford/PDPBioGen.git
cd PDPBioGen

# 2. Create venv and activate
python3 -m venv .venv
source .venv/bin/activate

# 3. Upgrade pip & install build tools
python -m pip install --upgrade pip setuptools wheel

# 4. Install requirements
# If requirements.txt pins versions:
pip install -r requirements.txt

# 5. Install package in editable mode so imports like `import pdpbiogen` work
pip install -e .

# 6. (If your tests need graphviz) Install system package:
# Debian/Ubuntu:
sudo apt-get update && sudo apt-get install -y graphviz

# 7. Run tests with pytest
pytest -q
