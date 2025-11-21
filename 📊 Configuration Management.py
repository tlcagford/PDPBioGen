# config/validators.py
class PipelineConfig:
    def __init__(self, config_dict):
        self.raw_config = config_dict
        self._validate()
    
    def _validate(self):
        # Validate BLAST parameters
        if self.raw_config.get('evalue', 0.1) <= 0:
            raise ConfigError("E-value must be positive")
        
        # Validate alignment method
        if self.raw_config.get('alignment_method') not in SUPPORTED_ALIGNERS:
            raise ConfigError(f"Unsupported alignment method")
        
        # Validate resource usage
        if self.raw_config.get('threads', 1) > os.cpu_count():
            raise ConfigError(f"Threads exceed available CPUs ({os.cpu_count()})")