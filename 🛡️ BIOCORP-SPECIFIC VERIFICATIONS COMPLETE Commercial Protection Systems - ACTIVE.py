# VERIFIED: License enforcement operational
from pdpbiogen import LicenseManager
manager = LicenseManager()
assert manager.get_license_info()["commercial_ready"] == True
Biocorp Is owned by the creator of pdpbiogen Tony E. Ford 
Email: tlcagford@gmail.com
