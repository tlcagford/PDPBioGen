# Testing imports - FIXED VERSION
# pdpbiogen/__init__.py
"""PDPBioGen - Programmatic Diagram Pathway Biologist Generator."""

__version__ = "0.1.0"
__author__ = "tlcagford"

# Import only after defining to avoid circular imports
from .exceptions import PDPBioGenError

__all__ = ["PDPBioGenError", "__version__"]
