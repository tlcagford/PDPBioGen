import pytest
import numpy as np
from scipy.linalg import expm, pinv

# =====================================================================
# 1. CORE PDP SYSTEM ENGINE & ESTIMATOR
# =====================================================================

class PDPStateEstimator:
    """
    Unified state estimator handling kinetic photon–dark-photon mixing,
    non-Hermitian decoherence, and Kalman filtering.
    """
    def __init__(self, omega_gamma: float, omega_a: float, epsilon: float, mass_a: float, gamma: float):
        self.w0 = omega_gamma
        self.wa = omega_a
        self.epsilon = epsilon
        self.ma = mass_a
        self.gamma = gamma
        self.delta = self.epsilon * (self.ma ** 2)
        
        # Effective Hamiltonian (Non-Hermitian for open quantum/dissipative systems)
        self.H_eff = np.array([
            [self.w0, self.delta],
            [self.delta, self.wa - 1j * self.gamma]
        ], dtype=complex)

    def propagate_state(self, psi0: np.ndarray, dt: float, steps: int) -> np.ndarray:
        """Propagates state vector [psi_gamma, psi_Aprime]^T through time."""
        U_dt = expm(-1j * self.H_eff * dt)
        states = np.zeros((steps, 2), dtype=complex)
        curr = psi0.astype(complex)
        for i in range(steps):
            curr = U_dt @ curr
            states[i] = curr
        return states

    def kalman_step(self, x_hat: np.ndarray, P: np.ndarray, z: np.ndarray, R: float, Q: np.ndarray, dt: float):
        """Extended Kalman Filter step with guaranteed Hermitian covariance."""
        F = expm(-1j * self.H_eff * dt)
        x_pred = F @ x_hat
        P_pred = F @ P @ F.conj().T + Q
        
        H_m = np.array([[1.0, 0.0]], dtype=complex)
        y = z - H_m @ x_pred
        S = H_m @ P_pred @ H_m.conj().T + R
        
        S_inv = 1.0 / S if np.abs(S) > 1e-12 else pinv(S)
        K = P_pred @ H_m.conj().T * S_inv
        
        x_updated = x_pred + K @ y
        I = np.eye(2, dtype=complex)
        P_updated = (I - K @ H_m) @ P_pred
        
        # Enforce Hermitian symmetry to prevent covariance drift
        P_updated = 0.5 * (P_updated + P_updated.conj().T)
        return x_updated, P_updated


# =====================================================================
# 2. PHOTON HEALING (REGENERATION) PIPELINE
# =====================================================================

class PhotonHealingPipeline:
    """
    Simulates Light Shining Through Walls (LSW) photon regeneration dynamics
    across Generation (L1), Barrier Isolation (L_barrier), and Regeneration (L2).
    """
    def __init__(self, omega: float, mass_a: float, epsilon: float):
        self.omega = omega
        self.ma = mass_a
        self.epsilon = epsilon
        self.delta_q = (self.ma ** 2) / (2.0 * self.omega) if self.omega > 0 else 0.0

    def conversion_probability(self, length: float) -> float:
        """Calculates vacuum photon-to-dark-photon conversion probability."""
        arg = (self.delta_q * length) / 2.0
        return 4.0 * (self.epsilon ** 2) * (np.sin(arg) ** 2)

    def execute_regeneration(self, L1: float, L_barrier: float, gamma_barrier: float, L2: float) -> dict:
        """Runs multi-stage regeneration pipeline."""
        P_gen = self.conversion_probability(L1)
        amp_aprime = np.sqrt(P_gen)
        
        # EM attenuation inside barrier; dark photon component passes freely
        em_leakage = np.exp(-gamma_barrier * L_barrier)
        
        P_regen = self.conversion_probability(L2)
        P_healed = (amp_aprime * np.sqrt(P_regen)) ** 2
        
        return {
            "P_gen": P_gen,
            "P_regen": P_regen,
            "em_leakage": em_leakage,
            "P_healed": P_healed
        }


# =====================================================================
# 3. BIOPHOTONIC CELLULAR DIAGNOSTIC & HEALING ENGINE
# =====================================================================

