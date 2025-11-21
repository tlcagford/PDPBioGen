# FINAL VERIFICATION: Clean environment install
python -m venv test_env
source test_env/bin/activate
pip install pdpbiogen
python -c "import pdpbiogen; print('✅ SUCCESS')"
