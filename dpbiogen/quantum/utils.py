# dpbiogen/quantum/utils.py  (new file for shared utilities like loaders)
"""
Utility functions for the quantum module, e.g., loading agent states from data files.
"""

import csv
from typing import Dict

def load_initial_states_from_csv(file_path: str) -> Dict[str, float]:
    """
    Load agent initial states from a CSV file.
    
    Expected CSV format (no header required):
    agent_name,initial_state
    Heart-Rate-Variability,25.0
    Blood-Pressure-Systolic,22.0
    ... etc.
    
    Returns a dict of {agent_name: initial_state}.
    """
    states = {}
    with open(file_path, mode='r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2:
                name, state_str = row
                try:
                    states[name.strip()] = float(state_str.strip())
                except ValueError:
                    print(f"Warning: Invalid state for {name}: {state_str} — skipping.")
    return states
