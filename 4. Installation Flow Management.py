# setup.py with dual license handling
from setuptools import setup
import os

def get_license_files():
    """Include both license files in distribution"""
    return ['LICENSE-OSL.md', 'LICENSE-COMMERCIAL.md']

def commercial_available():
    """Check if commercial version can be installed"""
    try:
        import pdpbiogen_commercial
        return True
    except ImportError:
        return False

setup(
    name="pdpbiogen",
    license="Dual: OSL or Commercial",
    # ... other configuration
)
