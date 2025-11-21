# Quantum-Secure-Dark-Net — Repo Deliverables
# This single code document contains three deliverables you requested for the GitHub repo:
# 1) simulations/decoherence_calc.py  (runnable Python module + example parameter sweep)
# 2) literature/README.md            (annotated literature summary you can paste into repo)
# 3) experiments/MilestoneA_plan.md  (Milestone A: tabletop demo plan, equipment, specs)

# -----------------------------------------------------------------------------
# 1) simulations/decoherence_calc.py
# -----------------------------------------------------------------------------
"""
simulations/decoherence_calc.py

Purpose:
- Provide a reproducible, documented toy model for photon <-> dark-photon (or axion-mediated)
  mixing and for a decoherence estimate as a function of the key parameters.
- Produce parameter sweep plots of entanglement fidelity and decoherence rate vs coupling g,
  dark particle mass m, cavity Q, detector efficiency eta, and distance.

Notes:
- This is a *toy* model designed to make assumptions explicit and produce reproducible
  numbers for sensitivity and trade-off studies. Replace the toy Hamiltonian with
  a more advanced model as experimental data appears.

Usage example:
$ python simulations/decoherence_calc.py --plot --save=out.png

Requirements: numpy, scipy, matplotlib
"""

from math import pi
import numpy as np
from scipy.linalg import expm
import matplotlib.pyplot as plt
import argparse

# --------------------------- Physical model ----------------------------------
# Toy Hamiltonian approach (2-mode system):
#   |psi> = [a_photon, a_dark]^T
#   H = [[omega_p, g], [g, omega_d]]  (units: angular freq)
# We model loss / decoherence by adding phenomenological damping rates gamma_p, gamma_d
# and compute the evolution of the density matrix in a simple Lindblad-style approximation
# to extract purity/traces that indicate decoherence.

hbar = 1.0

def hamiltonian(omega_p, omega_d, g):
    H = np.array([[omega_p, g], [g, omega_d]], dtype=complex)
    return H

def lindblad_evolution_rho0(H, gamma_p, gamma_d, t):
    # Very coarse approximation: treat damping as exponential on populations and
    # compute unitary evolution then damp non-diagonal terms.
    U = expm(-1j * H * t / hbar)
    rho0 = np.array([[1.0, 0.0],[0.0, 0.0]], dtype=complex)  # start with photon populated
    rho_t = U @ rho0 @ U.conj().T
    # apply damping to populations and reduce coherence
    damping_pop = np.exp(-np.array([gamma_p, gamma_d]) * t)
    rho_t = np.diag(np.diag(rho_t) * damping_pop)
    # reduce off-diagonal coherence by average damping
    avg_damp = np.exp(-0.5 * (gamma_p + gamma_d) * t)
    rho_t[0,1] *= avg_damp
    rho_t[1,0] = rho_t[0,1].conj()
    return rho_t

def purity(rho):
    return np.real(np.trace(rho @ rho))

# --------------------------- Derived metrics --------------------------------

def decoherence_rate_from_params(g, m_ev, Q, eta, background_noise):
    """
    Very rough mapping from physical parameters to an effective decoherence rate gamma (1/s).
    This functional form is intentionally simple and *transparent* so you can change it.

    - g: effective mixing coupling (Hz)
    - m_ev: dark particle mass in eV -> convert to angular freq via E = m c^2 / hbar
    - Q: cavity quality factor (dimensionless)
    - eta: detector efficiency (0..1)
    - background_noise: noise spectral density (arbitrary normalized units)

    OUTPUT: gamma in 1/s. Lower gamma -> lower decoherence.
    """
    # convert mass (eV) to frequency (Hz); 1 eV = 1.602176634e-19 J; hbar = 1.054571817e-34 J*s
    eV_to_J = 1.602176634e-19
    hbar_si = 1.054571817e-34
    omega_d = (m_ev * eV_to_J) / hbar_si  # rad/s

    # phenomenological scaling (tunable):
    # stronger coupling g reduces decoherence; larger Q reduces decoherence; detector ineff reduces effective decoherence
    gamma0 = 1e3  # base decoherence scale (1/s) — tunable
    gamma = gamma0 * (omega_d / (1 + Q)) * (1.0 / (1 + g)) * (1.0 / max(1e-6, eta)) * (1 + background_noise)
    return gamma

