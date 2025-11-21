from Bio.AlignIO import read
alignment = read("output.fasta", "fasta")
print(f"Valid alignment with {len(alignment)} sequences")