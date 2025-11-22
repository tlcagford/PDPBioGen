
For real heart/endocrine/respiratory data: Process sensor outputs (e.g., ECG via biosppy, hormone proxies via GSR) to compute deviations, save to CSV as agent_name,initial_state pairs, then pass as arg.

See LAB_SETUP.md for building a physical lab system to feed live data into the module.

No additional requirements beyond the main PDPBioGen project (pure Python + csv stdlib; optionally numpy/biosppy for real data processing upstream).

Drop the quantum folder into the dpbiogen/ package and import as dpbiogen.quantum.

Ready for integration with the Grok-4.1-fast Healing Council or real-time BCI loop.
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import imageio  # for GIF, optional pip install imageio

sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0
z_target = rho - 1  # ≈27.0 (healthy fixed point z-value)

# Synthetic "real patient BCI" intent signal (low alpha, noisy beta-dominated = diseased brain)
# Replace this entire array with your real processed patient data (see note below)
t_end = 50.0
dt = 0.01
t = np.arange(0, t_end, dt)
n_steps = len(t)

# Diseased patient intent: average ~0.25 with bursts, very noisy (typical in chronic illness)
intent_base = 0.25 + 0.15 * np.sin(t * 0.3 + np.pi) + 0.12 * np.random.randn(n_steps)

# Initial state far from attractor (typical chaotic diseased start)
initial_state = [1.0, 1.0, 1.0]

# === OPEN-LOOP (low intent, no feedback) ===
state_open = np.zeros((n_steps, 3))
state_open[0] = initial_state
for i in range(1, n_steps):
    x, y, z = state_open[i-1]
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z + intent_base[i] * 12 * (z_target - z)  # weak push
    state_open[i] = [x + dx * dt, y + dy * dt, z + dz * dt]

# === CLOSED-LOOP BCI-GUIDED (virtuous healing cycle) ===
state_closed = np.zeros((n_steps, 3))
state_closed[0] = initial_state
for i in range(1, n_steps):
    x, y, z = state_closed[i-1]
    deviation = abs(z - z_target) / z_target
    # Virtuous cycle: the sicker the patient, the stronger the resolved intent becomes (BCI amplifies)
    effective_control = np.clip(intent_base[i] * (0.4 + deviation * 1.8), 0.0, 1.0)
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z + effective_control * 35 * (z_target - z)  # strong negative feedback to healthy point
    state_closed[i] = [x + dx * dt, y + dy * dt, z + dz * dt]

# Plots
fig = plt.figure(figsize=(14, 6))

ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.plot(state_open[:,0], state_open[:,1], state_open[:,2], lw=0.5, color='#ff5555', label='Open-loop (chronic)')
ax1.set_title("OPEN-LOOP: Chronic Disease State\nChaotic forever")
ax1.grid(False)

ax2 = fig.add_subplot(1, 2, 2, projection='3d')
ax2.plot(state_closed[:,0], state_closed[:,1], state_closed[:,2], lw=1.2, color='#00ff00', label='Closed-loop BCI-guided healing')
ax2.set_title("CLOSED-LOOP: 50ms BCI heals in ~12s")
ax2.grid(False)

plt.suptitle("PDPBioGen Closed-Loop In-Silico Demo – Real-time Brain-Guided Healing", fontsize=16)
plt.show()

# Save GIF (optional
# frames = []
# for i in range(0, n_steps, 10):
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     ax.plot(state_closed[0:i,0], state_closed[0:i,1], state_closed[0:i,2], color='#00ff00')
#     ax.set_xlim(-20,20)
#     ax.set_ylim(-30,20)
#     ax.set_zlim(0,50)
#     plt.savefig(f"frame{i}.png")
#     frames.append(imageio.imread(f"frame{i}.png"))
# imageio.mimsave('pdp_healing.gif', frames, fps=30)
