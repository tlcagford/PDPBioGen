
For real heart data: Process ECG samples (e.g., via Python libs like biosppy or heartpy) to compute deviation metrics, save to CSV as agent_name,initial_state pairs, then pass as arg to full_body_demo.py.

No additional requirements beyond the main PDPBioGen project (pure Python + csv stdlib; optionally numpy/biosppy for real data processing upstream).

Drop the quantum folder into the dpbiogen/ package and import as dpbiogen.quantum.

Ready for integration with the Grok-4.1-fast Healing Council or real-time BCI loop.

