# compliance/contribution_tracker.py
class BiocorpCLATracker:
    def __init__(self):
        self.signed_contributors = self.load_signed_clas()
        
    def enforce_contribution_policy(self, username, contribution_size):
        """Different rules based on contribution size"""
        
        if contribution_size == "trivial":  # typo fixes
            return self.fast_track_trivial_contribution(username)
            
        elif contribution_size == "substantial":  # new features
            return self.require_full_cla_review(username)
            
    def audit_contributions(self):
        """Regular audits to ensure compliance"""
        all_contributors = self.get_all_contributors()
        unsigned = set(all_contributors) - set(self.signed_contributors)
        
        if unsigned:
            self.legal_team.review_unsigned_contributions(unsigned)
