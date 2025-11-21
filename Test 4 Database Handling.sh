# Test different BLAST databases
databases = ["swissprot", "nr", "pdb", "refseq_protein"]
for db in databases:
    poetry run python -m pdpbiogen blast_to_align \
        --sequence TEST.fasta \
        --database $db \
        --output test_${db}.fasta