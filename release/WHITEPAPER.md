# PDPBioGen v0.1 — Draft Whitepaper

## Abstract
PDPBioGen is a prototype simulation framework designed to explore closed-loop interactions between neural signals (BCI) and simplified biological process models. The goal of this framework is to provide a reproducible sandbox to design agents that can interpret neural features and suggest or apply control actions to a biological model in a transparent, testable environment. This early-stage work focuses on simulation and reproducibility; no clinical claims are made.

## Introduction & Motivation
Advances in brain–computer interfaces (BCIs), adaptive neurostimulation and systems biology motivate tools that can integrate neural signals and biological process models. Such tools can accelerate research into closed-loop neuromodulation strategies, personalized therapy simulations, and algorithmic safety testing. PDPBioGen aims to provide modular building blocks—signal ingestion, preprocessing, biological modeling, agent/controller, and experiment orchestration—so researchers can prototype and evaluate closed-loop ideas safely in silico.

## Related Work
Adaptive deep brain stimulation (DBS) systems and industrial efforts in real-time neural processing demonstrate the feasibility of low-latency closed-loop control. Representative systems include adaptive DBS clinical systems and frameworks leveraging GPUs for neural decoding. PDPBioGen does not attempt to replicate or compete with clinical-grade systems; instead it offers an open sandbox for research experiments and method development.

## Methods
### BCI simulation
The simulator produces synthetic time-series composed of multiple sinusoidal components (delta, alpha, gamma bands) corrupted by Gaussian noise. This provides controllable, repeatable inputs to the pipeline and allows stress-testing agents under variable SNR conditions.

### Biological model
We adopt a simple two-state ordinary differential equation (ODE) model as a toy metabolic or biomarker proxy. The model has parameters controlling decay and coupling between state variables, and accepts a scalar control input `u` representing an intervention.

### Agent & Control
The v0.1 agent is intentionally simple (hill-climb rule): it adjusts its control `u` based on feature thresholds from the BCI input. This demonstrates closed-loop logic while remaining interpretable. Future agents may leverage model-based control, reinforcement learning, or multi-agent coordination.

### Experimental Protocol & Metrics
Experiments are run as episodes: for each time-window the pipeline extracts features, the agent selects an action, the biological model evolves under the action, and results are logged. Evaluation metrics include convergence of the biomarker, action stability, robustness under noise, and false positive rates for event detection.

## Results (Simulated)
We provide example experiments in `notebooks/demo_simulation_polished.ipynb`. Sample outputs include time-series of extracted features, biomarker trajectory, and controller actions. These illustrate the basic closed-loop dynamics and serve as baseline references.

## Discussion & Limitations
PDPBioGen is a research sandbox. It intentionally uses simplified models to lower barriers to experimentation. It is **not** a clinical tool. Significant work is required to translate these methods to real data, including signal alignment, sensor calibration, ethical oversight, and rigorous validation with human subjects.

## Ethics & Safety
All use of real data requires informed consent and IRB approval. Interventions on live subjects must be human-in-the-loop and follow medical regulatory guidance. We include an `ETHICS.md` describing governance recommendations and fail-safe defaults.

## Roadmap
- v0.2: Modular adapters for EEG (`mne`) and live streams (`LSL`), unit tests, containerized reproducibility.
- v0.3: Expand agent library (RL, model predictive control), add example datasets, invite collaborators for validation studies.
- v1.0: Collaborate with clinical partners for translational research under IRB oversight (long-term).

## Acknowledgements & Attribution
This prototype leverages structural patterns and reproducibility practices from prior projects (e.g., Astronomical Image Refiner). See repository history for details.
