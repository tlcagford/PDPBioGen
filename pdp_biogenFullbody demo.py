import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Subsystems for full-body demo (aggregated for clarity in visualization)
subsystems = [
    "Brain Subsystem",
    "Heart Subsystem",
    "Endocrine Subsystem",
    "Respiratory Subsystem",
    "Other Subsystems"
]

# Initial deviations (sum of absolute states per subsystem, approx from demo)
initial_devs = [147.0, 215.0, 140.0, 119.0, 50.0]

# After collapse (each subsystem's agents pulled to ~0.889, sum abs ~ num_agents * 0.889)
collapsed_devs = [7.11, 9.78, 7.11, 6.22, 2.67]  # Calculated from 37 agents, target ~0.889

# Animation setup
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(subsystems, initial_devs, color='lightcoral')
ax.set_xlim(0, 250)
ax.set_title("PDPBioGen Quantum Module: Full-Body Healing Demo (~50ms Collapse)")
ax.set_xlabel("Total Deviation from Healthy Equilibrium")
ax.axvline(0, color='green', linestyle='--', label='Healthy (0.0)')
ax.legend()

# Add text for before/after and total deviation
total_initial = sum(initial_devs)  # 671.0
total_collapsed = sum(collapsed_devs)  # ~32.89
status_text = ax.text(0.05, 0.95, f"Before Collapse: Chaotic State (Total Dev: {total_initial:.2f})", 
                      transform=ax.transAxes, fontsize=12, verticalalignment='top')

def animate(frame):
    # Interpolate from initial to collapsed over 20 frames (linear for smooth demo; could make 'instant' by thresholding)
    t = frame / 20.0  # Normalize to [0,1]
    current_devs = [(1 - t) * initial + t * collapsed for initial, collapsed in zip(initial_devs, collapsed_devs)]
    
    for bar, height in zip(bars, current_devs):
        bar.set_width(height)
    
    current_total = sum(current_devs)
    if frame >= 10:  # Switch text mid-animation for emphasis
        status_text.set_text(f"After Collapse: Healed (Total Dev: {current_total:.2f})")
    
    return bars + [status_text]

# Create animation
anim = FuncAnimation(fig, animate, frames=21, interval=50, blit=True)

# Save as GIF
anim.save('pdpbiogen_full_body_demo.gif', writer='pillow', fps=20)

print("GIF saved as pdpbiogen_full_body_demo.gif! Post this on X to showcase the full-body healing simulation.")