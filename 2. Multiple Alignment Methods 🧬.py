# core/alignment_engine.py
class AlignmentEngine:
    SUPPORTED_ALIGNERS = {
        "mafft": {"install": "brew install mafft", "args": ["--auto", "--thread", "{}"]},
        "muscle": {"install": "brew install muscle", "args": ["-maxiters", "2"]},
        "clustalo": {"install": "brew install clustal-o", "args": ["--threads={}"]},
        "t-coffee": {"install": "brew install t-coffee", "args": []}
    }
    
    def align_sequences(self, sequences_file, method="mafft", threads=4):
        """Execute alignment with selected method"""
        if method not in self.SUPPORTED_ALIGNERS:
            raise AlignmentError(f"Unsupported aligner: {method}")
        
        if not self._check_aligner_installed(method):
            raise AlignmentError(f"{method} not installed. {self.SUPPORTED_ALIGNERS[method]['install']}")
        
        # Build command with configurable parameters
        aligner_args = [arg.format(threads) for arg in self.SUPPORTED_ALIGNERS[method]['args']]
        cmd = [method] + aligner_args + [sequences_file]
        
        return self._execute_alignment(cmd, sequences_file)