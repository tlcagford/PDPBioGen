# Using human hemoglobin alpha as query
poetry run python -m pdpbiogen blast_to_align \
    --sequence HBA_HUMAN.fasta \
    --database swissprot \
    --output globin_alignment.fasta \
    --aligner mafft