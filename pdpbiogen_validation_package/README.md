# PDPBioGen Validation Package — NV vs Classical Phantom Test

This package contains a reproducible, drop-in validation experiment demonstrating
a bench comparison between a quantum NV-diamond magnetometer (simulated interface)
and a classical magnetometer using a controlled phantom coil.

**Contents**
- `src/pdpbiogen/` : core code (simulator, sensors, analysis)
- `notebooks/validation_experiment.ipynb` : runnable notebook executing the protocol (simulated data)
- `docs/PROTOCOL.md` : experiment protocol & checklist
- `requirements.txt` : Python deps
- `.github/workflows/ci.yml` : CI that runs tests and the notebook
- `release/WHITEPAPER.md` : short methods summary for publication

This package is simulation-first: if you have real NV hardware and classical sensors,
replace the simulated sensor interfaces with your acquisition code (see sensors/README).
