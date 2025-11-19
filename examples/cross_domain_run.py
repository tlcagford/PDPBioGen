from pdpbiogen.core.integrator import Integrator
from pdpbiogen.core.utils import load_json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "sample"

def main():
    inputs = {
        "neural": load_json(DATA_DIR / "neural_sample.json"),
        "genomic": load_json(DATA_DIR / "genome_sample.json"),
        "metabolic": load_json(DATA_DIR / "metabolism_sample.json"),
    }
    integrator = Integrator()
    out = integrator.run(inputs)
    print("Pipeline result:")
    print(out)

if __name__ == "__main__":
    main()
