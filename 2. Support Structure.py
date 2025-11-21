class SupportTier:
    def __init__(self, license_type):
        self.license_type = license_type
        
    def get_support_level(self):
        return {
            "opensource": {
                "response_time": "7 business days",
                "channels": ["github_issues", "community_forum"],
                "scope": "bug_fixes_only"
            },
            "commercial": {
                "response_time": "2 business hours", 
                "channels": ["email", "phone", "dedicated_slack"],
                "scope": "full_support_including_feature_requests"
            }
        }[self.license_type]
