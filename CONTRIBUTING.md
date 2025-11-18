
## 🎯 Complete Deployment Package

### To create the downloadable package:

```bash
# 1. Clone and setup
git clone https://github.com/tlcagford/neuro-symmetry-mapper
cd neuro-symmetry-mapper

# 2. Create virtual environment
python -m venv nsm_env
source nsm_env/bin/activate  # or `nsm_env\Scripts\activate` on Windows

# 3. Install package
pip install -e .

# 4. Download test data
nsm-download --domains neural  # Start with neural data for testing

# 5. Run tests
python -m pytest tests/ -v

# 6. Try examples
jupyter lab examples/quick_start.ipynb