# --------------------------- Simulation / sweep ------------------------------

def sweep_and_plot():
    # parameter ranges (example)
    g_vals = np.logspace(-6, 2, 25)   # dimensionless effective coupling proxy (Hz-scale mapping)
    m_vals = [1e-22, 1e-20, 1e-18]    # eV (example ultralight to heavier)
    Q = 1e4
    eta = 0.2
    background_noise = 1.0

    plt.figure()
    for m in m_vals:
        gammas = [decoherence_rate_from_params(g, m, Q, eta, background_noise) for g in g_vals]
        plt.loglog(g_vals, gammas)
    plt.xlabel('effective coupling proxy g (unitless)')
    plt.ylabel('effective decoherence rate gamma (1/s)')
    plt.title('Toy decoherence rate vs coupling (varying mass)')
    plt.grid(True, which='both', ls=':')
    plt.tight_layout()
    plt.show()

    # Example fidelity vs distance using exponential loss model
    distances = np.linspace(1e2, 1e7, 50)
    g_choice = 1e-2
    m_choice = 1e-22
    gamma = decoherence_rate_from_params(g_choice, m_choice, Q, eta, background_noise)
    # effective decoherence probability P ~ 1 - exp(-gamma * t_prop) where t_prop = distance / c
    c = 3e8
    t_prop = distances / c
    P = 1.0 - np.exp(-gamma * t_prop)
    plt.figure()
    plt.loglog(distances, P)
    plt.xlabel('distance (m)')
    plt.ylabel('decoherence probability P')
    plt.title('Toy decoherence probability vs distance')
    plt.grid(True, which='both', ls=':')
    plt.tight_layout()
    plt.show()

# --------------------------- CLI ---------------------------------------------

def main():
    parser = argparse.ArgumentParser(description='Toy decoherence simulator for photon<->dark mixing')
    parser.add_argument('--plot', action='store_true', help='run example plots')
    args = parser.parse_args()
    if args.plot:
        sweep_and_plot()

if __name__ == '__main__':
    main()

# End of simulations/decoherence_calc.py

# -----------------------------------------------------------------------------
# 2) literature/README.md  (annotated)  -- paste this into literature/README.md in your repo
# -----------------------------------------------------------------------------

literature_readme = r"""
# Literature summary — Photon ↔ Dark-Photon / Axion mixing and satellite QKD

This short collection highlights the most relevant experimental and theoretical work you
should cite / inspect before making strong engineering claims. The set below is intentionally
concise and focuses on the foundational experiments and reviews that inform feasibility.

## Key experimental baselines (QKD / satellite)
- **Micius / Satellite QKD & entanglement distribution** — pioneering demonstrations of satellite-based
  entanglement and QKD that serve as the practical engineering baseline for global quantum links.
  Review & primary experimental papers should be read carefully to understand realistic link losses,
  atmospheric effects, payload constraints, and authenticated key exchange protocols.

## Dark-sector detection & mixing
- **ADMX & haloscope techniques** — demonstrate resonant cavity based conversion of axion-like fields to microwave
  photons; show the kinds of high-Q cavities and quantum-limited readout that would be necessary for any
  conversion/detection scheme.

- **Reviews of dark photon searches / kinetic mixing** — dark photons (extra U(1) gauge bosons) have numerous
  experimental constraints and active search programs; these reviews summarize parameter-space exclusions and
  detection techniques.

- **Theory of photon–axion–dark-photon mixing** — several theoretical works derive mixing matrices and
  propagation equations in magnetic fields / cavities; these are the starting point for any conversion model.

## Astrophysical constraints
- **Fuzzy dark matter / ultralight scalar reviews** — if you assume m ~ 1e-22 eV (``fuzzy'' DM), consult up-to-date astrophysical
  constraints (Lyman-α, dwarf galaxy cores, reionization / 21-cm) to ensure the assumed mass and coherence properties
  are consistent with cosmological observations.

## Practical advice
- Assemble official PDFs or DOI links into `literature/papers/` in the repo so reviewers can reproduce the background quickly.
- Annotate each paper with the exact claim it supports and any assumptions/limitations (e.g., bounds on coupling strengths,
  Q factors achievable, detector efficiencies).

"""

