# analytics/usage_tracking.py
import uuid
import platform
from datetime import datetime

class UsageTracker:
    def __init__(self):
        self.session_id = str(uuid.uuid4())
        self.license_manager = LicenseManager()
    
    def track_feature_usage(self, feature_name: str):
        """Anonymous usage tracking for both licenses"""
        data = {
            "session_id": self.session_id,
            "feature": feature_name,
            "timestamp": datetime.utcnow().isoformat(),
            "license_type": self.license_manager.license_type,
            "platform": platform.platform(),
            "version": "1.0.0"
        }
        
        # Send to analytics endpoint (commercial only)
        if self.license_manager.license_type == "commercial":
            self._send_to_commercial_endpoint(data)
        else:
            self._send_to_opensource_endpoint(data)
