# Missing: Input validation
class SequenceValidator:
    def validate_input_fasta(self, file_path):
        """Validate FASTA file before processing"""
        checks = [
            self._check_file_exists(file_path),
            self._check_fasta_format(file_path),
            self._check_sequence_lengths(file_path, min_len=10),
            self._check_sequence_chars(file_path)  # Valid AA/NT chars
        ]
        return all(checks)