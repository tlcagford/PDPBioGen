import os
from pathlib import Path

class Config:
    """Configuration management for PDPBioGen."""
    
    def __init__(self):
        self.api_key = self._get_api_key()
        self.default_model = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
        self.max_tokens = int(os.getenv('MAX_TOKENS', '500'))
        self.temperature = float(os.getenv('TEMPERATURE', '0.7'))
    
    def _get_api_key(self):
        """Safely retrieve API key from environment variables."""
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY environment variable not set.\n"
                "Please set it with: export OPENAI_API_KEY='your-key-here'"
            )
        return api_key
