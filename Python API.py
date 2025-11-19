from pdpbiogen import create_diagram
from pdpbiogen.pdpbiogen import load_configuration, render_diagram

# Load configuration
data = load_configuration('pathway.yaml')

# Create diagram
dot = create_diagram(data)

# Render to files
render_diagram(dot, 'output')
