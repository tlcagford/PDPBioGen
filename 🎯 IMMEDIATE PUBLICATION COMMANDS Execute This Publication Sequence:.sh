# 1. FINAL PRE-PUBLICATION CHECKS
python -m pytest tests/ -v --tb=short
python scripts/security_scan.py
python scripts/license_validation.py

# 2. BUILD DISTRIBUTION PACKAGES
python -m build
twine check dist/*

# 3. PUBLISH TO PyPI (Open Source)
twine upload dist/pdpbiogen-1.0.0*

# 4. PUBLISH COMMERCIAL PACKAGE (Private)
twine upload --repository-url https://pypi.biocorp.com dist/pdpbiogen-commercial-1.0.0*

# 5. CREATE GITHUB RELEASE
git tag v1.0.0
git push origin v1.0.0
