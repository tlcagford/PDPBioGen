import numpy as np
import torch
from fusion_network import FusionLSTM
from eeg_adapter import extract_eeg_features
from ecg_adapter import extract_ecg_features
from metabolic_core import update_metabolic, extract_metabolic_features
from controller import controller

def run_sim(model, eeg_source, ecg_source, steps=300):
    fs = 250
    glucose = 1.0
    all_states = []

    for step in range(steps):
        eeg_f = extract_eeg_features(eeg_source)
        ecg_f = extract_ecg_features(ecg_source)
        met_f = extract_metabolic_features(glucose)

        fused = np.concatenate([eeg_f, ecg_f, met_f])
        glucose = update_metabolic(glucose, stress=0.5)

        model_input = torch.tensor(fused, dtype=torch.float32)\
                           .unsqueeze(0).unsqueeze(0)
        nn_output = model(model_input).item()

        ctrl = controller(fused)
        all_states.append([*fused, nn_output, ctrl])

    return np.array(all_states)