class BioPhotonicCellEngine:
    """
    Adapts PDP filtering to estimate cellular health from biophoton emission
    and models resonant energy transfer for membrane restoration.
    """
    def __init__(self, health_index: float = 1.0, base_freq: float = 600e12):
        self.health_index = np.clip(health_index, 0.0, 1.0)
        self.base_freq = base_freq
        self.V_membrane = -70.0 + 40.0 * (1.0 - self.health_index)  # -70mV (healthy) to -30mV (pathological)

    def generate_biophoton_stream(self, samples: int, noise_std: float) -> np.ndarray:
        """Simulates ultra-weak biophoton emission under background noise."""
        t = np.linspace(0, 1e-12, samples)
        signal = self.health_index * np.cos(2 * np.pi * self.base_freq * t)
        return signal + np.random.normal(0, noise_std, samples)

    def diagnose_health(self, raw_emissions: np.ndarray, noise_var: float) -> float:
        """Estimates cellular health index from raw biophotonic variance."""
        signal_power = np.var(raw_emissions) - noise_var
        estimated_health = np.clip(np.sqrt(max(0.0, signal_power * 2.0)), 0.0, 1.0)
        return float(estimated_health)

    def apply_resonant_therapy(self, power_dosage: float, duration_ns: float) -> float:
        """Applies resonant biophotonic therapy to restore cellular membrane potential."""
        recovery_factor = 0.08 * power_dosage * duration_ns
        self.health_index = min(1.0, self.health_index + recovery_factor)
        self.V_membrane = -70.0 + 40.0 * (1.0 - self.health_index)
        return self.health_index


# =====================================================================
# 4. UNIFIED INTEGRATED TEST SUITE
# =====================================================================

class TestIntegratedPDPFilterSuite:

    @pytest.fixture
    def system_harness(self):
        """Initializes test system instances across physics and biological modules."""
        estimator = PDPStateEstimator(omega_gamma=2.5, omega_a=2.5, epsilon=1e-5, mass_a=1e-3, gamma=0.01)
        pipeline = PhotonHealingPipeline(omega=2.5, mass_a=1e-3, epsilon=1e-5)
        cell = BioPhotonicCellEngine(health_index=0.25)  # Pathological cell state
        return estimator, pipeline, cell

    # --- Module 1: State Estimator & EKF Invariants ---
    def test_kalman_covariance_hermitian_preservation(self, system_harness):
        estimator, _, _ = system_harness
        x_hat = np.array([[1.0 + 0j], [0.0 + 0j]])
        P = np.array([[1.0, 0.3j], [-0.3j, 1.0]], dtype=complex)
        z = np.array([[0.95 + 0.02j]])
        
        _, P_updated = estimator.kalman_step(x_hat, P, z, R=0.01, Q=np.eye(2)*1e-5, dt=0.05)
        np.testing.assert_allclose(P_updated, P_updated.conj().T, atol=1e-12)

    def test_decoherence_monotonic_norm_decay(self, system_harness):
        estimator, _, _ = system_harness
        psi0 = np.array([0.0, 1.0], dtype=complex)
        states = estimator.propagate_state(psi0, dt=0.1, steps=40)
        norms = np.sum(np.abs(states)**2, axis=1)
        assert np.all(np.diff(norms) <= 1e-12)

    # --- Module 2: Photon Healing Invariants ---
    def test_epsilon_fourth_power_law(self):
        eps1, eps2 = 1e-6, 3e-6
        pipe1 = PhotonHealingPipeline(omega=2.5, mass_a=1e-4, epsilon=eps1)
        pipe2 = PhotonHealingPipeline(omega=2.5, mass_a=1e-4, epsilon=eps2)
        
        res1 = pipe1.execute_regeneration(L1=10.0, L_barrier=1.0, gamma_barrier=100.0, L2=10.0)
        res2 = pipe2.execute_regeneration(L1=10.0, L_barrier=1.0, gamma_barrier=100.0, L2=10.0)
        
        ratio = res2["P_healed"] / res1["P_healed"]
        np.testing.assert_allclose(ratio, (eps2 / eps1) ** 4, rtol=1e-5)

    def test_barrier_isolation_purity(self, system_harness):
        _, pipeline, _ = system_harness
        res = pipeline.execute_regeneration(L1=10.0, L_barrier=5.0, gamma_barrier=50.0, L2=10.0)
        assert res["em_leakage"] < 1e-100
        assert res["P_healed"] > 0.0

    # --- Module 3: Cellular Diagnostic & Healing Invariants ---
    def test_cellular_diagnostic_accuracy(self, system_harness):
        np.random.seed(42)
        _, _, cell = system_harness
        noise_var = 0.04
        raw_emissions = cell.generate_biophoton_stream(samples=1000, noise_std=np.sqrt(noise_var))
        diagnosed_health = cell.diagnose_health(raw_emissions, noise_var=noise_var)
        assert np.isclose(diagnosed_health, cell.health_index, atol=0.08)

    def test_resonant_therapeutic_membrane_recovery(self, system_harness):
        _, _, cell = system_harness
        assert cell.V_membrane > -45.0  # Confirm initial sick membrane potential
        
        cell.apply_resonant_therapy(power_dosage=2.5, duration_ns=5.0)
        
        assert cell.health_index >= 0.95
        assert np.isclose(cell.V_membrane, -70.0, atol=2.0)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
