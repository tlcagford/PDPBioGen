# src/pdpbiogen/llm_verified_critic/biological_critic.py

class BiologicalCritic:
    """
    Adapted from llm-verified-critic for biological verification
    """
    
    def __init__(self, strict_mode: bool = True):
        self.strict_mode = strict_mode
        self.plausibility_checker = BiologicalPlausibilityChecker()
        self.constraint_solver = BiologicalConstraintSolver()
        
    def verify_biological_plausibility(self, proposal: Dict[str, Any]) -> Dict[str, Any]:
        """Verify biological plausibility of any proposal"""
        violations = []
        corrections = {}
        
        # Check energy conservation
        if not self.plausibility_checker.check_energy_conservation(proposal):
            violations.append("Energy conservation violation")
            corrections.update(
                self.constraint_solver.correct_energy_violation(proposal)
            )
        
        # Check mass balance
        if not self.plausibility_checker.check_mass_balance(proposal):
            violations.append("Mass balance violation")
            corrections.update(
                self.constraint_solver.correct_mass_balance(proposal)
            )
        
        # Check thermodynamic feasibility
        if not self.plausibility_checker.check_thermodynamics(proposal):
            violations.append("Thermodynamic feasibility violation")
            corrections.update(
                self.constraint_solver.correct_thermodynamics(proposal)
            )
        
        # Check biological constraints
        biological_violations = self.plausibility_checker.check_biological_constraints(proposal)
        if biological_violations:
            violations.extend(biological_violations)
            corrections.update(
                self.constraint_solver.correct_biological_constraints(proposal, biological_violations)
            )
        
        result = {
            'is_plausible': len(violations) == 0,
            'violations': violations,
            'corrections': corrections,
            'corrected_proposal': self._apply_corrections(proposal, corrections)
        }
        
        return result
    
    def verify_healing_instructions(self, instructions: Dict[str, Any]) -> Dict[str, Any]:
        """Specialized verification for healing instructions"""
        # Specific checks for healing protocols
        healing_violations = []
        
        # Check growth factor dosages
        if 'growth_factors' in instructions:
            for gf, dosage in instructions['growth_factors'].items():
                if not self.plausibility_checker.check_growth_factor_dosage(gf, dosage):
                    healing_violations.append(f"Excessive {gf} dosage: {dosage}")
        
        # Check timing constraints
        if not self.plausibility_checker.check_timing_constraints(instructions):
            healing_violations.append("Biologically implausible timing")
        
        return {
            'valid_instructions': len(healing_violations) == 0,
            'violations': healing_violations,
            'verified_instructions': instructions  # Would be corrected in real implementation
        }
    
    def _apply_corrections(self, original: Dict[str, Any], corrections: Dict[str, Any]) -> Dict[str, Any]:
        """Apply corrections to original proposal"""
        corrected = original.copy()
        corrected.update(corrections)
        return corrected