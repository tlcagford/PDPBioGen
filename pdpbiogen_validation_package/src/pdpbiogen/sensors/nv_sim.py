import numpy as np

class NVSimulatedSensor:
    """
    Simulated NV-diamond magnetometer interface.
    Produces a signal with defined sensitivity and bandwidth characteristics.
    """
    def __init__(self, fs=5000, noise_pT_per_sqrtHz=10.0):
        self.fs = fs
        self.noise_pT = noise_pT_per_sqrtHz

    def record_trials(self, trials):
        rec = []
        for t, sig in trials:
            noise = np.random.normal(scale=self.noise_pT, size=sig.shape)
            rec.append(sig + noise)
        return np.array(rec)
