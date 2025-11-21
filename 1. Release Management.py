# scripts/release_management.py
class DualLicenseReleaseManager:
    def create_releases(self, version: str):
        """Create both open source and commercial releases"""
        
        # 1. Build open source package
        self.build_opensource_package(version)
        
        # 2. Build commercial package  
        self.build_commercial_package(version)
        
        # 3. Upload to respective repositories
        self.upload_opensource_to_pypi(version)
        self.upload_commercial_to_private_repo(version)
    
    def update_license_files(self):
        """Keep license files synchronized"""
        self.ensure_consistent_copyright()
        self.update_contributor_list()
