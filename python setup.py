# Build for PyPI
python setup.py sdist bdist_wheel

# Upload to PyPI (after configuring credentials)
twine upload dist/*

# Or create GitHub release
git tag v0.1.0
git push origin v0.1.0