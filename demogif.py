import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Simulate agent states (from seizure demo example)
agents = [
    "Residual-Intent-Detector (Neural)",
    "Cerebral-Left",
    "Cerebral-Right",
    "Mitochondria-Net",
    "Immune-Response",
    "Neurotrans-Balance",
    "Heart-Rate-Var",
    "Blood-Brain-Flux"
]

# Initial states (neural at 9.0, others chaotic)
initial_states = [9.0, 18.0, -14.0, 23.0, -19.0, 16.0, 21.0, -17.0]

# After collapse (with neural_weight=200, neural forced to 0.0)
# Calculated weighted avg: neural dominates, all near 0.0 (approx +0.135 for bio)
collapsed_states = [0.0] + [0.135] * 7  # Simplified for animation

# Animation setup
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(agents, initial_states, color='skyblue')
ax.set_xlim(-25, 25)
ax.set_title("PDPBioGen Quantum Healing Demo: State Collapse (~50ms)")
ax.set_xlabel("Deviation from Healthy Equilibrium")
ax.axvline(0, color='red', linestyle='--', label='Healthy (0.0)')
ax.legend()

# Add text for before/after
status_text = ax.text(0.05, 0.95, "Before Collapse: Chaotic State", transform=ax.transAxes, fontsize=12, verticalalignment='top')

def animate(frame):
    # Interpolate from initial to collapsed over 20 frames
    t = frame / 20.0  # Normalize to [0,1]
    current_states = [(1 - t) * initial + t * collapsed for initial, collapsed in zip(initial_states, collapsed_states)]
    
    for bar, height in zip(bars, current_states):
        bar.set_width(height)
    
    if frame == 20:
        status_text.set_text("After Collapse: Healed (Near 0.0)")
    
    return bars + [status_text]

# Create animation
anim = FuncAnimation(fig, animate, frames=21, interval=50, blit=True)

# Save as GIF
anim.save('pdpbiogen_demo.gif', writer='pillow', fps=20)

print("GIF saved as pdpbiogen_demo.gif! You can post this on X for the demo.")
