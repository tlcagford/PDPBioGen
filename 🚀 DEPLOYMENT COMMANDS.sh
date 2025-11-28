# 1. Create all directories
mkdir -p validation/{results,benchmarks,datasets} examples test

# 2. Create all the files above (copy-paste the content)

# 3. Make test executable
chmod +x test/test_validation.py

# 4. Run validation tests
python test/test_validation.py

# 5. Add to git
git add validation/ examples/ test/
git commit -m "Add comprehensive validation data and test suite"
git push origin main
