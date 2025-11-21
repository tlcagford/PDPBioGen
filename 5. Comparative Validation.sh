# Run identical analysis manually for comparison
# Manual method:
blastp -query TEST.fasta -db nr -outfmt 6 -max_target_seqs 100 > manual_blast.out
# Extract hits, retrieve sequences, align with MAFFT

# Compare PDPBioGen vs Manual results:
compare_alignments.py pdpbiogen_alignment.fasta manual_alignment.fasta