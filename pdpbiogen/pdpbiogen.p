import yaml
import graphviz
import sys
import os
from typing import Dict, Any, List

from .exceptions import ConfigurationError, GraphvizError, ValidationError
from .validator import PathwayValidator
from .logger import logger

def load_configuration(input_file: str) -> Dict[str, Any]:
    """Load and validate YAML configuration."""
    try:
        with open(input_file, 'r') as f:
            data = yaml.safe_load(f)
        
        if data is None:
            raise ConfigurationError(f"YAML file '{input_file}' is empty or invalid")
        
        logger.info(f"Loaded configuration from {input_file}")
        return data
        
    except yaml.YAMLError as e:
        raise ConfigurationError(f"Invalid YAML in {input_file}: {e}")
    except FileNotFoundError:
        raise ConfigurationError(f"Input file not found: {input_file}")
    except PermissionError:
        raise ConfigurationError(f"Permission denied reading: {input_file}")

def create_diagram(data: Dict[str, Any]) -> graphviz.Digraph:
    """Create Graphviz diagram from configuration data."""
    try:
        # Validate configuration
        PathwayValidator.validate_configuration(data)
        
        # Create directed graph
        dot = graphviz.Digraph(comment='Biological Pathway')
        dot.attr(rankdir='TB')  # Top to bottom layout
        
        molecules = data.get('molecules', {})
        interactions = data.get('interactions', [])
        
        # Add molecules/nodes
        for molecule_id, config in molecules.items():
            label = config.get('label', molecule_id)
            node_type = config.get('type', 'default')
            
            # Set node attributes based on type
            node_attrs = {'label': label}
            
            # Color and shape based on molecule type
            if node_type == 'input':
                node_attrs.update({'color': 'lightblue', 'style': 'filled', 'shape': 'ellipse'})
            elif node_type == 'output':
                node_attrs.update({'color': 'lightcoral', 'style': 'filled', 'shape': 'ellipse'})
            else:
                node_attrs.update({'color': 'lightgreen', 'style': 'filled', 'shape': 'box'})
            
            # Override with custom color if specified
            if 'color' in config:
                node_attrs['color'] = config['color']
            
            dot.node(molecule_id, **node_attrs)
            logger.debug(f"Added molecule: {molecule_id}")
        
        # Add interactions/edges
        for interaction in interactions:
            from_mol = interaction['from']
            to_mol = interaction['to']
            edge_label = interaction.get('label', '')
            
            edge_attrs = {'label': edge_label}
            
            if 'color' in interaction:
                edge_attrs['color'] = interaction['color']
            
            dot.edge(from_mol, to_mol, **edge_attrs)
            logger.debug(f"Added interaction: {from_mol} -> {to_mol}")
        
        logger.info(f"Created diagram with {len(molecules)} molecules and {len(interactions)} interactions")
        return dot
        
    except graphviz.ExecutableNotFound as e:
        raise GraphvizError("Graphviz not installed. Please install Graphviz: https://graphviz.org/download/")
    except Exception as e:
        raise GraphvizError(f"Failed to create diagram: {e}")

def render_diagram(dot: graphviz.Digraph, output_basename: str, formats: List[str] = None):
    """Render diagram to multiple formats."""
    if formats is None:
        formats = ['png', 'svg', 'pdf']
    
    output_dir = os.path.dirname(output_basename) or '.'
    
    # Ensure output directory exists
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
        logger.info(f"Created output directory: {output_dir}")
    
    for format in formats:
        try:
            output_path = dot.render(
                filename=output_basename, 
                format=format, 
                cleanup=True,
                outfile=output_dir
            )
            logger.info(f"Generated {format.upper()} output: {output_path}")
        except Exception as e:
            raise GraphvizError(f"Failed to render {format.upper()} output: {e}")
