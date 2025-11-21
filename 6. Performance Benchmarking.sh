# Test with increasing dataset sizes
sequence_lengths = [100, 500, 1000]  # amino acids
num_sequences = [10, 50, 100, 500]   # homologs to retrieve

for size in sequence_lengths:
    poetry run python -m pdpbiogen blast_to_align \
        --sequence synthetic_${size}aa.fasta \
        --database swissprot \
        --output benchmark_${size}.fasta