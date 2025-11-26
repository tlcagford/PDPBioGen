import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt

# --------------------------
# Synthetic Signal Generators
# --------------------------

def gen_eeg(t, event=False):
    alpha = np.sin(2*np.pi*10*t)
    beta  = 0.5*np.sin(2*np.pi*20*t)
    noise = 0.3*np.random.randn(len(t))
    spike = np.zeros_like(t)
    if event:
        spike[len(t)//2:len(t)//2 + 10] = 5.0
    return alpha + beta + noise + spike

def gen_ecg(t, hr=70):
    # simple ECG-like wave via sawtooth + noise
    freq = hr / 60
    signal = 0.6 * np.sin(2*np.pi*freq*t) + 0.1*np.random.randn(len(t))
    return signal

def gen_metabolic(prev, stress):
    # slow metabolic dynamics
    return prev + 0.01*(stress - prev) + 0.005*np.random.randn()

# --------------------------
# Preprocessing
# --------------------------

def bandpass(data, low, high, fs):
    b, a = butter(4, [low/(fs/2), high/(fs/2)], btype='band')
    return filtfilt(b, a, data)

def eeg_features(data, fs):
    # power in alpha vs beta
    alpha = np.mean(np.abs(np.fft.rfft(data)[10:14]))
    beta  = np.mean(np.abs(np.fft.rfft(data)[20:25]))
    ratio = alpha / (beta + 1e-6)
    entropy = -np.sum((data**2)*np.log(data**2 + 1e-6))
    return np.array([ratio, entropy])

def ecg_features(signal, fs):
    hr = 60 + 5*np.random.randn()   # simulated
    hrv = np.abs(np.random.randn()) # simulated variability
    return np.array([hr, hrv])

def metabolic_features(glucose):
    return np.array([glucose, np.abs(glucose-1.0)])

# --------------------------
# Closed-loop Controller
# --------------------------

def controller(fused):
    # fused = [eeg_ratio, eeg_entropy, hr, hrv, glucose, gl_dev]
    stress = (
        0.4 * (1/fused[0]) + 
        0.3 * fused[2] +
        0.3 * fused[5]
    )
    return np.clip(stress, 0, 3)

# --------------------------
# Run Closed-Loop Simulation
# --------------------------

fs = 250
t = np.linspace(0, 1, fs)
glucose = 1.0
states = []

for step in range(200):
    eeg = gen
