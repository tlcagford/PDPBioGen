test_datasets = {
    "globin_family": {
        "description": "Well-conserved protein family with known evolutionary relationships",
        "sequences": ["HBA_HUMAN", "HBB_HUMAN", "MYG_HORSE", "GLB5_PETMA"],
        "expected_hits": 50-200,  # Expected BLAST results
        "alignment_length": ~140-150  # Conserved core length
    },
    "serine_proteases": {
        "description": "Diverse enzyme family with conserved catalytic triad",
        "sequences": ["TRY1_BOVIN", "EL1_HUMAN", "THRB_HUMAN"],
        "expected_hits": 100-500,
        "alignment_length": ~200-250
    },
    "kinase_domain": {
        "description": "Modular domain with conserved motifs",
        "sequences": ["SRC_HUMAN", "ABL1_HUMAN", "MAPK1_HUMAN"],
        "expected_hits": 1000+,
        "alignment_length": ~250-300
    }
}