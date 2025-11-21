# What it actually does:
blastp -query your_sequence.fasta -db nr | 
python parse_blast.py | 
python fetch_sequences.py | 
mafft > alignment.fasta