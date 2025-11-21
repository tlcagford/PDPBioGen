# core/__init__.py
from .license_management import LicenseManager

_license_manager = LicenseManager()

def check_commercial_features():
    """Decorator for commercial-only features"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not _license_manager.validate_usage("commercial_features"):
                raise LicenseError(
                    "This feature requires a commercial license. "
                    "Visit https://biocorp.com/pdpbiogen for licensing."
                )
            return func(*args, **kwargs)
        return wrapper
    return decorator

class LicenseError(Exception):
    """Custom exception for license violations"""
    pass
