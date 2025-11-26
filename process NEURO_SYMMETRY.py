process NEURO_SYMMETRY {
  input:
    path eeg
  output:
    path "symmetry.json"

  script:
    """
    python -m dpbiogen.neuro.run_symmetry \\
      --eeg $eeg \\
      --out symmetry.json
    """
}
