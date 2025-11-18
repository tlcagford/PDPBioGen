from pdpbiogen import PDPBioGenIntegrator

# Initialize complete system
integrator = PDPBioGenIntegrator()

# Run brain-guided healing
results = integrator.run_complete_healing_pipeline(
    brain_signals=eeg_data,
    biological_data=multi_omics_data, 
    target_tissue="cardiac_muscle",
    simulation_steps=100
)