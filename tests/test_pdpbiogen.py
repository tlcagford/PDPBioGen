import pytest
import os
import tempfile
from unittest.mock import patch, MagicMock

from pdpbiogen.pdpbiogen import load_configuration, create_diagram, render_diagram
from pdpbiogen.exceptions import ConfigurationError, GraphvizError, ValidationError

class TestPDPBioGen:
    
    def test_load_configuration_valid(self, temp_yaml_file, sample_config):
        """Test loading valid YAML configuration."""
        yaml_file = temp_yaml_file(sample_config)
        
        try:
            result = load_configuration(yaml_file)
            assert result == sample_config
        finally:
            os.unlink(yaml_file)
    
    def test_load_configuration_file_not_found(self):
        """Test loading non-existent file."""
        with pytest.raises(ConfigurationError, match="not found"):
            load_configuration('nonexistent.yaml')
    
    def test_load_configuration_invalid_yaml(self, temp_yaml_file):
        """Test loading invalid YAML."""
        yaml_file = temp_yaml_file("invalid: yaml: [content")
        
        try:
            with pytest.raises(ConfigurationError, match="Invalid YAML"):
                load_configuration(yaml_file)
        finally:
            os.unlink(yaml_file)
    
    def test_load_configuration_empty_file(self, temp_yaml_file):
        """Test loading empty YAML file."""
        yaml_file = temp_yaml_file(None)
        
        try:
            with pytest.raises(ConfigurationError, match="empty or invalid"):
                load_configuration(yaml_file)
        finally:
            os.unlink(yaml_file)
    
    def test_create_diagram_valid(self, sample_config):
        """Test creating diagram from valid configuration."""
        dot = create_diagram(sample_config)
        
        # Check that graph was created
        assert dot is not None
        assert len(dot.body) > 0
        
        # Verify nodes were added
        node_ids = [line.split('[')[0].strip() for line in dot.body if '[' in line and '->' not in line]
        expected_nodes = ['Ligand', 'Receptor', 'Complex', 'Response']
        for node in expected_nodes:
            assert any(node in node_id for node_id in node_ids)
    
    def test_create_diagram_invalid_config(self):
        """Test creating diagram from invalid configuration."""
        invalid_config = {
            'molecules': {
                'Invalid-Node': {'color': 'red'}  # Invalid node name
            }
        }
        
        with pytest.raises(ValidationError):
            create_diagram(invalid_config)
    
    @patch('pdpbiogen.pdpbiogen.graphviz.Digraph')
    def test_create_diagram_graphviz_error(self, mock_digraph, sample_config):
        """Test Graphviz errors during diagram creation."""
        mock_digraph.side_effect = Exception("Graphviz failed")
        
        with pytest.raises(GraphvizError, match="Failed to create diagram"):
            create_diagram(sample_config)
    
    def test_render_diagram_success(self, sample_config, cleanup_files):
        """Test successful diagram rendering."""
        dot = create_diagram(sample_config)
        
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = os.path.join(temp_dir, 'test_output')
            
            render_diagram(dot, output_path, formats=['svg'])
            
            # Check that file was created
            expected_file = output_path + '.svg'
            assert os.path.exists(expected_file)
    
    def test_render_diagram_multiple_formats(self, sample_config, cleanup_files):
        """Test rendering to multiple formats."""
        dot = create_diagram(sample_config)
        
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = os.path.join(temp_dir, 'test_output')
            
            render_diagram(dot, output_path, formats=['svg', 'png'])
            
            # Check that both files were created
            assert os.path.exists(output_path + '.svg')
            assert os.path.exists(output_path + '.png')