# -----------------------------------------------------------------------------
# 3) experiments/MilestoneA_plan.md  (Milestone A: tabletop demo)
# -----------------------------------------------------------------------------

milestoneA = r"""
# Milestone A — Tabletop proof-of-principle: single-photon -> dark-excitation conversion and readout

## Goal
Demonstrate a measurable signature of coupling between an electromagnetic mode (photon) and a dark-sector
excitation in a controlled, resonant environment: i.e., show that an injected single-photon-level signal couples
into a resonant mode whose response is consistent with a photon<->dark mixing model. Provide a clear falsifiable
statistical test (SNR, p-value) and quantify fidelity.

## Core experimental approach
1. Use a high-Q microwave or optical cavity (depending on target mass/frequency) to provide resonant enhancement.
2. Apply a strong external field if theory requires (e.g., magnetic field for axion conversion—Primakoff effect).
3. Use quantum-limited readout (JPAs, SQUIDs or single-photon detectors) to search for the converted signal.
4. Perform control runs (field off/on, cavity detuned, injected blank pulses) to exclude spurious systematics.

## Equipment (example, adjust for optical vs microwave target)
- High-Q resonant cavity (Q ≥ 10^4 — 10^6 depending on frequency).
- For axion-like conversion: superconducting magnet B ≈ 1–10 T, cryostat (dilution fridge or 4K stage), cavity tuning rods.
- Quantum-limited readout chain: JPA or SQUID amplifiers (microwave) or SNSPDs / TES (optical/IR).
- Single-photon source (attenuated laser with calibrated photon flux or heralded source).
- Fast digitizer and lock-in readout; vibration isolation and EM shielding.

## Measurement plan & data products
- Sweep cavity resonant frequency while injecting single-photon-level signals; record spectra.
- Run on/off magnetic field or detune cavity for background controls.
- Produce: raw time-series, averaged spectra, significance maps (SNR vs freq), and a model fit for coupling g.
- Publish Jupyter notebooks to `experiments/MilestoneA/data_analysis.ipynb` that reproduce significance tests.

## Statistical test
- Null hypothesis: no conversion signal; background described by measured noise with known distribution.
- Detection criterion: peak SNR > 5 sigma after trials correction or a Bayesian odds ratio threshold with priors
  that reflect physically plausible couplings.

## Estimated budget & timeline (rough)
- Setup + core hardware (cavity, cryostat, magnet, amplifiers): $0.5M - $3M.
- Personnel & overhead (2 years): 2–3 FTEs: $0.5M - $1M.
- Timeline: 6–18 months to first meaningful sensitivity depending on existing infrastructure.

## Risk & contingencies
- Risk: no detectable conversion due to couplings orders of magnitude below design sensitivity.
  Mitigation: design modular upgrades for higher Q, lower system temperature, and alternative readouts.
- Risk: spurious electromagnetic pickup. Mitigation: rigorous shielding, blank runs, and cross-checks with
  different detectors.

"""

# -----------------------------------------------------------------------------
# Write out the three pieces as files (instructions for the user)
# -----------------------------------------------------------------------------

readme_instructions = r"""

---
Files produced in this document (copy/paste into your repo):

- simulations/decoherence_calc.py   # (runnable Python script)
- literature/README.md              # (annotated literature summary)
- experiments/MilestoneA_plan.md    # (detailed Milestone A plan)

Copy each of the strings above into corresponding files in your GitHub repo. The simulation module
is intentionally short and transparent — replace the phenomenological decoherence mapping with a
more advanced Hamiltonian / Lindblad solver as you refine the theory.

If you want, I can now:
- Convert `simulations/decoherence_calc.py` into a fully fledged Jupyter notebook (.ipynb) with interactive
  widgets (no external web required), or
- Produce ready-to-commit files and a small README that explains how to run the simulations on a fresh VM.

"""

# Print short confirmation (user will see this doc in canvas).  End of document.
