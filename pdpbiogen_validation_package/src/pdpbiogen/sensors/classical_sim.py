import numpy as np

class ClassicalSimulatedSensor:
    """
    Simulated classical magnetometer (fluxgate-like) interface.
    Less sensitive than NV by default.
    """
    def __init__(self, fs=5000, noise_pT_per_sqrtHz=50.0):
        self.fs = fs
        self.noise_pT = noise_pT_per_sqrtHz

    def record_trials(self, trials):
        rec = []
        for t, sig in trials:
            noise = np.random.normal(scale=self.noise_pT, size=sig.shape)
            rec.append(sig + noise)
        return np.array(rec)
