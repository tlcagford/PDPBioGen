# If you see "command not found" for pdpbiogen:
source venv/bin/activate  # reactivate virtual environment
hash -r                   # clear command cache
pdpbiogen --help

# If you see Graphviz errors:
sudo apt install -y graphviz
export PATH="/usr/bin:/usr/local/bin:$PATH"

# If you see Python path issues:
export PYTHONPATH="$(pwd):$PYTHONPATH"

# If pip install fails:
pip install --upgrade pip setuptools wheel
