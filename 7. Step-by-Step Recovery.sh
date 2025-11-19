# 1. Start fresh
cd /tmp
git clone https://github.com/tlcagford/PDPBioGen
cd PDPBioGen

# 2. Set up clean environment
python3 -m venv pdpbiogen-venv
source pdpbiogen-venv/bin/activate

# 3. Install system dependencies
sudo apt update
sudo apt install -y graphviz

# 4. Install Python package
pip install -e .

# 5. Run minimal test
python3 -c "
import pdpbiogen
print('Success! Version:', pdpbiogen.__version__)
"

# 6. Test CLI
pdpbiogen --help
