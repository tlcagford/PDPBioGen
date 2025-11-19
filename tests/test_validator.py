import pytest
from pdpbiogen.validator import PathwayValidator
from pdpbiogen.exceptions import ValidationError

class TestPathwayValidator:
    
    def test_validate_molecule_id_valid(self):
        """Test valid molecule IDs."""
        valid_ids = ['ProteinA', 'gene_1', 'mRNA_123', 'A', 'a1_b2']
        for molecule_id in valid_ids:
            PathwayValidator.validate_molecule_id(molecule_id)  # Should not raise
    
    def test_validate_molecule_id_invalid(self):
        """Test invalid molecule IDs."""
        invalid_cases = [
            ('123protein', "starts with number"),
            ('protein-1', "contains hyphen"),
            ('protein 1', "contains space"),
            ('', "empty string"),
            (None, "None type"),
            (123, "integer type")
        ]
        
        for molecule_id, description in invalid_cases:
            with pytest.raises(ValidationError, match=f"Molecule ID"):
                PathwayValidator.validate_molecule_id(molecule_id)
    
    def test_validate_molecules_valid(self, sample_config):
        """Test valid molecules configuration."""
        PathwayValidator.validate_molecules(sample_config['molecules'])  # Should not raise
    
    def test_validate_molecules_empty(self):
        """Test empty molecules configuration."""
        with pytest.raises(ValidationError, match="No molecules defined"):
            PathwayValidator.validate_molecules({})
    
    def test_validate_molecules_invalid_structure(self):
        """Test invalid molecules structure."""
        invalid_molecules = {
            'ValidProtein': {'color': 'blue'},
            123: {'color': 'red'}  # Invalid key type
        }
        
        with pytest.raises(ValidationError, match="Molecule ID must be string"):
            PathwayValidator.validate_molecules(invalid_molecules)
    
    def test_validate_interactions_valid(self, sample_config):
        """Test valid interactions."""
        molecules = sample_config['molecules']
        interactions = sample_config['interactions']
        PathwayValidator.validate_interactions(interactions, molecules)  # Should not raise
    
    def test_validate_interactions_undefined_molecule(self, sample_config):
        """Test interactions with undefined molecules."""
        molecules = sample_config['molecules']
        invalid_interactions = [
            {'from': 'Ligand', 'to': 'UndefinedProtein'}
        ]
        
        with pytest.raises(ValidationError, match="target molecule 'UndefinedProtein' not defined"):
            PathwayValidator.validate_interactions(invalid_interactions, molecules)
    
    def test_validate_interactions_missing_keys(self):
        """Test interactions missing required keys."""
        molecules = {'ProteinA': {}, 'ProteinB': {}}
        invalid_interactions = [
            {'from': 'ProteinA'},  # Missing 'to'
            {'to': 'ProteinB'}     # Missing 'from'
        ]
        
        for interaction in invalid_interactions:
            with pytest.raises(ValidationError, match="must have 'from' and 'to' keys"):
                PathwayValidator.validate_interactions([interaction], molecules)
    
    def test_validate_configuration_valid(self, sample_config):
        """Test valid complete configuration."""
        PathwayValidator.validate_configuration(sample_config)  # Should not raise
    
    def test_validate_configuration_missing_molecules(self):
        """Test configuration missing molecules section."""
        invalid_config = {
            'interactions': [{'from': 'A', 'to': 'B'}]
        }
        
        with pytest.raises(ValidationError, match="must contain 'molecules' section"):
            PathwayValidator.validate_configuration(invalid_config)
