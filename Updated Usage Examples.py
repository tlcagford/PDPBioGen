#!/usr/bin/env python3
"""
Enhanced usage examples for PDPBioGen with new features
"""

from pdpbiogen import generate_protein_domain_plot

# Example 1: Basic usage with static export
print("Example 1: Basic with static export")
fig, domains = generate_protein_domain_plot(
    "example.fasta",
    output_html="basic_domains.html",
    output_static="basic_domains"  # Exports PNG, PDF, SVG
)

# Example 2: Large protein with filtering
print("\nExample 2: Large protein filtering")
fig, domains = generate_protein_domain_plot(
    "large_protein.fasta",
    output_html="filtered_domains.html", 
    output_static="filtered_domains",
    min_domain_length=50,      # Filter out small domains
    group_similar=True,        # Group repeated domains
    figure_width=1200          # Wider figure
)

# Example 3: Publication-ready
print("\nExample 3: Publication ready")
fig, domains = generate_protein_domain_plot(
    "publication_protein.fasta",
    output_html="publication_domains.html",
    output_static="publication_domains",
    min_domain_length=30,
    figure_width=800           # Standard publication width
)
