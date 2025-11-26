import os
import zipfile

# Define file contents for PDPBioGen FullPackage
files_content = {
    'README.md': """# 🧬 PDPBioGen
[Build Badge]

Full fixed README content placeholder.
""",
    'architecture.svg': "<svg xmlns='http://www.w3.org/2000/svg'></svg>",
    'mkdocs.yml': """site_name: PDPBioGen Documentation
""",
    'docs/index.md': "# Welcome to PDPBioGen Documentation",
    'docs/installation.md': "# Installation Instructions",
    'docs/architecture.md': "# Architecture Diagram",
    'docs/datasets.md': "# Dataset Details",
    'docs/api.md': "# API Reference",
    'docs/pipeline.md': "# Pipeline Usage"
}

zip_filename = '/mnt/data/PDPBioGen_FullPackage.zip'

# Create ZIP file
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for filepath, content in files_content.items():
        zipf.writestr(filepath, content)

zip_filename
