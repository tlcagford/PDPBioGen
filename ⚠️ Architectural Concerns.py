# Current: Nested YAML might become unwieldy
pipelines:
  standard_phylogeny:
    steps:
      - blast:
          evalue: 1e-5
          max_sequences: 100
      - alignment:
          method: mafft
      - tree_building:
          method: fasttree

# Suggestion: Flatter, more explicit structure
pipeline:
  name: "standard_phylogeny"
  blast_evalue: 1e-5
  blast_max_seqs: 100
  alignment_method: "mafft"
  tree_method: "fasttree"