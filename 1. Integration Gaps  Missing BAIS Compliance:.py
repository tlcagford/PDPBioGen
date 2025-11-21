# Suggested enhancement
def export_to_bais(self, experiment_config, output_path):
    """Export generated data in BAIS format"""
    bais_structure = {
        "bais_version": "1.0",
        "project_metadata": self._generate_metadata(experiment_config),
        "experimental_design": self._generate_design(experiment_config),
        "lab_protocol": self._generate_protocol(experiment_config),
        "raw_data": self._format_raw_data(),
        "analysis_parameters": self._define_analysis(),
        "processed_results": self._calculate_results()
    }
    
    with open(output_path, 'w') as f:
        json.dump(bais_structure, f, indent=2)
