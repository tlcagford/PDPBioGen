# Start all three download streams simultaneously
downloader = TripleDomainDownloader()
all_data = downloader.download_all()

# Initial datasets for each domain:
# Neural: HCP minimal preprocessing + Allen Brain Atlas
# Genomic: GTEx v8 + ProteomicsDB human proteome  
# Metabolic: HMDB + UK Biobank metabolomics