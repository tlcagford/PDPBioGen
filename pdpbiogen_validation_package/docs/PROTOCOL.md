# Protocol: NV vs Classical Phantom Test (simulation-ready)

This document contains the experimental protocol adapted for simulation and for easy translation to lab hardware.

Steps:
1. Generate phantom trials using `generate_phantom_trials()` in src/pdpbiogen/simulator.py
2. Record using NVSimulatedSensor and ClassicalSimulatedSensor (`src/pdpbiogen/sensors/`)
3. Compute matched-filter scores and SNR, evaluate ROC/AUC
4. Produce figures and report LOD and SNR improvements

Replace sensor.record_trials(...) with live-acquisition interfaces when hardware is available.
