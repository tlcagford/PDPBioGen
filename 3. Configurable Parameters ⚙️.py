# config/pipeline_presets.yaml
pipelines:
  standard_phylogeny:
    description: "Standard protein phylogeny pipeline"
    steps:
      - blast:
          evalue: 1e-5
          max_sequences: 100
          database: swissprot
          use_local: true
      - alignment:
          method: mafft
          strategy: auto
          threads: 4
      - tree_building:
          method: fasttree
          model: "JTT"  # For proteins
          support: 1000  # Bootstrap replicates
          
  orthology_analysis:
    description: "Ortholog detection with strict parameters"
    steps:
      - blast:
          evalue: 1e-10
          max_sequences: 50
          database: refseq_protein
      - alignment:
          method: clustalo
          strategy: accurate