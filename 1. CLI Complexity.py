# Current: Too many nested options
@cli.command()
@click.option('--config', '-c')
@click.option('--preset', '-p')
@click.option('--output-dir', '-o')

# Suggestion: Preset-based with override capability
@cli.command()
@click.argument('input_sequence')
@click.option('--preset', default='standard', 
              type=click.Choice(['quick', 'standard', 'publication']))
@click.option('--overrides', help='JSON string of parameter overrides')