git clone https://github.com/tlcagford/PDPBioGen
cd PDPBioGen
python -m venv pdp_env
source pdp_env/bin/activate  # Windows: pdp_env\Scripts\activate
pip install -e ".[dev]"
pytest tests/ -v