def emotional_state(eeg_features):
    # Simple mapping for synthetic emotional index
    ratio, entropy = eeg_features
    emotion = 0.5*(1/ratio) + 0.5*(entropy/10)
    return np.clip(emotion, 0, 1)
