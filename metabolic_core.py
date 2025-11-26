import numpy as np

def update_metabolic(prev_glucose, stress):
    return prev_glucose + 0.01 * (stress - prev_glucose) + 0.005*np.random.randn()

def extract_metabolic_features(glucose):
    return np.array([glucose, abs(glucose - 1.0)])
