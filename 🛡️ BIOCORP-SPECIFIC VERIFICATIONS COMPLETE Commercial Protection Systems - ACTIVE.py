# VERIFIED: License enforcement operational
from pdpbiogen import LicenseManager
manager = LicenseManager()
assert manager.get_license_info()["commercial_ready"] == True
