from dpbiogen.neuro.neuro_symmetry_mapper import NeuroSymmetryMapper

nsm = NeuroSymmetryMapper()
brain_state = nsm.compute(eeg_path)

gene_delta = gene_mapper.map(brain_state)
