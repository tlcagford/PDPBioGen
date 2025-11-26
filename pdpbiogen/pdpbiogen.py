import yaml
import graphviz
import sys
import os
from typing import Dict, Any, List

# Import local modules
from .exceptions import PDPBioGenError, ConfigurationError, GraphvizError, ValidationError
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
def get_expanded_color_scheme():
    """Enhanced color scheme with 30 distinct colors"""
    return [
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
        '#393b79', '#637939', '#8c6d31', '#843c39', '#7b4173',
        '#5254a3', '#6b6ecf', '#9c9ede', '#3182bd', '#e6550d',
        '#31a354', '#756bb1', '#636363', '#bd9e39', '#6baed6',
        '#fd8d3c', '#74c476', '#9e9ac8', '#969696', '#d9d9d9'
    ]

unique_domains = domains_df['domain_name'].unique()
color_mapping = {}
expanded_colors = get_expanded_color_scheme()
for i, domain in enumerate(unique_domains):
    color_mapping[domain] = expanded_colors[i % len(expanded_colors)]
                edge_attrs['color'] = interaction['color']
            
            dot.edge(from_mol, to_mol, **edge_attrs)
            logger.debug(f"Added interaction: {from_mol} -> {to_mol}")
        
        logger.info(f"Created diagram with {len(molecules)} molecules and {len(interactions)} interactions")
        return dot
        
    except graphviz.ExecutableNotFound as e:
        raise GraphvizError("Graphviz not installed. Please install Graphviz: https://graphviz.org/download/")
    except Exception as e:
        raise GraphvizError(f"Failed to create diagram: {e}")

def main():
    """Original main function for backward compatibility."""
    if len(sys.argv) != 3:
        print("Usage: python -m pdpbiogen.pdpbiogen <input_yaml> <output_basename>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_basename = sys.argv[2]
    
    try:
        data = load_configuration(input_file)
        dot = create_diagram(data)
        
        # Render to multiple formats
        for format in ['png', 'svg', 'pdf']:
            dot.render(output_basename, format=format, cleanup=True)
            print(f"Generated {output_basename}.{format}")
            
    except PDPBioGenError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
