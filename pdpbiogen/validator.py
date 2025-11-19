import re
from .exceptions import ValidationError
from .logger import logger

class PathwayValidator:
    """Validate pathway configuration data."""
    
    @staticmethod
    def validate_molecule_id(molecule_id):
        """Validate molecule identifier format."""
        if not isinstance(molecule_id, str):
            raise ValidationError(f"Molecule ID must be string, got {type(molecule_id)}")
        
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', molecule_id):
            raise ValidationError(
                f"Invalid molecule ID: '{molecule_id}'. "
                "Must start with letter/underscore and contain only alphanumeric characters."
            )
    
    @staticmethod
    def validate_color(color):
        """Validate color format."""
        if not isinstance(color, str):
            raise ValidationError(f"Color must be string, got {type(color)}")
        
        # Basic color validation (could be enhanced with proper color names/hex codes)
        if not color:
            raise ValidationError("Color cannot be empty")
    
    @staticmethod
    def validate_molecules(molecules):
        """Validate molecules configuration."""
        if not molecules:
            raise ValidationError("No molecules defined in configuration")
        
        for molecule_id, config in molecules.items():
            PathwayValidator.validate_molecule_id(molecule_id)
            
            if not isinstance(config, dict):
                raise ValidationError(f"Molecule '{molecule_id}' configuration must be a dictionary")
            
            if 'color' in config:
                PathwayValidator.validate_color(config['color'])
    
    @staticmethod
    def validate_interactions(interactions, molecules):
        """Validate interactions configuration."""
        if not interactions:
            logger.warning("No interactions defined in configuration")
            return
        
        for i, interaction in enumerate(interactions):
            if not isinstance(interaction, dict):
                raise ValidationError(f"Interaction at index {i} must be a dictionary")
            
            if 'from' not in interaction or 'to' not in interaction:
                raise ValidationError(f"Interaction at index {i} must have 'from' and 'to' keys")
            
            from_mol = interaction['from']
            to_mol = interaction['to']
            
            if from_mol not in molecules:
                raise ValidationError(f"Interaction {i}: source molecule '{from_mol}' not defined")
            
            if to_mol not in molecules:
                raise ValidationError(f"Interaction {i}: target molecule '{to_mol}' not defined")
            
            if 'color' in interaction:
                PathwayValidator.validate_color(interaction['color'])
    
    @staticmethod
    def validate_configuration(data):
        """Validate complete configuration."""
        if not isinstance(data, dict):
            raise ValidationError("Configuration must be a dictionary")
        
        if 'molecules' not in data:
            raise ValidationError("Configuration must contain 'molecules' section")
        
        PathwayValidator.validate_molecules(data['molecules'])
        
        if 'interactions' in data:
            PathwayValidator.validate_interactions(data['interactions'], data['molecules'])
