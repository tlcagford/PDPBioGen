"""
Demo runner for the healing_sim module.
Usage:
  python dpbiogen/quantum/demo_full_body.py --eeg sample.edf --sbml sample_model.xml --out demo_results
"""

import argparse
from dpbiogen.quantum.healing_sim import run_healing_sim

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--eeg", required=True, help="Path to EDF EEG sample")
    parser.add_argument("--sbml", required=True, help="Path to SBML metabolic model")
    parser.add_argument("--out", default="results/healing_demo", help="Output directory")
    args = parser.parse_args()

    manifest = run_healing_sim(args.eeg, args.sbml, outdir=args.out)
    print("Manifest written:", manifest)

if __name__ == "__main__":
    main()
