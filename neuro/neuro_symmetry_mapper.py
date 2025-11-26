
import numpy as np
import mne

class NeuroSymmetryMapper:
    """
    Computes hemispheric symmetry, coherence, entropy, and resonance indices
    and outputs a normalized Neuro-Symmetry Vector for downstream healing simulation.
    """

    def __init__(self):
        pass

    def load_eeg(self, eeg_path):
        return mne.io.read_raw_edf(eeg_path, preload=True)

    def preprocess(self, raw):
        raw = raw.copy().filter(1, 40)
        raw = raw.set_eeg_reference("average")
        return raw

    def hemispheric_symmetry(self, data, ch_names):
        left = [i for i, ch in enumerate(ch_names) if ch.startswith(("F3","C3","P3","O1","T3"))]
        right = [i for i, ch in enumerate(ch_names) if ch.startswith(("F4","C4","P4","O2","T4"))]

        L = np.mean(np.abs(data[left]))
        R = np.mean(np.abs(data[right]))

        return 1.0 - (abs(L - R) / (L + R + 1e-9))

    def coherence_index(self, raw):
        freqs = (8, 13)
        coh = mne.connectivity.spectral_connectivity(
            [raw.get_data()],
            method='coh',
            sfreq=raw.info['sfreq'],
            fmin=freqs[0],
            fmax=freqs[1],
            verbose=False
        )
        return np.mean(coh[0])

    def neural_entropy(self, data):
        hist, _ = np.histogram(data.flatten(), bins=100, density=True)
        hist += 1e-12
        return -np.sum(hist * np.log2(hist))

    def resonance_bands(self, raw):
        psd, freqs = raw.compute_psd().get_data(return_freqs=True)
        bands = {
            "delta": (0.5, 4),
            "theta": (4, 8),
            "alpha": (8, 12),
            "beta": (12, 30)
        }
        results = {b: np.mean(psd[:, (freqs >= lo) & (freqs <= hi)]) for b,(lo,hi) in bands.items()}
        return results

    def compute(self, eeg_path):
        raw = self.preprocess(self.load_eeg(eeg_path))
        data = raw.get_data()
        ch = raw.ch_names

        features = {
            "symmetry": self.hemispheric_symmetry(data, ch),
            "coherence": self.coherence_index(raw),
            "entropy": self.neural_entropy(data),
            "bands": self.resonance_bands(raw)
        }

        return features
