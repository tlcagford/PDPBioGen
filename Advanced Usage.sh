# With static exports and filtering
python pdpbiogen.py protein.fasta --static my_plot --min-length 50 --width 1200

# Publication-ready figures
python pdpbiogen.py protein.fasta --static publication --no-group

# Custom output name
python pdpbiogen.py protein.fasta -o domains.html --static figures/domains