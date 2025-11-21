# 1. Setup with local databases
pdpbiogen setup-database

# 2. Run standard pipeline
pdpbiogen run-pipeline --preset standard -i my_sequence.fasta -o results/

# 3. Run custom pipeline  
pdpbiogen run-pipeline --config my_custom_pipeline.yaml

# 4. Just do alignment with specific method
pdpbiogen align-sequences -i sequences.fasta --method clustalo