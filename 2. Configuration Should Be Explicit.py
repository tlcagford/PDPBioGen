# Instead of magical preset loading
PRESETS = {
    'quick': PipelineConfig(
        blast_evalue=1e-3,
        blast_max_seqs=50,
        alignment_method='muscle',
        tree_method='fasttree'
    ),
    'publication': PipelineConfig(
        blast_evalue=1e-10,
        blast_max_seqs=200,
        alignment_method='mafft',
        tree_method='raxml',
        bootstrap_replicates=1000
    )
}