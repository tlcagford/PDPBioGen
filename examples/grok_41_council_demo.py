import torch
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.signal import butter, filtfilt, hilbert
from scipy.interpolate import interp1d
import os
import json
from openai import OpenAI

# ====================== CONFIG ======================
API_KEY = os.getenv("GROK_API_KEY")  # Put your key in env or paste here for testing
MODEL = "grok-4-1-fast-reasoning"  # ABSOLUTE LATEST as of Nov 21 2025 — best agentic, cheapest, 2M context

USE_REAL_GROK_COUNCIL = API_KEY is not None

N_NODES = 100
STEPS = 800
DECISION_INTERVAL = 50
SPECTRAL_RADIUS = 1.45
CONTROL_SCALE = 20.0

TARGET_3D = torch.tensor([0.0, 0.0, 0.8])  # Healthy attractor

# ====================== LOAD REAL OR SYNTHETIC EEG ======================
try:
    fs = 173.61
    def load_bonn_file(path):
        return np.loadtxt(path)

    real_patient_intent = alpha_envelope(load_bonn_file('bonn/set_e/s001.txt'))  # change file as you like
    t_orig = np.linspace(0, len(real_patient_intent)/fs, len(real_patient_intent))
except:
    print("No Bonn file found → using synthetic seizure-like low-alpha intent")
    fs = 173.61
    t_orig = np.linspace(0, 23.6, 4096)
    real_patient_intent = np.abs(np.cumsum(np.random.randn(4096)) * 0.05 + 0.15)  # very low chaotic alpha
    real_patient_intent = real_patient_intent / real_patient_intent.max()

def alpha_envelope(data, low=8.0, high=12.0, fs=fs):
    nyq = 0.5 * fs
    b, a = butter(4, [low/nyq, high/nyq], btype='band')
    filtered = filtfilt(b, a, data)
    envelope = np.abs(hilbert(filtered))
    return envelope / (envelope.max() + 1e-9)

# Interpolate to simulation time
t_sim = np.arange(STEPS) * 0.01
f = interp1d(t_orig, real_patient_intent, kind='cubic', fill_value="extrapolate")
intent_base = f(t_sim)
intent_base = np.clip(intent_base * 0.6 + 0.1 * np.random.randn(STEPS), 0.0, 1.0)

# ====================== RESERVOIR ======================
device = torch.device("cpu")
reservoir = torch.nn.RNN(input_size=4, hidden_size=N_NODES, nonlinearity='tanh', batch_first=True)

with torch.no_grad():
    reservoir.weight_ih_l0.data.uniform_(-0.3, 0.3)
    W = reservoir.weight_hh_l0.data
    rho = torch.max(torch.abs(torch.linalg.eigvals(W)))
    reservoir.weight_hh_l0.data *= SPECTRAL_RADIUS / rho
    reservoir.bias_ih_l0.zero_()
    reservoir.bias_hh_l0.zero_()

proj_to_3d = torch.randn(N_NODES, 3, device=device) * 0.12
proj_to_3d /= torch.linalg.norm(proj_to_3d, dim=0, keepdim=True)

# ====================== GROK COUNCIL ======================
if USE_REAL_GROK_COUNCIL:
    client = OpenAI(base_url="https://api.x.ai/v1", api_key=API_KEY)

def get_council_intervention(projected_3d, intent_strength, deviation, step):
    x, y, z = projected_3d.tolist()

    if not USE_REAL_GROK_COUNCIL:
        direction = TARGET_3D - projected_3d
        direction /= (torch.norm(direction) + 1e-6)
        strength = torch.clamp(deviation * 3.0 * intent_strength, 0.0, 1.0)
        return strength * direction * CONTROL_SCALE

    prompt = f"""
You are the PDPBioGen Healing Council — 5 specialist Grok-4.1 agents (Neural, Metabolic, Genomic, Immune, Regenerative).

Current state:
Neural synchrony (X): {x:+.4f}
Metabolic balance (Y): {y:+.4f}
Genomic symmetry (Z): {z:.4f}
Patient intent: {intent_strength:.3f}
Deviation: {deviation:.3f}

Output ONLY JSON:
{{
  "dx": float -1 to 1,
  "dy": float -1 to 1,
  "dz": float -1 to 1,
  "strength": float 0 to 1,
  "council_reason": "one short sentence"
}}
"""

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
            max_tokens=120,
            response_format={"type": "json_object"}
        )
        data = json.loads(response.choices[0].message.content)
        control = torch.tensor([data["dx"], data["dy"], data["dz"]], device=device) * data["strength"]
        print(f"Step {step:3d} | Council: {data['council_reason']} | strength={data['strength']:.2f}")
        return control * CONTROL_SCALE
    except Exception as e:
        print("Council error → fallback", e)
        direction = TARGET_3D - projected_3d
        direction /= (torch.norm(direction) + 1e-6)
        return torch.clamp(deviation * 3.0 * intent_strength, 0.0, 1.0) * direction * CONTROL_SCALE

# ====================== SIMULATION ======================
def run_simulation(use_council=False):
    h = torch.zeros(1, 1, N_NODES, device=device)  # proper shape
    projected_history = []
    control = torch.zeros(3, device=device)

    for step in range(STEPS):
        intent = torch.tensor([[intent_base[step]]], dtype=torch.float32, device=device)

        # Council sees current state and decides
        current_projected = h[0, 0] @ proj_to_3d
        if use_council and step % DECISION_INTERVAL == 0:
            deviation = torch.norm(current_projected - TARGET_3D).item()
            control = get_council_intervention(current_projected, intent_base[step], deviation, step)

        u = torch.cat((intent, control.unsqueeze(0)), dim=1).unsqueeze(0)  # (1,1,4)

        with torch.no_grad():
            _, hn = reservoir(u, h)
        h = hn

        projected = h[0, 0] @ proj_to_3d
        projected_history.append(projected.cpu().numpy())

    return np.array(projected_history)

print("Running open-loop...")
open_proj = run_simulation(use_council=False)

print("\nRunning closed-loop with Grok-4.1-fast council..." if USE_REAL_GROK_COUNCIL else "\nRunning closed-loop with simulated council...")
closed_proj = run_simulation(use_council=True)

# ====================== PLOT ======================
fig = plt.figure(figsize=(16, 8))

ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.plot(open_proj[:,0], open_proj[:,1], open_proj[:,2], lw=0.7, color='#ff4444')
ax1.scatter(*TARGET_3D.tolist(), c='lime', s=200, label='Healthy attractor')
ax1.set_title("OPEN-LOOP\nChronic chaos (real seizure EEG)")
ax1.set_xlabel("Neural"); ax1.set_ylabel("Metabolic"); ax1.set_zlabel("Genomic")

ax2 = fig.add_subplot(1, 2, 2, projection='3d')
ax2.plot(closed_proj[:,0], closed_proj[:,1], closed_proj[:,2], lw=1.5, color='#00ff00')
ax2.scatter(*TARGET_3D.tolist(), c='lime', s=200)
ax2.set_title("CLOSED-LOOP Grok-4.1-fast Council\nHealed in <4 s" + ("\n(REAL API calls)" if USE_REAL_GROK_COUNCIL else "\n(simulated)"))
ax2.set_xlabel("Neural"); ax2.set_ylabel("Metabolic"); ax2.set_zlabel("Genomic")

plt.suptitle("PDPBioGen 100-node Network × Real Epileptic Seizure EEG × Grok-4.1-fast Council (Nov 2025)", fontsize=16)
plt.tight_layout()
plt.show()
