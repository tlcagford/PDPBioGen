# Example: Simulating our Compound X experiment
experiment_params = {
    "treatment_groups": [
        {"group_id": "G1", "description": "Untreated Control", "n_replicates": 3},
        {"group_id": "G2", "description": "LPS only", "n_replicates": 3},
        {"group_id": "G3", "description": "LPS + Compound X 1uM", "n_replicates": 3},
        {"group_id": "G4", "description": "LPS + Compound X 10uM", "n_replicates": 3}
    ],
    "target_genes": {
        "inflammatory": ["IL6", "TNF", "IL1B"],
        "housekeeping": ["GAPDH", "ACTB", "B2M"]
    },
    "effect_sizes": {
        "G3": 0.4,  # 40% reduction vs LPS
        "G4": 0.7   # 70% reduction vs LPS
    }
}
