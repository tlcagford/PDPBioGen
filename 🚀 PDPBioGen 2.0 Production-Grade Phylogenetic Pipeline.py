# New modular structure
pdpbiogen/
├── core/
│   ├── blast_engine.py      # Local/remote BLAST support
│   ├── alignment_engine.py  # Multiple aligners
│   └── tree_builder.py      # Phylogenetic inference
├── pipelines/
│   ├── standard_phylogeny.py
│   ├── orthology_pipeline.py
│   └── custom_workflow.py
├── config/
│   ├── presets/
│   └── validators.py
└── utils/
    ├── error_handling.py
    └── file_operations.py