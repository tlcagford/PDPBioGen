# Core structure (from repository analysis)
PDPBioGen/
├── data_generators/          # Biological data simulators
│   ├── sequence_generator.py
│   ├── expression_generator.py
│   └── network_generator.py
├── parameter_controllers/    # Parameter management
│   ├── distribution_controller.py
│   └── constraint_manager.py
├── file_exporters/          # Format handlers
│   ├── fasta_exporter.py
│   ├── csv_exporter.py
│   └── bio_formats.py
└── validation/              # Quality control
    ├── data_validator.py
    └── statistical_checks.py
