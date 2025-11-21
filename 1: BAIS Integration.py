class BaisExporter:
    """Export generated data in Biological Assay Integration Schema"""
    
    def create_qpcr_experiment(self, design_params):
        return {
            "bais_version": "1.0",
            "experimental_design": self._create_design(design_params),
            "raw_data": self._format_ct_values(),
            "processed_results": self._calculate_fold_changes()
        }
