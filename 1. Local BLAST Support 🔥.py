# core/blast_engine.py
class BlastEngine:
    def __init__(self, config):
        self.config = config
        self.local_dbs = self._discover_local_dbs()
    
    def blast_search(self, query_sequence, db_type="auto"):
        """Unified BLAST - tries local first, falls back to remote"""
        # Try local databases first
        if self.local_dbs and db_type != "remote":
            result = self._local_blast(query_sequence, db_type)
            if result.success:
                return result
        
        # Fallback to remote
        return self._remote_blast(query_sequence)
    
    def _local_blast(self, query_sequence, db_type):
        """Execute local BLAST with configurable parameters"""
        cmd = [
            "blastp" if self.config.protein else "blastn",
            "-query", query_sequence,
            "-db", self._select_local_db(db_type),
            "-outfmt", "6",  # Tabular format
            "-evalue", str(self.config.evalue),
            "-max_target_seqs", str(self.config.max_seqs),
            "-num_threads", str(self.config.threads)
        ]
        # Execute and parse results