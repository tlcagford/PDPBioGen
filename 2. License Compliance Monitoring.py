# compliance/monitoring.py
class LicenseCompliance:
    def scan_dependencies(self):
        """Ensure all dependencies are license-compatible"""
        opensource_deps = self.check_osi_approved()
        commercial_deps = self.check_commercial_friendly()
        
        return {
            "opensource_safe": opensource_deps,
            "commercial_safe": commercial_deps
        }
    
    def audit_usage(self):
        """Monitor for license violations"""
        self.check_public_repos_for_violations()
        self.monitor_commercial_usage()
