# 1. Check basic structure
ls -la PDPBioGen/
tree PDPBioGen/  # if you have tree installed

# 2. Test key files exist
ls -la pdpbiogen.nf environment.yml Dockerfile LICENSE README.md

# 3. Check script permissions
ls -la scripts/
chmod +x scripts/*.py  # ensure executable

# 4. Test environment creation
conda env create -f environment.yml --dry-run

# 5. Test Nextflow syntax
nextflow check pdpbiogen.nf

# 6. Verify license headers
head -5 pdpbiogen.nf scripts/*.py | grep -i "copyright\|2025"
