# Replace the old files with these new ones
# Then test:

pip install -r requirements.txt

# Test basic functionality
python pdpbiogen.py examples/example.fasta

# Test all enhanced features
python test_enhanced.py

# Test command line
python pdpbiogen.py examples/example.fasta --static test_output --min-length 20 --width 1200