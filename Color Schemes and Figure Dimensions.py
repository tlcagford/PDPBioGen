def _create_domain_plot(domains_df, protein_length, custom_colors=None, width=1200, height=400):
    """Enhanced plotting function with customization"""
    
    # Generate color scheme
    if custom_colors:
        color_scheme = custom_colors
    else:
        # Default color scheme with more distinct colors
        default_colors = [
            '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
            '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
            '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5',
            '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5'
        ]
        unique_domains = domains_df['domain_name'].unique()
        color_scheme = {domain: default_colors[i % len(default_colors)] 
                       for i, domain in enumerate(unique_domains)}
    
    fig = go.Figure()
    
    # Adjust height based on number of domains
    adaptive_height = max(height, len(domains_df) * 25 + 100)
    
    # Create domain rectangles with hover info
    for i, (idx, row) in enumerate(domains_df.iterrows()):
        fig.add_trace(go.Scatter(
            x=[row['start'], row['end'], row['end'], row['start'], row['start']],
            y=[i, i, i+0.8, i+0.8, i],
            fill="toself",
            fillcolor=color_scheme[row['domain_name']],
            line=dict(color='black', width=1),
            name=row['domain_name'],
            hoverinfo="text",
            hovertext=(
                f"Domain: {row['domain_name']}<br>"
                f"Database: {row['database']}<br>"
                f"Position: {row['start']}-{row['end']}<br>"
                f"Length: {row['end'] - row['start'] + 1} aa<br>"
                f"Accession: {row.get('accession', 'N/A')}"
            ),
            showlegend=False
        ))
    
    # Update layout with customizable dimensions
    fig.update_layout(
        width=width,
        height=adaptive_height,
        title="Protein Domain Architecture",
        xaxis_title="Amino Acid Position",
        yaxis=dict(showticklabels=False, showgrid=False),
        hovermode="closest"
    )
    
    return fig
