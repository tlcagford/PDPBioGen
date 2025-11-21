class BiologicalValidator:
    def run_comprehensive_checks(self, generated_data):
        return {
            "expression_ranges": self._validate_plausible_ranges(),
            "correlation_structure": self._check_biological_correlations(),
            "variance_components": self._validate_tech_vs_bio_variance(),
            "effect_size_plausibility": self._check_treatment_effects()
        }
