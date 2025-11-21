# license_management.py
import datetime
from typing import Optional

class LicenseManager:
    def __init__(self):
        self.license_type = self.detect_license()
        
    def detect_license(self) -> str:
        """Auto-detect license context"""
        # Check environment variables
        if os.getenv('PDPBIOGEN_COMMERCIAL_LICENSE'):
            return "commercial"
            
        # Check for license file
        if os.path.exists('/etc/pdpbiogen/commercial.lic'):
            return "commercial"
            
        # Default to open source
        return "open_source"
    
    def validate_usage(self, feature: str) -> bool:
        """Validate license for specific feature"""
        if self.license_type == "commercial":
            return True
            
        # Open source restrictions
        restricted_features = {
            "large_scale_commercial", 
            "enterprise_integration",
            "premium_support"
        }
        
        return feature not in restricted_features
    
    def get_license_info(self) -> dict:
        """Return current license information"""
        return {
            "type": self.license_type,
            "version": "1.0.0",
            "validated": True,
            "features": self.get_available_features()
        }
