# Instead of complex class hierarchy
def run_blast(query, database, evalue=1e-5, max_seqs=100, use_local=True):
    """Unified BLAST runner with automatic fallback"""
    if use_local and local_database_exists(database):
        return run_local_blast(query, database, evalue, max_seqs)
    else:
        return run_remote_blast(query, database, evalue, max_seqs)