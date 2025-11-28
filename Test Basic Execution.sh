# Dry run test
nextflow run pdpbiogen.nf --gwas_sumstats examples/ibd_gwas.tsv -resume

# Check if all processes are defined
nextflow run pdpbiogen.nf --help
