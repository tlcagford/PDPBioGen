# Core: Just these 3 well-implemented functions
def run_blast_pipeline(sequence_file, config) -> BlastResult
def run_alignment_pipeline(sequences, config) -> AlignmentResult  
def run_tree_pipeline(alignment, config) -> TreeResult

# Plus robust utilities:
validate_inputs()
manage_resources()
handle_errors()
track_progress()