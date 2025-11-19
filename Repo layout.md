PDPBioGen/
├── pdpbiogen/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── integrator.py
│   │   ├── agent_system.py
│   │   ├── domain_manager.py
│   │   └── utils.py
│   ├── modules/
│   │   ├── __init__.py
│   │   ├── neural/
│   │   │   └── neural_mapper.py
│   │   ├── genomic/
│   │   │   └── genomic_mapper.py
│   │   └── metabolic/
│   │       └── metabolic_mapper.py
│   └── validation/
│       └── validators.py
├── data/
│   └── sample/
│       ├── neural_sample.json
│       ├── genome_sample.json
│       └── metabolism_sample.json
├── examples/
│   ├── quick_start.ipynb             # notebook stub (contents described)
│   └── cross_domain_run.py
├── tests/
│   ├── unit/
│   │   ├── test_integrator.py
│   │   ├── test_agent_system.py
│   │   ├── test_mappers.py
│   │   └── test_utils.py
│   └── integration/
│       └── test_full_pipeline.py
├── README.md
├── requirements.txt
├── pyproject.toml
└── setup.cfg
